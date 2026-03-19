# createOrganizationInvitation()


> Use Clerk's JS Backend SDK to create an invitation for new users to join an Organization.

Creates an [`OrganizationInvitation`](/reference/backend/types/backend-organization-invitation) for new users to join an Organization.

> [!CAUTION]
>
> This endpoint is [rate limited](/guides/how-clerk-works/system-limits#backend-api-requests) to **250 requests per hour** per application instance.

```ts
function createOrganizationInvitation(
  params: CreateOrganizationInvitationParams,
): Promise
```

## `CreateOrganizationInvitationParams`

- **`organizationId`** `string`

  The Organization ID of the Organization a user is being invited to.

    ---

- **`inviterUserId`** `string | null`

  The user ID of the user creating the invitation.

    ---

- **`emailAddress`** `string`

  The email address to send the invitation to.

    ---

- **`role`** `string`

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

const inviterUserId = 'user_123'

const emailAddress = 'testclerk123@clerk.dev'

const role = 'org:member'

const response = await clerkClient.organizations.createOrganizationInvitation({
  organizationId,
  inviterUserId,
  emailAddress,
  role,
})
```

## Backend API (BAPI) endpoint

This method in the SDK is a wrapper around the BAPI endpoint `POST/organizations/{organization_id}/invitations`. See the [BAPI reference](/reference/backend-api/tag/organization-invitations/post/organizations/\{organization_id}/invitations) for more information.
