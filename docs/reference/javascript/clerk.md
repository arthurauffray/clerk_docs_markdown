# Clerk` class


> The Clerk class is the main entrypoint class for the @clerk/clerk-js package. It contains a number of methods and properties for interacting with the Clerk API.

The `Clerk` class is the main entrypoint class for the `@clerk/clerk-js` package. It contains a number of methods and properties for interacting with the Clerk API.

## Properties

- **`apiKeys`** [`APIKeys`][api-ref]

  The `APIKeys` object used for managing API keys.

    ---

- **`billing`** [`Billing`][billing-ref]

  The `Billing` object used for managing billing.

    ---

- **`client`** [`Client`][client-ref]

  The `Client` object for the current window.

    ---

- **`domain`** `string`

  The current Clerk app's domain. Prefixed with `clerk.` on production if not already prefixed. Returns `""` when ran on the server.

    ---

- **`instanceType`** `'production' | 'development'`

  Indicates if the Clerk instance is running in production or development mode.

    ---

- **`isSatellite`** `boolean`

  A boolean that indicates if the instance is a satellite app.

    ---

- **`isSignedIn`** `boolean`

  A boolean that indicates if the user is signed in.

    ---

- **`loaded`** `boolean`

  A boolean that indicates if the `Clerk` object is ready for use. Set to `false` when the `status` is `'loading'` or `'error'`. Set to `true` when the `status` is either `'ready'` or `'degraded'`.

    ---

- **`organization`** <code>[Organization][organization-ref] | null | undefined</code>

  A shortcut to the last active `Session.user.organizationMemberships` which holds an instance of a `Organization` object. If the session is `null` or `undefined`, the user field will match.

    ---

- **`proxyUrl`** `string`

  Your Clerk app's proxy URL. Required for applications that run behind a reverse proxy. Can be either a relative path (`/__clerk`) or a full URL (`https://<your-domain>/__clerk`).

    ---

- **`publishableKey`** `string | undefined`

  Your Clerk Publishable Key.

    ---

- **`sdkMetadata`** `{ name: string; version: string; environment: string }`

  Contains information about the SDK that the host application is using. You don't need to set this value yourself unless you're [developing an SDK](/guides/development/sdk-development/overview).

    ---

- **`session`** <code>[Session][session-ref] | null | undefined</code>

  The currently active `Session`, which is guaranteed to be one of the sessions in `Client.sessions`. If there is no active session, this field will be `null`. If the session is loading, this field will be `undefined`.

    ---

- **`status`** `'degraded' | 'error' | 'loading' | 'ready'`

  The status of the Clerk instance. Possible values are:

- **`'degraded'`: Set when Clerk is partially operational.** `'error'`: Set when hotloading `clerk-js` failed or `Clerk.load()` failed. `'loading'`: Set during initialization. `'ready'`: Set when Clerk is fully operational.

  ---

- **`telemetry?`** `{ disabled: boolean, debug: boolean }`

  [Telemetry](/guides/how-clerk-works/security/clerk-telemetry) configuration.

    ---

- **`user`** <code>[User][user-ref] | null | undefined</code>

  A shortcut to `Session.user` which holds the currently active `User` object. If the session is `null` or `undefined`, the user field will match.

    ---

- **`version`** `string`

  The Clerk SDK version.


## Methods

### `addListener()`

