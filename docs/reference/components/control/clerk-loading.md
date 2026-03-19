# <ClerkLoading>


> The <ClerkLoading> renders its children while Clerk is loading, and is helpful for showing a custom loading state.

The `` renders its children while Clerk is loading, and is helpful for showing a custom loading state.

## Example

It's not recommended to wrap the entire app in the `` component; instead, only wrap the components that need access to the `Clerk` object.


  
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


  > [!NOTE]
  > Unlike other Clerk components for Astro, `ClerkLoading` must be imported from `@clerk/astro/react`. This requires that your Astro app is set up with React. See [Use Clerk with Astro and React](/reference/astro/react) for guidance.

  ```astro
// Filename: index.astro

  ---
  import { ClerkLoading, ClerkLoaded } from '@clerk/astro/react'
  ---

  
    <p>Clerk is loading</p>
  
  
    <p>Clerk has loaded</p>
  
  ```


  ```tsx
// Filename: app/index.tsx

  import { ClerkLoading, ClerkLoaded } from '@clerk/expo'
  import { Text, View } from 'react-native'

  export default function Screen() {
    return (
      
        
          Clerk is loading
        
        
          Clerk has loaded
        
      
    )
  }
  ```


  ```vue
// Filename: App.vue

  <script setup lang="ts">
  import { ClerkLoading, ClerkLoaded } from '@clerk/vue'
  </script>

  <template>
    
      <p>Clerk is loading</p>
    
    
      <p>Clerk has loaded</p>
    
  </template>
  ```


  ```vue
// Filename: App.vue

  <script setup lang="ts">
  // Components are automatically imported
  </script>

  <template>
    
      <p>Clerk is loading</p>
    
    
      <p>Clerk has loaded</p>
    
  </template>
  ```
