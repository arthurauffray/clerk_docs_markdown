# clerkPlugin()


> The clerkPlugin() function is a Fastify plugin that integrates Clerk's authentication into your application.

The `clerkPlugin()` function is a Fastify plugin that integrates Clerk's authentication into your application. The function checks request cookies and headers for a session JWT. If valid, it attaches the [`Auth`](/reference/backend/types/auth-object) object to the `request` object under the `auth` key.

You can register the plugin for [all routes](#example-register-clerk-plugin-for-all-routes) or [limit it to specific ones](#example-register-clerk-plugin-for-specific-routes).

### Example: Register `clerkPlugin()` for all routes

```ts
import 'dotenv/config' // dotenv must be imported before @clerk/fastify
import Fastify from 'fastify'
import { clerkPlugin } from '@clerk/fastify'

const fastify = Fastify({ logger: true })

fastify.register(clerkPlugin)

const start = async () => {
  try {
    await fastify.listen({ port: 8080 })
  } catch (error) {
    fastify.log.error(error)
    process.exit(1)
  }
}

start()
```

### Example: Register `clerkPlugin()` for specific routes

To apply Clerk authentication only to specific routes, register the plugin in the scope of those routes.

In the following example, the application is split into protected and public routes:

```ts
// Filename: index.ts

import 'dotenv/config' // dotenv must be imported before @clerk/fastify
import Fastify, { FastifyPluginCallback } from 'fastify'
import { clerkClient, clerkPlugin, getAuth } from '@clerk/fastify'

const fastify = Fastify({ logger: true })

const protectedRoutes: FastifyPluginCallback = (instance, options, done) => {
  instance.register(clerkPlugin)

  instance.get('/protected', async (req, reply) => {
    // Use `getAuth()` to access `isAuthenticated` and the user's ID
    const { isAuthenticated, userId } = getAuth(req)

    // Protect the route from unauthenticated users
    if (!isAuthenticated) {
      return reply.code(403).send({ message: 'Access denied. Authentication required.' })
    }

    // Use `clerkClient` to access Clerk's JS Backend SDK methods
    const user = await clerkClient.users.getUser(userId)

    // Only authenticated users will see the following message
    reply.send({ message: 'This is a protected route.', user })
  })

  done()
}

const publicRoutes: FastifyPluginCallback = (instance, options, done) => {
  instance.get('/', async (req, reply) => {
    reply.send({ message: 'This is a public route.' })
  })

  done()
}

fastify.register(protectedRoutes)
fastify.register(publicRoutes)

const start = async () => {
  try {
    await fastify.listen({ port: 8080 })
  } catch (error) {
    fastify.log.error(error)
    process.exit(1)
  }
}

start()
```

### `clerkPlugin()` options

The `clerkPlugin()` function accepts the following options:

- **`secretKey` (required)** `string`

  Your Clerk Secret Key.

    ---

- **`jwtKey?`** `string`

  The **JWKS Public Key** from the [**API keys**](https://dashboard.clerk.com/~/api-keys) in the Clerk Dashboard. For more information, refer to [Manual JWT verification](/guides/sessions/manual-jwt-verification).

    ---

- **`publishableKey?`** `string`

  Your Clerk Publishable Key.

    ---

- **`domain?`** `string`

  The domain of a [satellite application](/guides/dashboard/dns-domains/satellite-domains) in a multi-domain setup.

    ---

- **`isSatellite?`** `boolean`

  Whether the instance is a satellite domain in a multi-domain setup. Defaults to `false`.

    ---

- **`satelliteAutoSync?`** `boolean`

  Controls whether a satellite app automatically syncs authentication state with the primary domain on first page load. When `false` (default), the satellite app skips the automatic redirect if no session cookies exist, and only triggers the handshake after the user initiates a sign-in or sign-up action. When `true`, the satellite app redirects to the primary domain on every first visit to sync state. Defaults to `false`. See [satellite domains](/guides/dashboard/dns-domains/satellite-domains) for more details.


    ---

- **`proxyUrl?`** `string`

  The proxy URL from a multi-domain setup.

    ---

- **`sdkMetadata?`** `{ name: string, version: string }`

  Metadata about the SDK.

    ---

- **`telemetry?`** `{ disabled: boolean, debug: boolean }`

  [Telemetry](/guides/how-clerk-works/security/clerk-telemetry) configuration.

    ---

- **`userAgent?`** `string`

  The User-Agent request header passed to the Clerk API.

    ---

- **`apiUrl?`** `string`

  The [Clerk Backend API](/reference/backend-api) endpoint. Defaults to `'https://api.clerk.com'`.

    ---

- **`apiVersion?`** `string`

  The version passed to the Clerk API. Defaults to `'v1'`.

    ---

- **`audience?`** `string | string[]`

  A string or list of [audiences](https://datatracker.ietf.org/doc/html/rfc7519#section-4.1.3).

    ---

- **`taskUrls?`** `Record`

  The URL paths users are redirected to after sign-up or sign-in when specific session tasks need to be completed. For example, `{ 'choose-organization': '/onboarding/choose-organization' }` redirects users to `/onboarding/choose-organization` after sign-up if they need to choose an Organization.


- **`hookName`** `'onRequest' | 'preHandler'`

  Determines which of Fastify's [Request/Reply hooks](https://fastify.dev/docs/latest/Reference/Hooks/#requestreply-hooks) Clerk should run. Default: `'preHandler'`


#### Example: Pass `hookName` in `clerkPlugin()` options

```ts
fastify.register(clerkPlugin, {
  hookName: 'preHandler',
})
```
