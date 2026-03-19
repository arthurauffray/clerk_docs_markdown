# <OrganizationProfile />` component


> Clerk's <OrganizationProfile /> component is used to render a beautiful, full-featured Organization management UI that allows users to manage their Organization profile and security settings.

The `` component allows users to manage their Organization membership, security, and billing settings.

This component's **General** tab displays the Organization's information and the **Leave organization** button. Admins will be able to see the **Update profile** button, **Verified domains** section, and **Delete organization** button.

The **Members** tab shows the Organization's members along with their join dates and Roles. Admins will have the ability to invite a member, change a member's Role, or remove them from the Organization. Admins will have tabs within the **Members** tab to view the Organization's [invitations](/guides/organizations/add-members/invitations) and [requests](/guides/organizations/add-members/verified-domains#membership-requests).

The **Billing** tab displays the Plans and Features that are available to the Organization, as well as the user's billing information, such as their invoices and payment methods.


  ## Example

  The following example includes a basic implementation of the `` component. You can use this as a starting point for your own implementation.

  
    The `` component must be embedded using the [Next.js optional catch-all route](https://nextjs.org/docs/pages/building-your-application/routing/dynamic-routes#optional-catch-all-routes) in order for the routing to work.

    ```jsx
// Filename: app/organization-profile/[[...organization-profile]]/page.tsx

    import { OrganizationProfile } from '@clerk/nextjs'

    export default function OrganizationProfilePage() {
      return }
    ```
  

  
    ```jsx
// Filename: src/App.tsx

    import { OrganizationProfile } from '@clerk/react'

    function App() {
      return }

    export default App
    ```
  

  
    ```astro
// Filename: /pages/organization-profile.astro

    ---
    import { OrganizationProfile } from '@clerk/astro/components'
    ---

    ```
  

  
    > [!NOTE]
> This component is for Expo web projects. For native iOS and Android apps, use the [native components](/reference/expo/native-components/overview) from `@clerk/expo/native` instead.


    ```jsx
// Filename: /app/organization-profile.web.tsx

    import { OrganizationProfile } from '@clerk/expo/web'

    export default function OrganizationProfilePage() {
      return }
    ```
  

  
    ```jsx
// Filename: src/routes/organization-profile.tsx

    import { OrganizationProfile } from '@clerk/chrome-extension'

    export default function OrganizationProfilePage() {
      return }
    ```
  

  
    ```tsx
// Filename: app/routes/organization-profile.tsx

    import { OrganizationProfile } from '@clerk/remix'

    export default function OrganizationProfilePage() {
      return }
    ```
  

  
    The `` component must be embedded using the [React Router Splat route](https://reactrouter.com/start/framework/routing#splats) in order for the routing to work.

    ```tsx
// Filename: app/routes/organization-profile.$.tsx

    import { OrganizationProfile } from '@clerk/react-router'

    export default function OrganizationProfilePage() {
      return }
    ```
  

  
    The `` component must be embedded using the [TanStack Router catch-all route](https://tanstack.com/router/latest/docs/framework/react/routing/routing-concepts#splat--catch-all-routes) in order for the routing to work.

    ```tsx
// Filename: app/routes/organization-profile.$.tsx

    import { OrganizationProfile } from '@clerk/tanstack-react-start'
    import { createFileRoute } from '@tanstack/react-router'

    export const Route = createFileRoute('/organization-profile/$')({
      component: OrganizationProfilePage,
    })

    function OrganizationProfilePage() {
      return }
    ```
  

  
    ```vue
// Filename: organization-profile.vue

    <script setup lang="ts">
    import { OrganizationProfile } from '@clerk/vue'
    </script>

    <template>
      </template>
    ```
  

  
    ```vue
// Filename: pages/organization-profile.vue

    <script setup lang="ts">
    // Components are automatically imported
    </script>

    <template>
      </template>
    ```
  


  ## Usage with JavaScript

  The following methods available on an instance of the [`Clerk`](/reference/javascript/clerk) class are used to render and control the `` component:

  - [`mountOrganizationProfile()`](#mount-organization-profile)
  - [`unmountOrganizationProfile()`](#unmount-organization-profile)
  - [`openOrganizationProfile()`](#open-organization-profile)
  - [`closeOrganizationProfile()`](#close-organization-profile)

  The following examples assume that you have followed the [quickstart](/js-frontend/getting-started/quickstart) in order to add Clerk to your JavaScript application.

  ### <code>mountOrganization<wbr />Profile()</code>

  Render the `` component to an HTML `<div>` element.

  ```typescript
  function mountOrganizationProfile(node: HTMLDivElement, props?: OrganizationProfileProps): void
  ```

  #### `mountOrganizationProfile()` params

  - **`node`** [`HTMLDivElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLDivElement)

  The `<div>` element used to render in the `` component

      ---

- **`props?`** [`OrganizationProfileProps`](#properties)

  The properties to pass to the `` component


  #### `mountOrganizationProfile()` usage

  ```js
// Filename: main.js

  import { Clerk } from '@clerk/clerk-js'

  // Initialize Clerk with your Clerk Publishable Key
  const clerkPubKey = import.meta.env.VITE_CLERK_PUBLISHABLE_KEY

  const clerk = new Clerk(clerkPubKey)
  await clerk.load()

  document.getElementById('app').innerHTML = `
    <div id="organization-profile"></div>
  `

  const orgProfileDiv = document.getElementById('organization-profile')

  clerk.mountOrganizationProfile(orgProfileDiv)
  ```

  ### <code>unmountOrganization<wbr />Profile()</code>

  Unmount and run cleanup on an existing `` component instance.

  ```typescript
  function unmountOrganizationProfile(node: HTMLDivElement): void
  ```

  #### `unmountOrganizationProfile()` params

  - **`node`** [`HTMLDivElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLDivElement)

  The container `<div>` element with a rendered `` component instance.


  #### `unmountOrganizationProfile()` usage

  ```js
// Filename: main.js

  import { Clerk } from '@clerk/clerk-js'

  // Initialize Clerk with your Clerk Publishable Key
  const clerkPubKey = import.meta.env.VITE_CLERK_PUBLISHABLE_KEY

  const clerk = new Clerk(clerkPubKey)
  await clerk.load()

  document.getElementById('app').innerHTML = `
    <div id="organization-profile"></div>
  `

  const orgProfileDiv = document.getElementById('organization-profile')

  clerk.mountOrganizationProfile(orgProfileDiv)

  // ...

  clerk.unmountOrganizationProfile(orgProfileDiv)
  ```

  ### `openOrganizationProfile()`

  Opens the `` component as an overlay at the root of your HTML `body` element.

  ```typescript
  function openOrganizationProfile(props?: OrganizationProfileProps): void
  ```

  #### `openOrganizationProfile()` params

  - **`props?`** [`OrganizationProfileProps`](#properties)

  The properties to pass to the `` component


  #### `openOrganizationProfile()` usage

  ```js
// Filename: main.js

  import { Clerk } from '@clerk/clerk-js'

  // Initialize Clerk with your Clerk Publishable Key
  const clerkPubKey = import.meta.env.VITE_CLERK_PUBLISHABLE_KEY

  const clerk = new Clerk(clerkPubKey)
  await clerk.load()

  document.getElementById('app').innerHTML = `
    <div id="organization-profile"></div>
  `

  const orgProfileDiv = document.getElementById('organization-profile')

  clerk.openOrganizationProfile(orgProfileDiv)
  ```

  ### `closeOrganizationProfile()`

  Closes the organization profile overlay.

  ```typescript
  function closeOrganizationProfile(): void
  ```

  #### `closeOrganizationProfile()` usage

  ```js
// Filename: main.js

  import { Clerk } from '@clerk/clerk-js'

  // Initialize Clerk with your Clerk Publishable Key
  const clerkPubKey = import.meta.env.VITE_CLERK_PUBLISHABLE_KEY

  const clerk = new Clerk(clerkPubKey)
  await clerk.load()

  document.getElementById('app').innerHTML = `
    <div id="organization-profile"></div>
  `

  const orgProfileDiv = document.getElementById('organization-profile')

  clerk.closeOrganizationProfile(orgProfileDiv)
  ```


## Properties

The `` component accepts the following properties, all of which are **optional**:

- **`appearance`** <code>[Appearance](/guides/customizing-clerk/appearance-prop/overview) | undefined</code>

  Optional object to style your components. Will only affect [Clerk components](/reference/components/overview) and not [Account Portal](/guides/account-portal/overview) pages.

    ---

- **`afterLeaveOrganizationUrl`** `string`

  The full URL or path to navigate to after leaving an Organization.

    ---

- **`customPages`** `CustomPages[]`

  An array of custom pages to add to the Organization profile. Only available for the [JavaScript SDK](/reference/javascript/overview). To add custom pages with React-based SDK's, see the [dedicated guide](/guides/customizing-clerk/adding-items/organization-profile).

    ---

- **`fallback?`** `ReactNode`

  An optional element to be rendered while the component is mounting.

    ---

- **`path`** `string`

  The path where the component is mounted on when `routing` is set to `path`. It is ignored in hash- and virtual-based routing.<br />For example: `/organization-profile`.

    ---

- **`routing`** `'hash' | 'path'`

  The [routing](/guides/how-clerk-works/routing) strategy for your pages. <br />Defaults to `'path'` for frameworks that handle routing, such as Next.js and Remix. Defaults to `hash` for all other SDK's, such as React.


## Customization

To learn about how to customize Clerk components, see the [customization documentation](/guides/customizing-clerk/appearance-prop/overview).

In addition, you also can add custom pages and links to the `` navigation sidenav. For more information, refer to the [Custom Pages](/guides/customizing-clerk/adding-items/organization-profile) documentation.
