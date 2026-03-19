# deleteAllowlistIdentifier()


> Use Clerk's JS Backend SDK to delete an allowlist identifier.

Deletes an [`AllowlistIdentifier`](/reference/backend/types/backend-allowlist-identifier).

```ts
function deleteAllowlistIdentifier(allowlistIdentifierId: string): Promise
```

## Parameters

- **`allowlistIdentifierId`** `string`

  The ID of the allowlist identifier to delete.


## Example

> [!NOTE]
> Using `clerkClient` varies based on your framework. Refer to the [JS Backend SDK overview](/js-backend/getting-started/quickstart) for usage details, including guidance on [how to access the `userId` and other properties](/js-backend/getting-started/quickstart#get-the-user-id-and-other-properties).


```tsx
const allowlistIdentifierId = 'alid_123'

const response =
  await clerkClient.allowlistIdentifiers.deleteAllowlistIdentifier(allowlistIdentifierId)
```

## Backend API (BAPI) endpoint

This method in the SDK is a wrapper around the BAPI endpoint `DELETE/allowlist-identifiers/{identifier_id}`. See the [BAPI reference](/reference/backend-api/tag/allow-list-block-list/delete/allowlist_identifiers/\{identifier_id}) for more information.
