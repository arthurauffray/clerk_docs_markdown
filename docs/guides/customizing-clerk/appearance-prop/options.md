# Options` prop


> Utilize Clerk's options prop in order to change the layout of the <SignIn /> and <SignUp /> components, as well as set important links to your support, terms and privacy pages.

The `options` property can be used to change the layout of the [``](/reference/components/authentication/sign-in) and [``](/reference/components/authentication/sign-up) components, as well as set important links to your support, terms, and privacy pages.

## Properties

- **`animations`** `boolean`

  Whether to enable animations inside the components. Defaults to `true`.

    ---

- **`helpPageUrl`** `string`

  The URL to your help page.

    ---

- **`logoImageUrl`** `string`

  The URL to your logo image. By default, the components will use the logo you've set in the Clerk Dashboard. This option is helpful when you need to display different logos for different themes, for example: white logo on dark themes, black logo on light themes.

    ---

- **`logoLinkUrl`** `string`

  Controls where the browser will redirect to after the user clicks the application logo. If a URL is provided, it will be used as the `href` of the link. If a value is not passed in, the components will use the Home URL as set in the Clerk Dashboard. Defaults to `undefined`.

    ---

- **`logoPlacement`** `'inside' | 'outside'`

  The placement of your logo. Defaults to `'inside'`.

    ---

- **`privacyPageUrl`** `string`

  The URL to your privacy page.

    ---

- **`shimmer`** `boolean`

  This option enables the shimmer animation for the avatars of `` and ``. Defaults to `true`.

    ---

- **`showOptionalFields`** `boolean`

  Whether to show optional fields on the sign in and sign up forms. Defaults to `false`.

    ---

- **`socialButtonsPlacement`** `'bottom' | 'top'`

  The placement of your social buttons. Defaults to `'top'`.

    ---

- **`socialButtonsVariant`** `'blockButton' | 'iconButton' | 'auto'`

  The variant of your social buttons. By default, the components will use `blockButton` if you have less than 3 social providers enabled, otherwise `iconButton` will be used.

    ---

- **`termsPageUrl`** `string`

  The URL to your terms page.

    ---

- **`unsafe_disableDevelopmentModeWarnings`** `boolean`

  Whether development warnings show up in development mode. **Only enable this if you want to preview how the components will look in production.**


## Usage


  Pass the `appearance` prop to the [``](/reference/components/clerk-provider) component. The `appearance` prop accepts the `options` property, which can be used to apply different changes to the widget.

  ```tsx

  
    
  
  ```


  Pass the `appearance` prop to the [`clerk()`](/reference/astro/overview) integration. The `appearance` prop accepts the `options` property, which can be used to apply different changes to the widget.

  ```js
// Filename: astro.config.mjs

  import clerk from '@clerk/astro'

  export default defineConfig({
    integrations: [
      clerk({
        appearance: {
          options: {
            socialButtonsPlacement: 'bottom',
            socialButtonsVariant: 'iconButton',
            termsPageUrl: 'https://clerk.com/terms',
          },
        },
      }),
    ],
  })
  ```


  Pass the `appearance` prop to the [`clerk.load()`](/reference/javascript/clerk#load) method. The `appearance` prop accepts the `options` property, which can be used to apply different changes to the widget.

  Use the following tabs to view the code necessary for each file.

  
**main.js:**

```js

    import { Clerk } from '@clerk/clerk-js'

    const clerkPubKey = import.meta.env.VITE_CLERK_PUBLISHABLE_KEY

    const clerk = new Clerk(clerkPubKey)
    await clerk.load({
      appearance: {
        options: {
          socialButtonsPlacement: 'bottom',
          socialButtonsVariant: 'iconButton',
          termsPageUrl: 'https://clerk.com/terms',
        },
      },
    })

    if (clerk.isSignedIn) {
      document.getElementById('app').innerHTML = `
          <div id="user-button"></div>
        `

      const userButtonDiv = document.getElementById('user-button')

      clerk.mountUserButton(userButtonDiv)
    } else {
      document.getElementById('app').innerHTML = `
          <div id="sign-in"></div>
        `

      const signInDiv = document.getElementById('sign-in')

      clerk.mountSignIn(signInDiv)
    }
    ```


**index.html:**

```html
    <!doctype html>
    <html lang="en">
      <head>
        <meta charset="UTF-8" />
        <link rel="icon" type="image/svg+xml" href="/vite.svg" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>Clerk + JavaScript App</title>
      </head>
      <body>
        <div id="app"></div>
        <script type="module" src="main.js" async crossorigin="anonymous"></script>
      </body>
    </html>
    ```


  Pass the `appearance` prop to the [`clerkPlugin()`](/reference/vue/overview) integration. The `appearance` prop accepts the `options` property, which can be used to apply different changes to the widget.

  ```ts
// Filename: src/main.ts

  import { createApp } from 'vue'
  import App from './App.vue'
  import { clerkPlugin } from '@clerk/vue'

  const app = createApp(App)
  app.use(clerkPlugin, {
    appearance: {
      options: {
        socialButtonsPlacement: 'bottom',
        socialButtonsVariant: 'iconButton',
        termsPageUrl: 'https://clerk.com/terms',
      },
    },
  })
  app.mount('#app')
  ```


  Pass the `appearance` prop to the [`defineNuxtConfig()`](/reference/nuxt/clerk-middleware) integration. The `appearance` prop accepts the `options` property, which can be used to apply different changes to the widget.

  ```ts
// Filename: nuxt.config.ts

  export default defineNuxtConfig({
    modules: ['@clerk/nuxt'],
    clerk: {
      appearance: {
        options: {
          socialButtonsPlacement: 'bottom',
          socialButtonsVariant: 'iconButton',
          termsPageUrl: 'https://clerk.com/terms',
        },
      },
    },
  })
  ```


  Pass the `appearance` prop to the [`clerkPlugin()`](/reference/fastify/clerk-plugin) integration. The `appearance` prop accepts the `options` property, which can be used to apply different changes to the widget.

  ```ts
// Filename: src/main.ts

  import Fastify from 'fastify'
  import { clerkPlugin } from '@clerk/fastify'

  const fastify = Fastify({ logger: true })

  fastify.register(clerkPlugin, {
    appearance: {
      options: {
        socialButtonsPlacement: 'bottom',
        socialButtonsVariant: 'iconButton',
        termsPageUrl: 'https://clerk.com/terms',
      },
    },
  })
  ```
