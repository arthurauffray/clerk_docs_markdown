# Build a custom flow for adding an email to a user's account


> Learn how to use the Clerk API to build a custom flow for adding an email to a user's account.

> [!WARNING]
> This guide is for users who want to build a custom flow. To use a _prebuilt_ UI, use the [Account Portal pages](/guides/account-portal/overview) or [prebuilt components](/reference/components/overview).


Users are able to add multiple email addresses to their account. Adding an email address requires the user to verify the email address before it can be added to the user's account.

This guide demonstrates how to build a custom user interface that allows users to add and verify an email address for their account.

## Configure email verification

There are two verification methods available for email addresses:

- **Email verification code**: Users receive an email with an OTP to verify their email address.
- **Email verification link**: Users receive an email with a **link** to verify their email address.

By default, the verification method that is enabled is **email verification code**. To use email code verification, skip to the [Email code verification](#email-code-verification) section.

To use email links, you must configure the following settings in the Clerk Dashboard:

1. On the [**User & authentication**](https://dashboard.clerk.com/~/user-authentication/user-and-authentication) page of the Clerk Dashboard, in the **Email** tab, under the **Sign-in with email** section, enable the **Email verification link** option. By default, **Require the same device and browser** is enabled, which means that email links are required to be verified from the same device and browser on which the sign-up or sign-in was initiated. For this guide, leave this setting enabled.
1. Disable **Email verification code**.
1. Save your changes.

Then skip to the [Email link verification](#email-link-verification) section.

## Email code verification


  1. Every user has a [`User`](/reference/javascript/user) object that represents their account. The `User` object has a `emailAddresses` property that contains all the email addresses associated with the user. The [`useUser()`](/reference/hooks/use-user) hook is used to get the `User` object.
  1. The [`User.createEmailAddress()`](/reference/javascript/user#create-email-address) method is passed to the [`useReverification()`](/reference/hooks/use-reverification) hook to require the user to reverify their credentials before being able to add an email address to their account.
  1. If the `createEmailAddress()` function is successful, a new [`EmailAddress`](/reference/javascript/types/email-address) object is created and stored in `User.emailAddresses`.
  1. The `prepareVerification()` method is used on the newly created `EmailAddress` object to send a verification code to the user.
  1. The `attemptVerification()` method is used on the same `EmailAddress` object with the verification code provided by the user to verify the email address.

  
    
      > [!TIP]
> Examples for this SDK aren't available yet. For now, try adapting the  available example to fit your SDK.

    

    ```tsx
// Filename: app/account/add-email/page.tsx

    'use client'

    import { useReverification, useUser } from '@clerk/nextjs'
    import { EmailAddressResource } from '@clerk/shared/types'
    import * as React from 'react'

    export default function Page() {
      const { isLoaded, isSignedIn, user } = useUser()

      const [email, setEmail] = React.useState('')
      const [code, setCode] = React.useState('')
      const [isVerifying, setIsVerifying] = React.useState(false)
      const [successful, setSuccessful] = React.useState(false)
      const [emailObj, setEmailObj] = React.useState()
      const createEmailAddress = useReverification((email: string) =>
        user?.createEmailAddress({ email }),
      )

      // Handle loading state
      if (!isLoaded) return <p>Loading...</p>

      // Handle signed-out state
      if (!isSignedIn) return <p>You must be signed in to access this page</p>

      // Handle addition of the email address
      const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault()

        try {
          // Add an unverified email address to user
          const res = await createEmailAddress(email)
          // Reload user to get updated User object
          await user.reload()

          // Find the email address that was just added
          const emailAddress = user.emailAddresses.find((a) => a.id === res?.id)
          // Create a reference to the email address that was just added
          setEmailObj(emailAddress)

          // Send the user an email with the verification code
          emailAddress?.prepareVerification({ strategy: 'email_code' })

          // Set to true to display second form
          // and capture the code
          setIsVerifying(true)
        } catch (err) {
          // See https://clerk.com/docs/guides/development/custom-flows/error-handling
          // for more info on error handling
          console.error(JSON.stringify(err, null, 2))
        }
      }

      // Handle the submission of the verification form
      const verifyCode = async (e: React.FormEvent) => {
        e.preventDefault()
        try {
          // Verify that the code entered matches the code sent to the user
          const emailVerifyAttempt = await emailObj?.attemptVerification({ code })

          if (emailVerifyAttempt?.verification.status === 'verified') {
            setSuccessful(true)
          } else {
            // If the status is not complete, check why. User may need to
            // complete further steps.
            console.error(JSON.stringify(emailVerifyAttempt, null, 2))
          }
        } catch (err) {
          console.error(JSON.stringify(err, null, 2))
        }
      }

      // Display a success message if the email was added successfully
      if (successful) {
        return <h1>Email added!</h1>
      }

      // Display the verification form to capture the code
      if (isVerifying) {
        return (
          <>
            <h1>Verify email</h1>
            <div>
              <form onSubmit={(e) => verifyCode(e)}>
                <div>
                  <label htmlFor="code">Enter code</label>
                  <input
                    onChange={(e) => setCode(e.target.value)}
                    id="code"
                    name="code"
                    type="text"
                    value={code}
                  />
                </div>
                <div>
                  <button type="submit">Verify</button>
                </div>
              </form>
            </div>
          </>
        )
      }

      // Display the initial form to capture the email address
      return (
        <>
          <h1>Add Email</h1>
          <div>
            <form onSubmit={(e) => handleSubmit(e)}>
              <div>
                <label htmlFor="email">Enter email address</label>
                <input
                  onChange={(e) => setEmail(e.target.value)}
                  id="email"
                  name="email"
                  type="email"
                  value={email}
                />
              </div>
              <div>
                <button type="submit">Continue</button>
              </div>
            </form>
          </div>
        </>
      )
    }
    ```
  

  
    ```tsx
// Filename: app/(account)/add-email/page.tsx

    import { ThemedText } from '@/components/themed-text'
    import { ThemedView } from '@/components/themed-view'
    import { useUser } from '@clerk/expo'
    import { EmailAddressResource } from '@clerk/shared/types'
    import { Redirect } from 'expo-router'
    import * as React from 'react'
    import { Pressable, StyleSheet, TextInput } from 'react-native'

    export default function Page() {
      const { isLoaded, isSignedIn, user } = useUser()

      const [email, setEmail] = React.useState('')
      const [code, setCode] = React.useState('')
      const [isVerifying, setIsVerifying] = React.useState(false)
      const [successful, setSuccessful] = React.useState(false)
      const [emailObj, setEmailObj] = React.useState()

      // Handle loading state
      if (!isLoaded) {
        return (
          
            Loading...
          
        )
      }

      // Handle signed-out state
      if (!isSignedIn) return // Handle addition of the email address
      const handleSubmit = async () => {
        try {
          // Add an unverified email address to user
          const res = await user?.createEmailAddress({ email })
          // Reload user to get updated User object
          await user?.reload()

          // Find the email address that was just added
          const emailAddress = user?.emailAddresses.find((a) => a.id === res?.id)
          // Create a reference to the email address that was just added
          setEmailObj(emailAddress)

          // Send the user an email with the verification code
          await emailAddress?.prepareVerification({ strategy: 'email_code' })

          // Set to true to display second form
          // and capture the code
          setIsVerifying(true)
        } catch (err) {
          // See https://clerk.com/docs/guides/development/custom-flows/error-handling
          // for more info on error handling
          console.error(JSON.stringify(err, null, 2))
        }
      }

      // Handle the submission of the verification form
      const verifyCode = async () => {
        try {
          // Verify that the code entered matches the code sent to the user
          const emailVerifyAttempt = await emailObj?.attemptVerification({ code })

          if (emailVerifyAttempt?.verification.status === 'verified') {
            setSuccessful(true)
          } else {
            // If the status is not complete, check why. User may need to
            // complete further steps.
            console.error(JSON.stringify(emailVerifyAttempt, null, 2))
          }
        } catch (err) {
          console.error(JSON.stringify(err, null, 2))
        }
      }

      // Display a success message if the email was added successfully
      if (successful) {
        return (
          
            
              Email added!
            
          
        )
      }

      // Display the verification form to capture the code
      if (isVerifying) {
        return (
          
            
              Verify email
            
            Enter code
             [
                styles.button,
                !code && styles.buttonDisabled,
                pressed && styles.buttonPressed,
              ]}
              onPress={verifyCode}
              disabled={!code}
            >
              Verify
            
          
        )
      }

      // Display the initial form to capture the email address
      return (
        
          
            Add Email
          
          Enter email address
           [
              styles.button,
              !email && styles.buttonDisabled,
              pressed && styles.buttonPressed,
            ]}
            onPress={handleSubmit}
            disabled={!email}
          >
            Continue
          
        
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
        borderColor: '#ccc',
        borderRadius: 8,
        padding: 12,
        fontSize: 16,
        backgroundColor: '#fff',
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
    })
    ```
  


  ```swift
// Filename: AddEmailView.swift

    import SwiftUI
    import ClerkKit

    struct AddEmailView: View {
      @State private var email = ""
      @State private var code = ""
      @State private var isVerifying = false
      @State private var newEmailAddress: EmailAddress?

      var body: some View {
        if newEmailAddress?.verification?.status == .verified {
          Text("Email added!")
        }

        if isVerifying {
          TextField("Enter code", text: $code)
          Button("Verify") {
            Task { await verifyCode(code) }
          }
        } else {
          TextField("Enter email address", text: $email)
          Button("Continue") {
            Task { await createEmail(email) }
          }
        }
      }
    }

    extension AddEmailView {

      func createEmail(_ email: String) async {
        do {
          guard let user = Clerk.shared.user else { return }

          // Create the email address
          let emailAddress = try await user.createEmailAddress(email)

          // Send the user an email with the verification code
          self.newEmailAddress = try await emailAddress.sendCode()

          isVerifying = true
        } catch {
          // See https://clerk.com/docs/guides/development/custom-flows/error-handling
          // for more info on error handling
          dump(error)
        }
      }

      func verifyCode(_ code: String) async {
        do {
          guard let newEmailAddress else { return }

          // Verify that the provided code matches the code sent to the user
          self.newEmailAddress = try await newEmailAddress.verifyCode(code)

          dump(self.newEmailAddress?.verification?.status)
        } catch {
          // See https://clerk.com/docs/guides/development/custom-flows/error-handling
          // for more info on error handling
          dump(error)
        }
      }
    }
  ```


  
**AddEmailViewModel.kt:**

```kotlin
// Filename: AddEmailViewModel.kt

    package com.clerk.customflows.addemail

    import android.util.Log
    import androidx.lifecycle.ViewModel
    import androidx.lifecycle.viewModelScope
    import com.clerk.api.Clerk
    import com.clerk.api.emailaddress.EmailAddress
    import com.clerk.api.emailaddress.attemptVerification
    import com.clerk.api.emailaddress.prepareVerification
    import com.clerk.api.network.serialization.errorMessage
    import com.clerk.api.network.serialization.flatMap
    import com.clerk.api.network.serialization.onFailure
    import com.clerk.api.network.serialization.onSuccess
    import com.clerk.api.user.createEmailAddress
    import kotlinx.coroutines.flow.MutableStateFlow
    import kotlinx.coroutines.flow.asStateFlow
    import kotlinx.coroutines.flow.combine
    import kotlinx.coroutines.flow.launchIn
    import kotlinx.coroutines.launch

    class AddEmailViewModel : ViewModel() {
    private val _uiState = MutableStateFlow(UiState.NeedsVerification)
    val uiState = _uiState.asStateFlow()

    init {
      combine(Clerk.isInitialized, Clerk.userFlow) { isInitialized, user ->
          _uiState.value =
            when {
              !isInitialized -> UiState.Loading
              user == null -> UiState.SignedOut
              else -> UiState.NeedsVerification
            }
        }
        .launchIn(viewModelScope)
    }

    fun createEmailAddress(emailAddress: String) {
      val user = requireNotNull(Clerk.userFlow.value)

      // Add an unverified email address to the user,
      // then send the user an email with the verification code
      viewModelScope.launch {
        user
          .createEmailAddress(emailAddress)
          .flatMap { it.prepareVerification(EmailAddress.PrepareVerificationParams.EmailCode()) }
          .onSuccess {
            // Update the state to show that the email address has been created
            // and that the user needs to verify the email address
            _uiState.value = UiState.Verifying(it)
          }
          .onFailure {
            Log.e(
              "AddEmailViewModel",
              "Failed to create email address and prepare verification: ${it.errorMessage}",
            )
          }
      }
    }

    fun verifyCode(code: String, newEmailAddress: EmailAddress) {
      viewModelScope.launch {
        newEmailAddress
          .attemptVerification(code)
          .onSuccess {
            // Update the state to show that the email addresshas been verified
            _uiState.value = UiState.Verified
          }
          .onFailure {
            Log.e("AddEmailViewModel", "Failed to verify email address: ${it.errorMessage}")
          }
      }
    }

    sealed interface UiState {
      data object Loading : UiState

      data object NeedsVerification : UiState

      data class Verifying(val emailAddress: EmailAddress) : UiState

      data object Verified : UiState

      data object SignedOut : UiState
    }
    }
    ```


**AddEmailActivity.kt:**

```kotlin
// Filename: AddEmailActivity.kt

    package com.clerk.customflows.addemail

    import android.os.Bundle
    import androidx.activity.ComponentActivity
    import androidx.activity.compose.setContent
    import androidx.activity.viewModels
    import androidx.compose.foundation.layout.Box
    import androidx.compose.foundation.layout.Column
    import androidx.compose.foundation.layout.fillMaxSize
    import androidx.compose.foundation.layout.padding
    import androidx.compose.material3.Button
    import androidx.compose.material3.CircularProgressIndicator
    import androidx.compose.material3.Text
    import androidx.compose.material3.TextField
    import androidx.compose.runtime.Composable
    import androidx.compose.runtime.getValue
    import androidx.compose.runtime.mutableStateOf
    import androidx.compose.runtime.remember
    import androidx.compose.runtime.setValue
    import androidx.compose.ui.Alignment
    import androidx.compose.ui.Modifier
    import androidx.compose.ui.unit.dp
    import androidx.lifecycle.compose.collectAsStateWithLifecycle
    import com.clerk.api.emailaddress.EmailAddress

    class AddEmailActivity : ComponentActivity() {
    val viewModel: AddEmailViewModel by viewModels()

    override fun onCreate(savedInstanceState: Bundle?) {
      super.onCreate(savedInstanceState)
      setContent {
        val state by viewModel.uiState.collectAsStateWithLifecycle()
        AddEmailView(
          state = state,
          onCreateEmailAddress = viewModel::createEmailAddress,
          onVerifyCode = viewModel::verifyCode,
        )
      }
    }
    }

    @Composable
    fun AddEmailView(
    state: AddEmailViewModel.UiState,
    onCreateEmailAddress: (String) -> Unit,
    onVerifyCode: (String, EmailAddress) -> Unit,
    ) {
    Box(modifier = Modifier.fillMaxSize(), contentAlignment = Alignment.Center) {
      when (state) {
        AddEmailViewModel.UiState.NeedsVerification -> {
          InputContentView(buttonText = "Continue", placeholder = "Enter email address") {
            onCreateEmailAddress(it)
          }
        }

        AddEmailViewModel.UiState.Verified -> Text("Verified!")

        is AddEmailViewModel.UiState.Verifying -> {
          InputContentView(buttonText = "Verify", placeholder = "Enter code") {
            onVerifyCode(it, state.emailAddress)
          }
        }

        AddEmailViewModel.UiState.Loading -> CircularProgressIndicator()
        AddEmailViewModel.UiState.SignedOut -> Text("You must be signed in to add an email address.")
      }
    }
    }

    @Composable
    fun InputContentView(
    buttonText: String,
    placeholder: String,
    modifier: Modifier = Modifier,
    onClick: (String) -> Unit,
    ) {
    var input by remember { mutableStateOf("") }
    Column(horizontalAlignment = Alignment.CenterHorizontally, modifier = modifier) {
      TextField(
        modifier = Modifier.padding(bottom = 16.dp),
        value = input,
        onValueChange = { input = it },
        placeholder = { Text(placeholder) },
      )
      Button(onClick = { onClick(input) }) { Text(buttonText) }
    }
    }
    ```


## Email link verification


  > [!WARNING]
  > This SDK doesn't currently support email link verification flows. Use [email code verification](/guides/development/custom-flows/authentication/email-sms-otp) instead.


  


  > [!TIP]
> Examples for this SDK aren't available yet. For now, try adapting the  available example to fit your SDK.


1. Every user has a [`User`](/reference/javascript/user) object that represents their account. The `User` object has a `emailAddresses` property that contains all the email addresses associated with the user. Use the [`useUser()`](/reference/hooks/use-user) hook to access the `User` object.
1. Pass the [`User.createEmailAddress()`](/reference/javascript/user#create-email-address) method to the [`useReverification()`](/reference/hooks/use-reverification) hook to require the user to [reverify their credentials](/guides/secure/reverification) before being able to add an email address to their account.
1. If the `createEmailAddress()` function is successful, a new [`EmailAddress`](/reference/javascript/types/email-address) object is created and stored in `User.emailAddresses`. Use the newly created `EmailAddress` object to access the [`createEmailLinkFlow()`](/reference/javascript/types/email-address#create-email-link-flow) method.
1. Use the `createEmailLinkFlow()` method to access the [`startEmailLinkFlow()`](/reference/javascript/types/email-address#create-email-link-flow) method. Call the `startEmailLinkFlow()` method to send an email with a verification link to the user. This method requires specifying a `redirectUrl`, which is the URL that the user will be redirected to after visiting the link in their email.
1. On your verification page (the URL you set as the `redirectUrl` parameter), call the [`useClerk()`](/reference/hooks/use-clerk) hook to access the [`handleEmailLinkVerification()`](/reference/javascript/clerk#handle-email-link-verification) method.
1. Call the `handleEmailLinkVerification()` method to verify the email address.


**Add email page:**

```tsx
// Filename: app/account/add-email/page.tsx

  'use client'

  import * as React from 'react'
  import { useUser, useReverification } from '@clerk/nextjs'

  export default function Page() {
    const { isLoaded, isSignedIn, user } = useUser()
    const createEmailAddress = useReverification((email: string) =>
      user?.createEmailAddress({ email }),
    )

    const [email, setEmail] = React.useState('')
    const [verifying, setVerifying] = React.useState(false)
    const [error, setError] = React.useState('')

    // Handle loading state
    if (!isLoaded) <p>Loading...</p>

    // Handle signed-out state
    if (!isSignedIn) <p>You must be signed in to access this page</p>

    const handleSubmit = async (e: React.FormEvent) => {
      e.preventDefault()

      try {
        setVerifying(true)

        // Add an unverified email address to user
        const res = await createEmailAddress(email)
        // Reload user to get updated User object
        await user?.reload()

        // Find the email address that was just added
        const emailAddress = user?.emailAddresses.find((a) => a.id === res?.id)

        if (!emailAddress) {
          setError('Email address not found')
          return
        }

        const { startEmailLinkFlow } = emailAddress.createEmailLinkFlow()

        // Dynamically set the host domain for dev and prod
        // You could instead use an environment variable or other source for the host domain
        const protocol = window.location.protocol
        const host = window.location.host

        // Send the user an email with the verification link
        startEmailLinkFlow({ redirectUrl: `${protocol}//${host}/account/add-email/verify` })
      } catch (err) {
        // See https://clerk.com/docs/guides/development/custom-flows/error-handling
        // for more info on error handling
        console.error(JSON.stringify(err, null, 2))
        setError('An error occurred.')
      }
    }

    async function reset(e: React.FormEvent) {
      e.preventDefault()
      setVerifying(false)
    }

    if (error) {
      return (
        <div>
          <p>Error: {error}</p>
          <button onClick={() => setError('')}>Try again</button>
        </div>
      )
    }

    if (verifying) {
      return (
        <div>
          <p>Check your email and visit the link that was sent to you.</p>
          <form onSubmit={reset}>
            <button type="submit">Restart</button>
          </form>
        </div>
      )
    }

    // Display the initial form to capture the email address
    return (
      <>
        <h1>Add email</h1>
        <div>
          <form onSubmit={(e) => handleSubmit(e)}>
            <label htmlFor="email">Enter email address</label>
            <input
              id="email"
              name="email"
              type="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
            />
            <button type="submit">Continue</button>
          </form>
        </div>
      </>
    )
  }
  ```


**Verify page:**

```tsx
// Filename: app/account/add-email/verify/page.tsx

  'use client'

  import * as React from 'react'
  import { useClerk } from '@clerk/nextjs'
  import { EmailLinkErrorCodeStatus, isEmailLinkError } from '@clerk/nextjs/errors'
  import Link from 'next/link'

  export type VerificationStatus =
    | 'expired'
    | 'failed'
    | 'loading'
    | 'verified'
    | 'verified_switch_tab'
    | 'client_mismatch'

  export default function VerifyEmailLink() {
    const [verificationStatus, setVerificationStatus] = React.useState('loading')

    const { handleEmailLinkVerification, loaded } = useClerk()

    async function verify() {
      try {
        await handleEmailLinkVerification({})
        setVerificationStatus('verified')
      } catch (err: any) {
        let status: VerificationStatus = 'failed'

        if (isEmailLinkError(err)) {
          // If link expired, set status to expired
          if (err.code === EmailLinkErrorCodeStatus.Expired) {
            status = 'expired'
          } else if (err.code === EmailLinkErrorCodeStatus.ClientMismatch) {
            // OPTIONAL: This check is only required if you have
            // the 'Require the same device and browser' setting
            // enabled in the Clerk Dashboard
            status = 'client_mismatch'
          }
        }

        setVerificationStatus(status)
        return
      }
    }

    React.useEffect(() => {
      if (!loaded) return

      verify()
    }, [handleEmailLinkVerification, loaded])

    if (verificationStatus === 'loading') {
      return <div>Loading...</div>
    }

    if (verificationStatus === 'failed') {
      return (
        <div>
          <h1>Verify your email</h1>
          <p>The email link verification failed.</p>
          Return to add email
        </div>
      )
    }

    if (verificationStatus === 'expired') {
      return (
        <div>
          <h1>Verify your email</h1>
          <p>The email link has expired.</p>
          Return to add email
        </div>
      )
    }

    // OPTIONAL: This check is only required if you have
    // the 'Require the same device and browser' setting
    // enabled in the Clerk Dashboard
    if (verificationStatus === 'client_mismatch') {
      return (
        <div>
          <h1>Verify your email</h1>
          <p>
            You must complete the email link verification on the same device and browser as you
            started it on.
          </p>
          Return to add email
        </div>
      )
    }

    return (
      <div>
        <h1>Verify your email</h1>
        <p>Successfully added email!</p>
      </div>
    )
  }
  ```
