# React Quickstart


> Add authentication and user management to your React app with Clerk.

This tutorial will demonstrate how to create a new React app using Vite and add authentication to it using Clerk. If you would like to create an application using the React Router framework, see the [React Router quickstart](/react-router/getting-started/quickstart).


  ## Create a new React app

  If you don't already have a React app, run the following commands to [create a new one using Vite](https://vitejs.dev/guide/#scaffolding-your-first-vite-project).

  ```npm
  npm create vite@latest clerk-react -- --template react-ts
  cd clerk-react
  npm install
  ```

  ## Install `@clerk/react`

  The [Clerk React SDK](/reference/react/overview) gives you access to prebuilt components, hooks, and helpers to make user authentication easier.

  Run the following command to install the SDK:

  ```npm
  npm install @clerk/react
  ```

  ## Set your Clerk API keys

  
  Add your Clerk Publishable Key to your `.env` file.


  1. In the Clerk Dashboard, navigate to the [**API keys**](https://dashboard.clerk.com/~/api-keys) page.
  1. In the **Quick Copy** section, copy your Clerk Publishable Key.
  1. Paste your key into your `.env` file.

  The final result should resemble the following:


  ```env
// Filename: .env

  VITE_CLERK_PUBLISHABLE_KEY={{pub_key}}
  ```

  ## Add `` to your app

  The [``](/reference/components/clerk-provider) component provides session and user context to Clerk's hooks and components. It's recommended to wrap your entire app at the entry point with `` to make authentication globally accessible. See the [reference docs](/reference/components/clerk-provider) for other configuration options.


  ```tsx
// Filename: src/main.tsx

  import { StrictMode } from 'react'
  import { createRoot } from 'react-dom/client'
  import './index.css'
  import App from './App.tsx'
  import { ClerkProvider } from '@clerk/react'

  createRoot(document.getElementById('root')!).render(
    
      
        
    ,
  )
  ```

  ## Create a header with Clerk components

  You can control which content signed-in and signed-out users can see with the [prebuilt control components](/reference/components/overview#control-components). The following example creates a header using the following components:

  - [``](/reference/components/control/show): Children of this component can only be seen while **signed in**.
- [``](/reference/components/control/show): Children of this component can only be seen while **signed out**.
- [``](/reference/components/user/user-button): Shows the signed-in user's avatar. Selecting it opens a dropdown menu with account management options.
- [``](/reference/components/unstyled/sign-in-button): An unstyled component that links to the sign-in page. In this example, since no props or [environment variables](/guides/development/clerk-environment-variables) are set for the sign-in URL, this component links to the [Account Portal sign-in page](/guides/account-portal/overview#sign-in).
- [``](/reference/components/unstyled/sign-up-button): An unstyled component that links to the sign-up page. In this example, since no props or [environment variables](/guides/development/clerk-environment-variables) are set for the sign-up URL, this component links to the [Account Portal sign-up page](/guides/account-portal/overview#sign-up).


  ```tsx
// Filename: src/App.tsx

  import './App.css'
  import { Show, SignInButton, SignUpButton, UserButton } from '@clerk/react'

  function App() {
    return (
      <>
        <header>
          
            </header>
      </>
    )
  }

  export default App
  ```

  ## Run your project

Run your project with the following command:

```npm
npm run dev
```


  ## Create your first user

1. Visit your app's homepage at [http://localhost:5173](http://localhost:5173).
1. Select "Sign up" on the page and authenticate to create your first user.


## Next steps

Learn more about Clerk components, how to customize them, and how to use Clerk's client-side helpers using the following guides.


  - [Prebuilt components](/reference/components/overview)
  - Learn how to quickly add authentication to your app using Clerk's suite of components.

  ---

  - [Customization & localization](/guides/customizing-clerk/appearance-prop/overview)
  - Learn how to customize and localize Clerk components.

  ---

  - [Client-side helpers (hooks)](/reference/react/overview#custom-hooks)
  - Learn more about Clerk's client-side helpers and how to use them.

  ---

  - [Declarative mode](/guides/development/declarative-mode)
  - Learn how to use Clerk with React Router in declarative mode to add authentication to your app.

  ---

  - [Get started with Organizations](/react/guides/organizations/getting-started)
  - Learn how to create and manage Organizations in your React app.

  ---

  - [Clerk React SDK Reference](/reference/react/overview)
  - Learn about the Clerk React SDK and how to integrate it into your app.
