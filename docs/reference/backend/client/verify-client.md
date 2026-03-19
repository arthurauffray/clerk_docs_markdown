# verifyClient()


> Use Clerk's JS Backend SDK to retrieve a client for a given session token, if the session is active.

Verifies the [`Client`](/reference/javascript/client) in the provided token.

```ts
function verifyClient(token: string): Promise
```

## Parameters

- **`token`** `string`

  The session token to verify.


## Example

> [!NOTE]
> Using `clerkClient` varies based on your framework. Refer to the [JS Backend SDK overview](/js-backend/getting-started/quickstart) for usage details, including guidance on [how to access the `userId` and other properties](/js-backend/getting-started/quickstart#get-the-user-id-and-other-properties).


```tsx
const token = 'my-session-token'

const response = await clerkClient.clients.verifyClient(token)
```

## Backend API (BAPI) endpoint

This method in the SDK is a wrapper around the BAPI endpoint `GET/clients/verify`. See the [BAPI reference](/reference/backend-api/tag/clients/post/clients/verify) for more information.
