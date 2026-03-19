# deleteRedirectUrl()


> Use Clerk's JS Backend SDK to delete a redirect URL.

Deletes a [`RedirectUrl`](/reference/backend/types/backend-redirect-url).

```ts
function deleteRedirectUrl(redirectUrlId: string): Promise
```

## Parameters

- **`redirectUrlId`** `string`

  The ID of the redirect URL to delete.


## Example

> [!NOTE]
> Using `clerkClient` varies based on your framework. Refer to the [JS Backend SDK overview](/js-backend/getting-started/quickstart) for usage details, including guidance on [how to access the `userId` and other properties](/js-backend/getting-started/quickstart#get-the-user-id-and-other-properties).


```tsx
const redirectUrlId = 'ru_123'

const response = await clerkClient.redirectUrls.deleteRedirectUrl(redirectUrlId)
```

## Backend API (BAPI) endpoint

This method in the SDK is a wrapper around the BAPI endpoint `DELETE/redirect_urls/{id}`. See the [BAPI reference](/reference/backend-api/tag/redirect-urls/delete/redirect_urls/\{id}) for more information.
