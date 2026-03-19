# Billing` object


> The Billing object provides methods for managing billing for a user or organization.

> [!WARNING]
>
> Billing is currently in Beta and its APIs are experimental and may undergo breaking changes. To mitigate potential disruptions, we recommend [pinning](/pinning) your SDK and `clerk-js` package versions.


The `Billing` object provides methods for managing billing for a user or organization.

> [!NOTE]
> If an `orgId` parameter is not provided, the methods will automatically use the current user's ID.

## Methods

### `getPaymentAttempt()`

Returns details of a specific payment attempt for the current user or supplied Organization. Returns a [`BillingPaymentResource`](/reference/javascript/types/billing-payment-resource) object.

```ts
function getPaymentAttempt(params: GetPaymentAttemptParams): Promise
```

#### `GetPaymentAttemptParams`

- **`id`** `string`

  The ID of the payment attempt to fetch.

    ---

- **`orgId?`** `string`

  The Organization ID to perform the request on.


#### Example

```js
await clerk.billing.getPaymentAttempt({
  id: 'payment_attempt_123',
})
```

### `getPaymentAttempts()`

Returns a list of payment attempts for the current user or supplied Organization. Returns a [`ClerkPaginatedResponse`](/reference/javascript/types/clerk-paginated-response) of [`BillingPaymentResource`](/reference/javascript/types/billing-payment-resource) objects.

```ts
function getPaymentAttempts(
  params: GetPaymentAttemptsParams,
): Promise>
```

#### `GetPaymentAttemptsParams`

- **`initialPage?`** `number`

  A number that specifies which page to fetch. For example, if `initialPage` is set to `10`, it will skip the first 9 pages and fetch the 10th page.

    ---

- **`pageSize?`** `number`

  A number that specifies the maximum number of results to return per page.

    ---

- **`orgId?`** `string`

  The Organization ID to perform the request on.


#### Example

```js
await clerk.billing.getPaymentAttempts()
```

### `getPlan()`

Returns a Billing Plan by ID. Returns a [`BillingPlanResource`](/reference/javascript/types/billing-plan-resource) object.

```ts
function getPlan(params: GetPlanParams): Promise
```

#### `GetPlanParams`

- **`id`** `string`

  The ID of the Plan to fetch.


#### Example

```js
await clerk.billing.getPlan({
  id: 'plan_123',
})
```

### `getPlans()`

Returns a list of all publically visible Billing Plans. Returns a [`ClerkPaginatedResponse`](/reference/javascript/types/clerk-paginated-response) of [`BillingPlanResource`](/reference/javascript/types/billing-plan-resource) objects.

```ts
function getPlans(params?: GetPlansParams): Promise>
```

#### `GetPlansParams`

- **`for?`** `"user" | "organization"`

  The type of payer for the Plans.

    ---

- **`initialPage?`** `number`

  A number that specifies which page to fetch. For example, if `initialPage` is set to `10`, it will skip the first 9 pages and fetch the 10th page.

    ---

- **`pageSize?`** `number`

  A number that specifies the maximum number of results to return per page.


#### Example

```js
await clerk.billing.getPlans()
```

### `getStatement()`

Returns a billing statement by ID. Returns a [`BillingStatementResource`](/reference/javascript/types/billing-statement-resource) object.

```ts
function getStatement(params: GetStatementParams): Promise
```

#### `GetStatementParams`

- **`id`** `string`

  The ID of the statement to fetch.

    ---

- **`orgId?`** `string`

  The Organization ID to perform the request on.


#### Example

```js
await clerk.billing.getStatement({
  id: 'statement_123',
})
```

### `getStatements()`

Returns a list of billing statements for the current user or supplied Organization. Returns a [`ClerkPaginatedResponse`](/reference/javascript/types/clerk-paginated-response) of [`BillingStatementResource`](/reference/javascript/types/billing-statement-resource) objects.

```ts
function getStatements(
  params: GetStatementsParams,
): Promise>
```

#### `GetStatementsParams`

- **`initialPage?`** `number`

  A number that specifies which page to fetch. For example, if `initialPage` is set to `10`, it will skip the first 9 pages and fetch the 10th page.

    ---

- **`pageSize?`** `number`

  A number that specifies the maximum number of results to return per page.

    ---

- **`orgId?`** `string`

  The Organization ID to perform the request on.


#### Example

```js
await clerk.billing.getStatements()
```

### `getSubscription()`

Returns the main Billing Subscription for the current user or supplied Organization. Returns a [`BillingSubscriptionResource`](/reference/javascript/types/billing-subscription-resource) object.

```ts
function getSubscription(params: GetSubscriptionParams): Promise
```

#### `GetSubscriptionParams`

- **`orgId?`** `string`

  The Organization ID to perform the request on.


#### Example

```js
await clerk.billing.getSubscription({
  orgId: 'org_123',
})
```

### `startCheckout()`

Creates a new billing checkout for the current user or supplied Organization. Returns a [`BillingCheckoutResource`](/reference/javascript/types/billing-checkout-resource) object.

```ts
function startCheckout(params: CreateCheckoutParams): Promise
```

#### `CreateCheckoutParams`

- **`planId`** `string`

  The unique identifier for the Plan.

    ---

- **`planPeriod`** `"month" | "annual"`

  The billing period for the Plan.

    ---

- **`orgId?`** `string`

  The Organization ID to perform the request on.


#### Example

```js
await clerk.billing.startCheckout({
  planId: 'plan_123',
  planPeriod: 'month',
})
```
