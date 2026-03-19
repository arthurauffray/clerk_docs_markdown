# useSignInWithGoogle()


> Clerk's useSignInWithGoogle() hook provides native Sign in with Google functionality for iOS and Android devices.

> [!IMPORTANT]
> This hook is available on iOS and Android devices and requires a native build. It will not work with Expo Go.

The `useSignInWithGoogle()` hook provides native [Sign in with Google](https://support.google.com/accounts/answer/12849458?hl=en) functionality for iOS and Android devices. It handles the ID token exchange with Clerk's backend and automatically manages the transfer flow between sign-up and sign-in.

## Installation

This hook requires the following peer dependency:

```bash
# Filename: terminal

npx expo install expo-crypto
```

## Returns

The `useSignInWithGoogle()` hook returns the `startGoogleAuthenticationFlow()` method, which you can use to initiate the native Google authentication flow.

### `startGoogleAuthenticationFlow()`

`startGoogleAuthenticationFlow()` has the following function signature:

```ts
function startGoogleAuthenticationFlow(
  startGoogleAuthenticationFlowParams?: StartGoogleAuthenticationFlowParams,
): Promise
```

#### Parameters

`startGoogleAuthenticationFlow()` accepts the following parameters (`StartGoogleAuthenticationFlowParams`):

- **`unsafeMetadata?`** [`SignUpUnsafeMetadata`](/reference/javascript/types/metadata#sign-up-unsafe-metadata)

  Metadata that can be read and set from the frontend and the backend. Once the authentication process is complete, the value of this field will be automatically copied to the created user's unsafe metadata (`User.unsafeMetadata`). One common use case is to collect custom information about the user during the authentication process and store it in this property. Read more about [unsafe metadata](/guides/users/extending#unsafe-metadata).


#### Returns

`startGoogleAuthenticationFlow()` returns the following:

- **`createdSessionId`** `string | null`

  The ID of the session that was created, if authentication is successful.

    ---

- **`setActive?`** `(params: SetActiveParams) => Promise<void>`

  A method used to set the active session and/or Organization. Accepts a [`SetActiveParams`](/reference/javascript/types/set-active-params) object.

    ---

- **`signIn?`** <code>[SignIn](/reference/javascript/sign-in) | undefined</code>

  The [`SignIn`](/reference/javascript/sign-in) object that was created, which holds the state of the current sign-in and provides helper methods to navigate and complete the sign-in process.

    ---

- **`signUp?`** <code>[SignUp](/reference/javascript/sign-up) | undefined</code>

  The [`SignUp`](/reference/javascript/sign-up) object that was created, which holds the state of the current sign-up and provides helper methods to navigate and complete the sign-up process.


## Examples

### Reusable component

The following example demonstrates how to use the [`useSignInWithGoogle()`](/reference/expo/native-hooks/use-sign-in-with-google) hook to manage the Google authentication flow. Because the `useSignInWithGoogle()` hook automatically manages the transfer flow between sign-up and sign-in, you can use this component for both your sign-up and sign-in pages.

```tsx
// Filename: components/GoogleSignInButton.tsx

import { useSignInWithGoogle } from '@clerk/expo/google'
import { useRouter } from 'expo-router'
import { Alert, Platform, StyleSheet, Text, TouchableOpacity, View } from 'react-native'

interface GoogleSignInButtonProps {
  onSignInComplete?: () => void
  showDivider?: boolean
}

export function GoogleSignInButton({
  onSignInComplete,
  showDivider = true,
}: GoogleSignInButtonProps) {
  const { startGoogleAuthenticationFlow } = useSignInWithGoogle()
  const router = useRouter()

  // Only render on iOS and Android
  if (Platform.OS !== 'ios' && Platform.OS !== 'android') {
    return null
  }

  const handleGoogleSignIn = async () => {
    try {
      const { createdSessionId, setActive } = await startGoogleAuthenticationFlow()

      if (createdSessionId && setActive) {
        await setActive({ session: createdSessionId })

        if (onSignInComplete) {
          onSignInComplete()
        } else {
          router.replace('/')
        }
      }
    } catch (err: any) {
      if (err.code === 'SIGN_IN_CANCELLED' || err.code === '-5') {
        return
      }

      Alert.alert('Error', err.message || 'An error occurred during Google sign-in')
      console.error('Sign in with Google error:', JSON.stringify(err, null, 2))
    }
  }

  return (
    <>
      
        Sign in with Google
      

      {showDivider && (
        
          OR
          
      )}
    </>
  )
}

const styles = StyleSheet.create({
  googleButton: {
    backgroundColor: '#4285F4',
    padding: 15,
    borderRadius: 8,
    alignItems: 'center',
    marginBottom: 10,
  },
  googleButtonText: {
    color: '#fff',
    fontSize: 16,
    fontWeight: '600',
  },
  divider: {
    flexDirection: 'row',
    alignItems: 'center',
    marginVertical: 20,
  },
  dividerLine: {
    flex: 1,
    height: 1,
    backgroundColor: '#ccc',
  },
  dividerText: {
    marginHorizontal: 10,
    color: '#666',
  },
})
```


### With custom metadata

The following example demonstrates how to pass custom metadata that will be saved to the user's [unsafe metadata](/guides/users/extending#unsafe-metadata) during sign-up.

```tsx
// Filename: app/(auth)/sign-in.tsx

import { useRouter } from 'expo-router'
import { useSignInWithGoogle } from '@clerk/expo/google'
import { Alert, Platform, TouchableOpacity, Text } from 'react-native'

export default function SignInPage() {
  const { startGoogleAuthenticationFlow } = useSignInWithGoogle()
  const router = useRouter()

  // Only show on iOS and Android
  if (Platform.OS !== 'ios' && Platform.OS !== 'android') {
    return null
  }

  const onGoogleSignInPress = async () => {
    try {
      const { createdSessionId, setActive } = await startGoogleAuthenticationFlow({
        // Add information about the user to their unsafe metadata
        unsafeMetadata: {
          referralSource: 'mobile-app',
          signupDate: new Date().toISOString(),
        },
      })

      if (createdSessionId && setActive) {
        // Set the created session as the active session
        await setActive({ session: createdSessionId })
        // Once the session is set as active,
        // redirect the user to the home page
        router.replace('/')
      }
    } catch (err: any) {
      // User canceled the sign-in flow
      if (err.code === 'SIGN_IN_CANCELLED' || err.code === '-5') {
        return
      }

      Alert.alert('Error', err.message || 'An error occurred during Google sign-in')
      console.error('Sign in with Google error:', JSON.stringify(err, null, 2))
    }
  }

  return (
    
      Sign in with Google
    
  )
}
```

## Error handling

The `useSignInWithGoogle()` hook may throw errors in the following scenarios:

- **User cancellation**: The user cancels the authentication flow, resulting in an error with code `SIGN_IN_CANCELLED` or `-5`.
- **Platform error**: The hook is called on an unsupported platform (not iOS or Android).
- **Authentication failure**: Google authentication fails or the returned ID token is invalid.
- **Play Services error** (Android only): Google Play Services is not available or outdated on the device.

> [!IMPORTANT]
> Always wrap calls to `startGoogleAuthenticationFlow()` in a `try/catch` block, and handle the `SIGN_IN_CANCELLED` and `-5` error codes separately.
