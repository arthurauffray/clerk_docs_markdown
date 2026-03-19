# banUser()


> Use Clerk's JS Backend SDK to mark a given user as banned.

Marks the given [`User`](/reference/backend/types/backend-user) as banned, which means that all their sessions are revoked and they are not allowed to sign in again.

```ts
function banUser(userId: string): Promise
```

## Parameters

- **`userId`** `string`

  The ID of the user to ban.


## Example

> [!NOTE]
> Using `clerkClient` varies based on your framework. Refer to the [JS Backend SDK overview](/js-backend/getting-started/quickstart) for usage details, including guidance on [how to access the `userId` and other properties](/js-backend/getting-started/quickstart#get-the-user-id-and-other-properties).


```tsx
const userId = 'user_123'

const response = await clerkClient.users.banUser(userId)
```

## Backend API (BAPI) endpoint

This method in the SDK is a wrapper around the BAPI endpoint `POST/users/{user_id}/ban`. See the [BAPI reference](/reference/backend-api/tag/users/post/users/\{user_id}/ban) for more information.
