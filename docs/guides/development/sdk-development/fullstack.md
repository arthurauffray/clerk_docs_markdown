# Fullstack SDK


> A reference for implementing a fullstack Clerk SDK

A fullstack SDK combines the [frontend-only SDK](/guides/development/sdk-development/frontend-only) and [backend-only SDK](/guides/development/sdk-development/backend-only) into one. A fullstack SDK is necessary for frameworks that support multiple rendering strategies (SSR, SSG, etc.), middleware, data fetching, and more. Examples of such frameworks would be Next.js or Rails.

## Expected features

- User only needs to provide their Publishable Key and Secret Key
- User only needs to adjust one or two files to add Clerk to their app (e.g. adding Clerk to the configuration file of that framework)
- User can use [Clerk’s components](/reference/components/overview) in their choice of framework (e.g. in a React-based framework you import these components as React components)
- Give users access to [`Client`](/reference/javascript/client), [`Session`](/reference/javascript/session), [`User`](/reference/javascript/user), and [`Organization`](/reference/javascript/organization) properties through the framework’s choice of state management
- User should be able to use [ClerkJS options](/reference/javascript/clerk#clerk-options)
- Centralized request authentication (e.g. in a middleware or plugin)
- Give access to the instance of [BAPI](/guides/development/sdk-development/terminology) client (so that users can use all methods)
- User should be able to limit access to routes by checking for [Roles and Permissions](/guides/organizations/control-access/roles-and-permissions)

## Optional features

- User should be able to enforce authentication on individual routes (e.g. with a [`requireAuth`](/guides/development/sdk-development/backend-only#create-a-require-auth-helper) helper)
- Use singleton pattern to only create a pre-configured instance of Clerk backend client

## Implementation

See the respective [frontend-only SDK](/guides/development/sdk-development/frontend-only) and [backend-only SDK](/guides/development/sdk-development/backend-only) implementation instructions.

In addition to these instructions, you'll need to go through the following steps to support all required features.

> [!NOTE]
> If you're looking for a real-world example, have a look at [`@clerk/nextjs`](https://github.com/clerk/javascript/tree/main/packages/nextjs).


  ### Add handshake support

  Inside your Clerk middleware, add checks for the `headers` on the `requestState`. Apply these headers to the `Response` and handle any existing `location` headers (e.g. redirects).

  ```ts
// Filename: clerk-middleware.ts

  import { clerkClient as defaultClerkClient } from './client.ts'

  const clerkMiddleware = (options) => {
    return async (context, next) => {
      const clerkClient = options.clerkClient || defaultClerkClient

      const requestState = await clerkClient.authenticateRequest(context.req, {
        authorizedParties: ['https://example.com'],
      })

      if (requestState.headers) {
        // This adds observability headers to the res
        requestState.headers.forEach((value, key) => context.res.headers.append(key, value))

        const locationHeader = requestState.headers.get('location')

        if (locationHeader) {
          return context.redirect(locationHeader, 307)
        } else if (requestState.status === 'handshake') {
          throw new Error('Clerk: unexpected handshake without redirect')
        }
      }

      context.set('clerkAuth', requestState.toAuth())
      context.set('clerk', clerkClient)

      await next()
    }
  }
  ```
