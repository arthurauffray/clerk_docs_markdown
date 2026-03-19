# updateOrganization()


> Use Clerk's JS Backend SDK to update an Organization's name.

Updates an [`Organization`](/reference/backend/types/backend-organization).

```ts
function updateOrganization(params: UpdateOrganizationParams): Promise
```

## `UpdateOrganizationParams`

- **`organizationId`** `string`

  The Organization ID of the Organization being updated.

    ---

- **`name?`** `string`

  The updated name of the Organization.

    ---

- **`slug?`** `string`

  The updated slug of the Organization.

    ---

- **`publicMetadata?`** [`OrganizationPublicMetadata`](/reference/javascript/types/metadata#organization-public-metadata)

  Metadata that can be read from both the Frontend API and [Backend API](/reference/backend-api), but can be set only from the Backend API. Updating this property will override the existing metadata. To merge metadata, use [`updateOrganizationMetadata()`](/reference/backend/organization/update-organization-metadata).

    ---

- **`privateMetadata?`** [`OrganizationPrivateMetadata`](/reference/javascript/types/metadata#organization-private-metadata)

  Metadata that is only visible to your [Backend API](/reference/backend-api). Updating this property will override the existing metadata. To merge metadata, use [`updateOrganizationMetadata()`](/reference/backend/organization/update-organization-metadata).

    ---

- **`maxAllowedMemberships?`** `number`

  The maximum number of memberships allowed in the Organization. Setting this value to `0` removes any limit, allowing an unlimited number of memberships.


## Example

> [!NOTE]
> Using `clerkClient` varies based on your framework. Refer to the [JS Backend SDK overview](/js-backend/getting-started/quickstart) for usage details, including guidance on [how to access the `userId` and other properties](/js-backend/getting-started/quickstart#get-the-user-id-and-other-properties).


```tsx

const organizationId = 'org_123'

const name = 'Test Updated'

const response = await clerkClient.organizations.updateOrganization(organizationId, { name })
```

## Backend API (BAPI) endpoint

This method in the SDK is a wrapper around the BAPI endpoint `PATCH/organizations/{organization_id}`. See the [BAPI reference](/reference/backend-api/tag/organizations/patch/organizations/\{organization_id}) for more information.
