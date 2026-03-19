# Sign in with Apple


> Learn how to use Clerk to natively sign in with Apple in your Expo app.

This guide will teach you how to add native [Sign in with Apple](https://developer.apple.com/sign-in-with-apple/) to your Clerk Expo application.

> [!IMPORTANT]
> If you're using [native components](/reference/expo/native-components/overview), Sign in with Apple is automatically available in [``](/reference/expo/native-components/auth-view) when Apple is enabled as a social connection in the Clerk Dashboard. This guide applies to applications that implement a custom sign-in UI using the [`useSignInWithApple()`](/reference/expo/native-hooks/use-sign-in-with-apple) hook.

> [!NOTE]
> Sign in with Apple works on both iOS Simulators and physical devices. However, physical devices provide full functionality including biometric authentication (Face ID/Touch ID), while simulators have limited support. Always test on a physical device before releasing to production.


  ## Add your Native Application

  Add your iOS application to the [**Native applications**](https://dashboard.clerk.com/~/native-applications) page in the Clerk Dashboard. You will need your iOS app's **App ID Prefix** (Team ID) and **Bundle ID**.

  ## Enable Apple as a social connection

  1. In the Clerk Dashboard, navigate to the [**SSO connections**](https://dashboard.clerk.com/~/user-authentication/sso-connections) page.
  1. Select **Add connection** and select **For all users**.
  1. Select **Apple** from the provider list.
  1. Ensure that **Enable for sign-up and sign-in** is toggled on.

  > [!NOTE]
  > Apple provides a privacy feature called [Hide My Email](https://support.apple.com/en-us/HT210425#hideemail), allowing users to sign in to your app with Apple without disclosing their actual email addresses. Instead, your instance receives an app-specific email address that forwards any emails to the user's real address. To be able to send emails properly to users with hidden addresses, you must configure an additional setting in the Apple Developer portal. See [Configure Email Source for Apple Private Relay](/guides/configure/auth-strategies/social-connections/apple#configure-email-source-for-apple-private-relay) for more information.

  ## Install dependencies

  > [!IMPORTANT]
> If you're using [``](/reference/expo/native-components/auth-view) from `@clerk/expo/native`, you do **not** need to install `expo-apple-authentication`, `expo-crypto`, or use the `useSignInWithApple()` hook — `` handles the sign-in flow automatically.


  The [`useSignInWithApple()`](/reference/expo/native-hooks/use-sign-in-with-apple) hook requires the following packages:

  - `expo-apple-authentication` provides access to Apple's native [Sign in with Apple](https://docs.expo.dev/versions/latest/sdk/apple-authentication/) functionality.
  - `expo-crypto` is used for generating secure nonces during the authentication flow.

  ```npm
// Filename: terminal

  npx expo install expo-apple-authentication expo-crypto
  ```

  ## Add `expo-apple-authentication` to your app config

  Add the `expo-apple-authentication` plugin to your `app.json` or `app.config.js`.

  
**app.json:**

```json
// Filename: app.json

    {
      "expo": {
        "plugins": ["expo-apple-authentication"]
      }
    }
    ```


**app.config.js:**

```js
// Filename: app.config.js

    export default {
      expo: {
        plugins: ['expo-apple-authentication'],
      },
    }
    ```


  ## Build your authentication flow

  > [!IMPORTANT]
> If you're using [``](/reference/expo/native-components/auth-view) from `@clerk/expo/native`, you do **not** need to install `expo-apple-authentication`, `expo-crypto`, or use the `useSignInWithApple()` hook — `` handles the sign-in flow automatically.


  1. The following example demonstrates how to use the [`useSignInWithApple()`](/reference/expo/native-hooks/use-sign-in-with-apple) hook to manage the Apple authentication flow. Because the `useSignInWithApple()` hook automatically manages the transfer flow between sign-up and sign-in, you can use this component for both your sign-up and sign-in pages.

```tsx
// Filename: components/AppleSignInButton.tsx

import { useSignInWithApple } from '@clerk/expo/apple'
import { useRouter } from 'expo-router'
import { Alert, Platform, Pressable, StyleSheet, Text, View } from 'react-native'

export function AppleSignInButton({ onSignInComplete }: { onSignInComplete?: () => void }) {
  const { startAppleAuthenticationFlow } = useSignInWithApple()
  const router = useRouter()

  // Only show on iOS
  if (Platform.OS !== 'ios') return null

  const handleAppleSignIn = async () => {
    try {
      const { createdSessionId, setActive } = await startAppleAuthenticationFlow()

      if (createdSessionId && setActive) {
        await setActive({ session: createdSessionId })

        if (onSignInComplete) {
          onSignInComplete()
        } else {
          router.replace('/')
        }
      }
    } catch (err: any) {
      if (err.code === 'ERR_REQUEST_CANCELED') return

      Alert.alert('Error', err.message || 'An error occurred during Apple sign-in')
      console.error('Sign in with Apple error:', JSON.stringify(err, null, 2))
    }
  }

  return (
    
       [styles.button, pressed && styles.buttonPressed]}
        onPress={handleAppleSignIn}
      >
        Continue with Apple
      
    
  )
}

const styles = StyleSheet.create({
  container: {
    width: '100%',
    marginVertical: 8,
  },
  button: {
    backgroundColor: '#000',
    paddingVertical: 14,
    paddingHorizontal: 24,
    borderRadius: 8,
    alignItems: 'center',
  },
  buttonPressed: {
    opacity: 0.7,
  },
  buttonText: {
    color: '#fff',
    fontSize: 16,
    fontWeight: '600',
  },
})
```

  1. Then, add the `` component to your sign-in or sign-up page.

  ## Create a native build

  Create a native build with EAS Build or a local prebuild, since Apple Authentication is not supported in Expo Go.

  ```bash
# Filename: terminal

  # Using EAS Build
  eas build --platform ios

  # Or using local prebuild
  npx expo prebuild && npx expo run:ios --device
  ```
