# <SignInButton>


> The <SignInButton> component is a button that links to the sign-in page or displays the sign-in modal.

The `` component is a button that, by default, links to your app's sign-in page. Your sign-in page will be hosted by Clerk using the [Account Portal](/guides/account-portal/overview) unless you have set up a [dedicated sign-in page](/guides/development/custom-sign-in-or-up-page).

## Usage

### Basic usage


  ```jsx
// Filename: app/page.tsx

  import { SignInButton } from '@clerk/nextjs'

  export default function Home() {
    return }
  ```


  ```jsx
// Filename: src/App.tsx

  import { SignInButton } from '@clerk/react'

  function App() {
    return }

  export default App
  ```


  ```astro
// Filename: pages/sign-in.astro

  ---
  import { SignInButton } from '@clerk/astro/components'
  ---

  ```


  > [!NOTE]
> This component is for Expo web projects. For native iOS and Android apps, use the [native components](/reference/expo/native-components/overview) from `@clerk/expo/native` instead.


  ```jsx
// Filename: /app/sign-in.web.tsx

  import { SignInButton } from '@clerk/expo/web'

  export default function SignInPage() {
    return }
  ```


  ```jsx
// Filename: src/routes/sign-in.tsx

  import { SignInButton } from '@clerk/chrome-extension'

  export default function SignInPage() {
    return }
  ```


  ```tsx
// Filename: app/routes/_index.tsx

  import { SignInButton } from '@clerk/remix'

  export default function Home() {
    return }
  ```


  ```tsx
// Filename: app/routes/home.tsx

  import { SignInButton } from '@clerk/react-router'

  export default function Home() {
    return }
  ```


  ```tsx
// Filename: app/routes/sign-in.tsx

  import { SignInButton } from '@clerk/tanstack-react-start'
  import { createFileRoute } from '@tanstack/react-router'

  export const Route = createFileRoute('/sign-in')({
    component: SignIn,
  })

  function SignIn() {
    return }
  ```


  ```vue
// Filename: pages/sign-in.vue

  <script setup>
  // Components are automatically imported
  </script>

  <template>
    </template>
  ```


  ```vue
// Filename: example.vue

  <script setup>
  import { SignInButton } from '@clerk/vue'
  </script>

  <template>
    </template>
  ```


### Custom usage

You can create a custom button by wrapping your own button, or button text, in the `` component.


  ```jsx
// Filename: pages/index.js

  import { SignInButton } from '@clerk/nextjs'

  export default function Home() {
    return (
      
        <button>Custom sign in button</button>
      
    )
  }
  ```


  ```jsx
// Filename: src/App.tsx

  import { SignInButton } from '@clerk/react'

  function App() {
    return (
      
        <button>Custom sign in button</button>
      
    )
  }

  export default App
  ```


  You must pass the `asChild` prop to the `` component if you are passing children to it.

  ```astro
// Filename: pages/index.astro

  ---
  import { SignInButton } from '@clerk/astro/components'
  ---

  
    <button>Custom sign in button</button>
  
  ```


  > [!NOTE]
> This component is for Expo web projects. For native iOS and Android apps, use the [native components](/reference/expo/native-components/overview) from `@clerk/expo/native` instead.


  ```jsx
// Filename: /app/index.tsx

  import { SignInButton } from '@clerk/expo/web'

  export default function Home() {
    return (
      
        <button>Custom sign in button</button>
      
    )
  }
  ```


  ```jsx
// Filename: src/routes/home.tsx

  import { SignInButton } from '@clerk/chrome-extension'

  export default function Home() {
    return (
      
        <button>Custom sign in button</button>
      
    )
  }
  ```


  ```tsx
// Filename: app/routes/_index.tsx

  import { SignInButton } from '@clerk/remix'

  export default function Home() {
    return (
      
        <button>Custom sign in button</button>
      
    )
  }
  ```


  ```tsx
// Filename: app/routes/home.tsx

  import { SignInButton } from '@clerk/react-router'

  export default function Home() {
    return (
      
        <button>Custom sign in button</button>
      
    )
  }
  ```


  ```tsx
// Filename: app/routes/sign-in.tsx

  import { SignInButton } from '@clerk/tanstack-react-start'
  import { createFileRoute } from '@tanstack/react-router'

  export const Route = createFileRoute('/sign-in')({
    component: SignIn,
  })

  function SignIn() {
    return (
      
        <button>Custom sign in button</button>
      
    )
  }
  ```


  ```vue
// Filename: pages/index.vue

  <script setup>
  // Components are automatically imported
  </script>

  <template>
    
      <button>Custom sign in button</button>
    
  </template>
  ```


  ```vue
// Filename: example.vue

  <script setup>
  import { SignInButton } from '@clerk/vue'
  </script>

  <template>
    
      <button>Custom sign in button</button>
    
  </template>
  ```


## Properties

- **`forceRedirectUrl?`** `string`

  If provided, this URL will always be redirected to after the user signs in. It's recommended to use [the environment variable](/guides/development/clerk-environment-variables#sign-in-and-sign-up-redirects) instead.

    ---

- **`fallbackRedirectUrl?`** `string`

  The fallback URL to redirect to after the user signs in, if there's no `redirect_url` in the path already. Defaults to `/`. It's recommended to use [the environment variable](/guides/development/clerk-environment-variables#sign-in-and-sign-up-redirects) instead.

    ---

- **`oauthFlow`** `"redirect" | "popup" | "auto"`

  Determines how OAuth authentication is performed. Accepts the following properties:

- **`"redirect"`: Redirect to the OAuth provider on the current page.** `"popup"`: Open a popup window. `"auto"`: Choose the best method based on whether the current domain typically requires the `"popup"` flow to correctly perform authentication.

  Defaults to `"auto"`.

    ---

- **`signUpForceRedirectUrl?`** `string`

  If provided, this URL will always be redirected to after the user signs up. It's recommended to use [the environment variable](/guides/development/clerk-environment-variables#sign-in-and-sign-up-redirects) instead.

    ---

- **`signUpFallbackRedirectUrl?`** `string`

  The fallback URL to redirect to after the user signs up, if there's no `redirect_url` in the path already. Defaults to `/`. It's recommended to use [the environment variable](/guides/development/clerk-environment-variables#sign-in-and-sign-up-redirects) instead.

    ---

- **`mode?`** `'redirect' | 'modal'`

  Determines what happens when a user clicks on the ``. Setting this to `'redirect'` will redirect the user to the sign-in route. Setting this to `'modal'` will open a modal on the current route. Defaults to `'redirect'`.

    ---

- **`children?`** `React.ReactNode`

  Children you want to wrap the `` in.

    ---

- **`initialValues`** [`SignInInitialValues`](/reference/javascript/types/sign-in-initial-values)

  The values used to prefill the sign-in fields with.


  - **`asChild?`** `boolean`

  If `true`, the `` component will render its children as a child of the component.
