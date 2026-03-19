# Add Box as a social connection


> Learn how to allow users to sign up and sign in to your Clerk app with their Box account using OAuth.

Enabling OAuth with Box allows your users to sign up and sign in to your Clerk app with their Box account.

## Configure for your development instance

For _development instances_, Clerk uses preconfigured shared OAuth credentials and redirect URIs—no other configuration is needed.

1. In the Clerk Dashboard, navigate to the [**SSO connections**](https://dashboard.clerk.com/~/user-authentication/sso-connections) page.
1. Select **Add connection** and select **For all users**.
1. Select **Box** from the provider list.

## Configure for your production instance

For _production instances_, you must provide custom credentials.

To make the setup process easier, it's recommended to keep two browser tabs open: one for the [Clerk Dashboard](https://dashboard.clerk.com/~/user-authentication/sso-connections) and one for your [Box Developer Console](https://app.box.com/developers/console).


  ### Enable Box as a social connection

  1. In the Clerk Dashboard, navigate to the [**SSO connections**](https://dashboard.clerk.com/~/user-authentication/sso-connections) page.
  1. Select **Add connection** and select **For all users**.
  1. Select **Box** from the provider list.
  1. Ensure that both **Enable for sign-up and sign-in** and **Use custom credentials** are toggled on.
  1. Save the **Redirect URI** somewhere secure. Keep this page open.

  ### Create a Box app

  1. On the homepage of the [Box Developer Console](https://app.box.com/developers/console), select **Custom App**. A modal will open.
  1. Fill out the necessary information. Use Box's [guide on OAuth 2.0 setup](https://developer.box.com/guides/authentication/oauth2/oauth2-setup/#app-creation-steps) to help you.
  1. Select **Next**.
  1. In the list of authentication methods, select **User Authentication (OAuth 2.0)**.
  1. Select **Create App**. You'll be redirected to the app's **Configuration** page.
  1. In the **OAuth 2.0 Redirect URIs** section, paste the **Redirect URI** value you saved from the Clerk Dashboard.
  1. In the **OAuth 2.0 Credentials** section, save the **Client ID** and **Client Secret** somewhere secure.

  ### Set the Client ID and Client Secret in the Clerk Dashboard

  1. Navigate back to the Clerk Dashboard where the configuration page should still be open. Paste the **Client ID** and **Client Secret** values that you saved into the respective fields.
1. Select **Save**.

> [!NOTE]
> If the page is no longer open, navigate to the [**SSO connections**](https://dashboard.clerk.com/~/user-authentication/sso-connections) page in the Clerk Dashboard. Select the connection. Under **Use custom credentials**, paste the values into their respective fields.


  ### Test your connection

  The simplest way to test your connection is to visit your Clerk app's [Account Portal](/guides/account-portal/overview), which is available for all Clerk apps out-of-the-box.

1. In the Clerk Dashboard, navigate to the [**Account Portal**](https://dashboard.clerk.com/~/account-portal) page.
1. Next to **Sign-in**, select the button to visit the sign-in page. The URL should resemble:
   - **For development** - `https://your-domain.accounts.dev/sign-in`
   - **For production** - `https://accounts.your-domain.com/sign-in`
1. Sign in with your connection's credentials.
