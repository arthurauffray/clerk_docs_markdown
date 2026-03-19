# Clerk Astro SDK


> The Clerk Astro SDK gives you access to prebuilt components, stores, and helpers to make user authentication easier.

The Clerk Astro SDK gives you access to prebuilt components, stores, and helpers to make user authentication easier. Refer to the [quickstart guide](/astro/getting-started/quickstart) to get started.

## Integration

To configure Clerk with Astro, you must pass [the `clerk()` integration](/reference/astro/integration) to the `integrations` array in your `astro.config.mjs` file. See the [quickstart](/astro/getting-started/quickstart#update-astro-config-mjs) for more information on configuring the integration.

## `updateClerkOptions()`

The `updateClerkOptions()` function is used to update Clerk's options at runtime. It can be called at any time after [Clerk has been initialized](/reference/astro/integration). See the [reference documentation](/reference/astro/update-clerk-options) for more information.

## Client-side helpers

The Astro SDK provides [stores](https://github.com/nanostores/nanostores) that give you access to the [`Clerk`](/reference/javascript/clerk) object and helper methods for authentication flows.

- [`$authStore`](/reference/astro/client-side-helpers/auth-store)
- [`$clerkStore`](/reference/astro/client-side-helpers/clerk-store)
- [`$userStore`](/reference/astro/client-side-helpers/user-store)
- [`$signInStore`](/reference/astro/client-side-helpers/sign-in-store)
- [`$signUpStore`](/reference/astro/client-side-helpers/sign-up-store)
- [`$sessionStore`](/reference/astro/client-side-helpers/session-store)
- [`$sessionListStore`](/reference/astro/client-side-helpers/session-list-store)
- [`$organizationStore`](/reference/astro/client-side-helpers/organization-store)

## Server-side helpers

The following references show how to integrate Clerk features into your Astro app on the server-side.

### Locals

The Astro SDK provides access to Clerk's authentication data through [Astro's `locals`](https://docs.astro.build/en/guides/middleware/#storing-data-in-contextlocals) object. The following references show how to access authentication data in server-side code:

- [`Auth`](/reference/astro/locals#locals-auth)
- [`CurrentUser`](/reference/astro/locals#locals-current-user)

### `clerkMiddleware()`

The `clerkMiddleware()` helper integrates Clerk authentication and authorization into your Astro application through middleware. You can learn more [here](/reference/astro/clerk-middleware).

### `clerkClient()`

[Clerk's JS Backend SDK](/js-backend/getting-started/quickstart) is a wrapper around the [Backend API](/reference/backend-api) that makes it easier to interact with the API. For example, to retrieve a list of all users in your application, you can use the `users.getUserList()` method from the JS Backend SDK instead of manually making a fetch request to the `https://api.clerk.com/v1/users` endpoint.

To access a resource, you must first instantiate a `clerkClient` instance. See the [reference documentation](/js-backend/getting-started/quickstart) for more information.

### Example: Use `clerkClient` to get a user's information

The following example uses `clerkClient` to get information about the currently signed-in user. If the user is authenticated, their `userId` is passed to [`clerkClient.users.getUser()`](/reference/backend/user/get-user) to get the current user's [`User`](/reference/javascript/user) object. If not authenticated, the user is redirected to the sign-in page.

```tsx
import { clerkClient } from '@clerk/astro/server'

export async function GET(context) {
  const { isAuthenticated, userId, redirectToSignIn } = context.locals.auth()

  if (!isAuthenticated) {
    return redirectToSignIn()
  }

  const user = await clerkClient(context).users.getUser(userId)

  return new Response(JSON.stringify({ user }))
}
```
