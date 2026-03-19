# <RedirectToTasks />


> The <RedirectToTasks /> component will navigate to the tasks flow which has been configured in your application instance when users have pending session tasks. The behavior will be just like a server-side (3xx) redirect, and will override the current location in the history stack.

The `` component will navigate to the tasks flow which has been configured in your application instance when users have pending session tasks. The behavior will be just like a server-side (3xx) redirect, and will override the current location in the history stack.

The prebuilt session task flow is hosted through Clerk's [Account Portal](/guides/account-portal/overview#sign-in). For example, if the user has a pending `choose-organization` task, they will be redirected to the `/tasks/choose-organization` Account Portal page. If you don't want to use the prebuilt components or Account Portal, you can build a [custom flow](/guides/development/custom-flows/authentication/session-tasks).

## Example

Your sign-up/sign-in flow should handle session tasks, but if a user's authentication flow is interrupted and they aren't able to complete the tasks, you can use the `` component to redirect them to the appropriate task page.

By default, the `` component will redirect to the `/sign-in/tasks/<task-key>` URL path, expecting [the `` component to be hosted on the `/sign-in` route](/guides/development/custom-sign-in-or-up-page). If it is, then the `` component will handle the session task flows. However, if you want to customize the paths where specific tasks are redirected, you can use the [`taskUrls` option on your Clerk integration](/guides/configure/session-tasks#using-the-task-urls-option).


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
