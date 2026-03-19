# Build your own sign-in-or-up page for your Expo web app


> Learn how to add custom sign-in-or-up page to your Expo web app with Clerk's prebuilt components.

This guide shows you how to use the [``](/reference/components/authentication/sign-in) prebuilt component in order to build custom page that **allows users to sign in or sign up within a single flow**.

To set up separate sign-in and sign-up pages, follow this guide, and then follow the [custom sign-up page guide](/guides/development/web-support/custom-sign-up-page).

This guide uses [Expo Router](https://docs.expo.dev/router/introduction/) and the [platform-specific extensions](https://docs.expo.dev/router/create-pages/#platform-specific-extensions) to build the sign-in-or-up page specifically for the **web** platform.


  ## Build a sign-in-or-up page

  The following example demonstrates how to render the [``](/reference/components/authentication/sign-in) component to allow users to both sign-in or sign-up from a single flow.

  ```tsx
// Filename: /app/sign-in.web.tsx

  import { SignIn } from '@clerk/expo/web'

  export default function Page() {
    return }
  ```

  ## Visit your new page

  To run your project, use the following command:

  ```npm
  npm run web
  ```

  Visit your new custom pages locally at [localhost:8081/sign-in](http://localhost:8081/sign-in).


## Next steps

Learn more about Clerk components, how to build custom flows for your native apps, and how to use Clerk's client-side helpers using the following guides.


  - [Create a custom sign-up page](/guides/development/web-support/custom-sign-up-page)
  - Learn how to add a custom sign-up page to your app with Clerk's components.

  ---

  - [Prebuilt components](/reference/components/overview)
  - Learn how to quickly add authentication to your app using Clerk's suite of components.

  ---

  - [Customization & localization](/guides/customizing-clerk/appearance-prop/overview)
  - Learn how to customize and localize Clerk components.

  ---

  - [Custom flows](/guides/development/custom-flows/overview)
  - Expo native apps require custom flows in place of prebuilt components.

  ---

  - [Client-side helpers](/reference/expo/overview#react-hooks)
  - Learn more about Clerk's client-side helpers and how to use them.
