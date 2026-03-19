# createEmailAddress()


> Use Clerk's JS Backend SDK to create an email address for the specified user.

Creates an [`EmailAddress`](/reference/javascript/types/email-address) for the specified user.

```ts
function createEmailAddress(params: CreateEmailAddressParams): Promise
```

## `CreateEmailAddressParams`

- **`userId`** `string`

  The ID of the user to create the email address for.

    ---

- **`emailAddress`** `string`

  The email address to assign to the specified user.

    ---

- **`primary?`** `boolean`

  Whether or not to set the email address as the user's primary email address. Defaults to `false`, unless it is the first email address.

    ---

- **`verified?`** `boolean`

  Whether or not the email address is verified.


## Example

> [!NOTE]
> Using `clerkClient` varies based on your framework. Refer to the [JS Backend SDK overview](/js-backend/getting-started/quickstart) for usage details, including guidance on [how to access the `userId` and other properties](/js-backend/getting-started/quickstart#get-the-user-id-and-other-properties).


```tsx
const response = await clerkClient.emailAddresses.createEmailAddress({
  userId: 'user_123',
  emailAddress: 'testclerk123@gmail.com',
  primary: true,
  verified: true,
})
```

## Backend API (BAPI) endpoint

This method in the SDK is a wrapper around the BAPI endpoint `POST/email_addresses`. See the [BAPI reference](/reference/backend-api/tag/email-addresses/post/email_addresses) for more information.
