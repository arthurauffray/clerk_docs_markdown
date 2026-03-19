# Deploy an Expo app to production


> Learn how to deploy an Expo app to production with Clerk.

There are a few caveats to deploying production Expo applications with Clerk. This guide will walk you through the steps to deploy your Expo app to production.

> [!IMPORTANT]
> If you're using [native components](/reference/expo/native-components/overview) or [native sign-in hooks](/reference/expo/overview#native-sign-in-hooks), you must add your application to the [**Native applications**](https://dashboard.clerk.com/~/native-applications) page in the Clerk Dashboard for your production instance. You will need your app's **Bundle ID** and **Team ID**.

## Acquire a domain

Before deploying your Expo app to production, you must acquire a domain. Even though there may not be a web application associated with an Expo app, Clerk still requires a domain for production instances.

## Configure your Expo app

With Clerk, you can [add OAuth flows in your Expo applications](/guides/development/custom-flows/authentication/oauth-connections).

Clerk ensures that security critical nonces are passed only to allowlisted URLs when the SSO flow is completed in native browsers or webviews. For maximum security in your **production** instances, you need to allowlist your custom redirect URLs via the [Clerk Dashboard](https://dashboard.clerk.com/) or the [Clerk Backend API](/reference/backend/redirect-urls/create-redirect-url).

To allowlist a redirect URL via the Clerk Dashboard:

1. In the Clerk Dashboard, navigate to the [**Native applications**](https://dashboard.clerk.com/~/native-applications) page.
1. Scroll down to the **Allowlist for mobile SSO redirect** section and add your redirect URLs.

> [!NOTE]
> By default, Clerk uses `{bundleIdentifier}://callback` as the redirect URL.


## Deploy to production

Now that you have acquired a domain and configured your Expo app, you can follow [the Clerk deployment guide](/guides/development/deployment/production).
