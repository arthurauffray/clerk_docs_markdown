# deleteUserExternalAccount()


> Use Clerk's JS Backend SDK to delete a user's external account by ID.

Deletes a user's external account by ID. Returns a [`DeletedObjectResource`](/reference/javascript/types/deleted-object-resource).

```ts
function deleteUserExternalAccount(
  params: DeleteUserExternalAccountParams,
): Promise
```

## `DeleteUserExternalAccountParams`

- **`userId`** `string`

  The ID of the user to delete the external account for.

    ---

- **`externalAccountId`** `string`

  The ID of the external account to delete.


## Example

> [!NOTE]
> Using `clerkClient` varies based on your framework. Refer to the [JS Backend SDK overview](/js-backend/getting-started/quickstart) for usage details, including guidance on [how to access the `userId` and other properties](/js-backend/getting-started/quickstart#get-the-user-id-and-other-properties).


```tsx
const userId = 'user_123'
const externalAccountId = 'external_account_123'

const response = await clerkClient.users.deleteUserExternalAccount({
  userId,
  externalAccountId,
})
```

## Backend API (BAPI) endpoint

This method in the SDK is a wrapper around the BAPI endpoint `DELETE/users/{user_id}/external_accounts/{external_account_id}`. See the [BAPI reference](/reference/backend-api/tag/users/delete/users/%7Buser_id%7D/external_accounts/%7Bexternal_account_id%7D) for more information.
