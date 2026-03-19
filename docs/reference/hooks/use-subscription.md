# useSubscription()


> Access Subscription information in your React application with Clerk's useSubscription() hook.

> [!WARNING]
>
> Billing is currently in Beta and its APIs are experimental and may undergo breaking changes. To mitigate potential disruptions, we recommend [pinning](/pinning) your SDK and `clerk-js` package versions.


The `useSubscription()` hook provides access to Subscription information for users or Organizations in your application. It returns the current Subscription data and includes methods for managing it.

> [!WARNING]
> The `useSubscription()` hook should only be used for accessing and displaying Subscription information. For authorization purposes (i.e., controlling access to Features or content), use the [`has()`](/guides/secure/authorization-checks#use-has-for-authorization-checks) helper or the [``](/reference/components/control/show) component instead.

## Parameters

`useSubscription()` accepts a single optional object with the following properties:

## Returns

`useSubscription()` returns an object with the following properties:

## Examples

### Basic usage

The following example shows how to fetch and display Subscription information.


  ```tsx
// Filename: app/pricing/subscription-details/page.tsx

  'use client'

  import { useSubscription } from '@clerk/nextjs/experimental'

  export default function SubscriptionInfo() {
    const { data, isLoading, error } = useSubscription()

    if (isLoading) {
      return <div>Loading Subscription...</div>
    }

    if (error) {
      return <div>Error loading Subscription: {error.message}</div>
    }

    if (!data) {
      return <div>No Subscription found</div>
    }

    return (
      <div>
        <h2>Your Subscription</h2>
        
      </div>
    )
  }
  ```


  ```tsx
// Filename: src/pages/pricing/SubscriptionDetails.tsx

  import { useSubscription } from '@clerk/react/experimental'

  export default function SubscriptionInfo() {
    const { data, isLoading, error } = useSubscription()

    if (isLoading) {
      return <div>Loading Subscription...</div>
    }

    if (error) {
      return <div>Error loading Subscription: {error.message}</div>
    }

    if (!data) {
      return <div>No Subscription found</div>
    }

    return (
      <div>
        <h2>Your Subscription</h2>
        
      </div>
    )
  }
  ```


### Organization subscription

The following example shows how to fetch an Organization's subscription.


  ```tsx
// Filename: app/pricing/organization-subscription-details/page.tsx

  'use client'

  import { useSubscription } from '@clerk/nextjs/experimental'

  export default function OrganizationSubscription() {
    const { data, isLoading, revalidate } = useSubscription({
      for: 'organization',
      keepPreviousData: true,
    })

    const handleSubscriptionUpdate = async () => {
      // After making changes to the Subscription
      await revalidate()
    }

    if (isLoading) {
      return <div>Loading Organization Subscription...</div>
    }

    return (
      <div>
        <h2>Organization Subscription</h2>
        
        <button onClick={handleSubscriptionUpdate}>Refresh Subscription</button>
      </div>
    )
  }
  ```


  ```tsx
// Filename: src/pages/pricing/OrganizationSubscription.tsx

  import { useSubscription } from '@clerk/react/experimental'

  export default function OrganizationSubscription() {
    const { data, isLoading, revalidate } = useSubscription({
      for: 'organization',
      keepPreviousData: true,
    })

    const handleSubscriptionUpdate = async () => {
      // After making changes to the Subscription
      await revalidate()
    }

    if (isLoading) {
      return <div>Loading Organization Subscription...</div>
    }

    return (
      <div>
        <h2>Organization Subscription</h2>
        
        <button onClick={handleSubscriptionUpdate}>Refresh Subscription</button>
      </div>
    )
  }
  ```


### With error handling

The following example shows how to handle Subscription data with proper error states.


  ```tsx
// Filename: app/pricing/subscription-details/page.tsx

  'use client'

  import { useSubscription } from '@clerk/nextjs/experimental'

  export function SubscriptionDetails() {
    const { data: subscription, isLoading } = useSubscription()

    if (isLoading) {
      return <div>Loading Subscription...</div>
    }

    if (!subscription) {
      return <div>No Subscription</div>
    }

    return (
      <div className="subscription-details">
        <h2>Subscription Details</h2>
        <div className="status">
          Status: <span className={`status-${subscription.status}`}>{subscription.status}</span>
        </div>

        <div className="dates">
          <p>Active since: {subscription.activeAt.toLocaleDateString()}</p>
          {subscription.pastDueAt && (
            <p className="warning">Past due since: {subscription.pastDueAt.toLocaleDateString()}</p>
          )}
        </div>

        {subscription.nextPayment && (
          <div className="next-payment">
            <h3>Next Payment</h3>
            <p>Amount: {subscription.nextPayment.amount.amountFormatted}</p>
            <p>Due: {subscription.nextPayment.date.toLocaleDateString()}</p>
          </div>
        )}

        <div className="subscription-items">
          <h3>Subscription Items</h3>
          <ul>
            {subscription.subscriptionItems.map((item) => (
              <li key={item.id}></li>
            ))}
          </ul>
        </div>
      </div>
    )
  }

  export default function Page() {
    const { data, isLoading, error, isFetching, revalidate } = useSubscription()

    if (error) {
      return (
        <div className="error-state">
          <h3>Failed to load Subscription</h3>
          <p>{error.message}</p>
          <button onClick={revalidate}>Try Again</button>
        </div>
      )
    }

    return (
      <div className="subscription-status">
        {isLoading ? (
          <div>Loading...</div>
        ) : (
          <>
            <div className="status-indicator">{isFetching && <span>Refreshing...</span>}</div>
            {data ? : <div>No active Subscription</div>}
          </>
        )}
      </div>
    )
  }
  ```


  ```tsx
// Filename: src/pages/pricing/SubscriptionDetails.tsx

  import { useSubscription } from '@clerk/react/experimental'

  export function SubscriptionDetails() {
    const { data: subscription, isLoading } = useSubscription()

    if (isLoading) {
      return <div>Loading Subscription...</div>
    }

    if (!subscription) {
      return <div>No Subscription</div>
    }

    return (
      <div className="subscription-details">
        <h2>Subscription Details</h2>
        <div className="status">
          Status: <span className={`status-${subscription.status}`}>{subscription.status}</span>
        </div>

        <div className="dates">
          <p>Active since: {subscription.activeAt.toLocaleDateString()}</p>
          {subscription.pastDueAt && (
            <p className="warning">Past due since: {subscription.pastDueAt.toLocaleDateString()}</p>
          )}
        </div>

        {subscription.nextPayment && (
          <div className="next-payment">
            <h3>Next Payment</h3>
            <p>Amount: {subscription.nextPayment.amount.amountFormatted}</p>
            <p>Due: {subscription.nextPayment.date.toLocaleDateString()}</p>
          </div>
        )}

        <div className="subscription-items">
          <h3>Subscription Items</h3>
          <ul>
            {subscription.subscriptionItems.map((item) => (
              <li key={item.id}></li>
            ))}
          </ul>
        </div>
      </div>
    )
  }

  export default function Page() {
    const { data, isLoading, error, isFetching, revalidate } = useSubscription()

    if (error) {
      return (
        <div className="error-state">
          <h3>Failed to load Subscription</h3>
          <p>{error.message}</p>
          <button onClick={revalidate}>Try Again</button>
        </div>
      )
    }

    return (
      <div className="subscription-status">
        {isLoading ? (
          <div>Loading...</div>
        ) : (
          <>
            <div className="status-indicator">{isFetching && <span>Refreshing...</span>}</div>
            {data ? : <div>No active Subscription</div>}
          </>
        )}
      </div>
    )
  }
  ```
