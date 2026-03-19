# getUser()


> Use Clerk's JS Backend SDK to retrieve a single user by their ID.

Retrieves a single [`User`](/reference/backend/types/backend-user) by their ID, if the ID is valid.

```ts
function getUser(userId: string): Promise
```

## Parameters

- **`userId`** `string`

  The ID of the user to retrieve.


## Example

> [!NOTE]
> Using `clerkClient` varies based on your framework. Refer to the [JS Backend SDK overview](/js-backend/getting-started/quickstart) for usage details, including guidance on [how to access the `userId` and other properties](/js-backend/getting-started/quickstart#get-the-user-id-and-other-properties).


```tsx
const userId = 'user_123'

const response = await clerkClient.users.getUser(userId)
```

## Backend API (BAPI) endpoint

This method in the SDK is a wrapper around the BAPI endpoint `GET/users/{user_id}`. See the [BAPI reference](/reference/backend-api/tag/users/get/users/\{user_id}) for more information.
