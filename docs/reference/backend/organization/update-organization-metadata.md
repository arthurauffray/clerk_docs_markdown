# updateOrganizationMetadata()


> Use Clerk's JS Backend SDK to update the metadata associated with a given Organization.

Updates the metadata attributes of an [`Organization`](/reference/backend/types/backend-organization) by merging existing values with the provided parameters. Metadata values will be updated via a "deep" merge - "deep" meaning that any nested JSON objects will be merged as well. You can remove metadata keys at any level by setting their value to `null`.

```ts
function updateOrganizationMetadata(
  organizationId: string,
  params: UpdateOrganizationMetadataParams,
): Promise
```

## `UpdateOrganizationMetadataParams`

- **`organizationId`** `string`

  The ID of the Organization to update.

    ---

- **`publicMetadata?`** [`OrganizationPublicMetadata`](/reference/javascript/types/metadata#organization-public-metadata)

  Metadata that can be read from both the Frontend API and [Backend API](/reference/backend-api), but can be set only from the Backend API .

    ---

- **`privateMetadata?`** [`OrganizationPrivateMetadata`](/reference/javascript/types/metadata#organization-private-metadata)

  Metadata that is only visible to your [Backend API](/reference/backend-api).


## Example

> [!NOTE]
> Using `clerkClient` varies based on your framework. Refer to the [JS Backend SDK overview](/js-backend/getting-started/quickstart) for usage details, including guidance on [how to access the `userId` and other properties](/js-backend/getting-started/quickstart#get-the-user-id-and-other-properties).


```tsx

const organizationId = 'org_123'

const response = await clerkClient.organizations.updateOrganizationMetadata(organizationId, {
  publicMetadata: {
    example: 'metadata',
  },
})
```

## Backend API (BAPI) endpoint

This method in the SDK is a wrapper around the BAPI endpoint `PATCH/organizations/{organization_id}/metadata`. See the [BAPI reference](/reference/backend-api/tag/organizations/patch/organizations/\{organization_id}/metadata) for more information.
