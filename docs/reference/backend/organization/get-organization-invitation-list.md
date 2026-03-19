# getOrganizationInvitationList()


> Use Clerk's JS Backend SDK to retrieve a list of Organization invitations.

Retrieves a list of Organization invitations. Returns a [`PaginatedResourceResponse`](/reference/backend/types/paginated-resource-response) object with a `data` property that contains an array of [`OrganizationInvitation`](/reference/backend/types/backend-organization-invitation) objects, and a `totalCount` property that indicates the total number of Organization invitations in the system for the specified Organization.

```ts
function getOrganizationInvitationList(
  params: GetOrganizationInvitationListParams,
): Promise>
```

## `GetOrganizationInvitationListParams`

- **`organizationId`** `string`

  The ID of the Organization to retrieve the list of pending invitations from.

    ---

- **`limit?`** `number`

  The number of results to return. Must be an integer greater than zero and less than 501. Can be used for paginating the results together with `offset`. Defaults to `10`.

    ---

- **`offset?`** `number`

  Skip the first `offset` results when paginating. Needs to be an integer greater or equal to zero. To be used in conjunction with `limit`. Defaults to `0`.

    ---

- **`status?`** `string[]`

  The status of the invitation. Possible values: `pending`, `accepted`, `revoked`, `expired`. Defaults to `pending`.


## Examples

### Basic

> [!NOTE]
> Using `clerkClient` varies based on your framework. Refer to the [JS Backend SDK overview](/js-backend/getting-started/quickstart) for usage details, including guidance on [how to access the `userId` and other properties](/js-backend/getting-started/quickstart#get-the-user-id-and-other-properties).


```tsx
const organizationId = 'org_123'

const response = await clerkClient.organizations.getOrganizationInvitationList({ organizationId })
```

### Filter by invitation status

Retrieves Organization invitation list that is filtered by the status of the invitation.

```tsx
const organizationId = 'org_123'

const { data, totalCount } = await clerkClient.organizations.getOrganizationInvitationList({
  organizationId,
  // returns a list of invitations that have not yet been accepted
  status: ['pending'],
})
```

### Limit the number of results

Retrieves Organization invitation list that is filtered by the number of results.

```tsx
const organizationId = 'org_123'

const { data, totalCount } = await clerkClient.organizations.getOrganizationInvitationList({
  organizationId,
  // returns the first 10 results
  limit: 10,
})
```

### Skip results

Retrieves Organization invitation list that is filtered by the number of results to skip.

```tsx
const organizationId = 'org_123'

const { data, totalCount } = await clerkClient.organizations.getOrganizationInvitationList({
  organizationId,
  // skips the first 10 results
  offset: 10,
})
```

## Backend API (BAPI) endpoint

This method in the SDK is a wrapper around the BAPI endpoint `GET/organizations/{organization_id}/invitations`. See the [BAPI reference](/reference/backend-api/tag/organization-invitations/get/organizations/\{organization_id}/invitations) for more information.
