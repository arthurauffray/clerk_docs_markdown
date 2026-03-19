# getOrganizationMembershipList()


> Use Clerk's JS Backend SDK to retrieve a list of Organization memberships for a given user.

Retrieves a list of Organization memberships for a given user. Returns a [`PaginatedResourceResponse`](/reference/backend/types/paginated-resource-response) object with a `data` property that contains an array of [`OrganizationMembership`](/reference/backend/types/backend-organization-membership) objects, and a `totalCount` property that indicates the total number of Organization memberships in the system for the specified Organization.

```ts
function getOrganizationMembershipList(
  params: GetOrganizationMembershipListParams,
): Promise>
```

## `GetOrganizationMembershipListParams`

- **`userId`** `string`

  The ID of the user to retrieve the list of Organization memberships for.

    ---

- **`limit?`** `number`

  The number of results to return. Must be an integer greater than zero and less than 501. Can be used for paginating the results together with `offset`. Defaults to `10`.

    ---

- **`offset?`** `number`

  Skip the first `offset` results when paginating. Needs to be an integer greater or equal to zero. To be used in conjunction with `limit`. Defaults to `0`.


## Examples

> [!NOTE]
> Using `clerkClient` varies based on your framework. Refer to the [JS Backend SDK overview](/js-backend/getting-started/quickstart) for usage details, including guidance on [how to access the `userId` and other properties](/js-backend/getting-started/quickstart#get-the-user-id-and-other-properties).


```tsx
const userId = 'user_123'

const response = await clerkClient.users.getOrganizationMembershipList({ userId })
```

### Limit the number of results

Retrieves a list of a user's Organization memberships that is filtered by the number of results.

```tsx
const userId = 'user_123'

const { data, totalCount } = await clerkClient.users.getOrganizationMembershipList({
  userId,
  // returns the first 10 memberships
  limit: 10,
})
```

### Skip results

Retrieves a list of a user's Organization memberships that is filtered by the number of results to skip.

```tsx
const userId = 'user_123'

const { data, totalCount } = await clerkClient.users.getOrganizationMembershipList({
  userId,
  // skips the first 10 memberships
  offset: 10,
})
```

## Backend API (BAPI) endpoint

This method in the SDK is a wrapper around the BAPI endpoint `GET/users/{user_id}/organization_memberships`. See the [BAPI reference](/reference/backend-api/tag/users/get/users/\{user_id}/organization_memberships) for more information.
