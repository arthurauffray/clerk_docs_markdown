# revokeSession()


> Use Clerk's JS Backend SDK to revoke a session given its ID.

Revokes a [`Session`](/reference/backend/types/backend-session).

User will be signed out from the particular client the referred to.

```ts
function revokeSession(sessionId: string): Promise
```

## Parameters

- **`sessionId`** `string`

  The ID of the session to revoke.


## Example

> [!NOTE]
> Using `clerkClient` varies based on your framework. Refer to the [JS Backend SDK overview](/js-backend/getting-started/quickstart) for usage details, including guidance on [how to access the `userId` and other properties](/js-backend/getting-started/quickstart#get-the-user-id-and-other-properties).


```tsx
const sessionId = 'sess_123'

const response = await clerkClient.sessions.revokeSession(sessionId)
```

## Backend API (BAPI) endpoint

This method in the SDK is a wrapper around the BAPI endpoint `POST/sessions/{session_id}/revoke`. See the [BAPI reference](/reference/backend-api/tag/sessions/post/sessions/\{session_id}/revoke) for more information.
