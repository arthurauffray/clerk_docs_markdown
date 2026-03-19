# Add Dropbox as a social connection


> Learn how to allow users to sign up and sign in to your Clerk app with their Dropbox account using OAuth.

Enabling OAuth with Dropbox allows your users to sign up and sign in to your Clerk application with their Dropbox account.

## Configure for your development instance

For _development instances_, Clerk uses preconfigured shared OAuth credentials and redirect URIs—no other configuration is needed.

1. In the Clerk Dashboard, navigate to the [**SSO connections**](https://dashboard.clerk.com/~/user-authentication/sso-connections) page.
1. Select **Add connection** and select **For all users**.
1. Select **Dropbox** from the provider list.

## Configure for your production instance

For _production instances_, you must provide custom credentials.

To make the setup process easier, it's recommended to keep two browser tabs open: one for the [Clerk Dashboard](https://dashboard.clerk.com/~/user-authentication/sso-connections) and one for your [Dropbox App Console](https://www.dropbox.com/developers/apps).


  ### Enable Dropbox as a social connection

  1. In the Clerk Dashboard, navigate to the [**SSO connections**](https://dashboard.clerk.com/~/user-authentication/sso-connections) page.
  1. Select **Add connection** and select **For all users**.
  1. Select **Dropbox** from the provider list.
  1. Ensure that both **Enable for sign-up and sign-in** and **Use custom credentials** are toggled on.
  1. Save the **Redirect URI** somewhere secure. Keep this page open.

  ### Configure your Dropbox app

  1. In the [Dropbox App Console](https://www.dropbox.com/developers/apps), select a project or [create a new one](https://www.dropbox.com/developers/apps/create).
  1. On your app's **Settings** page, save the **App key** and **App secret** somewhere secure.
  1. In the **Redirect URIs** input, paste the **Redirect URI** value you saved from the Clerk Dashboard and select **Add**.

  ### Set the App Key and App Secret in the Clerk Dashboard

  1. Navigate back to the Clerk Dashboard where the configuration page should still be open. Paste the **App key** and **App secret** values that you saved into the respective fields.
  1. Select **Save**.

  > [!NOTE]
  > If the page is no longer open, navigate to the [**SSO connections**](https://dashboard.clerk.com/~/user-authentication/sso-connections) page in the Clerk Dashboard. Select the connection. Under **Use custom credentials**, you can paste the values into their respective fields.

  ### Test your connection

  The simplest way to test your connection is to visit your Clerk app's [Account Portal](/guides/account-portal/overview), which is available for all Clerk apps out-of-the-box.

1. In the Clerk Dashboard, navigate to the [**Account Portal**](https://dashboard.clerk.com/~/account-portal) page.
1. Next to **Sign-in**, select the button to visit the sign-in page. The URL should resemble:
   - **For development** - `https://your-domain.accounts.dev/sign-in`
   - **For production** - `https://accounts.your-domain.com/sign-in`
1. Sign in with your connection's credentials.
