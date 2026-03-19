# Build a custom flow for adding a new payment method


> Learn how to use the Clerk API to build a custom flow for adding a new payment method to a user's account.

> [!WARNING]
> This guide is for users who want to build a custom flow. To use a _prebuilt_ UI, use the [Account Portal pages](/guides/account-portal/overview) or [prebuilt components](/reference/components/overview).


> [!WARNING]
>
> Billing is currently in Beta and its APIs are experimental and may undergo breaking changes. To mitigate potential disruptions, we recommend [pinning](/pinning) your SDK and `clerk-js` package versions.


This guide will walk you through how to build a custom user interface that allows users to **add a new payment method to their account**. This is a common feature in a user's billing or account settings page, allowing them to pre-emptively add a payment method for future use.

For the custom flow that allows users to add a new payment method **during checkout**, see the [dedicated guide](/guides/development/custom-flows/billing/checkout-new-payment-method).


  ## Enable Billing Features

  To use Billing Features, you first need to ensure they are enabled for your application. Follow the [Billing documentation](/guides/billing/overview) to enable them and set up your Plans.

  ## Build the custom flow

  To add a new payment method for a user, you must:

  1. Set up the [``](/reference/hooks/use-payment-element) to create a context for the user's payment actions.
  1. Render the [``](/reference/hooks/use-payment-element) to display the secure payment fields from your provider.
  1. Use the [`usePaymentElement()`](/reference/hooks/use-payment-element) hook to submit the form and create a payment token.
  1. Use the [`useUser()`](/reference/hooks/use-user) hook to attach the newly created payment method to the user.

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
