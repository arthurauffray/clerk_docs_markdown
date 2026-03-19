# verify()


> Use Clerk's JS Backend SDK to verify an M2M token.

Verifies an [M2M token](/guides/development/machine-auth/m2m-tokens). Must be authenticated via a Machine Secret Key.

> [!NOTE]
> JWT tokens are not stored by Clerk, so they cannot be fetched via the **list** endpoint (`clerkClient.m2m.list()`). The list endpoint will only return opaque tokens. Additionally, since JWT verification happens client-side, Clerk cannot track `last_used_at` for JWT tokens.


```ts
function verify(params: VerifyM2MTokenParams): Promise
```

## `VerifyM2MTokenParams`

- **`machineSecretKey?`** `string`

  Custom machine secret key for authentication. If not provided, the SDK will use the value from the environment variable.

    ---

- **`token`** `string`

  The M2M token to verify.


## Example

> [!NOTE]
> Using `clerkClient` varies based on your framework. Refer to the [JS Backend SDK overview](/js-backend/getting-started/quickstart) for usage details, including guidance on [how to access the `userId` and other properties](/js-backend/getting-started/quickstart#get-the-user-id-and-other-properties).


```ts
const response = await clerkClient.m2m.verify({ token })
```

## Backend API (BAPI) endpoint

This method in the SDK is a wrapper around the BAPI endpoint `POST/m2m_tokens/verify`. See the [BAPI reference](/reference/backend-api/tag/m2m-tokens/post/m2m_tokens/verify) for more information.
