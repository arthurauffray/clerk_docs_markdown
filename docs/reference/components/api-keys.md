# <APIKeys />` component


> Clerk's <APIKeys /> component renders a UI to manage API keys.

> [!WARNING]
> API keys is currently in beta. The API may change before general availability.


The `` component is used to manage API keys for your application. It allows you to create, edit, and revoke API keys for your application.

The component manages API keys based on the user's current context. When the user has an Active Organization selected, all operations are scoped to that Organization. Otherwise, operations are user-scoped.

To utilize the `` component, you must first enable API keys in the Clerk Dashboard. Refer to the [Using API keys](/guides/development/machine-auth/api-keys) guide for more information.


  ## Example

  The following example includes a basic implementation of the `` component. You can use this as a starting point for your own implementation.

  
    ```tsx
// Filename: app/api-keys/page.tsx

    import { APIKeys } from '@clerk/nextjs'

    export default function Page() {
      return }
    ```
  

  
    ```astro
// Filename: pages/api-keys.astro

    ---
    import { APIKeys } from '@clerk/astro/components'
    ---

    ```
  

  
    ```tsx
// Filename: src/api-keys.tsx

    import { APIKeys } from '@clerk/react'

    export default function Page() {
      return }
    ```
  

  
    ```tsx
// Filename: app/routes/api-keys.tsx

    import { APIKeys } from '@clerk/react-router'

    export default function Page() {
      return }
    ```
  

  
    ```jsx
// Filename: src/routes/api-keys.tsx

    import { APIKeys } from '@clerk/chrome-extension'

    export default function Page() {
      return }
    ```
  

  
    ```tsx
// Filename: src/routes/api-keys.tsx

    import { APIKeys } from '@clerk/tanstack-react-start'
    import { createFileRoute } from '@tanstack/react-router'

    export const Route = createFileRoute('/api-keys')({
      component: Page,
    })

    function Page() {
      return }
    ```
  

  
    ```vue
// Filename: api-keys.vue

    <script setup lang="ts">
    import { APIKeys } from '@clerk/vue'
    </script>

    <template>
      </template>
    ```
  

  
    ```vue
// Filename: api-keys.vue

    <script setup lang="ts">
    // Components are automatically imported
    </script>

    <template>
      </template>
    ```
  


  ## Usage with JavaScript

  The following methods available on an instance of the [`Clerk`](/reference/javascript/clerk) class are used to render and control the `` component:

  - [`mountAPIKeys()`](#mount-api-keys)
  - [`unmountAPIKeys()`](#unmount-api-keys)

  The following examples assume that you have followed the [quickstart](/js-frontend/getting-started/quickstart) in order to add Clerk to your JavaScript application.

  ### `mountAPIKeys()`

  Render the `` component to an HTML `<div>` element.

  ```typescript
  function mountAPIKeys(node: HTMLDivElement, props?: APIKeysProps): void
  ```

  #### `mountAPIKeys()` params

  - **`node`** [`HTMLDivElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLDivElement)

  The container `<div>` element used to render in the `` component

      ---

- **`props?`** [`APIKeysProps`](#properties)

  The properties to pass to the `` component


  #### `mountAPIKeys()` usage

  ```js
// Filename: main.js

  import { Clerk } from '@clerk/clerk-js'

  // Initialize Clerk with your Clerk Publishable Key
  const clerkPubKey = import.meta.env.VITE_CLERK_PUBLISHABLE_KEY

  const clerk = new Clerk(clerkPubKey)
  await clerk.load()

  document.getElementById('app').innerHTML = `
    <div id="api-keys"></div>
  `

  const apiKeysDiv = document.getElementById('api-keys')

  clerk.mountAPIKeys(apiKeysDiv, {
    perPage: 10,
    showDescription: true,
  })
  ```

  ### `unmountAPIKeys()`

  Unmount and run cleanup on an existing `` component instance.

  ```typescript
  function unmountAPIKeys(node: HTMLDivElement): void
  ```

  #### `unmountAPIKeys()` params

  - **`node`** [`HTMLDivElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLDivElement)

  The container `<div>` element with a rendered `` component instance


  #### `unmountAPIKeys()` usage

  ```js
// Filename: main.js

  import { Clerk } from '@clerk/clerk-js'

  // Initialize Clerk with your Clerk Publishable Key
  const clerkPubKey = import.meta.env.VITE_CLERK_PUBLISHABLE_KEY

  const clerk = new Clerk(clerkPubKey)
  await clerk.load()

  document.getElementById('app').innerHTML = `
    <div id="api-keys"></div>
  `

  const apiKeysDiv = document.getElementById('api-keys')

  clerk.mountAPIKeys(apiKeysDiv)

  // ...

  clerk.unmountAPIKeys(apiKeysDiv)
  ```


## Properties

All props are optional.

- **`perPage?`** `number`

  The number of API keys to show per page. Defaults to `10`.

    ---

- **`showDescription?`** `boolean`

  Whether to show the description field in the API key creation form. Defaults to `false`.

    ---

- **`appearance?`** <code>[Appearance](/guides/customizing-clerk/appearance-prop/overview) | undefined</code>

  Optional object to style your components. Will only affect [Clerk components](/reference/components/overview) and not [Account Portal](/guides/account-portal/overview) pages.

    ---

- **`fallback?`** `ReactNode`

  An optional element to be rendered while the component is mounting.


## Customization

To learn about how to customize Clerk components, see the [customization documentation](/guides/customizing-clerk/appearance-prop/overview).

If Clerk's prebuilt components don't meet your specific needs or if you require more control over the logic, you can rebuild the existing Clerk flows using the Clerk API. For more information, see the [custom flow guides](/guides/development/custom-flows/overview).
