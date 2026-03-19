# clerkMiddleware()` | React Router


> The clerkMiddleware() function allows you to protect your React Router application using middleware.

The `clerkMiddleware()` helper integrates Clerk authentication into your React Router application through middleware.

## Configure `clerkMiddleware()`

1. React Router middleware requires opting in via a future flag. Add the following to your `react-router.config.ts` file:

   ```ts
// Filename: react-router.config.ts

   import type { Config } from '@react-router/dev/config'

   export default {
     // ...

     future: {
       v8_middleware: true,
     },
   } satisfies Config
   ```

1. Export `clerkMiddleware()` from your root route file:

   ```tsx
// Filename: app/root.tsx

   import { clerkMiddleware } from '@clerk/react-router/server'
   import type { Route } from './+types/root'

   export const middleware: Route.MiddlewareFunction[] = [clerkMiddleware()]
   ```

## `clerkMiddleware()` options

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


### `OrganizationSyncOptions`

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
