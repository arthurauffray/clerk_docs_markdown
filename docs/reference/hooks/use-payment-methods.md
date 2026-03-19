# usePaymentMethods()


> Access and manage payment methods in your React application with Clerk's usePaymentMethods() hook.

> [!WARNING]
>
> Billing is currently in Beta and its APIs are experimental and may undergo breaking changes. To mitigate potential disruptions, we recommend [pinning](/pinning) your SDK and `clerk-js` package versions.


The `usePaymentMethods()` hook provides access to the payment methods associated with a user or Organization. It returns a paginated list of payment methods and includes methods for managing them.

## Parameters

`usePaymentMethods()` accepts a single optional object with the following properties:

## Returns

`usePaymentMethods()` returns an object with the following properties:

## Examples

### Basic usage

The following example demonstrates how to fetch and display a user's payment methods.


  ```tsx
// Filename: app/billing/payment-methods/page.tsx

  'use client'

  import { usePaymentMethods } from '@clerk/nextjs/experimental'

  export default function PaymentMethodsList() {
    const { data, isLoading } = usePaymentMethods({
      for: 'user',
      pageSize: 10,
    })

    if (isLoading) {
      return <div>Loading payment methods...</div>
    }

    if (!data || data.length === 0) {
      // Code for how to add a new payment method: https://clerk.com/docs/guides/development/custom-flows/billing/add-new-payment-method
      return <div>No payment methods found. Please add a payment method to your account.</div>
    }

    return (
      <ul>
        {data?.map((method) => (
          <li key={method.id}>
            {method.cardType} **** {method.last4}
            {method.isDefault ? ' (Default)' : null}
          </li>
        ))}
      </ul>
    )
  }
  ```


  ```tsx
// Filename: src/pages/billing/PaymentMethodsList.tsx

  import { usePaymentMethods } from '@clerk/react/experimental'

  export default function PaymentMethodsList() {
    const { data, isLoading } = usePaymentMethods({
      for: 'user',
      pageSize: 10,
    })

    if (isLoading) {
      return <div>Loading payment methods...</div>
    }

    if (!data || data.length === 0) {
      // Code for how to add a new payment method: https://clerk.com/docs/guides/development/custom-flows/billing/add-new-payment-method
      return <div>No payment methods found. Please add a payment method to your account.</div>
    }

    return (
      <ul>
        {data?.map((method) => (
          <li key={method.id}>
            {method.cardType} **** {method.last4}
            {method.isDefault ? ' (Default)' : null}
          </li>
        ))}
      </ul>
    )
  }
  ```


### Infinite pagination

The following example demonstrates how to implement infinite scrolling with payment methods.


  ```tsx
// Filename: app/billing/payment-methods/page.tsx

  'use client'

  import { usePaymentMethods } from '@clerk/nextjs/experimental'

  export default function InfinitePaymentMethods() {
    const { data, isLoading, hasNextPage, fetchNext } = usePaymentMethods({
      for: 'user',
      infinite: true,
      pageSize: 20,
    })

    if (isLoading) {
      return <div>Loading...</div>
    }

    if (!data || data.length === 0) {
      // Code for how to add a new payment method: https://clerk.com/docs/guides/development/custom-flows/billing/add-new-payment-method
      return <div>No payment methods found. Please add a payment method to your account.</div>
    }

    return (
      <div>
        <ul>
          {data?.map((method) => (
            <li key={method.id}>
              {method.cardType} ending in {method.last4}
              {method.status === 'expired' ? ' (Expired)' : null}
              {method.status === 'disconnected' ? ' (Disconnected)' : null}
            </li>
          ))}
        </ul>

        {hasNextPage && <button onClick={() => fetchNext()}>Load more payment methods</button>}
      </div>
    )
  }
  ```


  ```tsx
// Filename: src/pages/billing/PaymentMethodsList.tsx

  import { usePaymentMethods } from '@clerk/react/experimental'

  export default function InfinitePaymentMethods() {
    const { data, isLoading, hasNextPage, fetchNext } = usePaymentMethods({
      for: 'user',
      infinite: true,
      pageSize: 20,
    })

    if (isLoading) {
      return <div>Loading...</div>
    }

    if (!data || data.length === 0) {
      // Code for how to add a new payment method: https://clerk.com/docs/guides/development/custom-flows/billing/add-new-payment-method
      return <div>No payment methods found. Please add a payment method to your account.</div>
    }

    return (
      <div>
        <ul>
          {data?.map((method) => (
            <li key={method.id}>
              {method.cardType} ending in {method.last4}
              {method.status === 'expired' ? ' (Expired)' : null}
              {method.status === 'disconnected' ? ' (Disconnected)' : null}
            </li>
          ))}
        </ul>

        {hasNextPage && <button onClick={() => fetchNext()}>Load more payment methods</button>}
      </div>
    )
  }
  ```


