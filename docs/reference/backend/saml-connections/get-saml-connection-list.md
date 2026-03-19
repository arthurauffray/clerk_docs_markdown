# getSamlConnectionList()


> Use Clerk's JS Backend SDK to retrieve the list of SAML connections for an instance.

Retrieves the list of SAML connections for an instance. Returns a [`PaginatedResourceResponse`](/reference/backend/types/paginated-resource-response) object with a `data` property that contains an array of [`SamlConnection`](/reference/backend/types/backend-saml-connection) objects, and a `totalCount` property that indicates the total number of SAML connections for the instance.

```ts
function getSamlConnectionList(params: SamlConnectionListParams = {}): Promise
```

## `SamlConnectionListParams`

- **`limit?`** `number`

  The number of results to return. Must be an integer greater than zero and less than 501. Default: `10`

    ---

- **`offset?`** `number`

  The number of results to skip. Default: `0`


## Examples

### Basic

> [!NOTE]
> Using `clerkClient` varies based on your framework. Refer to the [JS Backend SDK overview](/js-backend/getting-started/quickstart) for usage details, including guidance on [how to access the `userId` and other properties](/js-backend/getting-started/quickstart#get-the-user-id-and-other-properties).


```tsx
const response = await clerkClient.samlConnections.getSamlConnectionList()
```

### Limit the number of results

Retrieves Organization list that is filtered by the number of results.

```tsx
const { data, totalCount } = await clerkClient.samlConnections.getSamlConnectionList({
  // returns the first 10 results
  limit: 10,
})
```

### Skip results

Retrieves Organization list that is filtered by the number of results to skip.

```tsx
const { data, totalCount } = await clerkClient.samlConnections.getSamlConnectionList({
  // skips the first 10 results
  offset: 10,
})
```

## Backend API (BAPI) endpoint

This method in the SDK is a wrapper around the BAPI endpoint `GET/saml_connections`. See the [BAPI reference](/reference/backend-api/tag/saml-connections/get/saml_connections) for more information.
