# verify()


> Use Clerk's JS Backend SDK to verify an API key secret.

> [!WARNING]
> API keys is currently in beta. The API may change before general availability.


Verifies an [API key](/guides/development/machine-auth/api-keys) secret. Returns an [`APIKey`](/reference/backend/types/backend-api-key) object.

- If the API key is valid, the method returns the API key object with its properties.
- If the API key is invalid, revoked, or expired, the method will throw an error.

> [!NOTE]
> In most cases, you'll want to verify API keys using framework-specific helpers like `auth()` in Next.js, which handles the verification automatically. See the [verifying API keys](/guides/development/verifying-api-keys) guide for more details.

```ts
function verify(secret: string): Promise
```

## Parameters

- **`secret`** `string`

  The API key secret to verify.


## Example

> [!NOTE]
> Using `clerkClient` varies based on your framework. Refer to the [JS Backend SDK overview](/js-backend/getting-started/quickstart) for usage details, including guidance on [how to access the `userId` and other properties](/js-backend/getting-started/quickstart#get-the-user-id-and-other-properties).


```tsx
const apiKeySecret = 'ak_live_123'

const response = await clerkClient.apiKeys.verify(apiKeySecret)
```

## Backend API (BAPI) endpoint

This method in the SDK is a wrapper around the BAPI endpoint `POST/api_keys/verify`. See the [BAPI reference](/reference/backend-api/tag/api-keys/post/api_keys/verify) for more information.