Registers a listener that triggers a callback whenever a change in the [`Client`][client-ref], [`Session`][session-ref], or [`User`][user-ref] object occurs. This method is primarily used to build frontend SDKs like [`@clerk/react`](https://www.npmjs.com/package/@clerk/react). Returns an `UnsubscribeCallback` function that can be used to remove the listener from the `Clerk` object.

```typescript
function addListener(listener: (emission: Resources) => void): UnsubscribeCallback
```

#### `Resources`

- **`client`** [`Client`][client-ref]

  ---

- **`session`** <code>[Session][session-ref] | null | undefined</code>

  ---

- **`user`** <code>[User][user-ref] | null | undefined</code>

  ---

- **`organization`** <code>[Organization][organization-ref] | null | undefined</code>

  ---

- **`lastOrganizationInvitation`** <code>[OrganizationInvitation](/reference/javascript/types/organization-invitation) | null | undefined</code>

  ---

- **`lastOrganizationMember`** <code>[OrganizationMembership](/reference/javascript/types/organization-membership) | null | undefined</code>


> [!NOTE]
> Note the following about `User` and `Session`:
>
> - When there is an active session, `user === session.user`.
> - When there is no active session, `User` and `Session` will both be `null`.

### `authenticateWithMetamask()`

Starts a sign-in flow that uses the MetaMask browser extension to authenticate the user using their Ethereum wallet address.

```typescript
function authenticateWithMetamask({
  redirectUrl,
  signUpContinueUrl,
  customNavigate,
}?: AuthenticateWithMetamaskParams): Promise<void>
```

#### `AuthenticateWithMetamaskParams`

- **`redirectUrl?`** `string | undefined`

  The full URL or path to navigate to after a successful sign-in or sign-up.

    ---

- **`signUpContinueUrl?`** `string | undefined`

  The URL to navigate to if the sign-up process is missing user information.

    ---

- **`customNavigate?`** `((to: string) => Promise<unknown> | unknown) | undefined`

  A function that overrides Clerk's default navigation behavior, allowing custom handling of navigation during sign-up and sign-in flows.


### `authenticateWithCoinbaseWallet()`

Starts a sign-in flow that uses the Coinbase Wallet to authenticate the user using their Web3 wallet address.

```typescript
function authenticateWithCoinbaseWallet({
  redirectUrl,
  signUpContinueUrl,
  customNavigate,
}?: AuthenticateWithCoinbaseWalletParams): Promise<void>
```

#### `AuthenticateWithCoinbaseWalletParams`

- **`redirectUrl?`** `string | undefined`

  The full URL or path to navigate to after a successful sign-in or sign-up.

    ---

- **`signUpContinueUrl?`** `string | undefined`

  The full URL or path to navigate to if the sign-up process is missing user information.

    ---

- **`customNavigate?`** `((to: string) => Promise<unknown> | unknown) | undefined`

  A function that overrides Clerk's default navigation behavior, allowing custom handling of navigation during sign-up and sign-in flows.


### `authenticateWithOKXWallet()`

Starts a sign-in flow that uses the OKX Wallet to authenticate the user using their Web3 wallet address.

```typescript
function authenticateWithOKXWallet(props?: AuthenticateWithOKXWalletParams): Promise<void>
```

#### `AuthenticateWithOKXWalletParams`

- **`redirectUrl?`** `string | undefined`

  The full URL or path to navigate to after a successful sign-in or sign-up.

    ---

- **`signUpContinueUrl?`** `string | undefined`

  The full URL or path to navigate to if the sign-up process is missing user information.

    ---

- **`customNavigate?`** `((to: string) => Promise<unknown> | unknown) | undefined`

  A function that overrides Clerk's default navigation behavior, allowing custom handling of navigation during sign-up and sign-in flows.

    ---

- **`unsafeMetadata?`** [`SignUpUnsafeMetadata`](/reference/javascript/types/metadata#sign-up-unsafe-metadata)

  Metadata that can be read and set from the frontend. Once the sign-up is complete, the value of this field will be automatically copied to the newly created user's unsafe metadata. One common use case for this attribute is to use it to implement custom fields that can be collected during sign-up and will automatically be attached to the created `User` object.

    ---

- **`legalAccepted?`** `boolean`

  A boolean indicating whether the user has agreed to the [legal compliance](/guides/secure/legal-compliance) documents.


### `authenticateWithBase()`

Starts a sign-in flow that uses Base to authenticate the user using their Web3 wallet address.

```typescript
function authenticateWithBase(props?: AuthenticateWithBaseParams): Promise<void>
```

#### `AuthenticateWithBaseParams`

- **`redirectUrl?`** `string | undefined`

  The full URL or path to navigate to after a successful sign-in or sign-up.

    ---

- **`signUpContinueUrl?`** `string | undefined`

  The full URL or path to navigate to if the sign-up process is missing user information.

    ---

- **`customNavigate?`** `((to: string) => Promise<unknown> | unknown) | undefined`

  A function that overrides Clerk's default navigation behavior, allowing custom handling of navigation during sign-up and sign-in flows.

    ---

- **`unsafeMetadata?`** [`SignUpUnsafeMetadata`](/reference/javascript/types/metadata#sign-up-unsafe-metadata)

  Metadata that can be read and set from the frontend. Once the sign-up is complete, the value of this field will be automatically copied to the newly created user's unsafe metadata. One common use case for this attribute is to use it to implement custom fields that can be collected during sign-up and will automatically be attached to the created `User` object.

    ---

- **`legalAccepted?`** `boolean`

  A boolean indicating whether the user has agreed to the [legal compliance](/guides/secure/legal-compliance) documents.


### `authenticateWithSolana()`

Starts a sign-in flow that uses Solana to authenticate the user using their Solana wallet address. This method prompts the user to connect their Solana wallet and sign a message to verify ownership of the wallet address. The `walletName` parameter specifies which Solana wallet provider to use for the authentication process, which is required to initiate the connection and signature request.

```typescript
function authenticateWithSolana(props?: AuthenticateWithSolanaParams): Promise<void>
```

#### `AuthenticateWithSolanaParams`

- **`walletName`** `string`

  The name of the Solana wallet provider to use for the authentication process.

    ---

- **`redirectUrl?`** `string | undefined`

  The full URL or path to navigate to after a successful sign-in or sign-up.

    ---

- **`signUpContinueUrl?`** `string | undefined`

  The full URL or path to navigate to if the sign-up process is missing user information.

    ---

- **`customNavigate?`** `((to: string) => Promise<unknown> | unknown) | undefined`

  A function that overrides Clerk's default navigation behavior, allowing custom handling of navigation during sign-up and sign-in flows.

    ---

- **`unsafeMetadata?`** [`SignUpUnsafeMetadata`](/reference/javascript/types/metadata#sign-up-unsafe-metadata)

  Metadata that can be read and set from the frontend. Once the sign-up is complete, the value of this field will be automatically copied to the newly created user's unsafe metadata. One common use case for this attribute is to use it to implement custom fields that can be collected during sign-up and will automatically be attached to the created `User` object.

    ---

- **`legalAccepted?`** `boolean`

  A boolean indicating whether the user has agreed to the [legal compliance](/guides/secure/legal-compliance) documents.


### `authenticateWithWeb3()`

```typescript
function authenticateWithWeb3({
  redirectUrl,
  signUpContinueUrl,
  customNavigate,
  strategy,
}: ClerkAuthenticateWithWeb3Params): Promise<void>
```

#### `ClerkAuthenticateWithWeb3Params`

- **`redirectUrl?`** `string | undefined`

  The full URL or path to navigate to after a successful sign in or sign up.

    ---

- **`signUpContinueUrl?`** `string | undefined`

  The full URL or path to navigate to if the sign-up process is missing user information.

    ---

- **`customNavigate?`** `((to: string) => Promise<unknown> | unknown) | undefined`

  A function that overrides Clerk's default navigation behavior, allowing custom handling of navigation during sign-up and sign-in flows.

    ---

- **`strategy`** `Web3Strategy`

  The Web3 verification strategy.

    ---

- **`unsafeMetadata?`** [`SignUpUnsafeMetadata`](/reference/javascript/types/metadata#sign-up-unsafe-metadata)

  Metadata that can be read and set from the frontend. Once the sign-up is complete, the value of this field will be automatically copied to the newly created user's unsafe metadata. One common use case for this attribute is to use it to implement custom fields that can be collected during sign-up and will automatically be attached to the created `User` object.

    ---

- **`legalAccepted?`** `boolean`

  A boolean indicating whether the user has agreed to the [legal compliance](/guides/secure/legal-compliance) documents.

    ---

- **`secondFactorUrl?`** `string`

  The full URL or path to navigate to during sign in, if [multi-factor authentication](/guides/configure/auth-strategies/sign-up-sign-in-options#multi-factor-authentication) is enabled.

    ---

- **`walletName?`** `string`

  The name of the wallet provider to use for the authentication process. This parameter is required when using `web3_solana_signature` as the `strategy`.


### `buildCreateOrganizationUrl()`

Returns the configured URL where [``](/reference/components/organization/create-organization) is mounted or a custom create-organization page is rendered.

```typescript
function buildCreateOrganizationUrl(): string
```

#### Example

```js
clerk.buildCreateOrganizationUrl()
```

### `buildHomeUrl()`

Returns the URL you've configured in the Clerk Dashboard.

```typescript
function buildHomeUrl(): string
```

#### Example

```js
clerk.buildHomeUrl()
```

### `buildOrganizationProfileUrl()`

Returns the configured URL where [``](/reference/components/organization/organization-profile) is mounted or a custom organization-profile page is rendered.

```typescript
function buildOrganizationProfileUrl(): string
```

#### Example

```js
clerk.buildOrganizationProfileUrl()
```

### `buildSignInUrl()`

Returns the configured URL where [``](/reference/components/authentication/sign-in) is mounted or a custom sign-in page is rendered.

```typescript
function buildSignInUrl(options?: RedirectOptions): string
```

#### Parameters

- **`options`** <code>[RedirectOptions](/reference/javascript/types/redirect-options) | undefined</code>

  Options used to control the redirect in the constructed URL.


#### Example

```js
clerk.buildSignInUrl({
  signInForceRedirectUrl: '/dashboard',
  signUpForceRedirectUrl: '/dashboard',
})
```

### `buildSignUpUrl()`

Returns the configured URL where [``](/reference/components/authentication/sign-up) is mounted or a custom sign-up page is rendered.

```typescript
function buildSignUpUrl(options?: RedirectOptions): string
```

#### Parameters

- **`options`** <code>[RedirectOptions](/reference/javascript/types/redirect-options) | undefined</code>

  Options used to control the redirect in the constructed URL.


#### Example

```js
clerk.buildSignUpUrl({
  signInForceRedirectUrl: '/dashboard',
  signUpForceRedirectUrl: '/dashboard',
})
```

### `buildUrlWithAuth()`

Decorates the provided URL with the auth token for development instances.

```typescript
function buildUrlWithAuth(to: string, options?: BuildUrlWithAuthParams): string
```

#### Parameters

- **`to`** `string`

  The route to create a URL towards.

    ---

- **`options`** [`BuildUrlWithAuthParams`](#build-url-with-auth-params)

  Options to apply toward the URL builder.


#### Example

```js
clerk.buildUrlWithAuth('/dashboard')
```

#### `BuildUrlWithAuthParams`

- **`useQueryParam`** `boolean | null | undefined`

  Controls if dev browser JWT is added as a query param.


### `buildUserProfileUrl()`

Returns the URL where [``](/reference/components/user/user-profile) is mounted or a custom user-profile page is rendered.

```typescript
function buildUserProfileUrl(): string
```

#### Example

```js
clerk.buildUserProfileUrl()
```

### `constructor()`

Create an instance of the `Clerk` class with dedicated options.

This method is only available when importing `Clerk` from `@clerk/clerk-js`, rather than using a Window script.

```typescript
class Clerk {
  constructor(key: string, options?: DomainOrProxyUrl)
}
```

#### Parameters

- **`key`** `string`

  Your Clerk Publishable Key.

    ---

- **`options?`** <code>[DomainOrProxyUrl](#domain-or-proxy-url) | undefined</code>

  The domain or proxy URL used to connect to Clerk.


#### `DomainOrProxyUrl`

Only one of the two properties are allowed to be set at a time.

- **`proxyUrl?`** `never | string | ((url: URL) => string)`

  The proxy URL used to connect to Clerk. If a function, will be called with a `URL` made from `window.location.href`.

    ---

- **`domain?`** `never | string | ((url: URL) => string)`

  The domain used to connect to Clerk. If a function, will be called with a `URL` made from `window.location.href`.


### `createOrganization()`

Creates an Organization programmatically. Returns an [`Organization`][organization-ref] object.

> [!NOTE]
> For React-based apps, consider using the [``](/reference/components/organization/create-organization) component.

```typescript
function createOrganization({ name, slug }: CreateOrganizationParams): Promise
```

#### Parameters

- **`name`** `string`

  The name of the Organization to be created.

    ---

- **`slug?`** `string`

  The optional slug of the Organization to be created.


#### Example

```js
await clerk.createOrganization({ name: 'test' })
```

### `getOrganization()`

Retrieves information for a specific Organization.

```typescript
function getOrganization(organizationId: string): Promise
```

#### Parameters

- **`organizationId`** `string`

  The ID of the Organization to be found.


#### Example

The following example demonstrates how to retrieve information about the Active Organization.

```js
await clerk.getOrganization(clerk.organization.id)
```

### `handleEmailLinkVerification()`

Handles the completion of an email link verification flow by processing the verification results from the redirect URL query parameters. This method should be called after the user is redirected back from visiting the verification link in their email.

```typescript
function handleEmailLinkVerification(
  params: handleEmailLinkVerificationParams,
  customNavigate?: ((to: string) => Promise<unknown>) | undefined,
): Promise<unknown>
```

The `handleEmailLinkVerification()` method finalizes an email verification flow that begins when a user initiates email verification and ends when they visit the verification link.

Email verification can be completed on any device - not necessarily the one where it was initiated. For example, a user could start verification on desktop but click the email link on mobile.

When a user visits the verification link, they are redirected to the URL specified during flow initialization. Clerk appends these query parameters to the URL:

- `__clerk_status`: The verification outcome:
  - `verified`: Verification succeeded.
  - `failed`: Verification failed.
  - `expired`: Link expired.
  - `client_mismatch`: Device/browser mismatch (only if [same device verification](/guides/secure/best-practices/protect-email-links) is enabled).
- `__clerk_created_session`: ID of any new session created. Since verification can happen on a different device, this session may not appear in [`Client.sessions`](/reference/javascript/client#properties).

The method handles the verification outcome as follows:

1. On successful verification, it:
   - Determines if sign-in/sign-up is complete
   - Redirects accordingly using the provided URLs (both optional):
     - `redirectUrlComplete`: URL for completed sign-in/sign-up.
     - `redirectUrl`: URL if there are further requirements for the sign-in/sign-up attempt, such as MFA.
   - Executes an optional callback if verification happened on another device.

1. On verification failure:
   - Throws an [`EmailLinkError`](/guides/development/custom-flows/authentication/email-links).
   - Error code indicates if link expired or verification failed.

Take a look at the function parameters below for more usage details.

#### Parameters

- **`params`** [`handleEmailLinkVerificationParams`](#handle-email-link-verification-params)

  Allows you to define the URLs where the user should be redirected to on successful verification or pending/completed sign-up or sign-in attempts. If the email link is successfully verified on another device, there's a callback function parameter that allows custom code execution.

    ---

- **`customNavigate?`** `(to: string) => Promise<unknown>`

  A function that overrides Clerk's default navigation behavior, allowing custom handling of navigation during sign-up and sign-in flows.


#### `handleEmailLinkVerificationParams`

- **`redirectUrlComplete?`** `string | undefined`

  The full URL to navigate to after successful email link verification on completed sign-up or sign-in on the same device.

    ---

- **`redirectUrl?`** `string | undefined`

  The full URL to navigate to after successful email link verification on the same device, but without completing sign-in or sign-up.

    ---

- **`onVerifiedOnOtherDevice?`** `() => void`

  Callback function to be executed after successful email link verification on another device.


#### Example

See the [custom flow](/guides/development/custom-flows/authentication/email-links) guide for a comprehensive example of how to use the `handleEmailLinkVerification()` method.

### `handleRedirectCallback()`

Completes a custom OAuth flow that was started by calling either [`SignIn.authenticateWithRedirect(params)`](/reference/javascript/sign-in) or [`SignUp.authenticateWithRedirect(params)`](/reference/javascript/sign-up).

```typescript
function handleRedirectCallback(
  params: HandleOAuthCallbackParams,
  customNavigate?: ((to: string) => Promise<unknown>) | undefined,
): Promise<unknown>
```

#### Parameters

- **`params`** [`HandleOAuthCallbackParams`](#handle-o-auth-callback-params)

  Additional props that define where the user will be redirected to at the end of a successful OAuth flow.

    ---

- **`customNavigate`** `(to: string) => Promise<unknown>`

  A function that overrides Clerk's default navigation behavior, allowing custom handling of navigation during sign-up and sign-in flows.


#### `HandleOAuthCallbackParams`

- **`continueSignUpUrl?`** `string | undefined | null`

  The full URL or path to navigate to if the sign up requires additional information.

    ---

- **`signInUrl?`** `string`

  The full URL or path where the `` component is mounted.

    ---

- **`signUpUrl?`** `string`

  The full URL or path where the `` component is mounted.

    ---

- **`signInFallbackRedirectUrl?`** `string`

  The fallback URL to redirect to after the user signs in, if there's no `redirect_url` in the path already. Defaults to `/`. It's recommended to use [the environment variable](/guides/development/clerk-environment-variables#sign-in-and-sign-up-redirects) instead.

    ---

- **`signUpFallbackRedirectUrl?`** `string`

  The fallback URL to redirect to after the user signs up, if there's no `redirect_url` in the path already. Defaults to `/`. It's recommended to use [the environment variable](/guides/development/clerk-environment-variables#sign-in-and-sign-up-redirects) instead.

    ---

- **`signInForceRedirectUrl?`** `string`

  If provided, this URL will always be redirected to after the user signs in. It's recommended to use [the environment variable](/guides/development/clerk-environment-variables#sign-in-and-sign-up-redirects) instead.

    ---

- **`signUpForceRedirectUrl?`** `string`

  If provided, this URL will always be redirected to after the user signs up. It's recommended to use [the environment variable](/guides/development/clerk-environment-variables#sign-in-and-sign-up-redirects) instead.

    ---

- **`firstFactorUrl?`** `string | undefined`

  The full URL or path to navigate to during sign in, if first factor verification is required.

    ---

- **`secondFactorUrl?`** `string | undefined`

  The full URL or path to navigate to during sign in, if [multi-factor authentication](/guides/configure/auth-strategies/sign-up-sign-in-options#multi-factor-authentication) is enabled.

    ---

- **`resetPasswordUrl?`** `string`

  The full URL or path to navigate to during sign in, if the user is required to reset their password.

    ---

- **`transferable?`** `boolean`

  A boolean that indicates whether or not sign in attempts are transferable to the sign up flow. Defaults to `true`. When set to `false`, prevents opaque sign ups when a user attempts to sign in via OAuth with an email that doesn't exist.

    ---

- **`verifyEmailAddressUrl?`** `string | undefined | null`

  The full URL or path to navigate to after requesting email verification.

    ---

- **`verifyPhoneNumberUrl?`** `string | undefined | null`

  The full URL or path to navigate to after requesting phone verification.


#### Example

```js
await clerk.handleRedirectCallback({
  signInForceRedirectUrl: '/dashboard',
  signUpForceRedirectUrl: '/dashboard',
})
```

See the [custom flow](/guides/development/custom-flows/authentication/oauth-connections) guide for implementation details on how to implement a custom OAuth flow.

### `handleUnauthenticated()`

Handles a 401 response from [Frontend API](/reference/frontend-api) by refreshing the client and session object accordingly.

```typescript
function handleUnauthenticated(opts?: { broadcast: boolean }): Promise<unknown>
```

#### Example

```js
await clerk.handleUnauthenticated()
```

### `joinWaitlist()`

Create a new waitlist entry programmatically. Requires that you set your app's sign-up mode to [**Waitlist**](/guides/secure/restricting-access#waitlist) in the Clerk Dashboard.

```typescript
function joinWaitlist({ emailAddress }: JoinWaitlistParams): Promise
```

#### Parameters

- **`emailAddress`** `string`

  The email address of the user you want to add in the waitlist.


#### Example

```js
await clerk.joinWaitlist({ emailAddress: 'user@example.com' })
```

### `load()`

Initializes the `Clerk` object and loads all necessary environment configuration and instance settings from the [Frontend API](/reference/frontend-api).

You must call this method before using the `Clerk` object in your code. Refer to the [quickstart guide](/js-frontend/getting-started/quickstart) for more information.

```typescript
function load(options?: ClerkOptions): Promise<void>
```

#### `ClerkOptions`

The `load()` method accepts an optional object that accepts the following props. All props are optional.

- **`appearance`** <code>[Appearance](/guides/customizing-clerk/appearance-prop/overview) | undefined</code>

  Optional object to style your components. Will only affect \[Clerk components]\[components-ref] and not \[Account Portal]\[ap-ref] pages.

    ---

- **`localization`** <code>[Localization](/guides/customizing-clerk/localization) | undefined</code>

  Optional object to localize your components. Will only affect \[Clerk components]\[components-ref] and not \[Account Portal]\[ap-ref] pages.

    ---

- **`routerPush?`** `(to: string) => Promise<unknown> | void`

  A function which takes the destination path as an argument and performs a "push" navigation.

    ---

- **`routerReplace?`** `(to: string) => Promise<unknown> | void`

  A function which takes the destination path as an argument and performs a "replace" navigation.

    ---

- **`polling`** `boolean | undefined`

  Dictates if we should poll against Clerk's backend every 5 minutes. Defaults to `true`.

    ---

- **`selectInitialSession`** <code>((client: \[Client]\[client-ref]) => Session | null) | undefined</code>

  An optional function which allows you to control which active session is the initial session to base a user's state off of. Defaults to the first session in the client's sessions array.

    ---

- **`standardBrowser`** `boolean | undefined`

  Controls if ClerkJS will load with the standard browser set up using Clerk cookies. Defaults to `true`.

    ---

- **`supportEmail`** `string | undefined`

  Optional support email for display in authentication screens.

    ---

- **`touchSession`** `boolean | undefined`

  Indicates whether the session should be "touched" when user interactions occur, used to record these interactions. Defaults to `true`.

    ---

- **`signInUrl`** `string | undefined`

  The default URL to use to direct to when the user signs in. It's recommended to use [the environment variable](/guides/development/clerk-environment-variables#sign-in-and-sign-up-redirects) instead.

    ---

- **`signUpUrl`** `string | undefined`

  The default URL to use to direct to when the user signs up. It's recommended to use [the environment variable](/guides/development/clerk-environment-variables#sign-in-and-sign-up-redirects) instead.

    ---

- **`signInForceRedirectUrl?`** `string`

  If provided, this URL will always be redirected to after the user signs in. It's recommended to use [the environment variable](/guides/development/clerk-environment-variables#sign-in-and-sign-up-redirects) instead.

    ---

- **`signUpForceRedirectUrl?`** `string`

  If provided, this URL will always be redirected to after the user signs up. It's recommended to use [the environment variable](/guides/development/clerk-environment-variables#sign-in-and-sign-up-redirects) instead.

    ---

- **`signInFallbackRedirectUrl?`** `string`

  The fallback URL to redirect to after the user signs in, if there's no `redirect_url` in the path already. Defaults to `/`. It's recommended to use [the environment variable](/guides/development/clerk-environment-variables#sign-in-and-sign-up-redirects) instead.

    ---

- **`signUpFallbackRedirectUrl?`** `string`

  The fallback URL to redirect to after the user signs up, if there's no `redirect_url` in the path already. Defaults to `/`. It's recommended to use [the environment variable](/guides/development/clerk-environment-variables#sign-in-and-sign-up-redirects) instead.

    ---

- **`afterSignOutUrl?`** `string`

  The full URL or path to navigate to after a successful sign-out.

    ---

- **`allowedRedirectOrigins?`** `Array<string | RegExp>`

  An optional array of domains to validate user-provided redirect URLs against. If no match is made, the redirect is considered unsafe and the default redirect will be used with a warning logged in the console.

    ---

- **`allowedRedirectProtocols?`** `Array<string>`

  An optional array of protocols to validate user-provided redirect URLs against. If no match is made, the redirect is considered unsafe and the default redirect will be used with a warning logged in the console.

    ---

- **`isSatellite`** `boolean | ((url: URL) => boolean) | undefined`

  Clerk flag for satellite apps. Experimental.

    ---

- **`telemetry?`** `false | { disabled?: boolean; debug?: boolean } | undefined`

  Controls whether or not Clerk will collect [telemetry data](/guides/how-clerk-works/security/clerk-telemetry).


#### Example

```js
await clerk.load()
```

### `navigate()`

Helper method which will use the custom push navigation function of your application to navigate to the provided URL or relative path.

Returns a promise that can be `await`ed in order to listen for the navigation to finish. The inner value should not be relied on, as it can change based on the framework it's used within.

```typescript
function navigate(to: string | undefined): Promise<unknown>
```

#### Example

```js
await clerk.navigate('/dashboard')
```

#### Parameters

- **`to`** `string | undefined`

  The route to navigate to.


### `on()`

Registers an event handler for a specific Clerk event.

```ts
type OnEventListener = <E extends ClerkEvent>(
  event: E,
  handler: EventHandler<E>,
  opt?: {
    notify: boolean
  },
) => void
```

#### Example

```js
window.Clerk.on('status', (status) => {})
window.Clerk.on('status', (status) => {}, { notify: true })
```

#### Parameters

- **`event`** `E`

  The event to listen to. Currently, the only supported event is `status`.

    ---

- **`handler`** `EventHandler<E>`

  The handler to call when the event is triggered.

    ---

- **`opt?`** `{ notify: boolean }`

  An optional object to control the behavior of the event handler. If true, and the event was previously dispatched, handler will be called immediately with the latest payload


### `off()`

Removes an event handler for a specific Clerk event.

```ts
type OffEventListener = <E extends ClerkEvent>(event: E, handler: EventHandler<E>) => void
```

#### Example

```js
window.Clerk.off('status')
window.Clerk.off('status', (status) => {})
```

#### Parameters

- **`event`** `E`

  The event to remove the handler from. Currently, the only supported event is `status`.

    ---

- **`handler`** `EventHandler<E>`

  The handler to remove.


### `redirectToCreateOrganization()`

Redirects to the configured URL where [``](/reference/components/organization/create-organization) is mounted. This method uses the [`navigate()`](#navigate) method under the hood.

Returns a promise that can be `await`ed in order to listen for the navigation to finish. The inner value should not be relied on, as it can change based on the framework it's used within.

```typescript
function redirectToCreateOrganization(): Promise<unknown>
```

#### Example

```js
await clerk.redirectToCreateOrganization()
```

### `redirectToOrganizationProfile()`

Redirects to the configured URL where [``](/reference/components/organization/organization-profile) is mounted. This method uses the [`navigate()`](#navigate) method under the hood.

Returns a promise that can be `await`ed in order to listen for the navigation to finish. The inner value should not be relied on, as it can change based on the framework it's used within.

```typescript
function redirectToOrganizationProfile(): Promise<unknown>
```

#### Example

```js
await clerk.redirectToOrganizationProfile()
```

### `redirectToSignIn()`

Redirects to the sign-in URL, as configured in your application's instance settings. This method uses the [`navigate()`](#navigate) method under the hood.

Returns a promise that can be `await`ed in order to listen for the navigation to finish. The inner value should not be relied on, as it can change based on the framework it's used within.

```typescript
function redirectToSignIn(options?: SignInRedirectOptions): Promise<unknown>
```

#### Parameters

- **`options?`** <code>[SignInRedirectOptions](/reference/javascript/types/sign-in-redirect-options) | undefined</code>

  Options to use in the redirect, such as `signInForceRedirectUrl` and `signInFallbackRedirectUrl`.


#### Example

```js
await clerk.redirectToSignIn({
  signInForceRedirectUrl: '/dashboard',
  signUpForceRedirectUrl: '/dashboard',
})
```

### `redirectToSignUp()`

Redirects to the sign-up URL, as configured in your application's instance settings. This method uses the [`navigate()`](#navigate) method under the hood.

Returns a promise that can be `await`ed in order to listen for the navigation to finish. The inner value should not be relied on, as it can change based on the framework it's used within.

```typescript
function redirectToSignUp(options?: SignUpRedirectOptions): Promise<unknown>
```

#### Parameters

- **`options?`** <code>[SignUpRedirectOptions](/reference/javascript/types/sign-up-redirect-options) | undefined</code>

  Options to use in the redirect, such as `signUpForceRedirectUrl` and `signUpFallbackRedirectUrl`.


#### Example

```js
await clerk.redirectToSignUp({
  signUpForceRedirectUrl: '/dashboard',
  signUpFallbackRedirectUrl: '/dashboard',
})
```

### `redirectToUserProfile()`

Returns a promise that can be `await`ed in order to listen for the navigation to finish. The inner value should not be relied on, as it can change based on the framework it's used within.

```typescript
function redirectToUserProfile(): Promise<unknown>
```

#### Example

```js
await clerk.redirectToUserProfile()
```

### `redirectWithAuth()`

Redirects to the provided URL after appending authentication credentials. For development instances, this method decorates the URL with an auth token to maintain authentication state. For production instances, the standard session cookie is used.

Returns a promise that can be `await`ed in order to listen for the navigation to finish. The inner value should not be relied on, as it can change based on the framework it's used within.

```typescript
function redirectWithAuth(to: string): Promise<unknown>
```

#### Parameters

- **`to`** `string | undefined`

  The route to navigate to


#### Example

```js
await clerk.redirectWithAuth('/dashboard')
```

### `setActive()`

A method used to set the current session and/or Organization for the client. Accepts a [`SetActiveParams`](/reference/javascript/types/set-active-params) object.

```typescript
function setActive(params: SetActiveParams): Promise<void>
```

#### Example

The `setActive()` method is most commonly used when building a [custom flow](/guides/development/custom-flows/overview) for your application.

For example, during authentication, when a user signs in or signs up successfully, a new session is created. `setActive()` needs to be used to set the new session as the active session. See the implementation of this in the [Custom authentication flow](/guides/development/custom-flows/overview) guide.

Another example is when a user switches Organizations in a multi-Organization application. `setActive()` needs to be used to set the new Organization as the Active Organization. See the implementation of this in the [Custom Organization switcher](/guides/development/custom-flows/organizations/organization-switcher) guide.

#### Using the `navigate()` parameter

Clerk relies on the `__client` cookie to authenticate requests to Clerk's Frontend API (the `clerk.` subdomain). Safari's Intelligent Tracking Prevention (ITP) limits cookies set via API responses from CNAME-cloaked subdomains to 7 days, and this cookie is subject to that limitation. This means sessions can unexpectedly expire for Safari users who don't visit your app frequently.

When using a custom `navigate()` callback with `setActive()`, use the `decorateUrl()` function to wrap your destination URLs. This enables automatic cookie refresh when needed:

```typescript
await clerk.setActive({
  session: newSession,
  navigate: ({ session, decorateUrl }) => {
    const url = decorateUrl('/dashboard')

    // decorateUrl may return an absolute URL for cookie refresh
    if (url.startsWith('http')) {
      window.location.href = url
    } else {
      window.location.href = url
    }
  },
})
```

The `decorateUrl` function:

- Returns a URL that redirects through Clerk's API to refresh the session cookie when needed.
- Returns the original URL unchanged when cookie refresh is not needed.
- Is safe to always use - it only modifies the URL when necessary.

> [!NOTE]
> If you're using a client-side router (Next.js, React Router, etc.), the `if/else` pattern above ensures full-page navigation only happens when cookie refresh is needed, preserving client-side navigation otherwise.

### `signOut()`

- In a [multi-session application](/guides/secure/session-options#multi-session-applications): Signs out the active user from all sessions
- In a single-session context: Signs out the active user from the current session

The current client will be deleted. You can specify a specific session to sign out by passing the `sessionId` parameter.

```typescript
function signOut(options?: SignOutOptions): Promise<void>
// OR
function signOut(
  signOutCallback?: () => void | Promise<any>,
  options?: SignOutOptions,
): Promise<void>
```

#### `SignOutOptions`

- **`sessionId?`** `string`

  Specify a specific session to sign out. Useful for multi-session applications.

    ---

- **`redirectUrl?`** `string`

  The full URL or path to navigate to after sign out is complete.


#### Example

```js
await clerk.signOut()
```

## Components

The `Clerk` class also contains a number of methods for interacting with prebuilt components.

### ``

- [`mountSignIn()`](/reference/components/authentication/sign-in#mount-sign-in)
- [`unmountSignIn()`](/reference/components/authentication/sign-in#unmount-sign-in)
- [`openSignIn()`](/reference/components/authentication/sign-in#open-sign-in)
- [`closeSignIn()`](/reference/components/authentication/sign-in#close-sign-in)

### ``

- [`mountSignUp()`](/reference/components/authentication/sign-up#mount-sign-up)
- [`unmountSignUp()`](/reference/components/authentication/sign-up#unmount-sign-up)
- [`openSignUp()`](/reference/components/authentication/sign-up#open-sign-up)
- [`closeSignUp()`](/reference/components/authentication/sign-up#close-sign-up)

### ``

- [`openGoogleOneTap()`](/reference/components/authentication/google-one-tap#open-google-one-tap)
- [`closeGoogleOneTap()`](/reference/components/authentication/google-one-tap#close-google-one-tap)
- [`authenticateWithGoogleOneTap()`](/reference/components/authentication/google-one-tap#authenticate-with-google-one-tap)
- [`handleGoogleOneTapCallback()`](/reference/components/authentication/google-one-tap#handle-google-one-tap-callback)

### ``

- [`mountUserAvatar()`](/reference/components/user/user-avatar#mount-user-avatar)
- [`unmountUserAvatar()`](/reference/components/user/user-avatar#unmount-user-avatar)

### ``

- [`mountUserButton()`](/reference/components/user/user-button#mount-user-button)
- [`unmountUserButton()`](/reference/components/user/user-button#unmount-user-button)

### ``

- [`mountUserProfile()`](/reference/components/user/user-profile#mount-user-profile)
- [`unmountUserProfile()`](/reference/components/user/user-profile#unmount-user-profile)
- [`openUserProfile()`](/reference/components/user/user-profile#open-user-profile)
- [`closeUserProfile()`](/reference/components/user/user-profile#close-user-profile)

### ``

- [`mountOrganizationProfile()`](/reference/components/organization/organization-profile#mount-organization-profile)
- [`unmountOrganizationProfile()`](/reference/components/organization/organization-profile#unmount-organization-profile)
- [`openOrganizationProfile()`](/reference/components/organization/organization-profile#open-organization-profile)
- [`closeOrganizationProfile()`](/reference/components/organization/organization-profile#close-organization-profile)

### ``

- [`mountOrganizationSwitcher()`](/reference/components/organization/organization-switcher#mount-organization-switcher)
- [`unmountOrganizationSwitcher()`](/reference/components/organization/organization-switcher#unmount-organization-switcher)

### ``

- [`mountCreateOrganization`](/reference/components/organization/create-organization#mount-create-organization)
- [`unmountCreateOrganization`](/reference/components/organization/create-organization#unmount-create-organization)
- [`openCreateOrganization`](/reference/components/organization/create-organization#open-create-organization)
- [`closeCreateOrganization`](/reference/components/organization/create-organization#close-create-organization)

### ``

- [`mountOrganizationList`](/reference/components/organization/organization-list#mount-organization-list)
- [`unmountOrganizationList`](/reference/components/organization/organization-list#unmount-organization-list)

### ``

- [`mountWaitlist()`](/reference/components/authentication/waitlist#mount-waitlist)
- [`unmountWaitlist()`](/reference/components/authentication/waitlist#unmount-waitlist)
- [`openWaitlist()`](/reference/components/authentication/waitlist#open-waitlist)
- [`closeWaitlist()`](/reference/components/authentication/waitlist#close-waitlist)

[client-ref]: /docs/reference/javascript/client

[session-ref]: /docs/reference/javascript/session

[user-ref]: /docs/reference/javascript/user

[organization-ref]: /docs/reference/javascript/organization

[api-ref]: /docs/reference/javascript/api-keys

[billing-ref]: /docs/reference/javascript/billing

[components-ref]: /docs/reference/components/overview

[ap-ref]: /docs/guides/account-portal/overview
