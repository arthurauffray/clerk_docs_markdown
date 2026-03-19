# Build your own sign-up page for your Remix app with Clerk


> Learn how to add a custom sign-up page to your Remix app with Clerk's prebuilt components.

> [!WARNING]
> The Remix SDK is in maintenance mode and will only receive security updates. Please migrate to the [React Router SDK](/react-router/getting-started/quickstart) for continued development and new features.


By default, the [``](/reference/components/authentication/sign-in) component handles signing in and signing up, but if you'd like to have a dedicated sign-up page, this guide shows you how to use the [``](/reference/components/authentication/sign-up) component to build a custom sign-up page.

To set up a single sign-in-or-up page, follow the [custom sign-in-or-up page guide](/remix/guides/development/custom-sign-in-or-up-page).

> [!NOTE]
> Just getting started with Clerk and Remix? See the [quickstart tutorial](/remix/getting-started/quickstart)!


  ## Build a sign-up page

  The following example demonstrates how to render the [``](/reference/components/authentication/sign-up) component on a dedicated sign-up page using the [Remix optional route](https://reactrouter.com/en/main/route/route#optional-segments).

  ```tsx
// Filename: app/routes/sign-up.$.tsx

  import { SignUp } from '@clerk/remix'

  export default function Page() {
    return }
  ```

  ## Configure your sign-up page

  
#### SSR Mode


      - Set the `CLERK_SIGN_UP_URL` environment variable to tell Clerk where the `` component is being hosted.
      - Set `CLERK_SIGN_UP_FALLBACK_REDIRECT_URL` as a fallback URL incase users visit the `/sign-up` route directly.
      - Set `CLERK_SIGN_IN_FALLBACK_REDIRECT_URL` as a fallback URL incase users select the 'Already have an account? Sign in' link at the bottom of the component.

      Learn more about these environment variables and how to customize Clerk's redirect behavior in the [dedicated guide](/guides/development/customize-redirect-urls).

      ```env
// Filename: .env

      CLERK_SIGN_UP_URL=/sign-up
      CLERK_SIGN_UP_FALLBACK_REDIRECT_URL=/
      CLERK_SIGN_IN_FALLBACK_REDIRECT_URL=/
      ```
    

#### SPA Mode


      - Set the `signUpUrl` property to your `ClerkApp` options to tell Clerk where the `` component is being hosted.
      - Set the `signUpFallbackRedirectUrl` property to a fallback URL incase users visit the `/sign-up` route directly.
      - Set the `signInFallbackRedirectUrl` property to a fallback URL incase users select the 'Already have an account? Sign in' link at the bottom of the component.

      Learn more about these environment variables and how to customize Clerk's redirect behavior in the [dedicated guide](/guides/development/customize-redirect-urls).

      ```ts
// Filename: app/root.tsx

      export default ClerkApp(App, {
        publishableKey: PUBLISHABLE_KEY,
        signUpUrl: '/sign-up',
        signUpFallbackRedirectUrl: '/',
        signInFallbackRedirectUrl: '/',
      })
      ```
    

  ## Visit your new page

  Run your project with the following command:

  ```npm
  npm run dev
  ```

  Visit your new custom page locally at [localhost:3000/sign-up](http://localhost:3000/sign-up).


## Next steps

Learn more about Clerk components, how to customize them, and how to use Clerk's client-side helpers using the following guides.


  - [Protect content and read user data](/remix/guides/users/reading)
  - Learn how to use Clerk's hooks and helpers to protect content and read user data in your Remix app.

  ---

  - [Client-side helpers](/reference/remix/overview#client-side-helpers)
  - Learn more about Clerk's client-side helpers and how to use them.

  ---

  - [Prebuilt components](/reference/components/overview)
  - Learn how to quickly add authentication to your app using Clerk's suite of components.

  ---

  - [Customization & localization](/guides/customizing-clerk/appearance-prop/overview)
  - Learn how to customize and localize Clerk components.

  ---

  - [Clerk Remix SDK Reference](/reference/remix/overview)
  - Learn about the Clerk Remix SDK and how to integrate it into your app.
