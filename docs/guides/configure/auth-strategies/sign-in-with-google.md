# Sign in with Google


> Learn how to use Clerk to natively sign in with Google in your Android app.

This guide will teach you how to add native [Sign in with Google](https://support.google.com/accounts/answer/12849458?hl=en) to your Clerk apps on Android platforms. This is different from Google OAuth - if you want to use Google OAuth, see the [dedicated guide](/guides/configure/auth-strategies/social-connections/google).

To make the setup process easier, it's recommended to keep two browser tabs open - one for the [Clerk Dashboard](https://dashboard.clerk.com/~/user-authentication/sso-connections) and one for your [Google Cloud Console](https://console.cloud.google.com/).


  ## Enable Google as a social connection

  1. In the Clerk Dashboard, navigate to the [**SSO connections**](https://dashboard.clerk.com/~/user-authentication/sso-connections) page.
1. Select **Add connection** and select **For all users**.
1. Select **Google** from the provider list.
1. Ensure that both **Enable for sign-up and sign-in** and **Use custom credentials** are toggled on.
1. Save the **Authorized Redirect URI** somewhere secure. Keep this page open.


  ## Create the Google Developer Android client

  1. Navigate to the [Google Cloud Console](https://console.cloud.google.com/).
  1. Select an existing project or [create a new one](https://console.cloud.google.com/projectcreate). You'll be redirected to your project's **Dashboard** page.
  1. In the top-left, select the menu icon (**≡**) and select **APIs & Services**. Then, select **Credentials**.
  1. Next to **Credentials**, select **Create Credentials**. Then, select **OAuth client ID.** You might need to [configure your OAuth consent screen](https://support.google.com/cloud/answer/6158849#userconsent). Otherwise, you'll be redirected to the **Create OAuth client ID** page.
  1. For the **Application type**, select **Android**.
  1. Complete the required fields.
     - **Package name**: Your package name is in your `build.gradle` file, formatted as `com.example.myclerkapp`.
     - **SHA-1 certificate fingerprint**: To get your SHA-1, run the following command in your terminal:

       > [!IMPORTANT]
       > Replace `path-to-debug-or-production-keystore` with the path to your debug or production keystore. By default, the debug keystore is located in `~/.android/debug.keystore`. It may ask for a keystore password, which is `android`. **You may need to install [OpenJDK](https://openjdk.org/) to run the `keytool` command.**

       ```sh
# Filename: terminal

       keytool -keystore path-to-debug-or-production-keystore -list -v
       ```
  1. Select **Create**.

  ## Create the Google Developer Web client

  1. In the same project, create another client. Next to **Credentials**, select **Create Credentials**. Then, select **OAuth client ID.**
  1. For the **Application type**, select **Web Application**.
  1. Complete the required fields. In the **Authorized Redirect URIs** setting, paste the **Authorized Redirect URI** value you saved from the Clerk Dashboard.
  1. Select **Create**. A modal will open with your **Client ID** and **Client Secret**. Save these values somewhere secure.

  ## Set the Client ID and Client Secret in the Clerk Dashboard

  1. Navigate back to the Clerk Dashboard where the configuration page should still be open. Paste the **Client ID** and **Client Secret** values that you saved into the respective fields.
1. Select **Save**.

> [!NOTE]
> If the page is no longer open, navigate to the [**SSO connections**](https://dashboard.clerk.com/~/user-authentication/sso-connections) page in the Clerk Dashboard. Select the connection. Under **Use custom credentials**, paste the values into their respective fields.


  ## Test your connection

  The simplest way to test your connection is to visit your Clerk app's [Account Portal](/guides/account-portal/overview), which is available for all Clerk apps out-of-the-box.

1. In the Clerk Dashboard, navigate to the [**Account Portal**](https://dashboard.clerk.com/~/account-portal) page.
1. Next to **Sign-in**, select the button to visit the sign-in page. The URL should resemble:
   - **For development** - `https://your-domain.accounts.dev/sign-in`
   - **For production** - `https://accounts.your-domain.com/sign-in`
1. Sign in with your connection's credentials.


  > [!WARNING]
  > Sign in with Google [**does not** allow users to sign in via in-app browsers](https://developers.googleblog.com/en/modernizing-oauth-interactions-in-native-apps-for-better-usability-and-security).


## Usage

To learn how to build a sign-up and sign-in flow that supports OAuth connections in your Android application, see the [custom flow guide](/guides/development/custom-flows/authentication/oauth-connections).
