# useClerk()


> Access and manage the Clerk object in your React application with Clerk's useClerk() hook.

> [!WARNING]
> This hook should only be used for advanced use cases, such as building a completely custom OAuth flow or as an escape hatch to access to the `Clerk` object.

The `useClerk()` hook provides access to the [`Clerk`](/reference/javascript/clerk) object, allowing you to build alternatives to any Clerk Component.

## Example

The following example uses the `useClerk()` hook to access the `clerk` object. The `clerk` object is used to call the [`openSignIn()`](/reference/javascript/clerk#sign-in) method to open the sign-in modal.


  ```tsx
// Filename: src/pages/Example.tsx

  import { useClerk } from '@clerk/react'

  export default function Example() {
    const clerk = useClerk()

    return <button onClick={() => clerk.openSignIn({})}>Sign in</button>
  }
  ```


  ```tsx
// Filename: app/page.tsx

  'use client'

  import { useClerk } from '@clerk/nextjs'

  export default function Page() {
    const clerk = useClerk()

    return <button onClick={() => clerk.openSignIn({})}>Sign in</button>
  }
  ```


  ```tsx
// Filename: app/routes/home.tsx

  import { useClerk } from '@clerk/react-router'

  export default function Home() {
    const clerk = useClerk()

    return <button onClick={() => clerk.openSignIn({})}>Sign in</button>
  }
  ```


  ```tsx
// Filename: src/routes/page.tsx

  import { useClerk } from '@clerk/chrome-extension'

  export default function Home() {
    const clerk = useClerk()

    return <button onClick={() => clerk.openSignIn({})}>Sign in</button>
  }
  ```


  ```tsx
// Filename: app/routes/index.tsx

  import { useClerk } from '@clerk/tanstack-react-start'
  import { createFileRoute } from '@tanstack/react-router'

  export const Route = createFileRoute('/')({
    component: Home,
  })

  export default function Home() {
    const clerk = useClerk()

    return <button onClick={() => clerk.openSignIn({})}>Sign in</button>
  }
  ```


  ```tsx
// Filename: app/(clerk)/index.tsx

  import { useClerk } from '@clerk/expo'
  import { Text, View, TouchableOpacity } from 'react-native'

  export default function Page() {
    const clerk = useClerk()

    return (
      
         clerk.openSignIn({})}>
          Sign in
        
      
    )
  }
  ```
