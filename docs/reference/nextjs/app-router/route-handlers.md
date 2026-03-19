# Route Handlers


> Learn how to use Clerk with your Route Handlers.

Clerk provides helpers that allow you to protect your Route Handlers, fetch the current user, and interact with the Clerk Backend API.

> [!TIP]
> If you have a `` tag on a public page that points to a protected page that returns a `400`-level error, like a `401`, the data prefetch will fail because it will be redirected to the sign-in page and throw a confusing error in the console. To prevent this behavior, disable prefetching by adding `prefetch={false}` to the `` component.


## Protect your Route Handlers

If you aren't protecting your Route Handler using [`clerkMiddleware()`](/reference/nextjs/clerk-middleware), you can protect your Route Handler in two ways:

- Use [`auth.protect()`](/reference/nextjs/app-router/auth#auth-protect) if you want Clerk to return a `404` error when there is no signed in user.
- Use [`auth().userId`](/reference/nextjs/app-router/auth#protect-pages-and-routes) if you want to customize the behavior or error message.


**auth.protect():**

```tsx
// Filename: app/api/route.ts

  import { auth } from '@clerk/nextjs/server'

  export async function GET() {
    // If there is no signed in user, this will return a 404 error
    await auth.protect()

    // Add your Route Handler logic here

    return Response.json({ message: 'Hello world!' })
  }
  ```


**auth().userId():**

```tsx
// Filename: app/api/route.ts

  import { auth } from '@clerk/nextjs/server'
  import { NextResponse } from 'next/server'

  export async function GET() {
    const { isAuthenticated, userId } = await auth()

    if (!isAuthenticated) {
      return NextResponse.json({ error: 'Error: No signed in user' }, { status: 401 })
    }

    // Add your Route Handler logic here

    return NextResponse.json({ userId })
  }
  ```


## Retrieve data from external sources

Clerk provides integrations with a number of popular databases.

The following example demonstrates how to use [`auth().getToken()`](/reference/backend/types/auth-object#get-token) to retrieve a token from a JWT template and use it to fetch data from the external source.

```ts
// Filename: app/api/route.ts

import { NextResponse } from 'next/server'
import { auth } from '@clerk/nextjs/server'
export async function GET() {
  const { isAuthenticated, getToken } = await auth()

  if (!isAuthenticated) {
    return new Response('Unauthorized', { status: 401 })
  }

  const token = await getToken({ template: 'supabase' })

  // Fetch data from Supabase and return it.
  const data = { supabaseData: 'Hello World' }

  return NextResponse.json({ data })
}
```

## Retrieve the current user

To retrieve information about the current user in your Route Handler, you can use the [`currentUser()`](/reference/nextjs/app-router/current-user) helper, which returns the [`Backend User`](/reference/backend/types/backend-user) object of the currently active user. **It does count towards the [Backend API request rate limit](/guides/how-clerk-works/system-limits)** so it's recommended to use the [`useUser()`](/reference/hooks/use-user) hook on the client side when possible and only use `currentUser()` when you specifically need user data in a server context. For more information on this helper, see the [`currentUser()`](/reference/nextjs/app-router/current-user) reference.

> [!WARNING]
> The [`Backend User`](/reference/backend/types/backend-user) object includes a `privateMetadata` field that should not be exposed to the frontend. Avoid passing the full user object returned by `currentUser()` to the frontend. Instead, pass only the specified fields you need.


```ts
// Filename: app/api/route.ts

import { NextResponse } from 'next/server'
import { currentUser } from '@clerk/nextjs/server'
export async function GET() {
  const { isAuthenticated } = await auth()
  const user = await currentUser()

  if (!isAuthenticated) {
    return new Response('Unauthorized', { status: 401 })
  }

  return NextResponse.json({ userId: user.id, email: user.emailAddresses[0].emailAddress })
}
```

## Interact with Clerk's Backend API

The [JS Backend SDK](/js-backend/getting-started/quickstart) exposes the [Backend API](/reference/backend-api) resources and low-level authentication utilities for JavaScript environments.

`clerkClient` exposes an instance of the JS Backend SDK for use in server environments.

```ts
// Filename: app/api/route.ts

import { NextResponse, NextRequest } from 'next/server'
import { auth, clerkClient } from '@clerk/nextjs/server'

export async function POST(req: NextRequest) {
  const { isAuthenticated, userId } = await auth()

  if (!isAuthenticated) return NextResponse.redirect(new URL('/sign-in', req.url))

  const params = { firstName: 'John', lastName: 'Wick' }

  const client = await clerkClient()

  const user = await client.users.updateUser(userId, params)

  return NextResponse.json({ user })
}
```
