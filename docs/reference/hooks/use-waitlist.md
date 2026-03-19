# useWaitlist()


> Access and manage the waitlist state in your React application with Clerk's useWaitlist() hook.

The `useWaitlist()` hook provides access to the [`Waitlist`](/reference/javascript/waitlist) object, which provides methods and properties to manage waitlist entries in your application. This hook is useful for building a custom flow instead of using the prebuilt [``](/reference/components/authentication/waitlist) component.

## Returns

- **`waitlist`** [`Waitlist`](/reference/javascript/waitlist)

  The current active `Waitlist` instance, for use in custom flows.

    ---

- **`errors`** `Errors`

  The errors that occurred during the last API request.

    ---

- **`fetchStatus`** `'idle' | 'fetching'`

  The fetch status of the underlying `Waitlist` resource.


## Example

The following example demonstrates how to use the `useWaitlist()` hook to create a custom waitlist form. Users can submit their email address to join the waitlist, and the component displays appropriate feedback based on the submission state.


  ```tsx
// Filename: app/waitlist/page.tsx

  'use client'

  import { useWaitlist } from '@clerk/nextjs'

  export default function Page() {
    const { waitlist, errors, fetchStatus } = useWaitlist()

    const handleSubmit = async (e: React.FormEvent) => {
      e.preventDefault()
      const formData = new FormData(e.currentTarget)
      const emailAddress = formData.get('emailAddress') as string

      const { error } = await waitlist.join({ emailAddress })
      if (error) {
        console.error('Failed to join waitlist:', error)
      }
    }

    if (waitlist.id) {
      return (
        <div>
          <h1>Successfully joined the waitlist!</h1>
          <p>We'll notify you when you're approved.</p>
        </div>
      )
    }

    return (
      <div>
        <h1>Join the Waitlist</h1>
        <form onSubmit={handleSubmit}>
          <label htmlFor="email">Email address</label>
          <input id="email" name="emailAddress" type="email" required />
          {errors.fields.emailAddress && <p>{errors.fields.emailAddress.longMessage}</p>}
          <button type="submit" disabled={fetchStatus === 'fetching'}>
            {fetchStatus === 'fetching' ? 'Submitting...' : 'Join Waitlist'}
          </button>
        </form>
      </div>
    )
  }
  ```


  ```tsx
// Filename: src/waitlist.tsx

  import { useWaitlist } from '@clerk/react'

  export default function WaitlistPage() {
    const { waitlist, errors, fetchStatus } = useWaitlist()

    const handleSubmit = async (e: React.FormEvent) => {
      e.preventDefault()
      const formData = new FormData(e.currentTarget)
      const emailAddress = formData.get('emailAddress') as string

      const { error } = await waitlist.join({ emailAddress })
      if (error) {
        console.error('Failed to join waitlist:', error)
      }
    }

    if (waitlist.id) {
      return (
        <div>
          <h1>Successfully joined the waitlist!</h1>
          <p>We'll notify you when you're approved.</p>
        </div>
      )
    }

    return (
      <div>
        <h1>Join the Waitlist</h1>
        <form onSubmit={handleSubmit}>
          <label htmlFor="email">Email address</label>
          <input id="email" name="emailAddress" type="email" required />
          {errors.fields.emailAddress && <p>{errors.fields.emailAddress.longMessage}</p>}
          <button type="submit" disabled={fetchStatus === 'fetching'}>
            {fetchStatus === 'fetching' ? 'Submitting...' : 'Join Waitlist'}
          </button>
        </form>
      </div>
    )
  }
  ```


  ```tsx
// Filename: routes/waitlist.tsx

  import { useWaitlist } from '@clerk/react-router'

  export default function WaitlistPage() {
    const { waitlist, errors, fetchStatus } = useWaitlist()

    const handleSubmit = async (e: React.FormEvent) => {
      e.preventDefault()
      const formData = new FormData(e.currentTarget)
      const emailAddress = formData.get('emailAddress') as string

      const { error } = await waitlist.join({ emailAddress })
      if (error) {
        console.error('Failed to join waitlist:', error)
      }
    }

    if (waitlist.id) {
      return (
        <div>
          <h1>Successfully joined the waitlist!</h1>
          <p>We'll notify you when you're approved.</p>
        </div>
      )
    }

    return (
      <div>
        <h1>Join the Waitlist</h1>
        <form onSubmit={handleSubmit}>
          <label htmlFor="email">Email address</label>
          <input id="email" name="emailAddress" type="email" required />
          {errors.fields.emailAddress && <p>{errors.fields.emailAddress.longMessage}</p>}
          <button type="submit" disabled={fetchStatus === 'fetching'}>
            {fetchStatus === 'fetching' ? 'Submitting...' : 'Join Waitlist'}
          </button>
        </form>
      </div>
    )
  }
  ```


  ```tsx
// Filename: app/routes/waitlist.tsx

  import { useWaitlist } from '@clerk/tanstack-react-start'
  import { createFileRoute } from '@tanstack/react-router'

  export const Route = createFileRoute('/waitlist')({
    component: WaitlistPage,
  })

  export default function WaitlistPage() {
    const { waitlist, errors, fetchStatus } = useWaitlist()

    const handleSubmit = async (e: React.FormEvent) => {
      e.preventDefault()
      const formData = new FormData(e.currentTarget)
      const emailAddress = formData.get('emailAddress') as string

      const { error } = await waitlist.join({ emailAddress })
      if (error) {
        console.error('Failed to join waitlist:', error)
      }
    }

    if (waitlist.id) {
      return (
        <div>
          <h1>Successfully joined the waitlist!</h1>
          <p>We'll notify you when you're approved.</p>
        </div>
      )
    }

    return (
      <div>
        <h1>Join the Waitlist</h1>
        <form onSubmit={handleSubmit}>
          <label htmlFor="email">Email address</label>
          <input id="email" name="emailAddress" type="email" required />
          {errors.fields.emailAddress && <p>{errors.fields.emailAddress.longMessage}</p>}
          <button type="submit" disabled={fetchStatus === 'fetching'}>
            {fetchStatus === 'fetching' ? 'Submitting...' : 'Join Waitlist'}
          </button>
        </form>
      </div>
    )
  }
  ```


  ```tsx
// Filename: app/(auth)/waitlist.tsx

  import { useWaitlist } from '@clerk/expo'
  import { useState } from 'react'
  import { View, Text, TextInput, Button, StyleSheet } from 'react-native'

  export default function WaitlistScreen() {
    const { waitlist, errors, fetchStatus } = useWaitlist()
    const [emailAddress, setEmailAddress] = useState('')

    const handleSubmit = async () => {
      const { error } = await waitlist.join({ emailAddress })
      if (error) {
        console.error('Failed to join waitlist:', error)
      }
    }

    if (waitlist.id) {
      return (
        
          Successfully joined the waitlist!
          We'll notify you when you're approved.
        
      )
    }

    return (
      
        Join the Waitlist
        {errors.fields.emailAddress && (
          {errors.fields.emailAddress.longMessage}
        )}
        
    )
  }

  const styles = StyleSheet.create({
    container: {
      flex: 1,
      padding: 20,
      justifyContent: 'center',
    },
    title: {
      fontSize: 24,
      fontWeight: 'bold',
      marginBottom: 20,
    },
    message: {
      fontSize: 16,
      color: '#666',
    },
    input: {
      borderWidth: 1,
      borderColor: '#ccc',
      borderRadius: 5,
      padding: 10,
      marginBottom: 10,
    },
    error: {
      color: 'red',
      marginBottom: 10,
    },
  })
  ```


  ```tsx
// Filename: src/pages/waitlist.tsx

  import { useWaitlist } from '@clerk/chrome-extension'

  export default function Waitlist() {
    const { waitlist, errors, fetchStatus } = useWaitlist()

    const handleSubmit = async (e: React.FormEvent) => {
      e.preventDefault()
      const formData = new FormData(e.currentTarget)
      const emailAddress = formData.get('emailAddress') as string

      const { error } = await waitlist.join({ emailAddress })
      if (error) {
        console.error('Failed to join waitlist:', error)
      }
    }

    if (waitlist.id) {
      return (
        <div>
          <h1>Successfully joined the waitlist!</h1>
          <p>We'll notify you when you're approved.</p>
        </div>
      )
    }

    return (
      <div>
        <h1>Join the Waitlist</h1>
        <form onSubmit={handleSubmit}>
          <label htmlFor="email">Email address</label>
          <input id="email" name="emailAddress" type="email" required />
          {errors.fields.emailAddress && <p>{errors.fields.emailAddress.longMessage}</p>}
          <button type="submit" disabled={fetchStatus === 'fetching'}>
            {fetchStatus === 'fetching' ? 'Submitting...' : 'Join Waitlist'}
          </button>
        </form>
      </div>
    )
  }
  ```
