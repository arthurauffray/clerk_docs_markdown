# get()


> Use Clerk's JS Backend SDK to retrieve an API key.

> [!WARNING]
> API keys is currently in beta. The API may change before general availability.


Retrieves a specific [API key](/guides/development/machine-auth/api-keys) by its ID. Returns an [`APIKey`](/reference/backend/types/backend-api-key) object.

```ts
function get(apiKeyId: string): Promise
```

## Parameters

- **`apiKeyId`** `string`

  The ID of the API key to retrieve.


## Example

> [!NOTE]
> Using `clerkClient` varies based on your framework. Refer to the [JS Backend SDK overview](/js-backend/getting-started/quickstart) for usage details, including guidance on [how to access the `userId` and other properties](/js-backend/getting-started/quickstart#get-the-user-id-and-other-properties).


```tsx
const apiKeyId = 'apikey_123'

const response = await clerkClient.apiKeys.get(apiKeyId)
```

## Backend API (BAPI) endpoint

This method in the SDK is a wrapper around the BAPI endpoint `GET/api_keys/{apiKeyId}`. See the [BAPI reference](/reference/backend-api/tag/api-keys/get/api_keys/%7BapiKeyID%7D) for more information.
