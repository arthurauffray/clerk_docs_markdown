# UserButton


> Clerk's UserButton renders a circular button that displays the current user's profile image and opens the user profile when tapped.

![The UserButton is a circular button that displays the signed-in user's profile image.](/images/ui-components/ios-user-button.png)


  ![The UserButton is a circular button that displays the signed-in user's profile image.](/images/ui-components/android-user-button.png)


The `UserButton` is a circular button that displays the user's profile image. When tapped, it presents a sheet with the [`UserProfileView`](/reference/views/user/user-profile-view).


  > [!IMPORTANT]
  > When a user is signed out, the `UserButton` renders the `signedOutContent` you provide. If you don't provide any, it renders nothing.

  ## Parameters

  - **`signedOutContent`** `@ViewBuilder () -> SignedOutContent`

  A view builder that renders when no user is signed in. Defaults to `EmptyView`, which renders nothing.


  ## Parameters

  - **`clerkTheme`** `ClerkTheme`

  The theme to apply to the `UserButton`. This will override any theme applied to the `UserButton`'s parent view, or configured in the `Clerk` global object.


## Usage

The following examples show how to use the `UserButton` in your app.

### Basic usage


  ```swift
  import SwiftUI
  import ClerkKit
  import ClerkKitUI

  struct HomeView: View {
    @State private var authViewIsPresented = false

    var body: some View {
      VStack {
        UserButton(signedOutContent: {
          Button("Sign in") {
            authViewIsPresented = true
          }
        })
      }
      .prefetchClerkImages()
      .sheet(isPresented: $authViewIsPresented) {
        AuthView()
      }
    }
  }
  ```


  ```kotlin
  import androidx.compose.runtime.Composable
  import androidx.compose.runtime.getValue
  import androidx.lifecycle.compose.collectAsStateWithLifecycle
  import com.clerk.api.Clerk
  import com.clerk.ui.userbutton.UserButton

  @Composable
  fun HomeScreen() {
      val user by Clerk.userFlow.collectAsStateWithLifecycle()
      if (user != null) {
          UserButton()
      }
  }
  ```


### In a navigation toolbar


  ```swift
  import SwiftUI
  import ClerkKit
  import ClerkKitUI

  struct ContentView: View {
    @State private var authViewIsPresented = false

    var body: some View {
      NavigationView {
        VStack {
          Text("Welcome!")
        }
        .toolbar {
          ToolbarItem(placement: .navigationBarTrailing) {
            UserButton(signedOutContent: {
              Button("Sign in") {
                authViewIsPresented = true
              }
            })
          }
        }
      }
      .prefetchClerkImages()
      .sheet(isPresented: $authViewIsPresented) {
        AuthView()
      }
    }
  }
  ```


  ```kotlin
  import androidx.compose.material3.ExperimentalMaterial3Api
  import androidx.compose.material3.Scaffold
  import androidx.compose.material3.Text
  import androidx.compose.material3.TopAppBar
  import androidx.compose.runtime.Composable
  import androidx.compose.runtime.getValue
  import androidx.lifecycle.compose.collectAsStateWithLifecycle
  import com.clerk.api.Clerk
  import com.clerk.ui.userbutton.UserButton


  @OptIn(ExperimentalMaterial3Api::class)
  @Composable
  fun UserProfileTopBar() {
      val user by Clerk.userFlow.collectAsStateWithLifecycle()
      Scaffold(
          topBar = {
              TopAppBar(title = { Text("Home screen") }, actions = { user?.let { UserButton() } })
          }
      ) {
          // Content goes here
      }
  }
  ```


## Customization

To learn how to customize Clerk views, see the [dedicated guide](/guides/customizing-clerk/clerk-theme).

If Clerk's prebuilt views don't meet your specific needs or if you require more control over the logic, you can rebuild the existing Clerk flows using the Clerk API. For more information, see the [custom flow guides](/guides/development/custom-flows/overview).
