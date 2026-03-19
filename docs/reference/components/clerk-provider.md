# <ClerkProvider>


> The <ClerkProvider> component provides session and user context to Clerk's hooks and components.

The `` component is required to integrate Clerk into your React application, providing session and user context to Clerk's hooks and components.

The recommended approach is to wrap your entire app with `` at the entry point to make authentication globally accessible. If you only need authentication for specific routes or pieces of your application, render `` deeper in the component tree. This allows you to implement Clerk's functionality precisely where required without impacting the rest of your app.

## Example


  
**App Router:**

```tsx
// Filename: app/layout.tsx

    import React from 'react'
    import { ClerkProvider } from '@clerk/nextjs'

    export default function RootLayout({ children }: { children: React.ReactNode }) {
      return (
        <html lang="en">
          <body>
            {children}
          </body>
        </html>
      )
    }
    ```


**Pages Router:**

```tsx
// Filename: _app.tsx

    import { ClerkProvider } from '@clerk/nextjs'
    import type { AppProps } from 'next/app'

    function MyApp({ Component, pageProps }: AppProps) {
      return (
        
          
      )
    }

    export default MyApp
    ```


  ```tsx
// Filename: index.tsx

  import React from 'react'
  import ReactDOM from 'react-dom/client'
  import App from './App.tsx'
  import { ClerkProvider } from '@clerk/react'

  // Import your Publishable Key
  const PUBLISHABLE_KEY = import.meta.env.VITE_CLERK_PUBLISHABLE_KEY

  if (!PUBLISHABLE_KEY) {
    throw new Error('Add your Clerk Publishable Key to the .env file')
  }

  ReactDOM.createRoot(document.getElementById('root')!).render(
    
      
        
    </React.StrictMode>,
  )
  ```


  ```tsx
// Filename: app/_layout.tsx

  import { ClerkProvider } from '@clerk/expo'
  import { Slot } from 'expo-router'

  // Import your Publishable Key
  const publishableKey = process.env.EXPO_PUBLIC_CLERK_PUBLISHABLE_KEY

  if (!publishableKey) {
    throw new Error('Add your Clerk Publishable Key to the .env file')
  }

  export default function Layout() {
    return (
      
        
    )
  }
  ```


  ```tsx
// Filename: app/root.tsx

  // Other imports

  import { ClerkProvider, Show, UserButton, SignInButton } from '@clerk/react-router'

  export default function App({ loaderData }: Route.ComponentProps) {
    return (
      
        <header className="flex items-center justify-center py-8 px-4">
          
            </header>
        <main>
          </main>
      
    )
  }

  // Rest of the root.tsx code
  ```


  ```jsx
// Filename: src/routes/index.tsx

  import { ClerkProvider, Show, SignInButton, UserButton } from '@clerk/chrome-extension'

  const PUBLISHABLE_KEY = process.env.PLASMO_PUBLIC_CLERK_PUBLISHABLE_KEY
  const EXTENSION_URL = chrome.runtime.getURL('.')

  if (!PUBLISHABLE_KEY) {
    throw new Error('Please add the PLASMO_PUBLIC_CLERK_PUBLISHABLE_KEY to the .env.development file')
  }

  export default function Index() {
    return (
      
        <header>
          
            </header>
      
    )
  }
  ```


  ```tsx
// Filename: src/routes/__root.tsx

  import * as React from 'react'
  import { HeadContent, Outlet, Scripts, createRootRoute } from '@tanstack/react-router'
  import { ClerkProvider } from '@clerk/tanstack-react-start'

  export const Route = createRootRoute({
    component: () => {
      return (
        
          
      )
    },
  })

  function RootDocument({ children }: { children: React.ReactNode }) {
    return (
      
        <html>
          <head>
            </head>
          <body>
            {children}
            </body>
        </html>
      
    )
  }
  ```


  - **`dynamic`** `boolean`

  Indicates whether or not Clerk should make dynamic auth data available based on the current request. Defaults to `false`. Opts the application into dynamic rendering when `true`. For more information, see [Next.js rendering modes and Clerk](/guides/development/rendering-modes).


  - **`tokenCache`** `TokenCache`

  Used to persist the active user's session token. Clerk stores this token in memory by default, however it is recommended to use a token cache for production applications.


  - **`syncHost`** `string`

  To enable, pass the URL of the web application that the extension will sync the authentication state from. See the [dedicated guide](/guides/sessions/sync-host) for more information.
