# getAuth()


> Access and manage the current user's authentication state in your React application with Clerk's getAuth() helper.

The `getAuth()` helper retrieves the current user's authentication state from the request object.

## Parameters

- **`args`** `LoaderFunctionArgs`

  The arguments object.

    ---

- **`opts?`** `{acceptsToken: TokenType, treatPendingAsSignedOut: boolean }`

  An optional object that can be used to configure the behavior of the `getAuth()` function. It accepts the following properties:

- **`acceptsToken?`: The type of authentication token(s) to accept. Valid values are:**

- **`'session_token'` - authenticates a user session.** `'oauth_token'` - authenticates a machine request using OAuth. `'m2m_token'` - authenticates a machine to machine request. `'api_key'` - authenticates a machine request using API keys.

  Can be set to:

    - A single token type.
    - An array of token types.

- **`'any'` to accept all available token types.**

  Defaults to `'session_token'`.

- **`treatPendingAsSignedOut?`: A boolean that indicates whether to treat [`pending` session status](/reference/javascript/types/session-status#properties) as signed out. Defaults to `true`.**


## Returns

`getAuth()` returns the `Auth` object. This JavaScript object contains important information like the current user's session ID, user ID, and Organization ID. Learn more about the [`Auth` object](/reference/backend/types/auth-object).

## Usage

See the [dedicated guide](/react-router/guides/users/reading#server-side) for example usage.
