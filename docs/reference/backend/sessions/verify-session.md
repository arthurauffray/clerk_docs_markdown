# verifySession()` (deprecated)


> Use Clerk's JS Backend SDK to to verify whether a session with a given ID corresponds to the provided session token.

> [!CAUTION]
> This method is now deprecated. Refer to the [Manual JWT Verification](/guides/sessions/manual-jwt-verification) guide for the recommended way to verify sessions/tokens.

Verifies whether a session with a given ID corresponds to the provided session token. Throws an error if the provided ID is invalid.

## Example

> [!NOTE]
> Using `clerkClient` varies based on your framework. Refer to the [JS Backend SDK overview](/js-backend/getting-started/quickstart) for usage details, including guidance on [how to access the `userId` and other properties](/js-backend/getting-started/quickstart#get-the-user-id-and-other-properties).


```tsx
const sessionId = 'my-session-id'

const token = 'my-session-token'

const session = await clerkClient.sessions.verifySession(sessionId, token)
```

## Required parameters

- **`sessionId`** `string`

  The ID of the session to verify.

    ---

- **`token`** `string`

  The token of the session to verify with.
