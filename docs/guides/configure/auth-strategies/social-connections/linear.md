# Add Linear as a social connection


> Learn how to allow users to sign up and sign in to your Clerk app with their Linear account using OAuth.

Enabling OAuth with [Linear](https://developers.linear.app/docs/oauth/authentication) allows your users to sign up and sign in to your Clerk app with their Linear account.

> [!IMPORTANT]
> You must be a workspace admin to create and manage OAuth apps in Linear.

## Configure for your development instance

For _development instances_, Clerk uses preconfigured shared OAuth credentials and redirect URIs—no other configuration is needed.

1. In the Clerk Dashboard, navigate to the [**SSO connections**](https://dashboard.clerk.com/~/user-authentication/sso-connections) page.
1. Select **Add connection** and select **For all users**.
1. Select **Linear** from the provider list.

## Configure for your production instance

For _production instances_, you must provide custom credentials.

To make the setup process easier, it's recommended to keep two browser tabs open: one for the [Clerk Dashboard](https://dashboard.clerk.com/~/user-authentication/sso-connections) and one for your [Linear's API settings](https://linear.app/clerk/settings/api) page.


  ### Enable Linear as a social connection in Clerk

  1. In the Clerk Dashboard, navigate to the [**SSO connections**](https://dashboard.clerk.com/~/user-authentication/sso-connections) page.
  1. Select **Add connection** and select **For all users**.
  1. Select **Linear** from the provider list.
  1. Ensure that both **Enable for sign-up and sign-in** and **Use custom credentials** are toggled on.
  1. Save the **Callback URL** somewhere secure. Keep this page open.

  ### Create a Linear app

  1. In the top-left of [Linear](https://linear.app/), select your workspace, then select **Settings**.
  1. In the sidenav, under **Account**, select **API**. Scroll down to **OAuth Applications** and select **Create new OAuth Application**. You'll be navigated to the [**Create new application**](https://linear.app/clerk/settings/api/applications/new) page.
  1. Complete the required fields. In **Callback URLs**, paste the **Redirect URI** you saved from the Clerk Dashboard.
  1. Select **Save**. The page will refresh and you should see the **Client ID** and **Client Secret** at the top. Save both values somewhere secure.

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
