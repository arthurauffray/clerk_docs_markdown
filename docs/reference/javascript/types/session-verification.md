# SessionVerification


> The SessionVerification interface represents the state of a session reverification process.

An interface that represents the state of the session verification process.

## Properties

- **`status`** `'needs_first_factor' | 'needs_second_factor' | 'complete'`

  The current state of the session verification.

    ---

- **`level`** `'first_factor' | 'second_factor' | 'multi_factor'`

  The requested level of the session verification.

    ---

- **`session`** [`Session`](/reference/javascript/session)

  The `Session` object that the session verification is attached to.

    ---

- **`firstFactorVerification`** [`VerificationResource`](/reference/javascript/types/verification-resource)

  The state of the verification process for the selected first factor. Initially, this property contains an empty `Verification` object, since there is no first factor selected. You need to call the [`prepareFirstFactorVerification()`](/reference/javascript/session#prepare-first-factor-verification) method in order to start the verification process.

    ---

- **`secondFactorVerification`** [`VerificationResource`](/reference/javascript/types/verification-resource)

  The state of the verification process for the selected second factor. Initially, this property contains an empty `Verification` object, since there is no second factor selected. For the `phone_code` strategy, you need to call the [`prepareSecondFactorVerification()`](/reference/javascript/session#prepare-second-factor-verification) method in order to start the verification process. For the `totp` or `backup_code` strategies, you can directly attempt the verification by calling the [`attemptSecondFactorVerification()`](/reference/javascript/session#attempt-second-factor-verification) method.

    ---

- **`supportedFirstFactors`** <code>[EmailCodeFactor](/reference/javascript/types/sign-in-first-factor#email-code-factor)\[] | [PhoneCodeFactor](/reference/javascript/types/sign-in-first-factor#phone-code-factor)\[] | [PasswordFactor](/reference/javascript/types/sign-in-first-factor#password-factor)\[]</code>

  Array of the first factors that are supported in the current session verification. Each factor contains information about the verification strategy that can be used.

    ---

- **`supportedSecondFactors`** <code>[TOTPFactor](/reference/javascript/types/sign-in-second-factor#totp-factor)\[] | [PhoneCodeFactor](/reference/javascript/types/sign-in-first-factor#phone-code-factor)\[] | [BackupCodeFactor](/reference/javascript/types/sign-in-second-factor#backup-code-factor)\[]</code>

  Array of the second factors that are supported in the current session verification. Each factor contains information about the verification strategy that can be used.
