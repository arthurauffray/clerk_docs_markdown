# getRedirectUrlList()


> Use Clerk's JS Backend SDK to retrieve a list of white-listed redirect URLs.

Retrieves a list of all white-listed redirect URLs. Returns a [`PaginatedResourceResponse`](/reference/backend/types/paginated-resource-response) object with a `data` property that contains an array of [`RedirectUrl`](/reference/backend/types/backend-redirect-url) objects, and a `totalCount` property that indicates the total number of redirect URLs for the application.

```tsx
function getRedirectUrlList(): () => Promise>
```

## Example

> [!NOTE]
> Using `clerkClient` varies based on your framework. Refer to the [JS Backend SDK overview](/js-backend/getting-started/quickstart) for usage details, including guidance on [how to access the `userId` and other properties](/js-backend/getting-started/quickstart#get-the-user-id-and-other-properties).


```tsx
const response = await clerkClient.redirectUrls.getRedirectUrlList()
```

## Backend API (BAPI) endpoint

This method in the SDK is a wrapper around the BAPI endpoint `GET/redirect_urls/{id}`. See the [BAPI reference](/reference/backend-api/tag/redirect-urls/get/redirect_urls) for more information.
