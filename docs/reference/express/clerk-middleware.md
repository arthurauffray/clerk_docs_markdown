# clerkMiddleware()


> The clerkMiddleware() function checks the request's cookies and headers for a session JWT and if found, attaches the Auth object to the request object under the auth key.

The `clerkMiddleware()` function checks the request's cookies and headers for a session JWT and if found, attaches the [`Auth`](/reference/backend/types/auth-object) object to the `request` object under the `auth` key. **It must be set before any other middleware.**

> [!TIP]
> Even if you are using [`requireAuth()`](/reference/express/require-auth) middleware, you should still use `clerkMiddleware()` as it will provide authentication state to routes that don't use `requireAuth()`. See the [example](#example-use-clerk-middleware-require-auth-and-get-auth-together).

```js
import { clerkMiddleware } from '@clerk/express'

const app = express()

// Pass no parameters
app.use(clerkMiddleware())

// Pass options
app.use(clerkMiddleware(options))
```

## Example: Use `clerkMiddleware()`, `requireAuth()`, and `getAuth()` together

The following example demonstrates how to use `clerkMiddleware()`, [`requireAuth()`](/reference/express/require-auth), and [`getAuth()`](/reference/express/get-auth) together. `clerkMiddleware()` will provide authentication state to routes that don't use `requireAuth()`, `requireAuth()` will provide authentication state to a route and also protect the route based on authentication status, and `getAuth()` can be used in a number of ways. In this example, `getAuth()` is used to protect the route based on authorization status.

```js
import { clerkMiddleware, getAuth, requireAuth } from '@clerk/express'
import express from 'express'

const app = express()
const PORT = 3000

// Apply `clerkMiddleware()` to all routes
app.use(clerkMiddleware())

// Use `getAuth()` to protect a route based on authorization status
const hasPermission = (req, res, next) => {
  const auth = getAuth(req)

  // Handle if the user is not authorized
  if (!auth.has({ permission: 'org:admin:example' })) {
    return res.status(403).send('Forbidden')
  }

  return next()
}

// Use `requireAuth()` to protect a route based on authentication status
// If user is not authenticated, requireAuth() will redirect back to the homepage
// Then, use the `hasPermission` function created above to protect the route based on authorization status
app.get('/path', requireAuth(), hasPermission, (req, res) => res.json(req.auth))

// This route is not protected but it will have authentication state
// attached to the request object because `clerkMiddleware()` was applied to all routes
app.get('/path2', (req, res) => res.json(req.auth))

// Start the server and listen on the specified port
app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`)
})
```

### `clerkMiddleware()` options

The `clerkMiddleware()` function accepts an optional object. The following options are available:

- **`audience?`** `string | string[]`

  A string or list of [audiences](https://datatracker.ietf.org/doc/html/rfc7519#section-4.1.3). If passed, it is checked against the `aud` claim in the token.

    ---

- **`authorizedParties?`** `string[]`

  An allowlist of origins to verify against, to protect your application from the subdomain cookie leaking attack. For example: `['http://localhost:3000', 'https://example.com']`

    ---

- **`clockSkewInMs?`** `number`

  Specifies the allowed time difference (in milliseconds) between the Clerk server (which generates the token) and the clock of the user's application server when validating a token. Defaults to 5000 ms (5 seconds).

    ---

- **`domain?`** `string`

  The domain used for satellites to inform Clerk where this application is deployed.

    ---

- **`isSatellite?`** `boolean`

  When using Clerk's satellite feature, this should be set to `true` for secondary domains.

    ---

- **`satelliteAutoSync?`** `boolean`

  Controls whether a satellite app automatically syncs authentication state with the primary domain on first page load. When `false` (default), the satellite app skips the automatic redirect if no session cookies exist, and only triggers the handshake after the user initiates a sign-in or sign-up action. When `true`, the satellite app redirects to the primary domain on every first visit to sync state. Defaults to `false`. See [satellite domains](/guides/dashboard/dns-domains/satellite-domains) for more details.


    ---

- **`jwtKey`** `string`

  Used to verify the session token in a networkless manner. Supply the **JWKS Public Key** from the [**API keys**](https://dashboard.clerk.com/~/api-keys) page in the Clerk Dashboard. **It's recommended to use [the environment variable](/guides/development/clerk-environment-variables) instead.** For more information, refer to [Manual JWT verification](/guides/sessions/manual-jwt-verification).

    ---

- **`organizationSyncOptions?`** <code>[OrganizationSyncOptions](#organization-sync-options) | undefined</code>

  Used to activate a specific [Organization](/guides/organizations/overview) or Personal Account based on URL path parameters. If there's a mismatch between the Active Organization in the session (e.g., as reported by [`auth()`](/reference/nextjs/app-router/auth)) and the Organization indicated by the URL, the middleware will attempt to activate the Organization specified in the URL.

    ---

- **`proxyUrl?`** `string`

  Specify the URL of the proxy, if using a proxy.

    ---

- **`signInUrl`** `string`

  The full URL or path to your sign-in page. Needs to point to your primary application on the client-side. **Required for a satellite application in a development instance.** It's recommended to use [the environment variable](/guides/development/clerk-environment-variables#sign-in-and-sign-up-redirects) instead.

    ---

- **`signUpUrl`** `string`

  The full URL or path to your sign-up page. Needs to point to your primary application on the client-side. **Required for a satellite application in a development instance.** It's recommended to use [the environment variable](/guides/development/clerk-environment-variables#sign-in-and-sign-up-redirects) instead.

    ---

- **`publishableKey`** `string`

  The Clerk Publishable Key for your instance.

    ---

- **`secretKey?`** `string`

  The Clerk Secret Key for your instance. The `CLERK_ENCRYPTION_KEY` environment variable must be set when providing `secretKey` as an option, refer to [Dynamic keys](#dynamic-keys).

    ---

- **`frontendApiProxy?`** [`FrontendApiProxyOptions`](#frontend-api-proxy-options)

  Configure Frontend API proxy handling. When enabled, requests to the proxy path are forwarded to [Clerk's Frontend API](/reference/frontend-api), and the `proxyUrl` is automatically derived for authentication handshake.


- **`clerkClient`** [`ClerkClient`](/js-backend/getting-started/quickstart#create-clerk-client-options)

  An instance of the `ClerkClient` class. This is used to interact with the Clerk API.

    ---

- **`debug`** `boolean`

  A flag to enable debug mode. When set to `true`, the middleware will log debug information to the console. Defaults to `false`.


### Frontend API proxy

The `frontendApiProxy` option enables built-in proxying of Clerk Frontend API requests through your application. Use this when requests to Clerk's API cannot be made directly from the browser and must be routed through your server.

When enabled, requests matching the proxy path (by default, `/__clerk`) are intercepted and forwarded to [Clerk's Frontend API](/reference/frontend-api) before authentication runs. The `proxyUrl` used for authentication handshake is automatically derived.

> [!NOTE]
> You must also [enable proxying](/guides/dashboard/dns-domains/proxy-fapi#enable-proxying) in the Clerk Dashboard and configure the client-side proxy URL so ClerkJS routes browser requests through your proxy.


```js
import { clerkMiddleware } from '@clerk/express'
import express from 'express'

