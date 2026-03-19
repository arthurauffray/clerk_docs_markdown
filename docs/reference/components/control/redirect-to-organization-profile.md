# <RedirectToOrganizationProfile />` (deprecated)


> The <RedirectToOrganizationProfile /> component will navigate to the Organization profile URL which has been configured in your application instance. The behavior will be just like a server-side (3xx) redirect, and will override the current location in the history stack.

> [!WARNING]
> This feature is deprecated. Please use the [`redirectToOrganizationProfile()` method](/reference/javascript/clerk#redirect-to-organization-profile) instead.

The `` component will navigate to the Organization profile URL which has been configured in your application instance. The behavior will be just like a server-side (3xx) redirect, and will override the current location in the history stack.

## Example


  ```tsx
// Filename: app/page.tsx

  import { Show, RedirectToOrganizationProfile } from '@clerk/nextjs'

  export default function Page() {
    return (
      <>
        
          You need to sign in to view your Organization profile.
      </>
    )
  }
  ```


  ```tsx
// Filename: pages/index.tsx

  import { Show, RedirectToOrganizationProfile } from '@clerk/react'

  export default function Page() {
    return (
      <>
        
          You need to sign in to view your Organization profile.
      </>
    )
  }
  ```


  ```tsx
// Filename: app/routes/Home.tsx

  import { Show, RedirectToOrganizationProfile } from '@clerk/react-router'

  export default function Home() {
    return (
      <>
        
          You need to sign in to view your Organization profile.
      </>
    )
  }
  ```


  ```tsx
// Filename: app/routes/_index.tsx

  import { Show, RedirectToOrganizationProfile } from '@clerk/remix'

  export default function Index() {
    return (
      <div>
        
          <p>You need to sign in to view your Organization profile.</p>
        
      </div>
    )
  }
  ```


  ```tsx
// Filename: app/routes/index.tsx

  import { Show, RedirectToOrganizationProfile } from '@clerk/tanstack-react-start'
  import { createFileRoute } from '@tanstack/react-router'

  export const Route = createFileRoute('/')({
    component: Home,
  })

  function Home() {
    return (
      <div>
        
          <p>You need to sign in to view your Organization profile.</p>
        
      </div>
    )
  }
  ```


  ```vue
// Filename: App.vue

  <script setup lang="ts">
  import { Show, RedirectToOrganizationProfile } from '@clerk/vue'
  </script>

  <template>
    
      <p>You need to sign in to view your Organization profile.</p>
    
  </template>
  ```


  ```vue
// Filename: App.vue

  <script setup lang="ts">
  // Components are automatically imported
  </script>

  <template>
    
      <p>You need to sign in to view your Organization profile.</p>
    
  </template>
  ```
