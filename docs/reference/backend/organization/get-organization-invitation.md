# getOrganizationInvitation()


> Use Clerk's JS Backend SDK to retrieve an Organization invitation.

Retrieves an [`OrganizationInvitation`](/reference/backend/types/backend-organization-invitation).

```ts
function getOrganizationInvitation(
  params: GetOrganizationInvitationParams,
): Promise
```

## `GetOrganizationInvitationParams`

- **`organizationId`** `string`

  The ID of the Organization that the invitation is for.

    ---

- **`invitationId`** `string`

  The ID of the invitation to retrieve.


## Example

> [!NOTE]
> Using `clerkClient` varies based on your framework. Refer to the [JS Backend SDK overview](/js-backend/getting-started/quickstart) for usage details, including guidance on [how to access the `userId` and other properties](/js-backend/getting-started/quickstart#get-the-user-id-and-other-properties).


```tsx
const organizationId = 'org_123'

const invitationId = 'orginv_123'

const response = await clerkClient.organizations.getOrganizationInvitation({
  organizationId,
  invitationId,
})
```

## Backend API (BAPI) endpoint

This method in the SDK is a wrapper around the BAPI endpoint `GET/organizations/{organization_id}/invitations/{invitation_id}`. See the [BAPI reference](/reference/backend-api/tag/organization-invitations/get/organizations/\{organization_id}/invitations/\{invitation_id}) for more information.
