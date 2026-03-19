# revokeToken()


> Use Clerk's JS Backend SDK to revoke a M2M token.

Revokes an [M2M token](/guides/development/machine-auth/m2m-tokens). This endpoint can be authenticated by either a Machine Secret Key or by a Clerk Secret Key.

- When revoking a M2M token with a Machine Secret Key, the token must be managed by the Machine associated with the Machine Secret Key.
- When revoking a M2M token with a Clerk Secret Key, any token on the instance can be revoked.

> [!IMPORTANT]
> Only opaque tokens can be revoked. JWT tokens are not stored by Clerk and therefore cannot be revoked. If you need revocation capability, use the default opaque token format when creating tokens.

```ts
function revokeToken(params: RevokeM2MTokenParams): Promise
```

## `RevokeM2MTokenParams`

- **`machineSecretKey?`** `string`

  Custom machine secret key for authentication. If not provided, the SDK will use the value from the environment variable.

    ---

- **`m2mTokenId`** `string`

  The ID of the M2M token to revoke.

    ---

- **`revocationReason?`** `string | null`

  Optional reason for revocation. Useful for your records.


## Example

> [!NOTE]
> Using `clerkClient` varies based on your framework. Refer to the [JS Backend SDK overview](/js-backend/getting-started/quickstart) for usage details, including guidance on [how to access the `userId` and other properties](/js-backend/getting-started/quickstart#get-the-user-id-and-other-properties).


```ts
const response = await clerkClient.m2m.revokeToken({ m2mTokenId })
```

## Backend API (BAPI) endpoint

This method in the SDK is a wrapper around the BAPI endpoint `POST/m2m_tokens/{m2m_token_id}/revoke`. See the [BAPI reference](/reference/backend-api/tag/m2m-tokens/post/m2m_tokens/%7Bm2m_token_id%7D/revoke) for more information.
