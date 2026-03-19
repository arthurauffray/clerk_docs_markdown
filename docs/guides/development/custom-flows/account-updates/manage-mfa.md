# Build a custom flow for managing multi-factor authentication


> Learn how to use the Clerk API to build a custom flow for managing multi-factor authentication.

> [!WARNING]
> This guide is for users who want to build a custom flow. To use a _prebuilt_ UI, use the [Account Portal pages](/guides/account-portal/overview) or [prebuilt components](/reference/components/overview).


[Multi-factor verification (MFA)](/guides/configure/auth-strategies/sign-up-sign-in-options#multi-factor-authentication) is an added layer of security that requires users to provide a second verification factor to access an account.

Clerk supports MFA through **SMS verification code**, **Authenticator application**, and **Backup codes**.

This guide will walk you through how to build a custom flow that allows users to manage their MFA settings:

- [SMS verification code & backup codes](#sms-verification-code)
- [Authenticator application (TOTP) & backup codes](#authenticator-application-totp)

## SMS verification code


  ### Enable multi-factor authentication

  For your users to be able to enable MFA for their account, you need to enable MFA for your application.

  1. In the Clerk Dashboard, navigate to the [**Multi-factor**](https://dashboard.clerk.com/~/user-authentication/multi-factor) page.
  1. For the purpose of this guide, toggle on both the **SMS verification code** and **Backup codes** strategies.
  1. Select **Save**.

  ### Build the custom flow

  This example consists of two pages:

  - The main page where users can manage their SMS MFA settings
  - The page where users can add a phone number to their account

  Use the following tabs to view the code necessary for each page.

  
#### Manage MFA page


      
        
          
            > [!TIP]
> Examples for this SDK aren't available yet. For now, try adapting the  available example to fit your SDK.

          

          ```tsx
// Filename: app/account/manage-mfa/page.tsx

          'use client'

          import * as React from 'react'
          import { useUser, useReverification, useClerk, useSession } from '@clerk/nextjs'
          import { BackupCodeResource, PhoneNumberResource } from '@clerk/shared/types'
          import Link from 'next/link'
          import { useRouter } from 'next/navigation'

          // Display phone numbers reserved for MFA
          const ManageMfaPhoneNumbers = () => {
            const { isSignedIn, user } = useUser()
            const clerk = useClerk()

            // Handle signed out state
            // If the user is trying to set up MFA, they should be able to access this page
            if (!isSignedIn && clerk.session?.currentTask?.key !== 'setup-mfa')
              return <p>You must be signed in to access this page</p>

            // Check if any phone numbers are reserved for MFA
            const mfaPhones = user?.phoneNumbers
              .filter((ph) => ph.verification.status === 'verified')
              .filter((ph) => ph.reservedForSecondFactor)
              .sort((ph: PhoneNumberResource) => (ph.defaultSecondFactor ? -1 : 1))

            if (!mfaPhones || mfaPhones.length === 0) {
              return <p>There are currently no phone numbers reserved for MFA.</p>
            }

            return (
              <>
                <h2>Phone numbers reserved for MFA</h2>
                <ul>
                  {mfaPhones.map((phone) => {
                    return (
                      <li key={phone.id} style={{ display: 'flex', gap: '10px' }}>
                        <p>
                          {phone.phoneNumber} {phone.defaultSecondFactor && '(Default)'}
                        </p>
                        <div>
                          <button onClick={() => phone.setReservedForSecondFactor({ reserved: false })}>
                            Disable for MFA
                          </button>
                        </div>

                        {!phone.defaultSecondFactor && (
                          <div>
                            <button onClick={() => phone.makeDefaultSecondFactor()}>Make default</button>
                          </div>
                        )}

                        <div>
                          <button onClick={() => phone.destroy()}>Remove from account</button>
                        </div>
                      </li>
                    )
                  })}
                </ul>
              </>
            )
          }

          // Display phone numbers that are not reserved for MFA
          const ManageAvailablePhoneNumbers = () => {
            const { isSignedIn, user } = useUser()
            const clerk = useClerk()
            const router = useRouter()

            const setReservedForSecondFactor = useReverification((phone: PhoneNumberResource) =>
              phone.setReservedForSecondFactor({ reserved: true }),
            )
            const destroyPhone = useReverification((phone: PhoneNumberResource) => phone.destroy())

            // Complete the session task when phone number is picked for MFA
            const completeTask = async () => {
              try {
                await clerk.setActive({
                  session: clerk.session?.id,
                  navigate: async ({ session, decorateUrl }) => {
                    const url = decorateUrl('/')
                    if (url.startsWith('http')) {
                      window.location.href = url
                    } else {
                      router.push(url)
                    }
                  },
                })
              } catch (err) {
                // See https://clerk.com/docs/guides/development/custom-flows/error-handling
                // for more info on error handling
                console.error(JSON.stringify(err, null, 2))
              }
            }

            // Handle signed out state
            // If the user is trying to set up MFA, they should be able to access this page
            if (!isSignedIn && clerk.session?.currentTask?.key !== 'setup-mfa')
              return <p>You must be signed in to access this page</p>

            // Get verified phone numbers that aren't reserved for MFA
            const availableForMfaPhones = user?.phoneNumbers
              .filter((ph) => ph.verification.status === 'verified')
              .filter((ph) => !ph.reservedForSecondFactor)

            // Enable a phone number for MFA
            const reservePhoneForMfa = async (phone: PhoneNumberResource) => {
              try {
                // Set the phone number as reserved for MFA
                await setReservedForSecondFactor(phone)
                if (clerk.session?.currentTask?.key === 'setup-mfa') completeTask()

                // Refresh the user information to reflect changes
                await user?.reload()
              } catch (err) {
                // See https://clerk.com/docs/guides/development/custom-flows/error-handling
                // for more info on error handling
                console.error(JSON.stringify(err, null, 2))
              }
            }

            if (!availableForMfaPhones || availableForMfaPhones.length === 0) {
              return <p>There are currently no verified phone numbers available to be reserved for MFA.</p>
            }

            return (
              <>
                <h2>Phone numbers that are not reserved for MFA</h2>

                <ul>
                  {availableForMfaPhones.map((phone) => {
                    return (
                      <li key={phone.id} style={{ display: 'flex', gap: '10px' }}>
                        <p>{phone.phoneNumber}</p>
                        <div>
                          <button onClick={() => reservePhoneForMfa(phone)}>Use for MFA</button>
                        </div>
                        <div>
                          <button onClick={() => destroyPhone(phone)}>Remove from account</button>
                        </div>
                      </li>
                    )
                  })}
                </ul>
              </>
            )
          }

          // Generate and display backup codes
          function GenerateBackupCodes() {
            const { user } = useUser()
            const [backupCodes, setBackupCodes] = React.useState(undefined)
            const createBackupCode = useReverification(() => user?.createBackupCode())

            const [loading, setLoading] = React.useState(false)

            React.useEffect(() => {
              if (backupCodes) return

              setLoading(true)
              void createBackupCode()
                .then((backupCode: BackupCodeResource | undefined) => {
                  if (backupCode) setBackupCodes(backupCode)
                  setLoading(false)
                })
                .catch((err) => {
                  // See https://clerk.com/docs/guides/development/custom-flows/error-handling
                  // for more info on error handling
                  console.error(JSON.stringify(err, null, 2))
                  setLoading(false)
                })
            }, [backupCodes, createBackupCode])

            if (loading) return <p>Loading...</p>

            if (!backupCodes) return <p>There was a problem generating backup codes</p>

            return (
              <ol>
                {backupCodes.codes.map((code, index) => (
                  <li key={index}>{code}</li>
                ))}
              </ol>
            )
          }

          export default function ManageMFA() {
            const [showBackupCodes, setShowBackupCodes] = React.useState(false)

            const { isLoaded, isSignedIn, user } = useUser()
            const { session } = useSession()
            const clerk = useClerk()
            const router = useRouter()

            // Complete the session task when phone number is picked for MFA
            const completeTask = async () => {
              try {
                await clerk.setActive({
                  session: clerk.session?.id,
                  navigate: async ({ session, decorateUrl }) => {
                    const url = decorateUrl('/')
                    if (url.startsWith('http')) {
                      window.location.href = url
                    } else {
                      router.push(url)
                    }
                  },
                })
              } catch (err) {
                // See https://clerk.com/docs/guides/development/custom-flows/error-handling
                // for more info on error handling
                console.error(JSON.stringify(err, null, 2))
              }
            }

            // Handle loading state
            if (!isLoaded) return <p>Loading...</p>

            // Handle signed out state
            // If the user is trying to set up MFA, they should be able to access this page
            if (!isSignedIn && session?.currentTask?.key !== 'setup-mfa')
              return <p>You must be signed in to access this page</p>

            return (
              <>
                <h1>User MFA Settings</h1>

                
                Add a new phone number

                
                {user?.twoFactorEnabled && (
                  <div>
                    <p>
                      Generate new backup codes? -{' '}
                      <button onClick={() => setShowBackupCodes(true)}>Generate</button>
                    </p>
                  </div>
                )}
                {showBackupCodes && (
                  <>
                    <button
                      onClick={() => {
                        setShowBackupCodes(false)
                        completeTask()
                      }}
                    >
                      Done
                    </button>
                  </>
                )}
              </>
            )
          }
          ```
        

        
          ```tsx
// Filename: app/(account)/manage-mfa.tsx

          import * as React from 'react'
          import {
            View,
            Text,
            ScrollView,
            TouchableOpacity,
            StyleSheet,
            ActivityIndicator,
          } from 'react-native'
          import { useUser, useReverification, useClerk, useSession } from '@clerk/expo'
          import { BackupCodeResource, PhoneNumberResource } from '@clerk/shared/types'
          import { Link, useRouter } from 'expo-router'

          // Display phone numbers reserved for MFA
          const ManageMfaPhoneNumbers = () => {
            const { isSignedIn, user } = useUser()
            const clerk = useClerk()

            // Handle signed out state
            // If the user is trying to set up MFA, they should be able to access this page
            if (!isSignedIn && clerk.session?.currentTask?.key !== 'setup-mfa')
              return You must be signed in to access this page

            // Check if any phone numbers are reserved for MFA
            const mfaPhones = user?.phoneNumbers
              .filter((ph) => ph.verification.status === 'verified')
              .filter((ph) => ph.reservedForSecondFactor)
              .sort((ph: PhoneNumberResource) => (ph.defaultSecondFactor ? -1 : 1))

            if (!mfaPhones || mfaPhones.length === 0) {
              return (
                There are currently no phone numbers reserved for MFA.
              )
            }

            return (
              
                Phone numbers reserved for MFA
                {mfaPhones.map((phone) => {
                  return (
                    
                      
                        
                          {phone.phoneNumber}{' '}
                          {phone.defaultSecondFactor && (Default)}
                        
                      

                      
                         phone.setReservedForSecondFactor({ reserved: false })}
                        >
                          Disable for MFA
                        

                        {!phone.defaultSecondFactor && (
                           phone.makeDefaultSecondFactor()}
                          >
                            Make default
                          
                        )}

                         phone.destroy()}
                        >
                          Remove
                        
                      
                    
                  )
                })}
              
            )
          }

          // Display phone numbers that are not reserved for MFA
          const ManageAvailablePhoneNumbers = () => {
            const { isSignedIn, user } = useUser()
            const clerk = useClerk()
            const router = useRouter()

            const setReservedForSecondFactor = useReverification((phone: PhoneNumberResource) =>
              phone.setReservedForSecondFactor({ reserved: true }),
            )
            const destroyPhone = useReverification((phone: PhoneNumberResource) => phone.destroy())

            // Complete the session task when phone number is picked for MFA
            const completeTask = async () => {
              try {
                await clerk.setActive({
                  session: clerk.session?.id,
                  navigate: async ({ decorateUrl }) => {
                    const url = decorateUrl('/')
                    if (url.startsWith('http')) {
                      window.location.href = url
                    } else {
                      router.push(url)
                    }
                  },
                })
              } catch (err) {
                // See https://clerk.com/docs/guides/development/custom-flows/error-handling
                // for more info on error handling
                console.error(JSON.stringify(err, null, 2))
              }
            }

            // Handle signed out state
            // If the user is trying to set up MFA, they should be able to access this page
            if (!isSignedIn && clerk.session?.currentTask?.key !== 'setup-mfa')
              return You must be signed in to access this page

            // Get verified phone numbers that aren't reserved for MFA
            const availableForMfaPhones = user?.phoneNumbers
              .filter((ph) => ph.verification.status === 'verified')
              .filter((ph) => !ph.reservedForSecondFactor)

            // Enable a phone number for MFA
            const reservePhoneForMfa = async (phone: PhoneNumberResource) => {
              try {
                // Set the phone number as reserved for MFA
                await setReservedForSecondFactor(phone)
                if (clerk.session?.currentTask?.key === 'setup-mfa') completeTask()

                // Refresh the user information to reflect changes
                await user?.reload()
              } catch (err) {
                // See https://clerk.com/docs/guides/development/custom-flows/error-handling
                // for more info on error handling
                console.error(JSON.stringify(err, null, 2))
              }
            }

            if (!availableForMfaPhones || availableForMfaPhones.length === 0) {
              return (
                
                  There are currently no verified phone numbers available to be reserved for MFA.
                
              )
            }

            return (
              
                Phone numbers not reserved for MFA

                {availableForMfaPhones.map((phone) => {
                  return (
                    
                      
                        {phone.phoneNumber}
                      

                      
                         reservePhoneForMfa(phone)}
                        >
                          Use for MFA
                        

                         destroyPhone(phone)}
                        >
                          Remove
                        
                      
                    
                  )
                })}
              
            )
          }

          // Generate and display backup codes
          function GenerateBackupCodes() {
            const { user } = useUser()
            const [backupCodes, setBackupCodes] = React.useState(undefined)
            const createBackupCode = useReverification(() => user?.createBackupCode())

            const [loading, setLoading] = React.useState(false)

            React.useEffect(() => {
              if (backupCodes) return

              setLoading(true)
              void createBackupCode()
                .then((backupCode: BackupCodeResource | undefined) => {
                  if (backupCode) setBackupCodes(backupCode)
                  setLoading(false)
                })
                .catch((err) => {
                  // See https://clerk.com/docs/guides/development/custom-flows/error-handling
                  // for more info on error handling
                  console.error(JSON.stringify(err, null, 2))
                  setLoading(false)
                })
            }, [backupCodes, createBackupCode])

            if (loading)
              return (
                
                  Generating backup codes...
                
              )

            if (!backupCodes)
              return There was a problem generating backup codes

            return (
              
                Save these backup codes:
                {backupCodes.codes.map((code, index) => (
                  
                    {index + 1}.
                    {code}
                  
                ))}
              
            )
          }

          export default function ManageMFA() {
            const [showBackupCodes, setShowBackupCodes] = React.useState(false)

            const { isLoaded, isSignedIn, user } = useUser()
            const { session } = useSession()
            const clerk = useClerk()
            const router = useRouter()

            // Complete the session task when phone number is picked for MFA
            const completeTask = async () => {
              try {
                await clerk.setActive({
                  session: clerk.session?.id,
                  navigate: async ({ decorateUrl }) => {
                    const url = decorateUrl('/')
                    if (url.startsWith('http')) {
                      window.location.href = url
                    } else {
                      router.push(url)
                    }
                  },
                })
              } catch (err) {
                // See https://clerk.com/docs/guides/development/custom-flows/error-handling
                // for more info on error handling
                console.error(JSON.stringify(err, null, 2))
              }
            }

            // Handle loading state
            if (!isLoaded)
              return (
                
                  Loading...
                
              )

            // Handle signed out state
            // If the user is trying to set up MFA, they should be able to access this page
            if (!isSignedIn && session?.currentTask?.key !== 'setup-mfa')
              return (
                
                  You must be signed in to access this page
                
              )

            return (
              
                User MFA Settings

                
                
                  
                    Add a new phone number
                  
                

                
                {user?.twoFactorEnabled && (
                  
                    Backup Codes
                    {!showBackupCodes ? (
                      
                        Generate new backup codes for account recovery
                         setShowBackupCodes(true)}
                        >
                          Generate Backup Codes
                        
                      
                    ) : (
                      
                         {
                            setShowBackupCodes(false)
                            completeTask()
                          }}
                        >
                          Done
                        
                      
                    )}
                  
                )}
              
            )
          }

          const styles = StyleSheet.create({
            container: {
              flex: 1,
              backgroundColor: '#f9fafb',
            },
            contentContainer: {
              padding: 20,
            },
            title: {
              fontSize: 28,
              fontWeight: 'bold',
              color: '#111827',
              marginBottom: 24,
            },
            section: {
              marginBottom: 24,
            },
            sectionTitle: {
              fontSize: 20,
              fontWeight: '600',
              color: '#374151',
              marginBottom: 12,
            },
            phoneItem: {
              backgroundColor: '#ffffff',
              borderRadius: 12,
              padding: 16,
              marginBottom: 12,
              shadowColor: '#000',
              shadowOffset: { width: 0, height: 1 },
              shadowOpacity: 0.1,
              shadowRadius: 3,
              elevation: 2,
            },
            phoneInfo: {
              marginBottom: 12,
            },
            phoneNumber: {
              fontSize: 16,
              color: '#111827',
              fontWeight: '500',
            },
            badge: {
              color: '#6366f1',
              fontWeight: '600',
            },
            buttonGroup: {
              flexDirection: 'row',
              flexWrap: 'wrap',
              gap: 8,
            },
            button: {
              paddingVertical: 10,
              paddingHorizontal: 16,
              borderRadius: 8,
              alignItems: 'center',
              justifyContent: 'center',
            },
            primaryButton: {
              backgroundColor: '#6366f1',
            },
            primaryButtonText: {
              color: '#ffffff',
              fontSize: 14,
              fontWeight: '600',
            },
            secondaryButton: {
              backgroundColor: '#f3f4f6',
              borderWidth: 1,
              borderColor: '#d1d5db',
            },
            secondaryButtonText: {
              color: '#374151',
              fontSize: 14,
              fontWeight: '600',
            },
            dangerButton: {
              backgroundColor: '#fef2f2',
              borderWidth: 1,
              borderColor: '#fecaca',
            },
            dangerButtonText: {
              color: '#dc2626',
              fontSize: 14,
              fontWeight: '600',
            },
            successButton: {
              backgroundColor: '#10b981',
            },
            successButtonText: {
              color: '#ffffff',
              fontSize: 14,
              fontWeight: '600',
            },
            linkButton: {
              marginTop: 8,
            },
            infoText: {
              fontSize: 14,
              color: '#6b7280',
              marginBottom: 12,
            },
            warningText: {
              fontSize: 14,
              color: '#dc2626',
              textAlign: 'center',
            },
            loadingContainer: {
              flex: 1,
              justifyContent: 'center',
              alignItems: 'center',
            },
            loadingText: {
              fontSize: 14,
              color: '#6b7280',
              marginTop: 12,
            },
            backupCodesContainer: {
              backgroundColor: '#ffffff',
              borderRadius: 12,
              padding: 16,
              marginBottom: 16,
            },
            backupCodesTitle: {
              fontSize: 16,
              fontWeight: '600',
              color: '#111827',
              marginBottom: 12,
            },
            backupCodeItem: {
              flexDirection: 'row',
              alignItems: 'center',
              paddingVertical: 8,
              paddingHorizontal: 12,
              backgroundColor: '#f9fafb',
              borderRadius: 6,
              marginBottom: 6,
            },
            backupCodeNumber: {
              fontSize: 14,
              fontWeight: '600',
              color: '#6b7280',
              width: 24,
            },
            backupCode: {
              fontSize: 16,
              fontFamily: 'monospace',
              color: '#111827',
              fontWeight: '500',
            },
            backupPrompt: {
              backgroundColor: '#ffffff',
              borderRadius: 12,
              padding: 16,
            },
            doneButton: {
              marginTop: 16,
            },
          })
          ```
        
      
    

#### Add phone number page


      
  
    > [!TIP]
> Examples for this SDK aren't available yet. For now, try adapting the  available example to fit your SDK.

  

  ```tsx
// Filename: app/account/add-phone/page.tsx

  'use client'

  import * as React from 'react'
  import { useSession, useUser, useReverification } from '@clerk/nextjs'
  import { PhoneNumberResource } from '@clerk/shared/types'

  export default function Page() {
    const { isLoaded, isSignedIn, user } = useUser()
    const { session } = useSession()
    const createPhoneNumber = useReverification((phone: string) =>
      user?.createPhoneNumber({ phoneNumber: phone }),
    )

    const [phone, setPhone] = React.useState('')
    const [code, setCode] = React.useState('')
    const [isVerifying, setIsVerifying] = React.useState(false)
    const [successful, setSuccessful] = React.useState(false)
    const [phoneObj, setPhoneObj] = React.useState()

    // Handle loading state
    if (!isLoaded) return <p>Loading...</p>

    // Handle signed-out state
    // If the user is trying to set up MFA, they should be able to access this page
    if (!isSignedIn && session?.currentTask?.key !== 'setup-mfa')
      return <p>You must be signed in to access this page</p>

    // Handle addition of the phone number
    const handleSubmit = async (e: React.FormEvent) => {
      e.preventDefault()

      try {
        // Add unverified phone number to user
        const res = await createPhoneNumber(phone)
        // Reload user to get updated User object
        await user.reload()

        // Create a reference to the new phone number to use related methods
        const phoneNumber = user.phoneNumbers.find((a) => a.id === res?.id)
        setPhoneObj(phoneNumber)

        // Send the user an SMS with the verification code
        phoneNumber?.prepareVerification()

        // Set to true to display second form
        // and capture the code
        setIsVerifying(true)
      } catch (err) {
        // See https://clerk.com/docs/guides/development/custom-flows/error-handling
        // for more info on error handling
        console.error(JSON.stringify(err, null, 2))
      }
    }

    // Handle the submission of the verification form
    const verifyCode = async (e: React.FormEvent) => {
      e.preventDefault()
      try {
        // Verify that the provided code matches the code sent to the user
        const phoneVerifyAttempt = await phoneObj?.attemptVerification({ code })

        if (phoneVerifyAttempt?.verification.status === 'verified') {
          setSuccessful(true)
        } else {
          // If the status is not complete, check why. User may need to
          // complete further steps.
          console.error(JSON.stringify(phoneVerifyAttempt, null, 2))
        }
      } catch (err) {
        console.error(JSON.stringify(err, null, 2))
      }
    }

    // Display a success message if the phone number was added successfully
    if (successful) return <h1>Phone added</h1>

    // Display the verification form to capture the code
    if (isVerifying) {
      return (
        <>
          <h1>Verify phone</h1>
          <div>
            <form onSubmit={(e) => verifyCode(e)}>
              <div>
                <label htmlFor="code">Enter code</label>
                <input
                  onChange={(e) => setCode(e.target.value)}
                  id="code"
                  name="code"
                  type="text"
                  value={code}
                />
              </div>
              <div>
                <button type="submit">Verify</button>
              </div>
            </form>
          </div>
        </>
      )
    }

    // Display the initial form to capture the phone number
    return (
      <>
        <h1>Add phone</h1>
        <div>
          <form onSubmit={(e) => handleSubmit(e)}>
            <div>
              <label htmlFor="phone">Enter phone number</label>
              <input
                onChange={(e) => setPhone(e.target.value)}
                id="phone"
                name="phone"
                type="phone"
                value={phone}
              />
            </div>
            <div>
              <button type="submit">Continue</button>
            </div>
          </form>
        </div>
      </>
    )
  }
  ```


  ```tsx
// Filename: app/(account)/add-phone.tsx

  import { ThemedText } from '@/components/themed-text'
  import { ThemedView } from '@/components/themed-view'
  import { useSession, useUser } from '@clerk/expo'
  import { PhoneNumberResource } from '@clerk/shared/types'
  import { Redirect } from 'expo-router'
  import * as React from 'react'
  import { Pressable, StyleSheet, TextInput } from 'react-native'

  export default function Page() {
    const { isLoaded, isSignedIn, user } = useUser()
    const { session } = useSession()

    const [phone, setPhone] = React.useState('')
    const [code, setCode] = React.useState('')
    const [isVerifying, setIsVerifying] = React.useState(false)
    const [successful, setSuccessful] = React.useState(false)
    const [phoneObj, setPhoneObj] = React.useState()

    // Handle loading state
    if (!isLoaded) {
      return (
        
          Loading...
        
      )
    }

    // Handle signed-out state
    // If the user is trying to set up MFA, they should be able to access this page
    if (!isSignedIn && session?.currentTask?.key !== 'setup-mfa') {
      return }

    // Handle addition of the phone number
    const handleSubmit = async () => {
      try {
        // Add unverified phone number to user
        const res = await user?.createPhoneNumber({ phoneNumber: phone })
        // Reload user to get updated User object
        await user?.reload()

        // Create a reference to the new phone number to use related methods
        const phoneNumber = user?.phoneNumbers.find((a) => a.id === res?.id)
        setPhoneObj(phoneNumber)

        // Send the user an SMS with the verification code
        await phoneNumber?.prepareVerification()

        // Set to true to display second form
        // and capture the code
        setIsVerifying(true)
      } catch (err) {
        // See https://clerk.com/docs/guides/development/custom-flows/error-handling
        // for more info on error handling
        console.error(JSON.stringify(err, null, 2))
      }
    }

    // Handle the submission of the verification form
    const verifyCode = async () => {
      try {
        // Verify that the provided code matches the code sent to the user
        const phoneVerifyAttempt = await phoneObj?.attemptVerification({ code })

        if (phoneVerifyAttempt?.verification.status === 'verified') {
          setSuccessful(true)
        } else {
          // If the status is not complete, check why. User may need to
          // complete further steps.
          console.error(JSON.stringify(phoneVerifyAttempt, null, 2))
        }
      } catch (err) {
        console.error(JSON.stringify(err, null, 2))
      }
    }

    // Display a success message if the phone number was added successfully
    if (successful) {
      return (
        
          
            Phone added
          
        
      )
    }

    // Display the verification form to capture the code
    if (isVerifying) {
      return (
        
          
            Verify phone
          
          Enter code
           [
              styles.button,
              !code && styles.buttonDisabled,
              pressed && styles.buttonPressed,
            ]}
            onPress={verifyCode}
            disabled={!code}
          >
            Verify
          
        
      )
    }

    // Display the initial form to capture the phone number
    return (
      
        
          Add phone
        
        Enter phone number
         [
            styles.button,
            !phone && styles.buttonDisabled,
            pressed && styles.buttonPressed,
          ]}
          onPress={handleSubmit}
          disabled={!phone}
        >
          Continue
        
      
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


  ```swift
// Filename: AddPhoneView.swift

    import SwiftUI
    import ClerkKit

    struct AddPhoneView: View {
      @State private var phone = ""
      @State private var code = ""
      @State private var isVerifying = false
      @State private var newPhoneNumber: PhoneNumber?

      var body: some View {
        if newPhoneNumber?.verification?.status == .verified {
          Text("Phone added!")
        }

        if isVerifying {
          TextField("Enter code", text: $code)
          Button("Verify") {
            Task { await verifyCode(code) }
          }
        } else {
          TextField("Enter phone number", text: $phone)
          Button("Continue") {
            Task { await createPhone(phone) }
          }
        }
      }
    }

    extension AddPhoneView {

      func createPhone(_ phone: String) async {
        do {
          guard let user = Clerk.shared.user else { return }

          // Create the phone number
          let phoneNumber = try await user.createPhoneNumber(phone)

          // Send the user an SMS with the verification code
          self.newPhoneNumber = try await phoneNumber.sendCode()

          isVerifying = true
        } catch {
          // See https://clerk.com/docs/guides/development/custom-flows/error-handling
          // for more info on error handling
          dump(error)
        }
      }

      func verifyCode(_ code: String) async {
        do {
          guard let newPhoneNumber else { return }

          // Verify that the provided code matches the code sent to the user
          self.newPhoneNumber = try await newPhoneNumber.verifyCode(code)

          dump(self.newPhoneNumber?.verification?.status)
        } catch {
          // See https://clerk.com/docs/guides/development/custom-flows/error-handling
          // for more info on error handling
          dump(error)
        }
      }
    }
  ```


  
**AddPhoneViewModel.kt:**

```kotlin
// Filename: AddPhoneViewModel.kt

    package com.clerk.customflows.addphone

    import android.util.Log
    import androidx.lifecycle.ViewModel
    import androidx.lifecycle.viewModelScope
    import com.clerk.api.Clerk
    import com.clerk.api.network.serialization.errorMessage
    import com.clerk.api.network.serialization.flatMap
    import com.clerk.api.network.serialization.onFailure
    import com.clerk.api.network.serialization.onSuccess
    import com.clerk.api.phonenumber.PhoneNumber
    import com.clerk.api.phonenumber.attemptVerification
    import com.clerk.api.phonenumber.prepareVerification
    import com.clerk.api.user.createPhoneNumber
    import kotlinx.coroutines.flow.MutableStateFlow
    import kotlinx.coroutines.flow.asStateFlow
    import kotlinx.coroutines.flow.combine
    import kotlinx.coroutines.flow.launchIn
    import kotlinx.coroutines.launch

    class AddPhoneViewModel : ViewModel() {
    private val _uiState = MutableStateFlow(UiState.NeedsVerification)
    val uiState = _uiState.asStateFlow()

    init {
      combine(Clerk.isInitialized, Clerk.userFlow) { isInitialized, user ->
          _uiState.value =
            when {
              !isInitialized -> UiState.Loading
              user == null -> UiState.SignedOut
              else -> UiState.NeedsVerification
            }
        }
        .launchIn(viewModelScope)
    }

    fun createPhoneNumber(phoneNumber: String) {
      val user = requireNotNull(Clerk.userFlow.value)

      // Add an unverified phone number to the user,
      // then send the user an SMS with the verification code
      viewModelScope.launch {
        user
          .createPhoneNumber(phoneNumber)
          .flatMap { it.prepareVerification() }
          .onSuccess {
            // Update the state to show that the phone number has been created
            // and that the user needs to verify the phone number
            _uiState.value = UiState.Verifying(it)
          }
          .onFailure {
            Log.e(
              "AddPhoneViewModel",
              "Failed to create phone number and prepare verification: ${it.errorMessage}",
            )
          }
      }
    }

    fun verifyCode(code: String, newPhoneNumber: PhoneNumber) {
      viewModelScope.launch {
        newPhoneNumber
          .attemptVerification(code)
          .onSuccess {
            // Update the state to show that the phone number has been verified
            _uiState.value = UiState.Verified
          }
          .onFailure {
            Log.e("AddPhoneViewModel", "Failed to verify phone number: ${it.errorMessage}")
          }
      }
    }

    sealed interface UiState {
      data object Loading : UiState

      data object NeedsVerification : UiState

      data class Verifying(val phoneNumber: PhoneNumber) : UiState

      data object Verified : UiState

      data object SignedOut : UiState
    }
    }
    ```


**AddPhoneActivity.kt:**

```kotlin
// Filename: AddPhoneActivity.kt

    package com.clerk.customflows.addphone

    import android.os.Bundle
    import androidx.activity.ComponentActivity
    import androidx.activity.compose.setContent
    import androidx.activity.viewModels
    import androidx.compose.foundation.layout.Box
    import androidx.compose.foundation.layout.Column
    import androidx.compose.foundation.layout.fillMaxSize
    import androidx.compose.foundation.layout.padding
    import androidx.compose.material3.Button
    import androidx.compose.material3.CircularProgressIndicator
    import androidx.compose.material3.Text
    import androidx.compose.material3.TextField
    import androidx.compose.runtime.Composable
    import androidx.compose.runtime.getValue
    import androidx.compose.runtime.mutableStateOf
    import androidx.compose.runtime.remember
    import androidx.compose.runtime.setValue
    import androidx.compose.ui.Alignment
    import androidx.compose.ui.Modifier
    import androidx.compose.ui.unit.dp
    import androidx.lifecycle.compose.collectAsStateWithLifecycle
    import com.clerk.api.phonenumber.PhoneNumber

    class AddPhoneActivity : ComponentActivity() {
    val viewModel: AddPhoneViewModel by viewModels()

    override fun onCreate(savedInstanceState: Bundle?) {
      super.onCreate(savedInstanceState)
      setContent {
        val state by viewModel.uiState.collectAsStateWithLifecycle()
        AddPhoneView(
          state = state,
          onCreatePhoneNumber = viewModel::createPhoneNumber,
          onVerifyCode = viewModel::verifyCode,
        )
      }
    }
    }

    @Composable
    fun AddPhoneView(
    state: AddPhoneViewModel.UiState,
    onCreatePhoneNumber: (String) -> Unit,
    onVerifyCode: (String, PhoneNumber) -> Unit,
    ) {
    Box(modifier = Modifier.fillMaxSize(), contentAlignment = Alignment.Center) {
      when (state) {
        AddPhoneViewModel.UiState.NeedsVerification -> {
          InputContentView(buttonText = "Continue", placeholder = "Enter phone number") {
            onCreatePhoneNumber(it)
          }
        }

        AddPhoneViewModel.UiState.Verified -> Text("Verified!")

        is AddPhoneViewModel.UiState.Verifying -> {
          InputContentView(buttonText = "Verify", placeholder = "Enter code") {
            onVerifyCode(it, state.phoneNumber)
          }
        }

        AddPhoneViewModel.UiState.Loading -> CircularProgressIndicator()
        AddPhoneViewModel.UiState.SignedOut -> Text("You must be signed in to add a phone number.")
      }
    }
    }

    @Composable
    fun InputContentView(
    buttonText: String,
    placeholder: String,
    modifier: Modifier = Modifier,
    onClick: (String) -> Unit,
    ) {
    var input by remember { mutableStateOf("") }
    Column(horizontalAlignment = Alignment.CenterHorizontally, modifier = modifier) {
      TextField(
        modifier = Modifier.padding(bottom = 16.dp),
        value = input,
        onValueChange = { input = it },
        placeholder = { Text(placeholder) },
      )
      Button(onClick = { onClick(input) }) { Text(buttonText) }
    }
    }
    ```


    


## Authenticator application (TOTP)


  ### Enable multi-factor authentication

  For your users to be able to enable MFA for their account, you need to enable MFA for your application.

  1. In the Clerk Dashboard, navigate to the [**Multi-factor**](https://dashboard.clerk.com/~/user-authentication/multi-factor) page.
  1. For the purpose of this guide, toggle on both the **Authenticator application** and **Backup codes** strategies.
  1. Select **Save**.

  
    ### Install dependencies

    Install `expo-checkbox` for the UI and `react-native-qr-svg` for the QR code.

    ```npm
    npm install expo-checkbox react-native-qr-svg
    ```
  

  ### Build the custom flow

  
    
      
        > [!TIP]
> Examples for this SDK aren't available yet. For now, try adapting the  available example to fit your SDK.

      

      This example consists of two pages:

      - The main page where users can manage their MFA settings
      - The page where users can add TOTP MFA

      Use the following tabs to view the code necessary for each page.

      
#### Manage MFA page


          ```tsx
// Filename: app/account/manage-mfa/page.tsx

          'use client'

          import * as React from 'react'
          import { useUser, useReverification, useClerk, useSession } from '@clerk/nextjs'
          import Link from 'next/link'
          import { BackupCodeResource } from '@clerk/shared/types'
          import { useRouter } from 'next/navigation'

          // If TOTP is enabled, provide the option to disable it
          const TotpEnabled = () => {
            const { user } = useUser()
            const disableTOTP = useReverification(() => user?.disableTOTP())

            return (
              <div>
                <p>
                  TOTP via authentication app enabled - <button onClick={() => disableTOTP()}>Remove</button>
                </p>
              </div>
            )
          }

          // If TOTP is disabled, provide the option to enable it
          const TotpDisabled = () => {
            return (
              <div>
                <p>
                  Add TOTP via authentication app -{' '}
                  
                    <button>Add</button>
                  
                </p>
              </div>
            )
          }

          // Generate and display backup codes
          export function GenerateBackupCodes() {
            const { user } = useUser()
            const [backupCodes, setBackupCodes] = React.useState(undefined)
            const createBackupCode = useReverification(() => user?.createBackupCode())

            const [loading, setLoading] = React.useState(false)

            React.useEffect(() => {
              if (backupCodes) return

              setLoading(true)
              void createBackupCode()
                .then((backupCode: BackupCodeResource | undefined) => {
                  setBackupCodes(backupCode)
                  setLoading(false)
                })
                .catch((err) => {
                  // See https://clerk.com/docs/guides/development/custom-flows/error-handling
                  // for more info on error handling
                  console.error(JSON.stringify(err, null, 2))
                  setLoading(false)
                })
            }, [backupCodes, createBackupCode])

            if (loading) return <p>Loading...</p>

            if (!backupCodes) return <p>There was a problem generating backup codes</p>

            return (
              <ol>
                {backupCodes.codes.map((code, index) => (
                  <li key={index}>{code}</li>
                ))}
              </ol>
            )
          }

          export default function ManageMFA() {
            const { isLoaded, isSignedIn, user } = useUser()
            const clerk = useClerk()
            const router = useRouter()

            // Complete the session task when phone number is picked for MFA
            const completeTask = async () => {
              try {
                await clerk.setActive({
                  session: clerk.session?.id,
                  navigate: async ({ decorateUrl }) => {
                    const url = decorateUrl('/')
                    if (url.startsWith('http')) {
                      window.location.href = url
                    } else {
                      router.push(url)
                    }
                  },
                })
              } catch (err) {
                // See https://clerk.com/docs/guides/development/custom-flows/error-handling
                // for more info on error handling
                console.error(JSON.stringify(err, null, 2))
              }
            }

            const [showNewCodes, setShowNewCodes] = React.useState(false)

            // Handle loading state
            if (!isLoaded) return <p>Loading...</p>

            // Handle signed out state
            // If the user is trying to set up MFA, they should be able to access this page
            if (!isSignedIn && clerk.session?.currentTask?.key !== 'setup-mfa')
              return <p>You must be signed in to access this page</p>

            return (
              <>
                <h1>User MFA Settings</h1>

                
                {user?.totpEnabled ? : }

                
                {user?.backupCodeEnabled && user.twoFactorEnabled && (
                  <div>
                    <p>
                      Generate new backup codes? -{' '}
                      <button
                        onClick={() => {
                          setShowNewCodes(true)
                        }}
                      >
                        Generate
                      </button>
                    </p>
                  </div>
                )}
                {showNewCodes && (
                  <>
                    <button onClick={() => setShowNewCodes(false)}>Done</button>
                  </>
                )}
              </>
            )
          }
          ```
        

#### Add TOTP page


          ```tsx
// Filename: app/account/manage-mfa/add/page.tsx

          'use client'

          import { useUser, useReverification, useClerk, useSession } from '@clerk/nextjs'
          import { TOTPResource } from '@clerk/shared/types'
          import Link from 'next/link'
          import * as React from 'react'
          import { QRCodeSVG } from 'qrcode.react'
          import { GenerateBackupCodes } from '../page'
          import { useRouter } from 'next/navigation'

          type AddTotpSteps = 'add' | 'verify' | 'backupcodes' | 'success'

          type DisplayFormat = 'qr' | 'uri'

          function AddTotpScreen({
            setStep,
          }: {
            setStep: React.Dispatch>
          }) {
            const { user } = useUser()
            const [totp, setTOTP] = React.useState(undefined)
            const [displayFormat, setDisplayFormat] = React.useState('qr')
            const createTOTP = useReverification(() => user?.createTOTP())

            React.useEffect(() => {
              void createTOTP()
                .then((totp: TOTPResource | undefined) => {
                  if (totp) setTOTP(totp)
                })
                .catch((err) =>
                  // See https://clerk.com/docs/guides/development/custom-flows/error-handling
                  // for more info on error handling
                  console.error(JSON.stringify(err, null, 2)),
                )
            }, [createTOTP])

            return (
              <>
                <h1>Add TOTP MFA</h1>

                {totp && displayFormat === 'qr' && (
                  <>
                    <div>
                      </div>
                    <button onClick={() => setDisplayFormat('uri')}>Use URI instead</button>
                  </>
                )}
                {totp && displayFormat === 'uri' && (
                  <>
                    <div>
                      <p>{totp.uri}</p>
                    </div>
                    <button onClick={() => setDisplayFormat('qr')}>Use QR Code instead</button>
                  </>
                )}
                <button onClick={() => setStep('add')}>Reset</button>

                <p>Once you have set up your authentication app, verify your code</p>
                <button onClick={() => setStep('verify')}>Verify</button>
              </>
            )
          }

          function VerifyTotpScreen({
            setStep,
          }: {
            setStep: React.Dispatch>
          }) {
            const { user } = useUser()
            const [code, setCode] = React.useState('')

            const verifyTotp = async (e: React.FormEvent) => {
              e.preventDefault()
              try {
                await user?.verifyTOTP({ code })
                setStep('backupcodes')
              } catch (err) {
                console.error(JSON.stringify(err, null, 2))
              }
            }

            return (
              <>
                <h1>Verify TOTP</h1>
                <form onSubmit={(e) => verifyTotp(e)}>
                  <label htmlFor="totp-code">Enter the code from your authentication app</label>
                  <input type="text" id="totp-code" onChange={(e) => setCode(e.currentTarget.value)} />
                  <button type="submit">Verify code</button>
                  <button onClick={() => setStep('add')}>Reset</button>
                </form>
              </>
            )
          }

          function BackupCodeScreen({
            setStep,
          }: {
            setStep: React.Dispatch>
          }) {
            const clerk = useClerk()
            const router = useRouter()

            // Complete the session task when phone number is picked for MFA
            const completeTask = async () => {
              try {
                await clerk.setActive({
                  session: clerk.session?.id,
                  navigate: async ({ decorateUrl }) => {
                    const url = decorateUrl('/')
                    if (url.startsWith('http')) {
                      window.location.href = url
                    } else {
                      router.push(url)
                    }
                  },
                })
              } catch (err) {
                // See https://clerk.com/docs/guides/development/custom-flows/error-handling
                // for more info on error handling
                console.error(JSON.stringify(err, null, 2))
              }
            }

            return (
              <>
                <h1>Verification was a success!</h1>
                <div>
                  <p>
                    Save this list of backup codes somewhere safe in case you need to access your account in
                    an emergency
                  </p>
                  <button
                    onClick={() => {
                      setStep('success')
                      completeTask()
                    }}
                  >
                    Finish
                  </button>
                </div>
              </>
            )
          }

          function SuccessScreen() {
            return (
              <>
                <h1>Success!</h1>
                <p>You have successfully added TOTP MFA via an authentication application.</p>
              </>
            )
          }

          export default function AddMFaScreen() {
            const [step, setStep] = React.useState('add')
            const { isLoaded, isSignedIn } = useUser()
            const { session } = useSession()

            // Handle loading state
            if (!isLoaded) return <p>Loading...</p>

            // Handle signed out state
            // If the user is trying to set up MFA, they should be able to access this page
            if (!isSignedIn && session?.currentTask?.key !== 'setup-mfa')
              return <p>You must be signed in to access this page</p>

            return (
              <>
                {step === 'add' && }
                {step === 'verify' && }
                {step === 'backupcodes' && }
                {step === 'success' && }
                Manage MFA
              </>
            )
          }
          ```
        
    

    
      To allow users to configure their MFA settings, you'll create a basic dashboard.

      This example consists of three pages:

      - The layout page that checks if the user is signed in
      - The page where users can manage their account, including their MFA settings
      - The page where users can add TOTP MFA

      Use the following tabs to view the code necessary for each page.

      
#### Layout


          1. Create the `(account)` route group. This groups your account page and the "Add TOTP" page.
          1. Create a `_layout.tsx` file with the following code. The [`useAuth()`](/reference/hooks/use-auth) hook is used to check if the user is signed in. If the user isn't signed in, they'll be redirected to the sign-in page. You check if the user has a pending `setup-mfa` task because if they're trying to access their account settings to set up MFA, they should be able to access these routes, so we don't want to redirect them to the sign-in page.

          ```tsx
// Filename: app/(account)/_layout.tsx

          import { Redirect, Stack } from 'expo-router'
          import { useAuth, useSession } from '@clerk/expo'

          export default function AuthenticatedLayout() {
            const { isSignedIn } = useAuth()
            const { session } = useSession()

            // If the user isn't signed in and they're not trying to set up MFA, redirect them to the sign-in page
            if (!isSignedIn && session?.currentTask?.key !== 'setup-mfa') {
              return }

            return }
          ```
        

#### Account page


          In the `(account)` group, create an `manage-mfa.tsx` file with the following code. This page shows users whether or not MFA is enabled, and allows them to add MFA with an authenticator app.

          ```tsx
// Filename: app/(account)/manage-mfa.tsx

          import * as React from 'react'
          import {
            View,
            Text,
            ScrollView,
            TouchableOpacity,
            StyleSheet,
            ActivityIndicator,
          } from 'react-native'
          import { useUser, useReverification, useClerk, useSession } from '@clerk/expo'
          import { Link, useRouter } from 'expo-router'
          import { BackupCodeResource } from '@clerk/shared/types'

          // If TOTP is enabled, provide the option to disable it
          const TotpEnabled = () => {
            const { user } = useUser()
            const disableTOTP = useReverification(() => user?.disableTOTP())

            return (
              
                
                  
                    Authenticator App (TOTP)
                    ✓ Enabled
                  
                   disableTOTP()}
                  >
                    Remove
                  
                
              
            )
          }

          // If TOTP is disabled, provide the option to enable it
          const TotpDisabled = () => {
            return (
              
                
                  
                    Authenticator App (TOTP)
                    
                      Add an authenticator app for two-factor authentication
                    
                  
                  
                    
                      Add
                    
                  
                
              
            )
          }

          // Generate and display backup codes
          export function GenerateBackupCodes() {
            const { user } = useUser()
            const [backupCodes, setBackupCodes] = React.useState(undefined)
            const createBackupCode = useReverification(() => user?.createBackupCode())

            const [loading, setLoading] = React.useState(false)

            React.useEffect(() => {
              if (backupCodes) return

              setLoading(true)
              void createBackupCode()
                .then((backupCode: BackupCodeResource | undefined) => {
                  setBackupCodes(backupCode)
                  setLoading(false)
                })
                .catch((err) => {
                  // See https://clerk.com/docs/guides/development/custom-flows/error-handling
                  // for more info on error handling
                  console.error(JSON.stringify(err, null, 2))
                  setLoading(false)
                })
            }, [backupCodes, createBackupCode])

            if (loading)
              return (
                
                  Generating backup codes...
                
              )

            if (!backupCodes)
              return There was a problem generating backup codes

            return (
              
                Save these backup codes:
                
                  Store them in a safe place. Each code can only be used once.
                
                {backupCodes.codes.map((code, index) => (
                  
                    {index + 1}.
                    {code}
                  
                ))}
              
            )
          }

          export default function ManageMFA() {
            const { isLoaded, isSignedIn, user } = useUser()
            const clerk = useClerk()
            const router = useRouter()

            const [showNewCodes, setShowNewCodes] = React.useState(false)

            // Complete the session task when phone number is picked for MFA
            const completeTask = async () => {
              try {
                await clerk.setActive({
                  session: clerk.session?.id,
                  navigate: async ({ decorateUrl }) => {
                    const url = decorateUrl('/')
                    if (url.startsWith('http')) {
                      window.location.href = url
                    } else {
                      router.push(url)
                    }
                  },
                })
              } catch (err) {
                // See https://clerk.com/docs/guides/development/custom-flows/error-handling
                // for more info on error handling
                console.error(JSON.stringify(err, null, 2))
              }
            }

            // Handle loading state
            if (!isLoaded)
              return (
                
                  Loading...
                
              )

            // Handle signed out state
            // If the user is trying to set up MFA, they should be able to access this page
            if (!isSignedIn && clerk.session?.currentTask?.key !== 'setup-mfa')
              return (
                
                  You must be signed in to access this page
                
              )

            return (
              
                User MFA Settings

                
                {user?.totpEnabled ? : }

                
                {user?.backupCodeEnabled && user.twoFactorEnabled && (
                  
                    Backup Codes
                    {!showNewCodes ? (
                      
                        Generate new backup codes for account recovery
                         {
                            setShowNewCodes(true)
                          }}
                        >
                          Generate New Codes
                        
                      
                    ) : (
                      
                         setShowNewCodes(false)}
                        >
                          Done
                        
                      
                    )}
                  
                )}
              
            )
          }

          const styles = StyleSheet.create({
            container: {
              flex: 1,
              backgroundColor: '#f9fafb',
            },
            contentContainer: {
              padding: 20,
            },
            title: {
              fontSize: 28,
              fontWeight: 'bold',
              color: '#111827',
              marginBottom: 24,
            },
            section: {
              marginBottom: 24,
            },
            sectionTitle: {
              fontSize: 20,
              fontWeight: '600',
              color: '#374151',
              marginBottom: 12,
            },
            card: {
              backgroundColor: '#ffffff',
              borderRadius: 12,
              padding: 16,
              shadowColor: '#000',
              shadowOffset: { width: 0, height: 1 },
              shadowOpacity: 0.1,
              shadowRadius: 3,
              elevation: 2,
            },
            cardContent: {
              marginBottom: 12,
            },
            cardTitle: {
              fontSize: 18,
              fontWeight: '600',
              color: '#111827',
              marginBottom: 4,
            },
            statusBadge: {
              fontSize: 14,
              fontWeight: '600',
              color: '#10b981',
              marginTop: 4,
            },
            button: {
              paddingVertical: 12,
              paddingHorizontal: 16,
              borderRadius: 8,
              alignItems: 'center',
              justifyContent: 'center',
            },
            primaryButton: {
              backgroundColor: '#6366f1',
            },
            primaryButtonText: {
              color: '#ffffff',
              fontSize: 14,
              fontWeight: '600',
            },
            dangerButton: {
              backgroundColor: '#fef2f2',
              borderWidth: 1,
              borderColor: '#fecaca',
            },
            dangerButtonText: {
              color: '#dc2626',
              fontSize: 14,
              fontWeight: '600',
            },
            successButton: {
              backgroundColor: '#10b981',
            },
            successButtonText: {
              color: '#ffffff',
              fontSize: 14,
              fontWeight: '600',
            },
            infoText: {
              fontSize: 14,
              color: '#6b7280',
              marginBottom: 12,
            },
            warningText: {
              fontSize: 14,
              color: '#dc2626',
              textAlign: 'center',
            },
            loadingContainer: {
              flex: 1,
              justifyContent: 'center',
              alignItems: 'center',
            },
            loadingText: {
              fontSize: 14,
              color: '#6b7280',
              marginTop: 12,
            },
            backupCodesContainer: {
              backgroundColor: '#ffffff',
              borderRadius: 12,
              padding: 16,
              marginBottom: 16,
            },
            backupCodesTitle: {
              fontSize: 18,
              fontWeight: '600',
              color: '#111827',
              marginBottom: 4,
            },
            backupCodesSubtitle: {
              fontSize: 14,
              color: '#6b7280',
              marginBottom: 16,
            },
            backupCodeItem: {
              flexDirection: 'row',
              alignItems: 'center',
              paddingVertical: 8,
              paddingHorizontal: 12,
              backgroundColor: '#f9fafb',
              borderRadius: 6,
              marginBottom: 6,
            },
            backupCodeNumber: {
              fontSize: 14,
              fontWeight: '600',
              color: '#6b7280',
              width: 24,
            },
            backupCode: {
              fontSize: 16,
              fontFamily: 'monospace',
              color: '#111827',
              fontWeight: '500',
            },
            doneButton: {
              marginTop: 16,
            },
          })
          ```
        

#### Add TOTP page


          In the `(account)` group, create an `add-mfa.tsx` file with the following code. This page adds the functionality for generating the QR code and backup codes.

          ```tsx
// Filename: app/(account)/add-mfa.tsx

          import { useUser, useReverification, useClerk, useSession } from '@clerk/expo'
          import { TOTPResource } from '@clerk/shared/types'
          import * as React from 'react'
          import {
            View,
            Text,
            Pressable,
            TextInput,
            ScrollView,
            StyleSheet,
            ActivityIndicator,
            Alert,
          } from 'react-native'
          import { Link, useRouter } from 'expo-router'
          import { QrCodeSvg } from 'react-native-qr-svg'
          import { GenerateBackupCodes } from './manage-mfa'

          type AddTotpSteps = 'add' | 'verify' | 'backupcodes' | 'success'

          type DisplayFormat = 'qr' | 'uri'

          function AddTotpScreen({
            setStep,
          }: {
            setStep: React.Dispatch>
          }) {
            const { user } = useUser()
            const createTOTP = useReverification(() => user?.createTOTP())

            const [totp, setTOTP] = React.useState(undefined)
            const [displayFormat, setDisplayFormat] = React.useState('uri')
            const [loading, setLoading] = React.useState(true)

            React.useEffect(() => {
              setLoading(true)
              void createTOTP()
                .then((totp: TOTPResource | undefined) => {
                  if (totp) setTOTP(totp)
                  setLoading(false)
                })
                .catch((err) => {
                  console.error(JSON.stringify(err, null, 2))
                  Alert.alert('Error', 'Failed to create TOTP. Please try again.')
                  setLoading(false)
                })
            }, [createTOTP])

            if (loading) {
              return (
                
                  
                    Setting up authenticator...
                  
                
              )
            }

            return (
              
                Add TOTP MFA
                
                  Set up two-factor authentication using an authenticator app
                

                {totp && (
                  
                    Step 1: Scan or Copy

                    {displayFormat === 'qr' && (
                      
                        
                          
                         setDisplayFormat('uri')}>
                          Use URI instead
                        
                      
                    )}

                    {displayFormat === 'uri' && (
                      
                        Copy this code into your authenticator app:
                        
                          
                            {totp.uri}
                          
                        
                         setDisplayFormat('qr')}>
                          Use QR Code instead
                        
                      
                    )}

                    
                      
                        • Open your authenticator app (Google Authenticator, Authy, etc.)
                      
                      
                        • {displayFormat === 'qr' ? 'Scan the QR code' : 'Enter the code manually'}
                      
                      • Your app will generate a 6-digit code
                    
                  
                )}

                
                   setStep('add')}>
                    Reset
                  

                   setStep('verify')}>
                    Continue to Verify
                  
                
              
            )
          }

          function VerifyTotpScreen({
            setStep,
          }: {
            setStep: React.Dispatch>
          }) {
            const { user } = useUser()
            const [code, setCode] = React.useState('')
            const [loading, setLoading] = React.useState(false)
            const [error, setError] = React.useState('')

            const verifyTotp = async () => {
              if (!code || code.length !== 6) {
                setError('Please enter a valid 6-digit code')
                return
              }

              setLoading(true)
              setError('')

              try {
                await user?.verifyTOTP({ code })
                setStep('backupcodes')
              } catch (err: any) {
                console.error(JSON.stringify(err, null, 2))
                setError(err?.errors?.[0]?.message || 'Invalid code. Please try again.')
              } finally {
                setLoading(false)
              }
            }

            return (
              
                Verify TOTP
                Enter the 6-digit code from your authenticator app

                
                  Step 2: Verify Code

                  
                    Authenticator Code
                     {
                        setCode(text)
                        setError('')
                      }}
                      keyboardType="number-pad"
                      maxLength={6}
                      autoFocus
                    />
                    {error && {error}}
                  

                  
                    
                      The code refreshes every 30 seconds in your authenticator app
                    
                  
                

                
                   setStep('add')} disabled={loading}>
                    Back
                  

                  
                    {loading ? (
                      ) : (
                      Verify Code
                    )}
                  
                
              
            )
          }

          function BackupCodeScreen({
            setStep,
          }: {
            setStep: React.Dispatch>
          }) {
            const clerk = useClerk()
            const router = useRouter()

            const [loading, setLoading] = React.useState(false)

            const completeSetup = async () => {
              setLoading(true)
              setStep('success')

              try {
                await clerk.setActive({
                  session: clerk.session?.id,
                  navigate: async ({ decorateUrl }) => {
                    const url = decorateUrl('/')
                    if (url.startsWith('http')) {
                      window.location.href = url
                    } else {
                      router.push(url)
                    }
                  },
                })
              } catch (err) {
                console.error(JSON.stringify(err, null, 2))
              } finally {
                setLoading(false)
              }
            }

            return (
              
                
                  ✓
                  Verification Successful!
                

                Save Your Backup Codes
                
                  Keep these codes safe. You can use them to access your account if you lose your device.
                

                
                  

                
                  
                    ⚠ Important: Each backup code can only be used once. Store them securely.
                  
                

                
                  {loading ? (
                    ) : (
                    Finish Setup
                  )}
                
              
            )
          }

          function SuccessScreen() {
            return (
              
                
                  
                    ✓
                  
                  All Set!
                  
                    You have successfully added TOTP MFA via an authentication application.
                  
                  Your account is now more secure.

                  
                    
                      Manage MFA Settings
                    
                  
                
              
            )
          }

          export default function AddMFaScreen() {
            const [step, setStep] = React.useState('add')
            const { isLoaded, isSignedIn } = useUser()
            const { session } = useSession()

            // Handle loading state
            if (!isLoaded) {
              return (
                
                  
                    Loading...
                  
                
              )
            }

            // Handle signed out state
            if (!isSignedIn && session?.currentTask?.key !== 'setup-mfa') {
              return (
                
                  
                    Access Denied
                    You must be signed in to access this page
                    
                      
                        Go Home
                      
                    
                  
                
              )
            }

            return (
              
                {step === 'add' && }
                {step === 'verify' && }
                {step === 'backupcodes' && }
                {step === 'success' && }
              
            )
          }

          const styles = StyleSheet.create({
            container: {
              flex: 1,
              backgroundColor: '#f9fafb',
            },
            contentContainer: {
              padding: 20,
              paddingBottom: 40,
            },
            loadingContainer: {
              flex: 1,
              justifyContent: 'center',
              alignItems: 'center',
            },
            loadingText: {
              fontSize: 14,
              color: '#6b7280',
              marginTop: 12,
            },
            errorContainer: {
              flex: 1,
              justifyContent: 'center',
              alignItems: 'center',
              padding: 20,
            },
            errorTitle: {
              fontSize: 24,
              fontWeight: 'bold',
              color: '#dc2626',
              marginBottom: 12,
            },
            title: {
              fontSize: 28,
              fontWeight: 'bold',
              color: '#111827',
              marginBottom: 8,
            },
            subtitle: {
              fontSize: 16,
              color: '#6b7280',
              marginBottom: 24,
              lineHeight: 24,
            },
            card: {
              backgroundColor: '#ffffff',
              borderRadius: 12,
              padding: 20,
              marginBottom: 16,
              borderWidth: 1,
              borderColor: '#e5e7eb',
              shadowColor: '#000',
              shadowOffset: { width: 0, height: 2 },
              shadowOpacity: 0.1,
              shadowRadius: 4,
              elevation: 3,
            },
            cardTitle: {
              fontSize: 18,
              fontWeight: '600',
              color: '#111827',
              marginBottom: 16,
            },
            qrSection: {
              alignItems: 'center',
            },
            qrContainer: {
              padding: 16,
              backgroundColor: '#ffffff',
              borderRadius: 12,
              marginBottom: 16,
            },
            uriSection: {
              marginBottom: 12,
            },
            uriLabel: {
              fontSize: 14,
              color: '#6b7280',
              marginBottom: 8,
            },
            uriContainer: {
              padding: 12,
              backgroundColor: '#f9fafb',
              borderRadius: 8,
              borderWidth: 1,
              borderColor: '#e5e7eb',
              marginBottom: 12,
            },
            uriText: {
              fontSize: 12,
              fontFamily: 'monospace',
              color: '#111827',
              lineHeight: 18,
            },
            switchButton: {
              paddingVertical: 10,
              paddingHorizontal: 16,
              backgroundColor: '#f9fafb',
              borderRadius: 8,
              alignItems: 'center',
            },
            switchButtonText: {
              fontSize: 14,
              fontWeight: '600',
              color: '#6366f1',
            },
            instructionsSection: {
              marginTop: 20,
              paddingTop: 20,
              borderTopWidth: 1,
              borderTopColor: '#e5e7eb',
            },
            instructionText: {
              fontSize: 14,
              color: '#6b7280',
              lineHeight: 24,
              marginBottom: 8,
            },
            inputGroup: {
              marginBottom: 16,
            },
            label: {
              fontSize: 14,
              fontWeight: '600',
              color: '#111827',
              marginBottom: 8,
            },
            input: {
              height: 56,
              backgroundColor: '#f9fafb',
              borderWidth: 1,
              borderColor: '#e5e7eb',
              borderRadius: 8,
              paddingHorizontal: 16,
              fontSize: 24,
              fontWeight: '600',
              color: '#111827',
              textAlign: 'center',
              letterSpacing: 8,
            },
            inputError: {
              borderColor: '#dc2626',
            },
            errorText: {
              fontSize: 12,
              color: '#dc2626',
              marginTop: 6,
            },
            hintBox: {
              padding: 12,
              borderRadius: 8,
              backgroundColor: '#f3f4f6',
              marginTop: 8,
            },
            hintText: {
              fontSize: 13,
              color: '#6b7280',
              lineHeight: 18,
              textAlign: 'center',
            },
            actionButtons: {
              flexDirection: 'row',
              gap: 12,
              marginTop: 8,
            },
            primaryButton: {
              flex: 1,
              paddingVertical: 14,
              paddingHorizontal: 20,
              backgroundColor: '#6366f1',
              borderRadius: 10,
              alignItems: 'center',
              justifyContent: 'center',
              minHeight: 50,
              shadowColor: '#000',
              shadowOffset: { width: 0, height: 2 },
              shadowOpacity: 0.15,
              shadowRadius: 3,
              elevation: 3,
            },
            primaryButtonText: {
              fontSize: 16,
              fontWeight: '600',
              color: '#ffffff',
            },
            secondaryButton: {
              flex: 1,
              paddingVertical: 14,
              paddingHorizontal: 20,
              backgroundColor: '#f9fafb',
              borderWidth: 1,
              borderColor: '#e5e7eb',
              borderRadius: 10,
              alignItems: 'center',
              justifyContent: 'center',
              minHeight: 50,
            },
            secondaryButtonText: {
              fontSize: 16,
              fontWeight: '600',
              color: '#6b7280',
            },
            successButton: {
              flex: 1,
              paddingVertical: 14,
              paddingHorizontal: 20,
              backgroundColor: '#10b981',
              borderRadius: 10,
              alignItems: 'center',
              justifyContent: 'center',
              minHeight: 50,
              shadowColor: '#000',
              shadowOffset: { width: 0, height: 2 },
              shadowOpacity: 0.15,
              shadowRadius: 3,
              elevation: 3,
            },
            successButtonText: {
              fontSize: 16,
              fontWeight: '600',
              color: '#ffffff',
            },
            fullWidthButton: {
              width: '100%',
              marginTop: 8,
            },
            buttonDisabled: {
              opacity: 0.6,
            },
            successBanner: {
              flexDirection: 'row',
              alignItems: 'center',
              backgroundColor: '#d1fae5',
              padding: 16,
              borderRadius: 12,
              marginBottom: 20,
            },
            successIcon: {
              fontSize: 24,
              marginRight: 12,
            },
            successBannerText: {
              fontSize: 18,
              fontWeight: '600',
              color: '#10b981',
            },
            warningBox: {
              padding: 16,
              borderRadius: 10,
              backgroundColor: '#fef2f2',
              marginTop: 16,
              marginBottom: 8,
            },
            warningText: {
              fontSize: 14,
              color: '#dc2626',
              lineHeight: 20,
              textAlign: 'center',
            },
            successContainer: {
              flex: 1,
              justifyContent: 'center',
              alignItems: 'center',
              padding: 20,
            },
            successCircle: {
              width: 80,
              height: 80,
              borderRadius: 40,
              backgroundColor: '#10b981',
              justifyContent: 'center',
              alignItems: 'center',
              marginBottom: 24,
            },
            successCheckmark: {
              fontSize: 48,
              color: '#ffffff',
              fontWeight: 'bold',
            },
            successScreenTitle: {
              fontSize: 32,
              fontWeight: 'bold',
              color: '#111827',
              marginBottom: 16,
            },
            successScreenText: {
              fontSize: 16,
              color: '#6b7280',
              textAlign: 'center',
              marginBottom: 8,
              lineHeight: 24,
            },
          })
          ```
