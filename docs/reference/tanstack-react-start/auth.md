# auth()


> The auth() helper retrieves the authentication state allowing you to protect your API routes or gather relevant data.

The `auth()` helper returns the [`Auth`](/reference/backend/types/auth-object) object of the currently active user.

## Parameters

- **`opts?`** `{acceptsToken: TokenType, treatPendingAsSignedOut: boolean }`

  An optional object that can be used to configure the behavior of the `auth()` function. It accepts the following properties:

- **`acceptsToken?`: The type of authentication token(s) to accept. Valid values are:**

- **`'session_token'` - authenticates a user session.** `'oauth_token'` - authenticates a machine request using OAuth. `'m2m_token'` - authenticates a machine to machine request. `'api_key'` - authenticates a machine request using API keys.

  Can be set to:

    - A single token type.
    - An array of token types.

- **`'any'` to accept all available token types.**

  Defaults to `'session_token'`.

- **`treatPendingAsSignedOut?`: A boolean that indicates whether to treat [`pending` session status](/reference/javascript/types/session-status#properties) as signed out. Defaults to `true`.**


## Returns

`auth()` returns the [`Auth`](/reference/backend/types/auth-object) object.

## Usage

See the [dedicated guide](/tanstack-react-start/guides/users/reading#server-side) for example usage.
