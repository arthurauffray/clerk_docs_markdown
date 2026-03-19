# Migrating from the Astro community SDK


> Learn how to migrate from the Astro community SDK to the Clerk Astro SDK.

In July 2024, we introduced official support for Astro. This migration guide covers converting from the [`astro-clerk-auth`](https://github.com/panteliselef/astro-with-clerk-auth) community SDK to Clerk's official SDK. It covers the breaking changes that were introduced and provides examples on how to resolve them.

## Installation

Uninstall the community SDK and install Clerk's new official SDK for Astro.

```npm
npm uninstall astro-clerk-auth
npm install @clerk/astro
```

## Breaking Changes

### The integration

With the community SDK, you could choose to either hotload Clerk's `clerk-js` library or bundle it with your application.

With Clerk's official SDK, `clerk-js` is hotloaded by default, and the option to use the bundled `clerk-js` variant has been removed.

The following changes are required in your Astro configuration file:

```js

import { defineConfig } from 'astro/config'
import node from '@astrojs/node'

import clerk from 'astro-clerk-auth/hotload'
import clerk from 'astro-clerk-auth/integration/hotload'
import clerk from 'astro-clerk-auth'
import clerk from 'astro-clerk-auth/integration'
import clerk from '@clerk/astro'

export default defineConfig({
  integrations: [clerk()],
  adapter: node({ mode: 'standalone' }),
  output: 'server',
})
```

### Prefix for environment variables

The prefix for environment variables used in client-side code has been updated to align with Astro's [best practices](https://docs.astro.build/en/guides/environment-variables/). This change affects all [environment variables](/guides/development/clerk-environment-variables) supported by Clerk.

```

PUBLIC_ASTRO_APP_CLERK_PUBLISHABLE_KEY=
PUBLIC_CLERK_PUBLISHABLE_KEY=

PUBLIC_ASTRO_APP_CLERK_SIGN_IN_URL=
PUBLIC_CLERK_SIGN_IN_URL=

PUBLIC_ASTRO_APP_*=
PUBLIC_*=

```

### Astro component export updates

The Astro components have been restructured to provide a more consistent API. The following changes are required to import your Astro components:

```js

import { UserProfile } from '@clerk/astro/components/interactive'
import { UserProfile } from '@clerk/astro/components'

import { Show } from '@clerk/astro/components/control'
import { Show } from '@clerk/astro/components'

import { SignInButton } from '@clerk/astro/components/unstyled'
import { SignInButton } from '@clerk/astro/components'
```

### Stores

Submodule `/stores` was replaced with `/client`. The following changes are required to import the [stores](/reference/astro/overview#client-side-helpers):

```js

import { $clerk } from 'astro-clerk-auth/stores'
import { $clerkStore } from '@clerk/astro/client'

import { $csrState } from 'astro-clerk-auth/stores'
import { $initialState } from 'astro-clerk-auth/stores'
import { $userStore } from '@clerk/astro/client'
import { $sessionStore } from '@clerk/astro/client'
```

### Submodule removal

Submodule `/v0` was dropped completely and the previously exported constants are no longer available.

```js

import { apiKey, secretKey, DOMAIN, ... } from 'astro-clerk-auth/v0'
```

### `clerkClient` changes

The `clerkClient` variable has been deprecated and should now be used as a function that accepts the Astro context.

```ts

import type { APIRoute } from 'astro'
import { clerkClient } from 'astro-clerk-auth/v0'
import { clerkClient } from '@clerk/astro/server'

export const GET: APIRoute = async (context) => {
  clerkClient.users.getUser(/* ... */)
  clerkClient(context).users.getUser(/* ... */)
  // ...
}
```

### React components changes

With the community SDK, there were to ways to use a React component inside a `.astro` file.

To avoid confusion, the official SDK removes the `/components/react` submodule.

```astro

---
import { Show } from '@clerk/astro/components/react'
import { Show } from '@clerk/astro/react'
---


  {...}

```

To use a React component inside a `.jsx` or `.tsx` file, update the import path.

```jsx

import { Show, SignInButton, UserButton } from '@clerk/astro/client/react'
import { Show, SignInButton, UserButton } from '@clerk/astro/react'

export default function Header() {
  return (
    <>
      <p>My App</p>
      
        </>
  )
}
```
