# Astro Quickstart


> Add authentication and user management to your Astro app with Clerk.

## Create a new Astro app

  If you don't already have an Astro app, run the following commands to [create a new one](https://docs.astro.build/en/install-and-setup/).

  ```npm
  npm create astro@latest clerk-astro
  cd clerk-astro
  npm install
  ```

  ## Install `@clerk/astro`

  The [Clerk Astro SDK](/reference/astro/overview) gives you access to a set of components, hooks, and stores to make user authentication easier.

  Run the following command to install the SDK:

  ```npm
  npm install @clerk/astro
  ```

  ## Set your Clerk API keys

  
  Add the following keys to your `.env` file. These keys can always be retrieved from the [**API keys**](https://dashboard.clerk.com/~/api-keys) page in the Clerk Dashboard.


  1. In the Clerk Dashboard, navigate to the [**API keys**](https://dashboard.clerk.com/~/api-keys) page.
  1. In the **Quick Copy** section, copy your Clerk Publishable Key and Secret Key.
  1. Paste your keys into your `.env` file.

  The final result should resemble the following:


  ```env
// Filename: .env

  PUBLIC_CLERK_PUBLISHABLE_KEY={{pub_key}}
  CLERK_SECRET_KEY={{secret}}
  ```

  ## Update `astro.config.mjs`

  To configure Clerk in your Astro app, you will need to update your `astro.config.mjs`.

  - Add the `clerk()` integration to the `integrations` list. For a list of available options, see the [integration reference](/reference/astro/integration).
  - Install an [SSR adapter](https://docs.astro.build/en/guides/server-side-rendering/#official-adapters). This quickstart uses the [`@astrojs/node`](https://docs.astro.build/en/guides/integrations-guide/node/) adapter.
  - Set `output` to `server`. This is required when deploying to a host supporting SSR.

  ```ts
// Filename: astro.config.mjs

  import { defineConfig } from 'astro/config'
  import node from '@astrojs/node'
  import clerk from '@clerk/astro'

  export default defineConfig({
    integrations: [clerk()],
    adapter: node({ mode: 'standalone' }),
    output: 'server',
  })
  ```

  ## Add `clerkMiddleware()` to your app

  [`clerkMiddleware()`](/reference/astro/clerk-middleware) grants you access to user authentication state throughout your app. It also allows you to protect specific routes from unauthenticated users. To add `clerkMiddleware()` to your app, follow these steps:

  1. Create a `middleware.ts` file.
     - If you're using the `/src` directory, create `middleware.ts` in the `/src` directory.
     - If you're not using the `/src` directory, create `middleware.ts` in the root directory alongside `.env`.
  1. In your `middleware.ts` file, export an `onRequest` constant and assign the result of the `clerkMiddleware()` function to it.
     ```tsx
// Filename: src/middleware.ts

     import { clerkMiddleware } from '@clerk/astro/server'

     export const onRequest = clerkMiddleware()
     ```
  1. By default, `clerkMiddleware()` will not protect any routes. All routes are public and you must opt-in to protection for routes. See the [`clerkMiddleware()` reference](/reference/astro/clerk-middleware) to learn how to require authentication for specific routes.

  ## Create a header with Clerk components

  You can control which content signed-in and signed-out users can see with Clerk's [prebuilt control components](/reference/components/overview#control-components). The following example creates a header using the following components:

  - [``](/reference/components/control/show): Children of this component can only be seen while **signed in**.
- [``](/reference/components/control/show): Children of this component can only be seen while **signed out**.
- [``](/reference/components/user/user-button): Shows the signed-in user's avatar. Selecting it opens a dropdown menu with account management options.
- [``](/reference/components/unstyled/sign-in-button): An unstyled component that links to the sign-in page. In this example, since no props or [environment variables](/guides/development/clerk-environment-variables) are set for the sign-in URL, this component links to the [Account Portal sign-in page](/guides/account-portal/overview#sign-in).
- [``](/reference/components/unstyled/sign-up-button): An unstyled component that links to the sign-up page. In this example, since no props or [environment variables](/guides/development/clerk-environment-variables) are set for the sign-up URL, this component links to the [Account Portal sign-up page](/guides/account-portal/overview#sign-up).


  ```astro
// Filename: src/layouts/Layout.astro

  ---
  import { Show, UserButton, SignInButton, SignUpButton } from '@clerk/astro/components'
  ---

  <!doctype html>
  <html lang="en">
    <head>
      <meta charset="UTF-8" />
      <meta name="viewport" content="width=device-width" />
      <link rel="icon" type="image/svg+xml" href="/favicon.svg" />
      <meta name="generator" content={Astro.generator} />
      <title>Astro Basics</title>
    </head>
    <body>
      <header>
        
          </header>
      <slot />
    </body>
  </html>

  <style>
    html,
    body {
      margin: 0;
      width: 100%;
      height: 100%;
    }
  </style>
  ```

  Then, use the layout on your homepage:

  ```astro
// Filename: src/pages/index.astro

  ---
  import Layout from '../layouts/Layout.astro'
  import { Show } from '@clerk/astro/components'
  ---

  
    
      <p>Sign in to try Clerk out!</p>
    
    
      <p>You are signed in!</p>
    
  
  ```

  ## Run your project

Run your project with the following command:

```npm
npm run dev
```


  ## Create your first user

  1. Visit your app's homepage at [http://localhost:4321](http://localhost:4321).
  1. Select "Sign up" on the page and authenticate to create your first user.


## Next steps

Learn more about Clerk components, how to customize them, and how to use Clerk's stores to access user data using the following guides.


  - [Prebuilt components](/reference/components/overview)
  - Learn how to quickly add authentication to your app using Clerk's suite of components.

  ---

  - [Customization & localization](/guides/customizing-clerk/appearance-prop/overview)
  - Learn how to customize and localize Clerk components.

  ---

  - [Protect routes using clerkMiddleware()](/reference/astro/clerk-middleware)
  - Learn how to protect specific routes from unauthenticated users.

  ---

  - [Protect content and read user data](/astro/guides/users/reading)
  - Learn how to use Clerk's stores and helpers to protect content and read user data in your Astro app.

  ---

  - [Use Clerk with Astro and React](/reference/astro/react)
  - Learn how to set up your Astro app to be integrated with React.

  ---

  - [Get started with Organizations](/astro/guides/organizations/getting-started)
  - Learn how to create and manage Organizations in your Astro app.

  ---

  - [Clerk Astro SDK Reference](/reference/astro/overview)
  - Learn about the Clerk Astro SDK and how to integrate it into your app.
