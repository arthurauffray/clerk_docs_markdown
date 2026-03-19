# getClient()


> Use Clerk's JS Backend SDK to retrieve a single client by its ID.

Retrieves a single [`Client`](/reference/javascript/client).

```ts
function getClient(clientId: string): Promise
```

## Parameters

- **`clientId`** `string`

  The ID of the client to retrieve.


## Example

> [!NOTE]
> Using `clerkClient` varies based on your framework. Refer to the [JS Backend SDK overview](/js-backend/getting-started/quickstart) for usage details, including guidance on [how to access the `userId` and other properties](/js-backend/getting-started/quickstart#get-the-user-id-and-other-properties).


```tsx
const clientId = 'client_123'

const response = await clerkClient.clients.getClient(clientId)
```

## Backend API (BAPI) endpoint

This method in the SDK is a wrapper around the BAPI endpoint `GET/clients/{client_id}`. See the [BAPI reference](/reference/backend-api/tag/clients/get/clients/\{client_id}) for more information.
