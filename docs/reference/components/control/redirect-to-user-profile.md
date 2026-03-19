# <RedirectToUserProfile />` (deprecated)


> The <RedirectToUserProfile /> component will navigate to the user profile URL which has been configured in your application instance. The behavior will be just like a server-side (3xx) redirect, and will override the current location in the history stack.

> [!WARNING]
> This feature is deprecated. Please use the [`redirectToUserProfile()` method](/reference/javascript/clerk#redirect-to-user-profile) instead.

The `` component will navigate to the Account Portal User Profile URL which has been configured in your application instance. The behavior will be just like a server-side (3xx) redirect, and will override the current location in the history stack.

To find your User Profile URL:

1. In the Clerk Dashboard, navigate to the [**Account Portal**](https://dashboard.clerk.com/~/account-portal) page.
1. Under **User profile**, select the **Visit** icon.

## Example


  ```tsx
// Filename: app/page.tsx

  import { Show, RedirectToUserProfile } from '@clerk/nextjs'

  function Page() {
    return (
      <>
        
          <p>You need to sign in to view your user profile.</p>
        
      </>
    )
  }
  ```


  ```tsx
// Filename: pages/index.tsx

  import { Show, RedirectToUserProfile } from '@clerk/react'

  export default function Page() {
    return (
      <>
        
          <p>You need to sign in to view your user profile.</p>
        
      </>
    )
  }
  ```


  ```tsx
// Filename: app/routes/home.tsx

  import { Show, RedirectToUserProfile } from '@clerk/react-router'

  export default function Home() {
    return (
      <>
        
          <p>You need to sign in to view your user profile.</p>
        
      </>
    )
  }
  ```


  ```tsx
// Filename: app/routes/_index.tsx

  import { Show, RedirectToUserProfile } from '@clerk/remix'

  export default function Index() {
    return (
      <div>
        
          <p>You need to sign in to view your user profile.</p>
        
      </div>
    )
  }
  ```


  ```tsx
// Filename: app/routes/index.tsx

  import { Show, RedirectToUserProfile } from '@clerk/tanstack-react-start'
  import { createFileRoute } from '@tanstack/react-router'

  export const Route = createFileRoute('/')({
    component: Home,
  })

  function Home() {
    return (
      <div>
        
          <p>You need to sign in to view your user profile.</p>
        
      </div>
    )
  }
  ```


  ```vue
// Filename: App.vue

  <script setup lang="ts">
  import { Show, RedirectToUserProfile } from '@clerk/vue'
  </script>

  <template>
    
      <p>You need to sign in to view your user profile.</p>
    
  </template>
  ```


  ```vue
// Filename: App.vue

  <script setup lang="ts">
  // Components are automatically imported
  </script>

  <template>
    
      <p>You need to sign in to view your user profile.</p>
    
  </template>
  ```
