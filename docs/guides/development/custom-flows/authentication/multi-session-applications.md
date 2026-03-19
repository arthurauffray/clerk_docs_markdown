# Build a custom multi-session flow


> Learn how to use the Clerk API to add multi-session handling to your application.

> [!WARNING]
> This guide is for users who want to build a custom flow. To use a _prebuilt_ UI, use the [Account Portal pages](/guides/account-portal/overview) or [prebuilt components](/reference/components/overview).


A multi-session application is an application that allows multiple accounts to be signed in from the same browser at the same time. The user can switch from one account to another seamlessly. Each account is independent from the rest and has access to different resources.

This guide provides you with the necessary information to build a custom multi-session flow using the Clerk API.

To implement the multi-session feature to your application, you need to handle the following scenarios:

- [Switching between different accounts](#switch-between-sessions)
- [Adding new accounts](#add-a-new-session)
- [Signing out from one account, while remaining signed in to the rest](#sign-out-active-session)
- [Signing out from all accounts](#sign-out-all-sessions)

## Enable multi-session in your application

To enable multi-session in your application, you need to configure it in the Clerk Dashboard.

1. In the Clerk Dashboard, navigate to the [**Sessions**](https://dashboard.clerk.com/~/sessions) page.
1. Toggle on **Multi-session handling**.
1. Select **Save changes**.

## Get the session and user


  ```jsx
  // Import the useClerk() hook from whatever SDK you're using
  import { useClerk } from '@clerk/react'

  // Get the session and user
  const { session, user } = useClerk()
  ```


  ```js
  // Get the session
  const currentSession = window.Clerk.session

  // Get the user
  const currentUser = window.Clerk.user
  ```


  ```swift
  // Get the current session
  var currentSession: Session? { clerk.session }

  // Get the current user
  var currentUser: User? { clerk.user }
  ```


  ```kotlin
  // Get the current session
  val currentSession = Clerk.session

  // Get the current user
  val currentUser = Clerk.user
  ```


## Switch between sessions


  ```jsx
  // Import the useClerk() hook from whatever SDK you're using
  import { useClerk } from '@clerk/react'

  const { client, setActive } = useClerk()

  // You can get all the available sessions through the client
  const availableSessions = client.sessions
  const currentSession = availableSessions[0].id

  // Use setActive() to set the session as active
  await setActive({
    session: currentSession.id,
    navigate: async ({ session, decorateUrl }) => {
      if (session?.currentTask) {
        //  Handle pending session tasks
        // See https://clerk.com/docs/guides/development/custom-flows/authentication/session-tasks
        console.log(session?.currentTask)
        return
      }

      const url = decorateUrl('/')
      if (url.startsWith('http')) {
        window.location.href = url
      } else {
        router.push(url)
      }
    },
  })
  ```


  ```js
  // You can get all the available sessions through the client
  const availableSessions = window.Clerk.client.sessions

  // Use setActive() to set the session as active
  await window.Clerk.setActive({
    session: availableSessions[0].id,
    navigate: async ({ session, decorateUrl }) => {
      if (session?.currentTask) {
        //  Handle pending session tasks
        // See https://clerk.com/docs/guides/development/custom-flows/authentication/session-tasks
        console.log(session?.currentTask)
        return
      }

      const url = decorateUrl('/')
      if (url.startsWith('http')) {
        window.location.href = url
      } else {
        window.location.href = url
      }
    },
  })
  ```


  ```swift
  // You can get all the available sessions through the client.
  var availableSessions: [Session] { clerk.auth.sessions }

  // Use setActive() to set the session as active.
  try await clerk.auth.setActive(sessionId: availableSessions[0].id)
  ```


  ```kotlin
  import com.clerk.api.Clerk
  import com.clerk.api.network.serialization.onFailure
  import com.clerk.api.network.serialization.onSuccess

  val availableSessions = Clerk.client.sessions
  val sessionId = availableSessions.firstOrNull()?.id ?: return

  Clerk.auth
    .setActive(sessionId = sessionId)
    .onSuccess {
      // Session switched
    }
    .onFailure {
      // See https://clerk.com/docs/guides/development/custom-flows/error-handling
      // for more info on error handling
    }
  ```


## Add a new session

To add a new session, simply link to your existing sign-in flow. New sign-ins will automatically add to the list of available sessions on the client. To create a sign-in flow, see one of the following popular guides:

- [Email and password](/guides/development/custom-flows/authentication/email-password)
- [Passwordless authentication](/guides/development/custom-flows/authentication/email-sms-otp)
- [Social sign-in (OAuth)](/guides/configure/auth-strategies/social-connections/overview)

## Sign out all sessions

Use [`signOut()`](/reference/javascript/clerk#sign-out) to deactivate all sessions on the current client.


  ```jsx
  // Import the useClerk() hook from whatever SDK you're using
  import { useClerk } from '@clerk/react'

  const { signOut, session } = useClerk()

  // Use signOut to sign-out all active sessions
  await signOut()
  ```


  ```js
  // Use signOut to sign-out all active sessions
  await window.Clerk.signOut()
  ```


  ```swift
  // Use signOut to sign-out all active sessions
  try await clerk.auth.signOut()
  ```


  ```kotlin
  import com.clerk.api.Clerk
  import com.clerk.api.network.serialization.onFailure
  import com.clerk.api.network.serialization.onSuccess

  // Use signOut to sign-out all active sessions
  Clerk.auth
    .signOut()
    .onSuccess {
      // Signed out
    }
    .onFailure {
      // See https://clerk.com/docs/guides/development/custom-flows/error-handling
      // for more info on error handling
    }
  ```


## Sign out active session

Use [`signOut()`](/reference/javascript/clerk#sign-out) to deactivate a specific session by passing the session ID.


  ```jsx
  import { useClerk } from '@clerk/react'

  // Get the signOut method and the active session
  const { signOut, session } = useClerk()

  // Use signOut to sign-out the active session
  await signOut(session.id)
  ```


  ```js
  // Get the current session
  const currentSession = window.Clerk.session

  // Use signOut to sign-out the active session
  await window.Clerk.signOut(currentSession.id)
  ```


  ```swift
  // Use signOut to sign-out a specific session
  try await clerk.auth.signOut(sessionId: session.id)
  ```


  ```kotlin
  import com.clerk.api.Clerk
  import com.clerk.api.network.serialization.onFailure
  import com.clerk.api.network.serialization.onSuccess

  val currentSessionId = Clerk.session?.id ?: return

  // Use signOut to sign-out a specific session
  Clerk.auth
    .signOut(sessionId = currentSessionId)
    .onSuccess {
      // Signed out from the active session
    }
    .onFailure {
      // See https://clerk.com/docs/guides/development/custom-flows/error-handling
      // for more info on error handling
    }
  ```
