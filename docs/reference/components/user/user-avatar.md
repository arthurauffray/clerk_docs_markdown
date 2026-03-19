# <UserAvatar />` component


> Clerk's <UserAvatar /> component is used to render the familiar user avatar on its own.

The `` component renders the authenticated user's avatar on its own, a common UI element found across many websites and applications.


  ## Example

  The following example includes a basic implementation of the `` component mounted in a header. When the user is signed in, they will see their avatar. You can use this as a starting point for your own implementation.

  
    
**App Router:**

```tsx
// Filename: layout.tsx

      import { ClerkProvider, Show, SignInButton, UserAvatar } from '@clerk/nextjs'

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

      import { ClerkProvider, Show, SignInButton, UserAvatar } from '@clerk/nextjs'
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

    import { Show, UserAvatar, SignInButton } from '@clerk/react'

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
    import { Show, UserAvatar, SignInButton } from '@clerk/astro/components'
    ---

    
      ```
  

  
    > [!NOTE]
> This component is for Expo web projects. For native iOS and Android apps, use the [native components](/reference/expo/native-components/overview) from `@clerk/expo/native` instead.


    ```jsx
// Filename: /app/user-avatar.web.tsx

    import { Show, UserAvatar, SignInButton } from '@clerk/expo/web'

    export default function Header() {
      return (
        <header>
          
            </header>
      )
    }
    ```
  

  
    ```jsx
// Filename: src/layouts/root-layout.tsx

    import { Show, UserAvatar, SignInButton } from '@clerk/chrome-extension'

    export default function Header() {
      return (
        <header>
          
            </header>
      )
    }
    ```
  

  
    ```tsx
// Filename: app/routes/_index.tsx

    import { Show, UserAvatar, SignInButton } from '@clerk/remix'

    export default function Index() {
      return (
        <header>
          
            </header>
      )
    }
    ```
  

  
    ```tsx
// Filename: app/routes/home.tsx

    import { Show, UserAvatar, SignInButton } from '@clerk/react-router'

    export default function Home() {
      return (
        <header>
          
            </header>
      )
    }
    ```
  

  
    ```tsx
// Filename: app/routes/index.tsx

    import { Show, UserAvatar, SignInButton } from '@clerk/tanstack-react-start'
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
    import { Show, UserAvatar, SignInButton } from '@clerk/vue'
    </script>

    <template>
      <header>
        
          </header>
    </template>
    ```
  


  ## Usage with JavaScript

  The following methods available on an instance of the [`Clerk`](/reference/javascript/clerk) class are used to render and control the `` component:

  - [`mountUserAvatar()`](#mount-user-avatar)
  - [`unmountUserAvatar()`](#unmount-user-avatar)

  The following examples assume that you have followed the [quickstart](/js-frontend/getting-started/quickstart) in order to add Clerk to your JavaScript application.

  ### `mountUserAvatar()`

  Render the `` component to an HTML `<div>` element.

  ```typescript
  function mountUserAvatar(node: HTMLDivElement, props?: UserAvatarProps): void
  ```

  #### `mountUserAvatar()` params

  - **`node`** [`HTMLDivElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLDivElement)

  The `<div>` element used to render in the `` component

      ---

- **`props?`** [`UserAvatarProps`](#properties)

  The properties to pass to the `` component


  #### `mountUserAvatar()` usage

  ```js
// Filename: main.js

  import { Clerk } from '@clerk/clerk-js'

  // Initialize Clerk with your Clerk Publishable Key
  const clerkPubKey = import.meta.env.VITE_CLERK_PUBLISHABLE_KEY

  const clerk = new Clerk(clerkPubKey)
  await clerk.load()

  document.getElementById('app').innerHTML = `
    <div id="user-avatar"></div>
  `

  const userAvatarDiv = document.getElementById('user-avatar')

  clerk.mountUserAvatar(userAvatarDiv)
  ```

  ### `unmountUserAvatar()`

  Unmount and run cleanup on an existing `` component instance.

  ```typescript
  function unmountUserAvatar(node: HTMLDivElement): void
  ```

  #### `unmountUserAvatar()` params

  - **`node`** [`HTMLDivElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLDivElement)

  The container `<div>` element with a rendered `` component instance.


  #### `unmountUserAvatar()` usage

  ```js
// Filename: main.js

  import { Clerk } from '@clerk/clerk-js'

  // Initialize Clerk with your Clerk Publishable Key
  const clerkPubKey = import.meta.env.VITE_CLERK_PUBLISHABLE_KEY

  const clerk = new Clerk(clerkPubKey)
  await clerk.load()

  document.getElementById('app').innerHTML = `
    <div id="user-avatar"></div>
  `

  const userAvatarDiv = document.getElementById('user-avatar')

  clerk.mountUserAvatar(userAvatarDiv)

  // ...

  clerk.unmountUserAvatar(userAvatarDiv)
  ```


## Properties

The `` component accepts the following properties, all of which are **optional**:

- **`rounded?`** `boolean`

  Determines whether the user avatar is displayed with rounded corners.

    ---

- **`appearance?`** <code>[Appearance](/guides/customizing-clerk/appearance-prop/overview) | undefined</code>

  Optional object to style your components. Will only affect [Clerk components](/reference/components/overview) and not [Account Portal](/guides/account-portal/overview) pages.

    ---

- **`fallback?`** `ReactNode`

  Optional element to be rendered while the component is mounting.


## Customization

To learn about how to customize Clerk components, see the [customization documentation](/guides/customizing-clerk/appearance-prop/overview).
