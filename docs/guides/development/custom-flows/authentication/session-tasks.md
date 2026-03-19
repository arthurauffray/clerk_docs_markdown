# Session tasks


> Learn how to handle session tasks in your custom authentication flow.

> [!WARNING]
> This guide is for users who want to build a custom flow. To use a _prebuilt_ UI, use the [Account Portal pages](/guides/account-portal/overview) or [prebuilt components](/reference/components/overview).


[Session tasks](/guides/configure/session-tasks) are pending requirements that users must complete after authentication, such as choosing an Organization. These tasks ensure that users meet all requirements before gaining full access to your application.

When enabled in the Clerk Dashboard, these tasks are handled automatically within the `` and `` components. If the prebuilt components don't meet your specific needs or if you require more control over the logic, you can opt out of using the `` and `` components and create a custom flow to display tasks.

This guide demonstrates how to use the Clerk API to build a custom user interface for handling session tasks.

## Available tasks

Each task is identified by a unique [`SessionTask['key']`](/reference/javascript/types/session-task). You can use these task keys to conditionally handle different requirements in your application logic.

The following table lists the available tasks and their corresponding keys.

| Setting | Key | Description |
| - | - | - |
| [Allow Personal Accounts](/guides/organizations/configure#personal-accounts) | `choose-organization` | Disabled by default when enabling Organizations for instances created after August 22, 2025. When disabled, users are required to choose an Organization after authenticating. When enabled, users can choose a Personal Account instead of an Organization. |
| [Force password reset](/guides/secure/password-protection-and-rules#manually-set-a-password-as-compromised) | `reset-password` | Enabled by default for instances created after December 8, 2025. When enabled, the user is required to reset their password on their next sign-in if their password is marked as compromised. |
| [Require multi-factor authentication](/guides/configure/auth-strategies/sign-up-sign-in-options#multi-factor-authentication) | `setup-mfa` | When enabled, users are required to set up multi-factor authentication (MFA) after authenticating. Users can choose between authenticator app (TOTP), SMS verification, or backup codes depending on which methods are enabled in the instance settings. |


  ## Detect pending session tasks

  First, you need to tell your app where to redirect users when they have pending session tasks.

  The `taskUrls` option allows you to specify custom URL paths where users are redirected after sign-up or sign-in when specific session tasks need to be completed.


  Configure the `taskUrls` option on the [``](/reference/components/clerk-provider) component.

  ```tsx
  
    {children}
  
  ```


  Configure the `taskUrls` option on the [`clerk()`](/reference/astro/overview) integration.

  ```js
// Filename: astro.config.mjs

  import { defineConfig } from 'astro/config'
  import node from '@astrojs/node'
  import clerk from '@clerk/astro'

  export default defineConfig({
    integrations: [
      clerk({
        taskUrls: {
          'choose-organization': '/session-tasks/choose-organization',
          'reset-password': '/session-tasks/reset-password',
        },
      }),
    ],
    adapter: node({ mode: 'standalone' }),
    output: 'server',
  })
  ```


  Configure the `taskUrls` option on the [`clerk.load()`](/reference/javascript/clerk#load) method.

  ```js
// Filename: main.ts

  import { Clerk } from '@clerk/clerk-js'

  const clerkPubKey = import.meta.env.VITE_CLERK_PUBLISHABLE_KEY

  const clerk = new Clerk(clerkPubKey)
  await clerk.load({
    taskUrls: {
      'choose-organization': '/session-tasks/choose-organization',
      'reset-password': '/session-tasks/reset-password',
    },
  })
  ```


  Configure the `taskUrls` option on the [`clerkPlugin()`](/reference/vue/overview) integration.

  ```ts
// Filename: src/main.ts

  import { createApp } from 'vue'
  import './styles.css'
  import App from './App.vue'
  import { clerkPlugin } from '@clerk/vue'

  const PUBLISHABLE_KEY = import.meta.env.VITE_CLERK_PUBLISHABLE_KEY

  if (!PUBLISHABLE_KEY) {
    throw new Error('Add your Clerk publishable key to the .env.local file')
  }

  const app = createApp(App)
  app.use(clerkPlugin, {
    publishableKey: PUBLISHABLE_KEY,
    taskUrls: {
      'choose-organization': '/session-tasks/choose-organization',
      'reset-password': '/session-tasks/reset-password',
    },
  })
  app.mount('#app')
  ```


  Configure the `taskUrls` option on the [`defineNuxtConfig()`](/reference/nuxt/clerk-middleware) integration.

  ```ts
// Filename: nuxt.config.ts

  export default defineNuxtConfig({
    compatibilityDate: '2025-07-15',
    devtools: { enabled: true },
    modules: ['@clerk/nuxt'],
    clerk: {
      taskUrls: {
        'choose-organization': '/session-tasks/choose-organization',
        'reset-password': '/session-tasks/reset-password',
      },
    },
  })
  ```


  Configure the `taskUrls` option on the [`clerkPlugin()`](/reference/fastify/clerk-plugin) integration.

  ```ts
// Filename: src/main.ts

  import Fastify from 'fastify'
  import { clerkPlugin } from '@clerk/fastify'

  const fastify = Fastify({ logger: true })

  fastify.register(clerkPlugin, {
    taskUrls: {
      'choose-organization': '/session-tasks/choose-organization',
      'reset-password': '/session-tasks/reset-password',
    },
  })
  ```


  ## Display tasks

  Now, the user will be redirected to the URL you've set with the `taskUrls` option. You need to display the appropriate task UI based on the task that the user needs to complete. If you were using the prebuilt components, you would simply [render the appropriate component based on the task](/guides/configure/session-tasks#displaying-tasks). However, since you're building a custom flow, you need to build the UI yourself. You can use the custom flow guide associated with the task to help get you started:

  | Session task | Custom flow guide |
  | - | - |
  | `choose-organization` | [Organization switcher guide](/guides/development/custom-flows/organizations/organization-switcher) |
  | `reset-password` | [Reset password guide](/guides/development/custom-flows/account-updates/forgot-password) |
  | `setup-mfa` | [Multi-factor authentication guide](/guides/development/custom-flows/account-updates/manage-mfa) |

  ## Protect routes

  What if your user exits the authentication or session task flow before completing their tasks and doesn't know how to get to the appropriate page to complete their session tasks? What if your user is navigating through your app as a `pending` user and can't figure out why they can't access certain content?

  If a user's authentication or session task flow is interrupted and they aren't able to complete the tasks, you can use the [``](/reference/components/control/redirect-to-tasks) component to redirect them to the appropriate task page so they can complete the tasks and move their session to an `active` (signed-in) state. This component will redirect users based on the URL's you've set with the `taskUrls` option.

  
  In the following example, the `` component is used to protect a page. Users can't access this page until they complete their pending session tasks. You can also wrap your entire application in the `` component, or place it in your application's layout file, so that users can't access **any** of your app until they complete their pending session tasks.


  In the following example, the `` component is used in the app's layout file so that users can't access **any** of the app until they complete their pending session tasks. However, you can also use the `` component to protect a single page or route group.

  ```tsx
// Filename: app/layout.tsx

  import { RedirectToTasks } from '@clerk/nextjs'

  export default function Layout({ children }: { children: React.ReactNode }) {
    return (
      <>
        {children}
      </>
    )
  }
  ```


  ```tsx
// Filename: pages/index.tsx

  import { RedirectToTasks } from '@clerk/react'

  export default function Page() {
    return }
  ```


  ```tsx
// Filename: app/routes/home.tsx

  import { RedirectToTasks } from '@clerk/react-router'

  export default function Home() {
    return }
  ```


  > [!NOTE]
  > This component relies on React Router for navigation. Ensure that you have integrated React Router into your Chrome Extension application before using it. [Learn how to add React Router to your Chrome Extension](/guides/development/add-react-router).

  ```jsx
// Filename: src/routes/home.tsx

  import { RedirectToTasks } from '@clerk/chrome-extension'

  export default function Home() {
    return }
  ```


  ```tsx
// Filename: app/routes/index.tsx

  import { RedirectToTasks } from '@clerk/tanstack-react-start'
  import { createFileRoute } from '@tanstack/react-router'

  export const Route = createFileRoute('/')({
    component: Home,
  })

  function Home() {
    return }
  ```


  ```vue
// Filename: App.vue

  <script setup lang="ts">
  import { RedirectToTasks } from '@clerk/vue'
  </script>

  <template>
    </template>
  ```


  ```vue
// Filename: App.vue

  <script setup lang="ts">
  // Components are automatically imported
  </script>

  <template>
    </template>
  ```


  This component is not available for your SDK. Please choose a different SDK.


## FAQ

### What is the `navigate` parameter in `finalize()` doing?

In the authentication custom flows, such as the [email/password custom flow](/guides/development/custom-flows/authentication/email-password), there's a step where you set the session to active using `finalize()`. If there are pending session tasks, the session won't actually be set as `active`. It will be in a `pending` state until all tasks are completed. By default, `pending` sessions are treated as signed-out across Clerk's authentication context, so the `pending` user won't be able to access protected content or routes. Therefore, this is the step where you should check for pending session tasks and redirect to the appropriate task page.

```tsx
await finalize({
  session: signIn.createdSessionId,
  navigate: async ({ session, decorateUrl }) => {
    // Handle session tasks
    // See https://clerk.com/docs/guides/development/custom-flows/authentication/session-tasks
    if (session?.currentTask) {
      console.log(session?.currentTask)
      return
    }

    const url = decorateUrl('/')
    if (url.startsWith('http')) {
      window.location.href = url
    } else {
      router.push(url)
    }
  },
})
```

However, if you've set the [`taskUrls` option on your Clerk integration](/guides/configure/session-tasks#using-the-task-urls-option), it will override the `navigate` behavior and will redirect the user to whatever URL path you've set for the task. It's recommended to rely on the `taskUrls` option so that you can maintain the task URLs in one place (your Clerk integration). However, the `navigate` parameter is still useful and can be used as a fallback.
