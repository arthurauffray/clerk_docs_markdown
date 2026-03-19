# getPlanList()


> Use Clerk's JS Backend SDK to retrieve a list of Billing Plans.

> [!WARNING]
>
> Billing is currently in Beta and its APIs are experimental and may undergo breaking changes. To mitigate potential disruptions, we recommend [pinning](/pinning) your SDK and `clerk-js` package versions.


Retrieves a list of Billing Plans. Returns a [`PaginatedResourceResponse`](/reference/backend/types/paginated-resource-response) object with a `data` property that contains an array of [`CommercePlan`](/reference/backend/types/commerce-plan) objects, and a `totalCount` property that indicates the total number of Billing Plans.

```ts
function getPlanList(
  params?: GetOrganizationListParams,
): Promise>
```

## `GetOrganizationListParams`

- **`limit?`** `number`

  The number of results to return. Must be an integer greater than zero and less than 501. Defaults to `10`.

    ---

- **`offset?`** `number`

  Skip the first `offset` results when paginating. Needs to be an integer greater or equal to zero. Defaults to `0`.

    ---

- **`payerType?`** `'org' | 'user'`

  Filter Plans by payer type.


## Example

> [!NOTE]
> Using `clerkClient` varies based on your framework. Refer to the [JS Backend SDK overview](/js-backend/getting-started/quickstart) for usage details, including guidance on [how to access the `userId` and other properties](/js-backend/getting-started/quickstart#get-the-user-id-and-other-properties).


```tsx
const { data, totalCount } = await clerkClient.billing.getPlanList({ payerType: 'org' })
```

## Backend API (BAPI) endpoint

This method in the SDK is a wrapper around the BAPI endpoint `GET /commerce/plans`. See the [BAPI reference](/reference/backend-api/tag/commerce/get/commerce/plans) for more information.
