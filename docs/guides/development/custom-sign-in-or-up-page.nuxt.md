# Build your own sign-in-or-up page for your Nuxt app with Clerk


> Learn how to add a custom sign-in-or-up page to your Nuxt app with Clerk's prebuilt components.

This guide shows you how to use the [``](/reference/components/authentication/sign-in) component to build a custom page **that allows users to sign in or sign up within a single flow**.

To set up separate sign-in and sign-up pages, follow this guide, and then follow the [custom sign-up page guide](/nuxt/guides/development/custom-sign-up-page).

> [!NOTE]
> Just getting started with Clerk and Nuxt? See the [quickstart tutorial](/nuxt/getting-started/quickstart)!


  ## Build a sign-in-or-up page

  The following example demonstrates how to render the `` component on a dedicated page using a [Nuxt catch-all route](https://nuxt.com/docs/directory-structure/app/pages#catch-all-route).

  ```vue
// Filename: app/pages/sign-in/[...slug].vue

  <template>
    </template>
  ```

  ## Configure your sign-in-or-up page

  Set the `CLERK_SIGN_IN_URL` environment variable to tell Clerk where the `` component is being hosted.

  There are other environment variables that you can set to customize Clerk's redirect behavior, such as `CLERK_SIGN_IN_FORCE_REDIRECT_URL`. Learn more about these environment variables and how to customize Clerk's redirect behavior in the [dedicated guide](/guides/development/customize-redirect-urls).

  ```env
// Filename: .env

  NUXT_PUBLIC_CLERK_SIGN_IN_URL=/sign-in
  ```

  ## Visit your new page

  Run your project with the following command:

  ```npm
  npm run dev
  ```

  Visit your new custom page locally at [localhost:3000/sign-in](http://localhost:3000/sign-in).


## Next steps

Learn more about Clerk components, how to use them to create custom pages, and how to use Clerk's client-side helpers using the following guides.


  - [Create a custom sign-up page](/nuxt/guides/development/custom-sign-up-page)
  - Learn how to add a custom sign-up page to your Nuxt app with Clerk's components.

  ---

  - [Protect content and read user data](/nuxt/guides/users/reading)
  - Learn how to use Clerk's composables and helpers to protect content and read user data in your Nuxt app.

  ---

  - [Client-side helpers](/reference/nuxt/overview#client-side-helpers)
  - Learn more about Clerk's client-side helpers and how to use them.

  ---

  - [Prebuilt components](/reference/components/overview)
  - Learn how to quickly add authentication to your app using Clerk's suite of components.

  ---

  - [Clerk Nuxt SDK Reference](/reference/nuxt/overview)
  - Learn about the Clerk Nuxt SDK and how to integrate it into your app.
