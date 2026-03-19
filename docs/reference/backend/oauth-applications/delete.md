# delete()


> Use Clerk's JS Backend SDK to delete an OAuth application.

Deletes an [`OAuthApplication`](/reference/backend/types/backend-oauth-application) by its ID. Returns a [`DeletedObjectResource`](/reference/javascript/types/deleted-object-resource) object.

```ts

function delete(oauthApplicationId: string): Promise
```

## Parameters

- **`oauthApplicationId`** `string`

  The ID of the OAuth application to delete.


## Example

> [!NOTE]
> Using `clerkClient` varies based on your framework. Refer to the [JS Backend SDK overview](/js-backend/getting-started/quickstart) for usage details, including guidance on [how to access the `userId` and other properties](/js-backend/getting-started/quickstart#get-the-user-id-and-other-properties).


```tsx
const oauthApplicationId = 'oauthapp_123'

const response = await clerkClient.oauthApplications.delete(oauthApplicationId)
```

## Backend API (BAPI) endpoint

This method in the SDK is a wrapper around the BAPI endpoint `DELETE/oauth_applications/{oauth_application_id}`. See the [BAPI reference](/reference/backend-api/tag/oauth-applications/delete/oauth_applications/%7Boauth_application_id%7D) for more information.
