# Build your own sign-up page with prebuilt components on web


> Learn how to add custom sign-up page to your Expo app with Clerk's prebuilt components.

By default, the [``](/guides/development/web-support/custom-sign-in-or-up-page) component handles signing in and signing up, but if you'd like to have a dedicated sign-up page, this guide shows you how to use the [``](/reference/components/authentication/sign-up) component to build a custom sign-up page.

To set up a single sign-in-or-up page, follow the [custom sign-in-or-up page guide](/guides/development/web-support/custom-sign-in-or-up-page).

This guide uses [Expo Router](https://docs.expo.dev/router/introduction/) and the [platform-specific extensions](https://docs.expo.dev/router/create-pages/#platform-specific-extensions) to build the sign-up page specifically for the **web** platform.


  ## Build a sign-up page

  The following example demonstrates how to render the [``](/reference/components/authentication/sign-up) component.

  ```tsx
// Filename: /app/sign-up.web.tsx

  import { SignUp } from '@clerk/expo/web'

  export default function Page() {
    return }
  ```

  ## Visit your new page

  To run your project, use the following command:

  ```npm
  npm run web
  ```

  Visit your new custom pages locally at [localhost:8081/sign-up](http://localhost:8081/sign-up).


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
