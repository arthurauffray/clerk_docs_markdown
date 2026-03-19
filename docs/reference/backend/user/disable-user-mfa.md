# disableUserMFA()


> Use Clerk's JS Backend SDK to disable all of a user's MFA methods at once.

> [!WARNING]
> On November 14, 2025, Clerk introduced [**Client Trust**](/guides/secure/client-trust). This free security protection automatically enforces MFA **the first time** a user logs in from a new device even if MFA is disabled. Learn more about [Client Trust and our commitment to security](/changelog/2025-11-14-client-trust-credential-stuffing-killer).

Disable all of a user's MFA methods (e.g. OTP sent via SMS, TOTP on their authenticator app) at once.

```ts
function disableUserMFA(userId: string): Promise
```

## Parameters

- **`userId`** `string`

  The ID of the user to disable MFA for.


## Example

> [!NOTE]
> Using `clerkClient` varies based on your framework. Refer to the [JS Backend SDK overview](/js-backend/getting-started/quickstart) for usage details, including guidance on [how to access the `userId` and other properties](/js-backend/getting-started/quickstart#get-the-user-id-and-other-properties).


```tsx
const userId = 'user_123'

const response = await clerkClient.users.disableUserMFA(userId)
```

## Backend API (BAPI) endpoint

This method in the SDK is a wrapper around the BAPI endpoint `DELETE/users/{user_id}/mfa`. See the [BAPI reference](/reference/backend-api/tag/users/delete/users/\{user_id}/mfa) for more information.
