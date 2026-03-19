# deleteUserBackupCodes()


> Use Clerk's JS Backend SDK to delete all of a user's backup codes.

Deletes all of a user's backup codes.

```ts
function deleteUserBackupCodes(userId: string): Promise
```

## Example

> [!NOTE]
> Using `clerkClient` varies based on your framework. Refer to the [JS Backend SDK overview](/js-backend/getting-started/quickstart) for usage details, including guidance on [how to access the `userId` and other properties](/js-backend/getting-started/quickstart#get-the-user-id-and-other-properties).


```tsx
const userId = 'user_123'

const response = await clerkClient.users.deleteUserBackupCodes(userId)
```

## Backend API (BAPI) endpoint

This method in the SDK is a wrapper around the BAPI endpoint `DELETE/users/{user_id}/backup_code`. See the [BAPI reference](/reference/backend-api/tag/users/delete/users/%7Buser_id%7D/backup_code) for more information.
