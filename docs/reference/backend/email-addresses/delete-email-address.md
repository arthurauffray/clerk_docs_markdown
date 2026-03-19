# deleteEmailAddress()


> Use Clerk's JS Backend SDK to delete an email address.

Deletes an [`EmailAddress`](/reference/javascript/types/email-address).

```ts
function deleteEmailAddress(emailAddressId: string): Promise
```

## Parameters

- **`emailAddressId`** `string`

  The ID of the email address to delete.


## Example

> [!NOTE]
> Using `clerkClient` varies based on your framework. Refer to the [JS Backend SDK overview](/js-backend/getting-started/quickstart) for usage details, including guidance on [how to access the `userId` and other properties](/js-backend/getting-started/quickstart#get-the-user-id-and-other-properties).


```tsx
const emailAddressId = 'idn_123'

const response = await clerkClient.emailAddresses.deleteEmailAddress(emailAddressId)
```

## Backend API (BAPI) endpoint

This method in the SDK is a wrapper around the BAPI endpoint `DELETE/email_addresses/{email_address_id}`. See the [BAPI reference](/reference/backend-api/tag/email-addresses/delete/email_addresses/\{email_address_id}) for more information.
