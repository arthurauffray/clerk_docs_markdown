# <SignIn />` component


> Clerk's <SignIn /> component renders a UI for signing in users.

The `` component renders a UI to allow users to sign in or sign up by default. The functionality of the `` component is controlled by the instance settings you specify in the [Clerk Dashboard](https://dashboard.clerk.com), such as [sign-in and sign-up options](/guides/configure/auth-strategies/sign-up-sign-in-options) and [social connections](/guides/configure/auth-strategies/social-connections/overview). You can further customize your `` component by passing additional [properties](#properties) at the time of rendering. The `` component also displays any session tasks that are required for the user to complete after signing in.

> [!NOTE]
> The `` and `` components cannot render when a user is already signed in, unless the application allows multiple sessions. If a user is already signed in and the application only allows a single session, Clerk will redirect the user to the Home URL instead.


  ## Example

  The following example includes a basic implementation of the `` component. You can use this as a starting point for your own implementation.

  
  If you would like to create a dedicated `/sign-in` page in your Next.js application, see the [dedicated guide](/nextjs/guides/development/custom-sign-in-or-up-page) for more information.

  ```tsx
// Filename: app/sign-in/[[...sign-in]]/page.tsx

  import { SignIn } from '@clerk/nextjs'

  export default function SignInPage() {
    return }
  ```


  ```astro
// Filename: pages/signin.astro

  ---
  import { SignIn } from '@clerk/astro/components'
  ---

  ```


  > [!NOTE]
> This component is for Expo web projects. For native iOS and Android apps, use the [native components](/reference/expo/native-components/overview) from `@clerk/expo/native` instead.


  If you would like to create a dedicated `/sign-in` page in your Expo application, see the [dedicated guide](/guides/development/web-support/custom-sign-in-or-up-page) for more information.

  ```tsx
// Filename: /app/sign-in.web.tsx

  import { SignIn } from '@clerk/expo/web'

  export default function SignInPage() {
    return }
  ```


  ```jsx
// Filename: src/pages/sign-in.tsx

  import { SignIn } from '@clerk/react'

  export default function SignInPage() {
    return }
  ```


  If you would like to create a dedicated `/sign-in` page in your React Router application, see the [dedicated guide](/react-router/guides/development/custom-sign-in-or-up-page) for more information.

  ```tsx
// Filename: app/routes/sign-in.tsx

  import { SignIn } from '@clerk/react-router'

  export default function SignInPage() {
    return }
  ```


  ```jsx
// Filename: src/routes/sign-in.tsx

  import { SignIn } from '@clerk/chrome-extension'

  export default function SignInPage() {
    return }
  ```


  If you would like to create a dedicated `/sign-in` page in your TanStack React Start application, see the [dedicated guide](/tanstack-react-start/guides/development/custom-sign-in-or-up-page) for more information.

  ```tsx
// Filename: app/routes/sign-in.$.tsx

  import { SignIn } from '@clerk/tanstack-react-start'
  import { createFileRoute } from '@tanstack/react-router'

  export const Route = createFileRoute('/sign-in')({
    component: SignInPage,
  })

  function SignInPage() {
    return }
  ```


  ```vue
// Filename: sign-in.vue

  <script setup lang="ts">
  import { SignIn } from '@clerk/vue'
  </script>

  <template>
    </template>
  ```


  ```vue
// Filename: sign-in.vue

  <script setup lang="ts">
  // Components are automatically imported
  </script>

  <template>
    </template>
  ```


  
    If you would like to create a dedicated `/sign-in` page in your Remix application, see the [dedicated guide](/remix/guides/development/custom-sign-in-or-up-page) for more information.

    ```tsx
// Filename: app/routes/sign-in.$.tsx

    import { SignIn } from '@clerk/remix'

    export default function SignInPage() {
      return }
    ```
  


  ## Usage with JavaScript

  The following methods available on an instance of the [`Clerk`](/reference/javascript/clerk) class are used to render and control the `` component:

  - [`mountSignIn()`](#mount-sign-in)
  - [`unmountSignIn()`](#unmount-sign-in)
  - [`openSignIn()`](#open-sign-in)
  - [`closeSignIn()`](#close-sign-in)

  The following examples assume that you have followed the [quickstart](/js-frontend/getting-started/quickstart) in order to add Clerk to your JavaScript application.

  ### `mountSignIn()`

  Render the `` component to an HTML `<div>` element.

  ```typescript
  function mountSignIn(node: HTMLDivElement, props?: SignInProps): void
  ```

  #### `mountSignIn()` params

  - **`node`** [`HTMLDivElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLDivElement)

  The container `<div>` element used to render in the `` component

      ---

- **`props?`** [`SignInProps`](#properties)

  The properties to pass to the `` component


  #### `mountSignIn()` usage

  ```js
// Filename: main.js

  import { Clerk } from '@clerk/clerk-js'

  // Initialize Clerk with your Clerk Publishable Key
  const clerkPubKey = import.meta.env.VITE_CLERK_PUBLISHABLE_KEY

  const clerk = new Clerk(clerkPubKey)
  await clerk.load()

  document.getElementById('app').innerHTML = `
    <div id="sign-in"></div>
  `

  const signInDiv = document.getElementById('sign-in')

  clerk.mountSignIn(signInDiv)
  ```

  ### `unmountSignIn()`

  Unmount and run cleanup on an existing `` component instance.

  ```typescript
  function unmountSignIn(node: HTMLDivElement): void
  ```

  #### `unmountSignIn()` params

  - **`node`** [`HTMLDivElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLDivElement)

  The container `<div>` element with a rendered `` component instance


  #### `unmountSignIn()` usage

  ```js
// Filename: index.js

  import { Clerk } from '@clerk/clerk-js'

  // Initialize Clerk with your Clerk Publishable Key
  const clerkPubKey = import.meta.env.VITE_CLERK_PUBLISHABLE_KEY

  const clerk = new Clerk(clerkPubKey)
  await clerk.load()

  document.getElementById('app').innerHTML = `
    <div id="sign-in"></div>
  `

  const signInDiv = document.getElementById('sign-in')

  clerk.mountSignIn(signInDiv)

  // ...

  clerk.unmountSignIn(signInDiv)
  ```

  ### `openSignIn()`

  Opens the `` component as an overlay at the root of your HTML `body` element.

  ```typescript
  function openSignIn(props?: SignInProps): void
  ```

  #### `openSignIn()` params

  - **`props?`** [`SignInProps`](#properties)

  The properties to pass to the `` component.


  #### `openSignIn()` usage

  ```js
// Filename: main.js

  import { Clerk } from '@clerk/clerk-js'

  // Initialize Clerk with your Clerk Publishable Key
  const clerkPubKey = import.meta.env.VITE_CLERK_PUBLISHABLE_KEY

  const clerk = new Clerk(clerkPubKey)
  await clerk.load()

  clerk.openSignIn()
  ```

  ### `closeSignIn()`

  Closes the sign in overlay.

  ```typescript
  function closeSignIn(): void
  ```

  #### `closeSignIn()` usage

  ```js
// Filename: index.js

  import { Clerk } from '@clerk/clerk-js'

  // Initialize Clerk with your Clerk Publishable Key
  const clerkPubKey = import.meta.env.VITE_CLERK_PUBLISHABLE_KEY

  const clerk = new Clerk(clerkPubKey)
  await clerk.load()

  clerk.openSignIn()

  // ...

  clerk.closeSignIn()
  ```


## Properties

All props are optional.

- **`appearance`** <code>[Appearance](/guides/customizing-clerk/appearance-prop/overview) | undefined</code>

  Optional object to style your components. Will only affect [Clerk components](/reference/components/overview) and not [Account Portal](/guides/account-portal/overview) pages.

    ---

- **`fallback`** `ReactNode`

  An optional element to be rendered while the component is mounting.

    ---

- **`fallbackRedirectUrl`** `string`

  The fallback URL to redirect to after the user signs in, if there's no `redirect_url` in the path already. Defaults to `/`. It's recommended to use [the environment variable](/guides/development/clerk-environment-variables#sign-in-and-sign-up-redirects) instead.

    ---

- **`forceRedirectUrl`** `string`

  If provided, this URL will always be redirected to after the user signs in. It's recommended to use [the environment variable](/guides/development/clerk-environment-variables#sign-in-and-sign-up-redirects) instead.

    ---

- **`initialValues`** [`SignInInitialValues`](/reference/javascript/types/sign-in-initial-values)

  The values used to prefill the sign-in fields with.

    ---

- **`oauthFlow`** `"redirect" | "popup" | "auto"`

  Determines how OAuth authentication is performed. Accepts the following properties:

- **`"redirect"`: Redirect to the OAuth provider on the current page.** `"popup"`: Open a popup window. `"auto"`: Choose the best method based on whether the current domain typically requires the `"popup"` flow to correctly perform authentication.

  Defaults to `"auto"`.

    ---

- **`path`** `string`

  The path where the component is mounted on when `routing` is set to `path`. It is ignored in hash-based routing. For example: `/sign-in`.

    ---

- **`routing`** `'hash' | 'path'`

  The [routing](/guides/how-clerk-works/routing) strategy for your pages. Defaults to `'path'` for frameworks that handle routing, such as Next.js and Remix. Defaults to `hash` for all other SDK's, such as React.

    ---

- **`signUpFallbackRedirectUrl`** `string`

  The fallback URL to redirect to after the user signs up, if there's no `redirect_url` in the path already. Used for the 'Don't have an account? Sign up' link that's rendered. Defaults to `/`. It's recommended to use [the environment variable](/guides/development/clerk-environment-variables#sign-in-and-sign-up-redirects) instead.

    ---

- **`signUpForceRedirectUrl`** `string`

  If provided, this URL will always used as the redirect destination after the user signs up. Used for the 'Don't have an account? Sign up' link that's rendered. It's recommended to use [the environment variable](/guides/development/clerk-environment-variables#sign-in-and-sign-up-redirects) instead.

    ---

- **`signUpUrl`** `string`

  The full URL or path to the sign-up page. Used for the 'Don't have an account? Sign up' link that's rendered. It's recommended to use [the environment variable](/guides/development/clerk-environment-variables#sign-in-and-sign-up-redirects) instead.

    ---

- **`transferable`** `boolean`

  Indicates whether or not sign in attempts are transferable to the sign up flow. Defaults to `true`. When set to `false`, prevents opaque sign ups when a user attempts to sign in via OAuth with an email that doesn't exist.

    ---

- **`waitlistUrl`** `string`

  Full URL or path to the waitlist page. Use this property to provide the target of the 'Waitlist' link that's rendered. If `undefined`, will redirect to the [Account Portal waitlist page](/guides/account-portal/overview#waitlist). If you've passed the `waitlistUrl` prop to the [``](/reference/components/clerk-provider) component, it will infer from that, and you can omit this prop.

    ---

- **`withSignUp`** `boolean`

  Opt into sign-in-or-up flow by setting this prop to `true`. When `true`, if a user does not exist, they will be prompted to sign up. If a user exists, they will be prompted to sign in. Defaults to `true` if the `CLERK_SIGN_IN_URL` environment variable is set. Otherwise, defaults to `false`.


## Customization

To learn about how to customize Clerk components, see the [customization documentation](/guides/customizing-clerk/appearance-prop/overview).

If Clerk's prebuilt components don't meet your specific needs or if you require more control over the logic, you can rebuild the existing Clerk flows using the Clerk API. For more information, see the [custom flow guides](/guides/development/custom-flows/overview).
