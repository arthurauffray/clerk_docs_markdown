# Expo Quickstart


> Add authentication and user management to your Expo app with Clerk.

There are three approaches for adding authentication to your Expo app.

| Approach | Auth UI | OAuth | Requires dev build | Best for |
| - | - | - | - | - |
| **JavaScript** | Custom flows | Browser-based | No (works in Expo Go) | Full control over UI |
| **JS + Native sign-in** | Custom flows + native OAuth buttons | Native (no browser) | Yes | Custom UI with native Sign in with Google/Apple |
| **Native components** | Pre-built native components | Native (no browser) | Yes | Fastest integration |

Use the following tabs to choose your preferred approach:


#### JavaScript (Native sign-in optional)


    

    This approach uses custom flows built with React Native components and **works in Expo Go — no dev build required.**

    
      ## Enable Native API

      In the Clerk Dashboard, navigate to the [**Native applications**](https://dashboard.clerk.com/~/native-applications) page and ensure that the Native API is enabled. This is required to integrate Clerk in your native application.


      ## Create a new Expo app

      If you don't already have an Expo app, run the following commands to [create a new one](https://docs.expo.dev/tutorial/create-your-first-app/).

```npm
npx create-expo-app@latest clerk-expo
cd clerk-expo
```


      ## Remove default template files

      The default Expo template includes files that will conflict with the routes you'll create in this guide. Remove the conflicting files and unused `components/` directory:

```bash
rm -rf "app/(tabs)" app/modal.tsx app/+not-found.tsx components/
```

The default template also includes `react-native-reanimated`, which can cause [known Android build issues](https://docs.expo.dev/versions/latest/sdk/reanimated/#known-issues). Since it's not needed for this guide, remove it to avoid build errors:

```bash
npm uninstall react-native-reanimated react-native-worklets --legacy-peer-deps
```

Then, remove the reanimated import from `app/_layout.tsx`:

```diff
// Filename: app/_layout.tsx

- import 'react-native-reanimated';
```

> [!IMPORTANT]
> You can skip this step if you used `npx create-expo-app@latest --template blank` to create your app. However, the blank template doesn't include [Expo Router](https://docs.expo.dev/router/introduction/) or pre-styled UI components. You'll need to install `expo-router` and its dependencies to follow along with this guide.


      ## Install dependencies

      Install the required packages. Use `npx expo install` to ensure SDK-compatible versions.

      - The [Clerk Expo SDK](/reference/expo/overview) gives you access to prebuilt components, hooks, and helpers to make user authentication easier.
      - Clerk stores the active user's session token in memory by default. In Expo apps, the recommended way to store sensitive data, such as tokens, is by using `expo-secure-store` which encrypts the data before storing it.

      ```bash
      npx expo install @clerk/expo expo-secure-store
      ```

      ## Set your Clerk API keys

      
  Add your Clerk Publishable Key to your `.env` file.


  1. In the Clerk Dashboard, navigate to the [**API keys**](https://dashboard.clerk.com/~/api-keys) page.
  1. In the **Quick Copy** section, copy your Clerk Publishable Key.
  1. Paste your key into your `.env` file.

  The final result should resemble the following:


      ```env
// Filename: .env

      EXPO_PUBLIC_CLERK_PUBLISHABLE_KEY={{pub_key}}
      ```

      ## Add `` to your root layout

      The [``](/reference/components/clerk-provider) component provides session and user context to Clerk's hooks and components. It's recommended to wrap your entire app at the entry point with `` to make authentication globally accessible. See the [reference docs](/reference/components/clerk-provider) for other configuration options.


Add the component to your root layout and pass your Publishable Key and `tokenCache` from `@clerk/expo/token-cache` as props, as shown in the following example:

```tsx
// Filename: app/_layout.tsx

import { ClerkProvider } from '@clerk/expo'
import { tokenCache } from '@clerk/expo/token-cache'
import { Slot } from 'expo-router'

const publishableKey = process.env.EXPO_PUBLIC_CLERK_PUBLISHABLE_KEY!

if (!publishableKey) {
  throw new Error('Add your Clerk Publishable Key to the .env file')
}

export default function RootLayout() {
  return (
    
      
  )
}
```


      ## Add sign-up and sign-in pages

      Clerk currently only supports [control components](/reference/components/overview#control-components) for Expo native. [UI components](/reference/components/overview) are only available for Expo web. Instead, you must build custom flows using Clerk's API. The following sections demonstrate how to build [custom email/password sign-up and sign-in flows](/guides/development/custom-flows/authentication/email-password). If you want to use different authentication methods, such as passwordless or OAuth, see the dedicated custom flow guides.

      ### Layout page

      First, protect your sign-up and sign-in pages.

      1. Create an `(auth)` [route group](https://docs.expo.dev/router/advanced/shared-routes/). This will group your sign-up and sign-in pages.
      1. In the `(auth)` group, create a `_layout.tsx` file with the following code. The [`useAuth()`](/reference/hooks/use-auth) hook is used to access the user's authentication state. If the user is already signed in, they will be redirected to the home page.

      ```tsx
// Filename: app/(auth)/_layout.tsx

      import { useAuth } from '@clerk/expo'
      import { Redirect, Stack } from 'expo-router'

      export default function AuthRoutesLayout() {
        const { isSignedIn, isLoaded } = useAuth()

        if (!isLoaded) {
          return null
        }

        if (isSignedIn) {
          return }

        return }
      ```

      ### Sign-up page

      In the `(auth)` group, create a `sign-up.tsx` file with the following code. The [`useSignUp()`](/reference/hooks/use-sign-up) hook is used to create a sign-up flow. The user can sign up using their email and password and will receive an email verification code to confirm their email.

```tsx
// Filename: app/(auth)/sign-up.tsx

import { ThemedText } from '@/components/themed-text'
import { ThemedView } from '@/components/themed-view'
import { useAuth, useSignUp } from '@clerk/expo'
import { type Href, Link, useRouter } from 'expo-router'
import React from 'react'
import { Pressable, StyleSheet, TextInput, View } from 'react-native'

export default function Page() {
  const { signUp, errors, fetchStatus } = useSignUp()
  const { isSignedIn } = useAuth()
  const router = useRouter()

  const [emailAddress, setEmailAddress] = React.useState('')
  const [password, setPassword] = React.useState('')
  const [code, setCode] = React.useState('')

  const handleSubmit = async () => {
    const { error } = await signUp.password({
      emailAddress,
      password,
    })
    if (error) {
      console.error(JSON.stringify(error, null, 2))
      return
    }

    if (!error) await signUp.verifications.sendEmailCode()
  }

  const handleVerify = async () => {
    await signUp.verifications.verifyEmailCode({
      code,
    })
    if (signUp.status === 'complete') {
      await signUp.finalize({
        // Redirect the user to the home page after signing up
        navigate: ({ session, decorateUrl }) => {
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
            router.push(url as Href)
          }
        },
      })
    } else {
      // Check why the sign-up is not complete
      console.error('Sign-up attempt not complete:', signUp)
    }
  }

  if (signUp.status === 'complete' || isSignedIn) {
    return null
  }

  if (
    signUp.status === 'missing_requirements' &&
    signUp.unverifiedFields.includes('email_address') &&
    signUp.missingFields.length === 0
  ) {
    return (
      
        
          Verify your account
        
         setCode(code)}
          keyboardType="numeric"
        />
        {errors.fields.code && (
          {errors.fields.code.message}
        )}
         [
            styles.button,
            fetchStatus === 'fetching' && styles.buttonDisabled,
            pressed && styles.buttonPressed,
          ]}
          onPress={handleVerify}
          disabled={fetchStatus === 'fetching'}
        >
          Verify
        
         [styles.secondaryButton, pressed && styles.buttonPressed]}
          onPress={() => signUp.verifications.sendEmailCode()}
        >
          I need a new code
        
      
    )
  }

  return (
    
      
        Sign up
      

      Email address
       setEmailAddress(emailAddress)}
        keyboardType="email-address"
      />
      {errors.fields.emailAddress && (
        {errors.fields.emailAddress.message}
      )}
      Password
       setPassword(password)}
      />
      {errors.fields.password && (
        {errors.fields.password.message}
      )}
       [
          styles.button,
          (!emailAddress || !password || fetchStatus === 'fetching') && styles.buttonDisabled,
          pressed && styles.buttonPressed,
        ]}
        onPress={handleSubmit}
        disabled={!emailAddress || !password || fetchStatus === 'fetching'}
      >
        Sign up
      
      
      {errors && {JSON.stringify(errors, null, 2)}}

      
        Already have an account? 
        
          Sign in
        
      

      
      
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
  secondaryButton: {
    paddingVertical: 12,
    paddingHorizontal: 24,
    borderRadius: 8,
    alignItems: 'center',
    marginTop: 8,
  },
  secondaryButtonText: {
    color: '#0a7ea4',
    fontWeight: '600',
  },
  linkContainer: {
    flexDirection: 'row',
    gap: 4,
    marginTop: 12,
    alignItems: 'center',
  },
  error: {
    color: '#d32f2f',
    fontSize: 12,
    marginTop: -8,
  },
  debug: {
    fontSize: 10,
    opacity: 0.5,
    marginTop: 8,
  },
})
```


      ### Sign-in page

      In the `(auth)` group, create a `sign-in.tsx` file with the following code. The [`useSignIn()`](/reference/hooks/use-sign-in) hook is used to create a sign-in flow. The user can sign in using email address and password, or navigate to the sign-up page.

```tsx
// Filename: app/(auth)/sign-in.tsx

import { ThemedText } from '@/components/themed-text'
import { ThemedView } from '@/components/themed-view'
import { useSignIn } from '@clerk/expo'
import { type Href, Link, useRouter } from 'expo-router'
import React from 'react'
import { Pressable, StyleSheet, TextInput, View } from 'react-native'

export default function Page() {
  const { signIn, errors, fetchStatus } = useSignIn()
  const router = useRouter()

  const [emailAddress, setEmailAddress] = React.useState('')
  const [password, setPassword] = React.useState('')
  const [code, setCode] = React.useState('')

  const handleSubmit = async () => {
    const { error } = await signIn.password({
      emailAddress,
      password,
    })
    if (error) {
      console.error(JSON.stringify(error, null, 2))
      return
    }

    if (signIn.status === 'complete') {
      await signIn.finalize({
        navigate: ({ session, decorateUrl }) => {
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
            router.push(url as Href)
          }
        },
      })
    } else if (signIn.status === 'needs_second_factor') {
      // See https://clerk.com/docs/guides/development/custom-flows/authentication/multi-factor-authentication
    } else if (signIn.status === 'needs_client_trust') {
      // For other second factor strategies,
      // see https://clerk.com/docs/guides/development/custom-flows/authentication/client-trust
      const emailCodeFactor = signIn.supportedSecondFactors.find(
        (factor) => factor.strategy === 'email_code',
      )

      if (emailCodeFactor) {
        await signIn.mfa.sendEmailCode()
      }
    } else {
      // Check why the sign-in is not complete
      console.error('Sign-in attempt not complete:', signIn)
    }
  }

  const handleVerify = async () => {
    await signIn.mfa.verifyEmailCode({ code })

    if (signIn.status === 'complete') {
      await signIn.finalize({
        navigate: ({ session, decorateUrl }) => {
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
            router.push(url as Href)
          }
        },
      })
    } else {
      // Check why the sign-in is not complete
      console.error('Sign-in attempt not complete:', signIn)
    }
  }

  if (signIn.status === 'needs_client_trust') {
    return (
      
        
          Verify your account
        
         setCode(code)}
          keyboardType="numeric"
        />
        {errors.fields.code && (
          {errors.fields.code.message}
        )}
         [
            styles.button,
            fetchStatus === 'fetching' && styles.buttonDisabled,
            pressed && styles.buttonPressed,
          ]}
          onPress={handleVerify}
          disabled={fetchStatus === 'fetching'}
        >
          Verify
        
         [styles.secondaryButton, pressed && styles.buttonPressed]}
          onPress={() => signIn.mfa.sendEmailCode()}
        >
          I need a new code
        
         [styles.secondaryButton, pressed && styles.buttonPressed]}
          onPress={() => signIn.reset()}
        >
          Start over
        
      
    )
  }

  return (
    
      
        Sign in
      

      Email address
       setEmailAddress(emailAddress)}
        keyboardType="email-address"
      />
      {errors.fields.identifier && (
        {errors.fields.identifier.message}
      )}
      Password
       setPassword(password)}
      />
      {errors.fields.password && (
        {errors.fields.password.message}
      )}
       [
          styles.button,
          (!emailAddress || !password || fetchStatus === 'fetching') && styles.buttonDisabled,
          pressed && styles.buttonPressed,
        ]}
        onPress={handleSubmit}
        disabled={!emailAddress || !password || fetchStatus === 'fetching'}
      >
        Continue
      
      
      {errors && {JSON.stringify(errors, null, 2)}}

      
        Don't have an account? 
        
          Sign up
        
      
    
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
  secondaryButton: {
    paddingVertical: 12,
    paddingHorizontal: 24,
    borderRadius: 8,
    alignItems: 'center',
    marginTop: 8,
  },
  secondaryButtonText: {
    color: '#0a7ea4',
    fontWeight: '600',
  },
  linkContainer: {
    flexDirection: 'row',
    gap: 4,
    marginTop: 12,
    alignItems: 'center',
  },
  error: {
    color: '#d32f2f',
    fontSize: 12,
    marginTop: -8,
  },
  debug: {
    fontSize: 10,
    opacity: 0.5,
    marginTop: 8,
  },
})
```


      For more information about building these custom flows, including guided comments in the code examples, see the [Build a custom email/password authentication flow](/guides/development/custom-flows/authentication/email-password) guide.

      ## Add a home screen

      You can control which content signed-in and signed-out users can see with Clerk's [prebuilt control components](/reference/components/overview#control-components). For this guide, you'll use:

      - [``](/reference/components/control/show): Children of this component can only be seen while **signed in**.
      - [``](/reference/components/control/show): Children of this component can only be seen while **signed out**.

      1. Create a `(home)` route group.
      1. In the `(home)` group, create a `_layout.tsx` file with the following code.

      ```tsx
// Filename: app/(home)/_layout.tsx

      import { useAuth } from '@clerk/expo'
      import { Redirect, Stack } from 'expo-router'

      export default function Layout() {
        const { isSignedIn, isLoaded } = useAuth()

        if (!isLoaded) {
          return null
        }

        if (!isSignedIn) {
          return }

        return }
      ```

      Then, in the same folder, create an `index.tsx` file. If the user is signed in, it displays their email and a sign-out button. If they're not signed in, it displays sign-in and sign-up links.

      ```tsx
// Filename: app/(home)/index.tsx

      import { Show, useUser } from '@clerk/expo'
      import { useClerk } from '@clerk/expo'
      import { Link } from 'expo-router'
      import { Text, View, Pressable, StyleSheet } from 'react-native'

      export default function Page() {
        const { user } = useUser()
        const { signOut } = useClerk()

        return (
          
            Welcome!
            
              
                Sign in
              
              
                Sign up
              
            
            
              Hello {user?.emailAddresses[0].emailAddress}
               signOut()}>
                Sign out
              
            
          
        )
      }

      const styles = StyleSheet.create({
        container: {
          flex: 1,
          padding: 20,
          paddingTop: 60,
          gap: 16,
        },
        title: {
          fontSize: 24,
          fontWeight: 'bold',
        },
        button: {
          backgroundColor: '#0a7ea4',
          paddingVertical: 12,
          paddingHorizontal: 24,
          borderRadius: 8,
          alignItems: 'center',
        },
        buttonText: {
          color: '#fff',
          fontWeight: '600',
        },
      })
      ```

      ## Run your project

      Run your project with the following command:

      ```bash
      npx expo start
      ```

      Then use the terminal shortcuts to run the app on your preferred platform:

- Press `i` to open the iOS simulator.
- Press `a` to open the Android emulator.
- Scan the QR code with Expo Go to run the app on a physical device.


      ## Create your first user

      Once the app opens on your device or simulator:

- Navigate to the Sign up screen.
- Enter your details and complete the authentication flow.
- After signing up, your first user will be created and you'll be signed in.


      ## Native sign-in with Google and Apple (optional)

      If you want to add native Sign in with Google and Sign in with Apple buttons that authenticate without opening a browser, you'll need to install `expo-crypto`:

      ```bash
      npx expo install expo-crypto
      ```

      Then, refer to the [Sign in with Google](/guides/configure/auth-strategies/sign-in-with-google) and [Sign in with Apple](/guides/configure/auth-strategies/sign-in-with-apple) guides for full setup instructions, including any additional dependencies specific to each provider. **This approach requires a [development build](https://docs.expo.dev/develop/development-builds/introduction/) because it uses native modules. It cannot run in Expo Go.**
    
  

#### Native components


    

    > [!WARNING]
> Expo native components are currently in beta. If you run into any issues, please reach out to our [support team](https://clerk.com/support).


    This approach uses Clerk's [pre-built native components](/reference/expo/native-components/overview) that render using SwiftUI on iOS and Jetpack Compose on Android. This requires the least code and a [development build](https://docs.expo.dev/develop/development-builds/introduction/).

    
      ## Enable Native API

      In the Clerk Dashboard, navigate to the [**Native applications**](https://dashboard.clerk.com/~/native-applications) page and ensure that the Native API is enabled. This is required to integrate Clerk in your native application.


      ## Create a new Expo app

      If you don't already have an Expo app, run the following commands to [create a new one](https://docs.expo.dev/tutorial/create-your-first-app/).

```npm
npx create-expo-app@latest clerk-expo
cd clerk-expo
```


      ## Remove default template files

      The default Expo template includes files that will conflict with the routes you'll create in this guide. Remove the conflicting files and unused `components/` directory:

```bash
rm -rf "app/(tabs)" app/modal.tsx app/+not-found.tsx components/
```

The default template also includes `react-native-reanimated`, which can cause [known Android build issues](https://docs.expo.dev/versions/latest/sdk/reanimated/#known-issues). Since it's not needed for this guide, remove it to avoid build errors:

```bash
npm uninstall react-native-reanimated react-native-worklets --legacy-peer-deps
```

Then, remove the reanimated import from `app/_layout.tsx`:

```diff
// Filename: app/_layout.tsx

- import 'react-native-reanimated';
```

> [!IMPORTANT]
> You can skip this step if you used `npx create-expo-app@latest --template blank` to create your app. However, the blank template doesn't include [Expo Router](https://docs.expo.dev/router/introduction/) or pre-styled UI components. You'll need to install `expo-router` and its dependencies to follow along with this guide.


      ## Install dependencies

      Install the required packages. Use `npx expo install` to ensure SDK-compatible versions.

      - The [Clerk Expo SDK](/reference/expo/overview) gives you access to prebuilt components, hooks, and helpers to make user authentication easier.
      - Clerk stores the active user's session token in memory by default. In Expo apps, the recommended way to store sensitive data, such as tokens, is by using `expo-secure-store` which encrypts the data before storing it.
      - `expo-auth-session` handles authentication redirects and OAuth flows in Expo apps.
      - `expo-web-browser` opens the system browser during authentication and returns the user to the app once the flow is complete.
      - `expo-dev-client` allows you to build and run your app in development mode.

      ```bash
      npx expo install @clerk/expo expo-secure-store expo-auth-session expo-web-browser expo-dev-client
      ```

      ## Set your Clerk API keys

      
  Add your Clerk Publishable Key to your `.env` file.


  1. In the Clerk Dashboard, navigate to the [**API keys**](https://dashboard.clerk.com/~/api-keys) page.
  1. In the **Quick Copy** section, copy your Clerk Publishable Key.
  1. Paste your key into your `.env` file.

  The final result should resemble the following:


      ```env
// Filename: .env

      EXPO_PUBLIC_CLERK_PUBLISHABLE_KEY={{pub_key}}
      ```

      ## Verify `app.json` plugins

      Run `npx expo install` to automatically add the required config plugins to your `app.json` file. Then verify that `@clerk/expo` and `expo-secure-store` appear in the `plugins` array:

      ```json
// Filename: app.json

      {
        "expo": {
          "plugins": ["expo-secure-store", "@clerk/expo"]
        }
      }
      ```

      ## Add `` to your root layout

      The [``](/reference/components/clerk-provider) component provides session and user context to Clerk's hooks and components. It's recommended to wrap your entire app at the entry point with `` to make authentication globally accessible. See the [reference docs](/reference/components/clerk-provider) for other configuration options.


Add the component to your root layout and pass your Publishable Key and `tokenCache` from `@clerk/expo/token-cache` as props, as shown in the following example:

```tsx
// Filename: app/_layout.tsx

import { ClerkProvider } from '@clerk/expo'
import { tokenCache } from '@clerk/expo/token-cache'
import { Slot } from 'expo-router'

const publishableKey = process.env.EXPO_PUBLIC_CLERK_PUBLISHABLE_KEY!

if (!publishableKey) {
  throw new Error('Add your Clerk Publishable Key to the .env file')
}

export default function RootLayout() {
  return (
    
      
  )
}
```


      ## Add authentication and home screen

      With [native components](/reference/expo/native-components/overview), you can build a complete app in a single file. The [``](/reference/expo/native-components/auth-view) component handles all sign-in and sign-up flows, [``](/reference/expo/native-components/user-button) provides a profile avatar that opens the native profile modal, and the [`useUserProfileModal()`](/reference/expo/native-components/user-profile-view) hook lets you open the profile modal from any button.

      Create an `index.tsx` file in your `app` folder with the following code. If the user is signed in, it displays their email, a profile button, and a sign-out button. If they're not signed in, it displays the `` component which handles both sign-in and sign-up.

      ```tsx
// Filename: app/index.tsx

      import { useAuth, useUser, useClerk, useUserProfileModal } from '@clerk/expo'
      import { AuthView, UserButton } from '@clerk/expo/native'
      import { Text, View, StyleSheet, Image, TouchableOpacity, ActivityIndicator } from 'react-native'

      export default function MainScreen() {
        const { isSignedIn, isLoaded } = useAuth()
        const { user } = useUser()
        const { signOut } = useClerk()
        const { presentUserProfile } = useUserProfileModal()

        if (!isLoaded) {
          return (
            
              
          )
        }

        if (!isSignedIn) {
          return }

        return (
          
            
              Welcome
              
                
            
            
              {user?.imageUrl && }
              
                
                  {user?.firstName || 'User'} {user?.lastName || ''}
                
                {user?.emailAddresses[0]?.emailAddress}
              
            
            
              Manage Profile
            
             signOut()}
            >
              Sign Out
            
          
        )
      }

      const styles = StyleSheet.create({
        centered: {
          flex: 1,
          justifyContent: 'center',
          alignItems: 'center',
          backgroundColor: '#fff',
          padding: 40,
        },
        container: {
          flex: 1,
          backgroundColor: '#fff',
          padding: 20,
          paddingTop: 60,
          gap: 16,
        },
        header: {
          flexDirection: 'row',
          alignItems: 'center',
          justifyContent: 'space-between',
        },
        title: {
          fontSize: 28,
          fontWeight: 'bold',
        },
        profileCard: {
          flexDirection: 'row',
          alignItems: 'center',
          padding: 16,
          backgroundColor: '#f5f5f5',
          borderRadius: 12,
          gap: 12,
        },
        avatar: {
          width: 48,
          height: 48,
          borderRadius: 24,
        },
        name: {
          fontSize: 18,
          fontWeight: '600',
        },
        email: {
          fontSize: 14,
          color: '#666',
        },
        linkButton: {
          backgroundColor: '#007AFF',
          padding: 16,
          borderRadius: 12,
          alignItems: 'center',
        },
        linkButtonText: {
          color: '#fff',
          fontSize: 16,
          fontWeight: '600',
        },
      })
      ```

      ## Build and run

      This approach requires a [development build](https://docs.expo.dev/develop/development-builds/introduction/) because it uses native modules. It **cannot** run in Expo Go.

      ```bash
# Filename: terminal

      # Using Expo CLI
      npx expo run:ios
      npx expo run:android

      # Using EAS Build
      eas build --platform ios
      eas build --platform android

      # Or using local prebuild
      npx expo prebuild && npx expo run:ios --device
      npx expo prebuild && npx expo run:android --device
      ```

      Then use the terminal shortcuts to run the app on your preferred platform:

- Press `i` to open the iOS simulator.
- Press `a` to open the Android emulator.
- Scan the QR code with Expo Go to run the app on a physical device.


      ## Create your first user

      Once the app opens on your device or simulator:

- Navigate to the Sign up screen.
- Enter your details and complete the authentication flow.
- After signing up, your first user will be created and you'll be signed in.


      ## Configure social connections (optional)

      `` automatically shows sign-in buttons for any social connections enabled in your [Clerk Dashboard](https://dashboard.clerk.com/~/user-authentication/sso-connections). However, native OAuth requires additional credential setup — without it, the buttons will appear but fail with an error when tapped.

### Sign in with Google

Follow the steps in the [Sign in with Google](/guides/configure/auth-strategies/sign-in-with-google) guide to complete the following:

1. [Enable Google as a social connection](https://dashboard.clerk.com/~/user-authentication/sso-connections) with **Use custom credentials** toggled on.
1. Create OAuth 2.0 credentials in the [Google Cloud Console](https://console.cloud.google.com/) — you'll need an **iOS Client ID**, **Android Client ID**, and **Web Client ID**.
1. Set the **Web Client ID** and **Client Secret** in the [Clerk Dashboard](https://dashboard.clerk.com/~/user-authentication/sso-connections).
1. Add your iOS application to the [**Native Applications**](https://dashboard.clerk.com/~/native-applications) page in the Clerk Dashboard (Team ID + Bundle ID).
1. Add your Android application to the [**Native Applications**](https://dashboard.clerk.com/~/native-applications) page in the Clerk Dashboard (package name).
1. Add the Google Client IDs as environment variables in your `.env` file. Follow the `.env.example` in the [Sign in with Google](/guides/configure/auth-strategies/sign-in-with-google#configure-environment-variables) guide.
1. Configure the `@clerk/expo` plugin with the iOS URL scheme in your `app.json`.

> [!IMPORTANT]
> You do **not** need to install `expo-crypto` or use the `useSignInWithGoogle()` hook — `` handles the sign-in flow automatically.

### Sign in with Apple

Follow the steps in the [Sign in with Apple](/guides/configure/auth-strategies/sign-in-with-apple) guide to complete the following:

1. Add your iOS application to the [**Native Applications**](https://dashboard.clerk.com/~/native-applications) page in the Clerk Dashboard (Team ID + Bundle ID).
1. [Enable Apple as a social connection](https://dashboard.clerk.com/~/user-authentication/sso-connections) in the Clerk Dashboard.

> [!IMPORTANT]
> You do **not** need to install `expo-apple-authentication`, `expo-crypto`, or use the `useSignInWithApple()` hook — `` handles the sign-in flow automatically.

    
  

## Enable OTA updates

Though not required, it is recommended to implement over-the-air (OTA) updates in your Expo app. This enables you to easily roll out Clerk's feature updates and security patches as they're released without having to resubmit your app to mobile marketplaces.

See the [`expo-updates`](https://docs.expo.dev/versions/latest/sdk/updates) library to learn how to get started.

## Next steps

Learn more about Clerk prebuilt components, custom flows for your native apps, and how to deploy an Expo app to production using the following guides.


  - [Create a custom sign-up and sign-in flow](/guides/development/custom-flows/authentication/email-password)
  - Learn how to build a custom sign-up and sign-in authentication flow.

  ---

  - [Prebuilt native components (beta)](/reference/expo/native-components/overview)
  - Learn how to quickly add authentication to your app using Clerk's pre-built native UI for iOS and Android.

  ---

  - [Protect content and read user data](/expo/guides/users/reading)
  - Learn how to use Clerk's hooks and helpers to protect content and read user data in your Expo app.

  ---

  - [Custom flows](/guides/development/custom-flows/overview)
  - Expo native apps require custom flows in place of prebuilt components.

  ---

  - [Deploy an Expo app to production](/guides/development/deployment/expo)
  - Learn how to deploy your Expo app to production.

  ---

  - [Clerk Expo SDK Reference](/reference/expo/overview)
  - Learn about the Clerk Expo SDK and how to integrate it into your app.
