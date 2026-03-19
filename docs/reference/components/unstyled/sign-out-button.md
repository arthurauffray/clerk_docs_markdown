# <SignOutButton>


> The <SignOutButton> component is a button that signs a user out.

The `` component is a button that signs a user out. By default, it is a `<button>` tag that says **Sign Out**, but it is completely customizable by passing children.

## Usage

### Basic usage


  ```jsx
// Filename: app/page.tsx

  import { SignOutButton } from '@clerk/nextjs'

  export default function Home() {
    return }
  ```


  ```jsx
// Filename: src/App.tsx

  import { SignOutButton } from '@clerk/react'

  function App() {
    return }

  export default App
  ```


  ```astro
// Filename: pages/sign-out.astro

  ---
  import { SignOutButton } from '@clerk/astro/components'
  ---

  ```


  > [!NOTE]
> This component is for Expo web projects. For native iOS and Android apps, use the [native components](/reference/expo/native-components/overview) from `@clerk/expo/native` instead.


  ```jsx
// Filename: /app/sign-out.web.tsx

  import { SignOutButton } from '@clerk/expo/web'

  export default function SignOutPage() {
    return }
  ```


  ```jsx
// Filename: src/routes/sign-out.tsx

  import { SignOutButton } from '@clerk/chrome-extension'

  export default function SignOutPage() {
    return }
  ```


  ```tsx
// Filename: app/routes/_index.tsx

  import { SignOutButton } from '@clerk/remix'

  export default function Home() {
    return }
  ```


  ```tsx
// Filename: app/routes/home.tsx

  import { SignOutButton } from '@clerk/react-router'

  export default function Home() {
    return }
  ```


  ```tsx
// Filename: app/routes/sign-out.tsx

  import { SignOutButton } from '@clerk/tanstack-react-start'
  import { createFileRoute } from '@tanstack/react-router'

  export const Route = createFileRoute('/sign-out')({
    component: SignOut,
  })

  function SignOut() {
    return }
  ```


  ```vue
// Filename: pages/sign-out.vue

  <script setup>
  // Components are automatically imported
  </script>

  <template>
    </template>
  ```


  ```vue
// Filename: sign-out.vue

  <script setup>
  import { SignOutButton } from '@clerk/vue'
  </script>

  <template>
    </template>
  ```


### Custom usage

You can create a custom button by wrapping your own button, or button text, in the `` component.


  ```jsx
// Filename: app/page.js

  import { SignOutButton } from '@clerk/nextjs'

  export default function Home() {
    return (
      
        <button>Custom sign out button</button>
      
    )
  }
  ```


  ```jsx
// Filename: src/App.tsx

  import { SignOutButton } from '@clerk/react'

  function App() {
    return (
      
        <button>Custom sign out button</button>
      
    )
  }

  export default App
  ```


  You must pass the `asChild` prop to the `` component if you are passing children to it.

  ```astro
// Filename: pages/index.astro

  ---
  import { SignOutButton } from '@clerk/astro/components'
  ---

  
    <button>Custom sign out button</button>
  
  ```


  > [!NOTE]
> This component is for Expo web projects. For native iOS and Android apps, use the [native components](/reference/expo/native-components/overview) from `@clerk/expo/native` instead.


  ```jsx
// Filename: /app/index.tsx

  import { SignOutButton } from '@clerk/expo/web'

  export default function Home() {
    return (
      
        <button>Custom sign out button</button>
      
    )
  }
  ```


  ```jsx
// Filename: src/routes/home.tsx

  import { SignOutButton } from '@clerk/chrome-extension'

  export default function Home() {
    return (
      
        <button>Custom sign out button</button>
      
    )
  }
  ```


  ```tsx
// Filename: app/routes/_index.tsx

  import { SignOutButton } from '@clerk/remix'

  export default function Home() {
    return (
      
        <button>Custom sign out button</button>
      
    )
  }
  ```


  ```tsx
// Filename: app/routes/home.tsx

  import { SignOutButton } from '@clerk/react-router'

  export default function Home() {
    return (
      
        <button>Custom sign out button</button>
      
    )
  }
  ```


  ```vue
// Filename: pages/index.vue

  <script setup>
  // Components are automatically imported
  </script>

  <template>
    
      <button>Custom sign out button</button>
    
  </template>
  ```


  ```vue
// Filename: example.vue

  <script setup>
  import { SignOutButton } from '@clerk/vue'
  </script>

  <template>
    
      <button>Custom sign out button</button>
    
  </template>
  ```


  ```tsx
// Filename: app/routes/index.tsx

  import { SignOutButton } from '@clerk/tanstack-react-start'
  import { createFileRoute } from '@tanstack/react-router'

  export const Route = createFileRoute('/')({
    component: Home,
  })

  function Home() {
    return (
      
        <button>Custom sign out button</button>
      
    )
  }
  ```


