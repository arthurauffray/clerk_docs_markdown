# deletePhoneNumber()


> Use Clerk's JS Backend SDK to delete a phone number.

Deletes a [`PhoneNumber`](/reference/javascript/types/phone-number).

```ts
function deletePhoneNumber(phoneNumberId: string): Promise
```

## Parameters

- **`phoneNumberId`** `string`

  The ID of the phone number to delete.


## Example

> [!NOTE]
> Using `clerkClient` varies based on your framework. Refer to the [JS Backend SDK overview](/js-backend/getting-started/quickstart) for usage details, including guidance on [how to access the `userId` and other properties](/js-backend/getting-started/quickstart#get-the-user-id-and-other-properties).


```tsx
const phoneNumberId = 'idn_123'

const response = await clerkClient.phoneNumbers.deletePhoneNumber(phoneNumberId)
```

## Backend API (BAPI) endpoint

This method in the SDK is a wrapper around the BAPI endpoint `DELETE/phone_numbers/{phone_number_id}`. See the [BAPI reference](/reference/backend-api/tag/phone-numbers/delete/phone_numbers/\{phone_number_id}) for more information.
