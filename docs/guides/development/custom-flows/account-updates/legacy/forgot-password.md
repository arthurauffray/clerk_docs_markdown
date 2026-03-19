# Build a custom flow for resetting a user's password


> Learn how to build a custom flow using Clerk's API to reset a user's password.

> [!WARNING]
> This guide is for users who want to build a custom flow. To use a _prebuilt_ UI, use the [Account Portal pages](/guides/account-portal/overview) or [prebuilt components](/reference/components/overview).


> [!IMPORTANT]
> This guide uses the Core 2 `useSignIn()` and `useSignUp()` hooks, which are available in Core 3 SDKs by adding the `/legacy` subpath to the import path. If you're using a Core 2 SDK, remove the `/legacy` subpath.


The password reset flow works as follows:

1. Users can have an email address or phone number, or both. The user enters their email address or phone number and asks for a password reset code.
1. Clerk sends an email or SMS to the user, containing a code.
1. The user enters the code and a new password.
1. Clerk verifies the code, and if successful, updates the user's password and signs them in.

This guide demonstrates how to use Clerk's API to build a custom flow for resetting a user's password. It covers the following scenarios:

- [The user has an email address as an identifier](#email-address)
- [The user has a phone number as an identifier](#phone-number)

## Email address


  
    > [!TIP]
> Examples for this SDK aren't available yet. For now, try adapting the  available example to fit your SDK.

  

  ```tsx
// Filename: app/forgot-password/page.tsx

  'use client'

  import React from 'react'
  import { useSignIn } from '@clerk/nextjs'
  import { useRouter } from 'next/navigation'

  export default function Page() {
    const { isLoaded, signIn, setActive } = useSignIn()
    const router = useRouter()

    const [email, setEmail] = React.useState('')
    const [password, setPassword] = React.useState('')
    const [code, setCode] = React.useState('')
    const [successfulCreation, setSuccessfulCreation] = React.useState(false)
    const [error, setError] = React.useState('')

    if (!isLoaded) return <p>Loading...</p>

    // Send the password reset code to the user's email
    async function create(e: React.FormEvent) {
      e.preventDefault()
      await signIn
        ?.create({
          strategy: 'reset_password_email_code',
          identifier: email,
        })
        .then((_) => {
          setSuccessfulCreation(true)
          setError('')
        })
        .catch((err) => {
          console.error('error', err.errors[0].longMessage)
          setError(err.errors[0].longMessage)
        })
    }

    // Reset the user's password.
    // Upon successful reset, the user will be
    // signed in and redirected to the home page
    async function reset(e: React.FormEvent) {
      e.preventDefault()
      await signIn
        ?.attemptFirstFactor({
          strategy: 'reset_password_email_code',
          code,
          password,
        })
        .then((result) => {
          if (result.status === 'needs_second_factor') {
            // See https://clerk.com/docs/guides/development/custom-flows/authentication/multi-factor-authentication
          } else if (result.status === 'complete') {
            // Set the active session to
            // the newly created session (user is now signed in)
            setActive({
              session: result.createdSessionId,
              navigate: async ({ session }) => {
                if (session?.currentTask) {
                  // Handle pending session tasks
                  // See https://clerk.com/docs/guides/development/custom-flows/authentication/session-tasks
                  console.log(session?.currentTask)
                  return
                }

                router.push('/')
              },
            })
            setError('')
          } else {
            console.log(result)
          }
        })
        .catch((err) => {
          console.error('error', err.errors[0].longMessage)
          setError(err.errors[0].longMessage)
        })
    }

    return (
      <div>
        <h1>Forgot Password?</h1>
        <form onSubmit={!successfulCreation ? create : reset}>
          {!successfulCreation && (
            <>
              <label htmlFor="email">Provide your email address</label>
              <input
                type="email"
                placeholder="e.g john@doe.com"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
              />

              <button>Send password reset code</button>
              {error && <p>{error}</p>}
            </>
          )}

          {successfulCreation && (
            <>
              <label htmlFor="password">Enter your new password</label>
              <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} />

              <label htmlFor="code">Enter the password reset code that was sent to your email</label>
              <input type="text" value={code} onChange={(e) => setCode(e.target.value)} />

              <button>Reset</button>
              {error && <p>{error}</p>}
            </>
          )}
        </form>
      </div>
    )
  }
  ```


  ```tsx
// Filename: app/(account)/forgot-password.tsx

  import { ThemedText } from '@/components/themed-text'
  import { ThemedView } from '@/components/themed-view'
  import { useSignIn } from '@clerk/clerk-expo'
  import { Redirect, useRouter } from 'expo-router'
  import React from 'react'
  import { Pressable, StyleSheet, TextInput, View } from 'react-native'

  export default function Page() {
    const { isLoaded, signIn, setActive } = useSignIn()
    const router = useRouter()

    const [email, setEmail] = React.useState('')
    const [password, setPassword] = React.useState('')
    const [code, setCode] = React.useState('')
    const [successfulCreation, setSuccessfulCreation] = React.useState(false)
    const [error, setError] = React.useState('')

    if (!isLoaded) {
      return (
        
          Loading...
        
      )
    }

    // Send the password reset code to the user's email
    async function create() {
      try {
        await signIn?.create({
          strategy: 'reset_password_email_code',
          identifier: email,
        })
        setSuccessfulCreation(true)
        setError('')
      } catch (err: any) {
        console.error('error', err.errors?.[0]?.longMessage)
        setError(err.errors?.[0]?.longMessage || 'An error occurred')
      }
    }

    // Reset the user's password.
    // Upon successful reset, the user will be
    // signed in and redirected to the home page
    async function reset() {
      try {
        const result = await signIn?.attemptFirstFactor({
          strategy: 'reset_password_email_code',
          code,
          password,
        })

        if (!result) return

        if (result.status === 'needs_second_factor') {
          // See https://clerk.com/docs/guides/development/custom-flows/authentication/multi-factor-authentication
        } else if (result.status === 'complete') {
          // Set the active session to
          // the newly created session (user is now signed in)
          await setActive?.({
            session: result.createdSessionId,
            navigate: async ({ session }) => {
              if (session?.currentTask) {
                // Handle pending session tasks
                // See https://clerk.com/docs/guides/development/custom-flows/authentication/session-tasks
                console.log(session?.currentTask)
                return
              }

              router.replace('/')
            },
          })
          setError('')
        } else {
          console.log(result)
        }
      } catch (err: any) {
        console.error('error', err.errors?.[0]?.longMessage)
        setError(err.errors?.[0]?.longMessage || 'An error occurred')
      }
    }

    return (
      
        
          Forgot Password?
        

        {!successfulCreation && (
          <>
            Provide your email address
             [
                styles.button,
                !email && styles.buttonDisabled,
                pressed && styles.buttonPressed,
              ]}
              onPress={create}
              disabled={!email}
            >
              Send password reset code
            

            {error && (
              
                {error}
              
            )}
          </>
        )}

        {successfulCreation && (
          <>
            
              A password reset code has been sent to your email
            

            Enter your new password
            Enter the password reset code
             [
                styles.button,
                (!password || !code) && styles.buttonDisabled,
                pressed && styles.buttonPressed,
              ]}
              onPress={reset}
              disabled={!password || !code}
            >
              Reset Password
            

            {error && (
              
                {error}
              
            )}
          </>
        )}
      
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
    errorContainer: {
      padding: 12,
      backgroundColor: '#ffebee',
      borderRadius: 8,
      marginTop: 8,
    },
    errorText: {
      color: '#c62828',
      fontWeight: '500',
    },
  })
  ```


## Phone number


  
    > [!TIP]
> Examples for this SDK aren't available yet. For now, try adapting the  available example to fit your SDK.

  

  ```tsx
// Filename: app/forgot-password/page.tsx

  'use client'

  import React from 'react'
  import { useSignIn } from '@clerk/nextjs'
  import { useRouter } from 'next/navigation'

  export default function Page() {
    const { isLoaded, signIn, setActive } = useSignIn()
    const router = useRouter()

    const [phoneNumber, setPhoneNumber] = React.useState('')
    const [password, setPassword] = React.useState('')
    const [code, setCode] = React.useState('')
    const [successfulCreation, setSuccessfulCreation] = React.useState(false)
    const [error, setError] = React.useState('')

    if (!isLoaded) return <p>Loading...</p>

    // Send the password reset code to the user's email
    async function create(e: React.FormEvent) {
      e.preventDefault()
      await signIn
        ?.create({
          strategy: 'reset_password_phone_code',
          identifier: phoneNumber,
        })
        .then((_) => {
          setSuccessfulCreation(true)
          setError('')
        })
        .catch((err) => {
          console.error('error', err.errors[0].longMessage)
          setError(err.errors[0].longMessage)
        })
    }

    // Reset the user's password.
    // Upon successful reset, the user will be
    // signed in and redirected to the home page
    async function reset(e: React.FormEvent) {
      e.preventDefault()
      await signIn
        ?.attemptFirstFactor({
          strategy: 'reset_password_phone_code',
          code,
          password,
        })
        .then((result) => {
          if (result.status === 'needs_second_factor') {
            // See https://clerk.com/docs/guides/development/custom-flows/authentication/multi-factor-authentication
          } else if (result.status === 'complete') {
            // Set the active session to
            // the newly created session (user is now signed in)
            setActive({
              session: result.createdSessionId,
              navigate: async ({ session }) => {
                if (session?.currentTask) {
                  // Handle pending session tasks
                  // See https://clerk.com/docs/guides/development/custom-flows/authentication/session-tasks
                  console.log(session?.currentTask)
                  return
                }

                router.push('/')
              },
            })
            setError('')
          } else {
            console.log(result)
          }
        })
        .catch((err) => {
          console.error('error', err.errors[0].longMessage)
          setError(err.errors[0].longMessage)
        })
    }

    return (
      <div>
        <h1>Forgot Password?</h1>
        <form onSubmit={!successfulCreation ? create : reset}>
          {!successfulCreation && (
            <>
              <label htmlFor="phoneNumber">Provide your phone number</label>
              <input
                type="tel"
                placeholder="e.g +1234567890"
                value={phoneNumber}
                onChange={(e) => setPhoneNumber(e.target.value)}
              />

              <button>Send password reset code</button>
              {error && <p>{error}</p>}
            </>
          )}

          {successfulCreation && (
            <>
              <label htmlFor="password">Enter your new password</label>
              <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} />

              <label htmlFor="code">
                Enter the password reset code that was sent to your phone number
              </label>
              <input type="text" value={code} onChange={(e) => setCode(e.target.value)} />

              <button>Reset</button>
              {error && <p>{error}</p>}
            </>
          )}
        </form>
      </div>
    )
  }
  ```


  ```tsx
// Filename: app/(account)/forgot-password.tsx

  import { ThemedText } from '@/components/themed-text'
  import { ThemedView } from '@/components/themed-view'
  import { useSignIn } from '@clerk/expo/legacy'
  import { useRouter } from 'expo-router'
  import React from 'react'
  import { Pressable, StyleSheet, TextInput, View } from 'react-native'

  export default function ForgotPasswordPage() {
    const { isLoaded, signIn, setActive } = useSignIn()
    const router = useRouter()

    const [phoneNumber, setPhoneNumber] = React.useState('')
    const [password, setPassword] = React.useState('')
    const [code, setCode] = React.useState('')
    const [successfulCreation, setSuccessfulCreation] = React.useState(false)
    const [error, setError] = React.useState('')

    if (!isLoaded) {
      return (
        
          Loading...
        
      )
    }

    // Send the password reset code to the user's phone
    async function create() {
      try {
        await signIn?.create({
          strategy: 'reset_password_phone_code',
          identifier: phoneNumber,
        })
        setSuccessfulCreation(true)
        setError('')
      } catch (err: any) {
        console.error('error', err.errors?.[0]?.longMessage)
        setError(err.errors?.[0]?.longMessage || 'An error occurred')
      }
    }

    // Reset the user's password.
    // Upon successful reset, the user will be
    // signed in and redirected to the home page
    async function reset() {
      try {
        const result = await signIn?.attemptFirstFactor({
          strategy: 'reset_password_phone_code',
          code,
          password,
        })

        if (!result) return

        if (result.status === 'needs_second_factor') {
          // See https://clerk.com/docs/guides/development/custom-flows/authentication/multi-factor-authentication
        } else if (result.status === 'complete') {
          // Set the active session to
          // the newly created session (user is now signed in)
          await setActive?.({
            session: result.createdSessionId,
            navigate: async ({ session }) => {
              if (session?.currentTask) {
                // Handle pending session tasks
                // See https://clerk.com/docs/guides/development/custom-flows/authentication/session-tasks
                console.log(session?.currentTask)
                return
              }

              router.replace('/')
            },
          })
          setError('')
        } else {
          console.log(result)
        }
      } catch (err: any) {
        console.error('error', err.errors?.[0]?.longMessage)
        setError(err.errors?.[0]?.longMessage || 'An error occurred')
      }
    }

    return (
      
        
          Forgot Password?
        

        {!successfulCreation && (
          <>
            Provide your phone number
             [
                styles.button,
                !phoneNumber && styles.buttonDisabled,
                pressed && styles.buttonPressed,
              ]}
              onPress={create}
              disabled={!phoneNumber}
            >
              Send password reset code
            

            {error && (
              
                {error}
              
            )}
          </>
        )}

        {successfulCreation && (
          <>
            
              A password reset code has been sent to your phone
            

            Enter your new password
            Enter the password reset code
             [
                styles.button,
                (!password || !code) && styles.buttonDisabled,
                pressed && styles.buttonPressed,
              ]}
              onPress={reset}
              disabled={!password || !code}
            >
              Reset Password
            

            {error && (
              
                {error}
              
            )}
          </>
        )}
      
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
    errorContainer: {
      padding: 12,
      backgroundColor: '#ffebee',
      borderRadius: 8,
      marginTop: 8,
    },
    errorText: {
      color: '#c62828',
      fontWeight: '500',
    },
  })
  ```


## Handle compromised passwords

If you have enabled the [**Reject compromised passwords**](/guides/secure/password-protection-and-rules#reject-compromised-passwords) setting, sign-up/sign-in and password update attempts will be rejected with an error if the password is compromised.

### User is trying to set a compromised password

If the user is trying to set a password that is compromised, the attempt will receive an HTTP status of `422 (Unprocessable Entity)` and the `form_password_pwned` error code.

```json
{
  "errors": [
    {
      "shortMessage": "Password has been found in an online data breach. For account safety, please <action>.",
      "code": "form_password_pwned",
      "meta": {
        "name": "param"
      }
    }
  ]
}
```

In this case, the user just needs to be prompted to use a different password. For example, you can add text to the form with the error's message so that the user can try again.

### User's password has been marked as compromised

> [!WARNING]
> If your instance is older than December 18, 2025, you will need to update your instance to the **Reset password session task** update.


If you have [manually marked a user's password as compromised](/guides/secure/password-protection-and-rules#manually-set-a-password-as-compromised), and the user tries authenticating with it, the sign-up/sign-in attempt will receive an HTTP status of `422 (Unprocessable Entity)` and the `form_password_compromised` error code.

```json
{
  "errors": [
    {
      "long_message": "Your password may be compromised. To protect your account, please continue with an alternative sign-in method. You will be required to reset your password after signing in.",
      "code": "form_password_compromised",
      "meta": {
        "name": "param"
      }
    }
  ]
}
```

The user will not be able to authenticate with their compromised password, so you should:

1. Update your sign-up or sign-in flow to prompt them to authenticate with another method, such as an email address (so they can use email OTP or email link), or a phone number (so they can use an SMS OTP). Once they authenticate with another method, their session will enter a `pending` state until they reset their password. If they do not have any other identification methods, e.g if they only have username and password, they will be authenticated but their session will enter a `pending` state until they reset their password.
1. Handle the `reset-password` session task so the user can reset their password and their session can be updated from `pending` to `active`.


  #### Update your sign-up/sign-in flow

  To update your sign-up/sign-in flow, you can check for the error code and then prompt the user to authenticate with another method. This example uses the [email/password custom flow](/guides/development/custom-flows/authentication/email-password) but adds code that prompts the user to authenticate with an email code when their password is compromised. You can use the same approach with other custom flows.

  
    
      > [!TIP]
> Examples for this SDK aren't available yet. For now, try adapting the  available example to fit your SDK.

    

    ```tsx
// Filename: app/sign-in/page.tsx

    'use client'

    import * as React from 'react'
    import { useSignIn } from '@clerk/nextjs'
    import { useRouter } from 'next/navigation'
    import { ClerkAPIError, EmailCodeFactor, SignInFirstFactor } from '@clerk/shared/types'
    import { isClerkAPIResponseError } from '@clerk/nextjs/errors'

    const SignInWithEmailCode = () => {
      const { isLoaded, signIn, setActive } = useSignIn()
      const router = useRouter()

      const [verifying, setVerifying] = React.useState(false)
      const [email, setEmail] = React.useState('')
      const [code, setCode] = React.useState('')

      async function handleSubmit(e: React.FormEvent) {
        e.preventDefault()

        if (!isLoaded && !signIn) return null

        try {
          // Start the sign-in process using the email code method
          const { supportedFirstFactors } = await signIn.create({
            identifier: email,
          })

          // Filter the returned array to find the 'email_code' entry
          const isEmailCodeFactor = (factor: SignInFirstFactor): factor is EmailCodeFactor => {
            return factor.strategy === 'email_code'
          }
          const emailCodeFactor = supportedFirstFactors?.find(isEmailCodeFactor)

          if (emailCodeFactor) {
            // Grab the emailAddressId
            const { emailAddressId } = emailCodeFactor

            // Send the OTP code to the user
            await signIn.prepareFirstFactor({
              strategy: 'email_code',
              emailAddressId,
            })

            // Set verifying to true to display second form
            // and capture the OTP code
            setVerifying(true)
          }
        } catch (err) {
          // See https://clerk.com/docs/guides/development/custom-flows/error-handling
          // for more info on error handling
          console.error('Error:', JSON.stringify(err, null, 2))
        }
      }

      async function handleVerification(e: React.FormEvent) {
        e.preventDefault()

        if (!isLoaded && !signIn) return null

        try {
          // Use the code provided by the user and attempt verification
          const signInAttempt = await signIn.attemptFirstFactor({
            strategy: 'email_code',
            code,
          })

          // If verification was completed, set the session to active
          // and redirect the user
          if (signInAttempt.status === 'complete') {
            await setActive({
              session: signInAttempt.createdSessionId,
              navigate: async ({ session }) => {
                if (session?.currentTask) {
                  // Handle pending session tasks
                  // See https://clerk.com/docs/guides/development/custom-flows/authentication/session-tasks
                  console.log(session?.currentTask)
                  return
                }

                router.push('/')
              },
            })
          } else {
            // If the status is not complete, check why. User may need to
            // complete further steps.
            console.error(signInAttempt)
          }
        } catch (err) {
          // See https://clerk.com/docs/guides/development/custom-flows/error-handling
          // for more info on error handling
          console.error('Error:', JSON.stringify(err, null, 2))
        }
      }

      if (verifying) {
        return (
          <>
            <h1>Verify your email address</h1>
            <form onSubmit={handleVerification}>
              <label htmlFor="code">Enter your email verification code</label>
              <input value={code} id="code" name="code" onChange={(e) => setCode(e.target.value)} />
              <button type="submit">Verify</button>
            </form>
          </>
        )
      }

      return (
        <>
          <form onSubmit={handleSubmit}>
            <label htmlFor="email">Enter email address</label>
            <input
              value={email}
              id="email"
              name="email"
              type="email"
              onChange={(e) => setEmail(e.target.value)}
            />
            <button type="submit">Continue</button>
          </form>
        </>
      )
    }

    export default function SignInForm() {
      const { isLoaded, signIn, setActive } = useSignIn()
      const router = useRouter()

      const [email, setEmail] = React.useState('')
      const [password, setPassword] = React.useState('')
      const [errors, setErrors] = React.useState()

      // Handle the submission of the sign-in form
      const handleSignInWithPassword = async (e: React.FormEvent) => {
        e.preventDefault()

        // Clear any errors that may have occurred during previous form submission
        setErrors(undefined)

        if (!isLoaded) {
          return
        }

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
              navigate: async ({ session }) => {
                if (session?.currentTask) {
                  // Handle pending session tasks
                  // See https://clerk.com/docs/guides/development/custom-flows/authentication/session-tasks
                  console.log(session?.currentTask)
                  return
                }

                router.push('/')
              },
            })
          } else {
            // If the status is not complete, check why. User may need to
            // complete further steps.
            console.error(JSON.stringify(signInAttempt, null, 2))
          }
        } catch (err) {
          if (isClerkAPIResponseError(err)) setErrors(err.errors)
          console.error(JSON.stringify(err, null, 2))
        }
      }

      if (errors && errors[0].code === 'form_password_compromised') {
        return (
          <>
            <h1>Sign in</h1>

            <p>
              Your password appears to have been compromised or it&apos;s no longer trusted and cannot
              be used. Please use email code to continue.
            </p>

            </>
        )
      }

      // Display a form to capture the user's email and password
      return (
        <>
          <h1>Sign in</h1>

          <form onSubmit={(e) => handleSignInWithPassword(e)}>
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

          {errors && (
            <ul>
              {errors.map((el, index) => (
                <li key={index}>{el.longMessage}</li>
              ))}
            </ul>
          )}
        </>
      )
    }
    ```
  

  
    ```tsx
// Filename: app/(auth)/sign-in.tsx

    import { ThemedText } from '@/components/themed-text'
    import { ThemedView } from '@/components/themed-view'
    import { isClerkAPIResponseError, useSignIn } from '@clerk/clerk-expo'
    import { ClerkAPIError, EmailCodeFactor, SignInFirstFactor } from '@clerk/shared/types'
    import { Link, useRouter } from 'expo-router'
    import * as React from 'react'
    import { Pressable, StyleSheet, TextInput, View } from 'react-native'

    const SignInWithEmailCode = () => {
      const { isLoaded, signIn, setActive } = useSignIn()
      const router = useRouter()

      const [verifying, setVerifying] = React.useState(false)
      const [email, setEmail] = React.useState('')
      const [code, setCode] = React.useState('')

      async function handleSubmit() {
        if (!isLoaded && !signIn) return

        try {
          // Start the sign-in process using the email code method
          const { supportedFirstFactors } = await signIn.create({
            identifier: email,
          })

          // Filter the returned array to find the 'email_code' entry
          const isEmailCodeFactor = (factor: SignInFirstFactor): factor is EmailCodeFactor => {
            return factor.strategy === 'email_code'
          }
          const emailCodeFactor = supportedFirstFactors?.find(isEmailCodeFactor)

          if (emailCodeFactor) {
            // Grab the emailAddressId
            const { emailAddressId } = emailCodeFactor

            // Send the OTP code to the user
            await signIn.prepareFirstFactor({
              strategy: 'email_code',
              emailAddressId,
            })

            // Set verifying to true to display second form
            // and capture the OTP code
            setVerifying(true)
          }
        } catch (err) {
          // See https://clerk.com/docs/guides/development/custom-flows/error-handling
          // for more info on error handling
          console.error('Error:', JSON.stringify(err, null, 2))
        }
      }

      async function handleVerification() {
        if (!isLoaded && !signIn) return

        try {
          // Use the code provided by the user and attempt verification
          const signInAttempt = await signIn.attemptFirstFactor({
            strategy: 'email_code',
            code,
          })

          // If verification was completed, set the session to active
          // and redirect the user
          if (signInAttempt.status === 'complete') {
            await setActive({
              session: signInAttempt.createdSessionId,
              navigate: async ({ session }) => {
                if (session?.currentTask) {
                  // Handle pending session tasks
                  // See https://clerk.com/docs/guides/development/custom-flows/authentication/session-tasks
                  console.log(session?.currentTask)
                  return
                }

                router.replace('/')
              },
            })
          } else {
            // If the status is not complete, check why. User may need to
            // complete further steps.
            console.error(signInAttempt)
          }
        } catch (err) {
          // See https://clerk.com/docs/guides/development/custom-flows/error-handling
          // for more info on error handling
          console.error('Error:', JSON.stringify(err, null, 2))
        }
      }

      if (verifying) {
        return (
          
            
              Verify your email address
            
            Enter your email verification code
             [styles.button, pressed && styles.buttonPressed]}
              onPress={handleVerification}
            >
              Verify
            
          
        )
      }

      return (
        
          Enter email address
           [
              styles.button,
              !email && styles.buttonDisabled,
              pressed && styles.buttonPressed,
            ]}
            onPress={handleSubmit}
            disabled={!email}
          >
            Continue
          
        
      )
    }

    export default function SignInForm() {
      const { isLoaded, signIn, setActive } = useSignIn()
      const router = useRouter()

      const [email, setEmail] = React.useState('')
      const [password, setPassword] = React.useState('')
      const [errors, setErrors] = React.useState()

      // Handle the submission of the sign-in form
      const handleSignInWithPassword = async () => {
        // Clear any errors that may have occurred during previous form submission
        setErrors(undefined)

        if (!isLoaded) {
          return
        }

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
              navigate: async ({ session }) => {
                if (session?.currentTask) {
                  // Handle pending session tasks
                  // See https://clerk.com/docs/guides/development/custom-flows/authentication/session-tasks
                  console.log(session?.currentTask)
                  return
                }

                router.replace('/')
              },
            })
          } else {
            // If the status is not complete, check why. User may need to
            // complete further steps.
            console.error(JSON.stringify(signInAttempt, null, 2))
          }
        } catch (err) {
          if (isClerkAPIResponseError(err)) setErrors(err.errors)
          console.error(JSON.stringify(err, null, 2))
        }
      }

      if (errors && errors[0].code === 'form_password_compromised') {
        return (
          
            
              Sign in
            

            
              
                Your password appears to have been compromised or it's no longer trusted and cannot be
                used. Please use email code to continue.
              
            

            
        )
      }

      // Display a form to capture the user's email and password
      return (
        
          
            Sign in
          

          Email address
          Password
           [
              styles.button,
              (!email || !password) && styles.buttonDisabled,
              pressed && styles.buttonPressed,
            ]}
            onPress={handleSignInWithPassword}
            disabled={!email || !password}
          >
            Sign in
          

          {errors && (
            
              {errors.map((el, index) => (
                
                  • {el.longMessage}
                
              ))}
            
          )}

          
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
      errorContainer: {
        padding: 12,
        backgroundColor: '#ffebee',
        borderRadius: 8,
        marginTop: 8,
        gap: 4,
      },
      errorText: {
        color: '#c62828',
        fontWeight: '500',
        fontSize: 14,
      },
      warningContainer: {
        padding: 12,
        backgroundColor: '#fff3e0',
        borderRadius: 8,
        marginBottom: 16,
      },
      warningText: {
        color: '#e65100',
        fontWeight: '500',
        fontSize: 14,
      },
      linkContainer: {
        flexDirection: 'row',
        gap: 4,
        marginTop: 12,
        alignItems: 'center',
      },
    })
    ```
  

  #### Handle the `reset-password` session task

  Once a user has authenticated, their password is still considered compromised. The `reset-password` session task will cause the user's session to be in a `pending` state until they reset their password.

  1. First, you need to tell your app where to redirect users when they have pending session tasks.
     The `taskUrls` option allows you to specify custom URL paths where users are redirected after sign-up or sign-in when specific session tasks need to be completed.


  Configure the `taskUrls` option on the [``](/reference/components/clerk-provider) component.

  ```tsx
  
    {children}
  
  ```


  Configure the `taskUrls` option on the [`clerk()`](/reference/astro/overview) integration.

  ```js
// Filename: astro.config.mjs

  import { defineConfig } from 'astro/config'
  import node from '@astrojs/node'
  import clerk from '@clerk/astro'

  export default defineConfig({
    integrations: [
      clerk({
        taskUrls: {
          'choose-organization': '/session-tasks/choose-organization',
          'reset-password': '/session-tasks/reset-password',
        },
      }),
    ],
    adapter: node({ mode: 'standalone' }),
    output: 'server',
  })
  ```


  Configure the `taskUrls` option on the [`clerk.load()`](/reference/javascript/clerk#load) method.

  ```js
// Filename: main.ts

  import { Clerk } from '@clerk/clerk-js'

  const clerkPubKey = import.meta.env.VITE_CLERK_PUBLISHABLE_KEY

  const clerk = new Clerk(clerkPubKey)
  await clerk.load({
    taskUrls: {
      'choose-organization': '/session-tasks/choose-organization',
      'reset-password': '/session-tasks/reset-password',
    },
  })
  ```


  Configure the `taskUrls` option on the [`clerkPlugin()`](/reference/vue/overview) integration.

  ```ts
// Filename: src/main.ts

  import { createApp } from 'vue'
  import './styles.css'
  import App from './App.vue'
  import { clerkPlugin } from '@clerk/vue'

  const PUBLISHABLE_KEY = import.meta.env.VITE_CLERK_PUBLISHABLE_KEY

  if (!PUBLISHABLE_KEY) {
    throw new Error('Add your Clerk publishable key to the .env.local file')
  }

  const app = createApp(App)
  app.use(clerkPlugin, {
    publishableKey: PUBLISHABLE_KEY,
    taskUrls: {
      'choose-organization': '/session-tasks/choose-organization',
      'reset-password': '/session-tasks/reset-password',
    },
  })
  app.mount('#app')
  ```


  Configure the `taskUrls` option on the [`defineNuxtConfig()`](/reference/nuxt/clerk-middleware) integration.

  ```ts
// Filename: nuxt.config.ts

  export default defineNuxtConfig({
    compatibilityDate: '2025-07-15',
    devtools: { enabled: true },
    modules: ['@clerk/nuxt'],
    clerk: {
      taskUrls: {
        'choose-organization': '/session-tasks/choose-organization',
        'reset-password': '/session-tasks/reset-password',
      },
    },
  })
  ```


  Configure the `taskUrls` option on the [`clerkPlugin()`](/reference/fastify/clerk-plugin) integration.

  ```ts
// Filename: src/main.ts

  import Fastify from 'fastify'
  import { clerkPlugin } from '@clerk/fastify'

  const fastify = Fastify({ logger: true })

  fastify.register(clerkPlugin, {
    taskUrls: {
      'choose-organization': '/session-tasks/choose-organization',
      'reset-password': '/session-tasks/reset-password',
    },
  })
  ```


  1. Now, the user will be redirected to the URL you've set with the `taskUrls` option. This page is where you will add the forgot/reset password code, such as the [reset user's password with an email address](#email-address) example from the previous section.
  1. What if your user exits the authentication or session task flow before completing their tasks and doesn't know how to get to the appropriate page to complete their session tasks? What if your user is navigating through your app as a `pending` user and can't figure out why they can't access certain content? If a user's authentication or session task flow is interrupted and they aren't able to complete the tasks, you can use the [``](/reference/components/control/redirect-to-tasks) component to redirect them to the appropriate task page so they can complete the tasks and move their session to an `active` (signed-in) state. This component will redirect users based on the URL's you've set with the `taskUrls` option.
     
  In the following example, the `` component is used to protect a page. Users can't access this page until they complete their pending session tasks. You can also wrap your entire application in the `` component, or place it in your application's layout file, so that users can't access **any** of your app until they complete their pending session tasks.


  In the following example, the `` component is used in the app's layout file so that users can't access **any** of the app until they complete their pending session tasks. However, you can also use the `` component to protect a single page or route group.

  ```tsx
// Filename: app/layout.tsx

  import { RedirectToTasks } from '@clerk/nextjs'

  export default function Layout({ children }: { children: React.ReactNode }) {
    return (
      <>
        {children}
      </>
    )
  }
  ```


  ```tsx
// Filename: pages/index.tsx

  import { RedirectToTasks } from '@clerk/react'

  export default function Page() {
    return }
  ```


  ```tsx
// Filename: app/routes/home.tsx

  import { RedirectToTasks } from '@clerk/react-router'

  export default function Home() {
    return }
  ```


  > [!NOTE]
  > This component relies on React Router for navigation. Ensure that you have integrated React Router into your Chrome Extension application before using it. [Learn how to add React Router to your Chrome Extension](/guides/development/add-react-router).

  ```jsx
// Filename: src/routes/home.tsx

  import { RedirectToTasks } from '@clerk/chrome-extension'

  export default function Home() {
    return }
  ```


  ```tsx
// Filename: app/routes/index.tsx

  import { RedirectToTasks } from '@clerk/tanstack-react-start'
  import { createFileRoute } from '@tanstack/react-router'

  export const Route = createFileRoute('/')({
    component: Home,
  })

  function Home() {
    return }
  ```


  ```vue
// Filename: App.vue

  <script setup lang="ts">
  import { RedirectToTasks } from '@clerk/vue'
  </script>

  <template>
    </template>
  ```


  ```vue
// Filename: App.vue

  <script setup lang="ts">
  // Components are automatically imported
  </script>

  <template>
    </template>
  ```


  This component is not available for your SDK. Please choose a different SDK.