const app = express()

// Enable proxy with default path ('/__clerk')
app.use(
  clerkMiddleware({
    frontendApiProxy: {
      enabled: true,
    },
  }),
)

// Or with a custom proxy path
app.use(
  clerkMiddleware({
    frontendApiProxy: {
      enabled: true,
      path: '/custom-clerk-proxy',
    },
  }),
)
```

#### `FrontendApiProxyOptions`

- **`enabled`** `boolean | ((url: URL) => boolean)`

  Enable Frontend API proxy handling. When `true`, requests to the proxy path are forwarded to [Clerk's Frontend API](/reference/frontend-api), and the `proxyUrl` is automatically derived for authentication handshake.

    ---

- **`path?`** `string`

  The path prefix for proxy requests. Defaults to `'/__clerk'`. Must be unique and not conflict with other routes in your application.


#### `OrganizationSyncOptions`

The `organizationSyncOptions` property on the [`clerkMiddleware()`](#clerk-middleware-options) options
object has the type `OrganizationSyncOptions`, which has the following properties:

- **`organizationPatterns`** <code>[Pattern](#pattern)\[]</code>

  Specifies URL patterns that are Organization-specific, containing an Organization ID or slug as a path parameter. If a request matches this path, the Organization identifier will be used to set that Organization as active.

    If the route also matches the `personalAccountPatterns` prop, this prop takes precedence.

    Patterns must have a path parameter named either `:id` (to match a Clerk Organization ID) or `:slug` (to match a Clerk Organization slug).

    > [!WARNING]
    > If the Organization can't be activated—either because it doesn't exist or the user lacks access—the previously Active Organization will remain unchanged. Components must detect this case and provide an appropriate error and/or resolution pathway, such as calling `notFound()` or displaying an [``](/reference/components/organization/organization-switcher).

    Common examples:

- **`["/orgs/:slug", "/orgs/:slug/(.*)"]`** `["/orgs/:id", "/orgs/:id/(.*)"]` `["/app/:any/orgs/:slug", "/app/:any/orgs/:slug/(.*)"]`

  ---

- **`personalAccountPatterns`** <code>[Pattern](#pattern)\[]</code>

  URL patterns for resources that exist within the context of a user's Personal Account.

    If the route also matches the `organizationPattern` prop, the `organizationPattern` prop takes precedence.

    Common examples:

- **`["/me", "/me/(.*)"]`** `["/user/:any", "/user/:any/(.*)"]`


### Pattern

A `Pattern` is a `string` that represents the structure of a URL path. In addition to any valid URL, it may include:

- Named path parameters prefixed with a colon (e.g., `:id`, `:slug`, `:any`).
- Wildcard token, `(.*)`, which matches the remainder of the path.

#### Examples

- `/orgs/:slug`

| URL | Matches | `:slug` value |
| - | - | - |
| `/orgs/acmecorp` | ✅ | `acmecorp` |
| `/orgs` | ❌ | n/a |
| `/orgs/acmecorp/settings` | ❌ | n/a |

- `/app/:any/orgs/:id`

| URL | Matches | `:id` value |
| - | - | - |
| `/app/petstore/orgs/org_123` | ✅ | `org_123` |
| `/app/dogstore/v2/orgs/org_123` | ❌ | n/a |

- `/personal-account/(.*)`

| URL | Matches |
| - | - |
| `/personal-account/settings` | ✅ |
| `/personal-account` | ❌ |