### Multi-session usage

#### Sign out of all sessions

Clicking the `` component signs the user out of all sessions. This is the default behavior.

#### Sign out of a specific session

You can sign out of a specific session by passing in a `sessionId` to the `sessionId` prop. This is useful for signing a single account out of a [multi-session application](/guides/secure/session-options#multi-session-applications).

In the following example, the `sessionId` is retrieved from the [`useAuth()`](/reference/hooks/use-auth) hook. If the user is not signed in, the `sessionId` will be `null`, and the user is shown the [``](/reference/components/unstyled/sign-in-button) component. If the user is signed in, the user is shown the `` component, which when clicked, signs the user out of that specific session.


  ```tsx
// Filename: app/page.tsx

  'use client'

  import { SignInButton, SignOutButton, useAuth } from '@clerk/nextjs'

  export default function Home() {
    const { sessionId } = useAuth()

    if (!sessionId) {
      return }

    return }
  ```


  ```jsx
// Filename: src/App.tsx

  import { SignInButton, SignOutButton, useAuth } from '@clerk/react'

  function App() {
    const { sessionId } = useAuth()

    if (!sessionId) {
      return }

    return }

  export default App
  ```


  ```tsx
// Filename: app/routes/_index.tsx

  import { SignInButton, SignOutButton, useAuth } from '@clerk/remix'

  export default function Home() {
    const { sessionId } = useAuth()

    if (!sessionId) {
      return }

    return }
  ```


  ```tsx
// Filename: app/routes/home.tsx

  import { SignInButton, SignOutButton, useAuth } from '@clerk/react-router'

  export default function Home() {
    const { sessionId } = useAuth()

    if (!sessionId) {
      return }

    return }
  ```


  ```jsx
// Filename: src/routes/home.tsx

  import { SignInButton, SignOutButton, useAuth } from '@clerk/chrome-extension'

  export default function Home() {
    const { sessionId } = useAuth()

    if (!sessionId) {
      return }

    return }
  ```


  ```vue
// Filename: pages/index.vue

  <script setup>
  // Components are automatically imported
  // Composables are automatically imported
  const { sessionId } = useAuth()
  </script>

  <template>
    </template>
  ```


  ```vue
// Filename: example.vue

  <script setup>
  import { SignInButton, SignOutButton, useAuth } from '@clerk/vue'

  const { sessionId } = useAuth()
  </script>

  <template>
    </template>
  ```


  ```astro
// Filename: pages/index.astro

  ---
  import { SignInButton, SignOutButton } from '@clerk/astro/components'
  import { useAuth } from '@clerk/astro/react'
  const { sessionId } = useAuth()
  ---

  {sessionId ? : }
  ```


  > [!NOTE]
> This component is for Expo web projects. For native iOS and Android apps, use the [native components](/reference/expo/native-components/overview) from `@clerk/expo/native` instead.


  ```jsx
// Filename: /app/index.web.tsx

  import { SignInButton, SignOutButton, useAuth } from '@clerk/expo/web'

  export default function Home() {
    const { sessionId } = useAuth()

    if (!sessionId) {
      return }

    return }
  ```


  ```tsx
// Filename: app/routes/index.tsx

  import { SignInButton, SignOutButton, useAuth } from '@clerk/tanstack-react-start'
  import { createFileRoute } from '@tanstack/react-router'

  export const Route = createFileRoute('/')({
    component: Home,
  })

  function Home() {
    const { sessionId } = useAuth()

    if (!sessionId) {
      return }

    return }
  ```


## Properties

- **`redirectUrl?`** `string`

  The full URL or path to navigate after successful sign-out.

    ---

- **`sessionId?`** `string`

  The ID of a specific session to sign out of. Useful for [multi-session applications](/guides/secure/session-options#multi-session-applications).

    ---

- **`children?`** `React.ReactNode`

  Children you want to wrap the `` in.


  - **`asChild?`** `boolean`

  If `true`, the `` component will render its children as a child of the component.
