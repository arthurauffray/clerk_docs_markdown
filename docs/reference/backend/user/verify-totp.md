# verifyTOTP()


> Use Clerk's JS Backend SDK to verify a TOTP or backup code for a user.

Verify that the provided TOTP or backup code is valid for the user. Verifying a backup code will result it in being consumed (i.e. it will become invalid). Useful for custom auth flows and re-verification.

```ts
function verifyTOTP(params: VerifyTOTPParams): Promise<{ verified: true; code_type: 'totp' }>
```

## `VerifyTOTPParams`

- **`userId`** `string`

  The ID of the user to verify the TOTP for.

    ---

- **`code`** `string`

  The TOTP or backup code to verify


## Example

> [!NOTE]
> Using `clerkClient` varies based on your framework. Refer to the [JS Backend SDK overview](/js-backend/getting-started/quickstart) for usage details, including guidance on [how to access the `userId` and other properties](/js-backend/getting-started/quickstart#get-the-user-id-and-other-properties).


```tsx
const userId = 'user_123'

const code = '123456'

const response = await clerkClient.users.verifyTOTP({
  userId,
  code,
})
```

## Backend API (BAPI) endpoint

This method in the SDK is a wrapper around the BAPI endpoint `POST/users/{user_id}/verify_totp`. See the [BAPI reference](/reference/backend-api/tag/users/post/users/\{user_id}/verify_totp) for more information.
