# <Waitlist />` component


> The <Waitlist /> component renders a waitlist form that allows users to join for early access to your application.

In **Waitlist** mode, users can register their interest in your app by joining a waitlist. This mode is ideal for apps in early development stages or those wanting to generate interest before launch. [Learn more about additional features available in **Waitlist** mode](/guides/secure/restricting-access#waitlist).

The `` component renders a form that allows users to join for early access to your app.


  > [!NOTE]
  > If you're using Next.js, the`` component is available in `@clerk/nextjs@6.2.0` and above.


## Enable Waitlist mode

Before using the `` component, you must enable **Waitlist** mode in the Clerk Dashboard:

1. In the Clerk Dashboard, navigate to the [**Waitlist**](https://dashboard.clerk.com/~/user-authentication/waitlist) page.
1. Toggle on **Enable waitlist** and select **Save**.


  ## Example

  > [!WARNING]
  > Before using the `` component, you must provide the `waitlistUrl` prop either in the [``](/reference/components/clerk-provider#properties) or [``](/reference/components/authentication/sign-in#properties) component to ensure proper functionality.

  The following example includes a basic implementation of the `` component. You can use this as a starting point for your own implementation.

  
  ```tsx
// Filename: app/waitlist/[[...waitlist]]/page.tsx

  import { Waitlist } from '@clerk/nextjs'

  export default function WaitlistPage() {
    return }
  ```


  ```tsx
// Filename: src/pages/waitlist.tsx

  import { Waitlist } from '@clerk/react'

  export default function WaitlistPage() {
    return }
  ```


  ```astro
// Filename: pages/waitlist.astro

  ---
  import { Waitlist as WaitlistAstro } from '@clerk/astro/components'
  ---

  ```


  > [!NOTE]
> This component is for Expo web projects. For native iOS and Android apps, use the [native components](/reference/expo/native-components/overview) from `@clerk/expo/native` instead.


  ```jsx
// Filename: /app/waitlist.web.tsx

  import { Waitlist } from '@clerk/expo/web'

  export default function WaitlistPage() {
    return }
  ```


  ```jsx
// Filename: src/routes/waitlist.tsx

  import { Waitlist } from '@clerk/chrome-extension'

  export default function WaitlistPage() {
    return }
  ```


  ```tsx
// Filename: app/routes/waitlist.tsx

  import { Waitlist } from '@clerk/react-router'

  export default function WaitlistPage() {
    return }
  ```


  ```tsx
// Filename: app/routes/waitlist.tsx

  import { Waitlist } from '@clerk/remix'

  export default function WaitlistPage() {
    return }
  ```


  ```tsx
// Filename: app/routes/waitlist.tsx

  import { Waitlist } from '@clerk/tanstack-react-start'
  import { createFileRoute } from '@tanstack/react-router'

  export const Route = createFileRoute('/waitlist')({
    component: WaitlistPage,
  })

  function WaitlistPage() {
    return }
  ```


  ```vue
// Filename: waitlist.vue

  <script setup>
  // Components are automatically imported
  </script>

  <template>
    </template>
  ```


  ```vue
// Filename: waitlist.vue

  <script setup lang="ts">
  import { Waitlist } from '@clerk/vue'
  </script>

  <template>
    </template>
  ```


  ## Usage with JavaScript

  The following methods available on an instance of the [`Clerk`](/reference/javascript/clerk) class are used to render and control the `` component:

  - [`mountWaitlist()`](#mount-waitlist)
  - [`unmountWaitlist()`](#unmount-waitlist)
  - [`openWaitlist()`](#open-waitlist)
  - [`closeWaitlist()`](#close-waitlist)

  The following examples assume that you followed the [quickstart](/js-frontend/getting-started/quickstart) to add Clerk to your JavaScript app.

  ### <code>mount<wbr />Waitlist()</code>

  Render the `` component to an HTML `<div>` element.

  ```typescript
  function mountWaitlist(node: HTMLDivElement, props?: WaitlistProps): void
  ```

  ### <code>mount<wbr />Waitlist()</code> params

  - **`node`** [`HTMLDivElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLDivElement)

  The `<div>` element used to render in the `` component

      ---

- **`props?`** [`WaitlistProps`](#properties)

  The properties to pass to the `` component


  #### `mountWaitlist()` usage

  ```js
// Filename: main.js

  import { Clerk } from '@clerk/clerk-js'

  // Initialize Clerk with your Clerk Publishable Key
  const clerk = new Clerk('{{pub_key}}')
  await clerk.load()

  document.getElementById('app').innerHTML = `
    <div id="waitlist"></div>
  `

  const waitlistDiv = document.getElementById('waitlist')

  clerk.mountWaitlist(waitlistDiv)
  ```

  ### <code>unmount<wbr />Waitlist()</code>

  Unmount and run cleanup on an existing `` component instance.

  ```typescript
  function unmountWaitlist(node: HTMLDivElement): void
  ```

  #### `unmountWaitlist()` params

  - **`node`** [`HTMLDivElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLDivElement)

  The container `<div>` element with a rendered `` component instance


  #### `unmountWaitlist()` usage

  ```js
// Filename: main.js

  import { Clerk } from '@clerk/clerk-js'

  // Initialize Clerk with your Clerk Publishable Key
  const clerk = new Clerk('{{pub_key}}')
  await clerk.load()

  document.getElementById('app').innerHTML = `
    <div id="waitlist"></div>
  `

  const waitlistDiv = document.getElementById('waitlist')

  clerk.mountWaitlist(waitlistDiv)

  // ...

  clerk.unmountWaitlist(waitlistDiv)
  ```

  ### `openWaitlist()`

  Opens the `` component as an overlay at the root of your HTML `body` element.

  ```typescript
  function openWaitlist(props?: WaitlistProps): void
  ```

  #### `openWaitlist()` params

  - **`props?`** [`WaitlistProps`](#properties)

  The properties to pass to the `` component


  #### `openWaitlist()` usage

  ```js
// Filename: main.js

  import { Clerk } from '@clerk/clerk-js'

  // Initialize Clerk with your Clerk Publishable Key
  const clerk = new Clerk('{{pub_key}}')
  await clerk.load()

  document.getElementById('app').innerHTML = `
    <div id="waitlist"></div>
  `

  const waitlistDiv = document.getElementById('waitlist')

  clerk.openWaitlist(waitlistDiv)
  ```

  ### `closeWaitlist()`

  Closes the waitlist overlay.

  ```typescript
  function closeWaitlist(): void
  ```

  #### `closeWaitlist()` usage

  ```js
// Filename: main.js

  import { Clerk } from '@clerk/clerk-js'

  // Initialize Clerk with your Clerk Publishable Key
  const clerk = new Clerk('{{pub_key}}')
  await clerk.load()

  document.getElementById('app').innerHTML = `
    <div id="waitlist"></div>
  `

  const waitlistDiv = document.getElementById('waitlist')

  clerk.openWaitlist(waitlistDiv)

  // ...

  clerk.closeWaitlist(waitlistDiv)
  ```


## Properties

All props are optional.

- **`afterJoinWaitlistUrl`** `string`

  The full URL or path to navigate to after joining the waitlist.

    ---

- **`appearance`** <code>[Appearance](/guides/customizing-clerk/appearance-prop/overview) | undefined</code>

  Optional object to style your components. Will only affect [Clerk components](/reference/components/overview) and not [Account Portal](/guides/account-portal/overview) pages.

    ---

- **`fallback?`** `ReactNode`

  An optional element to be rendered while the component is mounting.

    ---

- **`signInUrl`** `string`

  The full URL or path to the sign in page. Used for the 'Already have an account? Sign in' link that's rendered. It's recommended to use [the environment variable](/guides/development/clerk-environment-variables#sign-in-and-sign-up-redirects) instead.


## Customization

To learn about how to customize Clerk components, see the [customization guide](/guides/customizing-clerk/appearance-prop/overview).
