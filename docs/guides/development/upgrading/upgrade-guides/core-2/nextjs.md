# Upgrading `@clerk/nextjs` to Core 2


> Learn how to upgrade Clerk's Next.js SDK to the latest version.

Core 2 is included in the Next.js SDK starting with version 5.0.0. This new version ships with an improved design and UX for its built-in components, no "flash of white page" when authenticating, a substantially improved middleware import, and a variety of smaller DX improvements and housekeeping items. Each of the potentially breaking changes are detailed in this guide, below.

By the end of this guide, you’ll have successfully upgraded your Next.js project to use `@clerk/nextjs` v5. You’ll learn how to update your dependencies, resolve breaking changes, and find deprecations. Step-by-step instructions will lead you through the process.

## Preparing to upgrade

Before upgrading, it's highly recommended that you update your Clerk SDKs to the latest Core 1 version (`npm i @clerk/nextjs@4`). Some changes required for Core 2 SDKs can be applied incrementally to the v5 release, which should contribute to a smoother upgrading experience. After updating, look out for deprecation messages in your terminal and browser console. By resolving these deprecations you'll be able to skip many breaking changes from Core 2.

Additionally, some of the minimum version requirements for some base dependencies have been updated such that versions that are no longer supported or are at end-of-life are no longer guaranteed to work correctly with Clerk.

**Updating Node.js**

