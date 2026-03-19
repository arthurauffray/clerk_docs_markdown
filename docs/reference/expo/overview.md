# Clerk Expo SDK


> The Clerk Expo SDK gives you access to prebuilt components, React hooks, and helpers to make user authentication easier.

The Clerk Expo SDK gives you access to prebuilt components, React hooks, and helpers to make user authentication easier. Refer to the [quickstart guide](/expo/getting-started/quickstart) to get started.

## Available resources

The Expo SDK supports [three approaches to authentication](/getting-started/quickstart), each with its own set of resources:

### Components

#### Native components

> [!WARNING]
> Expo native components are currently in beta. If you run into any issues, please reach out to our [support team](https://clerk.com/support).


Pre-built native components rendered with **SwiftUI** on iOS and **Jetpack Compose** on Android. These components require a [development build](https://docs.expo.dev/develop/development-builds/introduction/).

- [``](/reference/expo/native-components/auth-view) - Renders a full authentication interface, supporting multiple sign-up and sign-in methods, multi-factor authentication (MFA), and password recovery flows.
- [``](/reference/expo/native-components/user-button) - Displays the signed-in user's profile image.
- [``](/reference/expo/native-components/user-profile-view) - Renders a complete user profile interface with personal information, security settings, account switching, and sign-out options.

See the [native components overview](/reference/expo/native-components/overview) for more details.

#### Control components

These components work across all approaches:

- [``](/reference/components/control/show) - Conditionally render content based on auth state
- [``](/reference/components/control/clerk-loaded) - Render children after Clerk loads
- [``](/reference/components/control/clerk-loading) - Render children while Clerk loads

#### Web components

All Clerk components are available from `@clerk/expo/web` for Expo web projects. See [the component docs](/reference/components/overview) for more information.

### Hooks

#### Native sign-in hooks

Hooks for native OAuth authentication without browser redirects. These hooks require a [development build](https://docs.expo.dev/develop/development-builds/introduction/).

- [`useSignInWithApple()`](/reference/expo/native-hooks/use-sign-in-with-apple) - Native Sign in with Apple (iOS only)
- [`useSignInWithGoogle()`](/reference/expo/native-hooks/use-sign-in-with-google) - Native Sign in with Google (iOS and Android)
- [`useSSO()`](/reference/expo/native-hooks/use-sso) - Browser-based SSO and OAuth flows

#### Expo-specific hooks

Hooks designed specifically for Expo environments. These provide additional authentication capabilities, such as biometric credential management and browser-based OAuth flows.

- [`useLocalCredentials()`](/reference/expo/native-hooks/use-local-credentials) - Biometric credential management
- [`useOAuth()`](/reference/expo/native-hooks/use-oauth) - Browser-based OAuth flows

#### React hooks

Because the Expo SDK is built on top of the Clerk React SDK, you can use the hooks that the React SDK provides. These hooks include access to the [`Clerk`](/reference/javascript/clerk) object, [`User` object](/reference/javascript/user), [`Organization` object](/reference/javascript/organization), and a set of useful helper methods for signing in and signing up.

- [`useUser()`](/reference/hooks/use-user)
- [`useClerk()`](/reference/hooks/use-clerk)
- [`useAuth()`](/reference/hooks/use-auth)
- [`useSignIn()`](/reference/hooks/use-sign-in)
- [`useSignUp()`](/reference/hooks/use-sign-up)
- [`useWaitlist()`](/reference/hooks/use-waitlist)
- [`useSession()`](/reference/hooks/use-session)
- [`useSessionList()`](/reference/hooks/use-session-list)
- [`useOrganization()`](/reference/hooks/use-organization)
- [`useOrganizationList()`](/reference/hooks/use-organization-list)
- [`useOrganizationCreationDefaults()`](/reference/hooks/use-organization-creation-defaults)
- [`useReverification()`](/reference/hooks/use-reverification)
- [`useCheckout()`](/reference/hooks/use-checkout)
- [`usePaymentElement()`](/reference/hooks/use-payment-element)
- [`usePaymentMethods()`](/reference/hooks/use-payment-methods)
- [`usePlans()`](/reference/hooks/use-plans)
- [`useSubscription()`](/reference/hooks/use-subscription)
- [`usePaymentAttempts()`](/reference/hooks/use-payment-attempts)
- [`useStatements()`](/reference/hooks/use-statements)


## Custom flows

Clerk provides prebuilt components for **native** applications and **web** applications. Use the components that correspond to your platform:

- For native apps, see the [native components](/reference/expo/native-components/overview).
- For web apps, see the [web components](/reference/components/overview).

If the prebuilt components don't meet your needs, you can build [custom flows](/guides/development/custom-flows/overview) using the Clerk API.

## Configure passkeys

To configure passkeys for your Expo app, see the [passkeys configuration guide](/reference/expo/passkeys).

## Deploy your app

To learn how to deploy your Expo application, see the [dedicated guide](/guides/development/deployment/expo).
