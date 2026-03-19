# <UserProfile />` component


> Clerk's <UserProfile /> component is used to render a beautiful, full-featured account management UI that allows users to manage their profile and security settings.

The `` component is used to render a beautiful, full-featured account management UI that allows users to manage their profile, security, and billing settings.


  ## Example

  The following example includes a basic implementation of the `` component. You can use this as a starting point for your own implementation.

  
    The `` component must be embedded using the [Next.js optional catch-all route](https://nextjs.org/docs/pages/building-your-application/routing/dynamic-routes#optional-catch-all-routes) in order for the routing to work.

    ```jsx
// Filename: app/user-profile/[[...user-profile]]/page.tsx

    import { UserProfile } from '@clerk/nextjs'

    const UserProfilePage = () => export default UserProfilePage
    ```
  

  
    ```jsx
// Filename: src/App.tsx

    import { UserProfile } from '@clerk/react'

    function App() {
      return }

    export default App
    ```
  

  
    ```astro
// Filename: pages/user.astro

    ---
    import { UserProfile } from '@clerk/astro/components'
    ---

    ```
  

  
    > [!NOTE]
> This component is for Expo web projects. For native iOS and Android apps, use the [native components](/reference/expo/native-components/overview) from `@clerk/expo/native` instead.


    ```jsx
// Filename: /app/user-profile.web.tsx

    import { UserProfile } from '@clerk/expo/web'

    export default function UserProfilePage() {
      return }
    ```
  

  
    ```jsx
// Filename: src/routes/user-profile.tsx

    import { UserProfile } from '@clerk/chrome-extension'

    export default function UserProfilePage() {
      return }
    ```
  

  
    The `` component must be embedded using the [Remix optional route](https://reactrouter.com/en/main/route/route#optional-segments) in order for the routing to work.

    ```tsx
// Filename: app/routes/user.$.tsx

    import { UserProfile } from '@clerk/remix'

    export default function UserProfilePage() {
      return }
    ```
  

  
    The `` component must be embedded using the [React Router Splat route](https://reactrouter.com/start/framework/routing#splats) in order for the routing to work.

    ```tsx
// Filename: app/routes/user-profile.$.tsx

    import { UserProfile } from '@clerk/react-router'

    export default function UserProfilePage() {
      return }
    ```
  

  
    The `` component must be embedded using the [TanStack Router catch-all route](https://tanstack.com/router/latest/docs/framework/react/routing/routing-concepts#splat--catch-all-routes) in order for the routing to work.

    ```tsx
// Filename: app/routes/user-profile.$.tsx

    import { UserProfile } from '@clerk/tanstack-react-start'
    import { createFileRoute } from '@tanstack/react-router'

    export const Route = createFileRoute('/user-profile/$')({
      component: UserProfilePage,
    })

    function UserProfilePage() {
      return }
    ```
  

  
    ```vue
// Filename: pages/user-profile/[...user-profile].vue

    <script setup>
    // Components are automatically imported
    </script>

    <template>
      </template>
    ```
  

  
    ```vue
// Filename: user.vue

    <script setup>
    import { UserProfile } from '@clerk/vue'
    </script>

    <template>
      </template>
    ```
  


  ## Usage with JavaScript

  The following methods available on an instance of the [`Clerk`](/reference/javascript/clerk) class are used to render and control the `` component:

  - [`mountUserProfile()`](#mount-user-profile)
  - [`unmountUserProfile()`](#unmount-user-profile)
  - [`openUserProfile()`](#open-user-profile)
  - [`closeUserProfile()`](#close-user-profile)

  The following examples assume that you have followed the [quickstart](/js-frontend/getting-started/quickstart) in order to add Clerk to your JavaScript application.

  ### `mountUserProfile()`

  Render the `` component to an HTML `<div>` element.

  ```typescript
  function mountUserProfile(node: HTMLDivElement, props?: UserProfileProps): void
  ```

  #### `mountUserProfile()` params

  - **`node`** [`HTMLDivElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLDivElement)

  The `<div>` element used to render in the `` component

      ---

- **`props?`** [`UserProfileProps`](#properties)

  The properties to pass to the `` component


  #### `mountUserProfile()` usage

  ```js
// Filename: main.js

  import { Clerk } from '@clerk/clerk-js'

  // Initialize Clerk with your Clerk Publishable Key
  const clerkPubKey = import.meta.env.VITE_CLERK_PUBLISHABLE_KEY

  const clerk = new Clerk(clerkPubKey)
  await clerk.load()

  document.getElementById('app').innerHTML = `
    <div id="user-profile"></div>
  `

  const userProfileDiv = document.getElementById('user-profile')

  clerk.mountUserProfile(userProfileDiv)
  ```

  ### `unmountUserProfile()`

  Unmount and run cleanup on an existing `` component instance.

  ```typescript
  function unmountUserProfile(node: HTMLDivElement): void
  ```

  #### `unmountUserProfile()` params

  - **`node`** [`HTMLDivElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLDivElement)

  The container `<div>` element with a rendered `` component instance.


  #### `unmountUserProfile()` usage

  ```js
// Filename: main.js

  import { Clerk } from '@clerk/clerk-js'

  // Initialize Clerk with your Clerk Publishable Key
  const clerkPubKey = import.meta.env.VITE_CLERK_PUBLISHABLE_KEY

  const clerk = new Clerk(clerkPubKey)
  await clerk.load()

  document.getElementById('app').innerHTML = `
    <div id="user-profile"></div>
  `

  const userProfileDiv = document.getElementById('user-profile')

  clerk.mountUserProfile(userProfileDiv)

  // ...

  clerk.unmountUserProfile(userProfileDiv)
  ```

  ### `openUserProfile()`

  Opens the `` component as an overlay at the root of your HTML `body` element.

  ```typescript
  function openUserProfile(props?: UserProfileProps): void
  ```

  #### `openUserProfile()` params

  - **`props?`** [`UserProfileProps`](#properties)

  The properties to pass to the `` component


  #### `openUserProfile()` usage

  ```js
// Filename: main.js

  import { Clerk } from '@clerk/clerk-js'

  // Initialize Clerk with your Clerk Publishable Key
  const clerkPubKey = import.meta.env.VITE_CLERK_PUBLISHABLE_KEY

  const clerk = new Clerk(clerkPubKey)
  await clerk.load()

  document.getElementById('app').innerHTML = `
    <div id="user-profile"></div>
  `

  const userProfileDiv = document.getElementById('user-profile')

  clerk.openUserProfile(userProfileDiv)
  ```

  ### `closeUserProfile()`

  Closes the user profile overlay.

  ```typescript
  function closeUserProfile(): void
  ```

  #### `closeUserProfile()` usage

  ```js
// Filename: main.js

  import { Clerk } from '@clerk/clerk-js'

  // Initialize Clerk with your Clerk Publishable Key
  const clerkPubKey = import.meta.env.VITE_CLERK_PUBLISHABLE_KEY

  const clerk = new Clerk(clerkPubKey)
  await clerk.load()

  document.getElementById('app').innerHTML = `
    <div id="user-profile"></div>
  `

  const userProfileDiv = document.getElementById('user-profile')

  clerk.closeUserProfile(userProfileDiv)
  ```


## Properties

All props are optional.

- **`appearance`** <code>[Appearance](/guides/customizing-clerk/appearance-prop/overview) | undefined</code>

  Optional object to style your components. Will only affect [Clerk components](/reference/components/overview) and not [Account Portal](/guides/account-portal/overview) pages.

    ---

- **`routing`** `'hash' | 'path'`

  The [routing](/guides/how-clerk-works/routing) strategy for your pages. Defaults to `'path'` for frameworks that handle routing, such as Next.js and Remix. Defaults to `hash` for all other SDK's, such as React.

    ---

- **`path`** `string`

  The path where the component is mounted on when `routing` is set to `path`. It is ignored in hash-based routing. For example: `/user-profile`.

    ---

- **`additionalOAuthScopes`** `object`

  Specify additional scopes per OAuth provider that your users would like to provide if not already approved.  For example: `{google: ['foo', 'bar'], github: ['qux']}`.

    ---

- **`customPages`** <code>[CustomPage](/reference/javascript/types/custom-page)\[]</code>

  An array of custom pages to add to the user profile. Only available for the [JavaScript SDK](/reference/javascript/overview). To add custom pages with React-based SDK's, see the [dedicated guide](/guides/customizing-clerk/adding-items/user-profile).

    ---

- **`fallback?`** `ReactNode`

  An optional element to be rendered while the component is mounting.


## Customization

To learn about how to customize Clerk components, see the [customization documentation](/guides/customizing-clerk/appearance-prop/overview).

In addition, you also can add custom pages and links to the `` navigation sidenav. For more information, refer to the [Custom Pages documentation](/guides/customizing-clerk/adding-items/user-profile).