### With checkout flow

The following example demonstrates how to use `usePaymentMethods()` in a checkout flow to select an existing payment method. For more information on how to build a checkout flow with an existing payment method, see [Build a custom checkout flow](/guides/development/custom-flows/billing/checkout-existing-payment-method).


  ```tsx
// Filename: app/billing/checkout/page.tsx

  'use client'

  import { usePaymentMethods, useCheckout } from '@clerk/nextjs/experimental'
  import { useRouter } from 'next/navigation'

  export default function CheckoutPaymentSelection() {
    const { data, isLoading } = usePaymentMethods({ for: 'user' })
    const { checkout } = useCheckout()
    const router = useRouter()

    const handlePaymentSubmit = async (paymentMethodId: string) => {
      try {
        // Confirm checkout with selected payment method
        const { error } = await checkout.confirm({ paymentMethodId })
        if (error) {
          console.error(JSON.stringify(error, null, 2))
          return
        }
        // Complete checkout and redirect
        await checkout.finalize({
          navigate: ({ decorateUrl }) => {
            const url = decorateUrl('/')
            if (url.startsWith('http')) {
              window.location.href = url
            } else {
              router.push(url)
            }
          },
        })
      } catch (error) {
        console.error('Payment failed:', error)
      }
    }

    if (isLoading) {
      return <div>Loading payment methods...</div>
    }

    if (!data || data.length === 0) {
      // Code for how to add a new payment method: https://clerk.com/docs/guides/development/custom-flows/billing/checkout-new-payment-method
      return <div>No payment methods found. Please add a payment method to your account.</div>
    }

    return (
      <div>
        <h3>Select a payment method</h3>
        {data?.map((method) => (
          <button key={method.id} onClick={() => handlePaymentSubmit(method.id)}>
            Pay with {method.cardType} ending in {method.last4}
          </button>
        ))}
      </div>
    )
  }
  ```


  ```tsx
// Filename: src/pages/billing/CheckoutPaymentSelection.tsx

  import { usePaymentMethods, useCheckout } from '@clerk/react/experimental'
  import { useNavigate } from 'react-router-dom'

  export default function CheckoutPaymentSelection() {
    const { data, isLoading } = usePaymentMethods({ for: 'user' })
    const { checkout } = useCheckout()
    const navigate = useNavigate()

    const handlePaymentSubmit = async (paymentMethodId: string) => {
      try {
        // Confirm checkout with selected payment method
        const { error } = await checkout.confirm({ paymentMethodId })
        if (error) {
          console.error(JSON.stringify(error, null, 2))
          return
        }
        // Complete checkout and redirect
        await checkout.finalize({
          navigate: ({ decorateUrl }) => {
            const url = decorateUrl('/')
            if (url.startsWith('http')) {
              window.location.href = url
            } else {
              navigate(url)
            }
          },
        })
      } catch (error) {
        console.error('Payment failed:', error)
      }
    }

    if (isLoading) {
      return <div>Loading payment methods...</div>
    }

    if (!data || data.length === 0) {
      // Code for how to add a new payment method: https://clerk.com/docs/guides/development/custom-flows/billing/checkout-new-payment-method
      return <div>No payment methods found. Please add a payment method to your account.</div>
    }

    return (
      <div>
        <h3>Select a payment method</h3>
        {data?.map((method) => (
          <button key={method.id} onClick={() => handlePaymentSubmit(method.id)}>
            Pay with {method.cardType} ending in {method.last4}
          </button>
        ))}
      </div>
    )
  }
  ```


## Next steps


  - [Checkout flow with a new payment method](/guides/development/custom-flows/billing/checkout-new-payment-method)
  - Build a custom checkout flow that allows users to add a new payment method during checkout.

  ---

  - [Add a new payment method outside of a checkout flow](/guides/development/custom-flows/billing/add-new-payment-method)
  - Build a custom user interface that allows users to add a new payment method to their account.
