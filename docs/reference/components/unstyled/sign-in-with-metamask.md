# <SignInWithMetamaskButton>


> The <SignInWithMetamaskButton> component is used to complete a one-click, cryptographically-secure sign-in flow using MetaMask.

The `` component is used to complete a one-click, cryptographically-secure sign-in flow using MetaMask.

## Usage

### Basic usage


  ```jsx
// Filename: app/page.tsx

  import { SignInWithMetamaskButton } from '@clerk/nextjs'

  export default function Home() {
    return }
  ```


  ```jsx
// Filename: src/App.tsx

  import { SignInWithMetamaskButton } from '@clerk/react'

  function App() {
    return }

  export default App
  ```


  > [!NOTE]
> This component is for Expo web projects. For native iOS and Android apps, use the [native components](/reference/expo/native-components/overview) from `@clerk/expo/native` instead.


  ```jsx
// Filename: /app/page.web.tsx

  import { SignInWithMetamaskButton } from '@clerk/expo/web'

  export default function Home() {
    return }
  ```


  ```tsx
// Filename: app/routes/_index.tsx

  import { SignInWithMetamaskButton } from '@clerk/remix'

  export default function Home() {
    return }
  ```


  ```tsx
// Filename: app/routes/index.tsx

  import { SignInWithMetamaskButton } from '@clerk/tanstack-react-start'
  import { createFileRoute } from '@tanstack/react-router'

  export const Route = createFileRoute('/')({
    component: Home,
  })

  function Home() {
    return }
  ```


  ```tsx
// Filename: app/routes/home.tsx

  import { SignInWithMetamaskButton } from '@clerk/react-router'

  export default function Home() {
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
  import { SignInWithMetamaskButton } from '@clerk/vue'
  </script>

  <template>
    </template>
  ```


### Custom usage

In some cases, you will want to use your own button, or button text. You can do that by wrapping your button in the `` component.


  ```jsx
// Filename: pages/index.js

  import { SignInWithMetamaskButton } from '@clerk/nextjs'

  export default function Home() {
    return (
      
        <button>Custom sign in button</button>
      
    )
  }
  ```


  ```jsx
// Filename: src/App.tsx

  import { SignInWithMetamaskButton } from '@clerk/react'

  function App() {
    return (
      
        <button>Custom sign in button</button>
      
    )
  }

  export default App
  ```


  > [!NOTE]
> This component is for Expo web projects. For native iOS and Android apps, use the [native components](/reference/expo/native-components/overview) from `@clerk/expo/native` instead.


  ```jsx
// Filename: /app/page.web.tsx

  import { SignInWithMetamaskButton } from '@clerk/expo/web'

  export default function Home() {
    return (
      
        <button>Custom sign in button</button>
      
    )
  }
  ```


  ```tsx
// Filename: app/routes/_index.tsx

  import { SignInWithMetamaskButton } from '@clerk/remix'

  export default function Home() {
    return (
      
        <button>Custom sign in button</button>
      
    )
  }
  ```


  ```tsx
// Filename: app/routes/index.tsx

  import { SignInWithMetamaskButton } from '@clerk/tanstack-react-start'
  import { createFileRoute } from '@tanstack/react-router'

  export const Route = createFileRoute('/')({
    component: Home,
  })

  function Home() {
    return (
      
        <button>Custom sign in button</button>
      
    )
  }
  ```


  ```tsx
// Filename: app/routes/home.tsx

  import { SignInWithMetamaskButton } from '@clerk/react-router'

  export default function Home() {
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
  import { SignInWithMetamaskButton } from '@clerk/vue'
  </script>

  <template>
    
      <button>Custom sign in button</button>
    
  </template>
  ```
