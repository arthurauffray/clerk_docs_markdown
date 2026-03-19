# <SignUpButton>


> The <SignUpButton> component is a button that links to the sign-up page or displays the sign-up modal.

The `` component is a button that, by default, links to your app's sign-up page. Your sign-up page will be hosted by Clerk using the [Account Portal](/guides/account-portal/overview) unless you have set up a [dedicated sign-up page](/guides/development/custom-sign-in-or-up-page).

## Usage

### Basic usage


  ```jsx
// Filename: app/page.tsx

  import { SignUpButton } from '@clerk/nextjs'

  export default function Home() {
    return }
  ```


  ```jsx
// Filename: src/App.tsx

  import { SignUpButton } from '@clerk/react'

  function App() {
    return }

  export default App
  ```


  ```astro
// Filename: pages/sign-up.astro

  ---
  import { SignUpButton } from '@clerk/astro/components'
  ---

  ```


  > [!NOTE]
> This component is for Expo web projects. For native iOS and Android apps, use the [native components](/reference/expo/native-components/overview) from `@clerk/expo/native` instead.


  ```jsx
// Filename: /app/sign-up.web.tsx

  import { SignUpButton } from '@clerk/expo/web'

  export default function SignUpPage() {
    return }
  ```


  ```jsx
// Filename: src/routes/sign-up.tsx

  import { SignUpButton } from '@clerk/chrome-extension'

  export default function SignUpPage() {
    return }
  ```


  ```jsx
// Filename: src/routes/_index.tsx

  import { SignUpButton } from '@clerk/remix'

  export default function Home() {
    return }
  ```


  ```tsx
// Filename: app/routes/home.tsx

  import { SignUpButton } from '@clerk/react-router'

  export default function Home() {
    return }
  ```


  ```tsx
// Filename: app/routes/sign-up.tsx

  import { SignUpButton } from '@clerk/tanstack-react-start'
  import { createFileRoute } from '@tanstack/react-router'

  export const Route = createFileRoute('/sign-up')({
    component: SignUp,
  })

  function SignUp() {
    return }
  ```


  ```vue
// Filename: pages/sign-up.vue

  <script setup>
  // Components are automatically imported
  </script>

  <template>
    </template>
  ```


  ```vue
// Filename: src/App.vue

  <script setup>
  import { SignUpButton } from '@clerk/vue'
  </script>

  <template>
    </template>
  ```


### Custom usage

You can create a custom button by wrapping your own button, or button text, in the `` component.


  ```jsx
// Filename: app/page.tsx

  import { SignUpButton } from '@clerk/nextjs'

  export default function Home() {
    return (
      
        <button>Custom sign up button</button>
      
    )
  }
  ```


  ```jsx
// Filename: src/App.jsx

  import { SignUpButton } from '@clerk/react'

  function App() {
    return (
      
        <button>Custom sign up button</button>
      
    )
  }

  export default App
  ```


  You must pass the `asChild` prop to the `` component if you are passing children to it.

  ```astro
// Filename: src/pages/index.astro

  ---
  import { SignUpButton } from '@clerk/astro/components'
  ---

  
    <button>Custom sign up button</button>
  
  ```


  > [!NOTE]
> This component is for Expo web projects. For native iOS and Android apps, use the [native components](/reference/expo/native-components/overview) from `@clerk/expo/native` instead.


  ```jsx
// Filename: /app/index.tsx

  import { SignUpButton } from '@clerk/expo/web'

  export default function Home() {
    return (
      
        <button>Custom sign up button</button>
      
    )
  }
  ```


  ```jsx
// Filename: src/routes/home.tsx

  import { SignUpButton } from '@clerk/chrome-extension'

  export default function Home() {
    return (
      
        <button>Custom sign up button</button>
      
    )
  }
  ```


  ```tsx
// Filename: app/routes/_index.tsx

  import { SignUpButton } from '@clerk/remix'

  export default function Home() {
    return (
      
        <button>Custom sign up button</button>
      
    )
  }
  ```


  ```tsx
// Filename: app/routes/home.tsx

  import { SignUpButton } from '@clerk/react-router'

  export default function Home() {
    return (
      
        <button>Custom sign up button</button>
      
    )
  }
  ```


  ```vue
// Filename: pages/index.vue

  <script setup>
  // Components are automatically imported
  </script>

  <template>
    
      <button>Custom sign up button</button>
    
  </template>
  ```


  ```vue
// Filename: src/App.vue

  <script setup>
  import { SignUpButton } from '@clerk/vue'
  </script>

  <template>
    
      <button>Custom sign up button</button>
    
  </template>
  ```


  ```tsx
// Filename: app/routes/index.tsx

  import { SignUpButton } from '@clerk/tanstack-react-start'
  import { createFileRoute } from '@tanstack/react-router'

  export const Route = createFileRoute('/')({
    component: Home,
  })

  function Home() {
    return (
      
        <button>Custom sign up button</button>
      
    )
  }
  ```


## Properties

- **`forceRedirectUrl?`** `string`

  If provided, this URL will always be redirected to after the user signs up. It's recommended to use [the environment variable](/guides/development/clerk-environment-variables#sign-in-and-sign-up-redirects) instead.

    ---

- **`fallbackRedirectUrl?`** `string`

  The fallback URL to redirect to after the user signs up, if there's no `redirect_url` in the path already. Defaults to `/`. It's recommended to use [the environment variable](/guides/development/clerk-environment-variables#sign-in-and-sign-up-redirects) instead.

    ---

- **`oauthFlow`** `"redirect" | "popup" | "auto"`

  Determines how OAuth authentication is performed. Accepts the following properties:

- **`"redirect"`: Redirect to the OAuth provider on the current page.** `"popup"`: Open a popup window. `"auto"`: Choose the best method based on whether the current domain typically requires the `"popup"` flow to correctly perform authentication.

  Defaults to `"auto"`.

    ---

- **`signInForceRedirectUrl?`** `string`

  If provided, this URL will always be redirected to after the user signs in. It's recommended to use [the environment variable](/guides/development/clerk-environment-variables#sign-in-and-sign-up-redirects) instead.

    ---

- **`signInFallbackRedirectUrl?`** `string`

  The fallback URL to redirect to after the user signs in, if there's no `redirect_url` in the path already. Defaults to `/`. It's recommended to use [the environment variable](/guides/development/clerk-environment-variables#sign-in-and-sign-up-redirects) instead.

    ---

- **`mode?`** `'redirect' | 'modal'`

  Determines what happens when a user clicks on the ``. Setting this to `'redirect'` will redirect the user to the sign-up route. Setting this to `'modal'` will open a modal on the current route. Defaults to `'redirect'`

    ---

- **`children?`** `React.ReactNode`

  Children you want to wrap the `` in.

    ---

- **`initialValues`** [`SignUpInitialValues`](/reference/javascript/types/sign-up-initial-values)

  The values used to prefill the sign-up fields with.

    ---

- **`unsafeMetadata`** [`SignUpUnsafeMetadata`](/reference/javascript/types/metadata#sign-up-unsafe-metadata)

  Metadata that can be read and set from the frontend and the backend. Once the sign-up is complete, the value of this field will be automatically copied to the created user's unsafe metadata (`User.unsafeMetadata`). One common use case is to collect custom information about the user during the sign-up process and store it in this property. Read more about [unsafe metadata](/guides/users/extending#unsafe-metadata).


  - **`asChild?`** `boolean`

  If `true`, the `` component will render its children as a child of the component.
