# <UserButton />` component


> Clerk's <UserButton /> component is used to render the familiar user button UI popularized by Google.

The `` component renders the familiar user button UI popularized by Google. When selected, it opens a dropdown menu with options to manage account settings and sign out. The "Manage account" option launches the [``](/reference/components/user/user-profile) component, providing access to profile and security settings.

For users that have [multi-session](/guides/secure/session-options#multi-session-applications) enabled, the `` also allows users to sign into multiple accounts at once and instantly switch between them without the need for a full page reload. Learn more [here](/guides/secure/session-options#multi-session-applications).


  ## Example

  The following example includes a basic implementation of the `` component mounted in a header. When the user is signed in, they will see their avatar and be able to open the popup menu. You can use this as a starting point for your own implementation.

  
    
**App Router:**

```tsx
// Filename: layout.tsx

      import { ClerkProvider, Show, SignInButton, UserButton } from '@clerk/nextjs'

      function Header() {
        return (
          <header style={{ display: 'flex', justifyContent: 'space-between', padding: 20 }}>
            <h1>My App</h1>
            
              </header>
        )
      }

      export default function RootLayout({ children }: { children: React.ReactNode }) {
        return (
          <html lang="en">
            
              {children}
            
          </html>
        )
      }
      ```


**Pages Router:**

```tsx
// Filename: pages/_app.tsx

      import { ClerkProvider, Show, SignInButton, UserButton } from '@clerk/nextjs'
      import type { AppProps } from 'next/app'

      function Header() {
        return (
          <header style={{ display: 'flex', justifyContent: 'space-between', padding: 20 }}>
            <h1>My App</h1>
            
              </header>
        )
      }

      function MyApp({ pageProps, Component }: AppProps) {
        return (
          
            
        )
      }

      export default MyApp
      ```

  

  
    ```tsx
// Filename: src/App.tsx

    import { Show, UserButton, SignInButton } from '@clerk/react'

    function App() {
      return (
        <header>
          
            </header>
      )
    }

    export default App
    ```
  

  
    ```astro
// Filename: pages/index.astro

    ---
    import { Show, UserButton, SignInButton } from '@clerk/astro/components'
    ---

    
      ```
  

  
    > [!NOTE]
> This component is for Expo web projects. For native iOS and Android apps, use the [native components](/reference/expo/native-components/overview) from `@clerk/expo/native` instead.


    ```jsx
// Filename: /app/user-button.web.tsx

    import { Show, UserButton, SignInButton } from '@clerk/expo/web'

    export default function Header() {
      return (
        <header>
          
            </header>
      )
    }
    ```
  

  
    ```jsx
// Filename: src/layouts/root-layout.tsx

    import { Show, UserButton, SignInButton } from '@clerk/chrome-extension'

    export default function Header() {
      return (
        <header>
          
            </header>
      )
    }
    ```
  

  
    ```tsx
// Filename: app/routes/_index.tsx

    import { Show, UserButton, SignInButton } from '@clerk/remix'

    export default function Index() {
      return (
        <header>
          
            </header>
      )
    }
    ```
  

  
    ```tsx
// Filename: app/routes/home.tsx

    import { Show, UserButton, SignInButton } from '@clerk/react-router'

    export default function Home() {
      return (
        <header>
          
            </header>
      )
    }
    ```
  

  
    ```tsx
// Filename: app/routes/index.tsx

    import { Show, UserButton, SignInButton } from '@clerk/tanstack-react-start'
    import { createFileRoute } from '@tanstack/react-router'

    export const Route = createFileRoute('/')({
      component: Home,
    })

    function Home() {
      return (
        <header>
          
            </header>
      )
    }
    ```
  

  
    ```vue
// Filename: components/AppHeader.vue

    <script setup>
    // Components are automatically imported
    </script>

    <template>
      <header style="display: flex; justify-content: space-between; padding: 20px">
        <h1>My App</h1>
        
          </header>
    </template>
    ```
  

  
    ```vue
// Filename: header.vue

    <script setup>
    import { Show, UserButton, SignInButton } from '@clerk/vue'
    </script>

    <template>
      <header>
        
          </header>
    </template>
    ```
  


  ## Usage with JavaScript

  The following methods available on an instance of the [`Clerk`](/reference/javascript/clerk) class are used to render and control the `` component:

  - [`mountUserButton()`](#mount-user-button)
  - [`unmountUserButton()`](#unmount-user-button)

  The following examples assume that you have followed the [quickstart](/js-frontend/getting-started/quickstart) in order to add Clerk to your JavaScript application.

  ### `mountUserButton()`

  Render the `` component to an HTML `<div>` element.

  ```typescript
  function mountUserButton(node: HTMLDivElement, props?: UserButtonProps): void
  ```

  #### `mountUserButton()` params

  - **`node`** [`HTMLDivElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLDivElement)

  The `<div>` element used to render in the `` component

      ---

- **`props?`** [`UserButtonProps`](#properties)

  The properties to pass to the `` component


  #### `mountUserButton()` usage

  ```js
// Filename: main.js

  import { Clerk } from '@clerk/clerk-js'

  // Initialize Clerk with your Clerk Publishable Key
  const clerkPubKey = import.meta.env.VITE_CLERK_PUBLISHABLE_KEY

  const clerk = new Clerk(clerkPubKey)
  await clerk.load()

  document.getElementById('app').innerHTML = `
    <div id="user-button"></div>
  `

  const userbuttonDiv = document.getElementById('user-button')

  clerk.mountUserButton(userbuttonDiv)
  ```

  ### `unmountUserButton()`

  Unmount and run cleanup on an existing `` component instance.

  ```typescript
  function unmountUserButton(node: HTMLDivElement): void
  ```

  #### `unmountUserButton()` params

  - **`node`** [`HTMLDivElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLDivElement)

  The container `<div>` element with a rendered `` component instance.


  #### `unmountUserButton()` usage

  ```js
// Filename: main.js

  import { Clerk } from '@clerk/clerk-js'

  // Initialize Clerk with your Clerk Publishable Key
  const clerkPubKey = import.meta.env.VITE_CLERK_PUBLISHABLE_KEY

  const clerk = new Clerk(clerkPubKey)
  await clerk.load()

  document.getElementById('app').innerHTML = `
    <div id="user-button"></div>
  `

  const userButtonDiv = document.getElementById('user-button')

  clerk.mountUserButton(userButtonDiv)

  // ...

  clerk.unmountUserButton(userButtonDiv)
  ```


## Properties

The `` component accepts the following properties, all of which are **optional**:

- **`afterMultiSessionSingleSignOutUrl` (deprecated)** `string`

  **Deprecated. Move `afterMultiSessionSingleSignOutUrl` to [``](/reference/components/clerk-provider).** The full URL or path to navigate to after signing out from a currently active account in a multi-session app.

    ---

- **`afterSignOutUrl` (deprecated)** `string`

  **Deprecated. Move `afterSignOutUrl` to [``](/reference/components/clerk-provider).** The full URL or path to navigate to after a successful sign-out.

    ---

- **`afterSwitchSessionUrl`** `string`

  The full URL or path to navigate to after a successful account change in a multi-session app.

    ---

- **`appearance`** <code>[Appearance](/guides/customizing-clerk/appearance-prop/overview) | undefined</code>

  Optional object to style your components. Will only affect [Clerk components](/reference/components/overview) and not [Account Portal](/guides/account-portal/overview) pages.

    ---

- **`defaultOpen`** `boolean`

  Controls whether the `` should open by default during the first render.

    ---

- **`showName`** `boolean`

  Controls if the user name is displayed next to the user image button.

    ---

- **`signInUrl`** `string`

  The full URL or path to navigate to when the **Add another account** button is clicked. It's recommended to use [the environment variable](/guides/development/clerk-environment-variables#sign-in-and-sign-up-redirects) instead.

    ---

- **`userProfileMode`** `'modal' | 'navigation'`

  Controls whether selecting the **Manage your account** button will cause the [``](/reference/components/user/user-profile) component to open as a modal, or if the browser will navigate to the `userProfileUrl` where `` is mounted as a page. Defaults to: `'modal'`.

    ---

- **`userProfileProps`** `object`

  Specify options for the underlying [``](/reference/components/user/user-profile) component. For example: `{additionalOAuthScopes: {google: ['foo', 'bar'], github: ['qux']}}`.

    ---

- **`userProfileUrl`** `string`

  The full URL or path leading to the user management interface.

    ---

- **`fallback?`** `ReactNode`

  An optional element to be rendered while the component is mounting.


## Customization

To learn about how to customize Clerk components, see the [customization documentation](/guides/customizing-clerk/appearance-prop/overview).

You can also [add custom actions and links to the `` menu](/guides/customizing-clerk/adding-items/user-button).
