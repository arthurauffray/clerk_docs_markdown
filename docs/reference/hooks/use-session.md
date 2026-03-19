# useSession()


> Access and manage the current user's session in your React application with Clerk's useSession() hook.

The `useSession()` hook provides access to the current user's [`Session`](/reference/javascript/session) object, as well as helpers for setting the active session.

## Example

### Access the `Session` object

The following example uses the `useSession()` hook to access the `Session` object, which has the `lastActiveAt` property. The `lastActiveAt` property is a `Date` object used to show the time the session was last active.


  ```tsx
// Filename: src/pages/Home.tsx

  import { useSession } from '@clerk/react'

  export default function Home() {
    const { isLoaded, session, isSignedIn } = useSession()

    // Handle loading state
    if (!isLoaded) return <div>Loading...</div>

    // Protect the page from unauthenticated users
    if (!isSignedIn) return <div>Sign in to view this page</div>

    return (
      <div>
        <p>This session has been active since {session.lastActiveAt.toLocaleString()}</p>
      </div>
    )
  }
  ```


  ```tsx
// Filename: app/home/page.tsx

  'use client'

  import { useSession } from '@clerk/nextjs'

  export default function Page() {
    const { isLoaded, session, isSignedIn } = useSession()

    // Handle loading state
    if (!isLoaded) return <div>Loading...</div>

    // Protect the page from unauthenticated users
    if (!isSignedIn) return <div>Sign in to view this page</div>

    return (
      <div>
        <p>This session has been active since {session.lastActiveAt.toLocaleString()}</p>
      </div>
    )
  }
  ```


  ```tsx
// Filename: app/routes/home.tsx

  import { useSession } from '@clerk/react-router'

  export default function Home() {
    const { isLoaded, session, isSignedIn } = useSession()

    // Handle loading state
    if (!isLoaded) return <div>Loading...</div>

    // Protect the page from unauthenticated users
    if (!isSignedIn) return <div>Sign in to view this page</div>

    return (
      <div>
        <p>This session has been active since {session.lastActiveAt.toLocaleString()}</p>
      </div>
    )
  }
  ```


  ```tsx
// Filename: src/routes/page.tsx

  import { useSession } from '@clerk/chrome-extension'

  export default function HomePage() {
    const { isLoaded, session, isSignedIn } = useSession()

    // Handle loading state
    if (!isLoaded) return <div>Loading...</div>

    // Protect the page from unauthenticated users
    if (!isSignedIn) return <div>Sign in to view this page</div>

    return (
      <div>
        <p>This session has been active since {session.lastActiveAt.toLocaleString()}</p>
      </div>
    )
  }
  ```


  ```tsx
// Filename: app/routes/index.tsx

  import { useSession } from '@clerk/tanstack-react-start'
  import { createFileRoute } from '@tanstack/react-router'

  export const Route = createFileRoute('/')({
    component: HomePage,
  })

  function HomePage() {
    const { isLoaded, session, isSignedIn } = useSession()

    // Handle loading state
    if (!isLoaded) return <div>Loading...</div>

    // Protect the page from unauthenticated users
    if (!isSignedIn) return <div>Sign in to view this page</div>

    return (
      <div>
        <p>This session has been active since {session.lastActiveAt.toLocaleString()}</p>
      </div>
    )
  }
  ```


  ```tsx
// Filename: app/(session)/page.tsx

  import { useSession } from '@clerk/expo'
  import { Text, View } from 'react-native'

  export default function HomePage() {
    const { isLoaded, session, isSignedIn } = useSession()

    // Handle loading state
    if (!isLoaded) return Loading...

    // Protect the page from unauthenticated users
    if (!isSignedIn) return Sign in to view this page

    return (
      
        This session has been active since {session.lastActiveAt.toLocaleString()}
      
    )
  }
  ```
