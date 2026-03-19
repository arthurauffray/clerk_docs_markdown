# EmailAddress


> The EmailAddress object is a model around an email address.

The `EmailAddress` object is a model around an email address. Email addresses are one of the identifiers used to provide identification for users.

Email addresses must be **verified** to ensure that they are assigned to their rightful owners. The `EmailAddress` object holds all necessary state around the verification process. The following steps outline the verification process:

1. Initiate the verification process by collecting the user's email address.
1. Prepare the verification process by calling the [`prepareVerification()`](#prepare-verification) method, which will send an OTP via an email link or code, depending on what parameters are passed to the method and the settings in the Clerk Dashboard.
1. Attempt to complete the verification by calling the [`attemptVerification()`](#attempt-verification) method, passing the OTP as a parameter.

For implementation examples for adding and verifying email addresses, see the [email link custom flow](/guides/development/custom-flows/authentication/email-links) and [email code custom flow](/guides/development/custom-flows/account-updates/add-email) guides.

## Properties

- **`id`** `string`

  The unique identifier for the email address.

    ---

- **`emailAddress`** `string`

  The value of the email address.

    ---

- **`matchesSsoConnection`** `boolean`

  Whether the email address matches an SSO connection.

    ---

- **`verification`** [`VerificationResource`](/reference/javascript/types/verification-resource)

  An object holding information on the verification of the email address.

    ---

- **`linkedTo`** <code>[IdentificationLinkResource](/reference/javascript/types/identification-link-resource)\[]</code>

  An array of objects containing information about any identifications that might be linked to the email address.


## Methods

### `create()`

Creates a new email address for the current user.

```typescript
function create(): Promise
```

### `destroy()`

Deletes the email address.

```typescript
function destroy(): Promise<void>
```

### `toString()`

Returns the value for the email address. Can also be accessed via the `EmailAddress.emailAddress` attribute.

```typescript
function toString(): string
```

### `prepareVerification()`

Initiates the email address verification process. Based on the specified strategy, sends either an OTP or a verification link to the email address. The verification status can be tracked through the `verification` property of the `EmailAddress` object.

```typescript
function prepareVerification(params: PrepareEmailAddressVerificationParams): Promise
```

#### `PrepareEmailAddressVerificationParams`

- **`strategy`** `'email_link' | 'email_code'`

  The verification strategy. Supported strategies are:

- **`email_link`: User will receive an email link via email.** `email_code`: User will receive an OTP via email.

  ---

- **`redirectUrl`** `string | undefined`

  **Required** if `strategy` is set to `email_link`. The full URL that the user will be redirected to when they visit the email link. See the [custom flow](/guides/development/custom-flows/authentication/email-links) for implementation details.


### `attemptVerification()`

Attempts to verify an email address using an OTP. The OTP must have been previously sent to the email address via the [EmailAddress.prepareVerification()](#prepare-verification) method with `strategy: 'email_code'`. Returns the updated `EmailAddress` object if verification is successful.

```typescript
function attemptVerification(params: AttemptEmailAddressVerificationParams): Promise
```

#### `AttemptEmailAddressVerificationParams`

- **`code`** `string`

  The OTP that was sent to the user's email address when [EmailAddress.prepareVerification()](#prepare-verification) was called with `strategy` set to `email_code`.


### `createEmailLinkFlow()`

Sets up an email verification with email link flow. Calling `createEmailLinkFlow()` will return two functions.

```typescript
function createEmailLinkFlow(): {
  startEmailLinkFlow: (params: StartEmailLinkFlowParams) => Promise
  cancelEmailLinkFlow: () => void
}
```

`createEmailLinkFlow` returns an object with two functions:

- **`startEmailLinkFlow`** <code>(params: [StartEmailLinkFlowParams](#start-email-link-flow-params)) => Promise\</code>

  Function to start the email link flow. It sends the email with the email link and polls for the verification result.

    ---

- **`cancelEmailLinkFlow`** `() => void`

  Function to stop polling for the verification result, allowing for full control of the flow and cleanup.


#### `StartEmailLinkFlowParams`

- **`redirectUrl`** `string`

  The full URL that the user will be redirected to when they visit the email link.


### `createEnterpriseSSOLinkFlow()`

Sets up an email verification with enterprise SSO link flow. Calling `createEnterpriseSSOLinkFlow()` will return two functions.

```typescript
function createEnterpriseSSOLinkFlow(): {
  startEnterpriseSSOLinkFlow: (params: StartEnterpriseSSOLinkFlowParams) => Promise
  cancelEnterpriseSSOLinkFlow: () => void
}
```

`createEnterpriseSSOLinkFlow` returns an object with two functions:

- **`startEnterpriseSSOLinkFlow`** <code>(params: [StartEnterpriseSSOLinkFlowParams](#start-enterprise-sso-link-flow-params)) => Promise\</code>

  Function to start the enterprise SSO link flow. It sends the email with the enterprise SSO link and polls for the verification result.

    ---

- **`cancelEnterpriseSSOLinkFlow`** `() => void`

  Function to stop polling for the verification result, allowing for full control of the flow and cleanup.


#### `StartEnterpriseSSOLinkFlowParams`

- **`redirectUrl`** `string`

  The full URL that the user will be redirected to when they visit the enterprise SSO link.
