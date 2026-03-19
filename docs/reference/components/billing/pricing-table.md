# <PricingTable />


> Clerk's <PricingTable /> component displays a table of Plans and Features that users can subscribe to.

The `` component displays a table of Plans and Features that users can subscribe to.


  ## Example

  The following example includes a basic implementation of the `` component. You can use this as a starting point for your own implementation.

  
    ```tsx
// Filename: app/pricing/page.tsx

    import { PricingTable } from '@clerk/nextjs'

    export default function Page() {
      return }
    ```
  

  
    ```tsx
// Filename: src/App.tsx

    import { PricingTable } from '@clerk/react'

    function App() {
      return }

    export default App
    ```
  

  
    ```astro
// Filename: pages/pricing.astro

    ---
    import { PricingTable } from '@clerk/astro/components'
    ---

    ```
  

  
    > [!NOTE]
> This component is for Expo web projects. For native iOS and Android apps, use the [native components](/reference/expo/native-components/overview) from `@clerk/expo/native` instead.


    ```jsx
// Filename: /app/pricing.web.tsx

    import { PricingTable } from '@clerk/expo/web'

    export default function PricingPage() {
      return }
    ```
  

  
    ```jsx
// Filename: src/routes/pricing.tsx

    import { PricingTable } from '@clerk/chrome-extension'

    export default function PricingPage() {
      return }
    ```
  

  
    ```tsx
// Filename: app/routes/pricing.tsx

    import { PricingTable } from '@clerk/react-router'

    export default function PricingPage() {
      return }
    ```
  

  
    ```tsx
// Filename: app/routes/pricing.tsx

    import { PricingTable } from '@clerk/remix'

    export default function PricingPage() {
      return }
    ```
  

  
    ```tsx
// Filename: app/routes/pricing.tsx

    import { PricingTable } from '@clerk/tanstack-react-start'
    import { createFileRoute } from '@tanstack/react-router'

    export const Route = createFileRoute('/pricing')({
      component: PricingPage,
    })

    function PricingPage() {
      return }
    ```
  

  
    ```vue
// Filename: pricing.vue

    <script setup lang="ts">
    import { PricingTable } from '@clerk/vue'
    </script>

    <template>
      </template>
    ```
  

  
    ```vue
// Filename: pages/pricing.vue

    <script setup lang="ts">
    // Components are automatically imported
    </script>

    <template>
      </template>
    ```
  


  ## Usage with JavaScript

  The following methods available on an instance of the [`Clerk`](/reference/javascript/clerk) class are used to render and control the `` component:

  - [`mountPricingTable()`](#mount-pricing-table)
  - [`unmountPricingTable()`](#unmount-pricing-table)

  The following examples assume that you followed the [quickstart](/js-frontend/getting-started/quickstart) to add Clerk to your JavaScript app.

  ### `mountPricingTable()`

  ```typescript
  function mountPricingTable(node: HTMLDivElement, props?: PricingTableProps): void
  ```

  #### `mountPricingTable()` params

  - **`node`** [`HTMLDivElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLDivElement)

  The container `<div>` element used to render in the `` component

      ---

- **`props?`** [`PricingTableProps`](#properties)

  The properties to pass to the `` component


  #### `mountPricingTable()` usage

  ```js
// Filename: main.js

  import { Clerk } from '@clerk/clerk-js'

  // Initialize Clerk with your Clerk Publishable Key
  const clerkPubKey = import.meta.env.VITE_CLERK_PUBLISHABLE_KEY

  const clerk = new Clerk(clerkPubKey)
  await clerk.load()

  document.getElementById('app').innerHTML = `
    <div id="pricing-table"></div>
  `

  const pricingTableDiv = document.getElementById('pricing-table')

  clerk.mountPricingTable(pricingTableDiv)
  ```

  ### `unmountPricingTable()`

  ```typescript
  function unmountPricingTable(node: HTMLDivElement): void
  ```

  #### `unmountPricingTable()` params

  - **`node`** [`HTMLDivElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLDivElement)

  The container `<div>` element with a rendered `` component instance


  #### `unmountPricingTable()` usage

  ```js
// Filename: main.js

  import { Clerk } from '@clerk/clerk-js'

  // Initialize Clerk with your Clerk Publishable Key
  const clerkPubKey = import.meta.env.VITE_CLERK_PUBLISHABLE_KEY

  const clerk = new Clerk(clerkPubKey)
  await clerk.load()

  document.getElementById('app').innerHTML = `
    <div id="pricing-table"></div>
  `

  const pricingTableDiv = document.getElementById('pricing-table')

  clerk.mountPricingTable(pricingTableDiv)

  // ...

  clerk.unmountPricingTable(pricingTableDiv)
  ```


## Properties

All props are optional.

- **`appearance`** <code>[Appearance](/guides/customizing-clerk/appearance-prop/overview) | undefined</code>

  Optional object to style your components. Will only affect [Clerk components](/reference/components/overview) and not [Account Portal](/guides/account-portal/overview) pages.

    ---

- **`checkoutProps`** `{ appearance: Appearance }`

  Options for the checkout drawer. Accepts the following properties:

    - [`appearance`](/guides/customizing-clerk/appearance-prop/overview): an object used to style your components. Will only affect [Clerk components](/reference/components/overview) and not [Account Portal](/guides/account-portal/overview) pages.

    ---

- **`collapseFeatures`** `boolean`

  A boolean that indicates whether the Features are collapsed. **Requires `layout` to be set to `'default'`**. Defaults to `false`.

    ---

- **`ctaPosition`** `'top' | 'bottom'`

  The placement of the CTA button. **Requires `layout` to be set to `'default'`**. Defaults to `'bottom'`.

    ---

- **`fallback`** `JSX`

  An optional UI to show when the pricing table is loading.

    ---

- **`for`** `'user' | 'organization'`

  A string that indicates whether the pricing table is for users or [Organizations](/guides/organizations/overview). If `'user'`, the pricing table will display a list of Plans and Features that **users** can subscribe to. If `'organization'`, the pricing table will display a list of Plans and Features that **Organizations** can subscribe to. Defaults to `'user'`.

    ---

- **`newSubscriptionRedirectUrl`** `string`

  The URL to navigate to after the user completes the checkout and selects the "Continue" button.
