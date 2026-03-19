# Vue Quickstart


> Add authentication and user management to your Vue app with Clerk.

This tutorial assumes that you're using [Vue 3](https://vuejs.org/) with [TypeScript](https://www.typescriptlang.org/).


  ## Create a new Vue app

  If you don't already have a Vue app, run the following commands to [create a new one using Vite](https://vitejs.dev/guide/#scaffolding-your-first-vite-project):

  ```npm
  npm create vite@latest clerk-vue -- --template vue-ts
  cd clerk-vue
  npm install
  ```

  ## Install `@clerk/vue`

  The [Clerk Vue SDK](/reference/vue/overview) gives you access to prebuilt components, composables, and helpers to make user authentication easier.

  Run the following command to install the SDK:

  ```npm
  npm install @clerk/vue
  ```

  ## Set your Clerk API keys

  
  Add your Clerk Publishable Key to your `.env` file.


  1. In the Clerk Dashboard, navigate to the [**API keys**](https://dashboard.clerk.com/~/api-keys) page.
  1. In the **Quick Copy** section, copy your Clerk Publishable Key.
  1. Paste your key into your `.env` file.

  The final result should resemble the following:


  ```env
// Filename: .env

  VITE_CLERK_PUBLISHABLE_KEY={{pub_key}}
  ```

  ## Add `clerkPlugin` to your app

  [`clerkPlugin`](/reference/vue/clerk-plugin) provides session and user context to Clerk's components and composables. It's required to pass your Clerk Publishable Key as an option. You can add an `if` statement to check that the key is imported properly. This prevents the app from running without the Publishable Key and catches TypeScript errors.

  The `clerkPlugin` accepts optional options, such as `{ signInForceRedirectUrl: '/dashboard' }`.

  ```ts
// Filename: src/main.ts

  import { createApp } from 'vue'
  import './style.css'
  import App from './App.vue'
  import { clerkPlugin } from '@clerk/vue'

  const PUBLISHABLE_KEY = import.meta.env.VITE_CLERK_PUBLISHABLE_KEY

  if (!PUBLISHABLE_KEY) {
    throw new Error('Add your Clerk Publishable Key to the .env file')
  }

  const app = createApp(App)
  app.use(clerkPlugin, { publishableKey: PUBLISHABLE_KEY })
  app.mount('#app')
  ```

  ## Create a header with Clerk components

  You can control which content signed-in and signed-out users can see with Clerk's [prebuilt control components](/reference/components/overview#control-components). The following example creates a header using the following components:

  - [``](/reference/components/control/show): Children of this component can only be seen while **signed in**.
- [``](/reference/components/control/show): Children of this component can only be seen while **signed out**.
- [``](/reference/components/user/user-button): Shows the signed-in user's avatar. Selecting it opens a dropdown menu with account management options.
- [``](/reference/components/unstyled/sign-in-button): An unstyled component that links to the sign-in page. In this example, since no props or [environment variables](/guides/development/clerk-environment-variables) are set for the sign-in URL, this component links to the [Account Portal sign-in page](/guides/account-portal/overview#sign-in).
- [``](/reference/components/unstyled/sign-up-button): An unstyled component that links to the sign-up page. In this example, since no props or [environment variables](/guides/development/clerk-environment-variables) are set for the sign-up URL, this component links to the [Account Portal sign-up page](/guides/account-portal/overview#sign-up).


  ```vue
// Filename: src/App.vue

  <script setup lang="ts">
  import { Show, SignInButton, SignUpButton, UserButton } from '@clerk/vue'
  </script>

  <template>
    <header>
      
        </header>
  </template>
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

  - [Client-side helpers (composables)](/reference/vue/overview#custom-composables)
  - Learn more about Clerk's client-side helpers and how to use them.

  ---

  - [Update Clerk options at runtime](/reference/vue/update-clerk-options)
  - Learn how to update Clerk's options at runtime in your Vue app.

  ---

  - [Clerk Vue SDK Reference](/reference/vue/overview)
  - Learn about the Clerk Vue SDK and how to integrate it into your app.
