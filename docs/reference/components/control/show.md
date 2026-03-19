# <Show>


> The Show component protects content or even entire routes based on authentication, and optionally, authorization.

The [``](/reference/components/control/show) component protects content or even entire routes based on:

- authentication: whether the user is signed-in or not.
- authorization: whether the user has been granted a specific type of access control (Role, Permission, Feature, or Plan)

`` with `when='signed-in'` or `when='signed-out'` performs authentication checks. To perform authorization checks, you can pass different values to the `when` prop, like `when={{ role: '...' }}`, `when={{ permission: '...' }}`, `when={{ feature: '...' }}`, or `when={{ plan: '...' }}`.

`` accepts a `fallback` prop that will be rendered if the user fails the authentication or authorization checks.

`` can be used both client-side and server-side (in Server Components).

> [!CAUTION]
> This component only **visually hides** its children. The contents of its children remain accessible via the browser's source code even if the user fails the authentication/authorization check. Do not use this component to hide sensitive information that should be completely inaccessible to unauthorized users. For truly sensitive data, perform authorization checks on the server before sending the data to the client.

## Usage

### Authentication checks

`` performs authentication checks. It will render its children if the user is signed-in, and its `fallback` prop if the user is signed-out.


  ```tsx
// Filename: app/dashboard/page.tsx

  import { Show } from '@clerk/nextjs'

  export default function Page() {
    return (
      Users that are signed-out can see this.</p>} when="signed-in">
        <p>Users that are signed-in can see this.</p>
      
    )
  }
  ```


  ```jsx
// Filename: src/App.tsx

  import { Show } from '@clerk/react'

  function App() {
    return (
      Users that are signed-out can see this.</p>} when="signed-in">
        <p>Users that are signed-in can see this.</p>
      
    )
  }

  export default App
  ```


  ```astro
// Filename: src/pages/dashboard.astro

  ---
  import { Show } from '@clerk/astro/components'
  ---

  
    <p slot="fallback">Users that are signed-out can see this.</p>
    <p>Users that are signed-in can see this.</p>
  
  ```


  ```jsx
  import { Show } from '@clerk/expo'
  import { Text } from 'react-native'

  export default function Screen() {
    return (
      Users that are signed-out can see this.} when="signed-in">
        Users that are signed-in can see this.
      
    )
  }
  ```


  ```jsx
// Filename: src/routes/dashboard.tsx

  import { Show } from '@clerk/chrome-extension'

  export default function DashboardPage() {
    return (
      Users that are signed-out can see this.</p>} when="signed-in">
        <p>Users that are signed-in can see this.</p>
      
    )
  }
  ```


  ```tsx
// Filename: app/routes/dashboard.tsx

  import { Show } from '@clerk/remix'

  export default function DashboardPage() {
    return (
      Users that are signed-out can see this.</p>} when="signed-in">
        <p>Users that are signed-in can see this.</p>
      
    )
  }
  ```


  ```tsx
// Filename: app/routes/dashboard.tsx

  import { Show } from '@clerk/react-router'

  export default function DashboardPage() {
    return (
      Users that are signed-out can see this.</p>} when="signed-in">
        <p>Users that are signed-in can see this.</p>
      
    )
  }
  ```


  ```tsx
// Filename: app/routes/dashboard.tsx

  import { Show } from '@clerk/tanstack-react-start'
  import { createFileRoute } from '@tanstack/react-router'

  export const Route = createFileRoute('/dashboard')({
    component: DashboardPage,
  })

  function DashboardPage() {
    return (
      Users that are signed-out can see this.</p>} when="signed-in">
        <p>Users that are signed-in can see this.</p>
      
    )
  }
  ```


  ```vue
  <script setup lang="ts">
  import { Show } from '@clerk/vue'
  </script>

  <template>
    
      <template #fallback>
        <p>Users that are signed-out can see this.</p>
      </template>
      <p>Users that are signed-in can see this.</p>
    
  </template>
  ```


  ```vue
// Filename: pages/dashboard.vue

  <script setup lang="ts">
  // Components are automatically imported
  </script>

  <template>
    
      <template #fallback>
        <p>Users that are signed-out can see this.</p>
      </template>
      <p>Users that are signed-in can see this.</p>
    
  </template>
  ```


