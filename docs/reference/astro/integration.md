# Integration


> The Astro integration provides session and user context to Clerk's hooks and components.

The Clerk integration is required to integrate Clerk into your Astro application, providing session and user context to Clerk's hooks, nanostores, and components.

## Usage

To configure Clerk with Astro, you must pass the `clerk()` integration to the `integrations` array in your `astro.config.mjs` file. The `clerk()` integration accepts optional options, such as `{ signInForceRedirectUrl: '/dashboard' }`. See the [properties section](#properties) for more information.

> [!WARNING]
> For SSR, there is further configuration required. See the [quickstart](/astro/getting-started/quickstart#update-astro-config-mjs) for more information.

```ts
// Filename: astro.config.mjs

import { defineConfig } from 'astro/config'
import clerk from '@clerk/astro'

export default defineConfig({
  // Can accept options, such as { signInForceRedirectUrl: '/dashboard' }
  integrations: [clerk()],
})
```
