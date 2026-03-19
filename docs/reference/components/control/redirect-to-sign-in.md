# <RedirectToSignIn />


> The <RedirectToSignIn /> component will navigate to the sign in URL which has been configured in your application instance. The behavior will be just like a server-side (3xx) redirect, and will override the current location in the history stack.

The `` component will navigate to the sign in URL which has been configured in your application instance. The behavior will be just like a server-side (3xx) redirect, and will override the current location in the history stack.

## Example


  ```tsx
// Filename: app/page.tsx

  import { Show, RedirectToSignIn, UserButton } from '@clerk/nextjs'

  export default function Page() {
    return (
      <>
        
          </>
    )
  }
  ```


  ```tsx
// Filename: pages/index.tsx

  import { Show, RedirectToSignIn, UserButton } from '@clerk/react'

  export default function Page() {
    return (
      <>
        
          </>
    )
  }
  ```


  ```tsx
// Filename: app/routes/home.tsx

  import { Show, RedirectToSignIn, UserButton } from '@clerk/react-router'

  export default function Home() {
    return (
      <>
        
          </>
    )
  }
  ```


  > [!NOTE]
  > This component relies on React Router for navigation. Ensure that you have integrated React Router into your Chrome Extension application before using it. [Learn how to add React Router to your Chrome Extension](/guides/development/add-react-router).

  ```jsx
// Filename: src/routes/home.tsx

  import { Show, RedirectToSignIn, UserButton } from '@clerk/chrome-extension'

  export default function Home() {
    return (
      <>
        
          </>
    )
  }
  ```


  ```tsx
// Filename: app/routes/_index.tsx

  import { Show, RedirectToSignIn, UserButton } from '@clerk/remix'

  export default function Index() {
    return (
      <div>
        
          </div>
    )
  }
  ```


  ```tsx
// Filename: app/routes/index.tsx

  import { Show, RedirectToSignIn, UserButton } from '@clerk/tanstack-react-start'
  import { createFileRoute } from '@tanstack/react-router'

  export const Route = createFileRoute('/')({
    component: Home,
  })

  function Home() {
    return (
      <div>
        
          </div>
    )
  }
  ```


  ```vue
// Filename: App.vue

  <script setup lang="ts">
  import { Show, RedirectToSignIn, UserButton } from '@clerk/vue'
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
