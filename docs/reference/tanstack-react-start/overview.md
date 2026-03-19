# Clerk TanStack React Start SDK


> The Clerk TanStack React Start SDK gives you access to prebuilt components, React hooks, and helpers to make user authentication easier.

The Clerk TanStack React Start SDK gives you access to prebuilt components, React hooks, and helpers to make user authentication easier. Refer to the [quickstart guide](/tanstack-react-start/getting-started/quickstart) to get started.

## Client-side helpers

Because the TanStack React Start SDK is built on top of the React SDK, you can use the hooks that the React SDK provides. These hooks include access to the [`Clerk`](/reference/javascript/clerk) object, [`User` object](/reference/javascript/user), [`Organization` object](/reference/javascript/organization), and a set of useful helper methods for signing in and signing up. Learn more in the [Clerk React SDK reference](/reference/react/overview).

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

The following references show how to integrate Clerk features into applications using TanStack React Start server functions and API routes.

- [`auth()`](/reference/tanstack-react-start/auth)
- [`clerkMiddleware()`](/reference/tanstack-react-start/clerk-middleware)

### `Auth` object

The `auth()` returns an `Auth` object. This JavaScript object contains important information like session data, your user's ID, as well as their Organization ID. Learn more about the `Auth` object [here](/reference/backend/types/auth-object).
