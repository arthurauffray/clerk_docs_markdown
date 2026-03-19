# usePlans()


> Access Plans in your React application with Clerk's usePlans() hook.

> [!WARNING]
>
> Billing is currently in Beta and its APIs are experimental and may undergo breaking changes. To mitigate potential disruptions, we recommend [pinning](/pinning) your SDK and `clerk-js` package versions.


The `usePlans()` hook provides access to the Subscription Plans available in your application. It returns a paginated list of Plans and includes methods for managing them.

## Parameters

`usePlans()` accepts a single optional object with the following properties:

## Returns

`usePlans()` returns an object with the following properties:

## Examples

### Basic usage

The following example shows how to fetch and display available Plans.


  ```tsx
// Filename: app/billing/plans/page.tsx

  'use client'

  import { usePlans } from '@clerk/nextjs/experimental'

  export default function PlansList() {
    const { data, isLoading, hasNextPage, fetchNext, hasPreviousPage, fetchPrevious } = usePlans({
      for: 'user',
      pageSize: 10,
    })

    if (isLoading) {
      return <div>Loading plans...</div>
    }

    return (
      <ul>
        {data?.map((plan) => (
          <li key={plan.id}>
            <h3>{plan.name}</h3>
            <p>{plan.description}</p>
            <p>Is free plan: {!plan.hasBaseFee ? 'Yes' : 'No'}</p>
            <p>
              Price per month: {plan.currency} {plan.amountFormatted}
            </p>
            <p>
              Price per year: {plan.currency} {plan.annualAmountFormatted} equivalent to{' '}
              {plan.currency} {plan.annualMonthlyAmountFormatted} per month
            </p>
            <h4>Features:</h4>
            <ul>
              {plan.features.map((feature) => (
                <li key={feature.id}>{feature.name}</li>
              ))}
            </ul>
          </li>
        ))}

        {hasNextPage && <button onClick={() => fetchNext()}>Next</button>}
        {hasPreviousPage && <button onClick={() => fetchPrevious()}>Previous</button>}
      </ul>
    )
  }
  ```


  ```tsx
// Filename: src/pages/billing/PlansList.tsx

  import { usePlans } from '@clerk/react/experimental'

  export default function PlansList() {
    const { data, isLoading, hasNextPage, fetchNext, hasPreviousPage, fetchPrevious } = usePlans({
      for: 'user',
      pageSize: 10,
    })

    if (isLoading) {
      return <div>Loading plans...</div>
    }

    return (
      <ul>
        {data?.map((plan) => (
          <li key={plan.id}>
            <h3>{plan.name}</h3>
            <p>{plan.description}</p>
            <p>Is free plan: {!plan.hasBaseFee ? 'Yes' : 'No'}</p>
            <p>
              Price per month: {plan.currency} {plan.amountFormatted}
            </p>
            <p>
              Price per year: {plan.currency} {plan.annualAmountFormatted} equivalent to{' '}
              {plan.currency} {plan.annualMonthlyAmountFormatted} per month
            </p>
            <h4>Features:</h4>
            <ul>
              {plan.features.map((feature) => (
                <li key={feature.id}>{feature.name}</li>
              ))}
            </ul>
          </li>
        ))}

        {hasNextPage && <button onClick={() => fetchNext()}>Next</button>}
        {hasPreviousPage && <button onClick={() => fetchPrevious()}>Previous</button>}
      </ul>
    )
  }
  ```


### Infinite pagination

The following example demonstrates how to implement infinite scrolling with Plans.


  ```tsx
// Filename: app/billing/plans/page.tsx

  'use client'

  import { usePlans } from '@clerk/nextjs/experimental'

  export default function InfinitePlansList() {
    const { data, isLoading, hasNextPage, fetchNext } = usePlans({
      for: 'user',
      infinite: true,
      pageSize: 2,
    })

    if (isLoading) {
      return <div>Loading plans...</div>
    }

    return (
      <div>
        <ul>
          {data?.map((plan) => (
            <li key={plan.id}>
              <h3>{plan.name}</h3>
              <p>{plan.description}</p>
              <p>Is free plan: {!plan.hasBaseFee ? 'Yes' : 'No'}</p>
              <p>
                Price per month: {plan.currency} {plan.amountFormatted}
              </p>
              <p>
                Price per year: {plan.currency} {plan.annualAmountFormatted} equivalent to{' '}
                {plan.currency} {plan.annualMonthlyAmountFormatted} per month
              </p>
              <h4>Features:</h4>
              <ul>
                {plan.features.map((feature) => (
                  <li key={feature.id}>{feature.name}</li>
                ))}
              </ul>
            </li>
          ))}
        </ul>

        {hasNextPage && <button onClick={() => fetchNext()}>Load more plans</button>}
      </div>
    )
  }
  ```


  ```tsx
// Filename: src/pages/billing/PlansList.tsx

  import { usePlans } from '@clerk/react/experimental'

  export default function InfinitePlansList() {
    const { data, isLoading, hasNextPage, fetchNext } = usePlans({
      for: 'user',
      infinite: true,
      pageSize: 2,
    })

    if (isLoading) {
      return <div>Loading plans...</div>
    }

    return (
      <div>
        <ul>
          {data?.map((plan) => (
            <li key={plan.id}>
              <h3>{plan.name}</h3>
              <p>{plan.description}</p>
              <p>Is free plan: {!plan.hasBaseFee ? 'Yes' : 'No'}</p>
              <p>
                Price per month: {plan.currency} {plan.amountFormatted}
              </p>
              <p>
                Price per year: {plan.currency} {plan.annualAmountFormatted} equivalent to{' '}
                {plan.currency} {plan.annualMonthlyAmountFormatted} per month
              </p>
              <h4>Features:</h4>
              <ul>
                {plan.features.map((feature) => (
                  <li key={feature.id}>{feature.name}</li>
                ))}
              </ul>
            </li>
          ))}
        </ul>

        {hasNextPage && <button onClick={() => fetchNext()}>Load more plans</button>}
      </div>
    )
  }
  ```


## Next steps


  - [Checkout flow with a new payment method](/guides/development/custom-flows/billing/checkout-new-payment-method)
  - Build a custom checkout flow that allows users to add a new payment method during checkout.

  ---

  - [Checkout flow for returning users](/guides/development/custom-flows/billing/checkout-existing-payment-method)
  - Build a custom checkout flow that allows users to select an existing payment method during checkout.
