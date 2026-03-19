# Build a custom authentication flow using passkeys


> Learn how to use the Clerk API to build a custom authentication flow using passkeys.

> [!WARNING]
> This guide is for users who want to build a custom flow. To use a _prebuilt_ UI, use the [Account Portal pages](/guides/account-portal/overview) or [prebuilt components](/reference/components/overview).


> [!IMPORTANT]
> This guide uses the Core 2 `useSignIn()` and `useSignUp()` hooks, which are available in Core 3 SDKs by adding the `/legacy` subpath to the import path. If you're using a Core 2 SDK, remove the `/legacy` subpath.


Clerk supports passwordless authentication via [passkeys](/guides/configure/auth-strategies/sign-up-sign-in-options#passkeys), enabling users to sign in without having to remember a password. Instead, users select a passkey associated with their device, which they can use to authenticate themselves.

This guide demonstrates how to use the Clerk API to build a custom user interface for creating, signing users in with, and managing passkeys.

## Enable passkeys

To use passkeys, first enable the strategy in the [Clerk Dashboard](https://dashboard.clerk.com/~/user-authentication/user-and-authentication?user_auth_tab=passkeys).


  When setting up passkeys with Android, there are a few additional steps to follow. [Learn more about passkeys for Android](/reference/android/passkeys).


  When setting up passkeys with Expo, there are a few additional steps to follow. [Learn more about passkeys for Expo](/reference/expo/passkeys).


### Domain restrictions for passkeys

Passkeys are tied to the domain they are created on and **cannot be used across different domains**. However, passkeys **do work on subdomains** if they are registered on the root domain. For example:

- Passkeys created on `your-domain.com` **cannot be used** on `your-domain-admin.com` (different domains).
- Passkeys created on `your-domain.com` **can be used** on `accounts.your-domain.com` (subdomain of the same root domain).
- Passkeys created on `staging1.your-domain.com` **cannot be used** on `staging2.your-domain.com` (sibling subdomains) unless the passkey was scoped to `your-domain.com` (i.e. the shared root domain).

**If you're using [satellite domains](/guides/dashboard/dns-domains/satellite-domains)**, in both development and production, passkeys won't be portable between your primary domain and your satellite domains so you should avoid using them.

If you're **not** using satellite domains:

- **In development**, you can either:
  - **The recommended approach**. Use Clerk's [components](/reference/components/overview), [Elements](/guides/customizing-clerk/elements/overview), or custom flows, instead of the [Account Portal](/guides/account-portal/overview). This ensures the passkey is created and used entirely on your development domain, so passkeys created on `localhost` will only work on `localhost`.
  - Create a passkey directly through the Account Portal instead of your local application to keep it tied to the Account Portal's domain. Passkeys created on your Account Portal (e.g., `your-app.accounts.dev`) will only work on that domain, which can cause issues if you switch between `localhost` and the Account Portal during development. If you choose this approach, ensure all testing happens on the same domain where the passkey was created.

- **In production,** your Account Portal is usually hosted on a subdomain of your main domain (e.g. `accounts.your-domain.com`), enabling passkeys to work seamlessly across your app. However, as stated above, if you use **satellite domains**, passkeys will not work as intended.


## Create user passkeys


  > [!TIP]
> Examples for this SDK aren't available yet. For now, try adapting the  available example to fit your SDK.


To create a passkey for a user, you must call [`User.createPasskey()`](/reference/javascript/user#create-passkey), as shown in the following example:


  ```tsx
// Filename: components/CustomCreatePasskeysButton.tsx

  export function CreatePasskeyButton() {
    const { isSignedIn, user } = useUser()

    const createClerkPasskey = async () => {
      if (!isSignedIn) {
        // Handle signed out state
        return
      }

      try {
        await user?.createPasskey()
      } catch (err) {
        // See https://clerk.com/docs/guides/development/custom-flows/error-handling
        // for more info on error handling
        console.error('Error:', JSON.stringify(err, null, 2))
      }
    }

    return <button onClick={createClerkPasskey}>Create a passkey</button>
  }
  ```


  ```tsx
// Filename: app/components/create-passkeys-button.tsx

  import { ThemedText } from '@/components/themed-text'
  import { useUser } from '@clerk/expo'
  import { Pressable, StyleSheet } from 'react-native'

  export function CreatePasskeyButton() {
    const { isSignedIn, user } = useUser()

    const createClerkPasskey = async () => {
      if (!isSignedIn) {
        return
      }

      try {
        await user?.createPasskey()
      } catch (err) {
        // See https://clerk.com/docs/guides/development/custom-flows/error-handling
        // for more info on error handling
        console.error('Error:', JSON.stringify(err, null, 2))
      }
    }

    return (
       [
          styles.button,
          !isSignedIn && styles.buttonDisabled,
          pressed && styles.buttonPressed,
        ]}
        onPress={createClerkPasskey}
        disabled={!isSignedIn}
      >
        Create a passkey
      
    )
  }

  const styles = StyleSheet.create({
    button: {
      backgroundColor: '#0a7ea4',
      paddingVertical: 12,
      paddingHorizontal: 24,
      borderRadius: 8,
      alignItems: 'center',
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


## Sign a user in with a passkey

To sign a user into your Clerk app with a passkey, you must call [`SignIn.authenticateWithPasskey()`](/reference/javascript/sign-in#authenticate-with-passkey). This method allows users to choose from their discoverable passkeys, such as hardware keys or passkeys in password managers.


  
    > [!TIP]
> Examples for this SDK aren't available yet. For now, try adapting the  available example to fit your SDK.

  

  ```tsx
// Filename: components/SignInWithPasskeyButton.tsx

  export function SignInWithPasskeyButton() {
    const { signIn } = useSignIn()
    const router = useRouter()

    const signInWithPasskey = async () => {
      // 'discoverable' lets the user choose a passkey
      // without auto-filling any of the options
      try {
        const signInAttempt = await signIn?.authenticateWithPasskey({
          flow: 'discoverable',
        })

        if (signInAttempt?.status === 'complete') {
          await setActive({
            session: signInAttempt.createdSessionId,
            redirectUrl: '/',
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
          console.error(JSON.stringify(signInAttempt, null, 2))
        }
      } catch (err) {
        // See https://clerk.com/docs/guides/development/custom-flows/error-handling
        // for more info on error handling
        console.error('Error:', JSON.stringify(err, null, 2))
      }
    }

    return <button onClick={signInWithPasskey}>Sign in with a passkey</button>
  }
  ```


  ```tsx
// Filename: app/components/sign-in-with-passkey-button.tsx

  import { ThemedText } from '@/components/themed-text'
  import { useSignIn } from '@clerk/expo/legacy'
  import { useRouter } from 'expo-router'
  import { Pressable, StyleSheet } from 'react-native'

  export function SignInWithPasskeyButton() {
    const { signIn, setActive } = useSignIn()
    const router = useRouter()

    const signInWithPasskey = async () => {
      // 'discoverable' lets the user choose a passkey
      // without auto-filling any of the options
      try {
        const signInAttempt = await signIn?.authenticateWithPasskey({
          flow: 'discoverable',
        })

        if (signInAttempt?.status === 'complete') {
          await setActive?.({
            session: signInAttempt.createdSessionId,
            redirectUrl: '/',
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
          console.error(JSON.stringify(signInAttempt, null, 2))
        }
      } catch (err) {
        // See https://clerk.com/docs/guides/development/custom-flows/error-handling
        // for more info on error handling
        console.error('Error:', JSON.stringify(err, null, 2))
      }
    }

    return (
       [styles.button, pressed && styles.buttonPressed]}
        onPress={signInWithPasskey}
      >
        Sign in with a passkey
      
    )
  }

  const styles = StyleSheet.create({
    button: {
      backgroundColor: '#0a7ea4',
      paddingVertical: 12,
      paddingHorizontal: 24,
      borderRadius: 8,
      alignItems: 'center',
    },
    buttonPressed: {
      opacity: 0.7,
    },
    buttonText: {
      color: '#fff',
      fontWeight: '600',
    },
  })
  ```


## Rename user passkeys

Clerk generates a name based on the device associated with the passkey when it's created. Sometimes users may want to rename a passkey to make it easier to identify.


  
    > [!TIP]
> Examples for this SDK aren't available yet. For now, try adapting the  available example to fit your SDK.

  

  ```tsx
// Filename: components/RenamePasskeyUI.tsx

  export function RenamePasskeyUI() {
    const { user } = useUser()
    const { passkeys } = user

    const passkeyToUpdateId = useRef(null)
    const newPasskeyName = useRef(null)
    const [success, setSuccess] = useState(false)

    const renamePasskey = async () => {
      try {
        const passkeyToUpdate = passkeys?.find(
          (pk: PasskeyResource) => pk.id === passkeyToUpdateId.current?.value,
        )

        await passkeyToUpdate?.update({
          name: newPasskeyName.current?.value,
        })

        setSuccess(true)
      } catch (err) {
        // See https://clerk.com/docs/guides/development/custom-flows/error-handling
        // for more info on error handling
        console.error('Error:', JSON.stringify(err, null, 2))
        setSuccess(false)
      }
    }

    return (
      <>
        <p>Passkeys:</p>
        <ul>
          {passkeys?.map((pk: PasskeyResource) => {
            return (
              <li key={pk.id}>
                Name: {pk.name} | ID: {pk.id}
              </li>
            )
          })}
        </ul>
        <input ref={passkeyToUpdateId} type="text" placeholder="Enter the passkey ID" />
        <input type="text" placeholder="Enter the passkey's new name" ref={newPasskeyName} />
        <button onClick={renamePasskey}>Rename passkey</button>
        <p>Passkey updated: {success ? 'Yes' : 'No'}</p>
      </>
    )
  }
  ```


  ```tsx
// Filename: app/components/rename-passkey.tsx

  import { ThemedText } from '@/components/themed-text'
  import { ThemedView } from '@/components/themed-view'
  import { useUser } from '@clerk/expo'
  import { PasskeyResource } from '@clerk/shared/types'
  import { useState } from 'react'
  import { FlatList, Pressable, StyleSheet, TextInput, View } from 'react-native'

  export function RenamePasskeyUI() {
    const { user } = useUser()
    const passkeys = user?.passkeys

    const [passkeyToUpdateId, setPasskeyToUpdateId] = useState('')
    const [newPasskeyName, setNewPasskeyName] = useState('')
    const [success, setSuccess] = useState(false)

    const renamePasskey = async () => {
      try {
        const passkeyToUpdate = passkeys?.find((pk: PasskeyResource) => pk.id === passkeyToUpdateId)

        await passkeyToUpdate?.update({
          name: newPasskeyName,
        })

        setSuccess(true)
      } catch (err) {
        // See https://clerk.com/docs/guides/development/custom-flows/error-handling
        // for more info on error handling
        console.error('Error:', JSON.stringify(err, null, 2))
        setSuccess(false)
      }
    }

    return (
      
        
          Passkeys:
        

        {passkeys && passkeys.length > 0 ? (
           item.id}
            renderItem={({ item: pk }) => (
              
                
                  Name: {pk.name} | ID: {pk.id}
                
              
            )}
            style={styles.list}
          />
        ) : (
          No passkeys available
        )}

        Enter the passkey ID
        Enter the passkey's new name
         [
            styles.button,
            (!passkeyToUpdateId || !newPasskeyName) && styles.buttonDisabled,
            pressed && styles.buttonPressed,
          ]}
          onPress={renamePasskey}
          disabled={!passkeyToUpdateId || !newPasskeyName}
        >
          Rename passkey
        

        
          
            Passkey updated: {success ? 'Yes' : 'No'}
          
        
      
    )
  }

  const styles = StyleSheet.create({
    container: {
      flex: 1,
      padding: 20,
      gap: 12,
    },
    sectionTitle: {
      fontWeight: '600',
      fontSize: 16,
      marginBottom: 8,
    },
    list: {
      marginBottom: 16,
    },
    passkeyCard: {
      padding: 12,
      backgroundColor: '#f5f5f5',
      borderRadius: 8,
      marginBottom: 8,
    },
    passkeyText: {
      fontSize: 14,
      fontFamily: 'monospace',
    },
    infoText: {
      fontSize: 14,
      opacity: 0.8,
      marginBottom: 16,
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
    statusContainer: {
      padding: 12,
      borderRadius: 8,
      marginTop: 8,
    },
    successContainer: {
      backgroundColor: '#e8f5e9',
    },
    neutralContainer: {
      backgroundColor: '#f5f5f5',
    },
    successText: {
      color: '#2e7d32',
      fontWeight: '500',
    },
    neutralText: {
      color: '#666',
      fontWeight: '500',
    },
  })
  ```


## Delete user passkeys


  > [!TIP]
> Examples for this SDK aren't available yet. For now, try adapting the  available example to fit your SDK.


To delete a user's passkey from your Clerk app, you must call the [`delete()`](/reference/javascript/types/passkey-resource#delete) method of the passkey object, as shown in the following example:


  ```tsx
// Filename: components/DeletePasskeyUI.tsx

  export function DeletePasskeyUI() {
    const { user } = useUser()
    const { passkeys } = user

    const passkeyToDeleteId = useRef(null)
    const [success, setSuccess] = useState(false)

    const deletePasskey = async () => {
      const passkeyToDelete = passkeys?.find((pk: any) => pk.id === passkeyToDeleteId.current?.value)
      try {
        await passkeyToDelete?.delete()

        setSuccess(true)
      } catch (err) {
        // See https://clerk.com/docs/guides/development/custom-flows/error-handling
        // for more info on error handling
        console.error('Error:', JSON.stringify(err, null, 2))
        setSuccess(false)
      }
    }

    return (
      <>
        <p>Passkeys:</p>
        <ul>
          {passkeys?.map((pk: any) => {
            return (
              <li key={pk.id}>
                Name: {pk.name} | ID: {pk.id}
              </li>
            )
          })}
        </ul>
        <input ref={passkeyToDeleteId} type="text" placeholder="Enter the passkey ID" />
        <button onClick={deletePasskey}>Delete passkey</button>
        <p>Passkey deleted: {success ? 'Yes' : 'No'}</p>
      </>
    )
  }
  ```


  ```tsx
// Filename: app/components/delete-passkey.tsx

  import { ThemedText } from '@/components/themed-text'
  import { ThemedView } from '@/components/themed-view'
  import { useUser } from '@clerk/expo'
  import { PasskeyResource } from '@clerk/shared/types'
  import { useState } from 'react'
  import { FlatList, Pressable, StyleSheet, TextInput, View } from 'react-native'

  export function DeletePasskeyUI() {
    const { user } = useUser()
    const passkeys = user?.passkeys

    const [passkeyToDeleteId, setPasskeyToDeleteId] = useState('')
    const [success, setSuccess] = useState(false)

    const deletePasskey = async () => {
      const passkeyToDelete = passkeys?.find((pk: PasskeyResource) => pk.id === passkeyToDeleteId)
      try {
        await passkeyToDelete?.delete()

        setSuccess(true)
      } catch (err) {
        // See https://clerk.com/docs/guides/development/custom-flows/error-handling
        // for more info on error handling
        console.error('Error:', JSON.stringify(err, null, 2))
        setSuccess(false)
      }
    }

    return (
      
        
          Passkeys:
        

        {passkeys && passkeys.length > 0 ? (
           item.id}
            renderItem={({ item: pk }) => (
              
                
                  Name: {pk.name} | ID: {pk.id}
                
              
            )}
            style={styles.list}
          />
        ) : (
          No passkeys available
        )}

        Enter the passkey ID
         [
            styles.button,
            styles.dangerButton,
            !passkeyToDeleteId && styles.buttonDisabled,
            pressed && styles.buttonPressed,
          ]}
          onPress={deletePasskey}
          disabled={!passkeyToDeleteId}
        >
          Delete passkey
        

        
          
            Passkey deleted: {success ? 'Yes' : 'No'}
          
        
      
    )
  }

  const styles = StyleSheet.create({
    container: {
      flex: 1,
      padding: 20,
      gap: 12,
    },
    sectionTitle: {
      fontWeight: '600',
      fontSize: 16,
      marginBottom: 8,
    },
    list: {
      marginBottom: 16,
    },
    passkeyCard: {
      padding: 12,
      backgroundColor: '#f5f5f5',
      borderRadius: 8,
      marginBottom: 8,
    },
    passkeyText: {
      fontSize: 14,
      fontFamily: 'monospace',
    },
    infoText: {
      fontSize: 14,
      opacity: 0.8,
      marginBottom: 16,
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
    dangerButton: {
      backgroundColor: '#c62828',
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
    statusContainer: {
      padding: 12,
      borderRadius: 8,
      marginTop: 8,
    },
    successContainer: {
      backgroundColor: '#e8f5e9',
    },
    neutralContainer: {
      backgroundColor: '#f5f5f5',
    },
    successText: {
      color: '#2e7d32',
      fontWeight: '500',
    },
    neutralText: {
      color: '#666',
      fontWeight: '500',
    },
  })
  ```
