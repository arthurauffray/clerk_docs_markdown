# $authStore


> Clerk's $authStore nanostore provides a convenient way to access the current auth state and helper methods for managing the session.

The `$authStore` store provides a convenient way to access the current auth state and helper methods for managing the session.

## Returns

- **`userId`** `string`

  The ID of the current user.

    ---

- **`sessionId`** `string`

  The ID of the current session.

    ---

- **`orgId`** `string`

  The ID of the user's Active Organization.

    ---

- **`orgRole`** `string`

  The current user's Role in their Active Organization.

    ---

- **`orgSlug`** `string`

  The URL-friendly identifier of the user's Active Organization.


## How to use the `$authStore` store

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
