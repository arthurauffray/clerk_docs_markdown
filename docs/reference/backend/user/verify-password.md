# verifyPassword()


> Use Clerk's JS Backend SDK to check that the user's password matches the supplied input. Useful for custom auth flows and re-verification.

Check that the user's password matches the supplied input. Useful for custom auth flows and re-verification.

```ts
function verifyPassword(params: VerifyPasswordParams): Promise<{ verified: true }>
```

## `VerifyPasswordParams`

- **`userId`** `string`

  The ID of the user to verify the password for.

    ---

- **`password`** `string`

  The password to verify.


## Example

> [!NOTE]
> Using `clerkClient` varies based on your framework. Refer to the [JS Backend SDK overview](/js-backend/getting-started/quickstart) for usage details, including guidance on [how to access the `userId` and other properties](/js-backend/getting-started/quickstart#get-the-user-id-and-other-properties).


```tsx
const userId = 'user_123'

const password = 'testpassword123'

const response = await clerkClient.users.verifyPassword({
  userId,
  password,
})
```

## Backend API (BAPI) endpoint

This method in the SDK is a wrapper around the BAPI endpoint `POST/users/{user_id}/verify_password`. See the [BAPI reference](/reference/backend-api/tag/users/post/users/\{user_id}/verify_password) for more information.
