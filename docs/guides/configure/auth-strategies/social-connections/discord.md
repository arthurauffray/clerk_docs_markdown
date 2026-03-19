# Add Discord as a social connection


> Learn how to allow users to sign up and sign in to your Clerk app with their Discord account with OAuth.

Enabling OAuth with [Discord](https://discord.com/developers/docs/topics/oauth2) allows your users to sign up and sign in to your Clerk application with their Discord account.

## Configure for your development instance

For _development instances_, Clerk uses preconfigured shared OAuth credentials and redirect URIs—no other configuration is needed.

1. In the Clerk Dashboard, navigate to the [**SSO connections**](https://dashboard.clerk.com/~/user-authentication/sso-connections) page.
1. Select **Add connection** and select **For all users**.
1. Select **Discord** from the provider list.

## Configure for your production instance

For _production instances_, you must provide custom credentials.

To make the setup process easier, it's recommended to keep two browser tabs open: one for the [Clerk Dashboard](https://dashboard.clerk.com/~/user-authentication/sso-connections) and one for your [Discord Developer Portal](https://discord.com/developers/applications).


  ### Enable Discord as a social connection in Clerk

  1. In the Clerk Dashboard, navigate to the [**SSO connections**](https://dashboard.clerk.com/~/user-authentication/sso-connections) page.
  1. Select **Add connection** and select **For all users**.
  1. Select **Discord** from the provider list.
  1. Ensure that both **Enable for sign-up and sign-in** and **Use custom credentials** are toggled on.
  1. Save the **Redirect URI** somewhere secure. Keep this page open.

  ### Create a Discord Developer app

  1. On a separate page, go to the [Discord Developer Portal](https://discord.com/developers/applications) and sign in.
  1. In the top-right, select **New Application**.
  1. Complete the required fields and select **Create**. You'll be redirected to the **General Information** page.
  1. In the left sidenav, select **OAuth2**.
  1. Under **Redirects**, select **Add Redirect**. Paste the **Redirect URI** you saved from the Clerk Dashboard.
  1. Select **Save Changes**. You may need to tap anywhere on the screen for the button to show.
  1. Save the **Client ID** and **Client Secret** somewhere secure. If you don't see the **Copy** button under the **Client Secret**, select **Reset Secret** to generate a new one.

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
