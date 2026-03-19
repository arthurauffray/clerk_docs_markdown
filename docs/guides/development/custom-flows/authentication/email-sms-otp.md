# Build a custom sign-in flow with email or phone code


> Learn how build a custom passwordless sign-in flow with email or phone code using the Clerk API.

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
  > If you're using an older version of one of these SDKs, or are using the legacy API, refer to the [legacy API documentation](/guides/development/custom-flows/authentication/legacy/email-sms-otp).


Clerk supports passwordless authentication, which lets users sign in and sign up without having to remember a password. Instead, users receive a one-time password (OTP) via email or phone, which they can use to authenticate themselves.

This guide demonstrates how to build a custom user interface for signing up and signing in using phone OTP. The process for using email OTP is similar, and the differences will be highlighted throughout.


  ## Enable phone OTP

  To use phone OTP:

  1. In the Clerk Dashboard, navigate to the [**User & authentication**](https://dashboard.clerk.com/~/user-authentication/user-and-authentication) page.
  1. Disable all email authentication settings, or these examples will error.
  1. Select the **Phone** tab and enable **Sign-up with phone** and **Sign-in with phone**. It's recommended to enable **Verify at sign-up**.
  1. Ensure **Password** is disabled, as you want to use SMS OTP and not password authentication.

  To use email OTP:

  1. In the Clerk Dashboard, navigate to the [**User & authentication**](https://dashboard.clerk.com/~/user-authentication/user-and-authentication) page.
  1. Ensure **Require email address** is enabled.
  1. Ensure **Verify at sign-up** is enabled, with **Email verification code** selected.
  1. Ensure **Sign-in with email** is enabled, with **Email verification code** selected.
  1. Ensure **Password** is disabled, as you want to use email OTP and not password authentication.

  ## Sign-up flow

  
    
      > [!TIP]
> Examples for this SDK aren't available yet. For now, try adapting the  available example to fit your SDK.

    

    First, understand that the `useSignUp()` hook returns an object with the following properties:

- `signUp`: The [`SignUpFuture`](/reference/javascript/sign-up-future) object. Use this to initiate the sign-up process and check the current state of the sign-up attempt.
- `errors`: The [`Errors`](/reference/javascript/types/errors) object that contains the errors that occurred during the last API request. You can use this to display errors to the user in your custom UI.
- `fetchStatus`: The fetch status of the underlying [`SignUpFuture`](/reference/javascript/sign-up-future) resource. You can use this to display a loading state or disable buttons while the request is in progress.


    Then, to sign up a user using their phone number and verify their sign-up with an SMS code, you must:

    1. Initiate the sign-up process by collecting the user's phone number with the [`signUp.create()`](/reference/javascript/sign-up-future#create) method.
    1. Send a one-time code to the provided phone number for verification with the [`signUp.verifications.sendPhoneCode()`](/reference/javascript/sign-up-future#verifications-send-phone-code) method (or [`signUp.verifications.sendEmailCode()`](/reference/javascript/sign-up-future#verifications-send-email-code) if you're modifying this example for email OTP).
    1. Collect the one-time code and verify it with the [`signUp.verifications.verifyPhoneCode()`](/reference/javascript/sign-up-future#verifications-verify-phone-code) method (or [`signUp.verifications.verifyEmailCode()`](/reference/javascript/sign-up-future#verifications-verify-email-code) if you're modifying this example for email OTP).
       > [!WARNING]
> Phone numbers must be in [E.164 format](https://en.wikipedia.org/wiki/E.164).

    1. If the phone number verification is successful, finalize the sign-up with the [`signUp.finalize()`](/reference/javascript/sign-up-future#finalize) method to create the user and set the newly created session as the active session.

    
      ```tsx
// Filename: app/sign-up/page.tsx

      'use client'

      import * as React from 'react'
      import { useAuth, useSignUp } from '@clerk/nextjs'
      import { useRouter } from 'next/navigation'

      export default function SignUpPage() {
        const { signUp, errors, fetchStatus } = useSignUp()
        const { isSignedIn } = useAuth()
        const router = useRouter()

        const handleSubmit = async (formData: FormData) => {
          // For email OTP: collect the email address instead of the phone number
          const phoneNumber = formData.get('phoneNumber') as string

          // For email OTP: change create({ phoneNumber }) to create({ emailAddress })
          const { error } = await signUp.create({ phoneNumber })
          if (error) {
            // See https://clerk.com/docs/guides/development/custom-flows/error-handling
            console.error(JSON.stringify(error, null, 2))
            return
          }

          // For email OTP: change sendPhoneCode() to sendEmailCode()
          if (!error) await signUp.verifications.sendPhoneCode()
        }

        const handleVerify = async (formData: FormData) => {
          const code = formData.get('code') as string

          // For email OTP: change verifyPhoneCode() to verifyEmailCode()
          await signUp.verifications.verifyPhoneCode({ code })

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
            // Check why the status is not complete
            console.error('Sign-up attempt not complete.', signUp)
          }
        }

        if (signUp.status === 'complete' || isSignedIn) {
          return null
        }

        if (
          signUp.status === 'missing_requirements' &&
          // For email OTP: check for phone_number instead of email_address
          signUp.unverifiedFields.includes('phone_number') &&
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
              
              <button onClick={() => signUp.verifications.sendPhoneCode()}>I need a new code</button>
            </>
          )
        }

        return (
          <>
            <h1>Sign up</h1>
            <form action={handleSubmit}>
              
              <div>
                <label htmlFor="phoneNumber">Phone number</label>
                <input id="phoneNumber" name="phoneNumber" type="tel" />
                {errors.fields.phoneNumber && <p>{errors.fields.phoneNumber.message}</p>}
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
    

    
      ```tsx
// Filename: app/sign-up/page.tsx

      import { ThemedText } from '@/components/themed-text'
      import { ThemedView } from '@/components/themed-view'
      import { useSignUp } from '@clerk/expo'
      import { type Href, Link, useRouter } from 'expo-router'
      import React from 'react'
      import { Pressable, StyleSheet, TextInput, View } from 'react-native'

      export default function Page() {
        const { signUp, errors, fetchStatus } = useSignUp()
        const router = useRouter()

        // For email OTP: collect the email address instead of the phone number
        const [phoneNumber, setPhoneNumber] = React.useState('')
        const [code, setCode] = React.useState('')

        const handleSubmit = async () => {
          // For email OTP: change create({ phoneNumber }) to create({ emailAddress })
          const { error } = await signUp.create({ phoneNumber })
          if (error) {
            console.error(JSON.stringify(error, null, 2))
            return
          }

          // For email OTP: change sendPhoneCode() to sendEmailCode()
          if (!error) await signUp.verifications.sendPhoneCode()
        }

        const handleVerify = async () => {
          // For email OTP: change verifyPhoneCode() to verifyEmailCode()
          await signUp.verifications.verifyPhoneCode({ code })

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

        if (signUp.status === 'complete') {
          return null
        }

        if (
          signUp.status === 'missing_requirements' &&
          // For email OTP: check for email_address instead of phone_number
          signUp.unverifiedFields.includes('phone_number') &&
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
                // For email OTP: change sendPhoneCode() to sendEmailCode()
                onPress={() => signUp.verifications.sendPhoneCode()}
              >
                I need a new code
              
            
          )
        }

        return (
          
            
              Sign up
            
            Phone number
            
             setPhoneNumber(phoneNumber)}
              keyboardType="phone-pad"
            />
            {errors.fields.phoneNumber && (
              {errors.fields.phoneNumber.message}
            )}
             [
                styles.button,
                (!phoneNumber || fetchStatus === 'fetching') && styles.buttonDisabled,
                pressed && styles.buttonPressed,
              ]}
              onPress={handleSubmit}
              disabled={!phoneNumber || fetchStatus === 'fetching'}
            >
              Continue
            
            
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
    
  

  
    1. Initiate the sign-up process by collecting the user's identifier, which for this example is a phone number.
    1. Prepare the verification, which sends a one-time code to the given identifier.
    1. Attempt to complete the verification with the code the user provides.
    1. If the verification is successful, set the newly created session as the active session.

    
      ```swift
// Filename: SMSOTPSignUpView.swift

      import SwiftUI
      import ClerkKit

      struct SMSOTPSignUpView: View {
      @Environment(Clerk.self) private var clerk
      // For email OTP: collect the email address instead of the phone number
      @State private var phoneNumber = ""
      @State private var code = ""
      @State private var isVerifying = false

      var body: some View {
        if isVerifying {
          TextField("Enter your verification code", text: $code)
          Button("Verify") {
            Task { await verify(code: code) }
          }
        } else {
          // For email OTP: change phoneNumber to emailAddress
          TextField("Enter phone number", text: $phoneNumber)
          Button("Continue") {
            Task { await submit(phoneNumber: phoneNumber) }
          }
        }
      }
      }

      extension SMSOTPSignUpView {

      func submit(phoneNumber: String) async {
        do {
          // For email OTP: change phoneNumber to emailAddress
          let signUp = try await clerk.auth.signUp(phoneNumber: phoneNumber)

          // For email OTP: change signUp.sendPhoneCode() to signUp.sendEmailCode()
          try await signUp.sendPhoneCode()

          isVerifying = true
      } catch {
        // See https://clerk.com/docs/guides/development/custom-flows/error-handling
        // for more info on error handling
        dump(error)
      }
      }

      func verify(code: String) async {
        do {
          guard var signUp = clerk.auth.currentSignUp else { return }

          // For email OTP: change signUp.verifyPhoneCode() to signUp.verifyEmailCode()
          signUp = try await signUp.verifyPhoneCode(code)

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
    

    
      
**SMSOTPSignUpViewModel.kt:**

```kotlin
// Filename: SMSOTPSignUpViewModel.kt

        import androidx.lifecycle.ViewModel
        import androidx.lifecycle.viewModelScope
        import com.clerk.api.Clerk
        import com.clerk.api.auth.types.VerificationType
        import com.clerk.api.network.serialization.flatMap
        import com.clerk.api.network.serialization.onFailure
        import com.clerk.api.network.serialization.onSuccess
        import com.clerk.api.signup.SignUp
        import com.clerk.api.signup.sendCode
        import com.clerk.api.signup.verifyCode
        import kotlinx.coroutines.flow.MutableStateFlow
        import kotlinx.coroutines.flow.asStateFlow
        import kotlinx.coroutines.flow.combine
        import kotlinx.coroutines.flow.launchIn
        import kotlinx.coroutines.launch

        class SMSOTPSignUpViewModel : ViewModel() {

        private val _uiState = MutableStateFlow(UiState.Unverified)
        val uiState = _uiState.asStateFlow()

        init {
        combine(Clerk.isInitialized, Clerk.userFlow) { isInitialized, user ->
            _uiState.value =
              when {
                !isInitialized -> UiState.Loading
                user == null -> UiState.Unverified
                else -> UiState.Verified
              }
          }
          .launchIn(viewModelScope)
        }

        fun submit(phoneNumber: String) {
        viewModelScope.launch {
          Clerk.auth
            // For email OTP: change phone = phoneNumber to email = emailAddress
            .signUp { phone = phoneNumber }
            .flatMap { it.sendCode { phone = phoneNumber } }
            .onSuccess { _uiState.value = UiState.Verifying }
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
            // For email OTP: change VerificationType.PHONE to VerificationType.EMAIL
            .verifyCode(code, VerificationType.PHONE)
            .onSuccess {
              if (it.status == SignUp.Status.COMPLETE) {
                _uiState.value = UiState.Verified
              } else {
                // The user may need to complete further steps
              }
            }
            .onFailure {
              // See https://clerk.com/docs/guides/development/custom-flows/error-handling
              // for more info on error handling
            }
        }
        }

        sealed interface UiState {
        data object Loading : UiState

        data object Unverified : UiState

        data object Verifying : UiState

        data object Verified : UiState
        }
        }
        ```


**SMSOTPSignUpActivity.kt:**

```kotlin
// Filename: SMSOTPSignUpActivity.kt

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
        import androidx.compose.ui.unit.dp
        import androidx.lifecycle.compose.collectAsStateWithLifecycle

        class SMSOTPSignUpActivity : ComponentActivity() {
        val viewModel: SMSOTPSignUpViewModel by viewModels()

        override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent {
          val state by viewModel.uiState.collectAsStateWithLifecycle()
          SMSOTPSignUpView(state, viewModel::submit, viewModel::verify)
        }
        }
        }

        @Composable
        fun SMSOTPSignUpView(
        state: SMSOTPSignUpViewModel.UiState,
        onSubmit: (String) -> Unit,
        onVerify: (String) -> Unit,
        ) {
        Box(modifier = Modifier.fillMaxSize(), contentAlignment = Alignment.Center) {
        when (state) {
          // For email OTP: collect the email address instead of the phone number
          SMSOTPSignUpViewModel.UiState.Unverified -> {
            InputContent(
              placeholder = "Enter your phone number",
              buttonText = "Continue",
              onClick = onSubmit,
            )
          }
          SMSOTPSignUpViewModel.UiState.Verified -> {
            Text("Verified")
          }
          SMSOTPSignUpViewModel.UiState.Verifying -> {
            InputContent(
              placeholder = "Enter your verification code",
              buttonText = "Verify",
              onClick = onVerify,
            )
          }

          SMSOTPSignUpViewModel.UiState.Loading -> {
            CircularProgressIndicator()
          }
        }
        }
        }

        @Composable
        fun InputContent(placeholder: String, buttonText: String, onClick: (String) -> Unit) {
        var value by remember { mutableStateOf("") }
        Column(
        horizontalAlignment = Alignment.CenterHorizontally,
        verticalArrangement = Arrangement.spacedBy(16.dp, Alignment.CenterVertically),
        ) {
        TextField(placeholder = { Text(placeholder) }, value = value, onValueChange = { value = it })
        Button(onClick = { onClick(value) }) { Text(buttonText) }
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


    1. Initiate the sign-in process by collecting the user's phone number with the [`signIn.phoneCode.sendCode()`](/reference/javascript/sign-in-future#phone-code-send-code) method.
    1. Send a one-time code to the provided phone number for verification with the [`signIn.phoneCode.verifyCode()`](/reference/javascript/sign-in-future#phone-code-verify-code) method (or [`signIn.emailCode.verifyCode()`](/reference/javascript/sign-in-future#email-code-verify-code) if you're modifying this example for email OTP).
    1. Collect the one-time code and verify it with the [`signIn.phoneCode.verifyCode()`](/reference/javascript/sign-in-future#phone-code-verify-code) method (or [`signIn.emailCode.verifyCode()`](/reference/javascript/sign-in-future#email-code-verify-code) if you're modifying this example for email OTP).
       > [!WARNING]
> Phone numbers must be in [E.164 format](https://en.wikipedia.org/wiki/E.164).

    1. If the phone number verification is successful, finalize the sign-in with the [`signIn.finalize()`](/reference/javascript/sign-in-future#finalize) method to set the newly created session as the active session.

    
      ```tsx
// Filename: app/sign-in/page.tsx

      'use client'

      import { useSignIn } from '@clerk/nextjs'
      import { useRouter } from 'next/navigation'

      export default function Page() {
        const { signIn, errors, fetchStatus } = useSignIn()
        const router = useRouter()

        async function handleSubmit(formData: FormData) {
          // For email OTP: collect the email address instead of the phone number
          const phoneNumber = formData.get('phoneNumber') as string

          // For email OTP: change phoneNumber to emailAddress
          const { error } = await signIn.create({ identifier: phoneNumber })
          if (error) {
            // See https://clerk.com/docs/guides/development/custom-flows/error-handling
            console.error(JSON.stringify(error, null, 2))
            return
          }

          // For email OTP: change phoneCode.sendCode() to emailCode.sendCode()
          if (!error) await signIn.phoneCode.sendCode({ phoneNumber })

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

        async function handleVerification(formData: FormData) {
          const code = formData.get('code') as string

          // For email OTP: change phoneCode.verifyCode() to emailCode.verifyCode()
          await signIn.phoneCode.verifyCode({ code })

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

        if (signIn.status === 'needs_first_factor') {
          return (
            <>
              <h1>Verify your phone number</h1>
              <form action={handleVerification}>
                <label htmlFor="code">Enter your verification code</label>
                <input id="code" name="code" type="text" />
                {errors.fields.code && <p>{errors.fields.code.message}</p>}
                <button type="submit" disabled={fetchStatus === 'fetching'}>
                  Verify
                </button>
              </form>
              
              <button onClick={() => signIn.phoneCode.sendCode()}>I need a new code</button>
              <button onClick={() => signIn.reset()}>Start over</button>
            </>
          )
        }

        return (
          <>
            <h1>Sign in</h1>
            <form action={handleSubmit}>
              
              <label htmlFor="phoneNumber">Enter phone number</label>
              <input id="phoneNumber" name="phoneNumber" type="tel" />
              {errors.fields.identifier && <p>{errors.fields.identifier.message}</p>}
              <button type="submit" disabled={fetchStatus === 'fetching'}>
                Continue
              </button>
            </form>
            
            {errors && <p>{JSON.stringify(errors, null, 2)}</p>}
          </>
        )
      }
      ```
    

    
      ```tsx
// Filename: app/sign-in/page.tsx

      import { ThemedText } from '@/components/themed-text'
      import { ThemedView } from '@/components/themed-view'
      import { useSignIn } from '@clerk/expo'
      import { type Href, Link, useRouter } from 'expo-router'
      import React from 'react'
      import { Pressable, StyleSheet, TextInput, View } from 'react-native'

      export default function Page() {
        const { signIn, errors, fetchStatus } = useSignIn()
        const router = useRouter()

        // For email OTP: collect the email address instead of the phone number
        const [phoneNumber, setPhoneNumber] = React.useState('')
        const [code, setCode] = React.useState('')

        const handleSubmit = async () => {
          // For email OTP: change phoneNumber to emailAddress
          const { error } = await signIn.create({ identifier: phoneNumber })
          if (error) {
            // See https://clerk.com/docs/guides/development/custom-flows/error-handling
            console.error(JSON.stringify(error, null, 2))
            return
          }

          // For email OTP: change phoneCode.sendCode() to emailCode.sendCode()
          if (!error) await signIn.phoneCode.sendCode({ phoneNumber })

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

        const handleVerification = async () => {
          // For email OTP: change phoneCode.verifyCode() to emailCode.verifyCode()
          await signIn.phoneCode.verifyCode({ code })

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

        if (signIn.status === 'needs_first_factor') {
          return (
            
              
                Verify your phone number
              
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
                onPress={handleVerification}
                disabled={fetchStatus === 'fetching'}
              >
                Verify
              
               [styles.secondaryButton, pressed && styles.buttonPressed]}
                // For email OTP: change phoneCode.sendCode() to emailCode.sendCode()
                onPress={() => signIn.phoneCode.sendCode()}
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
            
            
            Phone number
             setPhoneNumber(phoneNumber)}
              keyboardType="phone-pad"
            />
            {errors.fields.identifier && (
              {errors.fields.identifier.message}
            )}
             [
                styles.button,
                (!phoneNumber || fetchStatus === 'fetching') && styles.buttonDisabled,
                pressed && styles.buttonPressed,
              ]}
              onPress={handleSubmit}
              disabled={!phoneNumber || fetchStatus === 'fetching'}
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
    
  

  
    1. Initiate the sign-in process by creating a `SignIn` using the identifier provided, which for this example is a phone number.
    1. Prepare the first factor verification.
    1. Attempt verification with the code the user provides.
    1. If the attempt is successful, set the newly created session as the active session.

    
      ```swift
// Filename: SMSOTPSignInView.swift

      import SwiftUI
      import ClerkKit

      struct SMSOTPSignInView: View {
      @Environment(Clerk.self) private var clerk
      // For email OTP: collect the email address instead of the phone number
      @State private var phoneNumber = ""
      @State private var code = ""
      @State private var isVerifying = false

      var body: some View {
        if isVerifying {
          TextField("Enter your verification code", text: $code)
          Button("Verify") {
            Task { await verify(code: code) }
          }
        } else {
          // For email OTP: change phoneNumber to emailAddress
          TextField("Enter phone number", text: $phoneNumber)
          Button("Continue") {
            Task { await submit(phoneNumber: phoneNumber) }
          }
        }
      }
      }

      extension SMSOTPSignInView {

      func submit(phoneNumber: String) async {
        do {
          // For email OTP: change signInWithPhoneCode() to signInWithEmailCode()
          try await clerk.auth.signInWithPhoneCode(phoneNumber: phoneNumber)

          isVerifying = true
      } catch {
        // See https://clerk.com/docs/guides/development/custom-flows/error-handling
        // for more info on error handling.
        dump(error)
      }
      }

      func verify(code: String) async {
        do {
          guard var signIn = clerk.auth.currentSignIn else { return }

          signIn = try await signIn.verifyCode(code)

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
    

    
      
**SMSOTPSignInViewModel.kt:**

```kotlin
// Filename: SMSOTPSignInViewModel.kt

        import androidx.lifecycle.ViewModel
        import androidx.lifecycle.viewModelScope
        import com.clerk.api.Clerk
        import com.clerk.api.network.serialization.onFailure
        import com.clerk.api.network.serialization.onSuccess
        import com.clerk.api.signin.SignIn
        import com.clerk.api.signin.verifyCode
        import kotlinx.coroutines.flow.MutableStateFlow
        import kotlinx.coroutines.flow.asStateFlow
        import kotlinx.coroutines.flow.combine
        import kotlinx.coroutines.flow.launchIn
        import kotlinx.coroutines.launch

        class SMSOTPSignInViewModel : ViewModel() {
        private val _uiState = MutableStateFlow(UiState.Unverified)
        val uiState = _uiState.asStateFlow()

        init {
        combine(Clerk.isInitialized, Clerk.userFlow) { isInitialized, user ->
            _uiState.value =
              when {
                !isInitialized -> UiState.Loading
                user == null -> UiState.Unverified
                else -> UiState.Verified
              }
          }
          .launchIn(viewModelScope)
        }

        fun submit(phoneNumber: String) {
        viewModelScope.launch {
          Clerk.auth
            // For email OTP: change phone = phoneNumber to email = emailAddress
            .signInWithOtp { phone = phoneNumber }
            .onSuccess { _uiState.value = UiState.Verifying }
            .onFailure {
              // See https://clerk.com/docs/guides/development/custom-flows/error-handling
              // for more info on error handling
            }
        }
        }

        fun verify(code: String) {
        val inProgressSignIn = Clerk.auth.currentSignIn ?: return
        viewModelScope.launch {
          inProgressSignIn
            .verifyCode(code)
            .onSuccess {
              if (it.status == SignIn.Status.COMPLETE) {
                _uiState.value = UiState.Verified
              } else {
                // The user may need to complete further steps
              }
            }
            .onFailure {
              // See https://clerk.com/docs/guides/development/custom-flows/error-handling
              // for more info on error handling
            }
        }
        }

        sealed interface UiState {
        data object Loading : UiState

        data object Unverified : UiState

        data object Verifying : UiState

        data object Verified : UiState
        }
        }
        ```


**SMSOTPSignInActivity.kt:**

```kotlin
// Filename: SMSOTPSignInActivity.kt

        package com.clerk.customflows.otp.signin

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
        import androidx.compose.ui.unit.dp
        import androidx.lifecycle.compose.collectAsStateWithLifecycle

        class SMSOTPSignInActivity : ComponentActivity() {
        val viewModel: SMSOTPSignInViewModel by viewModels()

        override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent {
          val state by viewModel.uiState.collectAsStateWithLifecycle()
          SMSOTPSignInView(state, viewModel::submit, viewModel::verify)
        }
        }
        }

        @Composable
        fun SMSOTPSignInView(
        state: SMSOTPSignInViewModel.UiState,
        onSubmit: (String) -> Unit,
        onVerify: (String) -> Unit,
        ) {
        Box(modifier = Modifier.fillMaxSize(), contentAlignment = Alignment.Center) {
        when (state) {
          // For email OTP: collect the email address instead of the phone number
          SMSOTPSignInViewModel.UiState.Unverified -> {
            InputContent(
              placeholder = "Enter your phone number",
              buttonText = "Continue",
              onClick = onSubmit,
            )
          }
          SMSOTPSignInViewModel.UiState.Verified -> {
            Text("Verified")
          }
          SMSOTPSignInViewModel.UiState.Verifying -> {
            InputContent(
              placeholder = "Enter your verification code",
              buttonText = "Verify",
              onClick = onVerify,
            )
          }

          SMSOTPSignInViewModel.UiState.Loading -> {
            CircularProgressIndicator()
          }
        }
        }
        }

        @Composable
        fun InputContent(placeholder: String, buttonText: String, onClick: (String) -> Unit) {
        var value by remember { mutableStateOf("") }
        Column(
        horizontalAlignment = Alignment.CenterHorizontally,
        verticalArrangement = Arrangement.spacedBy(16.dp, Alignment.CenterVertically),
        ) {
        TextField(placeholder = { Text(placeholder) }, value = value, onValueChange = { value = it })
        Button(onClick = { onClick(value) }) { Text(buttonText) }
        }
        }
        ```
