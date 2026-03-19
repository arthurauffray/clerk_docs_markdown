# revoke()


> Use Clerk's JS Backend SDK to revoke an API key.

> [!WARNING]
> API keys is currently in beta. The API may change before general availability.


Revokes an [API key](/guides/development/machine-auth/api-keys) by its ID. This will immediately invalidate the API key and prevent it from being used to authenticate any future requests. Returns an [`APIKey`](/reference/backend/types/backend-api-key) object.

```ts
function revoke(params: RevokeAPIKeyParams): Promise
```

## `RevokeAPIKeyParams`

- **`apiKeyId`** `string`

  The ID of the API key to revoke.

    ---

- **`revocationReason?`** `string | null`

  Optional reason for revocation. Useful for your records.


## Example

> [!NOTE]
> Using `clerkClient` varies based on your framework. Refer to the [JS Backend SDK overview](/js-backend/getting-started/quickstart) for usage details, including guidance on [how to access the `userId` and other properties](/js-backend/getting-started/quickstart#get-the-user-id-and-other-properties).


### Revoke an API key

```tsx
const apiKeyId = 'apikey_123'

const response = await clerkClient.apiKeys.revoke({
  apiKeyId: apiKeyId,
})
```

### Revoke an API key with a reason

```tsx
const apiKeyId = 'apikey_123'

const response = await clerkClient.apiKeys.revoke({
  apiKeyId: apiKeyId,
  revocationReason: 'Key compromised',
})
```

> [!IMPORTANT]
> When you revoke an API key, it is immediately invalidated. Any requests using that API key will be rejected. Make sure to notify users or update your systems before revoking API keys that are in active use.

## Backend API (BAPI) endpoint

This method in the SDK is a wrapper around the BAPI endpoint `POST/api_keys/{apiKeyID}/revoke`. See the [BAPI reference](/reference/backend-api/tag/api-keys/post/api_keys/%7BapiKeyID%7D/revoke) for more information.
