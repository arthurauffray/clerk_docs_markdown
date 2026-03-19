# createPhoneNumber()


> Use Clerk's JS Backend SDK to create a phone number for the specified user.

Creates a [`PhoneNumber`](/reference/javascript/types/phone-number) for the specified user.

```ts
function createPhoneNumber(params: CreatePhoneNumberParams): Promise
```

## `CreatePhoneNumberParams`

- **`userId`** `string`

  The ID of the user to create the phone number for.

    ---

- **`phoneNumber`** `string`

  The phone number to assign to the specified user. Must adhere to the [E.164 format](https://en.wikipedia.org/wiki/E.164) standard for phone number format.

    ---

- **`primary?`** `boolean`

  Whether or not to set the phone number as the user's primary phone number. Defaults to `false`, unless it is the first phone number.

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
const response = await clerkClient.phoneNumbers.createPhoneNumber({
  userId: 'user_123',
  phoneNumber: '15551234567',
  primary: true,
  verified: true,
})
```

## Backend API (BAPI) endpoint

This method in the SDK is a wrapper around the BAPI endpoint `POST/phone_numbers`. See the [BAPI reference](/reference/backend-api/tag/phone-numbers/post/phone_numbers) for more information.
