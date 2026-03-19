# lockUser()


> Use Clerk's JS Backend SDK to mark a user as locked, which means they are not allowed to sign in again until the lock expires.

Marks the given [`User`](/reference/backend/types/backend-user) as locked, which means they are not allowed to sign in again until the lock expires.

By default, lockout duration is 1 hour, but it can be configured in the application's [**Attack protection**](https://dashboard.clerk.com/~/user-authentication/attack-protection) settings. For more information, see the [dedicated guide for customizing **Attack protection** settings](/guides/secure/user-lockout).

```ts
function lockUser(userId: string): Promise
```

## Parameters

- **`userId`** `string`

  The ID of the user to lockout.


## Example

> [!NOTE]
> Using `clerkClient` varies based on your framework. Refer to the [JS Backend SDK overview](/js-backend/getting-started/quickstart) for usage details, including guidance on [how to access the `userId` and other properties](/js-backend/getting-started/quickstart#get-the-user-id-and-other-properties).


```tsx
const userId = 'user_123'

const response = await clerkClient.users.lockUser(userId)
```

## Backend API (BAPI) endpoint

This method in the SDK is a wrapper around the BAPI endpoint `POST/users/{user_id}/lock`. See the [BAPI reference](/reference/backend-api/tag/users/post/users/\{user_id}/lock) for more information.
