# useSSO()


> Clerk's useSSO() hook is used to create a new SSO flow.

The `useSSO()` hook is used to create a new SSO flow. It can be used in both web and native apps.

## Returns

The `useSSO()` hook returns the `startSSOFlow()` method, which you can use to initiate the SSO flow.

### `startSSOFlow()`

`startSSOFlow()` has the following function signature:

```ts
function startSSOFlow(startSSOFlowParams: StartSSOFlowParams): Promise
```

#### Parameters

`startSSOFlow()` accepts the following parameters (`StartSSOFlowParams`):

- **`strategy`** [`OAuthStrategy`](/reference/javascript/types/sso#o-auth-strategy) | [`EnterpriseSSOStrategy`](/reference/javascript/types/sso#enterprise-sso-strategy)

  The strategy to use for authentication. The following strategies are supported:

- **`'oauth_<provider>'`: The user will be authenticated with their [social connection account](/guides/configure/auth-strategies/social-connections/overview). [See a list of supported values for `<provider>`](/reference/javascript/types/sso#o-auth-provider).** `'enterprise_sso'`: The user will be authenticated either through SAML, EASIE, or OIDC depending on the configuration of their [enterprise SSO account](/guides/configure/auth-strategies/enterprise-connections/overview).

  ---

- **`identifier?`** string

  **Required** if `strategy` is set to `'enterprise_sso'`. The [identifier](/guides/configure/auth-strategies/sign-up-sign-in-options) of the user.

    ---

- **`redirectUrl?`** `string`

  The full URL or path to redirect to after the SSO flow is complete. If not specified, defaults to `sso-callback` path.

    ---

- **`unsafeMetadata?`** [`SignUpUnsafeMetadata`](/reference/javascript/types/metadata#sign-up-unsafe-metadata)

  Metadata that can be read and set from the frontend and the backend. Once the authentication process is complete, the value of this field will be automatically copied to the created user's unsafe metadata (`User.unsafeMetadata`). One common use case is to collect custom information about the user during the authentication process and store it in this property. Read more about [unsafe metadata](/guides/users/extending#unsafe-metadata).


#### Returns

`startSSOFlow()` returns the following:

- **`createdSessionId`** `string | null`

  The ID of the session that was created.

    ---

- **`authSessionResult?`** `WebBrowser.WebBrowserAuthSessionResult | undefined`

  The result of the web browser session. See the [Expo WebBrowser documentation](https://docs.expo.dev/versions/latest/sdk/webbrowser/#webbrowserauthsessionresult) for more details.

    ---

- **`setActive?`** `(params: SetActiveParams) => Promise<void>`

  A method used to set the active session and/or Organization. Accepts a [`SetActiveParams`](/reference/javascript/types/set-active-params) object.

    ---

- **`signIn?`** <code>[SignIn](/reference/javascript/sign-in) | undefined</code>

  The [`SignIn`](/reference/javascript/sign-in) object that was created, which holds the state of the current sign-in and provides helper methods to navigate and complete the sign-in process.

    ---

- **`signUp?`** <code>[SignUp](/reference/javascript/sign-up) | undefined</code>

  The [`SignUp`](/reference/javascript/sign-up) object that was created, which holds the state of the current sign-up and provides helper methods to navigate and complete the sign-up process.


## How to use the `useSSO()` hook

For detailed examples of how to use the `useSSO()` hook, see the following guides:

- [OAuth custom flow](/guides/development/custom-flows/authentication/oauth-connections)
- [Enterprise SSO custom flow](/guides/development/custom-flows/authentication/enterprise-connections)
