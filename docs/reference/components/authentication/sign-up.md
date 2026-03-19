# <SignUp />` component


> Clerk's <SignUp /> component renders a UI for signing up users.

The `` component renders a UI for signing up users. The functionality of the `` component is controlled by the instance settings you specify in the [Clerk Dashboard](https://dashboard.clerk.com), such as [sign-in and sign-up options](/guides/configure/auth-strategies/sign-up-sign-in-options) and [social connections](/guides/configure/auth-strategies/social-connections/overview). You can further customize your `` component by passing additional [properties](#properties) at the time of rendering. The `` component also displays any session tasks that are required for the user to complete after signing up.

> [!NOTE]
> The `` and `` components cannot render when a user is already signed in, unless the application allows multiple sessions. If a user is already signed in and the application only allows a single session, Clerk will redirect the user to the Home URL instead.


  ## Example

  The following example includes a basic implementation of the `` component. You can use this as a starting point for your own implementation.

  
    If you would like to create a dedicated `/sign-up` page in your Next.js application, see the [dedicated guide](/nextjs/guides/development/custom-sign-up-page) for more information.

    ```tsx
// Filename: app/sign-up/[[...sign-up]]/page.tsx

    import { SignUp } from '@clerk/nextjs'

    export default function SignUpPage() {
      return }
    ```
  

  
    ```astro
// Filename: pages/signup.astro

    ---
    import { SignUp } from '@clerk/astro/components'
    ---

    ```
  

  
    > [!NOTE]
> This component is for Expo web projects. For native iOS and Android apps, use the [native components](/reference/expo/native-components/overview) from `@clerk/expo/native` instead.


    ```jsx
// Filename: /app/sign-up.web.tsx

    import { SignUp } from '@clerk/expo/web'

    export default function SignUpPage() {
      return }
    ```
  

  
    ```jsx
// Filename: src/pages/sign-up.tsx

    import { SignUp } from '@clerk/react'

    export default function SignUpPage() {
      return }
    ```
  

  
    If you would like to create a dedicated `/sign-up` page in your React Router application, see the [dedicated guide](/react-router/guides/development/custom-sign-up-page) for more information.

    ```tsx
// Filename: app/routes/sign-up.tsx

    import { SignUp } from '@clerk/react-router'

    export default function SignUpPage() {
      return }
    ```
  

  
    ```jsx
// Filename: src/routes/sign-up.tsx

    import { SignUp } from '@clerk/chrome-extension'

    export default function SignUpPage() {
      return }
    ```
  

  
    If you would like to create a dedicated `/sign-up` page in your Remix application, see the [dedicated guide](/remix/guides/development/custom-sign-up-page) for more information.

    ```tsx
// Filename: app/routes/sign-up.$.tsx

    import { SignUp } from '@clerk/remix'

    export default function SignUpPage() {
      return }
    ```
  

  
    If you would like to create a dedicated `/sign-up` page in your TanStack React Start application, see the [dedicated guide](/tanstack-react-start/guides/development/custom-sign-up-page) for more information.

    ```tsx
// Filename: app/routes/sign-up.$.tsx

    import { SignUp } from '@clerk/tanstack-react-start'
    import { createFileRoute } from '@tanstack/react-router'

    export const Route = createFileRoute('/sign-up')({
      component: SignUpPage,
    })

    function SignUpPage() {
      return }
    ```
  

  
    ```vue
// Filename: sign-up.vue

    <script setup lang="ts">
    import { SignUp } from '@clerk/vue'
    </script>

    <template>
      </template>
    ```
  

  
    ```vue
// Filename: sign-up.vue

    <script setup lang="ts">
    // Components are automatically imported
    </script>

    <template>
      </template>
    ```
  


  ## Usage with JavaScript

  The following methods available on an instance of the [`Clerk`](/reference/javascript/clerk) class are used to render and control the `` component:

  - [`mountSignUp()`](#mount-sign-up)
  - [`unmountSignUp()`](#unmount-sign-up)
  - [`openSignUp()`](#open-sign-up)
  - [`closeSignUp()`](#close-sign-up)

  The following examples assume that you have followed the [quickstart](/js-frontend/getting-started/quickstart) in order to add Clerk to your JavaScript application.

  ### `mountSignUp()`

  Render the `` component to an HTML `<div>` element.

  ```typescript
  function mountSignUp(node: HTMLDivElement, props?: SignUpProps): void
  ```

  #### `mountSignUp()` params

  - **`node `** [`HTMLDivElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLDivElement)

  The `<div>` element used to render in the `` component

      ---

- **`props?`** [`SignUpProps`](#properties)

  The properties to pass to the `` component.


  #### `mountSignUp()` usage

  ```typescript
// Filename: main.ts

  import { Clerk } from '@clerk/clerk-js'

  // Initialize Clerk with your Clerk Publishable Key
  const clerkPubKey = import.meta.env.VITE_CLERK_PUBLISHABLE_KEY

  const clerk = new Clerk(clerkPubKey)
  await clerk.load()

  document.getElementById('app').innerHTML = `
    <div id="sign-up"></div>
  `

  const signUpDiv = document.getElementById('sign-up')

  clerk.mountSignUp(signUpDiv)
  ```

  ### `unmountSignUp()`

  Unmount and run cleanup on an existing `` component instance.

  ```typescript
  function unmountSignUp(node: HTMLDivElement): void
  ```

  #### `unmountSignUp()` params

  - **`node `** [`HTMLDivElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLDivElement)

  The container `<div>` element with a rendered `` component instance


  #### `unmountSignUp()` usage

  ```typescript
// Filename: main.ts

  import { Clerk } from '@clerk/clerk-js'

  // Initialize Clerk with your Clerk Publishable Key
  const clerkPubKey = import.meta.env.VITE_CLERK_PUBLISHABLE_KEY

  const clerk = new Clerk(clerkPubKey)
  await clerk.load()

  document.getElementById('app').innerHTML = `
    <div id="sign-up"></div>
  `

  const signUpDiv = document.getElementById('sign-up')

  clerk.mountSignUp(signUpDiv)

  // ...

  clerk.unmountSignUp(signUpDiv)
  ```

  ### `openSignUp()`

  Opens the `` component as an overlay at the root of your HTML `body` element.

  ```typescript
  function openSignUp(props?: SignUpProps): void
  ```

  #### `openSignUp()` params

  - **`props?`** [`SignUpProps`](#properties)

  The properties to pass to the `` component


  #### `openSignUp()` usage

  ```js
// Filename: main.js

  import { Clerk } from '@clerk/clerk-js'

  // Initialize Clerk with your Clerk Publishable Key
  const clerkPubKey = import.meta.env.VITE_CLERK_PUBLISHABLE_KEY

  const clerk = new Clerk(clerkPubKey)
  await clerk.load()

  clerk.openSignUp()
  ```

  ### `closeSignUp()`

  Closes the sign up overlay.

  ```typescript
  function closeSignUp(): void
  ```

  #### `closeSignUp()` usage

  ```js
// Filename: main.js

  import { Clerk } from '@clerk/clerk-js'

  // Initialize Clerk with your Clerk Publishable Key
  const clerkPubKey = import.meta.env.VITE_CLERK_PUBLISHABLE_KEY

  const clerk = new Clerk(clerkPubKey)
  await clerk.load()

  clerk.openSignUp()

  // ...

  clerk.closeSignUp()
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

  The fallback URL to redirect to after the user signs up, if there's no `redirect_url` in the path already. Defaults to `/`. It's recommended to use [the environment variable](/guides/development/clerk-environment-variables#sign-in-and-sign-up-redirects) instead.

    ---

- **`forceRedirectUrl`** `string`

  If provided, this URL will always be used as the redirect destination after the user signs up. It's recommended to use [the environment variable](/guides/development/clerk-environment-variables#sign-in-and-sign-up-redirects) instead.

    ---

- **`initialValues`** [`SignUpInitialValues`](/reference/javascript/types/sign-up-initial-values)

  The values used to prefill the sign-up fields with.

    ---

- **`oauthFlow`** `"redirect" | "popup" | "auto"`

  Determines how OAuth authentication is performed. Accepts the following properties:

- **`"redirect"`: Redirect to the OAuth provider on the current page.** `"popup"`: Open a popup window. `"auto"`: Choose the best method based on whether the current domain typically requires the `"popup"` flow to correctly perform authentication.

  Defaults to `"auto"`.

    ---

- **`path`** `string`

  The path where the component is mounted on when `routing` is set to `path`. It is ignored in hash-based routing. For example: `/sign-up`.

    ---

- **`routing`** `'hash' | 'path'`

  The [routing](/guides/how-clerk-works/routing) strategy for your pages.  Defaults to `'path'` for frameworks that handle routing, such as Next.js and Remix. Defaults to `hash` for all other SDK's, such as React.

    ---

- **`signInFallbackRedirectUrl`** `string`

  The fallback URL to redirect to after the user signs in, if there's no `redirect_url` in the path already. Used for the 'Already have an account? Sign in' link that's rendered.  Defaults to `/`. It's recommended to use [the environment variable](/guides/development/clerk-environment-variables#sign-in-and-sign-up-redirects) instead.

    ---

- **`signInForceRedirectUrl?`** `string`

  If provided, this URL will always be redirected to after the user signs in. Used for the 'Already have an account? Sign in' link that's rendered. It's recommended to use [the environment variable](/guides/development/clerk-environment-variables#sign-in-and-sign-up-redirects) instead.

    ---

- **`signInUrl`** `string`

  The full URL or path to the sign-in page. Used for the 'Already have an account? Sign in' link that's rendered. It's recommended to use [the environment variable](/guides/development/clerk-environment-variables#sign-in-and-sign-up-redirects) instead.

    ---

- **`unsafeMetadata`** [`SignUpUnsafeMetadata`](/reference/javascript/types/metadata#sign-up-unsafe-metadata)

  Metadata that can be read and set from the frontend and the backend. Once the sign-up is complete, the value of this field will be automatically copied to the created user's unsafe metadata (`User.unsafeMetadata`). One common use case is to collect custom information about the user during the sign-up process and store it in this property. Read more about [unsafe metadata](/guides/users/extending#unsafe-metadata).


## Customization

To learn about how to customize Clerk components, see the [customization documentation](/guides/customizing-clerk/appearance-prop/overview).

If Clerk's prebuilt components don't meet your specific needs or if you require more control over the logic, you can rebuild the existing Clerk flows using the Clerk API. For more information, see the [custom flow guides](/guides/development/custom-flows/overview).
