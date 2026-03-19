# getSamlConnection()


> Use Clerk's JS Backend SDK to retrieve a SAML connection.

Retrieves a [`SamlConnection`](/reference/backend/types/backend-saml-connection) by its ID.

```ts
function getSamlConnection(samlConnectionId: string): Promise
```

## `GetOrganizationParams`

- **`samlConnectionId`** `string`

  The ID of the SAML connection to retrieve.


## Example

> [!NOTE]
> Using `clerkClient` varies based on your framework. Refer to the [JS Backend SDK overview](/js-backend/getting-started/quickstart) for usage details, including guidance on [how to access the `userId` and other properties](/js-backend/getting-started/quickstart#get-the-user-id-and-other-properties).


```tsx
const samlConnectionId = 'samlc_123'

const response = await clerkClient.samlConnections.getSamlConnection(samlConnectionId)
```

## Backend API (BAPI) endpoint

This method in the SDK is a wrapper around the BAPI endpoint `GET/saml_connections/{saml_connection_id}`. See the [BAPI reference](/reference/backend-api/tag/saml-connections/get/saml_connections/\{saml_connection_id}) for more information.
