# updateOrganizationLogo()


> Use Clerk's JS Backend SDK to update an Organization's logo.

Updates the Organization's logo. Returns an [`Organization`](/reference/backend/types/backend-organization) object.

```ts
function updateOrganizationLogo(
  organizationId: string,
  params: UpdateLogoParams,
): Promise
```

## `UpdateLogoParams`

- **`file`** `Blob | File`

  The file to upload as the Organization's logo.

    ---

- **`uploaderUserId?`** `string`

  The ID of the user uploading the logo.


## Example

> [!NOTE]
> Using `clerkClient` varies based on your framework. Refer to the [JS Backend SDK overview](/js-backend/getting-started/quickstart) for usage details, including guidance on [how to access the `userId` and other properties](/js-backend/getting-started/quickstart#get-the-user-id-and-other-properties).


> [!WARNING]
> Using JS Backend SDK methods can contribute towards rate limiting. To set an Organization's logo, it's recommended to use the frontend [`organization.setLogo()`](/reference/javascript/organization#set-logo) method instead.

```tsx
const organizationId = 'org_123'
const uploaderUserId = 'user_123'

const fileBits = ['logo-pic-content']
const fileName = 'logo.png'
const file = new File(fileBits, fileName, { type: 'image/png' })

const params = {
  file,
  uploaderUserId,
}

const response = await clerkClient.organizations.updateOrganizationLogo(organizationId, params)
```

## Backend API (BAPI) endpoint

This method in the SDK is a wrapper around the BAPI endpoint `PUT/organizations/{organization_id}/logo`. See the [BAPI reference](/reference/backend-api/tag/organizations/put/organizations/\{organization_id}/logo) for more information.
