# Frontend-only SDK


> A reference for implementing a frontend-only Clerk SDK

While [ClerkJS](/reference/javascript/overview) can be used in any browser context and framework, realistically users expect to consume its features through the conventions and syntax of their framework of choice. For example, `@clerk/react` turns ClerkJS into React components, `@clerk/astro` into Astro components, and so on.

In non-browser environments, you’ll need to re-implement the [Clerk class](/reference/javascript/clerk) in the SDK’s programming language, interacting with the [FAPI](/guides/development/sdk-development/terminology).

## Expected features

- User only needs to provide their [Publishable Key](/guides/development/sdk-development/terminology)
- User only needs to adjust one or two files to add Clerk to their app (e.g. adding Clerk to the configuration file of that framework)
- User can use [Clerk’s components](/reference/components/overview) in their choice of framework (e.g. in a React-based framework you import these components as React components)
- Give users access to [`Client`](/reference/javascript/client), [`Session`](/reference/javascript/session), [`User`](/reference/javascript/user), and [`Organization`](/reference/javascript/organization) properties through the framework’s choice of state management
- User should be able to use [ClerkJS options](/reference/javascript/clerk#clerk-options)

## Implementation

While the implementation details will vary for each SDK, there are certain steps you'll have to go through in any case. Consider the steps below a rough guidance on what needs to be done, and also remember to follow the [conventions](/guides/development/sdk-development/conventions).

> [!NOTE]
> The code blocks below will be written in pseudo-code. If you're looking for real-world examples, have a look at these repositories: [`@clerk/react`](https://github.com/clerk/javascript/tree/main/packages/react), [`@clerk/astro`](https://github.com/clerk/javascript/tree/main/packages/astro)


  ### Create a Clerk instance

  Create a Clerk instance that will only be invoked once (e.g. following the [singleton pattern](https://www.patterns.dev/vanilla/singleton-pattern/)). During its initialization you'll execute the following steps.

  ```ts
// Filename: create-clerk-instance.ts

  import { runOnce } from './utils'
  // States accessible to other parts of your SDK and/or its users
  import { $clerk, $state } from './stores'

  export const createClerkInstance = runOnce(createClerkInstanceInternal)

  async function createClerkInstanceInternal(options) {
    let clerkJSInstance = window.Clerk
  }
  ```

  ### Hotload ClerkJS

  In order to make `Clerk` available on the `window` object, your SDK needs to load ClerkJS. Call `loadClerkJsScript()` from `@clerk/shared`.

  ```ts
// Filename: create-clerk-instance.ts

  import { loadClerkJSScript } from '@clerk/shared/loadClerkJSScript'
  import { runOnce } from './utils'
  import { $clerk, $state } from './stores'

  export const createClerkInstance = runOnce(createClerkInstanceInternal)

  async function createClerkInstanceInternal(options) {
    let clerkJSInstance = window.Clerk

    if (!clerkJSInstance) {
      await loadClerkJSScript(options)

      if (!window.Clerk) {
        throw new Error('Failed to download latest ClerkJS.')
      }
      clerkJSInstance = window.Clerk
    }

    if (!$clerk.get()) {
      $clerk.set(clerkJSInstance)
    }
  }
  ```

  ### Call `window.Clerk.load()`

  By calling [`window.Clerk.load()`](/reference/javascript/clerk#load) the Clerk class is initialized and your SDK now has access to all its functionality.

  ```ts
// Filename: create-clerk-instance.ts

  import { loadClerkJSScript } from '@clerk/shared/loadClerkJSScript'
  import { runOnce } from './utils'
  import { $clerk, $state } from './stores'

  export const createClerkInstance = runOnce(createClerkInstanceInternal)

  async function createClerkInstanceInternal(options) {
    let clerkJSInstance = window.Clerk

    if (!clerkJSInstance) {
      // loadClerkJSScript() codepath
    }

    if (!$clerk.get()) {
      $clerk.set(clerkJSInstance)
    }

    await clerkJSInstance.load(options)
  }
  ```

  ### Add event listeners

  Expose properties to the internal state (e.g. a `useState` in React) through adding [event listeners](/reference/javascript/clerk#add-listener).

  ```ts
// Filename: create-clerk-instance.ts

  import { loadClerkJSScript } from '@clerk/shared/loadClerkJSScript'
  import { runOnce } from './utils'
  import { $clerk, $state } from './stores'

  export const createClerkInstance = runOnce(createClerkInstanceInternal)

  async function createClerkInstanceInternal(options) {
    let clerkJSInstance = window.Clerk

    if (!clerkJSInstance) {
      // loadClerkJSScript() codepath
    }

    await clerkJSInstance.load(options)

    if (!$clerk.get()) {
      $clerk.set(clerkJSInstance)
    }

    clerkJSInstance.addListener((resources) => {
      $state.setKey('client', resources.client)
      $state.setKey('session', resources.session)
      $state.setKey('user', resources.user)
      $state.setKey('organization', resources.organization)
    })
  }
  ```

  ### Add UI components

  Build out the components that your users will utilize in their app. Call the `mount()` function when the component is in view/mounts and the `unmount()` function when the component is unmounted. These functions are described in the [`Clerk` class components](/reference/javascript/clerk#components).

  Use the idiomatic way of your framework for doing this. If you can abstract these repetitions into a re-usable hook/directive, then do that.

  ```tsx
// Filename: SignIn.tsx

  import { $clerk } from './stores'

  const SignInComponent = (props: SignInProps) => {
    const el = ref()

    function onMount() {
      $clerk.mountSignIn(el, props)
    }

    function onUnMount() {
      $clerk.unmountSignIn(el)
    }
  }
  ```
