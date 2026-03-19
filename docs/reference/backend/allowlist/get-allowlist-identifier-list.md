# getAllowlistIdentifierList()


> Use Clerk's JS Backend SDK to retrieve a list of allowlist identifiers.

Retrieves the list of all allowlist identifiers. Returns a [`PaginatedResourceResponse`](/reference/backend/types/paginated-resource-response) object with a `data` property that contains an array of [`AllowlistIdentifier`](/reference/backend/types/backend-allowlist-identifier) objects, and a `totalCount` property that indicates the total number of allowlist identifiers in the system.

```ts
function getAllowlistIdentifierList(): Promise>
```

## Example

> [!NOTE]
> Using `clerkClient` varies based on your framework. Refer to the [JS Backend SDK overview](/js-backend/getting-started/quickstart) for usage details, including guidance on [how to access the `userId` and other properties](/js-backend/getting-started/quickstart#get-the-user-id-and-other-properties).


```tsx
const response = await clerkClient.allowlistIdentifiers.getAllowlistIdentifierList()
```

## Backend API (BAPI) endpoint

This method in the SDK is a wrapper around the BAPI endpoint `GET/allowlist-identifiers`. See the [BAPI reference](/reference/backend-api/tag/allow-list-block-list/get/allowlist_identifiers) for more information.
