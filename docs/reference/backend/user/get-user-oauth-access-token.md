# getUserOauthAccessToken()


> Use Clerk's JS Backend SDK to retrieve the corresponding OAuth access token for a user.

Retrieves the corresponding OAuth access token for a user that has previously authenticated with a particular OAuth provider. Returns a [`PaginatedResourceResponse`](/reference/backend/types/paginated-resource-response) object with a `data` property that contains an array of [`OauthAccessToken`](/reference/backend/types/backend-oauth-access-token) objects, and a `totalCount` property that indicates the total number of OAuth access tokens in the system for the specified user and provider.

```ts
function getUserOauthAccessToken(
  userId: string,
  provider: `${OAuthProvider}`,
): Promise>
```

## Parameters

- **`userId`** `string`

  The ID of the user to retrieve the OAuth access token for.

    ---

- **`provider`** <code>$\{[OAuthProvider](/reference/javascript/types/sso#o-auth-provider)}</code>

  The OAuth provider to retrieve the access token for. If using a custom OAuth provider, prefix the provider name with `custom_` (e.g., `custom_foo`).


## Example

> [!NOTE]
> Using `clerkClient` varies based on your framework. Refer to the [JS Backend SDK overview](/js-backend/getting-started/quickstart) for usage details, including guidance on [how to access the `userId` and other properties](/js-backend/getting-started/quickstart#get-the-user-id-and-other-properties).


```tsx
const userId = 'user_123'

const provider = 'google'

const response = await clerkClient.users.getUserOauthAccessToken(userId, provider)
```

You can also explore [the example](/guides/configure/auth-strategies/social-connections/overview#get-an-o-auth-access-token-for-a-social-provider) that demonstrates how this method retrieves a social provider's OAuth access token, enabling access to user data from both the provider and Clerk.

## Backend API (BAPI) endpoint

This method in the SDK is a wrapper around the BAPI endpoint `GET/users/{user_id}/oauth_access_tokens/{provider}`. See the [BAPI reference](/reference/backend-api/tag/users/get/users/\{user_id}/oauth_access_tokens/\{provider}) for more information.
