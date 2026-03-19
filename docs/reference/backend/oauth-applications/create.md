# create()


> Use Clerk's JS Backend SDK to create an OAuth application.

Creates a new [`OAuthApplication`](/reference/backend/types/backend-oauth-application).

```ts
function create(params: CreateOAuthApplicationParams): Promise
```

## `CreateOAuthApplicationParams`

- **`name`** `string`

  The name of the OAuth application.

    ---

- **`redirectUris?`** `string[] | null`

  An array of redirect URIs for the OAuth application.

    ---

- **`scopes?`** `string[] | null | undefined`

  Scopes for the OAuth application. Available scopes are `profile`, `email`, `public_metadata`, `private_metadata`. Defaults to `profile email`. Provide the requested scopes as a string, separated by spaces.

    ---

- **`consentScreenEnabled?`** `boolean | null | undefined`

  Specifies whether the consent screen should be displayed in the authentication flow. Cannot be disabled for dynamically registered OAuth applications. Defaults to `true`.

    ---

- **`public?`** `boolean | null | undefined`

  Indicates whether the client is public. If true, the Proof Key of Code Exchange (PKCE) flow can be used.


## Example

> [!NOTE]
> Using `clerkClient` varies based on your framework. Refer to the [JS Backend SDK overview](/js-backend/getting-started/quickstart) for usage details, including guidance on [how to access the `userId` and other properties](/js-backend/getting-started/quickstart#get-the-user-id-and-other-properties).


```tsx
const response = await clerkClient.oauthApplications.create({
  name: 'oauthapp_123',
  redirect_uris: [''],
  scopes: 'profile email public_metadata',
  public: null,
})
```

## Backend API (BAPI) endpoint

This method in the SDK is a wrapper around the BAPI endpoint `POST/oauth_applications`. See the [BAPI reference](/reference/backend-api/tag/oauth-applications/post/oauth_applications) for more information.
