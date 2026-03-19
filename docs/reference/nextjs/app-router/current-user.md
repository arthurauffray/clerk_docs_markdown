# currentUser()


> Use the currentUser() helper to access information about your user inside of your Server Components, Route Handlers, and Server Actions.

> [!WARNING]
> For optimal performance and to avoid rate limiting, it's recommended to use the [`useUser()`](/reference/hooks/use-user) hook on the client-side when possible. Only use `currentUser()` when you specifically need user data in a server context.

The `currentUser()` helper returns the [`Backend User`](/reference/backend/types/backend-user) object of the currently active user. It can be used in Server Components, Route Handlers, and Server Actions.

Under the hood, this helper:

- calls `fetch()`, so it is automatically deduped per request.
- uses the [`GET /v1/users/{user_id}`](/reference/backend-api/tag/users/get/users/\{user_id}) endpoint.
- counts towards the [Backend API request rate limit](/guides/how-clerk-works/system-limits).

> [!WARNING]
> The [`Backend User`](/reference/backend/types/backend-user) object includes a `privateMetadata` field that should not be exposed to the frontend. Avoid passing the full user object returned by `currentUser()` to the frontend. Instead, pass only the specified fields you need.


```tsx
// Filename: app/page.tsx

import { currentUser } from '@clerk/nextjs/server'

export default async function Page() {
  const user = await currentUser()

  if (!user) return <div>Not signed in</div>

  return <div>Hello {user?.firstName}</div>
}
```
