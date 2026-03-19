# Build your own sign-up page for your React Router app with Clerk


> Learn how to add a custom sign-up page to your React Router app with Clerk's prebuilt components.

By default, the [``](/reference/components/authentication/sign-in) component handles signing in and signing up, but if you'd like to have a dedicated sign-up page, this guide shows you how to use the [``](/reference/components/authentication/sign-up) component to build a custom sign-up page.

To set up a single sign-in-or-up page, follow the [custom sign-in-or-up page guide](/react-router/guides/development/custom-sign-in-or-up-page).

> [!NOTE]
> Just getting started with Clerk and React Router? See the [quickstart tutorial](/react-router/getting-started/quickstart)!


  ## Build a sign-up page

  The following example demonstrates how to render the [``](/reference/components/authentication/sign-up) component on a dedicated sign-up page using the [React Router Splat route](https://reactrouter.com/start/framework/routing#splats).

  ```tsx
// Filename: app/routes/sign-up.tsx

  import { SignUp } from '@clerk/react-router'

  export default function SignUpPage() {
    return (
      <div>
        <h1>Sign up route</h1>
        </div>
    )
  }
  ```

  ## Configure routes

  React Router expects you to define routes in [`app/routes.ts`](https://reactrouter.com/start/framework/routing). Add the previously created sign-up page to your route configuration.

  ```tsx
// Filename: app/routes.ts

  import { type RouteConfig, index, route } from '@react-router/dev/routes'

  export default [
    index('routes/home.tsx'),
    route('sign-in/*', 'routes/sign-in.tsx'),
    route('sign-up/*', 'routes/sign-up.tsx'),
  ] satisfies RouteConfig
  ```

  ## Configure redirect behavior

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

  These values control the behavior of the `` and `` components and when you visit the respective links at the bottom of each component.

  ## Visit your new page

  Run your project with the following command:

  ```npm
  npm run dev
  ```

  Visit your new custom page locally at [localhost:5173/sign-up](http://localhost:5173/sign-up).
