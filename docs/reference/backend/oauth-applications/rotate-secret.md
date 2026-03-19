# rotateSecret()


> Use Clerk's JS Backend SDK to rotate the OAuth application's client secret.

Rotates the client secret for a given [`OAuthApplication`](/reference/backend/types/backend-oauth-application) by its ID. When the client secret is rotated, ensure that you update it in your authorized OAuth clients.

```ts
function rotateSecret(oauthApplicationId: string): Promise
```

## Parameters

- **`oauthApplicationId`** `string`

  The ID of the OAuth application for which to rotate the client secret.


## Example

> [!NOTE]
> Using `clerkClient` varies based on your framework. Refer to the [JS Backend SDK overview](/js-backend/getting-started/quickstart) for usage details, including guidance on [how to access the `userId` and other properties](/js-backend/getting-started/quickstart#get-the-user-id-and-other-properties).


```tsx
const oauthApplicationId = 'oauthapp_123'

const response = await clerkClient.oauthApplications.rotateSecret(oauthApplicationId)
```

## Backend API (BAPI) endpoint

This method in the SDK is a wrapper around the BAPI endpoint `POST/oauth_applications/{oauth_application_id}/rotate_secret`. See the [BAPI reference](/reference/backend-api/tag/oauth-applications/post/oauth_applications/%7Boauth_application_id%7D/rotate_secret) for more information.
