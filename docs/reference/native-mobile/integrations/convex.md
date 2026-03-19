# Integrate Convex with Clerk


> Learn how to integrate Clerk with Convex in your native app.

With [Convex](https://www.convex.dev/), you can build a backend with a provided realtime database, file storage, text search, scheduling, and more. Paired with Clerk's authentication and user management features, you can build native mobile apps with a secure auth flow and realtime data access.

This guide shows how to integrate Convex with Clerk in your native mobile app. It assumes you have already integrated both Convex and Clerk in your app.


  ## Set up Clerk as a Convex auth provider

For your Clerk session token to work with Convex, you need to set up the Convex integration in Clerk.

1. In the Clerk Dashboard, navigate to the [Convex integration setup](https://dashboard.clerk.com/apps/setup/convex).
1. Choose your configuration options, and then select **Activate Convex integration**. This will reveal the Frontend API URL for your Clerk instance.
1. Save the URL. In development, its format is `https://verb-noun-00.clerk.accounts.dev`. In production, its format is `https://clerk.<your-domain>.com`.

## Map additional claims (optional)

If you need to map additional claims, navigate to the [**Sessions**](https://dashboard.clerk.com/~/sessions) page in the Clerk Dashboard.

In the **Claims** section, the default audience (`aud`) claim required by Convex is pre-mapped. You can include additional claims as necessary. [Shortcodes](/guides/sessions/jwt-templates#shortcodes) are available to make adding dynamic user values easy.


  ## Configure Convex with Clerk's Frontend API URL

  In your app's `convex` folder, create a `auth.config.ts` file with the following configuration, using the saved Frontend API URL from earlier:

  ```ts
// Filename: convex/auth.config.ts

  export default {
    providers: [
      {
        domain: '{{fapi_url}}',
        applicationID: 'convex',
      },
    ],
  }
  ```

  ## Deploy your changes to Convex

  Run `npx convex dev` to automatically sync your configuration to your backend.

  ## Add the Clerk Convex SDK to your app

  
    Add the `clerk-convex-kotlin` dependency to your app:

    ```kotlin
// Filename: app/build.gradle.kts

    dependencies {
        implementation("com.clerk:clerk-convex-kotlin:<latest-version>")
    }
    ```

    Initialize Clerk first with your Clerk Publishable Key, then create a `ConvexClientWithAuth` using `ClerkConvexAuthProvider().createConvexClientWithAuth()`, passing in your Convex deployment URL. Refer to the [Convex deployment docs](https://docs.convex.dev/dashboard/deployments/deployment-settings) for more info.

    ```kotlin
// Filename: MyApplication.kt

    import android.app.Application
    import com.clerk.api.Clerk
    import com.clerk.convex.ClerkConvexAuthProvider
    import com.clerk.convex.createConvexClientWithAuth

    class MyApplication : Application() {
      private val authProvider = ClerkConvexAuthProvider()

      override fun onCreate() {
        super.onCreate()
        Clerk.initialize(
          context = this,
          publishableKey = "{{pub_key}}",
        )

        val convex = authProvider.createConvexClientWithAuth(
          deploymentUrl = "YOUR_CONVEX_DEPLOYMENT_URL",
          context = applicationContext,
        )

        // Store `convex` in app state (for example, a repository or DI container).
      }
    }
    ```

    After users authenticate with Clerk, auth state is automatically synced to Convex. Use `convex` for queries, mutations, actions, and auth state. If you don't need to keep an auth provider instance, `createClerkConvexClient()` is available as a shorthand helper.
  

  
    Add `clerk-convex-swift` via Swift Package Manager to your app:

    ```swift
// Filename: Package.swift

    dependencies: [
      .package(url: "https://github.com/clerk/clerk-convex-swift", from: "0.1.0")
    ]

    targets: [
      .target(
        name: "YourApp",
        dependencies: [
          .product(name: "ClerkConvex", package: "clerk-convex-swift")
        ]
      )
    ]
    ```

    Configure Clerk first with your Clerk Publishable Key, then initialize `ConvexClientWithAuth` with `ClerkConvexAuthProvider` using your Convex deployment URL. Refer to the [Convex deployment docs](https://docs.convex.dev/dashboard/deployments/deployment-settings) for more info.

    ```swift
// Filename: MyApp.swift

    import ClerkConvex
    import ClerkKit
    import ConvexMobile
    import SwiftUI

    @MainActor
    let client = ConvexClientWithAuth(
      deploymentUrl: "YOUR_CONVEX_DEPLOYMENT_URL",
      authProvider: ClerkConvexAuthProvider()
    )

    @main
    struct MyApp: App {
      init() {
        Clerk.configure(publishableKey: "{{pub_key}}")
      }

      var body: some Scene {
        WindowGroup {
          ContentView()
            .environment(Clerk.shared)
        }
      }
    }
    ```

    After users authenticate with Clerk, auth state is automatically synced to Convex. Use `client` for subscriptions, mutations, actions, and auth state.
  

  ## Show UI based on auth state

  Convex exposes auth state from the authenticated client. Use that state to render loading, signed-out, and signed-in UI.

  
    ```kotlin
// Filename: AuthViewModel.kt

    import androidx.lifecycle.ViewModel
    import androidx.lifecycle.viewModelScope
    import dev.convex.android.AuthState
    import dev.convex.android.ConvexClientWithAuth
    import kotlinx.coroutines.launch

    class AuthViewModel(
      private val convex: ConvexClientWithAuth,
    ) : ViewModel() {
      init {
        viewModelScope.launch {
          convex.authState.collect { authState ->
            when (authState) {
              is AuthState.AuthLoading -> showLoading()
              is AuthState.Unauthenticated -> showSignIn()
              is AuthState.Authenticated -> showAuthenticatedContent()
            }
          }
        }
      }
    }
    ```

    Collect `convex.authState` in your `ViewModel` and map each state to the appropriate screen.
  

  
    ```swift
// Filename: ContentView.swift

    import ConvexMobile
    import SwiftUI

    struct ContentView: View {
      @State private var authState: AuthState = .loading

      var body: some View {
        Group {
          switch authState {
          case .loading:
            ProgressView()
          case .unauthenticated:
            Text("Unauthenticated")
          case .authenticated:
            AuthenticatedView()
          }
        }
        .task {
          for await state in client.authState.values {
            authState = state
          }
        }
      }
    }
    ```
  

  ## Make requests and present data in the UI

  With Clerk and Convex configured, authenticated requests stay in sync so you can subscribe and render data with minimal setup.

  
    ```kotlin
// Filename: MessagesViewModel.kt

    import androidx.lifecycle.ViewModel
    import androidx.lifecycle.viewModelScope
    import dev.convex.android.ConvexClientWithAuth
    import kotlinx.coroutines.flow.SharingStarted
    import kotlinx.coroutines.flow.StateFlow
    import kotlinx.coroutines.flow.catch
    import kotlinx.coroutines.flow.stateIn

    class MessagesViewModel(
      convex: ConvexClientWithAuth,
    ) : ViewModel() {

      val messages: StateFlow> =
        convex
          .subscribe>("messages:list")
          .catch { emit(emptyList()) } // keep old behavior: fail -> show nothing
          .stateIn(
            scope = viewModelScope,
            started = SharingStarted.WhileSubscribed(stopTimeoutMillis = 5_000),
            initialValue = emptyList()
          )
    }
    ```

    ```kotlin
// Filename: MessagesScreen.kt

    import androidx.compose.foundation.layout.Column
    import androidx.compose.foundation.layout.PaddingValues
    import androidx.compose.foundation.layout.fillMaxWidth
    import androidx.compose.foundation.layout.padding
    import androidx.compose.foundation.lazy.LazyColumn
    import androidx.compose.foundation.lazy.items
    import androidx.compose.material3.Text
    import androidx.compose.runtime.Composable
    import androidx.compose.ui.Modifier
    import androidx.compose.ui.unit.dp
    import androidx.lifecycle.compose.collectAsStateWithLifecycle

    @Composable
    fun MessagesScreen(
      viewModel: MessagesViewModel,
      modifier: Modifier = Modifier,
    ) {
      val messages = viewModel.messages.collectAsStateWithLifecycle().value

      LazyColumn(
        modifier = modifier,
        contentPadding = PaddingValues(12.dp),
      ) {
        items(items = messages, key = { it.id }) { message ->
          Column(Modifier.fillMaxWidth().padding(vertical = 6.dp)) {
            Text(message.author)
            Text(message.body)
          }
        }
      }
    }

    data class Message(
      val id: String,
      val author: String,
      val body: String,
    )
    ```
  

  
    ```swift
// Filename: AuthenticatedView.swift

    import ConvexMobile
    import SwiftUI

    struct AuthenticatedView: View {
      @State private var messages: [Message] = []

      var body: some View {
        List(messages) { message in
          VStack(alignment: .leading) {
            Text(message.author)
            Text(message.body)
          }
        }
        .task {
          let publisher = client
            .subscribe(to: "messages:list")
            .replaceError(with: [Message]())

          for await latest in publisher.values {
            messages = latest
          }
        }
      }
    }

    struct Message: Identifiable, Codable {
      let id: String
      let author: String
      let body: String
    }
    ```
  


## Next steps

For more information on how to use Convex with Clerk, see the [Convex docs](https://docs.convex.dev/auth/clerk).
