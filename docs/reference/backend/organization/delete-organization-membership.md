# deleteOrganizationMembership()


> Use Clerk's JS Backend SDK to remove a user from the specified Organization.

Removes a user from the specified Organization. Returns a [`OrganizationMembership`](/reference/backend/types/backend-organization-membership) object.

```ts
function deleteOrganizationMembership(
  params: DeleteOrganizationMembershipParams,
): Promise
```

## `DeleteOrganizationMembershipParams`

- **`organizationId`** `string`

  The ID of the Organization the user will be removed from.

    ---

- **`userId`** `string`

  The ID of the user to be removed from the Organization.


## Example

> [!NOTE]
> Using `clerkClient` varies based on your framework. Refer to the [JS Backend SDK overview](/js-backend/getting-started/quickstart) for usage details, including guidance on [how to access the `userId` and other properties](/js-backend/getting-started/quickstart#get-the-user-id-and-other-properties).


```tsx
const organizationId = 'org_123'

const userId = 'user_123'

const response = await clerkClient.organizations.deleteOrganizationMembership({
  organizationId,
  userId,
})
```

## Backend API (BAPI) endpoint

This method in the SDK is a wrapper around the BAPI endpoint `DELETE/organizations/{organization_id}/memberships/{user_id}`. See the [BAPI reference](/reference/backend-api/tag/organization-memberships/delete/organizations/\{organization_id}/memberships/\{user_id}) for more information.
