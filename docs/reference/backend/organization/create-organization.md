# createOrganization()


> Use Clerk's JS Backend SDK to create an Organization.

Creates an [`Organization`](/reference/backend/types/backend-organization).

```ts
function createOrganization(params: CreateParams): Promise
```

## `CreateParams`

- **`name`** `string`

  Name of the Organization.

    ---

- **`createdBy`** `string`

  The user ID for the user creating the Organization. The user will become an administrator for the Organization.

    ---

- **`slug?`** `string`

  Slug of the Organization.

    ---

- **`publicMetadata?`** [`OrganizationPublicMetadata`](/reference/javascript/types/metadata#organization-public-metadata)

  Metadata that can be read from both the Frontend API and [Backend API](/reference/backend-api), but can be set only from the Backend API.

    ---

- **`privateMetadata?`** [`OrganizationPrivateMetadata`](/reference/javascript/types/metadata#organization-private-metadata)

  Metadata that is only visible to your [Backend API](/reference/backend-api).

    ---

- **`maxAllowedMemberships?`** `number`

  The maximum number of memberships allowed in the Organization. Setting this value to `0` removes any limit, allowing an unlimited number of memberships.


## Example

> [!NOTE]
> Using `clerkClient` varies based on your framework. Refer to the [JS Backend SDK overview](/js-backend/getting-started/quickstart) for usage details, including guidance on [how to access the `userId` and other properties](/js-backend/getting-started/quickstart#get-the-user-id-and-other-properties).


```tsx
const name = 'test-org'

const createdBy = 'user_123'

const response = await clerkClient.organizations.createOrganization({ name, createdBy })
```

## Backend API (BAPI) endpoint

This method in the SDK is a wrapper around the BAPI endpoint `POST/organizations`. See the [BAPI reference](/reference/backend-api/tag/organizations/post/organizations) for more information.
