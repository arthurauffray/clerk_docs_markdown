# Set up a waitlist in your app


> Learn how to add a waitlist to your application.

In [**Waitlist** mode](/guides/secure/restricting-access#waitlist), users can register their interest in your app by joining a waitlist. This mode is ideal for apps in early development stages or those wanting to generate interest before launch. This guide shows you how to add a waitlist to your application.


  ## Enable Waitlist mode

  To enable **Waitlist** mode, follow these steps:

  1. In the Clerk Dashboard, navigate to the [**Waitlist**](https://dashboard.clerk.com/~/user-authentication/waitlist) page.
1. Toggle on **Enable waitlist** and select **Save**.


  ## Add the `` component to your app

  The [``](/reference/components/authentication/waitlist) component provides a form where users can submit their details to join the waitlist and express their interest in your app. Once approved by admins, users will receive an email with access instructions.

  
    > [!NOTE]
    > If you're using Next.js, the `` component is available in `@clerk/nextjs@6.2.0` and above.
  

  The following example includes a basic implementation of the `` component hosted under the `/waitlist` route. You can use this as a starting point for your own implementation.

  
  ```tsx
// Filename: app/waitlist/[[...waitlist]]/page.tsx

  import { Waitlist } from '@clerk/nextjs'

  export default function WaitlistPage() {
    return }
  ```


  ```tsx
// Filename: src/pages/waitlist.tsx

  import { Waitlist } from '@clerk/react'

  export default function WaitlistPage() {
    return }
  ```


  ```astro
// Filename: pages/waitlist.astro

  ---
  import { Waitlist as WaitlistAstro } from '@clerk/astro/components'
  ---

  ```


  > [!NOTE]
> This component is for Expo web projects. For native iOS and Android apps, use the [native components](/reference/expo/native-components/overview) from `@clerk/expo/native` instead.


  ```jsx
// Filename: /app/waitlist.web.tsx

  import { Waitlist } from '@clerk/expo/web'

  export default function WaitlistPage() {
    return }
  ```


  ```jsx
// Filename: src/routes/waitlist.tsx

  import { Waitlist } from '@clerk/chrome-extension'

  export default function WaitlistPage() {
    return }
  ```


  ```tsx
// Filename: app/routes/waitlist.tsx

  import { Waitlist } from '@clerk/react-router'

  export default function WaitlistPage() {
    return }
  ```


  ```tsx
// Filename: app/routes/waitlist.tsx

  import { Waitlist } from '@clerk/remix'

  export default function WaitlistPage() {
    return }
  ```


  ```tsx
// Filename: app/routes/waitlist.tsx

  import { Waitlist } from '@clerk/tanstack-react-start'
  import { createFileRoute } from '@tanstack/react-router'

  export const Route = createFileRoute('/waitlist')({
    component: WaitlistPage,
  })

  function WaitlistPage() {
    return }
  ```


  ```vue
// Filename: waitlist.vue

  <script setup>
  // Components are automatically imported
  </script>

  <template>
    </template>
  ```


  ```vue
// Filename: waitlist.vue

  <script setup lang="ts">
  import { Waitlist } from '@clerk/vue'
  </script>

  <template>
    </template>
  ```


  ## Provide the `waitlistUrl` prop

  The `waitlistUrl` prop is used to specify the URL of your waitlist page. It should point to the route where your `` component is mounted. If `undefined`, the user will be redirected to the [Account Portal waitlist page](/guides/account-portal/overview#waitlist). You'll need to set `waitlistUrl` where you initialize Clerk.

  
    Pass the `waitlistUrl` prop to the [``](/reference/components/clerk-provider) component, ensuring it matches your waitlist route.

    ```tsx

    
      
    
    ```
  

  
    Pass the `waitlistUrl` prop to the [`clerk()`](/reference/astro/overview) integration, ensuring it matches your waitlist route.

    ```js
// Filename: astro.config.mjs

    import clerk from '@clerk/astro'

    export default defineConfig({
      integrations: [
        clerk({
          waitlistUrl: '/waitlist',
        }),
      ],
    })
    ```
  

  
    Pass the `waitlistUrl` prop to the [`clerkPlugin()`](/reference/vue/overview) integration, ensuring it matches your waitlist route.

    ```ts
// Filename: src/main.ts

    import { createApp } from 'vue'
    import App from './App.vue'
    import { clerkPlugin } from '@clerk/vue'

    const app = createApp(App)

    app.use(clerkPlugin, {
      waitlistUrl: '/waitlist',
    })

    app.mount('#app')
    ```
  

  
    Pass the `waitlistUrl` prop to the [`defineNuxtConfig()`](/reference/nuxt/clerk-middleware) integration, ensuring it matches your waitlist route.

    ```ts
// Filename: nuxt.config.ts

    export default defineNuxtConfig({
      modules: ['@clerk/nuxt'],
      clerk: {
        waitlistUrl: '/waitlist',
      },
    })
    ```
  

  ## Add a sign-in page

  To allow users to sign in once they've been approved from the waitlist, you need to set up a custom sign-in page.

  The following example demonstrates how to render the [``](/reference/components/authentication/sign-in) component, which will only be accessible to users who have been approved from the waitlist.

  
  If you would like to create a dedicated `/sign-in` page in your Next.js application, see the [dedicated guide](/nextjs/guides/development/custom-sign-in-or-up-page) for more information.

  ```tsx
// Filename: app/sign-in/[[...sign-in]]/page.tsx

  import { SignIn } from '@clerk/nextjs'

  export default function SignInPage() {
    return }
  ```


  ```astro
// Filename: pages/signin.astro

  ---
  import { SignIn } from '@clerk/astro/components'
  ---

  ```


  > [!NOTE]
> This component is for Expo web projects. For native iOS and Android apps, use the [native components](/reference/expo/native-components/overview) from `@clerk/expo/native` instead.


  If you would like to create a dedicated `/sign-in` page in your Expo application, see the [dedicated guide](/guides/development/web-support/custom-sign-in-or-up-page) for more information.

  ```tsx
// Filename: /app/sign-in.web.tsx

  import { SignIn } from '@clerk/expo/web'

  export default function SignInPage() {
    return }
  ```


  ```jsx
// Filename: src/pages/sign-in.tsx

  import { SignIn } from '@clerk/react'

  export default function SignInPage() {
    return }
  ```


  If you would like to create a dedicated `/sign-in` page in your React Router application, see the [dedicated guide](/react-router/guides/development/custom-sign-in-or-up-page) for more information.

  ```tsx
// Filename: app/routes/sign-in.tsx

  import { SignIn } from '@clerk/react-router'

  export default function SignInPage() {
    return }
  ```


  ```jsx
// Filename: src/routes/sign-in.tsx

  import { SignIn } from '@clerk/chrome-extension'

  export default function SignInPage() {
    return }
  ```


  If you would like to create a dedicated `/sign-in` page in your TanStack React Start application, see the [dedicated guide](/tanstack-react-start/guides/development/custom-sign-in-or-up-page) for more information.

  ```tsx
// Filename: app/routes/sign-in.$.tsx

  import { SignIn } from '@clerk/tanstack-react-start'
  import { createFileRoute } from '@tanstack/react-router'

  export const Route = createFileRoute('/sign-in')({
    component: SignInPage,
  })

  function SignInPage() {
    return }
  ```


  ```vue
// Filename: sign-in.vue

  <script setup lang="ts">
  import { SignIn } from '@clerk/vue'
  </script>

  <template>
    </template>
  ```


  ```vue
// Filename: sign-in.vue

  <script setup lang="ts">
  // Components are automatically imported
  </script>

  <template>
    </template>
  ```


  > [!NOTE]
  > Alternatively, you can add the `waitlistUrl` prop to the `` component instead of `` if needed.

  ## Manage users on your waitlist

  Once users join your waitlist, you can manage their access from the Clerk Dashboard. You can approve or deny users, which will trigger an email notification to them with instructions on how to access your app if approved.

  1. In the Clerk Dashboard, navigate to the [**Waitlist**](https://dashboard.clerk.com/~/waitlist) page.
  1. On the right-side of a user's row, select the menu icon (...).
  1. Select **Invite** to invite the user to your application. Select **Deny** to deny the user access to your application.
