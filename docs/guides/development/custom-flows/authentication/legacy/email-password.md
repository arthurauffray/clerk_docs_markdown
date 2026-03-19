# Build a custom email/password authentication flow


> Learn how to build a custom email/password sign-up and sign-in flow using the Clerk API.

> [!WARNING]
> This guide is for users who want to build a custom flow. To use a _prebuilt_ UI, use the [Account Portal pages](/guides/account-portal/overview) or [prebuilt components](/reference/components/overview).


> [!IMPORTANT]
> This guide uses the Core 2 `useSignIn()` and `useSignUp()` hooks, which are available in Core 3 SDKs by adding the `/legacy` subpath to the import path. If you're using a Core 2 SDK, remove the `/legacy` subpath.


This guide will walk you through how to build a custom email and password sign-up and sign-in flow.


  ## Enable email and password authentication

  To use email and password authentication, you first need to ensure they are enabled for your application.

  1. Enable **Sign-up with email**.
     - For **Verify at sign-up**, **Email verification code** is enabled by default, and is used for this guide. If you'd like to use **Email verification link** instead, see the [email links custom flow](/guides/development/custom-flows/authentication/email-links).
  1. Enable **Sign in with email**.
     - This guide supports password authentication. If you'd like to build a custom flow that allows users to sign in passwordlessly, see the [email code custom flow](/guides/development/custom-flows/authentication/email-sms-otp) or the [email links custom flow](/guides/development/custom-flows/authentication/email-links).
  1. Select the **Password** tab and enable **Sign-up with password**.

  ## Sign-up flow

  
    
      > [!TIP]
> Examples for this SDK aren't available yet. For now, try adapting the  available example to fit your SDK.

    

    
      > [!TIP]
