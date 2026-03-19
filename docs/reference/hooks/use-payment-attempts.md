# usePaymentAttempts()


> Access and manage payment attempts in your React application with Clerk's usePaymentAttempts() hook.

> [!WARNING]
>
> Billing is currently in Beta and its APIs are experimental and may undergo breaking changes. To mitigate potential disruptions, we recommend [pinning](/pinning) your SDK and `clerk-js` package versions.


The `usePaymentAttempts()` hook provides access to the payment attempts associated with a user or Organization. It returns a paginated list of payment attempts and includes methods for managing them.

## Parameters

`usePaymentAttempts()` accepts a single optional object with the following properties:

## Returns

`usePaymentAttempts()` returns an object with the following properties:

## Examples

### Basic usage

The following example demonstrates how to fetch and display a user's payment attempts.


  ```tsx
// Filename: app/billing/payment-attempts/page.tsx

  'use client'

  import { usePaymentAttempts } from '@clerk/nextjs/experimental'

  export default function PaymentAttemptsList() {
    const { data, isLoading } = usePaymentAttempts({
      for: 'user',
      pageSize: 10,
    })

    if (isLoading) {
      return <div>Loading payment attempts...</div>
    }

    if (!data || data.length === 0) {
      return <div>No payment attempts found.</div>
    }

    return (
      <ul>
        {data?.map((attempt) => (
          <li key={attempt.id}>
            Payment #{attempt.id} - {attempt.status}
            <br />
            Amount: {attempt.amount.amountFormatted} on {new Date(attempt.updatedAt).toLocaleString()}
          </li>
        ))}
      </ul>
    )
  }
  ```


  ```tsx
// Filename: src/pages/billing/PaymentAttemptsList.tsx

  import { usePaymentAttempts } from '@clerk/react/experimental'

  export default function PaymentAttemptsList() {
    const { data, isLoading } = usePaymentAttempts({
      for: 'user',
      pageSize: 10,
    })

    if (isLoading) {
      return <div>Loading payment attempts...</div>
    }

    if (!data || data.length === 0) {
      return <div>No payment attempts found.</div>
    }

    return (
      <ul>
        {data?.map((attempt) => (
          <li key={attempt.id}>
            Payment #{attempt.id} - {attempt.status}
            <br />
            Amount: {attempt.amount.amountFormatted} on {new Date(attempt.updatedAt).toLocaleString()}
          </li>
        ))}
      </ul>
    )
  }
  ```


### Infinite pagination

The following example demonstrates how to implement infinite scrolling with payment attempts.


  ```tsx
// Filename: app/billing/payment-attempts/page.tsx

  'use client'

  import { usePaymentAttempts } from '@clerk/nextjs/experimental'

  export default function InfinitePaymentAttempts() {
    const { data, isLoading, hasNextPage, fetchNext } = usePaymentAttempts({
      for: 'user',
      infinite: true,
      pageSize: 20,
    })

    if (isLoading) {
      return <div>Loading...</div>
    }

    if (!data || data.length === 0) {
      return <div>No payment attempts found.</div>
    }

    return (
      <div>
        <ul>
          {data?.map((attempt) => (
            <li key={attempt.id}>
              Payment attempt for {attempt.amount.amountFormatted}
              <br />
              Status: {attempt.status}
              <br />
              {attempt.status === 'failed' && attempt.failedAt && (
                <span>Failed At: {new Date(attempt.failedAt).toLocaleString()}</span>
              )}
            </li>
          ))}
        </ul>

        {hasNextPage && <button onClick={() => fetchNext()}>Load more payment attempts</button>}
      </div>
    )
  }
  ```


  ```tsx
// Filename: src/pages/billing/PaymentAttemptsList.tsx

  import { usePaymentAttempts } from '@clerk/react/experimental'

  export default function InfinitePaymentAttempts() {
    const { data, isLoading, hasNextPage, fetchNext } = usePaymentAttempts({
      for: 'user',
      infinite: true,
      pageSize: 20,
    })

    if (isLoading) {
      return <div>Loading...</div>
    }

    if (!data || data.length === 0) {
      return <div>No payment attempts found.</div>
    }

    return (
      <div>
        <ul>
          {data?.map((attempt) => (
            <li key={attempt.id}>
              Payment attempt for {attempt.amount.amountFormatted}
              <br />
              Status: {attempt.status}
              <br />
              {attempt.status === 'failed' && attempt.failedAt && (
                <span>Failed At: {new Date(attempt.failedAt).toLocaleString()}</span>
              )}
            </li>
          ))}
        </ul>

        {hasNextPage && <button onClick={() => fetchNext()}>Load more payment attempts</button>}
      </div>
    )
  }
  ```


### Payment attempts history table

The following example demonstrates how to use `usePaymentAttempts()` to display a detailed payment history table.


  ```tsx
// Filename: app/billing/payment-attempts-history/page.tsx

  'use client'

  import { usePaymentAttempts } from '@clerk/nextjs/experimental'

  export default function PaymentAttemptsHistory() {
    const { data, isLoading } = usePaymentAttempts({ for: 'user' })

    if (isLoading) {
      return <div>Loading payment attempts...</div>
    }

    if (!data || data.length === 0) {
      return <div>No payment attempts found.</div>
    }

    const getStatusColor = (status: string) => {
      switch (status) {
        case 'paid':
          return 'green'
        case 'failed':
          return 'red'
        case 'pending':
          return 'orange'
        default:
          return 'gray'
      }
    }

    return (
      <table>
        <thead>
          <tr>
            <th>Payment ID</th>
            <th>Amount</th>
            <th>Status</th>
            <th>Date</th>
            <th>Payment Method</th>
          </tr>
        </thead>
        <tbody>
          {data?.map((attempt) => (
            <tr key={attempt.id}>
              <td>{attempt.id}</td>
              <td>{attempt.amount.amountFormatted}</td>
              <td style={{ color: getStatusColor(attempt.status) }}>{attempt.status}</td>
              <td>{attempt.paidAt ? new Date(attempt.paidAt).toLocaleDateString() : '-'}</td>
              <td>
                {attempt.paymentSource.cardType} ****{attempt.paymentSource.last4}
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    )
  }
  ```


  ```tsx
// Filename: src/pages/billing/PaymentAttemptsHistory.tsx

  import { usePaymentAttempts } from '@clerk/react/experimental'

  export default function PaymentAttemptsHistory() {
    const { data, isLoading } = usePaymentAttempts({ for: 'user' })

    if (isLoading) {
      return <div>Loading payment attempts...</div>
    }

    if (!data || data.length === 0) {
      return <div>No payment attempts found.</div>
    }

    const getStatusColor = (status: string) => {
      switch (status) {
        case 'paid':
          return 'green'
        case 'failed':
          return 'red'
        case 'pending':
          return 'orange'
        default:
          return 'gray'
      }
    }

    return (
      <table>
        <thead>
          <tr>
            <th>Payment ID</th>
            <th>Amount</th>
            <th>Status</th>
            <th>Date</th>
            <th>Payment Method</th>
          </tr>
        </thead>
        <tbody>
          {data?.map((attempt) => (
            <tr key={attempt.id}>
              <td>{attempt.id}</td>
              <td>{attempt.amount.amountFormatted}</td>
              <td style={{ color: getStatusColor(attempt.status) }}>{attempt.status}</td>
              <td>{attempt.paidAt ? new Date(attempt.paidAt).toLocaleDateString() : '-'}</td>
              <td>
                {attempt.paymentSource.cardType} ****{attempt.paymentSource.last4}
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    )
  }
  ```
