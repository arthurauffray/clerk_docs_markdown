# Build a custom waitlist form


> Learn how to use the Clerk API to build a custom waitlist form using Clerk's useWaitlist() hook.

> [!WARNING]
> This guide is for users who want to build a custom flow. To use a _prebuilt_ UI, use the [Account Portal pages](/guides/account-portal/overview) or [prebuilt components](/reference/components/overview).


Clerk's [``](/reference/components/authentication/waitlist) component provides an out-of-the-box solution for allowing users to join your waitlist for early access to your app. However, if you're building a custom user interface, you can use the [`useWaitlist()`](/reference/hooks/use-waitlist) hook to build a custom waitlist form.

This guide demonstrates how to use the Clerk API to build a custom user interface for joining your app's waitlist.

## Before you start

Before using the `useWaitlist()` hook, you must enable **Waitlist** mode in the Clerk Dashboard:

1. In the Clerk Dashboard, navigate to the [**Waitlist**](https://dashboard.clerk.com/~/user-authentication/waitlist) page.
1. Toggle on **Enable waitlist** and select **Save**.

## Build the custom flow

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


  
**index.html:**

```html
<!-- Filename: index.html -->

    <!doctype html>
    <html lang="en">
      <head>
        <meta charset="UTF-8" />
        <link rel="icon" type="image/svg+xml" href="/clerk.svg" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>Clerk + JavaScript App</title>
      </head>

      <body>
        <div id="success-message" style="display: none">
          <h1>Successfully joined the waitlist!</h1>
          <p>We'll notify you when you're approved.</p>
        </div>

        <div id="waitlist-form-container">
          <h1>Join the Waitlist</h1>
          <form id="waitlist-form">
            <label for="email">Email address</label>
            <input id="email" name="emailAddress" type="email" required />
            <p id="error" style="color: red"></p>
            <button type="submit">Join Waitlist</button>
          </form>
        </div>

        <script type="module" src="main.js" async crossorigin="anonymous"></script>
      </body>
    </html>
    ```


**main.js:**

```js
// Filename: main.js

    import { Clerk } from '@clerk/clerk-js'

    const pubKey = import.meta.env.VITE_CLERK_PUBLISHABLE_KEY

    const clerk = new Clerk(pubKey)
    await clerk.load()

    const successMessage = document.getElementById('success-message')
    const formContainer = document.getElementById('waitlist-form-container')
    const form = document.getElementById('waitlist-form')
    const errorElement = document.getElementById('error')

    // Check if user has already joined the waitlist
    if (clerk.waitlist?.id) {
      successMessage.style.display = 'block'
      formContainer.style.display = 'none'
    } else {
      form.addEventListener('submit', async (e) => {
        e.preventDefault()
        const formData = new FormData(e.target)
        const emailAddress = formData.get('emailAddress')

        try {
          await clerk.waitlist.join({ emailAddress })
          // Show success message
          successMessage.style.display = 'block'
          formContainer.style.display = 'none'
        } catch (error) {
          // Display error message
          errorElement.textContent = error.errors?.[0]?.longMessage || 'Failed to join waitlist'
        }
      })
    }
    ```