> Examples for this SDK aren't available yet. For now, try adapting the  available example to fit your SDK.

    

    1. Initiate the sign-up process by passing the user's email address and password to the [`SignUp.create()`](/reference/javascript/sign-up#create) method.
    1. To verify the user's email address, send a one-time code to the provided email address with the [`SignUp.prepareEmailAddressVerification()`](/reference/javascript/sign-up#prepare-email-address-verification) method.
    1. Collect the user's one-time code and verify it with the [`SignUp.attemptEmailAddressVerification()`](/reference/javascript/sign-up#attempt-email-address-verification) method.
    1. If the email address verification is successful, the `SignUp.status` will be `complete`, and you can finish the sign-up flow by calling the [`setActive()`](/reference/javascript/clerk#set-active) method, which will set the newly created session as the active session. You may need to check for session tasks that are required for the user to complete after signing up.

    ```tsx
// Filename: app/sign-up/[[...sign-up]]/page.tsx

    'use client'

    import * as React from 'react'
    import { useSignUp } from '@clerk/nextjs/legacy'
    import { useRouter } from 'next/navigation'

    export default function Page() {
      const { isLoaded, signUp, setActive } = useSignUp()
      const [emailAddress, setEmailAddress] = React.useState('')
      const [password, setPassword] = React.useState('')
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

            
            <div id="clerk-captcha" />

            <div>
              <button type="submit">Continue</button>
            </div>
          </form>
        </>
      )
    }
    ```
  

  
    In the `(auth)` group, create a `sign-up.tsx` file with the following code. The [`useSignUp()`](/reference/hooks/use-sign-up) hook is used to create a sign-up flow. The user can sign up using their email and password and will receive an email verification code to confirm their email.

```tsx
// Filename: app/(auth)/sign-up.tsx

import { ThemedText } from '@/components/themed-text'
import { ThemedView } from '@/components/themed-view'
import { useSignUp } from '@clerk/expo/legacy'
import { Link, useRouter } from 'expo-router'
import * as React from 'react'
import { Pressable, StyleSheet, TextInput, View } from 'react-native'

export default function Page() {
  const { isLoaded, signUp, setActive } = useSignUp()
  const router = useRouter()

  const [emailAddress, setEmailAddress] = React.useState('')
  const [password, setPassword] = React.useState('')
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
       [
          styles.button,
          (!emailAddress || !password) && styles.buttonDisabled,
          pressed && styles.buttonPressed,
        ]}
        onPress={onSignUpPress}
        disabled={!emailAddress || !password}
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

  

  
    
**index.html:**

```html
<!-- Filename: index.html -->

      <!doctype html>
      <html lang="en">
        <head>
          <meta charset="UTF-8" />
          <meta name="viewport" content="width=device-width, initial-scale=1.0" />
          <title>Clerk + JavaScript App</title>
        </head>
        <body>
          <div id="signed-in"></div>

          <div id="sign-up">
            <h2>Sign up</h2>
            <form id="sign-up-form">
              <label for="email">Enter email address</label>
              <input type="email" name="email" id="sign-up-email" />
              <label for="password">Enter password</label>
              <input type="password" name="password" id="sign-up-password" />
              <button type="submit">Continue</button>
            </form>
          </div>

          <form id="verifying" hidden>
            <h2>Verify your email</h2>
            <label for="code">Enter your verification code</label>
            <input id="code" name="code" />
            <button type="submit" id="verify-button">Verify</button>
          </form>

          <script type="module" src="/src/main.js" async crossorigin="anonymous"></script>
        </body>
      </html>
      ```


**main.js:**

```js
// Filename: main.js

      import { Clerk } from '@clerk/clerk-js'

      const pubKey = import.meta.env.VITE_CLERK_PUBLISHABLE_KEY

      const clerk = new Clerk(pubKey)
      await clerk.load()

      if (clerk.isSignedIn) {
        // Mount user button component
        document.getElementById('signed-in').innerHTML = `
          <div id="user-button"></div>
        `

        const userbuttonDiv = document.getElementById('user-button')

        clerk.mountUserButton(userbuttonDiv)
      } else {
        // Handle the sign-up form
        document.getElementById('sign-up-form').addEventListener('submit', async (e) => {
          e.preventDefault()

          const formData = new FormData(e.target)
          const emailAddress = formData.get('email')
          const password = formData.get('password')

          try {
            // Start the sign-up process using the email and password provided
            await clerk.client.signUp.create({ emailAddress, password })
            await clerk.client.signUp.prepareEmailAddressVerification()
            // Hide sign-up form
            document.getElementById('sign-up').setAttribute('hidden', '')
            // Show verification form
            document.getElementById('verifying').removeAttribute('hidden')
          } catch (error) {
            // See https://clerk.com/docs/guides/development/custom-flows/error-handling
            // for more info on error handling
            console.error(error)
          }
        })

        // Handle the verification form
        document.getElementById('verifying').addEventListener('submit', async (e) => {
          const formData = new FormData(e.target)
          const code = formData.get('code')

          try {
            // Use the code the user provided to attempt verification
            const signUpAttempt = await clerk.client.signUp.attemptEmailAddressVerification({
              code,
            })

            // Now that the user is created, set the session to active.
            await clerk.setActive({ session: signUpAttempt.createdSessionId })
          } catch (error) {
            // See https://clerk.com/docs/guides/development/custom-flows/error-handling
            // for more info on error handling
            console.error(error)
          }
        })
      }
      ```

  

  ## Sign-in flow

  
    
      > [!TIP]
> Examples for this SDK aren't available yet. For now, try adapting the  available example to fit your SDK.

    

    1. Initiate the sign-in process by passing the user's email address and password to the [`SignIn.create()`](/reference/javascript/sign-in#create) method.
    1. Check if the sign-in requires a second factor. [Client Trust](/guides/secure/client-trust), which is enabled by default for new Clerk applications, may require users to verify their identity with second factor. This example handles the `email_code` second factor, so send a one-time code to the provided email address with the [`SignIn.prepareSecondFactor()`](/reference/javascript/sign-in#prepare-second-factor) method.
    1. Collect the user's one-time code and verify it with the [`SignIn.attemptSecondFactor()`](/reference/javascript/sign-in#attempt-second-factor) method.
    1. If the second factor verification is successful, the `SignIn.status` will be `complete`, and you can finish the sign-in flow by calling the [`setActive()`](/reference/javascript/clerk#set-active) method, which will set the newly created session as the active session. You may need to check for session tasks that are required for the user to complete after signing in.

    ```tsx
// Filename: app/sign-in/[[...sign-in]]/page.tsx

    'use client'

    import * as React from 'react'
    import { useSignIn } from '@clerk/nextjs/legacy'
    import { useRouter } from 'next/navigation'
    import type { EmailCodeFactor } from '@clerk/shared/types'

    export default function SignInForm() {
      const { isLoaded, signIn, setActive } = useSignIn()
      const [email, setEmail] = React.useState('')
      const [password, setPassword] = React.useState('')
      const [code, setCode] = React.useState('')
      const [showEmailCode, setShowEmailCode] = React.useState(false)
      const router = useRouter()

      // Handle the submission of the sign-in form
      const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault()

        if (!isLoaded) return

        // Start the sign-in process using the email and password provided
        try {
          const signInAttempt = await signIn.create({
            identifier: email,
            password,
          })

          // If sign-in process is complete, set the created session as active
          // and redirect the user
          if (signInAttempt.status === 'complete') {
            await setActive({
              session: signInAttempt.createdSessionId,
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
          } else if (signInAttempt.status === 'needs_second_factor') {
            // Check if email_code is a valid second factor
            // This is required when Client Trust is enabled and the user
            // is signing in from a new device.
            // See https://clerk.com/docs/guides/secure/client-trust
            const emailCodeFactor = signInAttempt.supportedSecondFactors?.find(
              (factor): factor is EmailCodeFactor => factor.strategy === 'email_code',
            )

            if (emailCodeFactor) {
              await signIn.prepareSecondFactor({
                strategy: 'email_code',
                emailAddressId: emailCodeFactor.emailAddressId,
              })
              setShowEmailCode(true)
            }
          } else {
            // If the status is not complete, check why. User may need to
            // complete further steps.
            console.error(JSON.stringify(signInAttempt, null, 2))
          }
        } catch (err: any) {
          // See https://clerk.com/docs/guides/development/custom-flows/error-handling
          // for more info on error handling
          console.error(JSON.stringify(err, null, 2))
        }
      }

      // Handle the submission of the email verification code
      const handleEmailCode = async (e: React.FormEvent) => {
        e.preventDefault()

        if (!isLoaded) return

        try {
          const signInAttempt = await signIn.attemptSecondFactor({
            strategy: 'email_code',
            code,
          })

          if (signInAttempt.status === 'complete') {
            await setActive({
              session: signInAttempt.createdSessionId,
              navigate: async ({ session, decorateUrl }) => {
                // Handle pending session tasks
                // See https://clerk.com/docs/guides/development/custom-flows/authentication/session-tasks
                if (session?.currentTask) {
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
            console.error(JSON.stringify(signInAttempt, null, 2))
          }
        } catch (err: any) {
          console.error(JSON.stringify(err, null, 2))
        }
      }

      // Display email code verification form
      if (showEmailCode) {
        return (
          <>
            <h1>Verify your email</h1>
            <p>A verification code has been sent to your email.</p>
            <form onSubmit={handleEmailCode}>
              <div>
                <label htmlFor="code">Enter verification code</label>
                <input
                  onChange={(e) => setCode(e.target.value)}
                  id="code"
                  name="code"
                  type="text"
                  inputMode="numeric"
                  value={code}
                />
              </div>
              <button type="submit">Verify</button>
            </form>
          </>
        )
      }

      // Display a form to capture the user's email and password
      return (
        <>
          <h1>Sign in</h1>
          <form onSubmit={handleSubmit}>
            <div>
              <label htmlFor="email">Enter email address</label>
              <input
                onChange={(e) => setEmail(e.target.value)}
                id="email"
                name="email"
                type="email"
                value={email}
              />
            </div>
            <div>
              <label htmlFor="password">Enter password</label>
              <input
                onChange={(e) => setPassword(e.target.value)}
                id="password"
                name="password"
                type="password"
                value={password}
              />
            </div>
            <button type="submit">Sign in</button>
          </form>
        </>
      )
    }
    ```
  

  
    In the `(auth)` group, create a `sign-in.tsx` file with the following code. The [`useSignIn()`](/reference/hooks/use-sign-in) hook is used to create a sign-in flow. The user can sign in using email address and password, or navigate to the sign-up page.

```tsx
// Filename: app/(auth)/sign-in.tsx

import { ThemedText } from '@/components/themed-text'
import { ThemedView } from '@/components/themed-view'
import { useSignIn } from '@clerk/expo/legacy'
import type { EmailCodeFactor } from '@clerk/shared/types'
import { Link, useRouter } from 'expo-router'
import * as React from 'react'
import { Pressable, StyleSheet, TextInput, View } from 'react-native'

export default function Page() {
  const { signIn, setActive, isLoaded } = useSignIn()
  const router = useRouter()

  const [emailAddress, setEmailAddress] = React.useState('')
  const [password, setPassword] = React.useState('')
  const [code, setCode] = React.useState('')
  const [showEmailCode, setShowEmailCode] = React.useState(false)

  // Handle the submission of the sign-in form
  const onSignInPress = React.useCallback(async () => {
    if (!isLoaded) return

    // Start the sign-in process using the email and password provided
    try {
      const signInAttempt = await signIn.create({
        identifier: emailAddress,
        password,
      })

      // If sign-in process is complete, set the created session as active
      // and redirect the user
      if (signInAttempt.status === 'complete') {
        await setActive({
          session: signInAttempt.createdSessionId,
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
      } else if (signInAttempt.status === 'needs_second_factor') {
        // Check if email_code is a valid second factor
        // This is required when Client Trust is enabled and the user
        // is signing in from a new device.
        // See https://clerk.com/docs/guides/secure/client-trust
        const emailCodeFactor = signInAttempt.supportedSecondFactors?.find(
          (factor): factor is EmailCodeFactor => factor.strategy === 'email_code',
        )

        if (emailCodeFactor) {
          await signIn.prepareSecondFactor({
            strategy: 'email_code',
            emailAddressId: emailCodeFactor.emailAddressId,
          })
          setShowEmailCode(true)
        }
      } else {
        // If the status is not complete, check why. User may need to
        // complete further steps.
        console.error(JSON.stringify(signInAttempt, null, 2))
      }
    } catch (err) {
      // See https://clerk.com/docs/guides/development/custom-flows/error-handling
      // for more info on error handling
      console.error(JSON.stringify(err, null, 2))
    }
  }, [isLoaded, signIn, setActive, router, emailAddress, password])

  // Handle the submission of the email verification code
  const onVerifyPress = React.useCallback(async () => {
    if (!isLoaded) return

    try {
      const signInAttempt = await signIn.attemptSecondFactor({
        strategy: 'email_code',
        code,
      })

      if (signInAttempt.status === 'complete') {
        await setActive({
          session: signInAttempt.createdSessionId,
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
        console.error(JSON.stringify(signInAttempt, null, 2))
      }
    } catch (err) {
      console.error(JSON.stringify(err, null, 2))
    }
  }, [isLoaded, signIn, setActive, router, code])

  // Display email code verification form
  if (showEmailCode) {
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
    
      
        Sign in
      
      Email address
       setEmailAddress(emailAddress)}
        keyboardType="email-address"
      />
      Password
       setPassword(password)}
      />
       [
          styles.button,
          (!emailAddress || !password) && styles.buttonDisabled,
          pressed && styles.buttonPressed,
        ]}
        onPress={onSignInPress}
        disabled={!emailAddress || !password}
      >
        Sign in
      
      
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

  

  
    
**index.html:**

```html
<!-- Filename: index.html -->

      <!doctype html>
      <html lang="en">
        <head>
          <meta charset="UTF-8" />
          <meta name="viewport" content="width=device-width, initial-scale=1.0" />
          <title>Clerk + JavaScript App</title>
        </head>
        <body>
          <div id="signed-in"></div>

          <div id="sign-in">
            <h2>Sign in</h2>
            <form id="sign-in-form">
              <label for="email">Enter email address</label>
              <input name="email" id="sign-in-email" />
              <label for="password">Enter password</label>
              <input name="password" id="sign-in-password" />
              <button type="submit">Continue</button>
            </form>
          </div>

          <form id="email-code-form" hidden>
            <h2>Verify your email</h2>
            <p>A verification code has been sent to your email.</p>
            <label for="code">Enter verification code</label>
            <input id="code" name="code" />
            <button type="submit">Verify</button>
          </form>

          <script type="module" src="/src/main.js" async crossorigin="anonymous"></script>
        </body>
      </html>
      ```


**main.js:**

```js
// Filename: main.js

      import { Clerk } from '@clerk/clerk-js'

      const pubKey = import.meta.env.VITE_CLERK_PUBLISHABLE_KEY

      const clerk = new Clerk(pubKey)
      await clerk.load()

      if (clerk.isSignedIn) {
        // Mount user button component
        document.getElementById('signed-in').innerHTML = `
          <div id="user-button"></div>
        `

        const userbuttonDiv = document.getElementById('user-button')

        clerk.mountUserButton(userbuttonDiv)
      } else if (clerk.session?.currentTask) {
        // Handle pending session tasks
        // See https://clerk.com/docs/guides/development/custom-flows/authentication/session-tasks
        switch (clerk.session.currentTask.key) {
          case 'choose-organization': {
            document.getElementById('app').innerHTML = `
                  <div id="task"></div>
                `

            const taskDiv = document.getElementById('task')

            clerk.mountTaskChooseOrganization(taskDiv)
          }
        }
      } else {
        // Handle the sign-in form
        document.getElementById('sign-in-form').addEventListener('submit', async (e) => {
          e.preventDefault()

          const formData = new FormData(e.target)
          const emailAddress = formData.get('email')
          const password = formData.get('password')

          try {
            // Start the sign-in process
            const signInAttempt = await clerk.client.signIn.create({
              identifier: emailAddress,
              password,
            })

            // If the sign-in is complete, set the user as active
            if (signInAttempt.status === 'complete') {
              await clerk.setActive({ session: signInAttempt.createdSessionId })

              location.reload()
            } else if (signInAttempt.status === 'needs_second_factor') {
              // Check if email_code is a valid second factor
              // This is required when Client Trust is enabled and the user
              // is signing in from a new device.
              // See https://clerk.com/docs/guides/secure/client-trust
              const emailCodeFactor = signInAttempt.supportedSecondFactors?.find(
                (factor) => factor.strategy === 'email_code',
              )

              if (emailCodeFactor) {
                await clerk.client.signIn.prepareSecondFactor({
                  strategy: 'email_code',
                  emailAddressId: emailCodeFactor.emailAddressId,
                })

                // Hide sign-in form and show email code form
                document.getElementById('sign-in').setAttribute('hidden', '')
                document.getElementById('email-code-form').removeAttribute('hidden')
              }
            } else {
              // If the status is not complete, check why. User may need to
              // complete further steps.
              console.error(JSON.stringify(signInAttempt, null, 2))
            }
          } catch (error) {
            // See https://clerk.com/docs/guides/development/custom-flows/error-handling
            // for more info on error handling
            console.error(error)
          }
        })

        // Handle email code verification form
        document.getElementById('email-code-form').addEventListener('submit', async (e) => {
          e.preventDefault()

          const formData = new FormData(e.target)
          const code = formData.get('code')

          try {
            const signInAttempt = await clerk.client.signIn.attemptSecondFactor({
              strategy: 'email_code',
              code,
            })

            if (signInAttempt.status === 'complete') {
              await clerk.setActive({ session: signInAttempt.createdSessionId })

              location.reload()
            } else {
              console.error(JSON.stringify(signInAttempt, null, 2))
            }
          } catch (error) {
            console.error(error)
          }
        })
      }
      ```
