# getEmailAddress()


> Use Clerk's JS Backend SDK to retrieve a single email address by its ID.

Retrieves a single [`EmailAddress`](/reference/javascript/types/email-address).

```ts
function getEmailAddress(emailAddressId: string): Promise
```

## Parameters

- **`emailAddressId`** `string`

  The ID of the email address to retrieve.


## Example

> [!NOTE]
> Using `clerkClient` varies based on your framework. Refer to the [JS Backend SDK overview](/js-backend/getting-started/quickstart) for usage details, including guidance on [how to access the `userId` and other properties](/js-backend/getting-started/quickstart#get-the-user-id-and-other-properties).


```tsx
const emailAddressId = 'idn_123'

const response = await clerkClient.emailAddresses.getEmailAddress(emailAddressId)
```

## Backend API (BAPI) endpoint

This method in the SDK is a wrapper around the BAPI endpoint `GET/email_addresses/{email_address_id}`. See the [BAPI reference](/reference/backend-api/tag/email-addresses/get/email_addresses/\{email_address_id}) for more information.
