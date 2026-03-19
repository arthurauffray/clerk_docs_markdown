# useSessionList() | Vue


> Access and manage a list of sessions registered on the client device in your Vue application with Clerk's useSessionList() composable.

The `useSessionList()` composable returns an array of [`Session`](/reference/javascript/session) objects that have been registered on the client device.

## Returns

- **`isLoaded`** `Ref<boolean>`

  A boolean that indicates whether Clerk has completed initialization. Initially `false`, becomes `true` once Clerk loads.

    ---

- **`setActive()`** <code>Ref\<(params: [SetActiveParams](/reference/javascript/types/set-active-params)) => Promise\<void>></code>

  A function that sets the active session and/or Organization.

    ---

- **`sessions`** <code>Ref\<[Session](/reference/javascript/session)></code>

  A list of sessions that have been registered on the client device.


## How to use the `useSessionList()` composable

### Get a list of sessions

The following example uses `useSessionList()` to get a list of sessions that have been registered on the client device. The `sessions` property is used to show the number of times the user has visited the page.

```vue
// Filename: SessionList.vue

<script setup>
import { useSessionList } from '@clerk/vue'

const { isLoaded, sessions } = useSessionList()
</script>

<template>
  <div v-if="!isLoaded">
    <!-- Handle loading state -->
  </div>

  <div v-else>
    <p>Welcome back. You've been here {{ sessions.length }} times before.</p>
  </div>
</template>
```
