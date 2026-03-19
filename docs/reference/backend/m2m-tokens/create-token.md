# createToken()


> Use Clerk's JS Backend SDK to create a M2M token.

Creates a new [M2M token](/guides/development/machine-auth/m2m-tokens). Must be authenticated via a Machine Secret Key.

```ts
function createToken(params?: CreateM2MTokenParams): Promise
```

## `CreateM2MTokenParams`

- **`machineSecretKey?`** `string`

  Custom machine secret key for authentication. If not provided, the SDK will use the value from the environment variable.

    ---

- **`tokenFormat?`** `'opaque' | 'jwt'`

  The format of the token. Defaults to `'opaque'`. Set to `'jwt'` to create a [JSON Web Token](/guides/how-clerk-works/tokens-and-signatures#json-web-tokens-jwts) that can be verified locally without a network request. For a detailed comparison of the two formats, see [Token formats](/guides/development/machine-auth/token-formats).

    ---

- **`secondsUntilExpiration?`** `number | null`

  Number of seconds until the token expires. Defaults to `null` (token does not expire).

    ---

- **`claims?`** `Record<string, unknown> | null`

  Additional custom claims to include in the token payload.


## Example

> [!NOTE]
> Using `clerkClient` varies based on your framework. Refer to the [JS Backend SDK overview](/js-backend/getting-started/quickstart) for usage details, including guidance on [how to access the `userId` and other properties](/js-backend/getting-started/quickstart#get-the-user-id-and-other-properties).


```ts
const m2mToken = await clerkClient.m2m.createToken()
console.log(m2mToken)
```

By default, `createToken()` creates an opaque token. To create a JWT instead, pass `tokenFormat: 'jwt'`:

```ts
const m2mToken = await clerkClient.m2m.createToken({
  tokenFormat: 'jwt',
})
console.log(m2mToken)
```

While it is strongly recommended to use environment variables for security, if you need to pass in the machine secret key directly rather than using an environment variable, you can do so by passing it as an argument to the `createToken()` method, as shown in the following example:

```ts
const m2mToken = await clerkClient.m2m.createToken({
  machineSecretKey: 'ak_xxx',
})
console.log(m2mToken)
```


## Backend API (BAPI) endpoint

This method in the SDK is a wrapper around the BAPI endpoint `POST/m2m_tokens`. See the [BAPI reference](/reference/backend-api/tag/m2m-tokens/post/m2m_tokens) for more information.
