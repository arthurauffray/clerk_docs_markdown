# getSession()


> Use Clerk's JS Backend SDK to retrieve a single session by its ID.

Retrieves a single [`Session`](/reference/backend/types/backend-session).

```ts
function getSession(sessionId: string): Promise
```

## Parameters

- **`sessionId`** `string`

  The ID of the session to retrieve.


## Example

> [!NOTE]
> Using `clerkClient` varies based on your framework. Refer to the [JS Backend SDK overview](/js-backend/getting-started/quickstart) for usage details, including guidance on [how to access the `userId` and other properties](/js-backend/getting-started/quickstart#get-the-user-id-and-other-properties).


```tsx
const sessionId = 'sess_123'

const response = await clerkClient.sessions.getSession(sessionId)
```

## Backend API (BAPI) endpoint

This method in the SDK is a wrapper around the BAPI endpoint `GET/sessions/{session_id}`. See the [BAPI reference](/reference/backend-api/tag/sessions/get/sessions/\{session_id}) for more information.
