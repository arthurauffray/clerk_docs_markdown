# revokeOrganizationInvitation()


> Use Clerk's JS Backend SDK to revoke an Organization invitation from a user for a specified Organization.

Revokes an [`OrganizationInvitation`](/reference/backend/types/backend-organization-invitation) from a user for the specified Organization.

```ts
function revokeOrganizationInvitation(
  params: RevokeOrganizationInvitationParams,
): Promise
```

## `RevokeOrganizationInvitationParams`

- **`organizationId`** `string`

  The ID of the Organization the user was invited to.

    ---

- **`invitationId`** `string`

  The ID of the invitation to be revoked.

    ---

- **`requestingUserId`** `string`

  The ID of the user revoking the Organization invitation.


## Example

> [!NOTE]
> Using `clerkClient` varies based on your framework. Refer to the [JS Backend SDK overview](/js-backend/getting-started/quickstart) for usage details, including guidance on [how to access the `userId` and other properties](/js-backend/getting-started/quickstart#get-the-user-id-and-other-properties).


```tsx

const organizationId = 'org_123'

const invitationId = 'orginv_123'

const requestingUserId = 'user_123'

const response = await clerkClient.organizations.revokeOrganizationInvitation({
  organizationId,
  invitationId,
  requestingUserId,
})
```

## Backend API (BAPI) endpoint

This method in the SDK is a wrapper around the BAPI endpoint `POST/organizations/{organization_id}/invitations/{invitation_id}/revoke`. See the [BAPI reference](/reference/backend-api/tag/organization-invitations/post/organizations/\{organization_id}/invitations/\{invitation_id}/revoke) for more information.
