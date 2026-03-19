# <OrganizationSwitcher />` component


> Clerk's <OrganizationSwitcher /> component is used to enable the ability to switch between available Organizations the user may be part of in your application.

The `` component allows a user to switch between their joined Organizations. If Personal Accounts are enabled, users can also switch to their Personal Account. This component is useful for applications that have a multi-tenant architecture, where users can be part of multiple Organizations. It handles all Organization-related flows, including full Organization management for admins. Learn more about [Organizations](/guides/organizations/overview).


  ## Example

  The following example includes a basic implementation of the `` component. You can use this as a starting point for your own implementation.

  
    ```jsx
// Filename: app/organization-switcher/[[...organization-switcher]]/page.tsx

    import { OrganizationSwitcher } from '@clerk/nextjs'

    export default function OrganizationSwitcherPage() {
      return }
    ```
  

  
    ```jsx
// Filename: src/App.tsx

    import { OrganizationSwitcher } from '@clerk/react'

    function App() {
      return }

    export default App
    ```
  

  
    ```astro
// Filename: /pages/organization-switcher.astro

    ---
    import { OrganizationSwitcher } from '@clerk/astro/components'
    ---

    ```
  

  
    > [!NOTE]
> This component is for Expo web projects. For native iOS and Android apps, use the [native components](/reference/expo/native-components/overview) from `@clerk/expo/native` instead.


    ```jsx
// Filename: /app/organization-switcher.web.tsx

    import { OrganizationSwitcher } from '@clerk/expo/web'

    export default function OrganizationSwitcherPage() {
      return }
    ```
  

  
    ```jsx
// Filename: src/routes/organization-switcher.tsx

    import { OrganizationSwitcher } from '@clerk/chrome-extension'

    export default function OrganizationSwitcherPage() {
      return }
    ```
  

  
    ```tsx
// Filename: app/routes/organization-switcher.tsx

    import { OrganizationSwitcher } from '@clerk/remix'

    export default function OrganizationSwitcherPage() {
      return }
    ```
  

  
    ```tsx
// Filename: app/routes/organization-switcher.tsx

    import { OrganizationSwitcher } from '@clerk/react-router'

    export default function OrganizationSwitcherPage() {
      return }
    ```
  

  
    ```tsx
// Filename: app/routes/organization-switcher.tsx

    import { OrganizationSwitcher } from '@clerk/tanstack-react-start'
    import { createFileRoute } from '@tanstack/react-router'

    export const Route = createFileRoute('/organization-switcher')({
      component: OrganizationSwitcherPage,
    })

    function OrganizationSwitcherPage() {
      return }
    ```
  

  
    ```vue
// Filename: organization-switcher.vue

    <script setup lang="ts">
    import { OrganizationSwitcher } from '@clerk/vue'
    </script>

    <template>
      </template>
    ```
  

  
    ```vue
// Filename: pages/organization-switcher.vue

    <script setup lang="ts">
    // Components are automatically imported
    </script>

    <template>
      </template>
    ```
  


  ## Usage with JavaScript

  The following methods available on an instance of the [`Clerk`](/reference/javascript/clerk) class are used to render and control the `` component:

  - [`mountOrganizationSwitcher()`](#mount-organization-switcher)
  - [`unmountOrganizationSwitcher()`](#unmount-organization-switcher)

  The following examples assume that you have followed the [quickstart](/js-frontend/getting-started/quickstart) in order to add Clerk to your JavaScript application.

  ## `mountOrganizationSwitcher()`

  Render the `` component to an HTML `<div>` element.

  ```typescript
  function mountOrganizationSwitcher(node: HTMLDivElement, props?: OrganizationSwitcherProps): void
  ```

  ### <code>mountOrganization<wbr />Switcher()</code> params

  - **`node`** [`HTMLDivElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLDivElement)

  The `<div>` element used to render in the `` component

      ---

- **`props?`** [`OrganizationSwitcherProps`](#properties)

  The properties to pass to the `` component


  ### <code>mountOrganization<wbr />Switcher()</code> usage

  ```js
// Filename: main.js

  import { Clerk } from '@clerk/clerk-js'

  // Initialize Clerk with your Clerk Publishable Key
  const clerkPubKey = import.meta.env.VITE_CLERK_PUBLISHABLE_KEY

  const clerk = new Clerk(clerkPubKey)
  await clerk.load()

  document.getElementById('app').innerHTML = `
    <div id="organization-switcher"></div>
  `

  const orgSwitcherDiv = document.getElementById('organization-switcher')

  clerk.mountOrganizationSwitcher(orgSwitcherDiv)
  ```

  ## <code>unmountOrganization<wbr />Switcher()</code>

  Unmount and run cleanup on an existing `` component instance.

  ```typescript
  function unmountOrganizationSwitcher(node: HTMLDivElement): void
  ```

  ### <code>unmountOrganization<wbr />Switcher()</code> params

  - **`node`** [`HTMLDivElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLDivElement)

  The container `<div>` element with a rendered `` component instance


  ### <code>unmountOrganization<wbr />Switcher()</code> usage

  ```js
// Filename: main.js

  import { Clerk } from '@clerk/clerk-js'

  // Initialize Clerk with your Clerk Publishable Key
  const clerkPubKey = import.meta.env.VITE_CLERK_PUBLISHABLE_KEY

  const clerk = new Clerk(clerkPubKey)
  await clerk.load()

  document.getElementById('app').innerHTML = `
    <div id="organization-switcher"></div>
  `

  const orgSwitcherDiv = document.getElementById('organization-switcher')

  clerk.mountOrganizationSwitcher(orgSwitcherDiv)

  // ...

  clerk.unmountOrganizationSwitcher(orgSwitcherDiv)
  ```


## Properties

The `` component accepts the following properties, all of which are **optional**:

- **`afterCreateOrganizationUrl`** `string`

  The full URL or path to navigate to after creating a new Organization.

    ---

- **`afterLeaveOrganizationUrl`** `string`

  The full URL or path to navigate to after the user leaves the currently Active Organization.

    ---

- **`afterSelectOrganizationUrl`** `string`

  The full URL or path to navigate to after a successful Organization switch.

    ---

- **`afterSelectPersonalUrl`** `string`

  The full URL or path to navigate to after selecting the Personal Account. Defaults to `undefined`.

    ---

- **`appearance`** <code>[Appearance](/guides/customizing-clerk/appearance-prop/overview) | undefined</code>

  Optional object to style your components. Will only affect [Clerk components](/reference/components/overview) and not [Account Portal](/guides/account-portal/overview) pages.

    ---

- **`createOrganizationMode`** `'modal' | 'navigation'`

  A boolean that controls whether clicking the "Create organization" button will cause the [``][createorg-ref] component to open as a modal, or if the browser will navigate to the `createOrganizationUrl` where `` is mounted as a page. Defaults to: `'modal'`.

    ---

- **`createOrganizationUrl`** `string`

  The full URL or path where the ``][createorg-ref] component is mounted.

    ---

- **`defaultOpen`** `boolean`

  A boolean that controls the default state of the `` component.

    ---

- **`fallback?`** `ReactNode`

  An optional element to be rendered while the component is mounting.

    ---

- **`hidePersonal`** `boolean`

  A boolean that controls whether `` will include the user's Personal Account in the Organization list. Setting this to `true` will hide the Personal Account option, and users will only be able to switch between Organizations. Defaults to `false`.

    ---

- **`organizationProfileMode`** `'modal' | 'navigation'`

  A boolean that controls whether clicking the **Manage organization** button will cause the [``][orgprofile-ref] component to open as a modal, or if the browser will navigate to the `organizationProfileUrl` where `` is mounted as a page. Defaults to: `'modal'`.

    ---

- **`organizationProfileProps`** `object`

  Specify options for the underlying [``][orgprofile-ref] component. For example: `{appearance: {...}}`

    ---

- **`organizationProfileUrl`** `string`

  The full URL or path where the [``][orgprofile-ref] component is mounted.


## Customization

To learn about how to customize Clerk components, see the [customization documentation](/guides/customizing-clerk/appearance-prop/overview).

[createorg-ref]: /docs/reference/components/organization/create-organization

[orgprofile-ref]: /docs/reference/components/organization/organization-profile
