# <TaskResetPassword />` component


> Clerk's <TaskResetPassword /> component renders a UI for resolving the reset-password task.

The `` component renders a UI for resolving the `reset-password` session task. You can further customize your `` component by passing additional [properties](#properties) at the time of rendering.

> [!IMPORTANT]
> The `` component cannot render when a user doesn't have current session tasks.

## When to use ``

Clerk's sign-in flows, such as the [Sign-in Account Portal page](/guides/account-portal/overview#sign-in), [``](/reference/components/unstyled/sign-in-button), and [``](/reference/components/authentication/sign-in) component, automatically handle the `reset-password` session task flow for you, including rendering the `` component when needed.

If you want to customize the route where the `` component is rendered or customize its appearance, you can host it yourself within your application.


  ## Example

  The following example demonstrates how to host the `` component on a custom page. You first need to [set the `taskUrls` option on your Clerk integration](/guides/configure/session-tasks#using-the-task-urls-option) so that users are redirected to the page where you host the `` component when they have a pending `reset-password` session task.

  
    ```tsx
// Filename: app/layout.tsx

    import { ClerkProvider } from '@clerk/nextjs'

    export default function RootLayout({ children }: { children: React.ReactNode }) {
      return (
        <html lang="en">
          <body>
            
              {children}
            
          </body>
        </html>
      )
    }
    ```

    ```tsx
// Filename: app/session-tasks/reset-password/page.tsx

    import { TaskResetPassword } from '@clerk/nextjs'

    export default function Page() {
      return }
    ```
  

  
    ```tsx
// Filename: index.tsx

    import React from 'react'
    import ReactDOM from 'react-dom/client'
    import App from './App.tsx'
    import { ClerkProvider } from '@clerk/react'

    // Import your Publishable Key
    const PUBLISHABLE_KEY = import.meta.env.VITE_CLERK_PUBLISHABLE_KEY

    if (!PUBLISHABLE_KEY) {
      throw new Error('Add your Clerk Publishable Key to the .env file')
    }

    ReactDOM.createRoot(document.getElementById('root')!).render(
      
        
          
      </React.StrictMode>,
    )
    ```

    ```jsx
// Filename: src/session-tasks/reset-password.tsx

    import { TaskResetPassword } from '@clerk/react'

    const ResetPasswordPage = () => export default ResetPasswordPage
    ```
  

  
    > [!NOTE]
    > To see the full `root.tsx` setup you need for Clerk with React Router, see the [React Router quickstart](/react-router/getting-started/quickstart).

    ```tsx
// Filename: app/root.tsx

    import { ClerkProvider } from '@clerk/react-router'
    import { Outlet } from 'react-router'

    export default function App() {
      return (
        
          
      )
    }
    ```

    ```tsx
// Filename: app/routes/session-tasks/reset-password.tsx

    import { TaskResetPassword } from '@clerk/react-router'

    export default function ResetPasswordPage() {
      return }
    ```
  

  
    ```tsx
// Filename: app/root.tsx

    import type { MetaFunction, LoaderFunction } from '@remix-run/node'

    import { Links, Meta, Outlet, Scripts, ScrollRestoration } from '@remix-run/react'

    import { rootAuthLoader } from '@clerk/remix/ssr.server'
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

    export default ClerkApp(App, {
      taskUrls: { 'reset-password': '/session-tasks/reset-password' },
    })
    ```

    ```tsx
// Filename: app/routes/session-tasks.reset-password.tsx

    import { TaskResetPassword } from '@clerk/remix'

    export default function ResetPasswordPage() {
      return }
    ```
  

  
    > [!NOTE]
    > To see the full `__root.tsx` setup you need for Clerk with TanStack React Start, see the [TanStack React Start quickstart](/tanstack-react-start/getting-started/quickstart).

    ```tsx
// Filename: src/routes/__root.tsx

    import * as React from 'react'
    import { HeadContent, Scripts } from '@tanstack/react-router'
    import { ClerkProvider } from '@clerk/tanstack-react-start'

    function RootDocument({ children }: { children: React.ReactNode }) {
      return (
        <html>
          <head>
            </head>
          <body>
            
              {children}
            
            </body>
        </html>
      )
    }
    ```

    ```tsx
// Filename: src/routes/session-tasks/reset-password.tsx

    import { TaskResetPassword } from '@clerk/tanstack-react-start'
    import { createFileRoute } from '@tanstack/react-router'

    export const Route = createFileRoute('/session-tasks/reset-password')({
      component: ResetPasswordPage,
    })

    function ResetPasswordPage() {
      return }
    ```
  


  ## Usage with JavaScript

  You first need to set the `taskUrls` option on the [`clerk.load()`](/reference/javascript/clerk#load) method so that users are redirected to the page where you host the `` component when they have a pending `reset-password` session task.

  ```js
// Filename: main.ts

  import { Clerk } from '@clerk/clerk-js'

  const clerkPubKey = import.meta.env.VITE_CLERK_PUBLISHABLE_KEY

  const clerk = new Clerk(clerkPubKey)
  await clerk.load({
    taskUrls: {
      'reset-password': '/session-tasks/reset-password',
    },
  })
  ```

  The following methods available on an instance of the [`Clerk`](/reference/javascript/clerk) class are used to render and control the `` component:

  - [`mountTaskResetPassword()`](#mount-task-reset-password)
  - [`unmountTaskResetPassword()`](#unmount-task-reset-password)

  The following examples assume that you have followed the [quickstart](/js-frontend/getting-started/quickstart) in order to add Clerk to your JavaScript application.

  ### `mountTaskResetPassword()`

  Render the `` component to an HTML `<div>` element.

  ```typescript
  function mountTaskResetPassword(node: HTMLDivElement, props?: TaskResetPasswordProps): void
  ```

  #### `mountTaskResetPassword()` params

  - **`node `** [`HTMLDivElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLDivElement)

  The `<div>` element used to render in the `` component

      ---

- **`props?`** [`TaskResetPasswordProps`](#properties)

  The properties to pass to the `` component.


  #### `mountTaskResetPassword()` usage

  ```typescript
// Filename: main.ts

  import { Clerk } from '@clerk/clerk-js'

  const pubKey = import.meta.env.VITE_CLERK_PUBLISHABLE_KEY

  const clerk = new Clerk(pubKey)
  await clerk.load()

  if (clerk.isSignedIn) {
    // Mount user button component
    document.getElementById('signed-in').innerHTML = `
            <div id="user-button"></div>
          `

    const userbuttonDiv = document.getElementById('user-button')

    clerk.mountUserButton(userbuttonDiv)
  } else if (clerk.session?.currentTask) {
    switch (clerk.session.currentTask.key) {
      case 'reset-password': {
        document.getElementById('app').innerHTML = `
                <div id="task-reset-password"></div>
              `

        const taskResetPasswordDiv = document.getElementById('task-reset-password')

        clerk.mountTaskResetPassword(taskResetPasswordDiv)
      }
    }
  }
  ```

  ### `unmountTaskResetPassword()`

  Unmount and run cleanup on an existing `` component instance.

  ```typescript
  function unmountTaskResetPassword(node: HTMLDivElement): void
  ```

  #### `unmountTaskResetPassword()` params

  - **`node `** [`HTMLDivElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLDivElement)

  The container `<div>` element with a rendered `` component instance


  #### `unmountTaskResetPassword()` usage

  ```typescript
// Filename: main.ts

  import { Clerk } from '@clerk/clerk-js'

  const pubKey = import.meta.env.VITE_CLERK_PUBLISHABLE_KEY

  const clerk = new Clerk(pubKey)
  await clerk.load()

  if (clerk.isSignedIn) {
    // Mount user button component
    document.getElementById('signed-in').innerHTML = `
            <div id="user-button"></div>
          `

    const userbuttonDiv = document.getElementById('user-button')

    clerk.mountUserButton(userbuttonDiv)
  } else if (clerk.session?.currentTask) {
    switch (clerk.session.currentTask.key) {
      case 'reset-password': {
        document.getElementById('app').innerHTML = `
                <div id="task-reset-password"></div>
              `

        const taskResetPasswordDiv = document.getElementById('task-reset-password')

        clerk.mountTaskResetPassword(taskResetPasswordDiv)

        // ...

        clerk.unmountTaskResetPassword(taskResetPasswordDiv)
      }
    }
  }
  ```


## Properties

- **`redirectUrlComplete`** `string`

  The full URL or path to navigate to after successfully completing the task.

    ---

- **`appearance?`** <code>[Appearance](/guides/customizing-clerk/appearance-prop/overview) | undefined</code>

  Optional object to style your components. Will only affect [Clerk components](/reference/components/overview) and not [Account Portal](/guides/account-portal/overview) pages.


## Customization

To learn about how to customize Clerk components, see the [customization documentation](/guides/customizing-clerk/appearance-prop/overview).

If Clerk's prebuilt components don't meet your specific needs or if you require more control over the logic, you can rebuild the existing Clerk flows using the Clerk API. For more information, see the [custom flow guides](/guides/development/custom-flows/overview).
