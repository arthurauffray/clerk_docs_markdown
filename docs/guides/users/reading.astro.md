# Read session and user data in your Astro app with Clerk


> Learn how to use Clerk's helpers to protect content and read user data in your Astro application.

Clerk provides helpers that you can use to protect content and read user data in your Astro application.

## Server-side

The [`auth()`](/reference/astro/locals) and [`currentUser()`](/reference/astro/locals) locals are Astro-specific helpers that you can use inside of your Astro components and [endpoints](https://docs.astro.build/en/guides/endpoints/#server-endpoints-api-routes).

- The `auth()` local returns the [`Auth`](/reference/backend/types/auth-object) object of the currently active user.
- The `currentUser()` local returns the [`Backend User`](/reference/backend/types/backend-user) object of the currently active user. This is helpful if you want to render user information, like their first and last name, directly from the server. Under the hood, `currentUser()` uses the [`clerkClient`](/js-backend/getting-started/quickstart) wrapper to make a call to the Backend API. **This does count towards the [Backend API request rate limit](/guides/how-clerk-works/system-limits)**. This also uses `fetch()` so it is automatically deduped per request.

The following example demonstrates how to protect a page from unauthenticated users and access the current user's information.


**.astro component:**

```astro
// Filename: src/pages/me.astro

  ---
  // Use `locals.auth()` to access `isAuthenticated` and the user's ID
  const { isAuthenticated, userId } = Astro.locals.auth()

  // Protect the route by checking if the user is signed in
  if (!isAuthenticated) {
    return Astro.redirect('/login')
  }

  // Get the Backend User object when you need access to the user's information
  const user = await Astro.locals.currentUser()
  ---

  <!-- Use `user` to render user details or create UI elements -->
  <div>Welcome, {user.firstName}!</div>
  ```


**API Route:**

```tsx
// Filename: src/api/me.ts

  export async function GET({ locals }) {
    // Use `locals.auth()` to access `isAuthenticated` and the user's ID
    const { isAuthenticated, userId } = locals.auth()

    // Protect the route by checking if the user is signed in
    if (!isAuthenticated) {
      return new Response('Unauthorized', { status: 401 })
    }

    // Get the Backend User object when you need access to the user's information
    const user = await locals.currentUser()

    // Add your Route Handler's logic with the returned `user` object

    return new Response(
      JSON.stringify({ userId: user.id, email: user.emailAddresses[0].emailAddress }),
    )
  }
  ```


### Retrieve data from external sources

Clerk provides integrations with a number of popular databases.

To retrieve a token from a [JWT template](/guides/sessions/jwt-templates) and fetch data from an external source, use the [`getToken()`](/reference/backend/types/auth-object#get-token) method from the `auth()` local.

```ts
// Filename: src/pages/api/route.ts

export async function GET({ locals }) {
  // Use `locals.auth()` to access `isAuthenticated`, the user's ID, and the `getToken()` method
  const { isAuthenticated, userId, getToken } = locals.auth()

  // Protect the route by checking if the user is signed in
  if (!isAuthenticated) {
    return new Response('Unauthorized', { status: 401 })
  }

  // Use `getToken()` to get a token from the JWT template
  const token = await getToken({ template: 'supabase' })

  // Fetch data from Supabase and return it
  const data = { supabaseData: 'Hello World' }

  return new Response(JSON.stringify(data))
}
```

## Client-side

Clerk Astro provides a set of useful [stores](/reference/astro/overview#client-side-helpers) that give you access to many important objects, such as the `Clerk`, `User`, and `Session` object.

### `$authStore`

The following example demonstrates how to use the [`$authStore`](/reference/astro/client-side-helpers/auth-store) to access the current auth state. It uses `userId` to detect if the user is signed in.


**React:**

```tsx
// Filename: components/external-data.tsx

  import { useStore } from '@nanostores/react'
  import { $authStore } from '@clerk/astro/client'

  export default function ExternalData() {
    const { userId } = useStore($authStore)

    if (userId === undefined) {
      // Handle loading state however you like
      return <div>Loading...</div>
    }

    if (userId === null) {
      // Handle signed out state however you like
      return <div>Sign in to view this page</div>
    }

    return <div>...</div>
  }
  ```


**Vue:**

```vue
// Filename: components/external-data.vue

  <script setup>
  import { useStore } from '@nanostores/vue'
  import { $authStore } from '@clerk/astro/client'

  const auth = useStore($authStore)
  </script>

  <template>
    <div v-if="auth.userId === undefined">Loading...</div>
    <div v-else-if="auth.userId === null">Sign in to view this page</div>
    <div v-else>...</div>
  </template>
  ```


**Svelte:**

```svelte
// Filename: components/external-data.svelte

  <script>
    // The $ prefix is reserved in Svelte for its own reactivity system.
    // Alias the imports to avoid conflicts.
    import { $authStore as auth } from '@clerk/astro/client'
  </script>

  {#if $auth.userId === undefined}
    <div>Loading...</div>
  {:else if $auth.userId === null}
    <div>Sign in to view this page</div>
  {:else}
    <div>...</div>
  {/if}
  ```


### `$userStore`

The following example demonstrates how to use the [`$userStore`](/reference/astro/client-side-helpers/user-store) to access the `User` object. It returns `undefined` while Clerk is still loading and `null` if the user is not signed in.

For more information, see the [`User` reference](/reference/javascript/user).


**React:**

```tsx
// Filename: user.tsx

  import { useStore } from '@nanostores/react'
  import { $userStore } from '@clerk/astro/client'

  export default function User() {
    const user = useStore($userStore)

    if (user === undefined) {
      // Handle loading state however you like
      return null
    }

    if (user === null) {
      return <div>Not signed in</div>
    }

    return <div>Hello {user.fullName}!</div>
  }
  ```


**Vue:**

```vue
// Filename: user.vue

  <script setup>
  import { useStore } from '@nanostores/vue'
  import { $userStore } from '@clerk/astro/client'

  const user = useStore($userStore)
  </script>

  <template>
    <div v-if="user === undefined">
      <!-- Handle loading state however you like -->
    </div>
    <div v-else-if="user === null">Not signed in</div>
    <div v-else>Hello {{ user.fullName }}!</div>
  </template>
  ```


**Svelte:**

```svelte
// Filename: user.svelte

  <script>
    // The $ prefix is reserved in Svelte for its own reactivity system.
    // Alias the imports to avoid conflicts.
    import { $userStore as user } from '@clerk/astro/client'
  </script>

  {#if $user === undefined}
    <!-- Handle loading state however you like -->
  {:else if $user === null}
    <div>Not signed in</div>
  {:else}
    <div>Hello {$user.fullName}!</div>
  {/if}
  ```
