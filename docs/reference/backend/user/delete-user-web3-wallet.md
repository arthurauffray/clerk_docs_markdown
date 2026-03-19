# deleteUserWeb3Wallet()


> Use Clerk's JS Backend SDK to delete the Web3 wallet identification for a given user.

Deletes the Web3 wallet identification for a given user. Returns a [`DeletedObjectResource`](/reference/javascript/types/deleted-object-resource).

```ts
function deleteUserWeb3Wallet(params: DeleteWeb3WalletParams): Promise
```

## `DeleteWeb3WalletParams`

- **`userId`** `string`

  The ID of the user that owns the Web3 wallet identity.

    ---

- **`web3WalletIdentificationId`** `string`

  The ID of the Web3 wallet identity to be deleted.


## Example

> [!NOTE]
> Using `clerkClient` varies based on your framework. Refer to the [JS Backend SDK overview](/js-backend/getting-started/quickstart) for usage details, including guidance on [how to access the `userId` and other properties](/js-backend/getting-started/quickstart#get-the-user-id-and-other-properties).


```tsx
const userId = 'user_123'
const web3WalletIdentificationId = 'web3_wallet_identification_123'

const response = await clerkClient.users.deleteUserWeb3Wallet({
  userId,
  web3WalletIdentificationId,
})
```

## Backend API (BAPI) endpoint

This method in the SDK is a wrapper around the BAPI endpoint `DELETE/users/{user_id}/web3_wallets/{web3_wallet_identification_id}`. See the [BAPI reference](/reference/backend-api/tag/users/delete/users/%7Buser_id%7D/web3_wallets/%7Bweb3_wallet_identification_id%7D) for more information.
