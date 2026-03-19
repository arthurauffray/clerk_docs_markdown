# Build a custom email/password authentication flow


> Learn how to build a custom email/password sign-up and sign-in flow using the Clerk API.

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
  > If you're using an older version of one of these SDKs, or are using the legacy API, refer to the [legacy API documentation](/guides/development/custom-flows/authentication/legacy/email-password).


This guide demonstrates how to build a custom user interface for signing up and signing in using email and password.


  ## Enable email and password authentication

  To follow this guide, you first need to ensure email and password are enabled for your application.

  1. In the Clerk Dashboard, navigate to the [**User & authentication**](https://dashboard.clerk.com/~/user-authentication/user-and-authentication) page.
1. Enable **Sign-up with email**.
   - **Require email address** should be enabled.
   - For **Verify at sign-up**, **Email verification code** is enabled by default, and is used for this guide. If you'd like to use **Email verification link** instead, see the [dedicated custom flow](/guides/development/custom-flows/authentication/email-links).
1. Enable **Sign in with email**.
   - This guide supports password authentication. If you'd like to build a custom flow that allows users to sign in passwordlessly, see the [email code custom flow](/guides/development/custom-flows/authentication/email-sms-otp) or the [email links custom flow](/guides/development/custom-flows/authentication/email-links).
1. Select the **Password** tab and enable **Sign-up with password**.
   - [**Client Trust**](/guides/secure/client-trust) is enabled by default. The sign-in example supports it using email verification codes because it's the default second factor strategy.


  ## Sign-up flow

  
    
      > [!TIP]
> Examples for this SDK aren't available yet. For now, try adapting the  available example to fit your SDK.

    

    First, understand that the `useSignUp()` hook returns an object with the following properties:

- `signUp`: The [`SignUpFuture`](/reference/javascript/sign-up-future) object. Use this to initiate the sign-up process and check the current state of the sign-up attempt.
- `errors`: The [`Errors`](/reference/javascript/types/errors) object that contains the errors that occurred during the last API request. You can use this to display errors to the user in your custom UI.
- `fetchStatus`: The fetch status of the underlying [`SignUpFuture`](/reference/javascript/sign-up-future) resource. You can use this to display a loading state or disable buttons while the request is in progress.


    Then, to sign up a user using their email and password, and verify their sign-up with an email verification code, you must:

    1. Initiate the sign-up process by collecting the user's email address and password with the [`signUp.password()`](/reference/javascript/sign-up-future#password) method.
    1. Send a one-time code to the provided email address with the [`signUp.verifications.sendEmailCode()`](/reference/javascript/sign-up-future#verifications-send-email-code) method.
    1. Collect the user's one-time code and verify it with the [`signUp.verifications.verifyEmailCode()`](/reference/javascript/sign-up-future#verifications-verify-email-code) method.
    1. If the email address verification is successful, the `signUp.status` will be `complete`, and you can finish the sign-up flow with the [`signUp.finalize()`](/reference/javascript/sign-up-future#finalize) method to set the newly created session as the active session.

    
      ```tsx
// Filename: app/sign-up/page.tsx

      'use client'

      import { useAuth, useSignUp } from '@clerk/nextjs'
      import { useRouter } from 'next/navigation'

      export default function Page() {
        const { signUp, errors, fetchStatus } = useSignUp()
        const { isSignedIn } = useAuth()
        const router = useRouter()

        const handleSubmit = async (formData: FormData) => {
          const emailAddress = formData.get('email') as string
          const password = formData.get('password') as string

          const { error } = await signUp.password({
            emailAddress,
            password,
          })
          if (error) {
            // See https://clerk.com/docs/guides/development/custom-flows/error-handling
            // for more info on error handling
            console.error(JSON.stringify(error, null, 2))
            return
          }

          if (!error) await signUp.verifications.sendEmailCode()
        }

        const handleVerify = async (formData: FormData) => {
          const code = formData.get('code') as string

          await signUp.verifications.verifyEmailCode({
            code,
          })
          if (signUp.status === 'complete') {
            await signUp.finalize({
              // Redirect the user to the home page after signing up
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

        if (
          signUp.status === 'missing_requirements' &&
          signUp.unverifiedFields.includes('email_address') &&
          signUp.missingFields.length === 0
        ) {
          return (
            <>
              <h1>Verify your account</h1>
              <form action={handleVerify}>
                <div>
                  <label htmlFor="code">Code</label>
                  <input id="code" name="code" type="text" />
                </div>
                {errors.fields.code && <p>{errors.fields.code.message}</p>}
                <button type="submit" disabled={fetchStatus === 'fetching'}>
                  Verify
                </button>
              </form>
              <button onClick={() => signUp.verifications.sendEmailCode()}>I need a new code</button>
            </>
          )
        }

        return (
          <>
            <h1>Sign up</h1>
            <form action={handleSubmit}>
              <div>
                <label htmlFor="email">Enter email address</label>
                <input id="email" type="email" name="email" />
                {errors.fields.emailAddress && <p>{errors.fields.emailAddress.message}</p>}
              </div>
              <div>
                <label htmlFor="password">Enter password</label>
                <input id="password" type="password" name="password" />
                {errors.fields.password && <p>{errors.fields.password.message}</p>}
              </div>
              <button type="submit" disabled={fetchStatus === 'fetching'}>
                Continue
              </button>
            </form>
            
            {errors && <p>{JSON.stringify(errors, null, 2)}</p>}

            
            <div id="clerk-captcha" />
          </>
        )
      }
      ```
    

    
      In the `(auth)` group, create a `sign-up.tsx` file with the following code. The [`useSignUp()`](/reference/hooks/use-sign-up) hook is used to create a sign-up flow. The user can sign up using their email and password and will receive an email verification code to confirm their email.

```tsx
// Filename: app/(auth)/sign-up.tsx

import { ThemedText } from '@/components/themed-text'
import { ThemedView } from '@/components/themed-view'
import { useAuth, useSignUp } from '@clerk/expo'
import { type Href, Link, useRouter } from 'expo-router'
import React from 'react'
import { Pressable, StyleSheet, TextInput, View } from 'react-native'

export default function Page() {
  const { signUp, errors, fetchStatus } = useSignUp()
  const { isSignedIn } = useAuth()
  const router = useRouter()

  const [emailAddress, setEmailAddress] = React.useState('')
  const [password, setPassword] = React.useState('')
  const [code, setCode] = React.useState('')

  const handleSubmit = async () => {
    const { error } = await signUp.password({
      emailAddress,
      password,
    })
    if (error) {
      console.error(JSON.stringify(error, null, 2))
      return
    }

    if (!error) await signUp.verifications.sendEmailCode()
  }

  const handleVerify = async () => {
    await signUp.verifications.verifyEmailCode({
      code,
    })
    if (signUp.status === 'complete') {
      await signUp.finalize({
        // Redirect the user to the home page after signing up
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

  if (
    signUp.status === 'missing_requirements' &&
    signUp.unverifiedFields.includes('email_address') &&
    signUp.missingFields.length === 0
  ) {
    return (
      
        
          Verify your account
        
         setCode(code)}
          keyboardType="numeric"
        />
        {errors.fields.code && (
          {errors.fields.code.message}
        )}
         [
            styles.button,
            fetchStatus === 'fetching' && styles.buttonDisabled,
            pressed && styles.buttonPressed,
          ]}
          onPress={handleVerify}
          disabled={fetchStatus === 'fetching'}
        >
          Verify
        
         [styles.secondaryButton, pressed && styles.buttonPressed]}
          onPress={() => signUp.verifications.sendEmailCode()}
        >
          I need a new code
        
      
    )
  }

  return (
    
      
        Sign up
      

      Email address
       setEmailAddress(emailAddress)}
        keyboardType="email-address"
      />
      {errors.fields.emailAddress && (
        {errors.fields.emailAddress.message}
      )}
      Password
       setPassword(password)}
      />
      {errors.fields.password && (
        {errors.fields.password.message}
      )}
       [
          styles.button,
          (!emailAddress || !password || fetchStatus === 'fetching') && styles.buttonDisabled,
          pressed && styles.buttonPressed,
        ]}
        onPress={handleSubmit}
        disabled={!emailAddress || !password || fetchStatus === 'fetching'}
      >
        Sign up
      
      
      {errors && {JSON.stringify(errors, null, 2)}}

      
        Already have an account? 
        
          Sign in
        
      

      
      
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
  secondaryButton: {
    paddingVertical: 12,
    paddingHorizontal: 24,
    borderRadius: 8,
    alignItems: 'center',
    marginTop: 8,
  },
  secondaryButtonText: {
    color: '#0a7ea4',
    fontWeight: '600',
  },
  linkContainer: {
    flexDirection: 'row',
    gap: 4,
    marginTop: 12,
    alignItems: 'center',
  },
  error: {
    color: '#d32f2f',
    fontSize: 12,
    marginTop: -8,
  },
  debug: {
    fontSize: 10,
    opacity: 0.5,
    marginTop: 8,
  },
})
```

    
  

  
    ```swift
// Filename: EmailPasswordSignUpView.swift

      import SwiftUI
      import ClerkKit

      struct EmailPasswordSignUpView: View {
      @Environment(Clerk.self) private var clerk
      @State private var email = ""
      @State private var password = ""
      @State private var code = ""
      @State private var isVerifying = false

      var body: some View {
        if isVerifying {
          TextField("Enter your verification code", text: $code)
          Button("Verify") {
            Task { await verify(code: code) }
          }
        } else {
          TextField("Enter email address", text: $email)
          SecureField("Enter password", text: $password)
          Button("Next") {
            Task { await submit(email: email, password: password) }
          }
        }
      }
      }

      extension EmailPasswordSignUpView {

      func submit(email: String, password: String) async {
        do {
          // Start sign-up with email/password.
          var signUp = try await clerk.auth.signUp(
            emailAddress: email,
            password: password
          )

          // Send the email verification code.
          signUp = try await signUp.sendEmailCode()

          isVerifying = true
      } catch {
        // See https://clerk.com/docs/guides/development/custom-flows/error-handling
        // for more info on error handling.
        dump(error)
      }
      }

      func verify(code: String) async {
        do {
          // Verify the email code.
          guard var signUp = clerk.auth.currentSignUp else { return }

          signUp = try await signUp.verifyEmailCode(code)

          switch signUp.status {
          case .complete:
            dump(clerk.session)
          default:
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
  

  
    
**EmailPasswordSignUpViewModel.kt:**

```kotlin
// Filename: EmailPasswordSignUpViewModel.kt

      package com.clerk.customflows.emailpassword.signup

      import androidx.lifecycle.ViewModel
      import androidx.lifecycle.viewModelScope
      import com.clerk.api.Clerk
      import com.clerk.api.auth.types.VerificationType
      import com.clerk.api.network.serialization.flatMap
      import com.clerk.api.network.serialization.onFailure
      import com.clerk.api.network.serialization.onSuccess
      import com.clerk.api.signup.sendCode
      import com.clerk.api.signup.verifyCode
      import kotlinx.coroutines.flow.MutableStateFlow
      import kotlinx.coroutines.flow.asStateFlow
      import kotlinx.coroutines.flow.combine
      import kotlinx.coroutines.flow.launchIn
      import kotlinx.coroutines.launch

      class EmailPasswordSignUpViewModel : ViewModel() {
      private val _uiState =
      MutableStateFlow(EmailPasswordSignUpUiState.Loading)
      val uiState = _uiState.asStateFlow()

      init {
      combine(Clerk.userFlow, Clerk.isInitialized) { user, isInitialized ->
          _uiState.value =
            when {
              !isInitialized -> EmailPasswordSignUpUiState.Loading
              user != null -> EmailPasswordSignUpUiState.Verified
              else -> EmailPasswordSignUpUiState.Unverified
            }
        }
        .launchIn(viewModelScope)
      }

      fun submit(email: String, password: String) {
      viewModelScope.launch {
        Clerk.auth
          .signUp {
            this.email = email
            this.password = password
          }
          .flatMap { it.sendCode { this.email = email } }
          .onSuccess { _uiState.value = EmailPasswordSignUpUiState.Verifying }
          .onFailure {
            // See https://clerk.com/docs/guides/development/custom-flows/error-handling
            // for more info on error handling
          }
      }
      }

      fun verify(code: String) {
      val inProgressSignUp = Clerk.auth.currentSignUp ?: return
      viewModelScope.launch {
        inProgressSignUp
          .verifyCode(code, VerificationType.EMAIL)
          .onSuccess { _uiState.value = EmailPasswordSignUpUiState.Verified }
          .onFailure {
            // See https://clerk.com/docs/guides/development/custom-flows/error-handling
            // for more info on error handling
          }
      }
      }

      sealed interface EmailPasswordSignUpUiState {
      data object Loading : EmailPasswordSignUpUiState

      data object Unverified : EmailPasswordSignUpUiState

      data object Verifying : EmailPasswordSignUpUiState

      data object Verified : EmailPasswordSignUpUiState
      }
      }
      ```


**EmailPasswordSignUpActivity.kt:**

```kotlin
// Filename: EmailPasswordSignUpActivity.kt

      package com.clerk.customflows.emailpassword.signup

      import android.os.Bundle
      import androidx.activity.ComponentActivity
      import androidx.activity.compose.setContent
      import androidx.activity.viewModels
      import androidx.compose.foundation.layout.Arrangement
      import androidx.compose.foundation.layout.Box
      import androidx.compose.foundation.layout.Column
      import androidx.compose.foundation.layout.fillMaxSize
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
      import androidx.compose.ui.text.input.PasswordVisualTransformation
      import androidx.compose.ui.unit.dp
      import androidx.lifecycle.compose.collectAsStateWithLifecycle

      class EmailPasswordSignUpActivity : ComponentActivity() {

      val viewModel: EmailPasswordSignUpViewModel by viewModels()

      override fun onCreate(savedInstanceState: Bundle?) {
      super.onCreate(savedInstanceState)
      setContent {
        val state by viewModel.uiState.collectAsStateWithLifecycle()
        EmailPasswordSignInView(
          state = state,
          onSubmit = viewModel::submit,
          onVerify = viewModel::verify,
        )
      }
      }
      }

      @Composable
      fun EmailPasswordSignInView(
      state: EmailPasswordSignUpViewModel.EmailPasswordSignUpUiState,
      onSubmit: (String, String) -> Unit,
      onVerify: (String) -> Unit,
      ) {
      var email by remember { mutableStateOf("") }
      var password by remember { mutableStateOf("") }
      var code by remember { mutableStateOf("") }

      Box(modifier = Modifier.fillMaxSize(), contentAlignment = Alignment.Center) {
      when (state) {
        EmailPasswordSignUpViewModel.EmailPasswordSignUpUiState.Unverified -> {
          Column(
            verticalArrangement = Arrangement.spacedBy(16.dp, Alignment.CenterVertically),
            horizontalAlignment = Alignment.CenterHorizontally,
          ) {
            TextField(value = email, onValueChange = { email = it }, label = { Text("Email") })
            TextField(
              value = password,
              onValueChange = { password = it },
              visualTransformation = PasswordVisualTransformation(),
              label = { Text("Password") },
            )
            Button(onClick = { onSubmit(email, password) }) { Text("Next") }
          }
        }
        EmailPasswordSignUpViewModel.EmailPasswordSignUpUiState.Verified -> {
          Text("Verified!")
        }
        EmailPasswordSignUpViewModel.EmailPasswordSignUpUiState.Verifying -> {
          Column(
            verticalArrangement = Arrangement.spacedBy(16.dp, Alignment.CenterVertically),
            horizontalAlignment = Alignment.CenterHorizontally,
          ) {
            TextField(
              value = code,
              onValueChange = { code = it },
              label = { Text("Enter your verification code") },
            )
            Button(onClick = { onVerify(code) }) { Text("Verify") }
          }
        }
        EmailPasswordSignUpViewModel.EmailPasswordSignUpUiState.Loading -> CircularProgressIndicator()
      }
      }
      }
      ```

  

  ## Sign-in flow

  
    
      > [!TIP]
> Examples for this SDK aren't available yet. For now, try adapting the  available example to fit your SDK.

    

    First, understand that the `useSignIn()` hook returns an object with the following properties:

- `signIn`: The [`SignInFuture`](/reference/javascript/sign-in-future) object. Use this to initiate the sign-in process and check the current state of the sign-in attempt.
- `errors`: The [`Errors`](/reference/javascript/types/errors) object that contains the errors that occurred during the last API request. You can use this to display errors to the user in your custom UI.
- `fetchStatus`: The fetch status of the underlying [`SignInFuture`](/reference/javascript/sign-in-future) resource. You can use this to display a loading state or disable buttons while the request is in progress.


    Then, to sign in a user using their email and password, you must:

    1. Initiate the sign-in process by collecting the user's email address and password with the [`signIn.password()`](/reference/javascript/sign-in-future#password) method.
    1. If the `signIn.status` is `'needs_second_factor'`, the user has MFA enabled. See the [MFA custom flow guide](/guides/development/custom-flows/authentication/multi-factor-authentication) for how to handle this status. If the status is `'needs_client_trust'`, see the [Client Trust custom flow guide](/guides/development/custom-flows/authentication/client-trust).
    1. If the `signIn.status` is `'complete'`, finish the sign-in flow with the [`signIn.finalize()`](/reference/javascript/sign-in-future#finalize) method to set the newly created session as the active session.

    
      ```tsx
// Filename: app/sign-in/page.tsx

'use client'

import { useSignIn } from '@clerk/nextjs'
import { useRouter } from 'next/navigation'

export default function Page() {
  const { signIn, errors, fetchStatus } = useSignIn()
  const router = useRouter()

  const handleSubmit = async (formData: FormData) => {
    const emailAddress = formData.get('email') as string
    const password = formData.get('password') as string

    const { error } = await signIn.password({
      emailAddress,
      password,
    })
    if (error) {
      console.error(JSON.stringify(error, null, 2))
      return
    }

    if (signIn.status === 'complete') {
      await signIn.finalize({
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
    } else if (signIn.status === 'needs_second_factor') {
      // See https://clerk.com/docs/guides/development/custom-flows/authentication/multi-factor-authentication
    } else if (signIn.status === 'needs_client_trust') {
      // For other second factor strategies,
      // see https://clerk.com/docs/guides/development/custom-flows/authentication/client-trust
      const emailCodeFactor = signIn.supportedSecondFactors.find(
        (factor) => factor.strategy === 'email_code',
      )

      if (emailCodeFactor) {
        await signIn.mfa.sendEmailCode()
      }
    } else {
      // Check why the sign-in is not complete
      console.error('Sign-in attempt not complete:', signIn)
    }
  }

  const handleVerify = async (formData: FormData) => {
    const code = formData.get('code') as string

    await signIn.mfa.verifyEmailCode({ code })

    if (signIn.status === 'complete') {
      await signIn.finalize({
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
      // Check why the sign-in is not complete
      console.error('Sign-in attempt not complete:', signIn)
    }
  }

  if (signIn.status === 'needs_client_trust') {
    return (
      <>
        <h1>Verify your account</h1>
        <form action={handleVerify}>
          <div>
            <label htmlFor="code">Code</label>
            <input id="code" name="code" type="text" />
            {errors.fields.code && <p>{errors.fields.code.message}</p>}
          </div>
          <button type="submit" disabled={fetchStatus === 'fetching'}>
            Verify
          </button>
        </form>
        <button onClick={() => signIn.mfa.sendEmailCode()}>I need a new code</button>
        <button onClick={() => signIn.reset()}>Start over</button>
      </>
    )
  }

  return (
    <>
      <h1>Sign in</h1>
      <form action={handleSubmit}>
        <div>
          <label htmlFor="email">Enter email address</label>
          <input id="email" name="email" type="email" />
          {errors.fields.identifier && <p>{errors.fields.identifier.message}</p>}
        </div>
        <div>
          <label htmlFor="password">Enter password</label>
          <input id="password" name="password" type="password" />
          {errors.fields.password && <p>{errors.fields.password.message}</p>}
        </div>
        <button type="submit" disabled={fetchStatus === 'fetching'}>
          Continue
        </button>
      </form>
      
      {errors && <p>{JSON.stringify(errors, null, 2)}</p>}
    </>
  )
}
```

    

    
      In the `(auth)` group, create a `sign-in.tsx` file with the following code. The [`useSignIn()`](/reference/hooks/use-sign-in) hook is used to create a sign-in flow. The user can sign in using email address and password, or navigate to the sign-up page.

```tsx
// Filename: app/(auth)/sign-in.tsx

import { ThemedText } from '@/components/themed-text'
import { ThemedView } from '@/components/themed-view'
import { useSignIn } from '@clerk/expo'
import { type Href, Link, useRouter } from 'expo-router'
import React from 'react'
import { Pressable, StyleSheet, TextInput, View } from 'react-native'

export default function Page() {
  const { signIn, errors, fetchStatus } = useSignIn()
  const router = useRouter()

  const [emailAddress, setEmailAddress] = React.useState('')
  const [password, setPassword] = React.useState('')
  const [code, setCode] = React.useState('')

  const handleSubmit = async () => {
    const { error } = await signIn.password({
      emailAddress,
      password,
    })
    if (error) {
      console.error(JSON.stringify(error, null, 2))
      return
    }

    if (signIn.status === 'complete') {
      await signIn.finalize({
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
    } else if (signIn.status === 'needs_second_factor') {
      // See https://clerk.com/docs/guides/development/custom-flows/authentication/multi-factor-authentication
    } else if (signIn.status === 'needs_client_trust') {
      // For other second factor strategies,
      // see https://clerk.com/docs/guides/development/custom-flows/authentication/client-trust
      const emailCodeFactor = signIn.supportedSecondFactors.find(
        (factor) => factor.strategy === 'email_code',
      )

      if (emailCodeFactor) {
        await signIn.mfa.sendEmailCode()
      }
    } else {
      // Check why the sign-in is not complete
      console.error('Sign-in attempt not complete:', signIn)
    }
  }

  const handleVerify = async () => {
    await signIn.mfa.verifyEmailCode({ code })

    if (signIn.status === 'complete') {
      await signIn.finalize({
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
      // Check why the sign-in is not complete
      console.error('Sign-in attempt not complete:', signIn)
    }
  }

  if (signIn.status === 'needs_client_trust') {
    return (
      
        
          Verify your account
        
         setCode(code)}
          keyboardType="numeric"
        />
        {errors.fields.code && (
          {errors.fields.code.message}
        )}
         [
            styles.button,
            fetchStatus === 'fetching' && styles.buttonDisabled,
            pressed && styles.buttonPressed,
          ]}
          onPress={handleVerify}
          disabled={fetchStatus === 'fetching'}
        >
          Verify
        
         [styles.secondaryButton, pressed && styles.buttonPressed]}
          onPress={() => signIn.mfa.sendEmailCode()}
        >
          I need a new code
        
         [styles.secondaryButton, pressed && styles.buttonPressed]}
          onPress={() => signIn.reset()}
        >
          Start over
        
      
    )
  }

  return (
    
      
        Sign in
      

      Email address
       setEmailAddress(emailAddress)}
        keyboardType="email-address"
      />
      {errors.fields.identifier && (
        {errors.fields.identifier.message}
      )}
      Password
       setPassword(password)}
      />
      {errors.fields.password && (
        {errors.fields.password.message}
      )}
       [
          styles.button,
          (!emailAddress || !password || fetchStatus === 'fetching') && styles.buttonDisabled,
          pressed && styles.buttonPressed,
        ]}
        onPress={handleSubmit}
        disabled={!emailAddress || !password || fetchStatus === 'fetching'}
      >
        Continue
      
      
      {errors && {JSON.stringify(errors, null, 2)}}

      
        Don't have an account? 
        
          Sign up
        
      
    
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
  secondaryButton: {
    paddingVertical: 12,
    paddingHorizontal: 24,
    borderRadius: 8,
    alignItems: 'center',
    marginTop: 8,
  },
  secondaryButtonText: {
    color: '#0a7ea4',
    fontWeight: '600',
  },
  linkContainer: {
    flexDirection: 'row',
    gap: 4,
    marginTop: 12,
    alignItems: 'center',
  },
  error: {
    color: '#d32f2f',
    fontSize: 12,
    marginTop: -8,
  },
  debug: {
    fontSize: 10,
    opacity: 0.5,
    marginTop: 8,
  },
})
```

    
  

  
    ```swift
// Filename: EmailPasswordSignInView.swift

    import SwiftUI
    import ClerkKit

    struct EmailPasswordSignInView: View {
      @Environment(Clerk.self) private var clerk
      @State private var email = ""
      @State private var password = ""
      @State private var code = ""
      @State private var showEmailCode = false

      var body: some View {
        if showEmailCode {
          Text("Verify your email")
          Text("A verification code has been sent to your email.")
          TextField("Enter verification code", text: $code)
          Button("Verify") {
            Task { await verify(code: code) }
          }
        } else {
          TextField("Enter email address", text: $email)
          SecureField("Enter password", text: $password)
          Button("Sign In") {
            Task { await submit(email: email, password: password) }
          }
        }
      }
    }

    extension EmailPasswordSignInView {

      func submit(email: String, password: String) async {
        do {
          // Start sign-in with email/password
          var signIn = try await clerk.auth.signInWithPassword(
            identifier: email,
            password: password
          )

          switch signIn.status {
          case .complete:
            dump(clerk.session)
          case .needsSecondFactor:
            // This is required when Client Trust is enabled and the user
            // is signing in from a new device
            // See https://clerk.com/docs/guides/secure/client-trust
            signIn = try await signIn.sendMfaEmailCode()
            showEmailCode = true
          default:
            // If the status is not complete, check why. User may need to
            // complete further steps
            dump(signIn.status)
          }
      } catch {
        // See https://clerk.com/docs/guides/development/custom-flows/error-handling
        // for more info on error handling
        dump(error)
      }
    }

      func verify(code: String) async {
        do {
          // Verify the email code
          guard var signIn = clerk.auth.currentSignIn else { return }

          signIn = try await signIn.verifyMfaCode(code, type: .emailCode)

          switch signIn.status {
          case .complete:
            dump(clerk.session)
          default:
            dump(signIn.status)
          }
      } catch {
        // See https://clerk.com/docs/guides/development/custom-flows/error-handling
        // for more info on error handling.
        dump(error)
      }
    }
    }
    ```
  

  
    
**EmailPasswordSignInViewModel.kt:**

```kotlin
// Filename: EmailPasswordSignInViewModel.kt

      package com.clerk.customflows.emailpassword.signin

      import android.util.Log
      import androidx.lifecycle.ViewModel
      import androidx.lifecycle.viewModelScope
      import com.clerk.api.Clerk
      import com.clerk.api.network.serialization.onFailure
      import com.clerk.api.network.serialization.onSuccess
      import kotlinx.coroutines.flow.MutableStateFlow
      import kotlinx.coroutines.flow.asStateFlow
      import kotlinx.coroutines.flow.combine
      import kotlinx.coroutines.flow.launchIn
      import kotlinx.coroutines.launch

      class EmailPasswordSignInViewModel : ViewModel() {
      private val _uiState =
      MutableStateFlow(EmailPasswordSignInUiState.Loading)
      val uiState = _uiState.asStateFlow()

      init {
      combine(Clerk.userFlow, Clerk.isInitialized) { user, isInitialized ->
          Log.e("EmailPasswordSignInViewModel", "combine: $user, $isInitialized")
          _uiState.value =
            when {
              !isInitialized -> EmailPasswordSignInUiState.Loading
              user == null -> EmailPasswordSignInUiState.SignedOut
              else -> EmailPasswordSignInUiState.SignedIn
            }
        }
        .launchIn(viewModelScope)
      }

      fun submit(email: String, password: String) {
      viewModelScope.launch {
        Clerk.auth
          .signInWithPassword {
            identifier = email
            this.password = password
          }
          .onSuccess { _uiState.value = EmailPasswordSignInUiState.SignedIn }
          .onFailure {
            // See https://clerk.com/docs/guides/development/custom-flows/error-handling
            // for more info on error handling
          }
      }
      }

      sealed interface EmailPasswordSignInUiState {
      data object Loading : EmailPasswordSignInUiState

      data object SignedOut : EmailPasswordSignInUiState

      data object SignedIn : EmailPasswordSignInUiState
      }
      }
      ```


**EmailPasswordSignInActivity.kt:**

```kotlin
// Filename: EmailPasswordSignInActivity.kt

      package com.clerk.customflows.emailpassword.signin

      import android.os.Bundle
      import androidx.activity.ComponentActivity
      import androidx.activity.compose.setContent
      import androidx.activity.viewModels
      import androidx.compose.foundation.layout.Arrangement
      import androidx.compose.foundation.layout.Box
      import androidx.compose.foundation.layout.Column
      import androidx.compose.foundation.layout.fillMaxSize
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
      import androidx.compose.ui.text.input.PasswordVisualTransformation
      import androidx.compose.ui.unit.dp
      import androidx.lifecycle.compose.collectAsStateWithLifecycle
      import com.clerk.api.Clerk

      class EmailPasswordSignInActivity : ComponentActivity() {

      val viewModel: EmailPasswordSignInViewModel by viewModels()

      override fun onCreate(savedInstanceState: Bundle?) {
      super.onCreate(savedInstanceState)
      setContent {
        val state by viewModel.uiState.collectAsStateWithLifecycle()
        EmailPasswordSignInView(state = state, onSubmit = viewModel::submit)
      }
      }
      }

      @Composable
      fun EmailPasswordSignInView(
      state: EmailPasswordSignInViewModel.EmailPasswordSignInUiState,
      onSubmit: (String, String) -> Unit,
      ) {
      var email by remember { mutableStateOf("") }
      var password by remember { mutableStateOf("") }

      Box(modifier = Modifier.fillMaxSize(), contentAlignment = Alignment.Center) {
      when (state) {
        EmailPasswordSignInViewModel.EmailPasswordSignInUiState.SignedOut -> {
          Column(
            verticalArrangement = Arrangement.spacedBy(16.dp, Alignment.CenterVertically),
            horizontalAlignment = Alignment.CenterHorizontally,
          ) {
            TextField(value = email, onValueChange = { email = it }, label = { Text("Email") })
            TextField(
              value = password,
              onValueChange = { password = it },
              visualTransformation = PasswordVisualTransformation(),
              label = { Text("Password") },
            )
            Button(onClick = { onSubmit(email, password) }) { Text("Sign in") }
          }
        }
        EmailPasswordSignInViewModel.EmailPasswordSignInUiState.SignedIn -> {
          Text("Current session: ${Clerk.session?.id}")
        }

        EmailPasswordSignInViewModel.EmailPasswordSignInUiState.Loading ->
          Box(modifier = Modifier.fillMaxSize(), contentAlignment = Alignment.Center) {
            CircularProgressIndicator()
          }
      }
      }
      }
      ```
