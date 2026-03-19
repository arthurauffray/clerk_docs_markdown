# Build a custom checkout flow with a new payment method


> Learn how to use the Clerk API to build a custom checkout flow that allows users to add a new payment method during checkout.

> [!WARNING]
> This guide is for users who want to build a custom flow. To use a _prebuilt_ UI, use the [Account Portal pages](/guides/account-portal/overview) or [prebuilt components](/reference/components/overview).


> [!WARNING]
>
> Billing is currently in Beta and its APIs are experimental and may undergo breaking changes. To mitigate potential disruptions, we recommend [pinning](/pinning) your SDK and `clerk-js` package versions.


This guide will walk you through how to build a custom user interface for a checkout flow that allows users to **add a new payment method during checkout**.

For the custom flow that allows users to checkout **with an existing payment** method, see the [dedicated guide](/guides/development/custom-flows/billing/checkout-existing-payment-method).

For the custom flow that allows users to add a new payment method to their account, **outside of a checkout flow**, see the [dedicated guide](/guides/development/custom-flows/billing/add-new-payment-method).


  ## Enable Billing Features

  To use Billing Features, you first need to ensure they are enabled for your application. Follow the [Billing documentation](/guides/billing/overview) to enable them and setup your Plans.

  ## Build the custom flow

  To create a checkout session with a new payment card, you must:

  1. Set up the checkout provider with Plan details.
  1. Initialize the checkout session when the user is ready.
  1. Render the payment form for card collection.
  1. Confirm the payment with the collected payment method.
  1. Complete the checkout process and redirect the user.

  The following example:

  1. Uses the [`useCheckout()`](/reference/hooks/use-checkout) hook to initiate and manage the checkout session.
  1. Uses the [`usePaymentElement()`](/reference/hooks/use-payment-element) hook to control the payment element, which is rendered by ``.
  1. Assumes that you have already have a valid `planId`, which you can acquire in many ways.

  - [Copy from the Clerk Dashboard](https://dashboard.clerk.com/~/billing/plans).
  - Use the [Clerk Backend API](/reference/backend-api/tag/commerce/get/commerce/plans#tag/commerce/get/commerce/plans).
  - Use the new [`usePlans()`](/reference/hooks/use-plans) hook to get the Plan details.

  
    > [!TIP]
> Examples for this SDK aren't available yet. For now, try adapting the  available example to fit your SDK.

  

  ```tsx
// Filename: app/checkout/page.tsx

  'use client'
  import * as React from 'react'
  import { Show, ClerkLoaded } from '@clerk/nextjs'
  import {
    CheckoutProvider,
    useCheckout,
    PaymentElementProvider,
    PaymentElement,
    usePaymentElement,
  } from '@clerk/nextjs/experimental'
  import { useRouter } from 'next/navigation'

  export default function CheckoutPage() {
    return (
      // Update with your Plan ID and Plan Period
      
        
          
            
      
    )
  }

  function CustomCheckout() {
    const { checkout } = useCheckout()

    if (checkout.status === 'needs_initialization') {
      return }

    return (
      <div className="checkout-container">
        
          
      </div>
    )
  }

  function CheckoutInitialization() {
    const { checkout, fetchStatus } = useCheckout()

    if (checkout.status !== 'needs_initialization') {
      return null
    }

    return (
      <button onClick={() => checkout.start()} disabled={fetchStatus === 'fetching'}>
        {fetchStatus === 'fetching' ? 'Initializing...' : 'Start Checkout'}
      </button>
    )
  }

  function PaymentSection() {
    const { checkout, errors, fetchStatus } = useCheckout()

    const { isFormReady, submit } = usePaymentElement()
    const [isProcessing, setIsProcessing] = React.useState(false)

    const router = useRouter()

    const handleSubmit = async (e: React.FormEvent) => {
      e.preventDefault()
      if (!isFormReady || isProcessing || fetchStatus === 'fetching') return
      setIsProcessing(true)

      try {
        // Submit payment form to get payment method
        const { data, error } = await submit()
        // Usually a validation error from stripe that you can ignore
        if (error) {
          console.error(JSON.stringify(error, null, 2))
          return
        }
        // Confirm checkout with payment method
        const { error: confirmError } = await checkout.confirm(data)
        if (confirmError) {
          console.error(JSON.stringify(confirmError, null, 2))
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
      } finally {
        setIsProcessing(false)
      }
    }

    const isSubmitting = isProcessing || fetchStatus === 'fetching'

    return (
      <form onSubmit={handleSubmit}>
        Loading payment element...</div>} />

        {errors.global && (
          <ul>
            {errors.global.map((error, index) => (
              <li key={index}>{error.longMessage || error.message}</li>
            ))}
          </ul>
        )}

        <button type="submit" disabled={!isFormReady || isSubmitting}>
          {isSubmitting ? 'Processing...' : 'Complete Purchase'}
        </button>
      </form>
    )
  }

  function CheckoutSummary() {
    const { checkout } = useCheckout()

    if (!checkout.plan) {
      return null
    }

    return (
      <div>
        <h2>Order Summary</h2>
        <span>{checkout.plan.name}</span>
        <span>
          {checkout.totals.totalDueNow.currencySymbol} {checkout.totals.totalDueNow.amountFormatted}
        </span>
      </div>
    )
  }
  ```
