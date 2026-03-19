# deleteOrganizationLogo()


> Use Clerk's JS Backend SDK to delete an Organization's logo.

Deletes an Organization's logo.

```ts
function deleteOrganizationLogo(organizationId: string): Promise
```

## Parameters

- **`organizationId`** `string`

  The ID of the Organization for which the logo will be deleted.


## Example

> [!NOTE]
> Using `clerkClient` varies based on your framework. Refer to the [JS Backend SDK overview](/js-backend/getting-started/quickstart) for usage details, including guidance on [how to access the `userId` and other properties](/js-backend/getting-started/quickstart#get-the-user-id-and-other-properties).


```tsx
const organizationId = 'org_123'

const response = await clerkClient.organizations.deleteOrganizationLogo(organizationId)

console.log(response)
```

## Backend API (BAPI) endpoint

This method in the SDK is a wrapper around the BAPI endpoint `DELETE/organizations/{organization_id}/logo`. See the [BAPI reference](/reference/backend-api/tag/organizations/delete/organizations/\{organization_id}/logo) for more information.
