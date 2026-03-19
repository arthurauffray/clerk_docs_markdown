# Build a custom flow for handling legal acceptance


> Learn how to use the Clerk API to build a custom user interface for handling legal acceptance.

> [!WARNING]
> This guide is for users who want to build a custom flow. To use a _prebuilt_ UI, use the [Account Portal pages](/guides/account-portal/overview) or [prebuilt components](/reference/components/overview).


> [!IMPORTANT]
> This guide uses the Core 2 `useSignIn()` and `useSignUp()` hooks, which are available in Core 3 SDKs by adding the `/legacy` subpath to the import path. If you're using a Core 2 SDK, remove the `/legacy` subpath.


When the legal acceptance feature is enabled, users are required to agree to your Terms of Service and Privacy Policy before they can sign up to your application.

If you're using the `` component, a checkbox appears and the legal acceptance flow is handled for you. However, if you're building a custom user interface, you need to handle legal acceptance in your sign-up form.

This guide demonstrates how to use the Clerk API to build a custom user interface for handling legal acceptance.

## Before you start

By default, the legal acceptance feature is disabled. To enable it, navigate to the [**Legal**](https://dashboard.clerk.com/~/compliance/legal) page in the Clerk Dashboard.

## Add legal acceptance to your sign-up flow

The following example adds the legal acceptance logic to the [Email and password custom flow](/guides/development/custom-flows/authentication/email-password), but you can apply the same logic to any custom flow.


  
    > [!TIP]
> Examples for this SDK aren't available yet. For now, try adapting the  available example to fit your SDK.

  

  To support legal acceptance, you need to add a checkbox to your sign-up form, capture the checkbox value, and pass it to the [`SignUp.create()`](/reference/javascript/sign-up#create) method.

  ```tsx
// Filename: app/sign-up/[[...sign-up]]/page.tsx

  'use client'

  import * as React from 'react'
  import { useSignUp } from '@clerk/nextjs/legacy'
  import { useRouter } from 'next/navigation'
  import Link from 'next/link'

  export default function Page() {
    const { isLoaded, signUp, setActive } = useSignUp()
    const [emailAddress, setEmailAddress] = React.useState('')
    const [password, setPassword] = React.useState('')
    const [legalAccepted, setLegalAccepted] = React.useState(false)
    const [verifying, setVerifying] = React.useState(false)
    const [code, setCode] = React.useState('')
    const router = useRouter()

    // Handle submission of the sign-up form
    const handleSubmit = async (e: React.FormEvent) => {
      e.preventDefault()

      if (!isLoaded) return <div>Loading...</div>

      // Start the sign-up process using the email and password provided
      try {
        await signUp.create({
          emailAddress,
          password,
          legalAccepted,
        })

        // Send the user an email with the verification code
        await signUp.prepareEmailAddressVerification({
          strategy: 'email_code',
        })

        // Set 'verifying' true to display second form
        // and capture the code
        setVerifying(true)
      } catch (err: any) {
        // See https://clerk.com/docs/guides/development/custom-flows/error-handling
        // for more info on error handling
        console.error(JSON.stringify(err, null, 2))
      }
    }

    // Handle the submission of the verification form
    const handleVerify = async (e: React.FormEvent) => {
      e.preventDefault()

      if (!isLoaded) return <div>Loading...</div>

      try {
        // Use the code the user provided to attempt verification
        const signUpAttempt = await signUp.attemptEmailAddressVerification({
          code,
        })

        // If verification was completed, set the session to active
        // and redirect the user
        if (signUpAttempt.status === 'complete') {
          await setActive({
            session: signUpAttempt.createdSessionId,
            navigate: async ({ session, decorateUrl }) => {
              if (session?.currentTask) {
                //  Handle pending session tasks
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
          // If the status is not complete, check why. User may need to
          // complete further steps.
          console.error('Sign-up attempt not complete:', signUpAttempt)
          console.error('Sign-up attempt status:', signUpAttempt.status)
        }
      } catch (err: any) {
        // See https://clerk.com/docs/guides/development/custom-flows/error-handling
        // for more info on error handling
        console.error(JSON.stringify(err, null, 2))
      }
    }

    // Display the verification form to capture the code
    if (verifying) {
      return (
        <>
          <h1>Verify your email</h1>
          <form onSubmit={handleVerify}>
            <label id="code">Enter your verification code</label>
            <input value={code} id="code" name="code" onChange={(e) => setCode(e.target.value)} />
            <button type="submit">Verify</button>
          </form>
        </>
      )
    }

    // Display the initial sign-up form to capture the email and password
    return (
      <>
        <h1>Sign up</h1>
        <form onSubmit={handleSubmit}>
          <div>
            <label htmlFor="email">Enter email address</label>
            <input
              id="email"
              type="email"
              name="email"
              value={emailAddress}
              onChange={(e) => setEmailAddress(e.target.value)}
            />
          </div>

          <div>
            <label htmlFor="password">Enter password</label>
            <input
              id="password"
              type="password"
              name="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
            />
          </div>

          <div>
            <label htmlFor="legalAccepted">
              I accept the Terms of Service and{' '}
              Privacy Policy
            </label>
            <input
              id="legalAccepted"
              type="checkbox"
              name="legalAccepted"
              checked={legalAccepted}
              onChange={(e) => setLegalAccepted(e.target.checked)}
            />
          </div>

          
          <div id="clerk-captcha" />

          <div>
            <button type="submit">Continue</button>
          </div>
        </form>
      </>
    )
  }
  ```


  This example uses `expo-checkbox` to create the checkbox. Install it with the following command:

  ```npm
  npm install expo-checkbox
  ```

  Then, update your sign-up page to include the legal acceptance checkbox. The following example uses the [email and password sign-up example](/guides/development/custom-flows/authentication/email-password).

  ```tsx
// Filename: app/(auth)/sign-up.tsx

    import { ThemedText } from '@/components/themed-text'
    import { ThemedView } from '@/components/themed-view'
    import { useSignUp } from '@clerk/expo/legacy'
    import { Link, useRouter } from 'expo-router'
    import * as React from 'react'
    import { Pressable, StyleSheet, TextInput, View } from 'react-native'
  + import Checkbox from 'expo-checkbox'

    export default function Page() {
      const { isLoaded, signUp, setActive } = useSignUp()
      const router = useRouter()

      const [emailAddress, setEmailAddress] = React.useState('')
      const [password, setPassword] = React.useState('')
  +   const [legalAccepted, setLegalAccepted] = React.useState(false)
      const [pendingVerification, setPendingVerification] = React.useState(false)
      const [code, setCode] = React.useState('')

      // Handle submission of sign-up form
      const onSignUpPress = async () => {
        if (!isLoaded) return

        // Start sign-up process using email and password provided
        try {
          await signUp.create({
            emailAddress,
            password,
  +         legalAccepted,
          })

          // Send user an email with verification code
          await signUp.prepareEmailAddressVerification({ strategy: 'email_code' })

          // Set 'pendingVerification' to true to display second form
          // and capture code
          setPendingVerification(true)
        } catch (err) {
          // See https://clerk.com/docs/guides/development/custom-flows/error-handling
          // for more info on error handling
          console.error(JSON.stringify(err, null, 2))
        }
      }

      // Handle submission of verification form
      const onVerifyPress = async () => {
        if (!isLoaded) return

        try {
          // Use the code the user provided to attempt verification
          const signUpAttempt = await signUp.attemptEmailAddressVerification({
            code,
          })

          // If verification was completed, set the session to active
          // and redirect the user
          if (signUpAttempt.status === 'complete') {
            await setActive({
              session: signUpAttempt.createdSessionId,
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
            // If the status is not complete, check why. User may need to
            // complete further steps.
            console.error(JSON.stringify(signUpAttempt, null, 2))
          }
        } catch (err) {
          // See https://clerk.com/docs/guides/development/custom-flows/error-handling
          // for more info on error handling
          console.error(JSON.stringify(err, null, 2))
        }
      }

      if (pendingVerification) {
        return (
          
            
              Verify your email
            
            
              A verification code has been sent to your email.
            
             setCode(code)}
              keyboardType="numeric"
            />
             [styles.button, pressed && styles.buttonPressed]}
              onPress={onVerifyPress}
            >
              Verify
            
          
        )
      }

      return (
        
          
            Sign up
          
          Email address
           setEmailAddress(email)}
            keyboardType="email-address"
          />
          Password
           setPassword(password)}
          />
  +       
  +         +          setLegalAccepted(!legalAccepted)}>
  +           
  +             I accept the{' '}
  +             
  +               Terms of Service
  +             {' '}
  +             and{' '}
  +             
  +               Privacy Policy
  +             
  +           
  +         
  +       
           [
              styles.button,
              (!emailAddress || !password || !legalAccepted) && styles.buttonDisabled,
              pressed && styles.buttonPressed,
            ]}
            onPress={onSignUpPress}
            disabled={!emailAddress || !password || !legalAccepted}
          >
            Continue
          
          
            Have an account? 
            
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
      description: {
        fontSize: 14,
        marginBottom: 16,
        opacity: 0.8,
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
      legalContainer: {
        flexDirection: 'row',
        alignItems: 'center',
        marginVertical: 8,
      },
      checkbox: {
        marginRight: 8,
      },
      legalText: {
        flex: 1,
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
      linkContainer: {
        flexDirection: 'row',
        gap: 4,
        marginTop: 12,
        alignItems: 'center',
      },
    })
  ```
