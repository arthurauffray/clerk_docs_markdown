# updateEmailAddress()


> Use Clerk's JS Backend SDK to update an email address.

Updates an [`EmailAddress`](/reference/javascript/types/email-address).

```ts
function updateEmailAddress(
  emailAddressId: string,
  params: UpdateEmailAddressParams,
): Promise
```

## `UpdateEmailAddressParams`

- **`primary?`** `boolean`

  Whether or not to set the email address as the user's primary email address.

    ---

- **`verified?`** `boolean`

  Whether or not the email address is verified.


## Example

> [!NOTE]
> Using `clerkClient` varies based on your framework. Refer to the [JS Backend SDK overview](/js-backend/getting-started/quickstart) for usage details, including guidance on [how to access the `userId` and other properties](/js-backend/getting-started/quickstart#get-the-user-id-and-other-properties).


```tsx

const emailAddressId = 'idn_123'

const params = { verified: false }

const response = await clerkClient.emailAddresses.updateEmailAddress(emailAddressId, params)
```

## Backend API (BAPI) endpoint

This method in the SDK is a wrapper around the BAPI endpoint `PATCH/email_addresses/{email_address_id}`. See the [BAPI reference](/reference/backend-api/tag/email-addresses/patch/email_addresses/\{email_address_id}) for more information.
