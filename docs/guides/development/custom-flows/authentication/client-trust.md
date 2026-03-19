# Build a custom sign-in flow with client trust


> Learn how to build a custom sign-in flow that requires Client Trust.

> [!WARNING]
> This guide is for users who want to build a custom flow. To use a _prebuilt_ UI, use the [Account Portal pages](/guides/account-portal/overview) or [prebuilt components](/reference/components/overview).


  > [!IMPORTANT]
  > This guide applies to the following Clerk SDKs:
  >
  > - `@clerk/react` v6 or higher
  > - `@clerk/nextjs` v7 or higher
  > - `@clerk/expo` v3 or higher
  > - `@clerk/react-router` v3 or higher
  > - `@clerk/tanstack-react-start` v0.26.0 or higher
  >
  > If you're using an older version of one of these SDKs, or are using the legacy API, refer to the [legacy API documentation](/guides/development/custom-flows/authentication/legacy/email-password-mfa).


If you have [Client Trust](/guides/secure/client-trust) enabled for your application, when a user is signing in **with a password** on a new client (e.g. device), **the sign-in attempt will return a status of `needs_second_factor`**. Your custom sign-in flow needs to support handling either an email code or SMS code, depending on the settings you've enabled in the Clerk Dashboard.

If Client Trust **and** MFA are enabled, MFA will take precedence and the sign-in attempt will return a status of `needs_second_factor`. See the [MFA custom flow guide](/guides/development/custom-flows/authentication/multi-factor-authentication) for more information.


#### Email code


    ### Configure application settings

    **This example uses the [email and password sign-in custom flow](/guides/development/custom-flows/authentication/email-password) as a base. However, you can modify this approach according to the settings you've configured for your application's instance in the Clerk Dashboard.**

    

    1. In the Clerk Dashboard, navigate to the [**User & authentication**](https://dashboard.clerk.com/~/user-authentication/user-and-authentication) page.
    1. Enable **Sign-up with email**.
       - **Require email address** should be enabled.
       - For **Verify at sign-up**, **Email verification code** is enabled by default. This is the option you'll want for this example.
    1. Enable **Sign in with email**.
    1. Select the **Password** tab and enable **Sign-up with password**.

    ### Build the custom flow

    
      
        > [!TIP]
> Examples for this SDK aren't available yet. For now, try adapting the  available example to fit your SDK.

      

      ```tsx
// Filename: app/sign-in/page.tsx

        'use client'

        import { useSignIn } from '@clerk/nextjs'
        import { useRouter } from 'next/navigation'

        export default function Page() {
          const { signIn, errors, fetchStatus } = useSignIn()
          const router = useRouter()

          const handleSubmit = async (formData: FormData) => {
            const emailAddress = formData.get('email') as string
            const password = formData.get('password') as string

            await signIn.password({
              emailAddress,
              password,
            })

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
                    router.push(url)
                  }
                },
              })
            } else if (signIn.status === 'needs_second_factor') {
              // See https://clerk.com/docs/guides/development/custom-flows/authentication/multi-factor-authentication
      +     } else if (signIn.status === 'needs_client_trust') {
      +       const emailCodeFactor = signIn.supportedSecondFactors.find(
      +         (factor) => factor.strategy === 'email_code',
      +       )
      + 
      +       if (emailCodeFactor) {
      +         await signIn.mfa.sendEmailCode()
      +       }
            } else {
              // Check why the sign-in is not complete
              console.error('Sign-in attempt not complete:', signIn)
            }
          }

          const handleVerify = async (formData: FormData) => {
            const code = formData.get('code') as string

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
                    router.push(url)
                  }
                },
              })
            }
          }

      +   if (signIn.status === 'needs_client_trust') {
      +     return (
      +       <>
      +         <h1>Verify your account</h1>
      +         <form action={handleVerify}>
      +           <div>
      +             <label htmlFor="code">Code</label>
      +             <input id="code" name="code" type="text" />
      +             {errors.fields.code && <p>{errors.fields.code.message}</p>}
      +           </div>
      +           <button type="submit" disabled={fetchStatus === 'fetching'}>
      +             Verify
      +           </button>
      +         </form>
      +         <button onClick={() => signIn.mfa.sendEmailCode()}>I need a new code</button>
      +         <button onClick={() => signIn.reset()}>Start over</button>
      +         
      +         {errors && <p>{JSON.stringify(errors, null, 2)}</p>}
      +       </>
      +     )
      +   }

          return (
            <>
              <h1>Sign in</h1>
              <form action={handleSubmit}>
                <div>
                  <label htmlFor="email">Enter email address</label>
                  <input id="email" name="email" type="email" />
                  {errors.fields.identifier && <p>{errors.fields.identifier.message}</p>}
                </div>
                <div>
                  <label htmlFor="password">Enter password</label>
                  <input id="password" name="password" type="password" />
                  {errors.fields.password && <p>{errors.fields.password.message}</p>}
                </div>
                <button type="submit" disabled={fetchStatus === 'fetching'}>
                  Continue
                </button>
              </form>
              
              {errors && <p>{JSON.stringify(errors, null, 2)}</p>}
            </>
          )
        }
      ```
    

    
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
      +     } else if (signIn.status === 'needs_client_trust') {
      +       const emailCodeFactor = signIn.supportedSecondFactors.find(
      +         (factor) => factor.strategy === 'email_code',
      +       )
      + 
      +       if (emailCodeFactor) {
      +         await signIn.mfa.sendEmailCode()
      +       }
            } else {
              // Check why the sign-in is not complete
              console.error('Sign-in attempt not complete:', signIn)
            }
          }

      +   const handleVerify = async () => {
      +     await signIn.mfa.verifyEmailCode({ code })
      + 
      +     if (signIn.status === 'complete') {
      +       await signIn.finalize({
      +         navigate: ({ session, decorateUrl }) => {
      +           if (session?.currentTask) {
      +             // Handle pending session tasks
      +             // See https://clerk.com/docs/guides/development/custom-flows/authentication/session-tasks
      +             console.log(session?.currentTask)
      +             return
      +           }
      + 
      +           const url = decorateUrl('/')
      +           if (url.startsWith('http')) {
      +             window.location.href = url
      +           } else {
      +             router.push(url as Href)
      +           }
      +         },
      +       })
      +     } else {
      +       // Check why the sign-in is not complete
      +       console.error('Sign-in attempt not complete:', signIn)
      +     }
      +   }

      +   if (signIn.status === 'needs_client_trust') {
      +     return (
      +       
      +         
      +           Verify your account
      +         
      +          setCode(code)}
      +           keyboardType="numeric"
      +         />
      +         {errors.fields.code && (
      +           {errors.fields.code.message}
      +         )}
      +          [
      +             styles.button,
      +             fetchStatus === 'fetching' && styles.buttonDisabled,
      +             pressed && styles.buttonPressed,
      +           ]}
      +           onPress={handleVerify}
      +           disabled={fetchStatus === 'fetching'}
      +         >
      +           Verify
      +         
      +          [styles.secondaryButton, pressed && styles.buttonPressed]}
      +           onPress={() => signIn.mfa.sendEmailCode()}
      +         >
      +           I need a new code
      +         
      +       
      +     )
      +   }

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
    
  

