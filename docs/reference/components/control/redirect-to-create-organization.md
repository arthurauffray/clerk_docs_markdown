# <RedirectToCreateOrganization />` (deprecated)


> The <RedirectToCreateOrganization /> component will navigate to the create Organization flow which has been configured in your application instance. The behavior will be just like a server-side (3xx) redirect, and will override the current location in the history stack.

> [!WARNING]
> This feature is deprecated. Please use the [`redirectToCreateOrganization()` method](/reference/javascript/clerk#redirect-to-create-organization) instead.

The `` component will navigate to the create Organization flow which has been configured in your application instance. The behavior will be just like a server-side (3xx) redirect, and will override the current location in the history stack.

## Example


  ```tsx
// Filename: app/page.tsx

  import { Show, RedirectToCreateOrganization } from '@clerk/nextjs'

  export default function Page() {
    return (
      <>
        
          You need to sign in to create an Organization.
      </>
    )
  }
  ```


  ```tsx
// Filename: pages/index.tsx

  import { Show, RedirectToCreateOrganization } from '@clerk/react'

  export default function Page() {
    return (
      <>
        
          You need to sign in to create an Organization.
      </>
    )
  }
  ```


  ```tsx
// Filename: app/routes/home.tsx

  import { Show, RedirectToCreateOrganization } from '@clerk/react-router'

  export default function Home() {
    return (
      <>
        
          You need to sign in to create an Organization.
      </>
    )
  }
  ```


  ```tsx
// Filename: app/routes/_index.tsx

  import { Show, RedirectToCreateOrganization } from '@clerk/remix'

  export default function Index() {
    return (
      <div>
        
          <p>You need to sign in to create an Organization.</p>
        
      </div>
    )
  }
  ```


  ```tsx
// Filename: app/routes/index.tsx

  import { Show, RedirectToCreateOrganization } from '@clerk/tanstack-react-start'
  import { createFileRoute } from '@tanstack/react-router'

  export const Route = createFileRoute('/')({
    component: Home,
  })

  function Home() {
    return (
      <div>
        
          <p>You need to sign in to create an Organization.</p>
        
      </div>
    )
  }
  ```


  ```vue
// Filename: App.vue

  <script setup lang="ts">
  import { Show, RedirectToCreateOrganization } from '@clerk/vue'
  </script>

  <template>
    
      <p>You need to sign in to create an Organization.</p>
    
  </template>
  ```


  ```vue
// Filename: App.vue

  <script setup lang="ts">
  // Components are automatically imported
  </script>

  <template>
    
      <p>You need to sign in to create an Organization.</p>
    
  </template>
  ```
