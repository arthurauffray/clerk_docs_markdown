# Sign-up with application invitations


> Learn how to use the Clerk API to build a custom flow for handling application invitations.

> [!WARNING]
> This guide is for users who want to build a custom flow. To use a _prebuilt_ UI, use the [Account Portal pages](/guides/account-portal/overview) or [prebuilt components](/reference/components/overview).


  > [!IMPORTANT]
  > This guide applies to the following Clerk SDKs:
  >
  > - `@clerk/react` v6 or higher
  > - `@clerk/nextjs` v7 or higher
  > - `@clerk/expo` v3 or higher
  > - `@clerk/react-router` v3 or higher
  > - `@clerk/tanstack-react-start` v0.26.0 or higher
  >
  > If you're using an older version of one of these SDKs, or are using the legacy API, refer to the [legacy API documentation](/guides/development/custom-flows/authentication/legacy/application-invitations).


When a user visits an [invitation](/guides/users/inviting) link, Clerk first checks whether a custom redirect URL was provided.

**If no redirect URL is specified**, the user will be redirected to the appropriate Account Portal page (either [sign-up](/guides/account-portal/overview#sign-up) or [sign-in](/guides/account-portal/overview#sign-in)), or to the custom sign-up/sign-in pages that you've configured for your application.

**If you specified [a redirect URL when creating the invitation](/guides/users/inviting#with-a-redirect-url)**, you must handle the authentication flows in your code for that page. You can either embed the [``](/reference/components/authentication/sign-in) component on that page, or if the prebuilt component doesn't meet your specific needs or if you require more control over the logic, you can rebuild the existing Clerk flows using the Clerk API.

This guide demonstrates how to use Clerk's API to build a custom flow for accepting application invitations.

## Build the custom flow

Once the user visits the invitation link and is redirected to the specified URL, the query parameter `__clerk_ticket` will be appended to the URL. This query parameter contains the invitation token.

For example, if the redirect URL was `https://www.example.com/accept-invitation`, the URL that the user would be redirected to would be `https://www.example.com/accept-invitation?__clerk_ticket=.....`.


  
    > [!TIP]
> Examples for this SDK aren't available yet. For now, try adapting the  available example to fit your SDK.

  

  To create a sign-up flow using that invitation token, you need to call the [`signUp.ticket()`](/reference/javascript/sign-up-future#ticket) method, as shown in the following example. The following example also demonstrates how to collect additional user information for the sign-up; you can either remove these fields or adjust them to fit your application.

  ```tsx
// Filename: app/accept-invitation/page.tsx

  'use client'

  import * as React from 'react'
  import { useSignUp, useUser } from '@clerk/nextjs'
  import { useRouter } from 'next/navigation'

  export default function Page() {
    const { isSignedIn, user } = useUser()
    const { signUp, errors, fetchStatus } = useSignUp()
    const router = useRouter()

    const handleSubmit = async (formData: FormData) => {
      const firstName = formData.get('firstName') as string
      const lastName = formData.get('lastName') as string
      const password = formData.get('password') as string

      const { error } = await signUp.ticket({
        firstName,
        lastName,
        password,
      })
      if (error) {
        // See https://clerk.com/docs/guides/development/custom-flows/error-handling
        console.error(JSON.stringify(error, null, 2))
        return
      }

      if (signUp.status === 'complete') {
        await signUp.finalize({
          navigate: ({ session, decorateUrl }) => {
            if (session?.currentTask) {
              // Handle pending session tasks
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
      } else {
        // Check why the sign-up is not complete
        console.error('Sign-up attempt not complete:', signUp)
      }
    }

    if (signUp.status === 'complete' || isSignedIn) {
      return null
    }

    return (
      <>
        <h1>Sign up</h1>
        <form action={handleSubmit}>
          <div>
            <label htmlFor="firstName">Enter first name</label>
            <input id="firstName" type="text" name="firstName" />
            {errors.fields.firstName && <p>{errors.fields.firstName.message}</p>}
          </div>
          <div>
            <label htmlFor="lastName">Enter last name</label>
            <input id="lastName" type="text" name="lastName" />
            {errors.fields.lastName && <p>{errors.fields.lastName.message}</p>}
          </div>
          <div>
            <label htmlFor="password">Enter password</label>
            <input id="password" type="password" name="password" />
            {errors.fields.password && <p>{errors.fields.password.message}</p>}
          </div>
          <div id="clerk-captcha" />
          <div>
            <button type="submit" disabled={fetchStatus === 'fetching'}>
              Next
            </button>
          </div>
        </form>
      </>
    )
  }
  ```


  ```tsx
// Filename: app/(auth)/accept-invitation.tsx

  import { ThemedText } from '@/components/themed-text'
  import { ThemedView } from '@/components/themed-view'
  import { Colors } from '@/constants/theme'
  import { useColorScheme } from '@/hooks/use-color-scheme'
  import { useAuth, useSignUp } from '@clerk/expo'
  import { type Href, useRouter } from 'expo-router'
  import React from 'react'
  import { Pressable, StyleSheet, TextInput, View } from 'react-native'

  export default function Page() {
    const { isSignedIn } = useAuth()
    const { signUp, errors, fetchStatus } = useSignUp()
    const router = useRouter()
    const colorScheme = useColorScheme() ?? 'light'
    const themeColors = Colors[colorScheme]

    const [firstName, setFirstName] = React.useState('')
    const [lastName, setLastName] = React.useState('')

    const handleSubmit = async () => {
      const { error } = await signUp.ticket({
        firstName,
        lastName,
      })
      if (error) {
        // See https://clerk.com/docs/guides/development/custom-flows/error-handling
        console.error(JSON.stringify(error, null, 2))
        return
      }

      if (signUp.status === 'complete') {
        await signUp.finalize({
          navigate: ({ session, decorateUrl }) => {
            if (session?.currentTask) {
              // Handle pending session tasks
              // See https://clerk.com/docs/guides/development/custom-flows/authentication/session-tasks
              console.log(session?.currentTask)
              return
            }

            const url = decorateUrl('/')
            if (url.startsWith('http')) {
              window.location.href = url
            } else {
              router.push(url as Href)
            }
          },
        })
      } else {
        // Check why the sign-up is not complete
        console.error('Sign-up attempt not complete:', signUp)
      }
    }

    if (signUp.status === 'complete' || isSignedIn) {
      return null
    }

    return (
      
        
          Sign up
        
        Enter first name
         setFirstName(firstName)}
        />
        {errors.fields.firstName && (
          {errors.fields.firstName.message}
        )}
        Enter last name
         setLastName(lastName)}
        />
        {errors.fields.lastName && (
          {errors.fields.lastName.message}
        )}

        {errors.fields.password && (
          {errors.fields.password.message}
        )}
         [
            styles.button,
            fetchStatus === 'fetching' && styles.buttonDisabled,
            pressed && styles.buttonPressed,
          ]}
          onPress={handleSubmit}
          disabled={fetchStatus === 'fetching'}
        >
          Next
        
      
    )
  }

  const styles = StyleSheet.create({
    container: {
      flex: 1,
      padding: 20,
      gap: 12,
    },
    title: {
      marginBottom: 8,
    },
    label: {
      fontWeight: '600',
      fontSize: 14,
    },
    input: {
      borderWidth: 1,
      borderRadius: 8,
      padding: 12,
      fontSize: 16,
    },
    button: {
      backgroundColor: '#0a7ea4',
      paddingVertical: 12,
      paddingHorizontal: 24,
      borderRadius: 8,
      alignItems: 'center',
      marginTop: 8,
    },
    buttonPressed: {
      opacity: 0.7,
    },
    buttonDisabled: {
      opacity: 0.5,
    },
    buttonText: {
      color: '#fff',
      fontWeight: '600',
    },
    error: {
      color: '#d32f2f',
      fontSize: 12,
      marginTop: -8,
    },
  })
  ```


  To create a sign-up flow using that invitation token, you need to call the [`signUpWithTicket()`](/ios/reference/native-mobile/auth#sign-up-with-ticket) method, as shown in the following example. The following example also demonstrates how to collect additional user information for the sign-up; you can either remove these fields or adjust them to fit your application.

  ```swift
// Filename: AcceptInvitationView.swift

  import SwiftUI
  import ClerkKit

  struct AcceptInvitationView: View {
    @Environment(Clerk.self) private var clerk
    @State private var ticket = ""
    @State private var firstName = ""
    @State private var lastName = ""
    @State private var password = ""

    var body: some View {
      VStack {
        TextField("Enter invitation ticket", text: $ticket)
        TextField("Enter first name", text: $firstName)
        TextField("Enter last name", text: $lastName)
        SecureField("Enter password", text: $password)
        Button("Accept invitation") {
          Task {
            await acceptInvitation(
              ticket: ticket,
              firstName: firstName,
              lastName: lastName,
              password: password
            )
          }
        }
      }
    }
  }

  extension AcceptInvitationView {

    func acceptInvitation(
      ticket: String,
      firstName: String,
      lastName: String,
      password: String
    ) async {
      do {
        // Start sign-up with the invitation ticket.
        var signUp = try await clerk.auth.signUpWithTicket(ticket)

        // Collect any additional required fields.
        signUp = try await signUp.update(
          firstName: firstName,
          lastName: lastName,
          password: password
        )

        if signUp.status == .complete {
          dump(clerk.session)
        } else {
          dump(signUp.status)
        }
      } catch {
        // See https://clerk.com/docs/guides/development/custom-flows/error-handling
        // for more info on error handling
        dump(error)
      }
    }
  }
  ```


  To create a sign-up flow using that invitation token, you need to call the [`signUpWithTicket()`](/android/reference/native-mobile/auth#sign-up-with-ticket) method, as shown in the following example. The following example also demonstrates how to collect additional user information for the sign-up; you can either remove these fields or adjust them to fit your application.

  ```kotlin
  import com.clerk.api.Clerk
  import com.clerk.api.auth.signUpWithTicket
  import com.clerk.api.network.serialization.flatMap
  import com.clerk.api.network.serialization.onFailure
  import com.clerk.api.network.serialization.onSuccess
  import com.clerk.api.signup.SignUp
  import com.clerk.api.signup.update

  suspend fun acceptInvitation(
    ticket: String,
    firstName: String,
    lastName: String,
    password: String,
  ) {
    Clerk.auth
      .signUpWithTicket(ticket)
      .flatMap { signUp ->
        signUp.update(
          SignUp.SignUpUpdateParams.Standard(
            firstName = firstName,
            lastName = lastName,
            password = password,
          )
        )
      }
      .onSuccess { signUp ->
        if (signUp.status == SignUp.Status.COMPLETE && signUp.createdSessionId != null) {
          Clerk.auth
            .setActive(sessionId = signUp.createdSessionId)
            .onFailure {
              // See https://clerk.com/docs/guides/development/custom-flows/error-handling
              // for more info on error handling
            }
        }
      }
      .onFailure {
        // See https://clerk.com/docs/guides/development/custom-flows/error-handling
        // for more info on error handling
      }
  }
  ```
