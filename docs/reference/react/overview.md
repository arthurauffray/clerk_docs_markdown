# Clerk React SDK


> The Clerk React SDK gives you access to prebuilt components, React hooks, and helpers to make user authentication easier.

The Clerk React SDK is built on top of the [JavaScript SDK](/reference/javascript/overview) and gives you access to prebuilt components, hooks, and helpers to make user authentication easier. Refer to the [quickstart guide](/react/getting-started/quickstart) to get started.

## Custom hooks

The React SDK provides hooks that include access to the [`Clerk`](/reference/javascript/clerk) object, [`User` object](/reference/javascript/user), [`Organization` object](/reference/javascript/organization), and a set of useful helper methods for signing in and signing up.

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


## Framework-specific SDKs

> [!IMPORTANT]
> Clerk provides optimized SDKs for specific React frameworks. If you're using one of the supported frameworks below, you should use its dedicated SDK instead of `@clerk/react`.

Clerk offers framework-specific SDKs that are customized to provide the better developer experience and integration with each framework's features. Choose the appropriate SDK based on your framework:

| Framework | Package | Docs |
| - | - | - |
| Next.js | `@clerk/nextjs` | [Next.js SDK](/reference/nextjs/overview) |
| React Router | `@clerk/react-router` | [React Router SDK](/reference/react-router/overview) |
| Astro | `@clerk/astro` | [Astro SDK](/reference/astro/overview) |
| TanStack React Start | `@clerk/tanstack-react-start` | [TanStack React Start SDK](/reference/tanstack-react-start/overview) |

## Set up Clerk React

Before you can add Clerk to your React application, you must create a Clerk app in the Clerk Dashboard. To get started, follow the [setup guide](/getting-started/quickstart/setup-clerk). Then, follow the [quickstart guide](/react/getting-started/quickstart) to set up the React SDK in your app.
