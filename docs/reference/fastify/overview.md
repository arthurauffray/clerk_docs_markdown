# Clerk Fastify SDK


> The Clerk Fastify SDK provides a powerful set of tools and utilities to seamlessly integrate authentication, user management, and Organization management into your Fastify application.

The Clerk Fastify SDK provides a powerful set of tools and utilities to seamlessly integrate authentication, user management, and Organization management into your Fastify application. Refer to the [quickstart guide](/fastify/getting-started/quickstart) to get started.

## `clerkPlugin()`

The `clerkPlugin()` function is required to integrate Clerk's authentication into your application. The function checks request cookies and headers for a session JWT. If valid, it attaches the [`Auth`](/reference/backend/types/auth-object) object to the `request` object under the `auth` key. See the [reference doc](/reference/fastify/clerk-plugin) for more information.

## `getAuth()`

The `getAuth()` helper retrieves the current user's authentication state from the `request` object. It returns the [`Auth` object](/reference/backend/types/auth-object), which includes helpful authentication information like the user's ID, session ID, and Organization ID. It's also useful for protecting routes. See the [reference doc](/reference/fastify/get-auth) for more information.
