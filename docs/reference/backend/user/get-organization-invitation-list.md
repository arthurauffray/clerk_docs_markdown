# getOrganizationInvitationList()


> Use Clerk's JS Backend SDK to retrieve a list of Organization invitations for a given user.

Retrieves a list of Organization invitations for a given user. Returns a [`PaginatedResourceResponse`](/reference/backend/types/paginated-resource-response) object with a `data` property that contains an array of [`OrganizationInvitation`](/reference/backend/types/backend-organization-invitation) objects, and a `totalCount` property that indicates the total number of Organization invitations in the system for the specified Organization.

```ts
function getOrganizationInvitationList(
  params: GetOrganizationInvitationListParams,
): Promise>
```

## `GetOrganizationInvitationListParams`

- **`userId`** `string`

  The ID of the user to retrieve the list of Organization invitations for.

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
const userId = 'user_123'

const response = await clerkClient.users.getOrganizationInvitationList({ userId })
```

### Filter by invitation status

Retrieves a list of a user's Organization invitations that is filtered by the status of the invitation.

```tsx
const userId = 'user_123'

const { data, totalCount } = await clerkClient.users.getOrganizationInvitationList({
  userId,
  // returns a list of invitations that have not yet been accepted
  status: ['pending'],
})
```

### Limit the number of results

Retrieves a list of a user's Organization invitations that is filtered by the number of results.

```tsx
const userId = 'user_123'

const { data, totalCount } = await clerkClient.users.getOrganizationInvitationList({
  userId,
  // returns the first 10 invitations
  limit: 10,
})
```

### Skip results

Retrieves a list of a user's Organization invitations that is filtered by the number of results to skip.

```tsx
const userId = 'user_123'

const { data, totalCount } = await clerkClient.users.getOrganizationInvitationList({
  userId,
  // skips the first 10 invitations
  offset: 10,
})
```

## Backend API (BAPI) endpoint

This method in the SDK is a wrapper around the BAPI endpoint `GET/users/{user_id}/organization_invitations`. See the [BAPI reference](/reference/backend-api/tag/users/get/users/%7Buser_id%7D/organization_invitations) for more information.