#### SMS code


    ### Configure application settings

    Client Trust will fallback to SMS verification code **only if email is completely disabled for the application**, or else Client Trust will fallback to either email code or email link, depending on your application's settings.

    **This example uses the [SMS OTP custom flow](/guides/development/custom-flows/authentication/email-sms-otp) as a base. However, you can modify this approach according to the settings you've configured for your application's instance in the Clerk Dashboard.**

    

    1. In the Clerk Dashboard, navigate to the [**User & authentication**](https://dashboard.clerk.com/~/user-authentication/user-and-authentication) page.
    1. Ensure all email options are disabled.
    1. Select the **Phone** tab. Ensure all the settings are enabled.
    1. Select the **Password** tab and enable **Sign-up with password**. **Client Trust** is enabled by default.

    ### Build the custom flow

    
      
        > [!TIP]
> Examples for this SDK aren't available yet. For now, try adapting the  available example to fit your SDK.

      

      ```tsx
// Filename: app/sign-in/page.tsx

        'use client'

        import { useSignIn } from '@clerk/nextjs'
        import { PhoneCodeFactor } from '@clerk/nextjs/types'
        import { useRouter } from 'next/navigation'

        export default function Page() {
          const { signIn, errors, fetchStatus } = useSignIn()
          const router = useRouter()

          const handleSubmit = async (formData: FormData) => {
            const phoneNumber = formData.get('phoneNumber') as string
            const password = formData.get('password') as string

            await signIn.password({
              phoneNumber,
              password,
            })

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
                    router.push(url)
                  }
                },
              })
            } else if (signIn.status === 'needs_second_factor') {
              // See https://clerk.com/docs/guides/development/custom-flows/authentication/multi-factor-authentication
      +     } else if (signIn.status === 'needs_client_trust') {
      +       const phoneCodeFactor = signIn.supportedSecondFactors.find(
      +         (factor): factor is PhoneCodeFactor => factor.strategy === 'phone_code',
      +       )
      + 
      +       if (phoneCodeFactor) {
      +         await signIn.mfa.sendPhoneCode()
      +       }
            } else {
              // Check why the sign-in is not complete
              console.error('Sign-in attempt not complete:', signIn)
            }
          }

          const handleVerify = async (formData: FormData) => {
            const code = formData.get('code') as string

            await signIn.mfa.verifyPhoneCode({ code })

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
                    router.push(url)
                  }
                },
              })
            }
          }

      +   if (signIn.status === 'needs_client_trust') {
      +     return (
      +       <>
      +         <h1>Verify your account</h1>
      +         <form action={handleVerify}>
      +           <div>
      +             <label htmlFor="code">Code</label>
      +             <input id="code" name="code" type="text" />
      +             {errors.fields.code && <p>{errors.fields.code.message}</p>}
      +           </div>
      +           <button type="submit" disabled={fetchStatus === 'fetching'}>
      +             Verify
      +           </button>
      +         </form>
      +         <button onClick={() => signIn.mfa.sendPhoneCode()}>I need a new code</button>
      +         <button onClick={() => signIn.reset()}>Start over</button>
      +         
      +         {errors && <p>{JSON.stringify(errors, null, 2)}</p>}
      +       </>
      +     )
      +   }

          return (
            <>
              <h1>Sign in</h1>
              <form action={handleSubmit}>
                <div>
                  <label htmlFor="phoneNumber">Enter phone number</label>
                  <input id="phoneNumber" name="phoneNumber" type="tel" />
                  {errors.fields.identifier && <p>{errors.fields.identifier.message}</p>}
                </div>
                <div>
                  <label htmlFor="password">Enter password</label>
                  <input id="password" name="password" type="password" />
                  {errors.fields.password && <p>{errors.fields.password.message}</p>}
                </div>
                <button type="submit" disabled={fetchStatus === 'fetching'}>
                  Continue
                </button>
              </form>
              
              {errors && <p>{JSON.stringify(errors, null, 2)}</p>}
            </>
          )
        }
      ```
    

    
      ```tsx
// Filename: app/(auth)/sign-in.tsx

        import { ThemedText } from '@/components/themed-text'
        import { ThemedView } from '@/components/themed-view'
        import { Colors } from '@/constants/theme'
        import { useColorScheme } from '@/hooks/use-color-scheme'
        import { useSignIn } from '@clerk/expo'
        import { type Href, useRouter } from 'expo-router'
        import React from 'react'
        import { Pressable, StyleSheet, TextInput } from 'react-native'

        export default function Page() {
          const { signIn, errors, fetchStatus } = useSignIn()
          const router = useRouter()
          const colorScheme = useColorScheme() ?? 'light'
          const themeColors = Colors[colorScheme]

          const [phoneNumber, setPhoneNumber] = React.useState('')
          const [password, setPassword] = React.useState('')
          const [code, setCode] = React.useState('')

          const handleSubmit = async () => {
            await signIn.password({
              phoneNumber,
              password,
            })

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
      +     } else if (signIn.status === 'needs_client_trust') {
      +       const phoneCodeFactor = signIn.supportedSecondFactors.find(
      +         (factor): factor is PhoneCodeFactor => factor.strategy === 'phone_code',
      +       )
      + 
      +       if (phoneCodeFactor) {
      +         await signIn.mfa.sendPhoneCode()
      +       }
            } else {
              // Check why the sign-in is not complete
              console.error('Sign-in attempt not complete:', signIn)
            }
          }

      +   const handleVerify = async () => {
      +     await signIn.mfa.verifyPhoneCode({ code })
      + 
      +     if (signIn.status === 'complete') {
      +       await signIn.finalize({
      +         navigate: ({ session, decorateUrl }) => {
      +           if (session?.currentTask) {
      +             // Handle pending session tasks
      +             // See https://clerk.com/docs/guides/development/custom-flows/authentication/session-tasks
      +             console.log(session?.currentTask)
      +             return
      +           }
      + 
      +           const url = decorateUrl('/')
      +           if (url.startsWith('http')) {
      +             window.location.href = url
      +           } else {
      +             router.push(url as Href)
      +           }
      +         },
      +       })
      +     } else {
      +       // Check why the sign-in is not complete
      +       console.error('Sign-in attempt not complete:', signIn)
      +     }
      +   }

      +   if (signIn.status === 'needs_client_trust') {
      +     return (
      +       
      +         
      +           Verify your account
      +         
      +         Code
      +          setCode(code)}
      +           keyboardType="numeric"
      +         />
      +         {errors.fields.code && (
      +           {errors.fields.code.message}
      +         )}
      +          [
      +             styles.button,
      +             fetchStatus === 'fetching' && styles.buttonDisabled,
      +             pressed && styles.buttonPressed,
      +           ]}
      +           onPress={handleVerify}
      +           disabled={fetchStatus === 'fetching'}
      +         >
      +           Verify
      +         
      +          [styles.secondaryButton, pressed && styles.buttonPressed]}
      +           onPress={() => signIn.mfa.sendPhoneCode()}
      +         >
      +           I need a new code
      +         
      +          [styles.secondaryButton, pressed && styles.buttonPressed]}
      +           onPress={() => signIn.reset()}
      +         >
      +           Start over
      +         
      +         {errors && {JSON.stringify(errors, null, 2)}}
      +       
      +     )
      +   }

          return (
            
              
                Sign in
              
              Enter phone number
               setPhoneNumber(phoneNumber)}
                keyboardType="phone-pad"
              />
              {errors.fields.identifier && (
                {errors.fields.identifier.message}
              )}
              Enter password
               setPassword(password)}
              />
              {errors.fields.password && (
                {errors.fields.password.message}
              )}
               [
                  styles.button,
                  fetchStatus === 'fetching' && styles.buttonDisabled,
                  pressed && styles.buttonPressed,
                ]}
                onPress={handleSubmit}
                disabled={fetchStatus === 'fetching'}
              >
                Continue
              
              {errors && {JSON.stringify(errors, null, 2)}}
            
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
            borderRadius: 8,
            padding: 12,
            fontSize: 16,
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
