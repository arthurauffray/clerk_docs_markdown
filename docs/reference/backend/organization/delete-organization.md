# deleteOrganization()


> Use Clerk's JS Backend SDK to delete an Organization.

Deletes an [`Organization`](/reference/backend/types/backend-organization). Returns a [`DeletedObjectResource`](/reference/javascript/types/deleted-object-resource) object.

```ts
function deleteOrganization(organizationId: string): Promise
```

## Parameters

- **`organizationId`** `string`

  The ID of the Organization to delete.


## Example

> [!NOTE]
> Using `clerkClient` varies based on your framework. Refer to the [JS Backend SDK overview](/js-backend/getting-started/quickstart) for usage details, including guidance on [how to access the `userId` and other properties](/js-backend/getting-started/quickstart#get-the-user-id-and-other-properties).


```tsx
const organizationId = 'org_123'

const response = await clerkClient.organizations.deleteOrganization(organizationId)
```

## Backend API (BAPI) endpoint

This method in the SDK is a wrapper around the BAPI endpoint `DELETE/organizations/{organization_id}`. See the [BAPI reference](/reference/backend-api/tag/organizations/delete/organizations/\{organization_id}) for more information.
