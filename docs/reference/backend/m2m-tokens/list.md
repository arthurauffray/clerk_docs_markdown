# list()


> Use Clerk's JS Backend SDK to get a list of M2M tokens for your a given machine.

Retrieves a list of M2M tokens for a given machine. Returns a [`PaginatedResourceResponse`](/reference/backend/types/paginated-resource-response) object with a `data` property that contains an array of [M2M token](/guides/development/machine-auth/m2m-tokens) objects, and a `totalCount` property that indicates the total number of M2M tokens in the system. This endpoint can be authenticated by either a Machine Secret Key or by a Clerk Secret Key.

- When fetching M2M tokens with a Machine Secret Key, only tokens associated with the authenticated machine can be retrieved.
- When fetching M2M tokens with a Clerk Secret Key, tokens for any machine in the instance can be retrieved.

> [!NOTE]
> JWT tokens are not stored by Clerk, so they cannot be fetched via the **list** endpoint (`clerkClient.m2m.list()`). The list endpoint will only return opaque tokens. Additionally, since JWT verification happens client-side, Clerk cannot track `last_used_at` for JWT tokens.


```ts
function list(queryParams: GetM2MTokenListParams): Promise>
```

## `GetM2MTokenListParams`

- **`subject`** `string`

  The machine ID to query M2M tokens by.

    ---

- **`machineSecretKey?`** `string`

  Custom machine secret key for authentication. If not provided, the SDK will use the value from the environment variable.

    ---

- **`revoked?`** `boolean`

  Whether to include revoked M2M tokens. Defaults to `false`.

    ---

- **`expired?`** `boolean`

  Whether to include expired M2M tokens. Defaults to `false`.

    ---

- **`limit?`** `number`

  The maximum number of M2M tokens to return. Defaults to `10`.

    ---

- **`offset?`** `number`

  The number of M2M tokens to skip before returning results. Defaults to `0`.


## Example

> [!NOTE]
> Using `clerkClient` varies based on your framework. Refer to the [JS Backend SDK overview](/js-backend/getting-started/quickstart) for usage details, including guidance on [how to access the `userId` and other properties](/js-backend/getting-started/quickstart#get-the-user-id-and-other-properties).


### List M2M tokens for a machine

```tsx
const machineId = 'mt_123'

const m2mTokens = await clerkClient.m2m.list({
  subject: machineId,
})
```

### List M2M tokens for a machine, including revoked and expired ones

```tsx
const machineId = 'mt_123'

const m2mTokens = await clerkClient.m2m.list({
  subject: machineId,
  revoked: true,
  expired: true,
})
```

### List M2M tokens for a machine with pagination

```tsx
const machineId = 'mt_123'

const m2mTokens = await clerkClient.m2m.list({
  subject: machineId,
  limit: 20,
  offset: 0,
})
```

## Backend API (BAPI) endpoint

This method in the SDK is a wrapper around the BAPI endpoint `GET/m2m_tokens`. See the [BAPI reference](/reference/backend-api/tag/m2m-tokens/get/m2m_tokens) for more information.
