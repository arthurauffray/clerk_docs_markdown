# <AuthView />` component


> A native authentication component that provides complete sign-in and sign-up flows for iOS and Android.

> [!NOTE]
> This documents the native `` from `@clerk/expo/native`. For web projects, use the [web ``](/reference/components/authentication/sign-in) or [``](/reference/components/authentication/sign-up) components from `@clerk/expo/web`.

The `` component renders a complete native authentication interface using SwiftUI on iOS and Jetpack Compose on Android. It handles all authentication flows including email, phone, OAuth, passkeys, and multi-factor authentication. All methods enabled in your [Clerk Dashboard](https://dashboard.clerk.com) are automatically supported.

> [!IMPORTANT]
> Before using this component, ensure you meet the [Expo requirements](/reference/expo/native-components/overview#requirements).


## Usage

The following examples show how to use the `` in your Expo app. Use [`useAuth()`](/reference/hooks/use-auth) or [`useUser()`](/reference/hooks/use-user) in a `useEffect` to react to authentication state changes.

### Basic usage

```tsx
// Filename: app/(auth)/sign-in.tsx

import { AuthView } from '@clerk/expo/native'
import { useAuth } from '@clerk/expo'
import { useRouter } from 'expo-router'
import { useEffect } from 'react'

export default function SignInScreen() {
  const { isSignedIn } = useAuth()
  const router = useRouter()

  useEffect(() => {
    if (isSignedIn) {
      router.replace('/(home)')
    }
  }, [isSignedIn])

  return }
```

### Sign-in only

```tsx
```

### Sign-up only

```tsx
```

## Properties

- **`mode`** `'signIn' | 'signUp' | 'signInOrUp'`

  The authentication mode that determines which flows are available to the user. Defaults to `'signInOrUp'`.

- **`'signIn'` - Restricts the interface to sign-in flows only. Users can only authenticate with existing accounts.** `'signUp'` - Restricts the interface to sign-up flows only. Users can only create new accounts. `'signInOrUp'` - Automatically determines whether to sign users in or sign them up based on whether they already have an account. This is the default mode that provides seamless authentication without requiring users to choose between sign-in and sign-up.

  ---

- **`isDismissable`** `boolean`

  Whether the authentication view can be dismissed by the user. When `true`, a dismiss button appears. When `false`, no dismiss button is shown. Defaults to `false`.

    > [!IMPORTANT]
    > Do not set `isDismissable={true}` when rendering inside a React Native ``. The native dismiss button relies on SwiftUI (iOS) or Jetpack Compose (Android) to close the view, which cannot dismiss a React Native ``. Tapping the native dismiss button will not close the modal and may leave the screen unresponsive.


## Social connection (OAuth) configuration

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


## Platform support

| Platform | Status |
| - | - |
| iOS | Supported (SwiftUI) |
| Android | Supported (Jetpack Compose) |
| Web | Use [``](/reference/components/authentication/sign-in) from `@clerk/expo/web` |