You need to have Node.js `18.17.0` or later installed. Last year, Node.js 16 entered EOL (End of life) status, so support for this version has been removed across Clerk SDKs. You can check your Node.js version by running `node -v` in your terminal. Learn more about how to [update and install Node.js](https://nodejs.org/en/learn/getting-started/how-to-install-nodejs).

**Updating React**

All react-dependent Clerk SDKs now require you to use React 18 or higher. You can update your project by installing the latest version of `react` and `react-dom`.

```npm
npm install react@latest react-dom@latest
```

If you are upgrading from React 17 or lower, make sure to [learn about how to upgrade your React version to 18](https://react.dev/blog/2022/03/08/react-18-upgrade-guide) as well.

**Updating Next.js**

`@clerk/nextjs` now requires you to use Next.js version `13.0.4` or later. See Next's upgrade guides for more guidance if you have not yet upgraded to Next.js 13:

- [Upgrading from 12 to 13](https://nextjs.org/docs/pages/building-your-application/upgrading/version-13)
- [Upgrading from 13 to 14](https://nextjs.org/docs/app/building-your-application/upgrading/version-14)

## Updating to Core 2

Whenever you feel ready, go ahead and install the latest version of any Clerk SDKs you are using. Make sure that you are prepared to patch some breaking changes before your app will work properly, however. The commands below demonstrate how to install the latest version.

```npm
npm install @clerk/nextjs
```

## CLI upgrade helper

Clerk now provides a `@clerk/upgrade` CLI tool that you can use to ease the upgrade process. The tool will scan your codebase and produce a list of changes you'll need to apply to your project. It should catch the vast majority of the changes needed for a successful upgrade to any SDK including Core 2. This can save you a lot of time reading through changes that don't apply to your project.

To run the CLI tool, navigate to your project and run it in the terminal:

```npm
npx @clerk/upgrade --from=core-1
```

If you are having trouble with `npx`, it's also possible to install directly with `npm i @clerk/upgrade -g`, and can then be run with the `clerk-upgrade` command.

## Breaking Changes

### Component design adjustments

The new version ships with improved design and UX across all of Clerk's [UI components](/reference/components/overview). If you have used the [`appearance` prop](/guides/customizing-clerk/appearance-prop/overview) or tokens for a [custom theme](/guides/customizing-clerk/appearance-prop/overview), you will likely need to make some adjustments to ensure your styling is still looking great. If you're using the [localization prop](/guides/customizing-clerk/localization) you will likely need to make adjustments to account for added or removed localization keys.

[More detail on these changes »](/guides/development/upgrading/upgrade-guides/core-2#component-redesign)

### New Middleware architecture

User and customer feedback about `authMiddleware()` has been clear in that Middleware logic was a often friction point. As such, in v5 you will find a completely new Middleware helper called [`clerkMiddleware()`](/reference/nextjs/clerk-middleware) that should alleviate the issues folks had with `authMiddleware()`.

The primary change from the previous `authMiddleware()` is that `clerkMiddleware()` does not protect any routes by default, instead requiring the developer to add routes they would like to be protected by auth. This is a substantial contrast to the previous `authMiddleware()`, which protected all routes by default, requiring the developer to add exceptions. The API was also substantially simplified, and it has become easier to combine with other Middleware helpers smoothly as well.

Here's an example that demonstrates route protection based on both authentication and authorization:

```ts
// Filename: middleware.ts

import { clerkMiddleware, createRouteMatcher } from '@clerk/nextjs/server'

const isDashboardRoute = createRouteMatcher(['/dashboard(.*)'])
const isAdminRoute = createRouteMatcher(['/admin(.*)'])

export default clerkMiddleware(async (auth, req) => {
  // Restrict admin route to users with specific Role
  if (isAdminRoute(req)) await auth.protect({ role: 'org:admin' })

  // Restrict dashboard routes to signed in users
  if (isDashboardRoute(req)) await auth.protect()
})

export const config = {
  matcher: [
    // Skip Next.js internals and all static files, unless found in search params
    '/((?!_next|[^?]*\\.(?:html?|css|js(?!on)|jpe?g|webp|png|gif|svg|ttf|woff2?|ico|csv|docx?|xlsx?|zip|webmanifest)).*)',
    // Always run for API routes
    '/(api|trpc)(.*)',
  ],
}
```

A couple things to note here:

- The `createRouteMatcher` helper makes it easy to define route groups that you can leverage inside the Middleware function and check in whichever order you'd like. Note that it can take an array of routes as well.
- With `clerkMiddleware`, you're defining the routes you want **to be protected**, rather than the routes you don't want to be protected.
- The `auth.protect()` helper is used extensively here. See its [reference doc](/reference/nextjs/app-router/auth#auth-protect) for more info.

See the [`clerkMiddleware()`](/reference/nextjs/clerk-middleware) docs for more information and detailed usage examples.

#### Migrating to `clerkMiddleware()`

Clerk strongly recommends migrating to the new `clerkMiddleware()` for an improved DX and access to all present and upcoming features. However, `authMiddleware()`, while deprecated, will continue to work in v5 and will not be removed until the next major version, so you do not _need_ to make any changes to your Middleware setup this version.

The most basic migration will be updating the import and changing out the default export, then mirroring the previous behavior of protecting all routes except `/sign-in` or `/sign-up` by doing the following:

```js

import { authMiddleware } from '@clerk/nextjs/server'
import { clerkMiddleware, createRouteMatcher } from '@clerk/nextjs/server'

const isPublicRoute = createRouteMatcher(['/sign-in(.*)', '/sign-up(.*)'])

export default authMiddleware()
export default clerkMiddleware(async (auth, request) => {
  if (!isPublicRoute(request)) {
    await auth.protect()
  }
})

export const config = {
  matcher: ['/((?!.*\\..*|_next).*)', '/', '/(api|trpc)(.*)'],
}
```

Of course, in most cases you'll have a more complicated setup than this. You can find some examples below for how to migrate a few common use cases. Be sure to review the [`clerkMiddleware()` documentation](/reference/nextjs/clerk-middleware) if your specific use case is not mentioned.


  
**Details**

By default, `clerkMiddleware()` treats all pages as public unless explicitly protected. If you prefer for it to operate the other way around (all pages are protected unless explicitly made public), you can reverse the middleware logic in this way:

    Before:

    ```ts
// Filename: middleware.ts

    import { authMiddleware } from '@clerk/nextjs/server'

    export default authMiddleware({
      publicRoutes: ['/', '/contact'],
    })

    export const config = {
      matcher: [
        // Skip Next.js internals and all static files, unless found in search params
        '/((?!_next|[^?]*\\.(?:html?|css|js(?!on)|jpe?g|webp|png|gif|svg|ttf|woff2?|ico|csv|docx?|xlsx?|zip|webmanifest)).*)',
        // Always run for API routes
        '/(api|trpc)(.*)',
      ],
    }
    ```

    After:

    ```ts
// Filename: middleware.ts

    import { clerkMiddleware, createRouteMatcher } from '@clerk/nextjs/server'

    const isPublicRoute = createRouteMatcher(['/', '/contact(.*)'])

    export default clerkMiddleware(async (auth, req) => {
      if (isPublicRoute(req)) return // if it's a public route, do nothing
      await auth.protect() // for any other route, require auth
    })

    export const config = {
      matcher: [
        // Skip Next.js internals and all static files, unless found in search params
        '/((?!_next|[^?]*\\.(?:html?|css|js(?!on)|jpe?g|webp|png|gif|svg|ttf|woff2?|ico|csv|docx?|xlsx?|zip|webmanifest)).*)',
        // Always run for API routes
        '/(api|trpc)(.*)',
      ],
    }
    ```


  
**Details**

An example can be seen below of code that ensures that all routes are public except everything under `/dashboard`.

    Before:

    ```ts
// Filename: middleware.ts

    import { authMiddleware } from '@clerk/nextjs/server'

    export default authMiddleware({
      publicRoutes: (req) => !req.url.includes('/dashboard'),
    })

    export const config = {
      matcher: [
        // Skip Next.js internals and all static files, unless found in search params
        '/((?!_next|[^?]*\\.(?:html?|css|js(?!on)|jpe?g|webp|png|gif|svg|ttf|woff2?|ico|csv|docx?|xlsx?|zip|webmanifest)).*)',
        // Always run for API routes
        '/(api|trpc)(.*)',
      ],
    }
    ```

    After:

    ```ts
// Filename: middleware.ts

    import { clerkMiddleware, createRouteMatcher } from '@clerk/nextjs/server'

    const isDashboardRoute = createRouteMatcher(['/dashboard(.*)'])

    export default clerkMiddleware(async (auth, request) => {
      if (isDashboardRoute(request)) await auth.protect()
    })

    export const config = {
      matcher: [
        // Skip Next.js internals and all static files, unless found in search params
        '/((?!_next|[^?]*\\.(?:html?|css|js(?!on)|jpe?g|webp|png|gif|svg|ttf|woff2?|ico|csv|docx?|xlsx?|zip|webmanifest)).*)',
        // Always run for API routes
        '/(api|trpc)(.*)',
      ],
    }
    ```


  
**Details**

You can call other Middlewares inside `clerkMiddleware()`, giving you more direct control over what is called where. An example would be [next-intl](https://next-intl-docs.vercel.app/) to add internationalization to your app.

    Before:

    ```ts
// Filename: middleware.ts

    import { authMiddleware } from '@clerk/nextjs/server'
    import createMiddleware from 'next-intl/middleware'

    const intlMiddleware = createMiddleware({
      locales: ['en', 'de'],
      defaultLocale: 'en',
    })

    export default authMiddleware({
      beforeAuth: (req) => {
        return intlMiddleware(req)
      },
      publicRoutes: ['((?!^/dashboard/).*)'],
    })

    export const config = {
      matcher: [
        // Skip Next.js internals and all static files, unless found in search params
        '/((?!_next|[^?]*\\.(?:html?|css|js(?!on)|jpe?g|webp|png|gif|svg|ttf|woff2?|ico|csv|docx?|xlsx?|zip|webmanifest)).*)',
        // Always run for API routes
        '/(api|trpc)(.*)',
      ],
    }
    ```

    After:

    ```ts
// Filename: middleware.ts

    import { clerkMiddleware, createRouteMatcher } from '@clerk/nextjs/server'
    import createMiddleware from 'next-intl/middleware'

    const intlMiddleware = createMiddleware({
      locales: ['en', 'de'],
      defaultLocale: 'en',
    })

    const isDashboardRoute = createRouteMatcher(['/dashboard(.*)'])

    export default clerkMiddleware(async (auth, request) => {
      if (isDashboardRoute(request)) await auth.protect()

      return intlMiddleware(request)
    })

    export const config = {
      matcher: [
        // Skip Next.js internals and all static files, unless found in search params
        '/((?!_next|[^?]*\\.(?:html?|css|js(?!on)|jpe?g|webp|png|gif|svg|ttf|woff2?|ico|csv|docx?|xlsx?|zip|webmanifest)).*)',
        // Always run for API routes
        '/(api|trpc)(.*)',
      ],
    }
    ```


  
**Details**

You can now access `redirectToSignIn` from the `auth()` object, rather than importing at the top level.

    Before:

    ```ts
// Filename: middleware.ts

    import { authMiddleware, redirectToSignIn } from "@clerk/nextjs/server"

    export default authMiddleware({
      if (someCondition) redirectToSignIn()
    })

    export const config = {
      matcher: [
        // Skip Next.js internals and all static files, unless found in search params
        '/((?!_next|[^?]*\\.(?:html?|css|js(?!on)|jpe?g|webp|png|gif|svg|ttf|woff2?|ico|csv|docx?|xlsx?|zip|webmanifest)).*)',
        // Always run for API routes
        '/(api|trpc)(.*)',
      ],
    };
    ```

    After:

    ```ts
// Filename: middleware.ts

    import { clerkMiddleware } from '@clerk/nextjs/server'

    export default clerkMiddleware(async (auth, req) => {
      const { redirectToSignIn } = await auth()
      if (someCondition) redirectToSignIn()
    })

    export const config = {
      matcher: [
        // Skip Next.js internals and all static files, unless found in search params
        '/((?!_next|[^?]*\\.(?:html?|css|js(?!on)|jpe?g|webp|png|gif|svg|ttf|woff2?|ico|csv|docx?|xlsx?|zip|webmanifest)).*)',
        // Always run for API routes
        '/(api|trpc)(.*)',
      ],
    }
    ```


### Changes to top-level exports

As part of this release, some of the top-level exports of `@clerk/nextjs` have been changed in order to improve bundle size and tree-shaking efficiency. These changes have resulted in a \~75% reduction in build size for middleware bundles. However, you will likely need to make some changes to import paths as a result.

> [!NOTE]
> Use [the CLI tool](#cli-upgrade-helper) to automatically find occurrences of imports that need to be changed.


  
**Details**

Previously these exports have been exported both from `@clerk/nextjs` and `@clerk/nextjs/server`. As of v5 they are only exported from the latter. Going forward, the expectation can be that any imports that are intended to run within react on the client-side, will come from `@clerk/nextjs` and imports that are intended to run on the server, will come from `@clerk/nextjs/server`.

    ```js

    import {
      auth,
      currentUser,
      authMiddleware,
      buildClerkProps,
      verifyToken,
      verifyJwt,
      decodeJwt,
      signJwt,
      constants,
      redirect,
      createAuthenticateRequest,
      createIsomorphicRequest,
    } from '@clerk/nextjs'
    } from '@clerk/nextjs/server'
    ```


  
**Details**

Exports related to errors are now under `@clerk/nextjs/errors`.

    ```js

    import {
      isClerkAPIResponseError,
      isEmailLinkError,
      isKnownError,
      isMetamaskError,
      EmailLinkErrorCode,
    } from '@clerk/nextjs'
    } from '@clerk/nextjs/errors'
    ```


  
**Details**

The `@clerk/nextjs` import will work with both the App and Pages Router.

    ```js

    import { } from '@clerk/nextjs/app-beta'
    import { } from '@clerk/nextjs'
    ```

    Some behavior may have changed between Clerk's beta and the stable release. Check on your end if behavior stayed the same.


  
**Details**

The top-level exports support SSR by default now.

    ```js

    import { } from '@clerk/nextjs/ssr'
    import { } from '@clerk/nextjs'
    ```


  
**Details**

```js

    import { } from '@clerk/nextjs/edge-middleware'
    import { } from '@clerk/nextjs'
    ```


  
**Details**

```js

    import { } from '@clerk/nextjs/edge-middlewarefiles'
    import { } from '@clerk/nextjs'
    ```


  
**Details**

> [!IMPORTANT]
> The Node SDK is no longer supported. [Upgrade to the Express SDK](/guides/development/upgrading/upgrade-guides/node-to-express).


    The `@clerk/nextjs/api` subpath was removed completely. It re-exported helpers from `@clerk/clerk-sdk-node` and its types. If you relied on these, import from `@clerk/clerk-sdk-node` directly instead.

    ```js

    import type {
      ClerkMiddleware,
      ClerkMiddlewareOptions,
      LooseAuthProp,
      RequireAuthProp,
      StrictAuthProp,
      WithAuthProp,
    } from '@clerk/nextjs/api'
    } from '@clerk/clerk-sdk-node'

    import { requireAuth, withAuth } from '@clerk/nextjs/api'
    import { requireAuth, withAuth } from '@clerk/clerk-sdk-node'
    ```


### After sign up/in/out default value change

In Core 2, defining redirect URLs for after sign-up, sign-in, or sign-out via the Clerk Dashboard has been removed. Previously, the "Paths" section in the Clerk Dashboard included "Component paths" where URLs could be defined, accompanied by a deprecation warning. This functionality is now removed, and specifying redirect paths via the dashboard is no longer supported.

If you need to pass a redirect URL for after sign-up, sign-in, or sign-out, there are [several ways to achieve this](/guides/development/customize-redirect-urls), including environment variables, middleware, or passing them directly to the relevant components.

As part of this change, the default redirect URL for each of these props has been set to `/`, so if you are passing `/` explicitly to any one of the above props, that line is no longer necessary and can be removed.

```jsx

```

### `afterSignXUrl` changes

> [!NOTE]
> This section refers to `afterSignXUrl` where `X` could be `Up` or `In` depending on the context.

All `afterSignXUrl` props and `CLERK_AFTER_SIGN_X_URL` environment variables have been deprecated, and should be replaced by one of the following options:

- `CLERK_SIGN_X_FORCE_REDIRECT_URL` / `signXForceRedirectUrl` – If set, Clerk will always redirect to provided URL, regardless of what page the user was on before. Use this option with caution, as it will interrupt the user's flow by taking them away from the page they were on before.
- `CLERK_SIGN_X_FALLBACK_REDIRECT_URL` / `signXFallbackRedirectUrl` – If set, this will mirror the previous behavior, only redirecting to the provided URL if there is no `redirect_url` in the querystring.

In general, use the environment variables over the props.

> [!WARNING]
> If neither value is set, Clerk will redirect to the `redirect_url` if present, otherwise it will redirect to `/`.

To retain the current behavior of your app without any changes, you can switch `afterSignXUrl` with `signXFallbackRedirectUrl` as such:

```jsx

```

### Removed: `orgs` claim on JWT

In the previous version of Clerk's SDKs, if you decode the session token that Clerk returns from the server, you'll currently find an `orgs` claim on it. It lists all the orgs associated with the given user. Now, Clerk returns the `org_id`, `org_slug`, and `org_role` of the **active** organization.

The `orgs` claim was part of the `JwtPayload`. Here are a few examples of where the `JwtPayload` could be found.


  
**Details**

```typescript
// Filename: Next.js

    import { getAuth } from '@clerk/nextjs/server'
    const claims: JwtPayload = getAuth(request).sessionClaims

    import { getAuth } from '@clerk/ssr.server'
    const claims: JwtPayload = (await getAuth(request)).sessionClaims
    ```


  
**Details**

```typescript
// Filename: Fastify

    import { getAuth } from '@clerk/fastify'
    const claims: JwtPayload = (await getAuth(request)).sessionClaims
    ```


  
**Details**

```typescript
// Filename: @clerk/backend

    import { createClerkClient } from '@clerk/backend'

    const clerkClient = createClerkClient({ secretKey: '' })
    const requestState = await clerkClient.authenticateRequest(request, { publishableKey: '' })
    const claims: JwtPayload = requestState.toAuth().sessionClaims
    ```


  
**Details**

> [!IMPORTANT]
> The Node SDK is no longer supported. [Upgrade to the Express SDK](/guides/development/upgrading/upgrade-guides/node-to-express).


    ```typescript
// Filename: @clerk/clerk-sdk-node

    import { clerkClient } from '@clerk/clerk-sdk-node'

    router.use((...args) => clerkClient.expressRequireAuth()(...args))
    router.get('/me', async (req, reply: Response) => {
      return reply.json({ auth: req.auth })
    })
    ```


If you would like to have your JWT return all of the user's organizations, you can create a [custom JWT template](/guides/sessions/jwt-templates) in your dashboard. Add `{ "orgs": "user.organizations" }` to it.

### Path routing is now the default

On components like [``](/reference/components/authentication/sign-in) you can define the props `routing` and `path`. `routing` can be set to `'hash' | 'path'` and describes the routing strategy that should be used. `path` defines where the component is mounted when `routing="path"` is used. [Learn more about Clerk routing](/guides/how-clerk-works/routing).

In Core 2, the **default** `routing` strategy has become `'path'` for the Next.js SDK. Of course, you can still use `routing='hash'`.

```jsx

```

### Image URL Name Consolidation

There are a number of Clerk primitives that contain images, and previously they each had different property names, like `avatarUrl`, `logoUrl`, `profileImageUrl`, etc. In order to promote consistency and make it simpler for developers to know where to find associated images, all image properties are now named `imageUrl`. See the list below for all affected classes:

Organization.logoUrl</code> -&gt; <code>Organization.imageUrl</code>", "<code>User.profileImageUrl</code> -&gt; <code>.imageUrl</code>", "<code>ExternalAccount.avatarUrl</code> -&gt; <code>.imageUrl</code>", "<code>OrganizationMembershipPublicUserData.profileImageUrl</code> -&gt; <code>.imageUrl</code>"]}
>
  
**Details**

The `logoUrl` property of any [`Organization` object](/reference/javascript/organization) has been changed to `imageUrl`.


  
**Details**

The `profileImageUrl` property of any `User` object has been changed to `imageUrl`.


  
**Details**

The `avatarUrl` property of any [`ExternalAccount` object](/reference/javascript/types/external-account) has been changed to `imageUrl`.


  
**Details**

The `profileImageUrl` property of any `OrganizationMembershipPublicUserData` object has been changed to `imageUrl`.


### Deprecation removals & housekeeping

As part of this major version, a number of previously deprecated props, arguments, methods, etc. have been removed. Additionally there have been some changes to things that are only used internally, or only used very rarely. It's highly unlikely that any given app will encounter any of these items, but they are all breaking changes, so they have all been documented below.

> [!NOTE]
> For this section more than any other one, use the CLI upgrade tool (`npx @clerk/upgrade`). Changes in this
> section are very unlikely to appear in your codebase, the tool will save time looking for them.

#### Deprecation removals

User.update({ password: &#39;x&#39; })</code> -&gt; <code>User.updatePassword(&#39;x&#39;)</code>", "<code>CLERK_API_KEY</code> replaced by <code>CLERK_SECRET_KEY</code>", "<code>CLERK_FRONTEND_API</code> replaced by <code>CLERK_PUBLISHABLE_KEY</code>", "<code>CLERK_JS_VERSION</code> should be <code>NEXT_PUBLIC_CLERK_JS_VERSION</code>", "<code>apiKey</code> -&gt; <code>secretKey</code> as param to <code>authMiddleware</code>", "<code>frontendApi</code> -&gt; <code>publishableKey</code> as param to <code>authMiddleware</code>", "<code>apiKey</code> -&gt; <code>secretKey</code> as param to <code>createClerkClient</code>", "<code>frontendApi</code> -&gt; <code>publishableKey</code> as param to <code>createClerkClient</code>", "<code>apiKey</code> -&gt; <code>secretKey</code> as param to <code>getAuth</code>", "<code>frontendApi</code> -&gt; <code>publishableKey</code> as prop to <code>ClerkProvider</code>", "<code>@clerk/nextjs/app-beta</code> import removed", "<code>@clerk/nextjs/ssr</code> import removed", "<code>@clerk/nextjs/edge-middleware</code> import removed", "<code>@clerk/nextjs/edge-middlewarefiles</code> import removed", "<code>API_URL</code> constant removed", "<code>API_VERSION</code> constant removed", "<code>CLERK_JS_URL</code> constant removed", "<code>CLERK_JS_VERSION</code> constant removed", "<code>DOMAIN</code> constant removed", "<code>IS_SATELLITE</code> constant removed", "<code>PROXY_URL</code> constant removed", "<code>PUBLISHABLE_KEY</code> constant removed", "<code>SECRET_KEY</code> constant removed", "<code>SIGN_IN_URL</code> constant removed", "<code>SIGN_UP_URL</code> constant removed", "<code>@clerk/nextjs/api</code> import removed", "<code>MultiSessionAppSupport</code> import moved under <code>/internal</code>", "<code>NEXT_PUBLIC_CLERK_JS</code> should be <code>NEXT_PUBLIC_CLERK_JS_URL</code>"]}
>
  
**Details**

If you are updating a user's password via the [`User.update` method](/reference/javascript/user#update), it must be changed to [`User.updatePassword`](/reference/javascript/user#update-password) instead. This method will require the current password as well as the desired new password. We made this update to improve the security of password changes. Example below:

    ```js

    user.update({ password: 'foo' })

    user.updatePassword({
      currentPassword: 'bar',
      newPassword: 'foo',
      signOutOfOtherSessions: true,
    })
    ```


  
**Details**

The `CLERK_API_KEY` environment variable was renamed to `CLERK_SECRET_KEY`. To update, go to the [**API keys**](https://dashboard.clerk.com/~/api-keys) page in the Clerk Dashboard. After choosing your framework, copy and paste the new keys. Ensure this update is applied across all environments (e.g., development, staging, production).


  
**Details**

The `CLERK_FRONTEND_API` environment variable was renamed to `CLERK_PUBLISHABLE_KEY`. To update, go to the [**API keys**](https://dashboard.clerk.com/~/api-keys) page in the Clerk Dashboard. After choosing your framework, copy and paste the new keys. Ensure this update is applied across all environments (e.g., development, staging, production). **Note:** The values are different, so this isn't just a key replacement. [More information](/guides/development/deployment/production#api-keys-and-environment-variables).


  
**Details**

If you are using `CLERK_JS_VERSION` as an environment variable, it should be changed to `NEXT_PUBLIC_CLERK_JS_VERSION` instead.

    This change brings our SDK up to date with the latest standards for next.js - that public environment variables should have the `NEXT_PUBLIC_` prefix. This env variable is not private, so it should get the public prefix.


  
**Details**

The `apiKey` argument passed to `authMiddleware` must be changed to `secretKey`.

    ```js

    import { authMiddleware } from '@clerk/nextjs/server'

    authMiddleware({ apiKey: '...' })
    authMiddleware({ secretKey: '...' })
    ```


  
**Details**

The `frontendApi` argument passed to `authMiddleware` must be changed to `publishableKey`

    ```js

    import { authMiddleware } from '@clerk/nextjs/server'

    authMiddleware({ frontendApi: '...' })
    authMiddleware({ publishableKey: '...' })
    ```


  
**Details**

The `apiKey` argument passed to `createClerkClient` must be changed to `secretKey`.

    ```js

    import { createClerkClient } from '@clerk/nextjs/server'

    createClerkClient({ apiKey: '...' })
    createClerkClient({ secretKey: '...' })
    ```


  
**Details**

The `frontendApi` argument passed to `createClerkClient` must be changed to `publishableKey`. Note that the values of the two keys are different, so both keys and values need to be changed. You can find your application's Publishable Key in the Clerk Dashboard.

    ```js

    import { createClerkClient } from '@clerk/nextjs/server'

    createClerkClient({ frontendApi: '...' })
    createClerkClient({ publishableKey: '...' })
    ```


  
**Details**

The `apiKey` argument passed to `getAuth` must be changed to `secretKey`.

    ```js

    getAuth({ apiKey: '...' })
    getAuth({ secretKey: '...' })
    ```


  
**Details**

The `frontendApi` prop passed to `` was renamed to `publishableKey`. To update, go to the [**API keys**](https://dashboard.clerk.com/~/api-keys) page in the Clerk Dashboard. After choosing your framework, copy and paste the new keys. Ensure this update is applied across all environments (e.g., development, staging, production). **Note:** The values are different, so this isn't just a key replacement. [More information](/guides/development/deployment/production#api-keys-and-environment-variables).


  
**Details**

If you are using the `@clerk/nextjs/app-beta` import anywhere, it should use `@clerk/nextjs` instead. The `app-beta` import has been removed as our App Router support is stable.

    Make this change carefully as some behavior may have changed between our beta and stable releases. You can refer to [our documentation](/nextjs/getting-started/quickstart) and/or [approuter example](https://github.com/clerk/clerk-nextjs-app-quickstart) for up-to-date usage.

    The `@clerk/nextjs` import will work with both App Router and Pages Router.


  
**Details**

If you are importing from `@clerk/nextjs/ssr`, you can use `@clerk/nextjs` instead. Our top-level import supports SSR functionality by default now, so the subpath on the import is no longer needed. This import can be directly replaced without any other considerations.


  
**Details**

This deprecated import has been replaced by `@clerk/nextjs/server`. Usage should now look as such: `import { authMiddleware } from @clerk/nextjs/server`. There may be changes in functionality between the two exports depending on how old the version used is, so upgrade with caution.


  
**Details**

This deprecated import has been replaced by `@clerk/nextjs/server`. Usage should now look as such: `import { authMiddleware } from @clerk/nextjs/server`. There may be changes in functionality between the two exports depending on how old the version used is, so upgrade with caution.


  
**Details**

This deprecated constant has been removed as an export from `@clerk/nextjs`. Instead, set and use the `CLERK_API_URL` environment variable.


  
**Details**

This deprecated constant has been removed as an export from `@clerk/nextjs`. Instead, set and use the `CLERK_API_VERSION` environment variable.


  
**Details**

This deprecated constant has been removed as an export from `@clerk/nextjs`. Instead, set and use the `NEXT_PUBLIC_CLERK_JS_URL` environment variable.


  
**Details**

This deprecated constant has been removed as an export from `@clerk/nextjs`. Instead, set and use the `NEXT_PUBLIC_CLERK_JS_VERSION` environment variable.


  
**Details**

This deprecated constant has been removed as an export from `@clerk/nextjs`. Instead, set and use the `NEXT_PUBLIC_CLERK_DOMAIN` environment variable.


  
**Details**

This deprecated constant has been removed as an export from `@clerk/nextjs`. Instead, set and use the `NEXT_PUBLIC_CLERK_IS_SATELLITE` environment variable.


  
**Details**

This deprecated constant has been removed as an export from `@clerk/nextjs`. Instead, set and use the `NEXT_PUBLIC_CLERK_PROXY_URL` environment variable.


  
**Details**

This deprecated constant has been removed as an export from `@clerk/nextjs`. Instead, set and use the `NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY` environment variable.


  
**Details**

This deprecated constant has been removed as an export from `@clerk/nextjs`. Instead, set and use the `CLERK_SECRET_KEY` environment variable.


  
**Details**

This deprecated constant has been removed as an export from `@clerk/nextjs`. Instead, set and use the `NEXT_PUBLIC_CLERK_SIGN_IN_URL` environment variable.


  
**Details**

This deprecated constant has been removed as an export from `@clerk/nextjs`. Instead, set and use the `NEXT_PUBLIC_CLERK_SIGN_UP_URL` environment variable.


  
**Details**

> [!IMPORTANT]
> The Node SDK is no longer supported. [Upgrade to the Express SDK](/guides/development/upgrading/upgrade-guides/node-to-express).


    The import subpath `@clerk/nextjs/api` has been removed. This includes the following imports:

    ```js
    // These have been removed
    import {
      ClerkMiddleware,
      ClerkMiddlewareOptions,
      LooseAuthProp,
      RequireAuthProp,
      StrictAuthProp,
      WithAuthProp,
    } from '@clerk/nextjs/api'
    ```

    If you still need to use any of these functions, they can be instead imported from `@clerk/clerk-sdk-node`.


  
**Details**

The `MultiSessionAppSupport` import path has changed from `@clerk/nextjs` to `@clerk/nextjs/internal`. You must update your import path in order for it to work correctly. Note that internal imports are not intended for usage and are outside the scope of semver. Example below of the fix that needs to be made:

    ```js

    import { MultiSessionAppSupport } from '@clerk/nextjs'
    import { MultiSessionAppSupport } from '@clerk/nextjs/internal'
    ```


  
**Details**

If you are using `NEXT_PUBLIC_CLERK_JS` as an environment variable, it should be changed to `NEXT_PUBLIC_CLERK_JS_URL` instead. This variable was renamed for consistency across public APIs. Make sure to also check your production host configuration when changing environment variable values.


#### Other Breaking changes

Organization.getRoles</code> arguments changed", "<code>Organization.getMemberships</code> arguments changed", "<code>Organization.getDomains</code> arguments changed", "<code>Organization.getInvitations</code> arguments changed", "<code>Organization.getMembershipRequests</code> arguments changed", "<code>User.getOrganizationInvitations</code> arguments changed", "<code>User.getOrganizationSuggestions</code> arguments changed", "<code>User.getOrganizationMemberships</code> arguments changed", "<code>Users.getOrganizationMembershipList</code> return signature changed", "<code>Users.getOrganizationInvitationList</code> return signature changed", "<code>Organizations.getOrganizationInvitationList</code> return type changed", "<code>User.getOrganizationMembershipList</code> return type changed", "<code>Users.getOrganizationList</code> return signature changed", "<code>Organization.getOrganizationList</code> return type changed", "<code>Invitations.getInvitationList</code> return signature changed", "<code>Sessions.getSessionList</code> return signature changed", "<code>Users.getUserList</code> return signature changed", "<code>AllowlistIdentifiers.getAllowlistIdentifierList</code> return signature changed", "<code>Clients.getClientList</code> return signature changed", "<code>RedirectUrls.getRedirectUrlList</code> return signature changed", "<code>Users.getUserOauthAccessToken</code> return signature changed", "<code>setSession</code> -&gt; <code>setActive</code>", "<code>Organization.create(&#39;x&#39;)</code> -&gt; <code>Organization.create({ name: &#39;x&#39; })</code>", "<code>Organization.getPendingInvitations()</code> -&gt; <code>Organization.getInvitations({ status: &#39;pending&#39; })</code>", "<code>API_URL</code> value has changed", "<code>isMagicLinkError</code> -&gt; <code>isEmailLinkError</code>", "<code>useMagicLink</code> -&gt; <code>useEmailLink</code>", "<code>MagicLinkErrorCode</code> -&gt; <code>EmailLinkErrorCode</code>", "<code>isMetamaskError</code> import moved under <code>/errors</code>", "<code>WithSession</code> component removed", "<code>WithClerk</code> component removed", "<code>WithUser</code> component removed", "<code>withClerk</code> function removed", "<code>withSession</code> function removed", "<code>withUser</code> function removed", "Replace <code>signOutCallback</code> prop on <code>SignOutButton</code> with <code>redirectUrl</code>"]}
>
  
**Details**

There have been a couple changes to the pagination arguments that can be passed into this function - `limit` has been renamed to `pageSize`, and `offset` has been renamed to `initialPage`. This will help to make it more clear and simple to reason about pagination control. Example of how changes might look below:

    ```js

    const { data } = await organization.getRoles({
      limit: 10,
      pageSize: 10,
      offset: 10,
      initialPage: 2,
    })
    ```


  
**Details**

There have been a couple changes to the pagination arguments that can be passed into this function - `limit` has been renamed to `pageSize`, and `offset` has been renamed to `initialPage`. This will help to make it more clear and simple to reason about pagination control. Example of how changes might look below:

    ```js

    const { data } = await organization.getMemberships({
      limit: 10,
      pageSize: 10,
      offset: 10,
      initialPage: 2,
    })
    ```


  
**Details**

There have been a couple changes to the pagination arguments that can be passed into this function - `limit` has been renamed to `pageSize`, and `offset` has been renamed to `initialPage`. This will help to make it more clear and simple to reason about pagination control. Example of how changes might look below:

    ```js

    const { data } = await organization.getDomains({
      limit: 10,
      pageSize: 10,
      offset: 10,
      initialPage: 2,
    })
    ```


  
**Details**

There have been a couple changes to the pagination arguments that can be passed into this function - `limit` has been renamed to `pageSize`, and `offset` has been renamed to `initialPage`. This will help to make it more clear and simple to reason about pagination control. Example of how changes might look below:

    ```js

    const { data } = await organization.getInvitations({
      limit: 10,
      pageSize: 10,
      offset: 10,
      initialPage: 2,
    })
    ```


  
**Details**

There have been a couple changes to the pagination arguments that can be passed into this function - `limit` has been renamed to `pageSize`, and `offset` has been renamed to `initialPage`. This will help to make it more clear and simple to reason about pagination control. Example of how changes might look below:

    ```js

    const { data } = await organization.getMembershipRequests({
      limit: 10,
      pageSize: 10,
      offset: 10,
      initialPage: 2,
    })
    ```


  
**Details**

There have been a couple changes to the pagination arguments that can be passed into this function - `limit` has been renamed to `pageSize`, and `offset` has been renamed to `initialPage`. This will help to make it more clear and simple to reason about pagination control. Example of how changes might look below:

    ```js

    const { data } = await user.getOrganizationInvitations({
      limit: 10,
      pageSize: 10,
      offset: 10,
      initialPage: 2,
    })
    ```


  
**Details**

There have been a couple changes to the pagination arguments that can be passed into this function - `limit` has been renamed to `pageSize`, and `offset` has been renamed to `initialPage`. This will help to make it more clear and simple to reason about pagination control. Example of how changes might look below:

    ```js

    const { data } = await user.getOrganizationSuggestions({
      limit: 10,
      pageSize: 10,
      offset: 10,
      initialPage: 2,
    })
    ```


  
**Details**

There have been a couple changes to the pagination arguments that can be passed into this function - `limit` has been renamed to `pageSize`, and `offset` has been renamed to `initialPage`. This will help to make it more clear and simple to reason about pagination control. Example of how changes might look below:

    ```js

    const { data } = await user.getOrganizationMemberships({
      limit: 10,
      pageSize: 10,
      offset: 10,
      initialPage: 2,
    })
    ```


  
**Details**

The response payload of `Users.getOrganizationMembershipList` was changed as part of the core 2 release. Rather than directly returning ` data`, the return signature is now `{ data, totalCount }`. Since Backend API responses are paginated, the `totalCount` property is helpful in determining the total number of items in the response easily, and this change in the backend SDK aligns the response shape with what the Backend API returns directly.

    Here's an example of how the response shape would change with this modification:

    ```js

    const data = await clerkClient.users.getOrganizationMembershipList()
    const { data, totalCount } = await clerkClient.users.getOrganizationMembershipList()
    ```


  
**Details**

The response payload of `Users.getOrganizationInvitationList` was changed as part of the core 2 release. Rather than directly returning ` data`, the return signature is now `{ data, totalCount }`. Since Backend API responses are paginated, the `totalCount` property is helpful in determining the total number of items in the response easily, and this change in the backend SDK aligns the response shape with what the Backend API returns directly.

    Here's an example of how the response shape would change with this modification:

    ```js

    const data = await clerkClient.users.getOrganizationInvitationList()
    const { data, totalCount } = await clerkClient.users.getOrganizationInvitationList()
    ```


  
**Details**

The return type for this function was previously `[Items]` but has now been updated to `{ data: [Items], totalCount: number }`. Since the Clerk API responses are paginated, the `totalCount` property is helpful in determining the total number of items in the response easily. A before/after code example can be seen below:

    ```js

    const data = await clerkClient.organizations.getOrganizationInvitationList({
      organizationId: '...',
    })

    data.forEach(() => {})
    data.data.forEach(() => {})
    ```


  
**Details**

The return type for this function was previously `[Items]` but has now been updated to `{ data: [Items], totalCount: number }`. Since the Clerk API responses are paginated, the `totalCount` property is helpful in determining the total number of items in the response easily. A before/after code example can be seen below:

    ```js

    const { user } = useUser()
    const membershipList = user.getOrganizationMembershipList()

    membershipList.forEach(() => {})
    membershipList.data.forEach(() => {})
    ```


  
**Details**

The response payload of `Users.getOrganizationList` was changed as part of the core 2 release. Rather than directly returning ` data`, the return signature is now `{ data, totalCount }`. Since Backend API responses are paginated, the `totalCount` property is helpful in determining the total number of items in the response easily, and this change in the backend SDK aligns the response shape with what the Backend API returns directly.

    Here's an example of how the response shape would change with this modification:

    ```js

    const data = await clerkClient.users.getOrganizationList()
    const { data, totalCount } = await clerkClient.users.getOrganizationList()
    ```


  
**Details**

The return type for this function was previously `[Items]` but has now been updated to `{ data: [Items], totalCount: number }`. Since the Clerk API responses are paginated, the `totalCount` property is helpful in determining the total number of items in the response easily. A before/after code example can be seen below:

    ```js

    const { organization } = useOrganization()
    const orgList = organization.getOrganizationList()

    orgList.forEach(() => {})
    orgList.data.forEach(() => {})
    ```


  
**Details**

The response payload of `Invitations.getInvitationList` was changed as part of the core 2 release. Rather than directly returning ` data`, the return signature is now `{ data, totalCount }`. Since Backend API responses are paginated, the `totalCount` property is helpful in determining the total number of items in the response easily, and this change in the backend SDK aligns the response shape with what the Backend API returns directly.

    Here's an example of how the response shape would change with this modification:

    ```js

    const data = await clerkClient.invitations.getInvitationList()
    const { data, totalCount } = await clerkClient.invitations.getInvitationList()
    ```


  
**Details**

The response payload of `Sessions.getSessionList` was changed as part of the core 2 release. Rather than directly returning ` data`, the return signature is now `{ data, totalCount }`. Since Backend API responses are paginated, the `totalCount` property is helpful in determining the total number of items in the response easily, and this change in the backend SDK aligns the response shape with what the Backend API returns directly.

    Here's an example of how the response shape would change with this modification:

    ```js

    const data = await clerkClient.sessions.getSessionList()
    const { data, totalCount } = await clerkClient.sessions.getSessionList()
    ```


  
**Details**

The response payload of `Users.getUserList` was changed as part of the core 2 release. Rather than directly returning ` data`, the return signature is now `{ data, totalCount }`. Since Backend API responses are paginated, the `totalCount` property is helpful in determining the total number of items in the response easily, and this change in the backend SDK aligns the response shape with what the Backend API returns directly.

    Here's an example of how the response shape would change with this modification:

    ```js

    const data = await clerkClient.users.getUserList()
    const { data, totalCount } = await clerkClient.users.getUserList()
    ```


  
**Details**

The response payload of `AllowlistIdentifiers.getAllowlistIdentifierList` was changed as part of the core 2 release. Rather than directly returning ` data`, the return signature is now `{ data, totalCount }`. Since Backend API responses are paginated, the `totalCount` property is helpful in determining the total number of items in the response easily, and this change in the backend SDK aligns the response shape with what the Backend API returns directly.

    Here's an example of how the response shape would change with this modification:

    ```js

    const data = await clerkClient.allowlistIdentifiers.getAllowlistIdentifierList()
    const { data, totalCount } = await clerkClient.allowlistIdentifiers.getAllowlistIdentifierList()
    ```


  
**Details**

The response payload of `Clients.getClientList` was changed as part of the core 2 release. Rather than directly returning ` data`, the return signature is now `{ data, totalCount }`. Since Backend API responses are paginated, the `totalCount` property is helpful in determining the total number of items in the response easily, and this change in the backend SDK aligns the response shape with what the Backend API returns directly.

    Here's an example of how the response shape would change with this modification:

    ```js

    const data = await clerkClient.clients.getClientList()
    const { data, totalCount } = await clerkClient.allowlistIdentifiers.getClientList()
    ```


  
**Details**

The response payload of `RedirectUrls.getRedirectUrlList` was changed as part of the core 2 release. Rather than directly returning ` data`, the return signature is now `{ data, totalCount }`. Since Backend API responses are paginated, the `totalCount` property is helpful in determining the total number of items in the response easily, and this change in the backend SDK aligns the response shape with what the Backend API returns directly.

    Here's an example of how the response shape would change with this modification:

    ```js

    const data = await clerkClient.redirectUrls.getRedirectUrlList()
    const { data, totalCount } = await clerkClient.redirectUrls.getRedirectUrlList()
    ```


  
**Details**

The response payload of `Users.getUserOauthAccessToken` was changed as part of the core 2 release. Rather than directly returning ` data`, the return signature is now `{ data, totalCount }`. Since Backend API responses are paginated, the `totalCount` property is helpful in determining the total number of items in the response easily, and this change in the backend SDK aligns the response shape with what the Backend API returns directly.

    Here's an example of how the response shape would change with this modification:

    ```js

    const data = await clerkClient.users.getUserOauthAccessToken()
    const { data, totalCount } = await clerkClient.users.getUserOauthAccessToken()
    ```


  
**Details**

`setSession` should be replaced with `setActive`. The format of the parameters has changed slightly - `setActive` takes an object where `setSession` took params directly. The `setActive` function also can accept an `organization` param that is used to set the currently Active Organization. The return signature did not change. Read the [API documentation](/reference/javascript/clerk#set-active) for more detail. This function should be expected to be returned from one of the following Clerk hooks: `useSessionList`, `useSignUp`, or `useSignIn`. Some migration examples:

    ```js

    await setSession('sessionID', () => void)
    await setActive({ session: 'sessionID', beforeEmit: () => void })

    await setSession(sessionObj)
    await setActive({ session: sessionObj })

    await setSession(sessionObj, () => void)
    await setActive({ session: sessionObj, beforeEmit: () => void })
    ```

    `setActive` also supports setting an Active Organization:

    ```js

    await setActive({
      session: 'sessionID',
      organization: 'orgID',
      beforeEmit: () => void,
    })

    await setActive({
      session: sessionObj,
      organization: orgObj,
      beforeEmit: () => void,
    })
    ```


  
**Details**

Passing a string as an argument to `Organization.create` is no longer possible - instead, pass an object with the `name` property.

    ```js

    Organization.create('...')
    Organization.create({ name: '...' })
    ```


  
**Details**

The `Organization.getPendingInvitations()` method has been removed. You can use `Organization.getInvitations` instead.

    ```js

    Organization.getPendingInvitations()
    Organization.getInvitations({ status: 'pending' })
    ```


  
**Details**

The value of this export has changed from `https://api.clerk.dev` to `https://api.clerk.com`. If you were relying on the text content of this value not changing, you may need to make adjustments.


  
**Details**

Across Clerk's documentation and codebases the term "magic link" was changed to "email link" as it more accurately reflects the functionality.


  
**Details**

Across Clerk's documentation and codebases the term "magic link" was changed to "email link" as it more accurately reflects functionality.


  
**Details**

Across Clerk's documentation and codebases the term "magic link" was changed to "email link" as it more accurately reflects the functionality.


  
**Details**

The `isMetamaskError` import path has changed from `@clerk/react` to `@clerk/react/errors`. You must update your import path in order for it to work correctly. Example below of the fix that needs to be made:

    ```js

    import { isMetamaskError } from '@clerk/react'
    import { isMetamaskError } from '@clerk/react/errors'
    ```


  
**Details**

The `WithSession` higher order component has been removed. If you would still like to use this function in the way its implemented, it can be created quickly using Clerk's [custom hooks](/reference/react/overview). An example of how to do so is below:

    ```js
    export const WithSession = ({ children }) => {
      const session = useSession()
      if (typeof children !== 'function') throw new Error()

      return children(session)
    }
    ```


  
**Details**

The `WithClerk` higher order component has been removed. If you would still like to use this function in the way its implemented, it can be created quickly using Clerk's [custom hooks](/reference/react/overview). An example of how to do so is below:

    ```js
    export const WithClerk = ({ children }) => {
      const clerk = useClerk()
      if (typeof children !== 'function') throw new Error()

      return children(clerk)
    }
    ```


  
**Details**

The `WithUser` higher order component has been removed. If you would still like to use this function in the way its implemented, it can be created quickly using Clerk's [custom hooks](/reference/react/overview). An example of how to do so is below:

    ```js
    export const WithUser = ({ children }) => {
      const user = useUser()
      if (typeof children !== 'function') throw new Error()

      return children(user)
    }
    ```


  
**Details**

The `withClerk` higher order function has been removed. If you would still like to use this function in the way its implemented, it can be created quickly using Clerk's [custom hooks](/reference/react/overview). An example of how to do so is below:

    ```js
    function withClerk(Component, displayName) {
      displayName = displayName || Component.displayName || Component.name || 'Component'
      Component.displayName = displayName
      const HOC = (props) => {
        const clerk = useIsomorphicClerkContext()

        if (!clerk.loaded) return null

        return }

      HOC.displayName = `withClerk(${displayName})`
      return HOC
    }
    ```


  
**Details**

The `withSession` higher order function has been removed. If you would still like to use this function in the way its implemented, it can be created quickly using Clerk's [custom hooks](/reference/react/overview). An example of how to do so is below:

    ```js
    function withSession(Component, displayName) {
      displayName = displayName || Component.displayName || Component.name || 'Component'
      Component.displayName = displayName
      const HOC = (props) => {
        const session = useSessionContext()

        if (!session) return null

        return }

      HOC.displayName = `withSession(${displayName})`
      return HOC
    }
    ```


  
**Details**

The `withUser` higher order function has been removed. If you would still like to use this function in the way its implemented, it can be created quickly using Clerk's [custom hooks](/reference/react/overview). An example of how to do so is below:

    ```js
    function withUser(Component, displayName) {
      displayName = displayName || Component.displayName || Component.name || 'Component'
      Component.displayName = displayName
      const HOC = (props) => {
        const clerk = useUserContext()

        if (!user) return null

        return }

      HOC.displayName = `withUser(${displayName})`
      return HOC
    }
    ```


  
**Details**

The `signOutCallback` prop on the [`` component](/reference/components/unstyled/sign-out-button) has been removed. Instead, you can use the `redirectUrl` prop. Example below:

    ```jsx

    import { SignOutButton } from '@clerk/clerk-react'

    export const Signout = () => {
      return (
         {
            window.location.href = '/your-path'
          }}
          redirectUrl="/your-path"
        >
          <button>Sign Out</button>
        
      )
    }
    ```
