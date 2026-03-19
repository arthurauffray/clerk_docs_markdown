# updatePhoneNumber()


> Use Clerk's JS Backend SDK to update a phone number.

Updates a [`PhoneNumber`](/reference/javascript/types/phone-number).

```ts
function updatePhoneNumber(
  phoneNumberId: string,
  params: UpdatePhoneNumberParams,
): Promise
```

## `UpdatePhoneNumberParams`

- **`primary?`** `boolean`

  Whether or not to set the phone number as the user's primary phone number.

    ---

- **`verified?`** `boolean`

  Whether or not the phone number is verified.

    ---

- **`reservedForSecondFactor`** `boolean`

  Whether or not the phone number is reserved for [multi-factor authentication](/guides/configure/auth-strategies/sign-up-sign-in-options#multi-factor-authentication). The phone number must also be verified. If there are no other reserved second factors, the phone number will be set as the default second factor.


## Example

> [!NOTE]
> Using `clerkClient` varies based on your framework. Refer to the [JS Backend SDK overview](/js-backend/getting-started/quickstart) for usage details, including guidance on [how to access the `userId` and other properties](/js-backend/getting-started/quickstart#get-the-user-id-and-other-properties).


```tsx

const phoneNumberId = 'idn_123'

const params = { verified: false }

const response = await clerkClient.phoneNumbers.updatePhoneNumber(phoneNumberId, params)
```

## Backend API (BAPI) endpoint

This method in the SDK is a wrapper around the BAPI endpoint `PATCH/phone_numbers/{phone_number_id}`. See the [BAPI reference](/reference/backend-api/tag/phone-numbers/patch/phone_numbers/\{phone_number_id}) for more information.
