# Clerk Next.js SDK


> The Clerk Next.js SDK gives you access to prebuilt components, React hooks, and helpers to make user authentication easier.

The Clerk Next.js SDK gives you access to prebuilt components, React hooks, and helpers to make user authentication easier. Refer to the [quickstart guide](/nextjs/getting-started/quickstart) to get started.

## `clerkMiddleware()`

The `clerkMiddleware()` helper integrates Clerk authentication into your Next.js application through middleware. It allows you to integrate authorization into both the client and server of your application. You can learn more [here](/reference/nextjs/clerk-middleware).

## Client-side helpers

Because the Next.js SDK is built on top of the Clerk React SDK, you can use the hooks that the React SDK provides. These hooks include access to the [`Clerk`](/reference/javascript/clerk) object, [`User` object](/reference/javascript/user), [`Organization` object](/reference/javascript/organization), and a set of useful helper methods for signing in and signing up.

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

### App router

Clerk provides first-class support for the [Next.js App Router](https://nextjs.org/docs/app). The following references show how to integrate Clerk features into apps using the latest App Router and React Server Components features.

- [`auth()`](/reference/nextjs/app-router/auth)
- [`currentUser()`](/reference/nextjs/app-router/current-user)
- [Route Handlers](/reference/nextjs/app-router/route-handlers)
- [Server Actions](/reference/nextjs/app-router/server-actions)

### Pages router

Clerk continues to provide drop-in support for the Next.js Pages Router. In addition to the main Clerk integration, the following references are available for apps using Pages Router.

- [`getAuth()`](/reference/nextjs/pages-router/get-auth)
- [`buildClerkProps()`](/reference/nextjs/pages-router/build-clerk-props)

## `clerkClient`

[Clerk's JS Backend SDK](/js-backend/getting-started/quickstart) is a wrapper around the [Backend API](/reference/backend-api) that makes it easier to interact with the API. For example, to retrieve a list of all users in your application, you can use the `users.getUserList()` method from the JS Backend SDK instead of manually making a fetch request to the `https://api.clerk.com/v1/users` endpoint.

To access a resource, you must first instantiate a `clerkClient` instance. See the [reference documentation](/js-backend/getting-started/quickstart) for more information.

## `Auth` object

Both `auth()` (App Router) and `getAuth()` (Pages Router) return an `Auth` object. This JavaScript object contains important information like the current user's session ID, user ID, and Organization ID. Learn more about the [`Auth` object](/reference/backend/types/auth-object).

## Demo repositories

For examples of Clerk's features, such as user and Organization management, integrated into a single application, see the Next.js demo repositories:

- [Clerk + Next.js App Router Demo](https://github.com/clerk/clerk-nextjs-demo-app-router)
- [Clerk + Next.js Pages Router Demo](https://github.com/clerk/clerk-nextjs-demo-pages-router)
