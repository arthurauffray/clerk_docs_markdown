# createAllowlistIdentifier()


> Use Clerk's JS Backend SDK to add a new identifier to the allowlist.

Adds a new identifier to the allowlist. Returns the created [`AllowlistIdentifier`](/reference/backend/types/backend-allowlist-identifier) object.

```ts
function createAllowlistIdentifier(
  params: AllowlistIdentifierCreateParams,
): Promise
```

## `AllowlistIdentifierCreateParams`

- **`identifier`** `string`

  The identifier to be added in the allowlist. Can be an email address, a phone number in international [E.164](https://en.wikipedia.org/wiki/E.164) format, a domain, or a Web3 wallet address.

    ---

- **`notify`** `boolean`

  Whether the given identifier will receive an invitation to join the application. Note that this only works for email address and phone number identifiers. Not available for wildcard identifiers or Web3 wallet addresses. Defaults to `true`.


## Example

> [!NOTE]
> Using `clerkClient` varies based on your framework. Refer to the [JS Backend SDK overview](/js-backend/getting-started/quickstart) for usage details, including guidance on [how to access the `userId` and other properties](/js-backend/getting-started/quickstart#get-the-user-id-and-other-properties).


```tsx
const response = await clerkClient.allowlistIdentifiers.createAllowlistIdentifier({
  identifier: 'test@example.com',
  notify: false,
})
```

## Backend API (BAPI) endpoint

This method in the SDK is a wrapper around the BAPI endpoint `POST/allowlist-identifiers`. See the [BAPI reference](/reference/backend-api/tag/allow-list-block-list/post/allowlist_identifiers) for more information.
