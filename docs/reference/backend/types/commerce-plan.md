# CommercePlan


> The Backend CommercePlan object holds information about a Plan of your application.

> [!WARNING]
>
> Billing is currently in Beta and its APIs are experimental and may undergo breaking changes. To mitigate potential disruptions, we recommend [pinning](/pinning) your SDK and `clerk-js` package versions.


The `CommercePlan` object is similar to the [`BillingPlanResource`](/reference/javascript/types/billing-plan-resource) object as it holds information about a Plan, as well as methods for managing it. However, the `CommercePlan` object is different in that it is used in the [Backend API](/reference/backend-api/model/commerceplan) and is not directly accessible from the Frontend API.

## Properties

- **`id`** `string`

  The unique identifier for the Plan.

    ---

- **`productId`** `string`

  The ID of the product the Plan belongs to.

    ---

- **`name`** `string`

  The name of the Plan.

    ---

- **`slug`** `string`

  The URL-friendly identifier of the Plan.

    ---

- **`description`** `undefined | string`

  The description of the Plan.

    ---

- **`isDefault`** `boolean`

  Whether the Plan is the default Plan.

    ---

- **`isRecurring`** `boolean`

  Whether the Plan is recurring.

    ---

- **`hasBaseFee`** `boolean`

  Whether the Plan has a base fee.

    ---

- **`publiclyVisible`** `boolean`

  Whether the Plan is displayed in the `` component.

    ---

- **`fee`** <code>[BillingMoneyAmount](/reference/javascript/types/billing-money-amount)</code>

  The monthly fee of the Plan.

    ---

- **`annualFee`** <code>[BillingMoneyAmount](/reference/javascript/types/billing-money-amount)</code>

  The annual fee of the Plan.

    ---

- **`annualMonthlyFee`** <code>[BillingMoneyAmount](/reference/javascript/types/billing-money-amount)</code>

  The annual fee of the Plan on a monthly basis.

    ---

- **`forPayerType`** `'user' | 'org'`

  The type of payer for the Plan.

    ---

- **`features`** [`Feature[]`](/reference/backend/types/feature)

  The Features the Plan offers.
