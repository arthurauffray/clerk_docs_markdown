# createOrganizationInvitationBulk()


> Use Clerk's JS Backend SDK to create multiple invitations for new users to join an Organization.

Creates multiple [`OrganizationInvitation`](/reference/backend/types/backend-organization-invitation)s in bulk for new users to join an Organization.

> [!CAUTION]
>
> This endpoint is [rate limited](/guides/how-clerk-works/system-limits#backend-api-requests) to **50 requests per hour** per application instance.

```ts
function createOrganizationInvitationBulk(
  organizationId: string,
  params: CreateBulkOrganizationInvitationParams,
): Promise
```

## Parameters

`createOrganizationInvitationBulk()` accepts the following parameters:

- **`organizationId`** `string`

  The Organization ID of the Organization you want to invite users to.

    ---

- **`params`** [`CreateBulkOrganizationInvitationParams[]`](#create-bulk-organization-invitation-params)

  An array of objects, each representing a single invitation.


### `CreateBulkOrganizationInvitationParams`

- **`inviterUserId`** `string | null`

  The user ID of the user creating the invitation.

    ---

- **`emailAddress`** `string`

  The email address to send the invitation to.

    ---

- **`role`** [`OrganizationCustomRoleKey`](/reference/javascript/types/organization-custom-role-key)

  The [Role](/guides/organizations/control-access/roles-and-permissions) to assign the invited user within the Organization.

    ---

- **`redirectUrl?`** `string`

  The full URL or path where users will land once the Organization invitation has been accepted.

    ---

- **`publicMetadata?`** [`OrganizationInvitationPublicMetadata`](/reference/javascript/types/metadata#organization-invitation-public-metadata)

  Metadata that can be read from both the Frontend API and [Backend API](/reference/backend-api), but can be set only from the Backend API.


## Example

> [!NOTE]
> Using `clerkClient` varies based on your framework. Refer to the [JS Backend SDK overview](/js-backend/getting-started/quickstart) for usage details, including guidance on [how to access the `userId` and other properties](/js-backend/getting-started/quickstart#get-the-user-id-and-other-properties).


```tsx
const organizationId = 'org_123'
// Each object in the array represents a single invitation
const params = [
  {
    inviterUserId: 'user_1',
    emailAddress: 'testclerk1@clerk.dev',
    role: 'org:admin',
  },
  {
    inviterUserId: 'user_2',
    emailAddress: 'testclerk2@clerk.dev',
    role: 'org:member',
  },
]

const response = await clerkClient.organizations.createOrganizationInvitationBulk(
  organizationId,
  params,
)
```

## Backend API (BAPI) endpoint

This method in the SDK is a wrapper around the BAPI endpoint `POST/organizations/{organization_id}/invitations/bulk`. See the [BAPI reference](/reference/backend-api/tag/organization-invitations/post/organizations/\{organization_id}/invitations/bulk) for more information.
