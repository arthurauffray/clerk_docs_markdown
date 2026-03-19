# useSignUp()


> Access and manage the current user's sign-up state in your React application with Clerk's useSignUp() hook.

> [!WARNING]
> This hook uses our legacy API, which will be removed in a future release. We recommend migrating to the new [`useSignUp()`](/reference/hooks/use-sign-up) hook instead.

The `useSignUp()` hook provides access to the [`SignUp`](/reference/javascript/sign-up) object, which allows you to check the current state of a sign-up attempt and manage the sign-up flow. You can use this to create a custom sign-up flow.

## Examples

### Check the current state of a sign-up

The following example uses the `useSignUp()` hook to access the [`SignUp`](/reference/javascript/sign-up) object, which contains the current sign-up attempt status and methods to create a new sign-up attempt. The `isLoaded` property is used to handle the loading state.


  ```tsx
// Filename: src/pages/SignUpPage.tsx

  import { useSignUp } from '@clerk/react'

  export default function SignUpPage() {
    const { isLoaded, signUp } = useSignUp()

    // Handle loading state
    if (!isLoaded) return <div>Loading...</div>

    return <div>The current sign-up attempt status is {signUp?.status}.</div>
  }
  ```


  ```tsx
// Filename: app/sign-up/page.tsx

  'use client'

  import { useSignUp } from '@clerk/nextjs'

  export default function Page() {
    const { isLoaded, signUp } = useSignUp()

    // Handle loading state
    if (!isLoaded) return <div>Loading...</div>

    return <div>The current sign-up attempt status is {signUp?.status}.</div>
  }
  ```


  ```tsx
// Filename: app/routes/sign-up.tsx

  import { useSignUp } from '@clerk/react-router'

  export default function SignUpPage() {
    const { isLoaded, signUp } = useSignUp()

    // Handle loading state
    if (!isLoaded) return <div>Loading...</div>

    return <div>The current sign-up attempt status is {signUp?.status}.</div>
  }
  ```


  ```tsx
// Filename: src/routes/page.tsx

  import { useSignUp } from '@clerk/chrome-extension'

  export default function SignUpPage() {
    const { isLoaded, signUp } = useSignUp()

    // Handle loading state
    if (!isLoaded) return <div>Loading...</div>

    return <div>The current sign-up attempt status is {signUp?.status}.</div>
  }
  ```


  ```tsx
// Filename: app/routes/index.tsx

  import { useSignUp } from '@clerk/tanstack-react-start'
  import { createFileRoute } from '@tanstack/react-router'

  export const Route = createFileRoute('/')({
    component: SignUpPage,
  })

  export default function SignUpPage() {
    const { isLoaded, signUp } = useSignUp()

    // Handle loading state
    if (!isLoaded) return Loading...

    return <div>The current sign-up attempt status is {signUp?.status}.</div>
  }
  ```


  ```tsx
// Filename: app/(auth)/sign-up.tsx

  import { useSignUp } from '@clerk/expo'
  import { Text, View } from 'react-native'

  export default function SignUpPage() {
    const { isLoaded, signUp } = useSignUp()

    // Handle loading state
    if (!isLoaded) return Loading...

    return (
      
        The current sign-up attempt status is {signUp?.status}.
      
    )
  }
  ```


### Create a custom sign-up flow with `useSignUp()`

The `useSignUp()` hook can also be used to build fully custom sign-up flows, if Clerk's prebuilt components don't meet your specific needs or if you require more control over the authentication flow. Different sign-up flows include email and password, email and phone codes, email links, and multifactor (MFA). To learn more about using the `useSignUp()` hook to create custom flows, see the [custom flow guides](/guides/development/custom-flows/overview).
