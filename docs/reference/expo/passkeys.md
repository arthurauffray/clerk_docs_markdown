# Configure passkeys for Expo


> Learn how to configure passkeys for your Expo application.

[Passkeys](/guides/configure/auth-strategies/sign-up-sign-in-options#passkeys) are a secure, passwordless authentication method that use biometrics and a physical device to authenticate users. This guide shows you how to configure passkeys for your Expo application.

> [!WARNING]
> This API is available only for [`@clerk/clerk-expo >=2.2.0` and `@clerk/expo`](/guides/development/upgrading/upgrade-guides/expo-v2).


  ## Enable passkeys

  To use passkeys, first enable the strategy in the [Clerk Dashboard](https://dashboard.clerk.com/~/user-authentication/user-and-authentication?user_auth_tab=passkeys).

  ## Configure passkeys

  Use the following tabs to configure your passkeys for `iOS` or `Android`.

  
#### iOS


      > [!WARNING]
      > iOS supports passkeys from version iOS 16+
      >
      > This library includes native code and will not work when running Expo Go. Instead, use a development build by running `npx expo run:ios`.

      ### Get your App ID Prefix and Bundle ID from Apple

      To get your **App ID Prefix** and **Bundle ID**, follow these steps:

      1. Navigate to the [Apple Developer dashboard](https://developer.apple.com/account).
      1. Under **Certificates, IDs and Profiles**, select [**Identifiers**](https://developer.apple.com/account/resources/identifiers/list).
      1. In the top-right, select the dropdown and select **App IDs**.
      1. Select the **App ID** you want to configure passkeys for. You'll be redirect to the **Review your App ID Configuration** page.
      1. At the top of the page, you'll see your **App ID Prefix** and **Bundle ID**. Save these values somewhere secure.

      ### Set up your associated domain file in the Clerk Dashboard

      1. In the Clerk Dashboard, navigate to the [**Native applications**](https://dashboard.clerk.com/~/native-applications) page.
      1. Select the **iOS** tab.
      1. Select **Add iOS App**.
      1. Paste the **App ID Prefix** and **Bundle ID** that you copied in the previous step.
      1. Select **Add App**.
      1. On the right-side, save your Frontend API URL somewhere secure.

      ### Update `app.json` in your Expo app

      1. In your app's `app.json` file, under the `ios` object, add the `associatedDomains` property as shown in the following example. Replace `` with the Frontend API URL value that you saved in the previous step.

      ```json
// Filename: app.json

      {
        "expo": {
          //...existing properties
          "plugins": [
            [
              "expo-build-properties",
              {
                "ios": {
                  "deploymentTarget": "16.0" //  iOS Support passkeys from version iOS 16+
                }
              }
            ]
          ],
          "ios": {
            //...existing properties
            "associatedDomains": [
              "applinks:",
              "webcredentials:"
            ]
          }
        }
      }
      ```
    

#### Android


      > [!WARNING]
      > Android supports passkeys from version 9+. Passkeys will not work with Android emulators. You must use a physical device.
      >
      > This library includes native code and [will not work when running Expo Go](https://docs.expo.dev/workflow/customizing/#using-libraries-that-include-native-code). Instead, use a development build by running `npx expo run:android`.

      ### Set up your Android app links in the Clerk Dashboard

      1. In the Clerk Dashboard, navigate to the [**Native applications**](https://dashboard.clerk.com/~/native-applications) page.
      1. Select the **Android** tab.
      1. Select **Add Android app**.
      1. Fill out the form with the following information:
         - The `namespace` (This guide uses the default value: `android_app`)
         - Your Android app's package name
         - The `SHA256 certificate fingerprints`. If you don't know where to find the `SHA256 certificate fingerprints`, see the [Expo docs](https://docs.expo.dev/linking/android-app-links/#create-assetlinksjson-file).
      1. After submitting the form, you can verify that your `assetlinks.json` file is properly associated with your app by using [Google's **Statement List Generator and Tester**](https://developers.google.com/digital-asset-links/tools/generator).
      1. On the right-side, save your Frontend API URL somewhere secure.

      ### Install `expo-build-properties` in your Expo application

      ```npm
      npm install expo-build-properties
      ```

      ### Update `app.json` in your Expo application

      1. In your app's `app.json` file, under `android`, add the `intentFilters` property as shown in the following example. Replace `` with the Frontend API URL value that you saved in the previous step.

      ```json
// Filename: app.json

      {
        "expo": {
          "plugins": [["expo-build-properties"]],
          "android": {
            //...existing properties
            "intentFilters": [
              {
                "action": "VIEW",
                "autoVerify": true,
                "data": [
                  {
                    "scheme": "https",
                    "host": ""
                  }
                ],
                "category": ["BROWSABLE", "DEFAULT"]
              }
            ]
          }
        }
      }
      ```
    

  ## Install `@clerk/expo-passkeys`

  Run the following command to install the `@clerk/expo-passkeys` package:

  ```npm
  npm install @clerk/expo-passkeys
  ```

  ## Prebuild Expo project

  Run the following command to prebuild your Expo project:

  ```bash
# Filename: terminal

  npx expo prebuild
  ```

  ## Update your ``

  Pass the `passkeys` object to the `__experimental_passkeys` property of your `` component, as shown in the following example:

  ```tsx
// Filename: app/_layout.tsx

  import { ClerkProvider } from '@clerk/expo'
  import { Slot } from 'expo-router'
  import { tokenCache } from '@clerk/expo/token-cache'
  import { passkeys } from '@clerk/expo/passkeys'

  // Import your Publishable Key
  const publishableKey = process.env.EXPO_PUBLIC_CLERK_PUBLISHABLE_KEY

  if (!publishableKey) {
    throw new Error('Add your Clerk Publishable Key to the .env file')
  }

  export default function RootLayout() {
    return (
      
        
    )
  }
  ```


## Usage

To learn how to use passkeys in your Expo application, such as creating, deleting, and authenticating users with passkeys, see the [custom flow guide](/guides/development/custom-flows/authentication/passkeys).
