# deleteUserPasskey()


> Use Clerk's JS Backend SDK to delete the passkey identification for a given user.

Deletes the passkey identification for a given user and notifies them through email. Returns a [`DeletedObjectResource`](/reference/javascript/types/deleted-object-resource).

```ts
function deleteUserPasskey(params: DeleteUserPasskeyParams): Promise
```

## `DeleteUserPasskeyParams`

- **`userId`** `string`

  The ID of the user that owns the passkey identity.

    ---

- **`passkeyIdentificationId`** `string`

  The ID of the passkey identity to be deleted.


## Example

> [!NOTE]
> Using `clerkClient` varies based on your framework. Refer to the [JS Backend SDK overview](/js-backend/getting-started/quickstart) for usage details, including guidance on [how to access the `userId` and other properties](/js-backend/getting-started/quickstart#get-the-user-id-and-other-properties).


```tsx
const userId = 'user_123'
const passkeyIdentificationId = 'passkey_identification_123'

const response = await clerkClient.users.deleteUserPasskey({
  userId,
  passkeyIdentificationId,
})
```

## Backend API (BAPI) endpoint

This method in the SDK is a wrapper around the BAPI endpoint `DELETE/users/{user_id}/passkeys/{passkey_identification_id}`. See the [BAPI reference](/reference/backend-api/tag/users/delete/users/%7Buser_id%7D/passkeys/%7Bpasskey_identification_id%7D) for more information.
