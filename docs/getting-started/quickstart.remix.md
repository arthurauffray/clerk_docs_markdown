# Remix Quickstart


> Learn how to use Clerk to quickly and easily add secure authentication and user management to your Remix application.

> [!WARNING]
> The Remix SDK is in maintenance mode and will only receive security updates. Please migrate to the [React Router SDK](/react-router/getting-started/quickstart) for continued development and new features.


Learn how to use Clerk to quickly and easily add secure authentication and user management to your Remix app. This guide assumes that you are using Remix v2 or later.

> [!NOTE]
> If you are using Remix SPA mode, follow the [Remix SPA mode guide](/guides/development/spa-mode).


  ## Create a new Remix app

  If you don't already have a Remix app, run the following commands to [create a new one](https://v2.remix.run/docs/start/quickstart).

  ```npm
  npx create-remix@latest clerk-remix
  cd clerk-remix
  npm install
  ```

  ## Install `@clerk/remix`

  The [Clerk Remix SDK](/reference/remix/overview) gives you access to prebuilt components, hooks, and helpers to make user authentication easier.

  Run the following command to install the SDK:

  ```npm
  npm install @clerk/remix
  ```

  ## Set your Clerk API keys

  
  Add the following keys to your `.env` file. These keys can always be retrieved from the [**API keys**](https://dashboard.clerk.com/~/api-keys) page in the Clerk Dashboard.


  1. In the Clerk Dashboard, navigate to the [**API keys**](https://dashboard.clerk.com/~/api-keys) page.
  1. In the **Quick Copy** section, copy your Clerk Publishable Key and Secret Key.
  1. Paste your keys into your `.env` file.

  The final result should resemble the following:


  ```env
// Filename: .env

  CLERK_PUBLISHABLE_KEY={{pub_key}}
  CLERK_SECRET_KEY={{secret}}
  ```

  ## Configure `rootAuthLoader()`

  The [`rootAuthLoader()`](/reference/remix/root-auth-loader) function is a helper function that provides the authentication state to your Remix application. You must export `rootAuthLoader()` as the root `loader()` function.

  Update your `root.tsx` file with the following code:

  ```tsx
// Filename: app/root.tsx

  import type { MetaFunction, LoaderFunction } from '@remix-run/node'
  import { Links, Meta, Outlet, Scripts, ScrollRestoration } from '@remix-run/react'

  // Import `rootAuthLoader()`
  import { rootAuthLoader } from '@clerk/remix/ssr.server'

  export const meta: MetaFunction = () => [
    {
      charset: 'utf-8',
      title: 'New Remix App',
      viewport: 'width=device-width,initial-scale=1',
    },
  ]

  // Export `rootAuthLoader()` as the root route `loader`
  export const loader: LoaderFunction = (args) => rootAuthLoader(args)

  export function Layout({ children }: { children: React.ReactNode }) {
    return (
      <html lang="en">
        <head>
          </head>
        <body>
          {children}
          </body>
      </html>
    )
  }

  export default function App() {
    return }
  ```

  ## Configure `ClerkApp`

  Clerk provides a [`ClerkApp`](/reference/remix/clerk-app) wrapper to provide the authentication state to your React tree. This helper works with Remix SSR out-of-the-box and follows the "higher-order component" paradigm.

  Update your `root.tsx` file with the following code:

  ```tsx
// Filename: app/root.tsx

  import type { MetaFunction, LoaderFunction } from '@remix-run/node'

  import { Links, Meta, Outlet, Scripts, ScrollRestoration } from '@remix-run/react'

  import { rootAuthLoader } from '@clerk/remix/ssr.server'
  // Import ClerkApp
  import { ClerkApp } from '@clerk/remix'

  export const meta: MetaFunction = () => [
    {
      charset: 'utf-8',
      title: 'New Remix App',
      viewport: 'width=device-width,initial-scale=1',
    },
  ]

  export const loader: LoaderFunction = (args) => rootAuthLoader(args)

  export function Layout({ children }: { children: React.ReactNode }) {
    return (
      <html lang="en">
        <head>
          </head>
        <body>
          {children}
          </body>
      </html>
    )
  }

  function App() {
    return }

  // Wrap your app with `ClerkApp`
  export default ClerkApp(App)
  ```

  ## Protect your pages

  ### Client-side

  To protect your pages on the client-side, you can use Clerk's [prebuilt control components](/reference/components/overview#control-components) that control the visibility of content based on the user's authentication state.

  The following example uses the following components:

  - [``](/reference/components/control/show): Children of this component can only be seen while **signed in**.
- [``](/reference/components/control/show): Children of this component can only be seen while **signed out**.
- [``](/reference/components/user/user-button): Shows the signed-in user's avatar. Selecting it opens a dropdown menu with account management options.
- [``](/reference/components/unstyled/sign-in-button): An unstyled component that links to the sign-in page. In this example, since no props or [environment variables](/guides/development/clerk-environment-variables) are set for the sign-in URL, this component links to the [Account Portal sign-in page](/guides/account-portal/overview#sign-in).
- [``](/reference/components/unstyled/sign-up-button): An unstyled component that links to the sign-up page. In this example, since no props or [environment variables](/guides/development/clerk-environment-variables) are set for the sign-up URL, this component links to the [Account Portal sign-up page](/guides/account-portal/overview#sign-up).


  ```tsx
// Filename: routes/_index.tsx

  import { Show, SignInButton, SignUpButton, UserButton } from '@clerk/remix'

  export default function Index() {
    return (
      <div>
        <h1>Index Route</h1>
        
          </div>
    )
  }
  ```

  ### Server-side

  To protect your routes, use the [`getAuth()`](/reference/nextjs/pages-router/get-auth) function in your loader. This function retrieves the authentication state from the request object, returning an [`Auth`](/reference/backend/types/auth-object) object that includes the `isAuthenticated`, allowing you to determine if the user is authenticated.

  ```tsx
// Filename: routes/_index.tsx

  import { UserButton } from '@clerk/remix'
  import { getAuth } from '@clerk/remix/ssr.server'
  import { LoaderFunction, redirect } from '@remix-run/node'

  export const loader: LoaderFunction = async (args) => {
    const { isAuthenticated } = await getAuth(args)
    if (!isAuthenticated) {
      return redirect('/sign-in')
    }
    return {}
  }

  export default function Index() {
    return (
      <div>
        <h1>Index route</h1>
        <p>You are signed in!</p>
        </div>
    )
  }
  ```

  ## Run your project

Run your project with the following command:

```npm
npm run dev
```


  ## Create your first user

1. Visit your app's homepage at [http://localhost:5173](http://localhost:5173).
1. Select "Sign up" on the page and authenticate to create your first user.


## Next steps

Learn more about Clerk components, how to customize them, and how to use Clerk's client-side helpers using the following guides.


  - [Prebuilt components](/reference/components/overview)
  - Learn how to quickly add authentication to your app using Clerk's suite of components.

  ---

  - [Customization & localization](/guides/customizing-clerk/appearance-prop/overview)
  - Learn how to customize and localize Clerk components.

  ---

  - [Create a custom sign-in-or-up page](/remix/guides/development/custom-sign-in-or-up-page)
  - Learn how to create a custom sign-in-or-up page with Clerk components.

  ---

  - [Protect content and read user data](/remix/guides/users/reading)
  - Learn how to use Clerk's hooks and helpers to protect content and read user data in your Remix app.

  ---

  - [Remix SPA Mode](/guides/development/spa-mode)
  - Learn how to use Clerk with Remix in SPA mode.

  ---

  - [Clerk Remix SDK Reference](/reference/remix/overview)
  - Learn about the Clerk Remix SDK and how to integrate it into your app.
