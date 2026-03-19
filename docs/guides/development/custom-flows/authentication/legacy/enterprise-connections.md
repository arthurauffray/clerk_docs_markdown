# Build a custom flow for authenticating with enterprise connections


> Learn how to use the Clerk API to build a custom sign-up and sign-in flow that supports enterprise connections.

> [!WARNING]
> This guide is for users who want to build a custom flow. To use a _prebuilt_ UI, use the [Account Portal pages](/guides/account-portal/overview) or [prebuilt components](/reference/components/overview).


> [!IMPORTANT]
> This guide uses the Core 2 `useSignIn()` and `useSignUp()` hooks, which are available in Core 3 SDKs by adding the `/legacy` subpath to the import path. If you're using a Core 2 SDK, remove the `/legacy` subpath.


## Before you start

You must configure your application instance through the Clerk Dashboard for the enterprise connection(s) that you want to use. Visit [the appropriate guide for your platform](/guides/configure/auth-strategies/enterprise-connections/overview) to learn how to configure your instance.

## Create the sign-up and sign-in flow


  
    > [!TIP]
> Examples for this SDK aren't available yet. For now, try adapting the  available example to fit your SDK.

  

  The following example **will both sign up _and_ sign in users**, eliminating the need for a separate sign-up page. However, if you want to have separate sign-up and sign-in pages, the sign-up and sign-in flows are equivalent, meaning that all you have to do is swap out the `SignIn` object for the `SignUp` object using the [`useSignUp()`](/reference/hooks/use-sign-up) hook.

  The following example:

  1. Accesses the [`SignIn`](/reference/javascript/sign-in) object using the [`useSignIn()`](/reference/hooks/use-sign-in) hook.
  1. Starts the authentication process by calling [`SignIn.sso(params)`](/reference/javascript/sign-in-future#sso). This method requires the following params:
     - `redirectUrl`: The URL that the browser will be redirected to once the user authenticates with the identity provider if no additional requirements are needed, and a session has been created.
     - `redirectCallbackUrl`: The URL that the browser will be redirected to once the user authenticates with the identity provider if additional requirements are needed.
  1. Creates a route at the URL that the `redirectCallbackUrl` param points to. The following example re-uses the `/sign-in` route, which should be written to handle when a sign-in attempt is in a non-complete status such as `needs_second_factor`.

  
**Sign in page:**

```tsx
// Filename: app/sign-in/[[...sign-in]]/page.tsx

    'use client'

    import * as React from 'react'
    import { useSignIn } from '@clerk/nextjs/legacy'

    export default function Page() {
      const { signIn, isLoaded } = useSignIn()

      const signInWithEnterpriseSSO = (e: React.FormEvent) => {
        e.preventDefault()

        if (!isLoaded) return null

        const email = (e.target as HTMLFormElement).email.value

        signIn
          .authenticateWithRedirect({
            identifier: email,
            strategy: 'enterprise_sso',
            redirectUrl: '/sign-in/sso-callback',
            redirectUrlComplete: '/',
          })
          .then((res) => {
            console.log(res)
          })
          .catch((err: any) => {
            // See https://clerk.com/docs/guides/development/custom-flows/error-handling
            // for more info on error handling
            console.log(err.errors)
            console.error(err, null, 2)
          })
      }

      return (
        <form onSubmit={(e) => signInWithEnterpriseSSO(e)}>
          <input id="email" type="email" name="email" placeholder="Enter email address" />
          <button>Sign in with Enterprise SSO</button>
        </form>
      )
    }
    ```


**SSO callback page:**

```jsx
// Filename: app/sign-in/sso-callback/page.tsx

    import { AuthenticateWithRedirectCallback } from '@clerk/nextjs'

    export default function Page() {
      // Handle the redirect flow by calling the Clerk.handleRedirectCallback() method
      // or rendering the prebuilt component.
      // This is the final step in the custom Enterprise SSO flow.
      return }
    ```


  To **handle both sign-up and sign-in** without a separate sign-up page, the following example:

  1. Uses the [`useSSO()`](/reference/expo/native-hooks/use-sso) hook to access the `startSSOFlow()` method.
  1. Calls the `startSSOFlow()` method with the `strategy` param set to `enterprise_sso` and the `identifier` param set to the user's email address that they provided. The optional `redirect_url` param is also set in order to redirect the user once they finish the authentication flow.
     - If authentication is successful, the `setActive()` method is called to set the active session with the new `createdSessionId`. You may need to check for session tasks that are required for the user to complete after signing up.
     - If authentication is not successful, you can handle the missing requirements, such as MFA, using the [`signIn`](/reference/javascript/sign-in) or [`signUp`](/reference/javascript/sign-up) object returned from `startSSOFlow()`, depending on if the user is signing in or signing up. These objects include properties, like `status`, that can be used to determine the next steps. See the respective linked references for more information.

  ```tsx
// Filename: app/(auth)/sign-in.tsx

  import { ThemedText } from '@/components/themed-text'
  import { ThemedView } from '@/components/themed-view'
  import { useSSO } from '@clerk/expo'
  import * as AuthSession from 'expo-auth-session'
  import { useRouter } from 'expo-router'
  import * as WebBrowser from 'expo-web-browser'
  import React, { useEffect, useState } from 'react'
  import { Platform, Pressable, StyleSheet, TextInput } from 'react-native'

  export const useWarmUpBrowser = () => {
    useEffect(() => {
      // Preloads the browser for Android devices to reduce authentication load time
      // See: https://docs.expo.dev/guides/authentication/#improving-user-experience
      if (Platform.OS !== 'android') return
      void WebBrowser.warmUpAsync()
      return () => {
        // Cleanup: closes browser when component unmounts
        void WebBrowser.coolDownAsync()
      }
    }, [])
  }

  // Handle any pending authentication sessions
  WebBrowser.maybeCompleteAuthSession()

  export default function Page() {
    useWarmUpBrowser()

    const router = useRouter()
    const [email, setEmail] = useState('')

    // Use the `useSSO()` hook to access the `startSSOFlow()` method
    const { startSSOFlow } = useSSO()

    const onPress = async () => {
      try {
        // Start the authentication process by calling `startSSOFlow()`
        const { createdSessionId, setActive, signIn, signUp } = await startSSOFlow({
          strategy: 'enterprise_sso',
          identifier: email,
          // For web, defaults to current path
          // For native, you must pass a scheme, like AuthSession.makeRedirectUri({ scheme, path })
          // For more info, see https://docs.expo.dev/versions/latest/sdk/auth-session/#authsessionmakeredirecturioptions
          redirectUrl: AuthSession.makeRedirectUri(),
        })

        // If sign in was successful, set the active session
        if (createdSessionId) {
          setActive!({
            session: createdSessionId,
            navigate: async ({ session, decorateUrl }) => {
              if (session?.currentTask) {
                // Handle pending session tasks
                // See https://clerk.com/docs/guides/development/custom-flows/authentication/session-tasks
                console.log(session?.currentTask)
                return
              }

              const url = decorateUrl('/')
              if (url.startsWith('http')) {
                window.location.href = url
              } else {
                router.push(url)
              }
            },
          })
        } else {
          // If there is no `createdSessionId`,
          // there are missing requirements, such as MFA
          // Use the `signIn` or `signUp` returned from `startSSOFlow`
          // to handle next steps
        }
      } catch (err) {
        // See https://clerk.com/docs/guides/development/custom-flows/error-handling
        // for more info on error handling
        console.error(JSON.stringify(err, null, 2))
      }
    }

    return (
      
        
          Sign in with SAML
        
        Email address
         [
            styles.button,
            !email && styles.buttonDisabled,
            pressed && styles.buttonPressed,
          ]}
          onPress={onPress}
          disabled={!email}
        >
          Sign in with SAML
        
      
    )
  }

  const styles = StyleSheet.create({
    container: {
      flex: 1,
      padding: 20,
      gap: 12,
    },
    title: {
      marginBottom: 8,
    },
    label: {
      fontWeight: '600',
      fontSize: 14,
    },
    input: {
      borderWidth: 1,
      borderColor: '#ccc',
      borderRadius: 8,
      padding: 12,
      fontSize: 16,
      backgroundColor: '#fff',
    },
    button: {
      backgroundColor: '#0a7ea4',
      paddingVertical: 12,
      paddingHorizontal: 24,
      borderRadius: 8,
      alignItems: 'center',
      marginTop: 8,
    },
    buttonPressed: {
      opacity: 0.7,
    },
    buttonDisabled: {
      opacity: 0.5,
    },
    buttonText: {
      color: '#fff',
      fontWeight: '600',
    },
  })
  ```
