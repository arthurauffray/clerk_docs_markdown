# createRedirectUrl()


> Use Clerk's JS Backend SDK to create a redirect URL.

Creates a [`RedirectUrl`](/reference/backend/types/backend-redirect-url).

```ts
function createRedirectUrl(params: CreateRedirectUrlParams): Promise
```

## `CreateRedirectUrlParams`

- **`url`** `string`

  The full url value prefixed with `https://` or a custom scheme. For example, `https://my-app.com/oauth-callback` or `my-app://oauth-callback`


## Example

> [!NOTE]
> Using `clerkClient` varies based on your framework. Refer to the [JS Backend SDK overview](/js-backend/getting-started/quickstart) for usage details, including guidance on [how to access the `userId` and other properties](/js-backend/getting-started/quickstart#get-the-user-id-and-other-properties).


```tsx
const response = await clerkClient.redirectUrls.createRedirectUrl({
  url: 'https://example.com',
})
```

## Backend API (BAPI) endpoint

This method in the SDK is a wrapper around the BAPI endpoint `POST/redirect_urls`. See the [BAPI reference](/reference/backend-api/tag/redirect-urls/post/redirect_urls) for more information.
