# Add React Router to your Clerk + React application


> Learn how to add React Router to your Clerk + React application.

React Router supports three different routing strategies, or ["modes"](https://reactrouter.com/start/modes):

- **Declarative mode:** Enables basic routing features like matching URLs to components, navigating around the app, and providing active states with APIs like ``, `useNavigate()`, and `useLocation()`.
- **Data mode:** Adds data loading, actions, pending states and more with APIs like loader, action, and useFetcher. To use React Router in data mode, see the [demo repository](https://github.com/clerk/clerk-react-quickstart/blob/integrate-react-router-dom-using-data-router-method/src/main.tsx). A guide is coming soon.
- **Framework mode:** Use React Router as a framework to build your entire app. To use React Router as a framework instead, see the [React Router quickstart](/react-router/getting-started/quickstart).

This guide will cover how to add React Router in **declarative mode**, assuming you have followed the [React quickstart](/react/getting-started/quickstart).


  ## Install `react-router` and `@clerk/react-router`

  Run the following command to install both React Router and the Clerk React Router SDK:

  ```npm
  npm install react-router @clerk/react-router
  ```

  ## Set your Clerk API keys

  > [!NOTE]
  > You will not need the Clerk Secret Key in React Router's declarative mode, as it should never be used on the client-side.

  
  Add your Clerk Publishable Key to your `.env` file.


  1. In the Clerk Dashboard, navigate to the [**API keys**](https://dashboard.clerk.com/~/api-keys) page.
  1. In the **Quick Copy** section, copy your Clerk Publishable Key.
  1. Paste your key into your `.env` file.

  The final result should resemble the following:


  ```env
// Filename: .env

  VITE_CLERK_PUBLISHABLE_KEY={{pub_key}}
  ```

  ## Update ``

  Update `` to be imported from `@clerk/react-router` instead of `@clerk/react`.

  ```tsx
// Filename: src/main.tsx

  import { StrictMode } from 'react'
  import { createRoot } from 'react-dom/client'
  import { ClerkProvider } from '@clerk/react-router'
  import './index.css'
  import App from './App.tsx'

  // Import your Publishable Key
  const PUBLISHABLE_KEY = import.meta.env.VITE_CLERK_PUBLISHABLE_KEY

  if (!PUBLISHABLE_KEY) {
    throw new Error('Add your Clerk Publishable Key to the .env file')
  }

  createRoot(document.getElementById('root')!).render(
    
      
        
    ,
  )
  ```

  ## Set up React Router

  To use declarative mode, wrap your app in a ``. To define your app's routes, add `` and `` components. This example adds the `/` (home) route and renders the `` component when the URL matches. Read more about routing in the [React Router docs](https://reactrouter.com/start/declarative/routing).

  ```tsx
// Filename: src/main.tsx

  import { StrictMode } from 'react'
  import { createRoot } from 'react-dom/client'
  import { BrowserRouter, Routes, Route } from 'react-router'
  import { ClerkProvider } from '@clerk/react-router'
  import './index.css'
  import App from './App.tsx'

  // Import your Publishable Key
  const PUBLISHABLE_KEY = import.meta.env.VITE_CLERK_PUBLISHABLE_KEY

  if (!PUBLISHABLE_KEY) {
    throw new Error('Add your Clerk Publishable Key to the .env file')
  }

  createRoot(document.getElementById('root')!).render(
    
      
        
          
            } />
          
        
      
    ,
  )
  ```


## Next steps

Learn more about Clerk components, how to use them to create custom pages, and how to use Clerk's client-side helpers using the following guides.


  - [Create a custom sign-up page](/react-router/guides/development/custom-sign-up-page)
  - Learn how to add a custom sign-up page to your React Router app with Clerk's components.

  ---

  - [Protect content and read user data](/react-router/guides/users/reading)
  - Learn how to use Clerk's hooks and helpers to protect content and read user data in your React Router app.

  ---

  - [Client-side helpers](/reference/react-router/overview#client-side-helpers)
  - Learn more about Clerk's client-side helpers and how to use them.

  ---

  - [Prebuilt components](/reference/components/overview)
  - Learn how to quickly add authentication to your app using Clerk's suite of components.

  ---

  - [Clerk React Router SDK Reference](/reference/react-router/overview)
  - Learn about the Clerk React Router SDK and how to integrate it into your app.
