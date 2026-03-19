# Nuxt Quickstart


> Add authentication and user management to your Nuxt app with Clerk.

## Create a new Nuxt app

  If you don't already have a Nuxt app, run the following commands to [create a new one](https://nuxt.com/docs/4.x/getting-started/installation).

  ```npm
  npm create nuxt@latest clerk-nuxt
  cd clerk-nuxt
  npm install
  ```

  ## Install `@clerk/nuxt`

  The [Clerk Nuxt SDK](/reference/nuxt/overview) gives you access to prebuilt components, Vue composables, and helpers to make user authentication easier.

  Run the following command to install the SDK:

  ```npm
  npm install @clerk/nuxt
  ```

  ## Set your Clerk API keys

  
  Add the following keys to your `.env` file. These keys can always be retrieved from the [**API keys**](https://dashboard.clerk.com/~/api-keys) page in the Clerk Dashboard.


  1. In the Clerk Dashboard, navigate to the [**API keys**](https://dashboard.clerk.com/~/api-keys) page.
  1. In the **Quick Copy** section, copy your Clerk Publishable Key and Secret Key.
  1. Paste your keys into your `.env` file.

  The final result should resemble the following:


  ```env
// Filename: .env

  NUXT_PUBLIC_CLERK_PUBLISHABLE_KEY={{pub_key}}
  NUXT_CLERK_SECRET_KEY={{secret}}
  ```

  ## Configure `nuxt.config.ts`

  To enable Clerk in your Nuxt app, add `@clerk/nuxt` to your modules array in `nuxt.config.ts`. This automatically configures Clerk's middleware and plugins and imports Clerk's components.

  ```ts
// Filename: nuxt.config.ts

  export default defineNuxtConfig({
    modules: ['@clerk/nuxt'],
  })
  ```

  ## Create a header with Clerk components

  Nuxt 3 automatically imports and makes all components in the `components/` directory globally available without requiring explicit imports. See the [Nuxt docs](https://nuxt.com/docs/guide/concepts/auto-imports) for details.

  You can control which content signed-in and signed-out users can see with Clerk's [prebuilt control components](/reference/components/overview#control-components).

  The following example creates a header using the following components:

  - [``](/reference/components/control/show): Children of this component can only be seen while **signed in**.
- [``](/reference/components/control/show): Children of this component can only be seen while **signed out**.
- [``](/reference/components/user/user-button): Shows the signed-in user's avatar. Selecting it opens a dropdown menu with account management options.
- [``](/reference/components/unstyled/sign-in-button): An unstyled component that links to the sign-in page. In this example, since no props or [environment variables](/guides/development/clerk-environment-variables) are set for the sign-in URL, this component links to the [Account Portal sign-in page](/guides/account-portal/overview#sign-in).
- [``](/reference/components/unstyled/sign-up-button): An unstyled component that links to the sign-up page. In this example, since no props or [environment variables](/guides/development/clerk-environment-variables) are set for the sign-up URL, this component links to the [Account Portal sign-up page](/guides/account-portal/overview#sign-up).


  ```vue
// Filename: app/app.vue

  <script setup lang="ts">
  // Components are automatically imported
  </script>

  <template>
    <header>
      
        </header>

    <main>
      </main>
  </template>
  ```

  ## Run your project

Run your project with the following command:

```npm
npm run dev
```


  ## Create your first user

1. Visit your app's homepage at [http://localhost:3000](http://localhost:3000).
1. Select "Sign up" on the page and authenticate to create your first user.


## Next steps

Learn more about Clerk components, how to customize them, and how to use Clerk's client-side helpers using the following guides.


  - [Prebuilt components](/reference/components/overview)
  - Learn how to quickly add authentication to your app using Clerk's suite of components.

  ---

  - [Customization & localization](/guides/customizing-clerk/appearance-prop/overview)
  - Learn how to customize and localize Clerk components.

  ---

  - [Protect routes using clerkMiddleware()](/reference/nuxt/clerk-middleware)
  - Learn how to protect specific routes from unauthenticated users.

  ---

  - [Protect content and read user data](/nuxt/guides/users/reading)
  - Learn how to use Clerk's composables and helpers to protect content and read user data in your Nuxt app.

  ---

  - [Client-side helpers (composables)](/reference/nuxt/overview#client-side-helpers)
  - Learn more about Clerk's client-side helpers and how to use them.

  ---

  - [Get started with Organizations](/nuxt/guides/organizations/getting-started)
  - Learn how to create and manage Organizations in your Nuxt app.

  ---

  - [Clerk Nuxt SDK Reference](/reference/nuxt/overview)
  - Learn about the Clerk Nuxt SDK and how to integrate it into your app.
