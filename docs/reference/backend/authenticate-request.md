# authenticateRequest()


> Use Clerk's JS Backend SDK to verify a token passed from the frontend.

Authenticates a token passed from the frontend. Networkless if the `jwtKey` is provided. Otherwise, performs a network call to retrieve the JWKS from the [Backend API](/reference/backend-api/tag/jwks/get/jwks).

```ts
function authenticateRequest(
  request: Request,
  options: AuthenticateRequestOptions,
): Promise
```

## Parameters

- **`request`** `Request`

  `Request` object

    ---

- **`options?`** [`AuthenticateRequestOptions`](#authenticate-request-options)

  Optional options to configure the authentication.


## `AuthenticateRequestOptions`

It is recommended to set these options as [environment variables](/guides/development/clerk-environment-variables#api-and-sdk-configuration) where possible, and then pass them to the function. For example, you can set the `secretKey` option using the `CLERK_SECRET_KEY` environment variable, and then pass it to the function like this: `createClerkClient({ secretKey: process.env.CLERK_SECRET_KEY })`.

> [!WARNING]
> You must provide either `jwtKey` or `secretKey`.
>
> For better security, it's highly recommended to explicitly set the `authorizedParties` option when authorizing requests. The value should be a list of domains that are allowed to make requests to your application. Not setting this value can open your application to [CSRF attacks](https://owasp.org/www-community/attacks/csrf).

## Returns

- **`isAuthenticated`** `boolean`

  A boolean that indicates whether the incoming request is authenticated. Initially `false`, becomes `true` once the request is authenticated.

    ---

- **`isSignedIn` (deprecated)** `boolean`

  **Deprecated. Use `isAuthenticated` instead.** Indicates whether the incoming request is authenticated.

    ---

- **`status`** `'signed-in' | 'signed-out' | 'handshake'`

  The authentication state.

    ---

- **`reason`** `string | null`

  The error code or reason for the current state. When there is a signed-in user, the value will be `null`.

    ---

- **`message`** `string | null`

  The full error message or additional context. When there is a signed-in user, the value will be `null`.

    ---

- **`tokenType`** `'session_token' | 'oauth_token' | 'm2m_token' | 'api_key'`

  The type of token.

    ---

- **`token`** `string`

  The value of the token.

    ---

- **`headers`** [Headers](https://developer.mozilla.org/en-US/docs/Web/API/Headers)

  A `Headers` object containing debug or status headers.

    ---

- **`toAuth()`** `function`

  A function that returns the `Auth` object. This JavaScript object contains important information like the current user's session ID, user ID, and Organization ID. Learn more about the [`Auth` object](/reference/backend/types/auth-object).


## Examples


#### JS Backend SDK


If you are using the [JS Backend SDK](/js-backend/getting-started/quickstart) on its own, you need to provide the `secretKey` and `publishableKey` to `createClerkClient()` so that it is passed to `authenticateRequest()`. You can set these values as [environment variables](/guides/development/clerk-environment-variables#clerk-publishable-and-secret-keys) and then pass them to the function.

```tsx
import { createClerkClient } from '@clerk/backend'

export async function GET(req: Request) {
  const clerkClient = createClerkClient({
    secretKey: process.env.CLERK_SECRET_KEY,
    publishableKey: process.env.CLERK_PUBLISHABLE_KEY,
  })

  const { isAuthenticated } = await clerkClient.authenticateRequest(req, {
    authorizedParties: ['https://example.com'],
  })

  if (!isAuthenticated) {
    return Response.json({ status: 401 })
  }

  // Add logic to perform protected actions

  return Response.json({ message: 'This is a reply' })
}
```
  

#### With other Clerk SDKs


`authenticateRequest()` requires `publishableKey` to be set. If you are importing `clerkClient` from a higher-level SDK, such as Next.js, then `clerkClient` infers the `publishableKey` from your [environment variables](/guides/development/clerk-environment-variables#clerk-publishable-and-secret-keys). **The following example uses Next.js, but you can use the comments in the example to help you adapt it to other SDKs.**

```tsx
import { clerkClient } from '@clerk/nextjs/server'

// Initialize the JS Backend SDK
// This varies depending on the SDK you're using
// https://clerk.com/docs/js-backend/getting-started/quickstart
const client = await clerkClient()

export async function GET(req: Request) {
  // Use the `authenticateRequest()` method to verify the token
  const { isAuthenticated } = await client.authenticateRequest(req, {
    authorizedParties: ['https://example.com'],
  })

  // Protect the route from unauthenticated users
  if (!isAuthenticated) {
    return Response.json({ status: 401 })
  }

  // Add logic to perform protected actions

  return Response.json({ message: 'This is a reply' })
}
```
  

### Machine authentication

By default, `authenticateRequest()` will authenticate a session request. To authenticate a machine request, you need to set the `acceptsToken` option to a machine token type, such as `'api_key'`, `'oauth_token'` or `'m2m_token'`.


#### JS Backend SDK


```tsx
import { createClerkClient } from '@clerk/backend'

export async function GET(request: Request) {
  // Initialize the JS Backend SDK
  // This varies depending on the SDK you're using
  // https://clerk.com/docs/js-backend/getting-started/quickstart
  const clerkClient = createClerkClient({
    secretKey: process.env.CLERK_SECRET_KEY,
    publishableKey: process.env.CLERK_PUBLISHABLE_KEY,
  })

  // Use the `authenticateRequest()` method to verify the token
  const { isAuthenticated } = await clerkClient.authenticateRequest(request, {
    acceptsToken: 'oauth_token',
  })

  // Protect the route from unauthenticated users
  if (!isAuthenticated) {
    return Response.json({ status: 401 })
  }

  // Add logic to perform protected actions

  return Response.json({ message: 'This is a machine-to-machine reply' })
}
```
  

#### With other Clerk SDKs


**This example uses Next.js, but you can use the comments in the example to help you adapt it to other SDKs.**

```tsx
import { clerkClient } from '@clerk/nextjs/server'

// Initialize the JS Backend SDK
// This varies depending on the SDK you're using
// https://clerk.com/docs/js-backend/getting-started/quickstart
const client = await clerkClient()

export async function GET(req: Request) {
  // Use the `authenticateRequest()` method to verify the token
  const { isAuthenticated } = await client.authenticateRequest(request, {
    acceptsToken: 'oauth_token',
  })

  // Protect the route from unauthenticated users
  if (!isAuthenticated) {
    return Response.json({ status: 401 })
  }

  // Add logic to perform protected actions

  return Response.json({ message: 'This is a machine-to-machine reply' })
}
```
  

### Networkless token verification

The following example uses the `authenticateRequest()` method with the [JS Backend SDK](/js-backend/getting-started/quickstart) to verify the token passed by the frontend, and performs a networkless authentication by passing `jwtKey`. This will verify if the user is signed into the application or not.


#### Next.js


    ```tsx
// Filename: app/api/example/route.ts

    import { clerkClient } from '@clerk/nextjs/server'

    // Initialize the JS Backend SDK
    // This varies depending on the SDK you're using
    // https://clerk.com/docs/js-backend/getting-started/quickstart
    const client = await clerkClient()

    export async function GET(req: Request) {
      // Use the `authenticateRequest()` method to verify the token
      const { isAuthenticated } = await client.authenticateRequest(req, {
        authorizedParties: ['https://example.com'],
        jwtKey: process.env.CLERK_JWT_KEY,
      })

      // Protect the route from unauthenticated users
      if (!isAuthenticated) {
        return Response.json({ status: 401 })
      }

      // Add logic to perform protected actions

      return Response.json({ message: 'This is a reply' })
    }
    ```
  

#### Astro


    ```tsx
// Filename: src/api/example.ts

    import { clerkClient } from '@clerk/astro/server'
    import type { APIRoute } from 'astro'

    export const GET: APIRoute = async (context) => {
      // Use the `authenticateRequest()` method to verify the token
      const { isAuthenticated } = await clerkClient(context).authenticateRequest(context.request, {
        authorizedParties: ['https://example.com'],
        jwtKey: process.env.CLERK_JWT_KEY,
      })

      // Protect the route from unauthenticated users
      if (!isAuthenticated) {
        return Response.json({ status: 401 })
      }

      // Add logic to perform protected actions

      return Response.json({ message: 'This is a reply' })
    }
    ```
  

#### Express


    ```js
// Filename: index.js

    import { createClerkClient } from '@clerk/express'
    import express from 'express'

    const app = express()
    const clerkClient = createClerkClient({ secretKey: process.env.CLERK_SECRET_KEY })

    app.get('/user', async (req, res) => {
      const { isAuthenticated } = await clerkClient.authenticateRequest(req, {
        authorizedParties: ['https://example.com'],
        jwtKey: process.env.CLERK_JWT_KEY,
      })

      if (!isAuthenticated) {
        res.status(401).json({ error: 'User not authenticated' })
      }

      // Add logic to perform protected actions

      // Return the Backend User object
      res.json({ message: 'This is a reply' })
    })
    ```
  

#### JS Backend SDK


If you are using the [JS Backend SDK](/js-backend/getting-started/quickstart) on its own, you need to provide the `secretKey` and `publishableKey` to `createClerkClient()` so that it is passed to `authenticateRequest()`. You can set these values as [environment variables](/guides/development/clerk-environment-variables#clerk-publishable-and-secret-keys) and then pass them to the function.

```tsx
import { createClerkClient } from '@clerk/backend'

// Initialize the JS Backend SDK
// This varies depending on the SDK you're using
// https://clerk.com/docs/js-backend/getting-started/quickstart
const clerkClient = createClerkClient({
  secretKey: process.env.CLERK_SECRET_KEY,
  publishableKey: process.env.CLERK_PUBLISHABLE_KEY,
})

export async function GET(req: Request) {
  // Use the `authenticateRequest()` method to verify the token
  const { isAuthenticated } = await clerkClient.authenticateRequest(req, {
    authorizedParties: ['https://example.com'],
    jwtKey: process.env.CLERK_JWT_KEY,
  })

  // Protect the route from unauthenticated users
  if (!isAuthenticated) {
    return Response.json({ status: 401 })
  }

  // Add logic to perform protected actions

  return Response.json({ message: 'This is a reply' })
}
```
  

#### React Router


    ```tsx
// Filename: app/routes/example.tsx

    import { redirect } from 'react-router'
    import { clerkClient } from '@clerk/react-router/server'
    import type { Route } from './+types/example'

    export async function loader(args: Route.LoaderArgs) {
      // Use the `authenticateRequest()` method to verify the token
      const { isAuthenticated } = await clerkClient(args).authenticateRequest(args.request, {
        authorizedParties: ['https://example.com'],
        jwtKey: process.env.CLERK_JWT_KEY,
      })

      if (!isAuthenticated) {
        return redirect('/sign-in?redirect_url=' + args.request.url)
      }

      // Add logic to perform protected actions

      return Response.json({ message: 'This is a reply' })
    }
    ```
  

#### TanStack React Start


    ```tsx
// Filename: app/routes/api/example.tsx

    import { createFileRoute } from '@tanstack/react-router'
    import { clerkClient } from '@clerk/tanstack-react-start/server'

    export const ServerRoute = createFileRoute('/api/example')({
      server: {
        handlers: {
          GET: async ({ request }) => {
            // Use the `authenticateRequest()` method to verify the token
            const { isAuthenticated } = await clerkClient().authenticateRequest(request, {
              authorizedParties: ['https://example.com'],
              jwtKey: process.env.CLERK_JWT_KEY,
            })

            if (!isAuthenticated) {
              return Response.json({ status: 401 })
            }

            // Add logic to perform protected actions

            return Response.json({ message: 'This is a reply' })
          },
        },
      },
    })
    ```
