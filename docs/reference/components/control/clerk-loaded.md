# <ClerkLoaded>


> The <ClerkLoaded> component guarantees that the Clerk object has loaded and will be available under window.Clerk. This allows you to wrap child components to access the Clerk object without the need to check it exists.

The `` component guarantees that the Clerk object has loaded (the `status` is `'ready'` or `'degraded'`) and will be available under `window.Clerk`. This allows you to wrap child components to access the `Clerk` object without the need to check it exists.


  ## Example

  It's not recommended to wrap the entire app in the `` component; instead, only wrap the components that need access to the `Clerk` object.

  
  
**App Router:**

```tsx
// Filename: app/page.tsx

    import { ClerkLoaded, ClerkLoading, ClerkDegraded, ClerkFailed } from '@clerk/nextjs'

    export default function Page() {
      return (
        <>
          
            <p>Clerk is loading...</p>
          
          
            <p>Clerk has loaded (ready or degraded)</p>
            
              <p>Clerk is experiencing issues. Please try again later.</p>
            
          
          
            <p>Something went wrong with Clerk. Please contact support.</p>
          
        </>
      )
    }
    ```


**Pages Router:**

```tsx
// Filename: pages/index.tsx

    import { ClerkLoaded, ClerkLoading, ClerkDegraded, ClerkFailed } from '@clerk/nextjs'

    export default function Page() {
      return (
        <>
          
            <p>Clerk is loading...</p>
          
          
            <p>Clerk has loaded (ready or degraded)</p>
            
              <p>Clerk is experiencing issues. Please try again later.</p>
            
          
          
            <p>Something went wrong with Clerk. Please contact support.</p>
          
        </>
      )
    }
    ```


  ```tsx
// Filename: src/App.tsx

  import { ClerkLoaded, ClerkLoading, ClerkDegraded, ClerkFailed } from '@clerk/react'

  export default function App() {
    return (
      <>
        
          <p>Clerk is loading...</p>
        
        
          <p>Clerk has loaded (ready or degraded)</p>
          
            <p>Clerk is experiencing issues. Please try again later.</p>
          
        
        
          <p>Something went wrong with Clerk. Please contact support.</p>
        
      </>
    )
  }

  export default App
  ```


  ```tsx
// Filename: app/routes/example.tsx

  import { ClerkLoading, ClerkLoaded, ClerkDegraded, ClerkFailed } from '@clerk/react-router'

  export default function Example() {
    return (
      <>
        
          <p>Clerk is loading...</p>
        
        
          <p>Clerk has loaded (ready or degraded)</p>
          
            <p>Clerk is experiencing issues. Please try again later.</p>
          
        
        
          <p>Something went wrong with Clerk. Please contact support.</p>
        
      </>
    )
  }
  ```


  ```jsx
// Filename: src/routes/home.tsx

  import { ClerkLoaded, ClerkLoading, ClerkDegraded, ClerkFailed } from '@clerk/chrome-extension'

  export default function Home() {
    return (
      <>
        
          <p>Clerk is loading...</p>
        
        
          <p>Clerk has loaded (ready or degraded)</p>
          
            <p>Clerk is experiencing issues. Please try again later.</p>
          
        
        
          <p>Something went wrong with Clerk. Please contact support.</p>
        
      </>
    )
  }
  ```


  ```tsx
// Filename: app/routes/_index.tsx

  import { ClerkLoading, ClerkLoaded, ClerkDegraded, ClerkFailed } from '@clerk/remix'

  export default function Index() {
    return (
      <>
        
          <p>Clerk is loading...</p>
        
        
          <p>Clerk has loaded (ready or degraded)</p>
          
            <p>Clerk is experiencing issues. Please try again later.</p>
          
        
        
          <p>Something went wrong with Clerk. Please contact support.</p>
        
      </>
    )
  }
  ```


  ```tsx
// Filename: app/routes/index.tsx

  import { ClerkLoading, ClerkLoaded, ClerkDegraded, ClerkFailed } from '@clerk/tanstack-react-start'
  import { createFileRoute } from '@tanstack/react-router'

  export const Route = createFileRoute('/')({
    component: Home,
  })

  function Home() {
    return (
      <>
        
          <p>Clerk is loading...</p>
        
        
          <p>Clerk has loaded (ready or degraded)</p>
          
            <p>Clerk is experiencing issues. Please try again later.</p>
          
        
        
          <p>Something went wrong with Clerk. Please contact support.</p>
        
      </>
    )
  }
  ```


  
    > [!NOTE]
    > Unlike other Clerk components for Astro, `` must be imported from `@clerk/astro/react`. This requires that your Astro app is set up with React. See [Use Clerk with Astro and React](/reference/astro/react) for guidance.

    ```astro
// Filename: index.astro

    ---
    import { ClerkLoaded } from '@clerk/astro/react'
    ---

    
      <p>Clerk has loaded</p>
    
    ```
  

  
    ```tsx
// Filename: app/index.tsx

    import { ClerkLoaded } from '@clerk/expo'
    import { Text, View } from 'react-native'

    export default function Screen() {
      return (
        
          
            Clerk has loaded
          
        
      )
    }
    ```
  

  
    ```vue
// Filename: App.vue

    <script setup lang="ts">
    import { ClerkLoaded } from '@clerk/vue'
    </script>

    <template>
      
        <p>Clerk has loaded</p>
      
    </template>
    ```
  

  
    ```vue
// Filename: App.vue

    <script setup lang="ts">
    // Components are automatically imported
    </script>

    <template>
      
        <p>Clerk has loaded</p>
      
    </template>
    ```
  


  ## Usage with JavaScript

  The following methods available on an instance of the [`Clerk`](/reference/javascript/clerk) class is used to render and control the `` component:

  - [`load()`](#load)

  The following examples assume that you have followed the [quickstart](/js-frontend/getting-started/quickstart) in order to add Clerk to your JavaScript application.

  ### `load()`

  Render the `` component to an HTML `<div>` element.

  ```typescript
  function load(options?: ClerkOptions): Promise<void>
  ```

  #### `ClerkOptions`

  The `load()` method accepts an optional object that accepts the following props. All props are optional.

- **`appearance`** <code>[Appearance](/guides/customizing-clerk/appearance-prop/overview) | undefined</code>

  Optional object to style your components. Will only affect \[Clerk components]\[components-ref] and not \[Account Portal]\[ap-ref] pages.

    ---

- **`localization`** <code>[Localization](/guides/customizing-clerk/localization) | undefined</code>

  Optional object to localize your components. Will only affect \[Clerk components]\[components-ref] and not \[Account Portal]\[ap-ref] pages.

    ---

- **`routerPush?`** `(to: string) => Promise<unknown> | void`

  A function which takes the destination path as an argument and performs a "push" navigation.

    ---

- **`routerReplace?`** `(to: string) => Promise<unknown> | void`

  A function which takes the destination path as an argument and performs a "replace" navigation.

    ---

- **`polling`** `boolean | undefined`

  Dictates if we should poll against Clerk's backend every 5 minutes. Defaults to `true`.

    ---

- **`selectInitialSession`** <code>((client: \[Client]\[client-ref]) => Session | null) | undefined</code>

  An optional function which allows you to control which active session is the initial session to base a user's state off of. Defaults to the first session in the client's sessions array.

    ---

- **`standardBrowser`** `boolean | undefined`

  Controls if ClerkJS will load with the standard browser set up using Clerk cookies. Defaults to `true`.

    ---

- **`supportEmail`** `string | undefined`

  Optional support email for display in authentication screens.

    ---

- **`touchSession`** `boolean | undefined`

  Indicates whether the session should be "touched" when user interactions occur, used to record these interactions. Defaults to `true`.

    ---

- **`signInUrl`** `string | undefined`

  The default URL to use to direct to when the user signs in. It's recommended to use [the environment variable](/guides/development/clerk-environment-variables#sign-in-and-sign-up-redirects) instead.

    ---

- **`signUpUrl`** `string | undefined`

  The default URL to use to direct to when the user signs up. It's recommended to use [the environment variable](/guides/development/clerk-environment-variables#sign-in-and-sign-up-redirects) instead.

    ---

- **`signInForceRedirectUrl?`** `string`

  If provided, this URL will always be redirected to after the user signs in. It's recommended to use [the environment variable](/guides/development/clerk-environment-variables#sign-in-and-sign-up-redirects) instead.

    ---

- **`signUpForceRedirectUrl?`** `string`

  If provided, this URL will always be redirected to after the user signs up. It's recommended to use [the environment variable](/guides/development/clerk-environment-variables#sign-in-and-sign-up-redirects) instead.

    ---

- **`signInFallbackRedirectUrl?`** `string`

  The fallback URL to redirect to after the user signs in, if there's no `redirect_url` in the path already. Defaults to `/`. It's recommended to use [the environment variable](/guides/development/clerk-environment-variables#sign-in-and-sign-up-redirects) instead.

    ---

- **`signUpFallbackRedirectUrl?`** `string`

  The fallback URL to redirect to after the user signs up, if there's no `redirect_url` in the path already. Defaults to `/`. It's recommended to use [the environment variable](/guides/development/clerk-environment-variables#sign-in-and-sign-up-redirects) instead.

    ---

- **`afterSignOutUrl?`** `string`

  The full URL or path to navigate to after a successful sign-out.

    ---

- **`allowedRedirectOrigins?`** `Array<string | RegExp>`

  An optional array of domains to validate user-provided redirect URLs against. If no match is made, the redirect is considered unsafe and the default redirect will be used with a warning logged in the console.

    ---

- **`allowedRedirectProtocols?`** `Array<string>`

  An optional array of protocols to validate user-provided redirect URLs against. If no match is made, the redirect is considered unsafe and the default redirect will be used with a warning logged in the console.

    ---

- **`isSatellite`** `boolean | ((url: URL) => boolean) | undefined`

  Clerk flag for satellite apps. Experimental.

    ---

- **`telemetry?`** `false | { disabled?: boolean; debug?: boolean } | undefined`

  Controls whether or not Clerk will collect [telemetry data](/guides/how-clerk-works/security/clerk-telemetry).


  #### `load()` usage

  ```js
// Filename: main.js

  import { Clerk } from '@clerk/clerk-js'

  // Initialize Clerk with your Clerk Publishable Key
  const clerkPubKey = import.meta.env.VITE_CLERK_PUBLISHABLE_KEY

  const clerk = new Clerk(clerkPubKey)
  await clerk.load()
  ```
