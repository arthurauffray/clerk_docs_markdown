# Remix SPA Mode


> Clerk supports Remix SPA mode out-of-the-box.

> [!WARNING]
> The Remix SDK is in maintenance mode and will only receive security updates. Please migrate to the [React Router SDK](/react-router/getting-started/quickstart) for continued development and new features.


This guide explains how to use Clerk with [Remix in SPA mode](https://remix.run/docs/en/main/guides/spa-mode). To use Clerk with Remix in SSR mode, follow the [Remix quickstart](/remix/getting-started/quickstart).


  ## Install `@clerk/remix`

  The [Clerk Remix SDK](/reference/remix/overview) gives you access to prebuilt components, hooks, and helpers to make user authentication easier.

  Run the following command to install the SDK:

  ```npm
  npm install @clerk/remix
  ```

  ## Set your environment variables

  
  Add your Clerk Publishable Key to your `.env` file.


  1. In the Clerk Dashboard, navigate to the [**API keys**](https://dashboard.clerk.com/~/api-keys) page.
  1. In the **Quick Copy** section, copy your Clerk Publishable Key.
  1. Paste your key into your `.env` file.

  The final result should resemble the following:


  > [!WARNING]
  > You will not need the Clerk Secret Key in Remix SPA mode, as it should never be used on the client-side.

  ```env
// Filename: .env

  VITE_CLERK_PUBLISHABLE_KEY={{pub_key}}
  ```

  ## Configure `ClerkApp`

  Clerk provides a `ClerkApp` wrapper to provide the authentication state to your React tree. You must pass your Publishable Key to `ClerkApp`.

  ```tsx
// Filename: app/root.tsx

  import { ClerkApp } from '@clerk/remix'
  import { Links, Meta, Outlet, Scripts, ScrollRestoration } from '@remix-run/react'

  function App() {
    return (
      <html lang="en">
        <head>
          <meta charSet="utf-8" />
          <meta name="viewport" content="width=device-width, initial-scale=1" />
          </head>
        <body>
          </body>
      </html>
    )
  }

  // Import your Publishable Key
  const PUBLISHABLE_KEY = import.meta.env.VITE_CLERK_PUBLISHABLE_KEY

  // Wrap your app with `ClerkApp`
  export default ClerkApp(App, {
    publishableKey: PUBLISHABLE_KEY,
  })
  ```

  ## Update your paths through `ClerkApp` options

  Next, add paths to your `ClerkApp` [options](/reference/remix/clerk-app#clerk-app-options) to control the behavior of the components when you sign in or sign up.

  ```ts
// Filename: app/root.tsx

  export default ClerkApp(App, {
    publishableKey: PUBLISHABLE_KEY,
    signInFallbackRedirectUrl: '/',
    signUpFallbackRedirectUrl: '/',
  })
  ```

  ## Protect your pages

  To protect your pages on the client-side, Clerk's [prebuilt control components](/reference/components/overview#control-components) control the visibility of content based on the user's authentication state.

  The following example uses the following components:

  - [``](/reference/components/control/show): Children of this component can only be seen while **signed in**.
  - [``](/reference/components/control/show): Children of this component can only be seen while **signed out**.
  - [``](/reference/components/user/user-button): Shows the signed-in user's avatar. Selecting it opens a dropdown menu with account management options.
  - [``](/reference/components/unstyled/sign-in-button): An unstyled component that links to the sign-in page. In this example, since no props or [environment variables](/guides/development/clerk-environment-variables) are set for the sign-in URL, this component links to the [Account Portal sign-in page](/guides/account-portal/overview#sign-in).

  ```tsx
// Filename: routes/_index.tsx

  import { Show, SignInButton, SignOutButton, SignUpButton, UserButton } from '@clerk/remix'

  export default function Index() {
    return (
      <div>
        <h1>Index Route</h1>
        
          <p>You are signed in!</p>

          <p>You are signed out</p>

          </div>
    )
  }
  ```


## Next steps

Learn more about Clerk components, how to customize them, and how to use Clerk's client-side helpers using the following guides.


  - [Prebuilt components](/reference/components/overview)
  - Learn how to quickly add authentication to your app using Clerk's suite of components.

  ---

  - [Customization & localization](/guides/customizing-clerk/appearance-prop/overview)
  - Learn how to customize and localize Clerk components.

  ---

  - [Client-side helpers](/remix/guides/users/reading#client-side)
  - Learn more about Clerk's client-side helpers and how to use them.

  ---

  - [Clerk Remix SDK Reference](/reference/remix/overview)
  - Learn about the Clerk Remix SDK and how to integrate it into your app.
