# useAuth()


> Access and manage authentication state in your application with Clerk's useAuth() hook.

The `useAuth()` hook provides access to the current user's authentication state and methods to manage the active session. You can use this hook to get the user's authentication and organization information, like their ID, session ID, session token, organization ID, and organization role, and to check if the user is authenticated or authorized to access a specific resource.

> [!NOTE]
> To access auth data server-side, see the [`Auth` object reference doc](/reference/backend/types/auth-object).


  By default, Next.js opts all routes into static rendering. If you need to opt a route or routes into dynamic rendering because you need to access the authentication data at request time, you can create a boundary by passing the `dynamic` prop to ``. See the [guide on rendering modes](/guides/development/rendering-modes) for more information, including code examples.


## Example

The following example demonstrates how to use the `useAuth()` hook to access the current auth state, like whether the user is signed in or not. It also includes a basic example for using the `getToken()` method to retrieve a session token for fetching data from an external resource.


  ```tsx
// Filename: src/pages/ExternalDataPage.tsx

  import { useAuth } from '@clerk/react'

  export default function ExternalDataPage() {
    const { userId, sessionId, getToken, isLoaded, isSignedIn } = useAuth()

    const fetchExternalData = async () => {
      const token = await getToken()

      // Fetch data from an external API
      const response = await fetch('https://api.example.com/data', {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      })

      return response.json()
    }

    // Handle loading state
    if (!isLoaded) return <div>Loading...</div>

    // Protect the page from unauthenticated users
    if (!isSignedIn) return <div>Sign in to view this page</div>

    return (
      <div>
        <p>
          Hello, {userId}! Your current active session is {sessionId}.
        </p>
        <button onClick={fetchExternalData}>Fetch Data</button>
      </div>
    )
  }
  ```


  ```tsx
// Filename: app/external-data/page.tsx

  'use client'

  import { useAuth } from '@clerk/nextjs'

  export default function Page() {
    const { userId, sessionId, getToken, isLoaded, isSignedIn } = useAuth()

    const fetchExternalData = async () => {
      const token = await getToken()

      // Fetch data from an external API
      const response = await fetch('https://api.example.com/data', {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      })

      return response.json()
    }

    // Handle loading state
    if (!isLoaded) return <div>Loading...</div>

    // Protect the page from unauthenticated users
    if (!isSignedIn) return <div>Sign in to view this page</div>

    return (
      <div>
        <p>
          Hello, {userId}! Your current active session is {sessionId}.
        </p>
        <button onClick={fetchExternalData}>Fetch Data</button>
      </div>
    )
  }
  ```


  ```tsx
// Filename: app/routes/home.tsx

  import { useAuth } from '@clerk/react-router'

  export default function Home() {
    const { userId, sessionId, getToken, isLoaded, isSignedIn } = useAuth()

    const fetchExternalData = async () => {
      const token = await getToken()

      // Fetch data from an external API
      const response = await fetch('https://api.example.com/data', {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      })

      return response.json()
    }

    // Handle loading state
    if (!isLoaded) return <div>Loading...</div>

    // Protect the page from unauthenticated users
    if (!isSignedIn) return <div>Sign in to view this page</div>

    return (
      <div>
        <p>
          Hello, {userId}! Your current active session is {sessionId}.
        </p>
        <button onClick={fetchExternalData}>Fetch Data</button>
      </div>
    )
  }
  ```


  ```tsx
// Filename: src/components/external-data.jsx

  import { useAuth } from '@clerk/astro/react'
  import { useState } from 'react'

  export default function ExternalData() {
    const { userId, sessionId, getToken, isLoaded, isSignedIn } = useAuth()
    const [data, setData] = useState(null)

    const fetchExternalData = async () => {
      const token = await getToken()
      const response = await fetch('https://api.example.com/data', {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      })
      const json = await response.json()
      setData(json)
    }

    // Handle loading state
    if (!isLoaded) return <div>Loading...</div>

    // Protect the page from unauthenticated users
    if (!isSignedIn) return <div>Sign in to view this page</div>

    return (
      <div>
        <p>
          Hello, {userId}! Your current active session is {sessionId}.
        </p>
        <button onClick={fetchExternalData}>Fetch Data</button>

        {data && <pre>{JSON.stringify(data, null, 2)}</pre>}
      </div>
    )
  }
  ```

  ```astro
// Filename: src/pages/auth.astro

  ---
  import ExternalData from '../components/external-data'
  ---

  ```


  ```tsx
// Filename: src/routes/page.tsx

  import { useAuth } from '@clerk/chrome-extension'

  export default function ExternalDataPage() {
    const { userId, sessionId, getToken, isLoaded, isSignedIn } = useAuth()

    const fetchExternalData = async () => {
      const token = await getToken()

      // Fetch data from an external API
      const response = await fetch('https://api.example.com/data', {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      })

      return response.json()
    }

    // Handle loading state
    if (!isLoaded) return <div>Loading...</div>

    // Protect the page from unauthenticated users
    if (!isSignedIn) return <div>Sign in to view this page</div>

    return (
      <div>
        <p>
          Hello, {userId}! Your current active session is {sessionId}.
        </p>
        <button onClick={fetchExternalData}>Fetch Data</button>
      </div>
    )
  }
  ```


  ```tsx
// Filename: app/routes/index.tsx

  import { useAuth } from '@clerk/tanstack-react-start'
  import { createFileRoute } from '@tanstack/react-router'

  export const Route = createFileRoute('/')({
    component: ExternalDataPage,
  })

  function ExternalDataPage() {
    const { userId, sessionId, getToken, isLoaded, isSignedIn } = useAuth()

    const fetchExternalData = async () => {
      const token = await getToken()

      // Fetch data from an external API
      const response = await fetch('https://api.example.com/data', {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      })

      return response.json()
    }

    // Handle loading state
    if (!isLoaded) return <div>Loading...</div>

    // Protect the page from unauthenticated users
    if (!isSignedIn) return <div>Sign in to view this page</div>

    return (
      <div>
        <p>
          Hello, {userId}! Your current active session is {sessionId}.
        </p>
        <button onClick={fetchExternalData}>Fetch Data</button>
      </div>
    )
  }
  ```


  ```tsx
// Filename: app/external-data.tsx

  import { useAuth } from '@clerk/expo'
  import { Text, View, TouchableOpacity } from 'react-native'

  export default function ExternalData() {
    const { userId, sessionId, getToken, isLoaded, isSignedIn } = useAuth()

    const fetchExternalData = async () => {
      const token = await getToken()

      // Fetch data from an external API
      const response = await fetch('https://api.example.com/data', {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      })

      return response.json()
    }

    // Handle loading state
    if (!isLoaded) return Loading...

    // Protect the page from unauthenticated users
    if (!isSignedIn) return Sign in to view this page

    return (
      
        
          Hello, {userId}! Your current active session is {sessionId}.
        
        
          Fetch Data
        
      
    )
  }
  ```
