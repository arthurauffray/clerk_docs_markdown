# Clerk Remix SDK


> The Clerk Remix SDK gives you access to prebuilt components, React hooks, and helpers to make user authentication easier.

> [!WARNING]
> The Remix SDK is in maintenance mode and will only receive security updates. Please migrate to the [React Router SDK](/react-router/getting-started/quickstart) for continued development and new features.


The Clerk Remix SDK gives you access to prebuilt components, React hooks, and helpers to make user authentication easier. Refer to the [quickstart guide](/remix/getting-started/quickstart) to get started.

## `ClerkApp`

The `ClerkApp` component is a wrapper that provides Clerk's authentication state to your React tree. It is required to configure Clerk in your Remix application. Learn more in the [reference](/reference/remix/clerk-app).

## `rootAuthLoader()`

The `rootAuthLoader()` function is a helper function that provides the authentication state to your Remix application. It is required to configure Clerk in your Remix application. Learn more in the [reference](/reference/remix/root-auth-loader).

## Client-side helpers

Because the Remix SDK is built on top of the Clerk React SDK, you can use the hooks that the React SDK provides. These hooks include access to the [`Clerk`](/reference/javascript/clerk) object, [`User` object](/reference/javascript/user), [`Organization` object](/reference/javascript/organization), and a set of useful helper methods for signing in and signing up.

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


## Server-side helpers

### `getAuth()`

The `getAuth()` helper retrieves authentication state from the request object. Returns the [`Auth`](/reference/backend/types/auth-object) object. Accepts the following parameters:

- **`args`**

  The arguments object.

    ---

- **`opts?`**

  An optional object that can be used to configure the behavior of the `getAuth()` function. It accepts the following properties:

- **`secretKey?`: A string that represents the Secret Key used to sign the session token. If not provided, the Secret Key is retrieved from the environment variable `CLERK_SECRET_KEY`.**


See the [dedicated guide](/remix/guides/users/reading#server-side) for example usage.

## SPA mode

Clerk supports [Remix in SPA mode](https://remix.run/docs/en/main/guides/spa-mode) out-of-the-box. Learn more in the [tutorial](/guides/development/spa-mode).
