# Build your own sign-in-or-up page for your Remix app with Clerk


> Learn how to add a custom sign-in-or-up page to your Remix app with Clerk's prebuilt components.

> [!WARNING]
> The Remix SDK is in maintenance mode and will only receive security updates. Please migrate to the [React Router SDK](/react-router/getting-started/quickstart) for continued development and new features.


This guide shows you how to use the [``](/reference/components/authentication/sign-in) component to build a custom page **that allows users to sign in or sign up within a single flow**.

To set up separate sign-in and sign-up pages, follow this guide, and then follow the [custom sign-up page guide](/remix/guides/development/custom-sign-up-page).

> [!NOTE]
> Just getting started with Clerk and Remix? See the [quickstart tutorial](/remix/getting-started/quickstart)!


  ## Build a sign-in-or-up page

  The following example demonstrates how to render the [``](/reference/components/authentication/sign-in) component on a dedicated page using the [Remix optional route](https://reactrouter.com/en/main/route/route#optional-segments).

  ```tsx
// Filename: app/routes/sign-in.$.tsx

  import { SignIn } from '@clerk/remix'

  export default function Page() {
    return }
  ```

  ## Configure your sign-in-or-up page

  
#### SSR Mode


      - Set the `CLERK_SIGN_IN_URL` environment variable to tell Clerk where the `` component is being hosted.
      - Set `CLERK_SIGN_IN_FALLBACK_REDIRECT_URL` as a fallback URL incase users visit the `/sign-in` route directly.
      - Set `CLERK_SIGN_UP_FALLBACK_REDIRECT_URL` as a fallback URL incase users select the 'Don't have an account? Sign up' link at the bottom of the component.

      Learn more about these environment variables and how to customize Clerk's redirect behavior in the [dedicated guide](/guides/development/customize-redirect-urls).

      ```env
// Filename: .env

      CLERK_SIGN_IN_URL=/sign-in
      CLERK_SIGN_IN_FALLBACK_REDIRECT_URL=/
      CLERK_SIGN_UP_FALLBACK_REDIRECT_URL=/
      ```
    

#### SPA Mode


      - Set the `signInUrl` property to your `ClerkApp` options to tell Clerk where the `` component is being hosted.
      - Set the `signInFallbackRedirectUrl` property to a fallback URL incase users visit the `/sign-in` route directly.
      - Set the `signUpFallbackRedirectUrl` property to a fallback URL incase users select the 'Don't have an account? Sign up' link at the bottom of the component.

      Learn more about these environment variables and how to customize Clerk's redirect behavior in the [dedicated guide](/guides/development/customize-redirect-urls).

      ```ts
// Filename: app/root.tsx

      export default ClerkApp(App, {
        publishableKey: PUBLISHABLE_KEY,
        signInUrl: '/sign-in',
        signInFallbackRedirectUrl: '/',
        signUpFallbackRedirectUrl: '/',
      })
      ```
    

  ## Visit your new page

  Run your project with the following terminal command from the root directory of your project:

  ```npm
  npm run dev
  ```

  Visit your new custom page locally at [localhost:3000/sign-in](http://localhost:3000/sign-in).


## Next steps

Learn more about Clerk components, how to use them to create custom pages, and how to use Clerk's client-side helpers using the following guides.


  - [Create a custom sign-up page](/remix/guides/development/custom-sign-up-page)
  - Learn how to add a custom sign-up page to your Remix app with Clerk's components.

  ---

  - [Protect content and read user data](/remix/guides/users/reading)
  - Learn how to use Clerk's hooks and helpers to protect content and read user data in your Remix app.

  ---

  - [Client-side helpers](/reference/remix/overview#client-side-helpers)
  - Learn more about Clerk's client-side helpers and how to use them.

  ---

  - [Prebuilt components](/reference/components/overview)
  - Learn how to quickly add authentication to your app using Clerk's suite of components.

  ---

  - [Clerk Remix SDK Reference](/reference/remix/overview)
  - Learn about the Clerk Remix SDK and how to integrate it into your app.
