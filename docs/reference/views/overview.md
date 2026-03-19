# View Reference


> A list of Clerk's comprehensive suite of views designed to seamlessly integrate authentication and multi-tenancy into your application.

Clerk offers a comprehensive suite of views designed to seamlessly integrate authentication and multi-tenancy into your application. With Clerk views, you can easily customize the appearance of authentication views and pages, manage the entire authentication flow to suit your specific needs, and even build robust SaaS applications.

## Clerk views

- [`AuthView`](/reference/views/authentication/auth-view) - Renders a full authentication interface, supporting multiple sign-up and sign-in methods, multi-factor authentication (MFA), and password recovery flows.
- [`UserButton`](/reference/views/user/user-button) - Displays the signed-in user's profile image.
- [`UserProfileView`](/reference/views/user/user-profile-view) - Renders a complete user profile interface with personal information, security settings, account switching, and sign-out options.


  ## Installation

  The Clerk Android SDK is now split into two packages:

  - `com.clerk:clerk-android-api` - The core Clerk SDK for authentication and user management.
  - `com.clerk:clerk-android-ui` - The Clerk UI components for authentication and user management.

  The `com.clerk:clerk-android-ui` pulls the `com.clerk:clerk-android-api` package as a dependency, so you only need to add the `com.clerk:clerk-android-ui` package to your dependencies if you're using Clerk's UI components.

  ```gradle
  dependencies {
      // Only if you're using the Clerk API without the Clerk UI components
      implementation("com.clerk:clerk-android-api:<latest-version>")
      
      implementation("com.clerk:clerk-android-ui:<latest-version>")
  }
  ```

  You can find the latest version of the Clerk Android SDK on the [GitHub release page](https://github.com/clerk/clerk-android/releases).


## Customization

To learn how to customize Clerk views, see the [dedicated guide](/guides/customizing-clerk/clerk-theme).

If Clerk's prebuilt views don't meet your specific needs or if you require more control over the logic, you can rebuild the existing Clerk flows using the Clerk API. For more information, see the [custom flow guides](/guides/development/custom-flows/overview).


### Secured by Clerk branding

> [!WARNING]
> This feature requires a [paid plan](/pricing) for production use, but all features are free to use in development mode so that you can try out what works for you. See the [pricing](/pricing) page for more information.


By default, Clerk displays a **Secured by Clerk** badge on Clerk views. You can remove this branding by following these steps:

1. In the Clerk Dashboard, navigate to your application's [**Settings**](https://dashboard.clerk.com/~/settings).
1. Under **Branding**, toggle on the **Remove "Secured by Clerk" branding** option.


  - [Join our Discord](https://clerk.com/discord 'Join Discord')
  - Join our official Discord server to chat with us directly and become a part of the Clerk community.
  - 

  ---

  - [Need help?](/support 'Get help')
  - Contact us through Discord, Twitter, or email to receive answers to your questions and learn more about Clerk.
  -
