# useSessionList()


> Access and manage the current user's session list in your React application with Clerk's useSessionList() hook.

The `useSessionList()` hook returns an array of [`Session`](/reference/javascript/session) objects that have been registered on the client device.

## Example

### Get a list of sessions

The following example uses `useSessionList()` to get a list of sessions that have been registered on the client device. The `sessions` property is used to show the number of times the user has visited the page.


  ```tsx
// Filename: src/pages/Home.tsx

  import { useSessionList } from '@clerk/react'

  export default function Home() {
    const { isLoaded, sessions } = useSessionList()

    // Handle loading state
    if (!isLoaded) return <div>Loading...</div>

    return (
      <div>
        <p>Welcome back. You've been here {sessions.length} times before.</p>
      </div>
    )
  }
  ```


  ```tsx
// Filename: app/home/page.tsx

  'use client'

  import { useSessionList } from '@clerk/nextjs'

  export default function Page() {
    const { isLoaded, sessions } = useSessionList()

    // Handle loading state
    if (!isLoaded) return <div>Loading...</div>

    return (
      <div>
        <p>Welcome back. You've been here {sessions.length} times before.</p>
      </div>
    )
  }
  ```


  ```tsx
// Filename: app/routes/home.tsx

  import { useSessionList } from '@clerk/react-router'

  export default function Home() {
    const { isLoaded, sessions } = useSessionList()

    // Handle loading state
    if (!isLoaded) return <div>Loading...</div>

    return (
      <div>
        <p>Welcome back. You've been here {sessions.length} times before.</p>
      </div>
    )
  }
  ```


  ```tsx
// Filename: src/routes/page.tsx

  import { useSessionList } from '@clerk/chrome-extension'

  export default function Home() {
    const { isLoaded, sessions } = useSessionList()

    // Handle loading state
    if (!isLoaded) return <div>Loading...</div>

    return (
      <div>
        <p>Welcome back. You've been here {sessions.length} times before.</p>
      </div>
    )
  }
  ```


  ```tsx
// Filename: app/routes/index.tsx

  import { useSessionList } from '@clerk/tanstack-react-start'
  import { createFileRoute } from '@tanstack/react-router'

  export const Route = createFileRoute('/')({
    component: Home,
  })

  export default function Home() {
    const { isLoaded, sessions } = useSessionList()

    // Handle loading state
    if (!isLoaded) return <div>Loading...</div>

    return (
      <div>
        <p>Welcome back. You've been here {sessions.length} times before.</p>
      </div>
    )
  }
  ```


  ```tsx
// Filename: app/(session-list)/page.tsx

  import { useSessionList } from '@clerk/expo'
  import { Text, View } from 'react-native'

  export default function Home() {
    const { isLoaded, sessions } = useSessionList()

    // Handle loading state
    if (!isLoaded) return Loading...

    return (
      
        Welcome back. You've been here {sessions.length} times before.
      
    )
  }
  ```
