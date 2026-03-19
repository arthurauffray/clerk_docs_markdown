# Sign in with Google


> Learn how to use Clerk to natively sign in with Google in your Expo app.

This guide will teach you how to add native [Sign in with Google](https://support.google.com/accounts/answer/12849458?hl=en) to your Clerk Expo application. This is different from Google OAuth - if you want to use Google OAuth, see the [dedicated guide](/guides/configure/auth-strategies/social-connections/google).

To make the setup process easier, it's recommended to keep two browser tabs open - one for the [Clerk Dashboard](https://dashboard.clerk.com/~/user-authentication/sso-connections) and one for your [Google Cloud Console](https://console.cloud.google.com/).


  ## Enable Google as a social connection

  1. In the Clerk Dashboard, navigate to the [**SSO connections**](https://dashboard.clerk.com/~/user-authentication/sso-connections) page.
1. Select **Add connection** and select **For all users**.
1. Select **Google** from the provider list.
1. Ensure that both **Enable for sign-up and sign-in** and **Use custom credentials** are toggled on.
1. Save the **Authorized Redirect URI** somewhere secure. Keep this page open.


  ## Configure Google Cloud Console

  Before you can use Sign in with Google in your app, you need to create OAuth 2.0 credentials in the Google Cloud Console.

  ### Create a Google Cloud Project

  1. Navigate to the [Google Cloud Console](https://console.cloud.google.com/).
  1. Select an existing project or [create a new one](https://console.cloud.google.com/projectcreate). You'll be redirected to your project's **Dashboard** page.
  1. Enable the [**Google+ API**](https://console.cloud.google.com/apis/library/plus.googleapis.com?project=expo-testing-480017) for your project.

  ### Create OAuth 2.0 Credentials

  You'll need to create two sets of OAuth 2.0 credentials: one for your native platform and one for the web client. **Even if you are building a native app, you still need to create the web client for Clerk's token verification.**

  If you're building for both iOS and Android, ensure that you create all three sets of credentials (iOS, Android, and web).

  
#### iOS


      #### Create an iOS Client ID

      1. Navigate to [**APIs & Services**](https://console.cloud.google.com/apis/dashboard). Then, in the left sidebar, select **Credentials**.
      1. Next to **Credentials**, select **Create Credentials**. Then, select **OAuth client ID**. You might need to [configure your OAuth consent screen](https://support.google.com/cloud/answer/6158849#userconsent). Otherwise, you'll be redirected to the **Create OAuth client ID** page.
      1. For the **Application type**, select **iOS**.
      1. Complete the required fields:
         - **Name**: Add a name for your client.
         - **Bundle ID**: Add your iOS **Bundle ID**.
      1. Select **Create**. A modal will open with your **Client ID**. Copy and save the **Client ID** - you'll need this for `EXPO_PUBLIC_CLERK_GOOGLE_IOS_CLIENT_ID`.

      #### Create a Web Client ID and Client Secret

      1. In the same project, create another client. Next to **Credentials**, select **Create Credentials**. Then, select **OAuth client ID**.
1. For the **Application type**, select **Web application**.
1. Add a name (e.g., "Web client for token verification").
1. Under **Authorized redirect URIs**, select **Add URI** and paste the **Authorized Redirect URI** you saved from the Clerk Dashboard.
1. Select **Create**. A modal will open with your **Client ID** and **Client Secret**. Save these values somewhere secure. You'll need these for the following steps.

    

#### Android


      #### Create an Android Client ID

      1. In the same project, create another client. Next to **Credentials**, select **Create Credentials**. Then, select **OAuth client ID**.
      1. For the **Application type**, select **Android**.
      1. Complete the required fields:
         - **Package name**: Your package name is in your `app.json` or `app.config.ts` under the `expo.android.package` key.
         - **SHA-1 certificate fingerprint**: To get your SHA-1, run the following command in your terminal:

           > [!IMPORTANT]
           > Replace `path-to-debug-or-production-keystore` with the path to your debug or production keystore. By default, the debug keystore is located in `~/.android/debug.keystore`. It may ask for a keystore password, which is `android`. **You may need to install [OpenJDK](https://openjdk.org/) (Java) to run the `keytool` command.**

           ```sh
# Filename: terminal

           keytool -keystore path-to-debug-or-production-keystore -list -v
           ```
      1. Select **Create**. A modal will open with your **Client ID**.
      1. Copy and save the **Client ID** - you'll need this for `EXPO_PUBLIC_CLERK_GOOGLE_ANDROID_CLIENT_ID`.

      #### Create a Web Client ID and Client Secret

      1. In the same project, create another client. Next to **Credentials**, select **Create Credentials**. Then, select **OAuth client ID**.
1. For the **Application type**, select **Web application**.
1. Add a name (e.g., "Web client for token verification").
1. Under **Authorized redirect URIs**, select **Add URI** and paste the **Authorized Redirect URI** you saved from the Clerk Dashboard.
1. Select **Create**. A modal will open with your **Client ID** and **Client Secret**. Save these values somewhere secure. You'll need these for the following steps.

    

  ## Set the Client ID and Client Secret in the Clerk Dashboard (from your web client)

  1. Navigate back to the Clerk Dashboard where the configuration page should still be open. Paste the **Client ID** and **Client Secret** values that you saved into the respective fields.
1. Select **Save**.

> [!NOTE]
> If the page is no longer open, navigate to the [**SSO connections**](https://dashboard.clerk.com/~/user-authentication/sso-connections) page in the Clerk Dashboard. Select the connection. Under **Use custom credentials**, paste the values into their respective fields.


  ## Add your native application to Clerk

  
#### iOS


Add your iOS application to the [**Native Applications**](https://dashboard.clerk.com/~/native-applications) page in the Clerk Dashboard. You'll need your iOS app's **App ID Prefix** (Team ID) and **Bundle ID**.
    

#### Android


      Add your Android application to the [**Native Applications**](https://dashboard.clerk.com/~/native-applications) page in the Clerk Dashboard.

      - **Namespace**: A name for your application.
      - **Package name**: Your package name is in your `build.gradle` file, formatted as `com.example.myclerkapp`.
      - **SHA-256 certificate fingerprint**: To get your SHA-256, run the following command in your terminal:

        > [!IMPORTANT]
        > Replace `path-to-debug-or-production-keystore` with the path to your debug or production keystore. By default, the debug keystore is located in `~/.android/debug.keystore`. It may ask for a keystore password, which is `android`. **You may need to install [OpenJDK](https://openjdk.org/) to run the `keytool` command.**

        ```sh
# Filename: terminal

        keytool -keystore path-to-debug-or-production-keystore -list -v
        ```
    

  ## Configure environment variables

  Add the Google OAuth client IDs to your `.env` file. You'll have saved these values in the previous steps.

  
#### iOS


      ```bash
# Filename: .env

      EXPO_PUBLIC_CLERK_GOOGLE_WEB_CLIENT_ID=your-web-client-id.apps.googleusercontent.com
      EXPO_PUBLIC_CLERK_GOOGLE_IOS_CLIENT_ID=your-ios-client-id.apps.googleusercontent.com

      # (iOS only)
      # EXPO_PUBLIC_CLERK_GOOGLE_IOS_URL_SCHEME is the URL scheme for Google sign-in callback
      # Replace your-ios-client-id with the same <your-ios-client-id> from EXPO_PUBLIC_CLERK_GOOGLE_IOS_CLIENT_ID. It should only be the part of your iOS Client ID before ".apps.googleusercontent.com".
      EXPO_PUBLIC_CLERK_GOOGLE_IOS_URL_SCHEME=com.googleusercontent.apps.your-ios-client-id
      ```
    

#### Android


      ```bash
# Filename: .env

      EXPO_PUBLIC_CLERK_GOOGLE_WEB_CLIENT_ID=your-web-client-id.apps.googleusercontent.com
      EXPO_PUBLIC_CLERK_GOOGLE_ANDROID_CLIENT_ID=your-android-client-id.apps.googleusercontent.com
      ```
    

  ## Set up native Sign in with Google (iOS only)

  This step is for **iOS only** and is **optional**. Currently, Sign in with Google will open a web browser to initiate the flow. If you'd rather have the app handle the flow natively and not open a web browser, follow this step.

  ### Configure the Clerk Expo plugin

  The `@clerk/expo` config plugin configures the URL scheme needed for Google's authentication callback. Add the plugin to your `app.json` or `app.config.ts`, depending on your app's configuration:

  > [!QUIZ]
  > What is the difference between `app.json` and `app.config.ts`?
  >
  > ---
  >
  > `app.json` is for projects using static JSON configuration. `app.config.ts` is for projects that need dynamic configuration (environment variables, conditional logic, etc.). When both files exist, `app.config.ts` receives the values from `app.json` and can extend or override them.

  
#### app.json


      Replace `your-ios-client-id` with the same `<your-ios-client-id>` from your `EXPO_PUBLIC_CLERK_GOOGLE_IOS_CLIENT_ID` environment variable (it should only be the part of your iOS Client ID before ".apps.googleusercontent.com").

      ```json
// Filename: app.json

      {
        "expo": {
          "plugins": ["@clerk/expo"],
          "extra": {
            "EXPO_PUBLIC_CLERK_GOOGLE_IOS_URL_SCHEME": "com.googleusercontent.apps.your-ios-client-id"
          }
        }
      }
      ```
    

#### app.config.ts


      ```ts
// Filename: app.config.ts

      export default {
        expo: {
          plugins: ['@clerk/expo'],
          extra: {
            EXPO_PUBLIC_CLERK_GOOGLE_IOS_URL_SCHEME: process.env.EXPO_PUBLIC_CLERK_GOOGLE_IOS_URL_SCHEME,
          },
        },
      }
      ```
    

  The plugin resolves the `EXPO_PUBLIC_CLERK_GOOGLE_IOS_URL_SCHEME` value from either of the following:

  1. An environment variable (recommended for EAS builds, configured in `eas.json`).
  1. The `config.extra` field in your app config.

  For EAS builds, add the environment variable to your build profile in `eas.json`:

  ```json
// Filename: eas.json

  {
    "build": {
      "development": {
        "env": {
          "EXPO_PUBLIC_CLERK_GOOGLE_IOS_URL_SCHEME": "com.googleusercontent.apps.your-ios-client-id"
        }
      }
    }
  }
  ```

  ## Build your authentication flow

  > [!IMPORTANT]
> If you're using [``](/reference/expo/native-components/auth-view) from `@clerk/expo/native`, you do **not** need to install `expo-crypto` or use the `useSignInWithGoogle()` hook — `` handles the sign-in flow automatically.


  1. The [`useSignInWithGoogle()`](/reference/expo/native-hooks/use-sign-in-with-google) hook requires `expo-crypto` for generating secure nonces during the authentication flow.
     ```bash
# Filename: terminal

     npx expo install expo-crypto
     ```
  1. The following example demonstrates how to use the [`useSignInWithGoogle()`](/reference/expo/native-hooks/use-sign-in-with-google) hook to manage the Google authentication flow. Because the `useSignInWithGoogle()` hook automatically manages the transfer flow between sign-up and sign-in, you can use this component for both your sign-up and sign-in pages.

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

  1. Then, add the `` component to your sign-in or sign-up page.

  ## Create a native build

  Create a native build with EAS Build or a local prebuild, since Google Authentication is not supported in Expo Go.

  ```bash
# Filename: terminal

  # Using EAS Build
  eas build --platform ios
  eas build --platform android

  # Or using local prebuild
  npx expo prebuild && npx expo run:ios --device
  npx expo prebuild && npx expo run:android --device
  ```