### Authorization checks

To limit who is able to see the content that `` renders, you can pass **one** of the access control values to the `when` prop: `when={{ permission: '...' }}`, `when={{ role: '...' }}`, `when={{ feature: '...' }}`, or `when={{ plan: '...' }}`. It's recommended to use **Permission-based** authorization over **Role-based** authorization, and **Feature-based** authorization over **Plan-based** authorization, as they are more flexible, easier to manage, and more secure.

If you use `when='signed-in'` without any access control values, `` will render its children if the user is signed in, regardless of their Role or its Permissions.

For more complex authorization logic, [pass conditional logic to the `when` prop](#render-content-conditionally).

### Render content by Permissions

The following example demonstrates how to use the `` component to protect content by checking if the user has the `org:invoices:create` Permission.


  ```jsx
// Filename: app/protected/invoices/page.tsx

  import { Show } from '@clerk/nextjs'

  export default function Page() {
    return (
      You do not have the Permissions to create an invoice.</p>}
      >
        <p>Users with Permission org:invoices:create can see this.</p>
      
    )
  }
  ```


  ```jsx
// Filename: src/App.tsx

  import { Show } from '@clerk/react'

  function App() {
    return (
      You do not have the Permissions to create an invoice.</p>}
      >
        <p>Users with Permission org:invoices:create can see this.</p>
      
    )
  }

  export default App
  ```


  ```astro
// Filename: src/pages/invoices.astro

  ---
  import { Show } from '@clerk/astro/components'
  ---

  
    <p slot="fallback">You do not have the Permissions to create an invoice.</p>
    <p>Users with Permission org:invoices:create can see this.</p>
  
  ```


  ```jsx
  import { Show } from '@clerk/expo'
  import { Text } from 'react-native'

  export default function Screen() {
    return (
      You do not have the Permissions to create an invoice.}
      >
        Users with Permission org:invoices:create can see this.
      
    )
  }
  ```


  ```jsx
// Filename: src/routes/invoices.tsx

  import { Show } from '@clerk/chrome-extension'

  export default function InvoicesPage() {
    return (
      You do not have the Permissions to create an invoice.</p>}
      >
        <p>Users with Permission org:invoices:create can see this.</p>
      
    )
  }
  ```


  ```tsx
// Filename: app/routes/invoices.tsx

  import { Show } from '@clerk/remix'

  export default function InvoicesPage() {
    return (
      You do not have the Permissions to create an invoice.</p>}
      >
        <p>Users with Permission org:invoices:create can see this.</p>
      
    )
  }
  ```


  ```tsx
// Filename: app/routes/invoices.tsx

  import { Show } from '@clerk/react-router'

  export default function InvoicesPage() {
    return (
      You do not have the Permissions to create an invoice.</p>}
      >
        <p>Users with Permission org:invoices:create can see this.</p>
      
    )
  }
  ```


  ```tsx
// Filename: app/routes/invoices.tsx

  import { Show } from '@clerk/tanstack-react-start'
  import { createFileRoute } from '@tanstack/react-router'

  export const Route = createFileRoute('/invoices')({
    component: InvoicesPage,
  })

  function InvoicesPage() {
    return (
      You do not have the Permissions to create an invoice.</p>}
      >
        <p>Users with Permission org:invoices:create can see this.</p>
      
    )
  }
  ```


  ```vue
  <script setup lang="ts">
  import { Show } from '@clerk/vue'
  </script>

  <template>
    
      <template #fallback>
        <p>You do not have the Permissions to create an invoice.</p>
      </template>
      <p>Users with Permission org:invoices:create can see this.</p>
    
  </template>
  ```


  ```vue
// Filename: pages/invoices.vue

  <script setup lang="ts">
  // Components are automatically imported
  </script>

  <template>
    
      <template #fallback>
        <p>You do not have the Permissions to create an invoice.</p>
      </template>
      <p>Users with Permission org:invoices:create can see this.</p>
    
  </template>
  ```


### Render content by Role

While authorization by `when={{ permission: '...' }}` is **recommended**, for convenience, `` allows a `when={{ role: '...' }}` prop to be passed.

The following example demonstrates how to use the `` component to protect content by checking if the user has the `org:billing` Role.


  ```jsx
// Filename: app/protected/billing/page.tsx

  import { Show } from '@clerk/nextjs'

  export default function ProtectPage() {
    return (
      Only a member of the Billing department can access this content.</p>}
      >
        <p>Users with Role org:billing can see this.</p>
      
    )
  }
  ```


  ```jsx
// Filename: src/App.tsx

  import { Show } from '@clerk/react'

  function App() {
    return (
      Only a member of the Billing department can access this content.</p>}
      >
        <p>Users with Role org:billing can see this.</p>
      
    )
  }

  export default App
  ```


  ```astro
// Filename: src/pages/billing.astro

  ---
  import { Show } from '@clerk/astro/components'
  ---

  
    <p slot="fallback">Only a member of the Billing department can access this content.</p>
    <p>Users with Role org:billing can see this.</p>
  
  ```


  ```jsx
  import { Show } from '@clerk/expo'
  import { Text } from 'react-native'

  export default function Screen() {
    return (
      Only a member of the Billing department can access this content.}
      >
        Users with Role org:billing can see this.
      
    )
  }
  ```


  ```jsx
// Filename: src/routes/billing.tsx

  import { Show } from '@clerk/chrome-extension'

  export default function BillingPage() {
    return (
      Only a member of the Billing department can access this content.</p>}
      >
        <p>Users with Role org:billing can see this.</p>
      
    )
  }
  ```


  ```tsx
// Filename: app/routes/billing.tsx

  import { Show } from '@clerk/remix'

  export default function BillingPage() {
    return (
      Only a member of the Billing department can access this content.</p>}
      >
        <p>Users with Role org:billing can see this.</p>
      
    )
  }
  ```


  ```tsx
// Filename: app/routes/billing.tsx

  import { Show } from '@clerk/react-router'

  export default function BillingPage() {
    return (
      Only a member of the Billing department can access this content.</p>}
      >
        <p>Users with Role org:billing can see this.</p>
      
    )
  }
  ```


  ```tsx
// Filename: app/routes/billing.tsx

  import { Show } from '@clerk/tanstack-react-start'
  import { createFileRoute } from '@tanstack/react-router'

  export const Route = createFileRoute('/billing')({
    component: BillingPage,
  })

  function BillingPage() {
    return (
      Only a member of the Billing department can access this content.</p>}
      >
        <p>Users with Role org:billing can see this.</p>
      
    )
  }
  ```


  ```vue
  <script setup lang="ts">
  import { Show } from '@clerk/vue'
  </script>

  <template>
    
      <template #fallback>
        <p>Only a member of the Billing department can access this content.</p>
      </template>
      <p>Users with Role org:billing can see this.</p>
    
  </template>
  ```


  ```vue
// Filename: pages/billing.vue

  <script setup lang="ts">
  // Components are automatically imported
  </script>

  <template>
    
      <template #fallback>
        <p>Only a member of the Billing department can access this content.</p>
      </template>
      <p>Users with Role org:billing can see this.</p>
    
  </template>
  ```


### Render content by Plan

The following example demonstrates how to use `` to protect content by checking if the user has a Plan.


  ```tsx
// Filename: app/protected/bronze/page.tsx

  import { Show } from '@clerk/nextjs'

  export default function ProtectPage() {
    return (
      Sorry, only subscribers to the Bronze plan can access this content.</p>}
      >
        <p>Welcome, Bronze subscriber!</p>
      
    )
  }
  ```


  ```tsx
// Filename: src/App.tsx

  import { Show } from '@clerk/react'

  function App() {
    return (
      Sorry, only subscribers to the Bronze plan can access this content.</p>}
      >
        <p>Welcome, Bronze subscriber!</p>
      
    )
  }

  export default App
  ```


  ```astro
// Filename: src/pages/bronze.astro

  ---
  import { Show } from '@clerk/astro/components'
  ---

  
    <p slot="fallback">Sorry, only subscribers to the Bronze plan can access this content.</p>
    <p>Welcome, Bronze subscriber!</p>
  
  ```


  ```tsx
// Filename: app/(billing)/bronze.tsx

  import { Show } from '@clerk/expo'
  import { Text } from 'react-native'

  export default function Page() {
    return (
      Sorry, only subscribers to the Bronze plan can access this content.}
      >
        Welcome, Bronze subscriber!
      
    )
  }
  ```


  ```jsx
// Filename: src/routes/bronze.tsx

  import { Show } from '@clerk/chrome-extension'

  export default function BronzePage() {
    return (
      Sorry, only subscribers to the Bronze plan can access this content.</p>}
      >
        <p>Welcome, Bronze subscriber!</p>
      
    )
  }
  ```


  ```tsx
// Filename: app/routes/bronze.tsx

  import { Show } from '@clerk/remix'

  export default function BronzePage() {
    return (
      Sorry, only subscribers to the Bronze plan can access this content.</p>}
      >
        <p>Welcome, Bronze subscriber!</p>
      
    )
  }
  ```


  ```tsx
// Filename: app/routes/bronze.tsx

  import { Show } from '@clerk/react-router'

  export default function BronzePage() {
    return (
      Sorry, only subscribers to the Bronze plan can access this content.</p>}
      >
        <p>Welcome, Bronze subscriber!</p>
      
    )
  }
  ```


  ```tsx
// Filename: app/routes/bronze.tsx

  import { Show } from '@clerk/tanstack-react-start'
  import { createFileRoute } from '@tanstack/react-router'

  export const Route = createFileRoute('/bronze')({
    component: BronzePage,
  })

  function BronzePage() {
    return (
      Sorry, only subscribers to the Bronze plan can access this content.</p>}
      >
        <p>Welcome, Bronze subscriber!</p>
      
    )
  }
  ```


  ```vue
  <script setup lang="ts">
  import { Show } from '@clerk/vue'
  </script>

  <template>
    
      <template #fallback>
        <p>Sorry, only subscribers to the Bronze plan can access this content.</p>
      </template>
      <p>Welcome, Bronze subscriber!</p>
    
  </template>
  ```


  ```vue
// Filename: pages/bronze.vue

  <script setup lang="ts">
  // Components are automatically imported
  </script>

  <template>
    
      <template #fallback>
        <p>Sorry, only subscribers to the Bronze plan can access this content.</p>
      </template>
      <p>Welcome, Bronze subscriber!</p>
    
  </template>
  ```


### Render content by Feature

The following example demonstrates how to use `` to protect content by checking if the user has a Feature.


  ```tsx
// Filename: app/protected/premium-access/page.tsx

  import { Show } from '@clerk/nextjs'

  export default function Page() {
    return (
      Sorry, only subscribers with the Premium Access feature can access this content.</p>
        }
      >
        <p>Congratulations! You have access to the Premium Access feature.</p>
      
    )
  }
  ```


  ```tsx
// Filename: src/App.tsx

  import { Show } from '@clerk/react'

  function App() {
    return (
      Sorry, only subscribers with the Premium Access feature can access this content.</p>
        }
      >
        <p>Congratulations! You have access to the Premium Access feature.</p>
      
    )
  }

  export default App
  ```


  ```astro
// Filename: src/pages/premium-access.astro

  ---
  import { Show } from '@clerk/astro/components'
  ---

  
    <p slot="fallback">
      Sorry, only subscribers with the Premium Access feature can access this content.
    </p>
    <p>Congratulations! You have access to the Premium Access feature.</p>
  
  ```


  ```tsx
// Filename: app/(billing)/premium-access.tsx

  import { Show } from '@clerk/expo'
  import { Text } from 'react-native'

  export default function Page() {
    return (
      
            Sorry, only subscribers with the Premium Access feature can access this content.
          
        }
      >
        Congratulations! You have access to the Premium Access feature.
      
    )
  }
  ```


  ```jsx
// Filename: src/routes/premium-access.tsx

  import { Show } from '@clerk/chrome-extension'

  export default function PremiumAccessPage() {
    return (
      Sorry, only subscribers with the Premium Access feature can access this content.</p>
        }
      >
        <p>Congratulations! You have access to the Premium Access feature.</p>
      
    )
  }
  ```


  ```tsx
// Filename: app/routes/premium-access.tsx

  import { Show } from '@clerk/remix'

  export default function PremiumAccessPage() {
    return (
      Sorry, only subscribers with the Premium Access feature can access this content.</p>
        }
      >
        <p>Congratulations! You have access to the Premium Access feature.</p>
      
    )
  }
  ```


  ```tsx
// Filename: app/routes/premium-access.tsx

  import { Show } from '@clerk/react-router'

  export default function PremiumAccessPage() {
    return (
      Sorry, only subscribers with the Premium Access feature can access this content.</p>
        }
      >
        <p>Congratulations! You have access to the Premium Access feature.</p>
      
    )
  }
  ```


  ```tsx
// Filename: app/routes/premium-access.tsx

  import { Show } from '@clerk/tanstack-react-start'
  import { createFileRoute } from '@tanstack/react-router'

  export const Route = createFileRoute('/premium-access')({
    component: PremiumAccessPage,
  })

  function PremiumAccessPage() {
    return (
      Sorry, only subscribers with the Premium Access feature can access this content.</p>
        }
      >
        <p>Congratulations! You have access to the Premium Access feature.</p>
      
    )
  }
  ```


  ```vue
  <script setup lang="ts">
  import { Show } from '@clerk/vue'
  </script>

  <template>
    
      <template #fallback>
        <p>Sorry, only subscribers with the Premium Access feature can access this content.</p>
      </template>
      <p>Congratulations! You have access to the Premium Access feature.</p>
    
  </template>
  ```


  ```vue
// Filename: pages/premium-access.vue

  <script setup lang="ts">
  // Components are automatically imported
  </script>

  <template>
    
      <template #fallback>
        <p>Sorry, only subscribers with the Premium Access feature can access this content.</p>
      </template>
      <p>Congratulations! You have access to the Premium Access feature.</p>
    
  </template>
  ```


### Render content conditionally

The following example uses ``'s `when` prop with a callback function to conditionally render its children if the user has the correct Role.


  ```tsx
// Filename: app/dashboard/settings/page.tsx

  import type { PropsWithChildren } from 'react'
  import { Show } from '@clerk/nextjs'

  export default function Page() {
    return (
       has({ role: 'org:admin' }) || has({ role: 'org:billing_manager' })}
        fallback={<p>Only an Admin or Billing Manager can access this content.</p>}
      >
        <p>The settings page.</p>
      
    )
  }
  ```


  ```tsx
// Filename: src/App.tsx

  import { Show } from '@clerk/react'

  function App() {
    return (
       has({ role: 'org:admin' }) || has({ role: 'org:billing_manager' })}
        fallback={<p>Only an Admin or Billing Manager can access this content.</p>}
      >
        <p>The settings page.</p>
      
    )
  }

  export default App
  ```


  ```astro
  ---
  import { Show } from '@clerk/astro/components'
  ---

   has({ role: 'org:admin' }) || has({ role: 'org:billing_manager' })}>
    <p slot="fallback">Only an Admin or Billing Manager can access this content.</p>
    <p>The settings page.</p>
  
  ```


  ```tsx
// Filename: app/dashboard/settings/page.tsx

  import { Show } from '@clerk/expo'
  import { Text } from 'react-native'

  export default function Page() {
    return (
       has({ role: 'org:admin' }) || has({ role: 'org:billing_manager' })}
        fallback={Only an Admin or Billing Manager can access this content.}
      >
        The settings page.
      
    )
  }
  ```


  ```jsx
// Filename: src/routes/settings.tsx

  import { Show } from '@clerk/chrome-extension'

  export default function SettingsPage() {
    return (
       has({ role: 'org:admin' }) || has({ role: 'org:billing_manager' })}
        fallback={<p>Only an Admin or Billing Manager can access this content.</p>}
      >
        <p>The settings page.</p>
      
    )
  }
  ```


  ```tsx
// Filename: app/routes/settings.tsx

  import { Show } from '@clerk/remix'

  export default function SettingsPage() {
    return (
       has({ role: 'org:admin' }) || has({ role: 'org:billing_manager' })}
        fallback={<p>Only an Admin or Billing Manager can access this content.</p>}
      >
        <p>The settings page.</p>
      
    )
  }
  ```


  ```tsx
// Filename: app/routes/settings.tsx

  import { Show } from '@clerk/react-router'

  export default function SettingsPage() {
    return (
       has({ role: 'org:admin' }) || has({ role: 'org:billing_manager' })}
        fallback={<p>Only an Admin or Billing Manager can access this content.</p>}
      >
        <p>The settings page.</p>
      
    )
  }
  ```


  ```tsx
// Filename: app/routes/settings.tsx

  import { Show } from '@clerk/tanstack-react-start'
  import { createFileRoute } from '@tanstack/react-router'

  export const Route = createFileRoute('/settings')({
    component: SettingsPage,
  })

  function SettingsPage() {
    return (
       has({ role: 'org:admin' }) || has({ role: 'org:billing_manager' })}
        fallback={<p>Only an Admin or Billing Manager can access this content.</p>}
      >
        <p>The settings page.</p>
      
    )
  }
  ```


  ```vue
  <script setup>
  import { Show } from '@clerk/vue'
  </script>

  <template>
     has({ role: 'org:admin' }) || has({ role: 'org:billing_manager' })">
      <template #fallback>
        <p>Only an Admin or Billing Manager can access this content.</p>
      </template>
      <p>The settings page.</p>
    
  </template>
  ```


  ```vue
// Filename: pages/settings.vue

  <script setup lang="ts">
  // Components are automatically imported
  </script>

  <template>
     has({ role: 'org:admin' }) || has({ role: 'org:billing_manager' })">
      <template #fallback>
        <p>Only an Admin or Billing Manager can access this content.</p>
      </template>
      <p>The settings page.</p>
    
  </template>
  ```


## Properties

- **`fallback?`** `JSX`

  Optional UI to show when a user doesn't have the correct type of access control to access the protected content.

    ---

- **`treatPendingAsSignedOut?`** `boolean`

  A boolean that indicates whether to treat [pending sessions](/reference/javascript/types/session-status#properties) as signed out. Defaults to `true`.

    ---

- **`when`** `'signed-in' | 'signed-out' | { feature: string } | { permission: string } | { plan: string } | { role: string } | (has) => boolean`

  Determines when to render the children. Can be `'signed-in'` or `'signed-out'` for authentication checks, an object with a [Feature](/guides/billing/overview), [Permission](/guides/organizations/control-access/roles-and-permissions), [Plan](/guides/billing/overview), or [Role](/guides/organizations/control-access/roles-and-permissions) for authorization checks, or a callback function for custom conditional logic.
