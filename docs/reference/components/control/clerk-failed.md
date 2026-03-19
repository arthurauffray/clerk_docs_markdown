# <ClerkFailed>


> The <ClerkFailed> component indicates that the Clerk object has failed to load.

The `` component indicates that the Clerk object has failed to load. This is useful for displaying an error message to the user.

## Example

It's not recommended to wrap the entire app in control components; instead, only wrap the components that need access to the `Clerk` object, such as custom flows.


  
**App Router:**

```tsx
// Filename: app/page.tsx

    import { ClerkLoaded, ClerkLoading, ClerkDegraded, ClerkFailed } from '@clerk/nextjs'

    export default function Page() {
      return (
        <>
          
            <p>Clerk is loading...</p>
          
          
            <p>Clerk has loaded (ready or degraded)</p>
            
              <p>Clerk is experiencing issues. Please try again later.</p>
            
          
          
            <p>Something went wrong with Clerk. Please contact support.</p>
          
        </>
      )
    }
    ```


**Pages Router:**

```tsx
// Filename: pages/index.tsx

    import { ClerkLoaded, ClerkLoading, ClerkDegraded, ClerkFailed } from '@clerk/nextjs'

    export default function Page() {
      return (
        <>
          
            <p>Clerk is loading...</p>
          
          
            <p>Clerk has loaded (ready or degraded)</p>
            
              <p>Clerk is experiencing issues. Please try again later.</p>
            
          
          
            <p>Something went wrong with Clerk. Please contact support.</p>
          
        </>
      )
    }
    ```


  ```tsx
// Filename: src/App.tsx

  import { ClerkLoaded, ClerkLoading, ClerkDegraded, ClerkFailed } from '@clerk/react'

  export default function App() {
    return (
      <>
        
          <p>Clerk is loading...</p>
        
        
          <p>Clerk has loaded (ready or degraded)</p>
          
            <p>Clerk is experiencing issues. Please try again later.</p>
          
        
        
          <p>Something went wrong with Clerk. Please contact support.</p>
        
      </>
    )
  }

  export default App
  ```


  ```tsx
// Filename: app/routes/example.tsx

  import { ClerkLoading, ClerkLoaded, ClerkDegraded, ClerkFailed } from '@clerk/react-router'

  export default function Example() {
    return (
      <>
        
          <p>Clerk is loading...</p>
        
        
          <p>Clerk has loaded (ready or degraded)</p>
          
            <p>Clerk is experiencing issues. Please try again later.</p>
          
        
        
          <p>Something went wrong with Clerk. Please contact support.</p>
        
      </>
    )
  }
  ```


  ```jsx
// Filename: src/routes/home.tsx

  import { ClerkLoaded, ClerkLoading, ClerkDegraded, ClerkFailed } from '@clerk/chrome-extension'

  export default function Home() {
    return (
      <>
        
          <p>Clerk is loading...</p>
        
        
          <p>Clerk has loaded (ready or degraded)</p>
          
            <p>Clerk is experiencing issues. Please try again later.</p>
          
        
        
          <p>Something went wrong with Clerk. Please contact support.</p>
        
      </>
    )
  }
  ```


  ```tsx
// Filename: app/routes/_index.tsx

  import { ClerkLoading, ClerkLoaded, ClerkDegraded, ClerkFailed } from '@clerk/remix'

  export default function Index() {
    return (
      <>
        
          <p>Clerk is loading...</p>
        
        
          <p>Clerk has loaded (ready or degraded)</p>
          
            <p>Clerk is experiencing issues. Please try again later.</p>
          
        
        
          <p>Something went wrong with Clerk. Please contact support.</p>
        
      </>
    )
  }
  ```


  ```tsx
// Filename: app/routes/index.tsx

  import { ClerkLoading, ClerkLoaded, ClerkDegraded, ClerkFailed } from '@clerk/tanstack-react-start'
  import { createFileRoute } from '@tanstack/react-router'

  export const Route = createFileRoute('/')({
    component: Home,
  })

  function Home() {
    return (
      <>
        
          <p>Clerk is loading...</p>
        
        
          <p>Clerk has loaded (ready or degraded)</p>
          
            <p>Clerk is experiencing issues. Please try again later.</p>
          
        
        
          <p>Something went wrong with Clerk. Please contact support.</p>
        
      </>
    )
  }
  ```
