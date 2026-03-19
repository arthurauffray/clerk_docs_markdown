# updateOrganizationMembership()


> Use Clerk's JS Backend SDK to update a user's Organization membership.

Updates a user's [`OrganizationMembership`](/reference/backend/types/backend-organization-membership). Currently, only the role can be updated.

```ts
function updateOrganizationMembership(
  params: UpdateOrganizationMembershipParams,
): Promise
```

## `UpdateOrganizationMembershipParams`

- **`organizationId`** `string`

  The ID of the Organization this membership belongs to.

    ---

- **`userId`** `string`

  The ID of the user that this membership belongs to.

    ---

- **`role`** `string`

  The [Role](/guides/organizations/control-access/roles-and-permissions) to assign the user.


## Example

> [!NOTE]
> Using `clerkClient` varies based on your framework. Refer to the [JS Backend SDK overview](/js-backend/getting-started/quickstart) for usage details, including guidance on [how to access the `userId` and other properties](/js-backend/getting-started/quickstart#get-the-user-id-and-other-properties).


```tsx

const organizationId = 'org_123'

const userId = 'user_123'

const role = 'org:admin'

const response = await clerkClient.organizations.updateOrganizationMembership({
  organizationId,
  userId,
  role,
})
```

## Backend API (BAPI) endpoint

This method in the SDK is a wrapper around the BAPI endpoint `PATCH/organizations/{organization_id}/memberships/{user_id}`. See the [BAPI reference](/reference/backend-api/tag/organization-memberships/patch/organizations/\{organization_id}/memberships/\{user_id}) for more information.
