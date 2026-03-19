# usePaymentElement()


> Clerk's usePaymentElement() hook provides methods and state for interacting with a payment form.

> [!WARNING]
>
> Billing is currently in Beta and its APIs are experimental and may undergo breaking changes. To mitigate potential disruptions, we recommend [pinning](/pinning) your SDK and `clerk-js` package versions.


The `usePaymentElement()` hook is used to control the payment form rendered by the [``](#payment-element) component. It provides the necessary state and methods to submit payment details to a payment provider like Stripe.

This hook must be used within a component that is a descendant of the `` component. It is typically used in a checkout flow that prompts a user to add a new payment method, or for adding a new payment method outside of a checkout.

## Parameters

`usePaymentElement()` doesn't accept any parameters. It derives its state and configuration from the nearest [``](#payment-element-provider).

## Returns

`usePaymentElement()` returns an object with the following properties:

## Payment element components

The `usePaymentElement()` hook works in conjunction with the `` and `` components.

### ``

The `` component sets up the context for the payment element. It fetches all the necessary data from the payment provider (e.g., Stripe) and makes it available to its children.

#### Properties

### ``

This component renders the actual payment form from the provider (e.g., the Stripe Payment Element). It should be rendered as a child of ``.

#### Properties

## Example

The following example demonstrates how to create a billing page where a user can add a new payment method. It is split into two components:

- **``**: Sets up the ``, which specifies that the payment actions within its children are `for` the `user`.
- **``**: Renders the payment form and handles the submission logic. It uses `usePaymentElement()` to get the `submit` function and `useUser()` to get the `user` object. When the form is submitted, it first creates a payment token and then attaches it to the user.


  
**:**

```tsx
// Filename: app/user/billing/page.tsx

    import { ClerkLoaded } from '@clerk/nextjs'
    import { PaymentElementProvider } from '@clerk/nextjs/experimental'
    import { AddPaymentMethodForm } from './AddPaymentMethodForm'

    export default function Page() {
      return (
        <div>
          <h1>Billing Settings</h1>

          
            
              
          
        </div>
      )
    }
    ```


**:**

```tsx
// Filename: app/user/billing/AddPaymentMethodForm.tsx

    'use client'

    import { useUser } from '@clerk/nextjs'
    import { usePaymentElement, PaymentElement } from '@clerk/nextjs/experimental'
    import { useState } from 'react'

    export function AddPaymentMethodForm() {
      const { user } = useUser()
      const { submit, isFormReady } = usePaymentElement()
      const [isSubmitting, setIsSubmitting] = useState(false)
      const [error, setError] = useState<string | null>(null)

      const handleAddPaymentMethod = async (e: React.FormEvent) => {
        e.preventDefault()
        if (!isFormReady || !user) {
          return
        }

        setError(null)
        setIsSubmitting(true)

        try {
          // 1. Submit the form to the payment provider to get a payment token
          const { data, error } = await submit()

          // Usually a validation error from stripe that you can ignore.
          if (error) {
            setIsSubmitting(false)
            return
          }

          // 2. Use the token to add the payment source to the user
          await user.addPaymentSource(data)

          // 3. Handle success (e.g., show a confirmation, clear the form)
          alert('Payment method added successfully!')
        } catch (err: any) {
          setError(err.message || 'An unexpected error occurred.')
        } finally {
          setIsSubmitting(false)
        }
      }

      return (
        <form onSubmit={handleAddPaymentMethod}>
          <h3>Add a new payment method</h3>
          <button type="submit" disabled={!isFormReady || isSubmitting}>
            {isSubmitting ? 'Saving...' : 'Save Card'}
          </button>
          {error && <p style={{ color: 'red' }}>{error}</p>}
        </form>
      )
    }
    ```


  
**:**

```tsx
// Filename: src/pages/user/billing/page.tsx

    import { ClerkLoaded } from '@clerk/react'
    import { PaymentElementProvider } from '@clerk/react/experimental'
    import { AddPaymentMethodForm } from './AddPaymentMethodForm'

    export default function Page() {
      return (
        <div>
          <h1>Billing Settings</h1>

          
            
              
          
        </div>
      )
    }
    ```


**:**

```tsx
// Filename: src/pages/user/billing/AddPaymentMethodForm.tsx

    import { useUser } from '@clerk/react'
    import { usePaymentElement, PaymentElement } from '@clerk/react/experimental'
    import { useState } from 'react'

    export function AddPaymentMethodForm() {
      const { user } = useUser()
      const { submit, isFormReady } = usePaymentElement()
      const [isSubmitting, setIsSubmitting] = useState(false)
      const [error, setError] = useState<string | null>(null)

      const handleAddPaymentMethod = async (e: React.FormEvent) => {
        e.preventDefault()
        if (!isFormReady || !user) {
          return
        }

        setError(null)
        setIsSubmitting(true)

        try {
          // 1. Submit the form to the payment provider to get a payment token
          const { data, error } = await submit()

          // Usually a validation error from stripe that you can ignore.
          if (error) {
            setIsSubmitting(false)
            return
          }

          // 2. Use the token to add the payment source to the user
          await user.addPaymentSource(data)

          // 3. Handle success (e.g., show a confirmation, clear the form)
          alert('Payment method added successfully!')
        } catch (err: any) {
          setError(err.message || 'An unexpected error occurred.')
        } finally {
          setIsSubmitting(false)
        }
      }

      return (
        <form onSubmit={handleAddPaymentMethod}>
          <h3>Add a new payment method</h3>
          <button type="submit" disabled={!isFormReady || isSubmitting}>
            {isSubmitting ? 'Saving...' : 'Save Card'}
          </button>
          {error && <p style={{ color: 'red' }}>{error}</p>}
        </form>
      )
    }
    ```


## Next steps


  - [Checkout flow with a new payment method](/guides/development/custom-flows/billing/checkout-new-payment-method)
  - Build a custom checkout flow that allows users to add a new payment method during checkout.

  ---

  - [Add a new payment method outside of a checkout flow](/guides/development/custom-flows/billing/add-new-payment-method)
  - Build a custom user interface that allows users to add a new payment method to their account.
