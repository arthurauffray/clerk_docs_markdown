# unbanUser()


> Use Clerk's JS Backend SDK to remove the ban mark from a user.

Removes the ban mark from the given [`User`](/reference/backend/types/backend-user).

```ts
function unbanUser(userId: string): Promise
```

## Parameters

- **`userId`** `string`

  The ID of the user to unban.


## Example

> [!NOTE]
> Using `clerkClient` varies based on your framework. Refer to the [JS Backend SDK overview](/js-backend/getting-started/quickstart) for usage details, including guidance on [how to access the `userId` and other properties](/js-backend/getting-started/quickstart#get-the-user-id-and-other-properties).


```tsx
const userId = 'user_123'

const response = await clerkClient.users.unbanUser(userId)
```

## Backend API (BAPI) endpoint

This method in the SDK is a wrapper around the BAPI endpoint `POST/users/{user_id}/unban`. See the [BAPI reference](/reference/backend-api/tag/users/post/users/\{user_id}/unban) for more information.
