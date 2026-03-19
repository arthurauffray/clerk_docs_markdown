# updateOrganizationMembershipMetadata()


> Use Clerk's JS Backend SDK to update the metadata associated with a user's Organization membership.

Update the metadata attributes of an [`OrganizationMembership`](/reference/backend/types/backend-organization-membership) by merging existing values with the provided parameters. Metadata values will be updated via a "deep" merge - "deep" means that any nested JSON objects will be merged as well. You can remove metadata keys at any level by setting their value to `null`.

```ts
function updateOrganizationMembershipMetadata(
  params: UpdateOrganizationMembershipMetadataParams,
): Promise
```

## `UpdateOrganizationMembershipMetadataParams`

- **`organizationId`** `string`

  The ID of the Organization this membership belongs to.

    ---

- **`userId`** `string`

  The ID of the user that this membership belongs to.

    ---

- **`publicMetadata?`** [`OrganizationMembershipPublicMetadata`](/reference/javascript/types/metadata#organization-membership-public-metadata)

  Metadata that can be read from both the Frontend API and [Backend API](/reference/backend-api), but can be set only from the Backend API.

    ---

- **`privateMetadata?`** [`OrganizationMembershipPrivateMetadata`](/reference/javascript/types/metadata#organization-membership-private-metadata)

  Metadata that is only visible to your [Backend API](/reference/backend-api).


## Example

> [!NOTE]
> Using `clerkClient` varies based on your framework. Refer to the [JS Backend SDK overview](/js-backend/getting-started/quickstart) for usage details, including guidance on [how to access the `userId` and other properties](/js-backend/getting-started/quickstart#get-the-user-id-and-other-properties).


```tsx

const organizationId = 'org_123'

const userId = 'user_123'

const response = await clerkClient.organizations.updateOrganizationMembershipMetadata({
  organizationId,
  userId,
  publicMetadata: {
    example: 'this value is updated!',
  },
})
```

## Backend API (BAPI) endpoint

This method in the SDK is a wrapper around the BAPI endpoint `PATCH/organizations/{organization_id}/memberships/{user_id}/metadata`. See the [BAPI reference](/reference/backend-api/tag/organization-memberships/patch/organizations/\{organization_id}/memberships/\{user_id}/metadata) for more information.
