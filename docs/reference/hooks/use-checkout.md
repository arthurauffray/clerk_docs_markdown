# useCheckout()


> Clerk's useCheckout() hook provides state and methods to manage a Subscription checkout flow.

> [!WARNING]
>
> Billing is currently in Beta and its APIs are experimental and may undergo breaking changes. To mitigate potential disruptions, we recommend [pinning](/pinning) your SDK and `clerk-js` package versions.


The `useCheckout()` hook is used to create, manage, and confirm a checkout session for a user or an Organization's Subscription Plan. It provides the state of the current checkout process, such as its status and any errors, along with methods to initiate and complete the checkout.

There are two ways to use `useCheckout()`:

1. In conjunction with [``](#checkout-provider) to create a shared checkout context. All child components inside the provider can then use `useCheckout()` to access or update the same checkout state.
1. On its own by passing configuration options directly to it. This is ideal for self-contained components that handle their own checkout flow without needing a shared context.

### `UseCheckoutOptions`

## Returns

`useCheckout()` returns an object with `checkout`, `errors`, and `fetchStatus`.

- `checkout` includes the checkout state and methods.
- `errors` contains any global or raw errors from the latest checkout request.
- `fetchStatus` indicates whether the checkout request is currently in progress.

Checkout data properties are `null` until the checkout process is started by calling the `start()` method.

## `CheckoutFlowResource`

## ``

The `` component is a wrapper that provides a checkout context to its children, allowing checkout state to be shared across multiple components. Child components can access the checkout context by calling `useCheckout()`.

### Properties

The `` component accepts the following props:

## Usage

For the best user experience and to prevent potential errors, always wrap components using `useCheckout()` with both `` and `` components. This ensures that the user is properly authenticated and Clerk is fully initialized before accessing checkout functionality.

```tsx
function CheckoutPage() {
  return (
    
      
        
  )
}
```

### Examples

The `useCheckout()` hook can be used with a context provider for managing state across multiple components or as a standalone hook for more isolated use cases.


#### With ", "Standalone Hook"]}>
  

#### Standalone Hook


The following example shows the basic structure for a checkout flow. A parent component, ``, sets up the `` and renders the checkout flow. A child component, ``, uses the `useCheckout()` hook to access the checkout state.


#### Tab 3

", ""]}>
      

#### Tab 4


        
          ```tsx
// Filename: src/components/SubscriptionPage.tsx

          import { CheckoutProvider } from '@clerk/nextjs/experimental'
          import { ClerkLoaded } from '@clerk/nextjs'
          import { CheckoutFlow } from './CheckoutFlow'

          export default function SubscriptionPage() {
            // `` sets the context for the checkout flow.
            // Any child component can now call `useCheckout()` to access this context.
            return (
              // Update with your Plan ID and Plan Period
              
                <div>
                  <h1>Upgrade Your Plan</h1>
                  <p>You are about to subscribe to our monthly plan</p>
                  
                    
                </div>
              
            )
          }
          ```
        

        
          ```tsx
// Filename: src/components/SubscriptionPage.tsx

          import { CheckoutProvider } from '@clerk/react/experimental'
          import { ClerkLoaded } from '@clerk/react'
          import { CheckoutFlow } from './CheckoutFlow'

          export default function SubscriptionPage() {
            // `` sets the context for the checkout flow.
            // Any child component can now call `useCheckout()` to access this context.
            return (
              // Update with your Plan ID and Plan Period
              
                <div>
                  <h1>Upgrade Your Plan</h1>
                  <p>You are about to subscribe to our monthly plan</p>
                  
                    
                </div>
              
            )
          }
          ```
        
      

#### Tab 5


        
          ```tsx
// Filename: src/components/CheckoutFlow.tsx

          'use client'

          import { useCheckout } from '@clerk/nextjs/experimental'
          import { useState } from 'react'
          import { useRouter } from 'next/navigation'

          export function CheckoutFlow() {
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

            return (
              <button onClick={() => checkout.start()} disabled={fetchStatus === 'fetching'}>
                {fetchStatus === 'fetching' ? 'Initializing...' : 'Start Checkout'}
              </button>
            )
          }

          function PaymentSection() {
            const { checkout, errors, fetchStatus } = useCheckout()

            const [paymentMethodId, setPaymentMethodId] = useState<string | null>(null)
            const router = useRouter()

            const submitSelectedMethod = async () => {
              if (fetchStatus === 'fetching' || !paymentMethodId) return

              try {
                // Confirm checkout with payment method
                const { error } = await checkout.confirm({
                  paymentMethodId,
                })
                if (error) {
                  console.error(JSON.stringify(error, null, 2))
                  return
                }
                // Calling `.finalize` enables you to sync the client-side state with the server-side state of your users.
                // It revalidates all authorization checks computed within server components.
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

            return (
              <>
                
                {errors.global && (
                  <ul>
                    {errors.global.map((error, index) => (
                      <li key={index}>{error.longMessage || error.message}</li>
                    ))}
                  </ul>
                )}

                <button type="button" disabled={fetchStatus === 'fetching'} onClick={submitSelectedMethod}>
                  {fetchStatus === 'fetching' ? 'Processing...' : 'Complete Purchase'}
                </button>
              </>
            )
          }

          function CheckoutSummary() {
            const { checkout } = useCheckout()

            return (
              <div>
                <h2>Order Summary</h2>
                <span>{checkout.plan?.name}</span>
                <span>
                  {checkout.totals?.totalDueNow.currencySymbol}
                  {checkout.totals?.totalDueNow.amountFormatted}
                </span>
              </div>
            )
          }
          ```
        

        
          ```tsx
// Filename: src/components/CheckoutFlow.tsx

          import { useCheckout } from '@clerk/react/experimental'
          import { useState } from 'react'
          import { useNavigate } from 'react-router-dom'

          export function CheckoutFlow() {
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

            return (
              <button onClick={() => checkout.start()} disabled={fetchStatus === 'fetching'}>
                {fetchStatus === 'fetching' ? 'Initializing...' : 'Start Checkout'}
              </button>
            )
          }

          function PaymentSection() {
            const { checkout, errors, fetchStatus } = useCheckout()

            const [paymentMethodId, setPaymentMethodId] = useState<string | null>(null)
            const navigate = useNavigate()

            const submitSelectedMethod = async () => {
              if (fetchStatus === 'fetching' || !paymentMethodId) return

              try {
                // Confirm checkout with payment method
                const { error } = await checkout.confirm({
                  paymentMethodId,
                })
                if (error) {
                  console.error(JSON.stringify(error, null, 2))
                  return
                }
                // Calling `.finalize` enables you to sync the client-side state with the server-side state of your users.
                // It revalidates all authorization checks computed within server components.
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

            return (
              <>
                
                {errors.global && (
                  <ul>
                    {errors.global.map((error, index) => (
                      <li key={index}>{error.longMessage || error.message}</li>
                    ))}
                  </ul>
                )}

                <button type="button" disabled={fetchStatus === 'fetching'} onClick={submitSelectedMethod}>
                  {fetchStatus === 'fetching' ? 'Processing...' : 'Complete Purchase'}
                </button>
              </>
            )
          }

          function CheckoutSummary() {
            const { checkout } = useCheckout()

            return (
              <div>
                <h2>Order Summary</h2>
                <span>{checkout.plan?.name}</span>
                <span>
                  {checkout.totals?.totalDueNow.currencySymbol}
                  {checkout.totals?.totalDueNow.amountFormatted}
                </span>
              </div>
            )
          }
          ```
        
      
  

  
    For simple, self-contained components, you can use `useCheckout()` by passing the configuration options directly to the hook. This avoids the need to wrap the component in a provider.

    The following example shows an `` component that manages its own checkout flow.

    
      ```tsx
// Filename: src/components/UpgradeButton.tsx

      'use client'

      import { useCheckout } from '@clerk/nextjs/experimental'

      export function UpgradeButton({
        planId,
        planPeriod,
      }: {
        planId: string
        planPeriod: 'month' | 'annual'
      }) {
        // Pass options directly to the hook when not using a provider.
        const { checkout, errors, fetchStatus } = useCheckout({
          planId,
          planPeriod,
          for: 'user',
        })

        const isStarting = fetchStatus === 'fetching'

        const handleStartCheckout = async () => {
          try {
            const { error } = await checkout.start()
            if (error) {
              console.error(JSON.stringify(error, null, 2))
              return
            }
            // In a real app, you would now use the `externalClientSecret`
            // from the checkout object to render a payment form.
            console.log('Checkout started! Status:', checkout.status)
          } catch (e) {
            console.error('Error starting checkout:', e)
          }
        }

        return (
          <div>
            <button onClick={handleStartCheckout} disabled={isStarting}>
              {isStarting ? 'Initializing...' : `Upgrade to ${planPeriod} plan`}
            </button>
            {errors.global && (
              <ul>
                {errors.global.map((error, index) => (
                  <li key={index}>{error.longMessage || error.message}</li>
                ))}
              </ul>
            )}
          </div>
        )
      }
      ```
    

    
      ```tsx
// Filename: src/components/UpgradeButton.tsx

      import { useCheckout } from '@clerk/react/experimental'

      export function UpgradeButton({
        planId,
        planPeriod,
      }: {
        planId: string
        planPeriod: 'month' | 'annual'
      }) {
        // Pass options directly to the hook when not using a provider.
        const { checkout, errors, fetchStatus } = useCheckout({
          planId,
          planPeriod,
          for: 'user',
        })

        const isStarting = fetchStatus === 'fetching'

        const handleStartCheckout = async () => {
          try {
            const { error } = await checkout.start()
            if (error) {
              console.error(JSON.stringify(error, null, 2))
              return
            }
            // In a real app, you would now use the `externalClientSecret`
            // from the checkout object to render a payment form.
            console.log('Checkout started! Status:', checkout.status)
          } catch (e) {
            console.error('Error starting checkout:', e)
          }
        }

        return (
          <div>
            <button onClick={handleStartCheckout} disabled={isStarting}>
              {isStarting ? 'Initializing...' : `Upgrade to ${planPeriod} plan`}
            </button>
            {errors.global && (
              <ul>
                {errors.global.map((error, index) => (
                  <li key={index}>{error.longMessage || error.message}</li>
                ))}
              </ul>
            )}
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
