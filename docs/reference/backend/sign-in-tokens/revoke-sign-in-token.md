# revokeSignInToken()


> Use Clerk's JS Backend SDK to revoke a pending sign-in token.

Revokes a pending sign-in token.

```ts
function revokeSignInToken(signInTokenId: string): Promise
```

## Parameters

- **`signInTokenId`** `string`

  The ID of the sign-in token to revoke.


## Example

> [!NOTE]
> Using `clerkClient` varies based on your framework. Refer to the [JS Backend SDK overview](/js-backend/getting-started/quickstart) for usage details, including guidance on [how to access the `userId` and other properties](/js-backend/getting-started/quickstart#get-the-user-id-and-other-properties).


```tsx
const signInTokenId = 'sit_123'

const response = await clerkClient.signInTokens.revokeSignInToken(signInTokenId)
```

## Backend API (BAPI) endpoint

This method in the SDK is a wrapper around the BAPI endpoint `POST/sign_in_tokens/{sign_in_token_id}/revoke`. See the [BAPI reference](/reference/backend-api/tag/sign-in-tokens/post/sign_in_tokens/\{sign_in_token_id}/revoke) for more information.
