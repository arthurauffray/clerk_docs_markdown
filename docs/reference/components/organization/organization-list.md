# <OrganizationList />` component


> Clerk's <OrganizationList /> component is used to display Organization related memberships, invitations, and suggestions for the user.

The `` component displays Organization-related memberships and automatic [invitations](/guides/organizations/add-members/verified-domains#automatic-invitations) and [suggestions](/guides/organizations/add-members/verified-domains#automatic-suggestions) for the user.


  ## Example

  The following example includes a basic implementation of the `` component. You can use this as a starting point for your own implementation.

  
    ```jsx
// Filename: app/organizations/page.tsx

    import { OrganizationList } from '@clerk/nextjs'

    export default function OrganizationListPage() {
      return (
        )
    }
    ```
  

  
    ```jsx
// Filename: src/App.tsx

    import { OrganizationList } from '@clerk/react'

    function App() {
      return }

    export default App
    ```
  

  
    ```astro
// Filename: /pages/organizations.astro

    ---
    import { OrganizationList } from '@clerk/astro/components'
    ---

    ```
  

  
    > [!NOTE]
> This component is for Expo web projects. For native iOS and Android apps, use the [native components](/reference/expo/native-components/overview) from `@clerk/expo/native` instead.


    ```jsx
// Filename: /app/organizations.web.tsx

    import { OrganizationList } from '@clerk/expo/web'

    export default function OrganizationListPage() {
      return (
         `/organization/${org.slug}`}
          afterSelectPersonalUrl={(user) => `/user/${user.id}`}
          afterSelectOrganizationUrl={(org) => `/organization/${org.slug}`}
        />
      )
    }
    ```
  

  
    ```jsx
// Filename: src/routes/organizations.tsx

    import { OrganizationList } from '@clerk/chrome-extension'

    export default function OrganizationListPage() {
      return }
    ```
  

  
    ```tsx
// Filename: app/routes/organizations.tsx

    import { OrganizationList } from '@clerk/remix'

    export default function OrganizationListPage() {
      return (
         `/organization/${org.slug}`}
          afterSelectPersonalUrl={(user) => `/user/${user.id}`}
          afterSelectOrganizationUrl={(org) => `/organization/${org.slug}`}
        />
      )
    }
    ```
  

  
    ```tsx
// Filename: app/routes/organizations.tsx

    import { OrganizationList } from '@clerk/react-router'

    export default function OrganizationListPage() {
      return (
         `/organization/${org.slug}`}
          afterSelectPersonalUrl={(user) => `/user/${user.id}`}
          afterSelectOrganizationUrl={(org) => `/organization/${org.slug}`}
        />
      )
    }
    ```
  

  
    ```tsx
// Filename: app/routes/organizations.tsx

    import { OrganizationList } from '@clerk/tanstack-react-start'
    import { createFileRoute } from '@tanstack/react-router'

    export const Route = createFileRoute('/organizations')({
      component: OrganizationListPage,
    })

    function OrganizationListPage() {
      return (
         `/organization/${org.slug}`}
          afterSelectPersonalUrl={(user) => `/user/${user.id}`}
          afterSelectOrganizationUrl={(org) => `/organization/${org.slug}`}
        />
      )
    }
    ```
  

  
    ```vue
// Filename: organizations.vue

    <script setup lang="ts">
    import { OrganizationList } from '@clerk/vue'
    </script>

    <template>
       `/organization/${org.slug}`"
        :after-select-personal-url="(org) => `/organization/${org.slug}`"
        :after-select-organization-url="(org) => `/organization/${org.slug}`"
      />
    </template>
    ```
  

  
    ```vue
// Filename: pages/organizations.vue

    <script setup lang="ts">
    // Components are automatically imported
    </script>

    <template>
       `/organization/${org.slug}`"
        :after-select-personal-url="(user) => `/user/${user.id}`"
        :after-select-organization-url="(org) => `/organization/${org.slug}`"
      />
    </template>
    ```
  


  ## Usage with JavaScript

  The following methods available on an instance of the [`Clerk`](/reference/javascript/clerk) class are used to render and control the `` component:

  - [`mountOrganizationList()`](#mount-organization-list)
  - [`unmountOrganizationList()`](#unmount-organization-list)

  The following examples assume that you have followed the [quickstart](/js-frontend/getting-started/quickstart) in order to add Clerk to your JavaScript application.

  ## `mountOrganizationList()`

  Render the `` component to an HTML `<div>` element.

  ```typescript
  function mountOrganizationList(node: HTMLDivElement, props?: OrganizationListProps): void
  ```

  ### `mountOrganizationList()` params

  - **`node`** [`HTMLDivElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLDivElement)

  The `<div>` element used to render in the `` component

      ---

- **`props?`** [`OrganizationListProps`](#properties)

  The properties to pass to the `` component


  ### `mountOrganizationList()` usage

  ```js
// Filename: main.js

  import { Clerk } from '@clerk/clerk-js'

  // Initialize Clerk with your Clerk Publishable Key
  const clerkPubKey = import.meta.env.VITE_CLERK_PUBLISHABLE_KEY

  const clerk = new Clerk(clerkPubKey)
  await clerk.load()

  document.getElementById('app').innerHTML = `
    <div id="organization-list"></div>
  `

  const orgListDiv = document.getElementById('organization-list')

  clerk.mountOrganizationList(orgListDiv)
  ```

  ## `unmountOrganizationList()`

  Unmount and run cleanup on an existing `` component instance.

  ```typescript
  function unmountOrganizationList(node: HTMLDivElement): void
  ```

  ### `unmountOrganizationList()` params

  - **`node`** [`HTMLDivElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLDivElement)

  The container `<div>` element with a rendered `` component instance


  ### `unmountOrganizationList()` usage

  ```js
// Filename: main.js

  import { Clerk } from '@clerk/clerk-js'

  // Initialize Clerk with your Clerk Publishable Key
  const clerkPubKey = import.meta.env.VITE_CLERK_PUBLISHABLE_KEY

  const clerk = new Clerk(clerkPubKey)
  await clerk.load()

  document.getElementById('app').innerHTML = `
    <div id="organization-list"></div>
  `

  const orgListDiv = document.getElementById('organization-list')

  clerk.mountOrganizationList(orgListDiv)

  // ...

  clerk.unmountOrganizationList(orgListDiv)
  ```


## Properties

The `` component accepts the following properties, all of which are **optional**:

- **`afterCreateOrganizationUrl`** <code>((org: [Organization][org-ref]) => string) | string</code>

  The full URL or path to navigate to after creating a new Organization.

    ---

- **`afterSelectOrganizationUrl`** <code>((org: [Organization][org-ref]) => string) | string</code>

  The full URL or path to navigate to after selecting an Organization. Defaults to `undefined`.

    ---

- **`afterSelectPersonalUrl`** <code>((org: [Organization][org-ref]) => string) | string</code>

  The full URL or path to navigate to after selecting the Personal Account. Defaults to `undefined`.

    ---

- **`appearance`** <code>[Appearance](/guides/customizing-clerk/appearance-prop/overview) | undefined</code>

  Optional object to style your components. Will only affect [Clerk components](/reference/components/overview) and not [Account Portal](/guides/account-portal/overview) pages.

    ---

- **`fallback?`** `ReactNode`

  An optional element to be rendered while the component is mounting.

    ---

- **`hidePersonal`** `boolean`

  A boolean that controls whether `` will include the user's Personal Account in the Organization list. Setting this to `true` will hide the Personal Account option, and users will only be able to switch between Organizations. Defaults to `false`.

    ---

- **`skipInvitationScreen`** `boolean | undefined`

  A boolean that controls whether the screen for sending invitations after an Organization is created is hidden. When `undefined`, Clerk will automatically hide the screen if the number of max allowed members is equal to 1. Defaults to `false`.


## Customization

To learn about how to customize Clerk components, see the [customization documentation](/guides/customizing-clerk/appearance-prop/overview).

[org-ref]: /docs/reference/javascript/organization
