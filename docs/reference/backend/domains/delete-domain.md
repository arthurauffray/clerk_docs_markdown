# deleteDomain()


> Use Clerk's JS Backend SDK to delete a satellite domain for the instance.

Deletes a satellite domain for the instance. It is currently not possible to delete the instance's primary domain. Returns a [`DeletedObjectResource`](/reference/javascript/types/deleted-object-resource).

```ts
function deleteDomain(id: string): Promise
```

## Parameters

- **`id`** `string`

  The ID of the domain that will be deleted. Must be a satellite domain.


## Example

> [!NOTE]
> Using `clerkClient` varies based on your framework. Refer to the [JS Backend SDK overview](/js-backend/getting-started/quickstart) for usage details, including guidance on [how to access the `userId` and other properties](/js-backend/getting-started/quickstart#get-the-user-id-and-other-properties).


```tsx
const id = 'test_123'

const response = await clerkClient.users.deleteDomain(id)
```

## Backend API (BAPI) endpoint

This method in the SDK is a wrapper around the BAPI endpoint `DELETE/domains/{domain_id}`. See the [BAPI reference](/reference/backend-api/tag/domains/delete/domains/\{domain_id}) for more information.
