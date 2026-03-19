# OrganizationMembership


> The OrganizationMembership object is the model around an Organization membership entity and describes the relationship between users and Organizations.

The `OrganizationMembership` object is the model around an Organization membership entity and describes the relationship between users and Organizations.

## Properties

- **`id`** `string`

  The unique identifier for this Organization membership.

    ---

- **`publicMetadata`** [`OrganizationMembershipPublicMetadata`](/reference/javascript/types/metadata#organization-membership-public-metadata)

  Metadata that can be read from the Frontend API and [Backend API](/reference/backend-api) and can be set only from the Backend API.

    ---

- **`role`** `string`

  The [Role](/guides/organizations/control-access/roles-and-permissions) of the current user in the Organization.

    ---

- **`publicUserData`** [`PublicUserData`](/reference/javascript/types/public-user-data)

  Public information about the user that this membership belongs to.

    ---

- **`organization`** [`Organization`](/reference/javascript/organization)

  The [`Organization`](/reference/javascript/organization) object the membership belongs to.

    ---

- **`createdAt`** `Date`

  The date when the membership was created.

    ---

- **`updatedAt`** `Date`

  The date when the membership was last updated.


## Methods

### `destroy()`

Deletes the membership from the Organization the membership belongs to.

```typescript
function destroy(): Promise
```

### `update()`

Updates the member's Role.

```typescript
function update(updateParams: UpdateOrganizationMembershipParams): Promise
```

#### `UpdateOrganizationMembershipParams`

- **`role`** `string`

  The [Role](/guides/organizations/control-access/roles-and-permissions) of the new member.
