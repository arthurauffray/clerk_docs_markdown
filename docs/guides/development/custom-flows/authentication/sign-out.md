# Build a custom sign-out flow


> Learn how to use the Clerk API to build a custom sign-out flow using Clerk's signOut() function.

> [!WARNING]
> This guide is for users who want to build a custom flow. To use a _prebuilt_ UI, use the [Account Portal pages](/guides/account-portal/overview) or [prebuilt components](/reference/components/overview).


Clerk's [``](/reference/components/user/user-button) and [``](/reference/components/unstyled/sign-out-button) components provide an out-of-the-box solution for signing out users. However, if you're building a custom solution, you can use the `signOut()` function to handle the sign-out process.

The `signOut()` function signs a user out of all sessions in a [multi-session application](/guides/secure/session-options#multi-session-applications), or only the current session in a single-session context. You can also specify a specific session to sign out by passing the `sessionId` parameter.

> [!NOTE]
> The sign-out flow deactivates only the current session. Other valid sessions associated with the same user (e.g., if the user is signed in on another device) will remain active.


  The [`useClerk()`](/reference/hooks/use-clerk) hook is used to access the `signOut()` function, which is called when the user clicks the "Sign out" button.

  
    
      > [!TIP]
> Examples for this SDK aren't available yet. For now, try adapting the  available example to fit your SDK.

    

    ```jsx
// Filename: app/components/sign-out-button.tsx

    'use client'

    import { useClerk } from '@clerk/nextjs'

    export const SignOutButton = () => {
      const { signOut } = useClerk()

      return (
        // Clicking this button signs out a user
        // and redirects them to the home page "/".
        <button onClick={() => signOut({ redirectUrl: '/' })}>Sign out</button>
      )
    }
    ```
  

  
    ```tsx
// Filename: app/components/sign-out-button.tsx

import { ThemedText } from '@/components/themed-text'
import { useClerk } from '@clerk/expo'
import { useRouter } from 'expo-router'
import { Pressable, StyleSheet } from 'react-native'

export const SignOutButton = () => {
  // Use `useClerk()` to access the `signOut()` function
  const { signOut } = useClerk()
  const router = useRouter()

  const handleSignOut = async () => {
    try {
      await signOut()
      // Redirect to your desired page
      router.replace('/')
    } catch (err) {
      // See https://clerk.com/docs/guides/development/custom-flows/error-handling
      // for more info on error handling
      console.error(JSON.stringify(err, null, 2))
    }
  }

  return (
     [styles.button, pressed && styles.buttonPressed]}
      onPress={handleSignOut}
    >
      Sign out
    
  )
}

const styles = StyleSheet.create({
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
  buttonText: {
    color: '#fff',
    fontWeight: '600',
  },
})
```

  


  
**index.html:**

```html
<!-- Filename: index.html -->

    <!doctype html>
    <html lang="en">
      <head>
        <meta charset="UTF-8" />
        <link rel="icon" type="image/svg+xml" href="/clerk.svg" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>Clerk + JavaScript App</title>
      </head>

      <body>
        <div id="app"></div>
        <button id="sign-out">Sign out</button>
        <script type="module" src="main.js" async crossorigin="anonymous"></script>
      </body>
    </html>
    ```


**main.js:**

```js
// Filename: main.js

    import { Clerk } from '@clerk/clerk-js'

    const pubKey = import.meta.env.VITE_CLERK_PUBLISHABLE_KEY

    const clerk = new Clerk(pubKey)
    await clerk.load()

    if (clerk.isSignedIn) {
      // Attach signOut function to the sign-out button
      document.getElementById('sign-out').addEventListener('click', async () => {
        await clerk.signOut()
        // Optional: refresh page after sign-out
        window.location.reload()
      })
    }
    ```


  ```swift
// Filename: SignOutView.swift

    import SwiftUI
    import ClerkKit

    struct SignOutView: View {
      @Environment(Clerk.self) private var clerk

      var body: some View {
        if let user = clerk.user {
          Text("Signed in as: \(user.id)")
          Button("Sign out") {
            Task { await signOut() }
          }
        } else {
          Text("You are signed out")
        }
      }
    }

    extension SignOutView {

      func signOut() async {
        do {
          // Sign out the active user
          try await clerk.auth.signOut()
        } catch {
          // See https://clerk.com/docs/guides/development/custom-flows/error-handling
          // for more info on error handling.
          dump(error)
        }
      }
    }
  ```


  

  
**MainViewModel.kt:**

```kotlin
// Filename: MainViewModel.kt

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

    class MainViewModel : ViewModel() {

      private val _uiState = MutableStateFlow(UiState.Loading)
      val uiState = _uiState.asStateFlow()

      init {
        combine(Clerk.isInitialized, Clerk.userFlow) { isInitialized, user ->
            _uiState.value =
              when {
                !isInitialized -> UiState.Loading
                user != null -> UiState.SignedIn
                else -> UiState.SignedOut
              }
          }
          .launchIn(viewModelScope)
      }

      fun signOut() {
        viewModelScope.launch {
          Clerk.signOut()
            .onSuccess { _uiState.value = UiState.SignedOut }
            .onFailure {
              // See https://clerk.com/docs/guides/development/custom-flows/error-handling
              // for more info on error handling
            }
        }
      }

      sealed interface UiState {
        data object SignedIn : UiState

        data object SignedOut : UiState

        data object Loading : UiState
      }
    }
    ```


**MainActivity.kt:**

```kotlin
// Filename: MainActivity.kt

    import android.os.Bundle
    import androidx.activity.ComponentActivity
    import androidx.activity.compose.setContent
    import androidx.activity.enableEdgeToEdge
    import androidx.activity.viewModels
    import androidx.compose.foundation.layout.Box
    import androidx.compose.foundation.layout.fillMaxSize
    import androidx.compose.material3.Button
    import androidx.compose.material3.CircularProgressIndicator
    import androidx.compose.material3.Text
    import androidx.compose.runtime.getValue
    import androidx.compose.ui.Alignment
    import androidx.compose.ui.Modifier
    import androidx.lifecycle.compose.collectAsStateWithLifecycle

    class MainActivity : ComponentActivity() {
        val viewModel: MainViewModel by viewModels()

        override fun onCreate(savedInstanceState: Bundle?) {
            super.onCreate(savedInstanceState)
            enableEdgeToEdge()
            setContent {
                val state by viewModel.uiState.collectAsStateWithLifecycle()

                Box(
                    modifier = Modifier.fillMaxSize(),
                    contentAlignment = Alignment.Center
                ) {
                    when (state) {
                        MainViewModel.UiState.Loading -> {
                            CircularProgressIndicator()
                        }

                        MainViewModel.UiState.SignedIn -> {
                            Button(onClick = { viewModel.signOut() }) {
                                Text("Sign out")
                            }
                        }

                        MainViewModel.UiState.SignedOut -> {
                            // Signed out content
                        }
                    }
                }
            }
        }
    }
    ```
