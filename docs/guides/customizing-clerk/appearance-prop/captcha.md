# captcha` prop


> Utilize Clerk's captcha prop in order to change the appearance of the CAPTCHA widget.

The `captcha` property can be used to change the appearance of the CAPTCHA widget.

## Properties

- **`theme`** `'auto' | 'light' | 'dark'`

  The CAPTCHA widget theme. Defaults to `auto`.

    ---

- **`size`** `'normal' | 'flexible' | 'compact'`

  The CAPTCHA widget size. Defaults to `normal`.

    ---

- **`language`** `string`

  The CAPTCHA widget language/locale. When setting the language for CAPTCHA, this is how localization is prioritized:

- **`appearance.captcha.language`: Set by this `language` property.** `localization.locale`: Set by the [`localization` prop on ``](/guides/customizing-clerk/localization). Some languages are [supported by Clerk](/guides/customizing-clerk/localization) but not by Cloudflare Turnstile, which is used for the CAPTCHA widget. See [Cloudflare Turnstile's supported languages](https://developers.cloudflare.com/turnstile/reference/supported-languages). `en-US`: Clerk's default language.


## Usage


  To customize the CAPTCHA widget, pass the `appearance` prop to the [``](/reference/components/clerk-provider) component. The `appearance` prop accepts the property `captcha`, which can be used to apply different changes to the widget.

  In the following example, the CAPTCHA is customized to use the dark theme, a flexible size, and Spanish as the display language.

  ```tsx

  
    
  
  ```


  To customize the CAPTCHA widget, pass the `appearance` prop to the [`clerk()`](/reference/astro/overview) integration. The `appearance` prop accepts the property `captcha`, which can be used to apply different changes to the widget.

  In the following example, the CAPTCHA is customized to use the dark theme, a flexible size, and Spanish as the display language.

  ```js
// Filename: astro.config.mjs

  import clerk from '@clerk/astro'

  export default defineConfig({
    integrations: [
      clerk({
        appearance: {
          captcha: {
            theme: 'dark',
            size: 'flexible',
            language: 'es-ES',
          },
        },
      }),
    ],
  })
  ```


  To customize the CAPTCHA widget, pass the `appearance` prop to the [`clerk.load()`](/reference/javascript/clerk#load) method. The `appearance` prop accepts the property `captcha`, which can be used to apply different changes to the widget.

  In the following example, the CAPTCHA is customized to use the dark theme, a flexible size, and Spanish as the display language.

  Use the following tabs to view the code necessary for each file.

  
**main.js:**

```js

    import { Clerk } from '@clerk/clerk-js'

    const clerkPubKey = import.meta.env.VITE_CLERK_PUBLISHABLE_KEY

    const clerk = new Clerk(clerkPubKey)
    await clerk.load({
      appearance: {
        captcha: {
          theme: 'dark',
          size: 'flexible',
          language: 'es-ES',
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


  To customize the CAPTCHA widget, pass the `appearance` prop to the [`clerkPlugin()`](/reference/vue/overview) integration. The `appearance` prop accepts the property `captcha`, which can be used to apply different changes to the widget.

  In the following example, the CAPTCHA is customized to use the dark theme, a flexible size, and Spanish as the display language.

  ```ts
// Filename: src/main.ts

  import { createApp } from 'vue'
  import App from './App.vue'
  import { clerkPlugin } from '@clerk/vue'

  const app = createApp(App)
  app.use(clerkPlugin, {
    appearance: {
      captcha: {
        theme: 'dark',
        size: 'flexible',
        language: 'es-ES',
      },
    },
  })
  app.mount('#app')
  ```


  To customize the CAPTCHA widget, pass the `appearance` prop to the [`defineNuxtConfig()`](/reference/nuxt/clerk-middleware) integration. The `appearance` prop accepts the property `captcha`, which can be used to apply different changes to the widget.

  In the following example, the CAPTCHA is customized to use the dark theme, a flexible size, and Spanish as the display language.

  ```ts
// Filename: nuxt.config.ts

  export default defineNuxtConfig({
    modules: ['@clerk/nuxt'],
    clerk: {
      appearance: {
        captcha: {
          theme: 'dark',
          size: 'flexible',
          language: 'es-ES',
        },
      },
    },
  })
  ```


  To customize the CAPTCHA widget, pass the `appearance` prop to the [`clerkPlugin()`](/reference/fastify/clerk-plugin) integration. The `appearance` prop accepts the property `captcha`, which can be used to apply different changes to the widget.

  In the following example, the CAPTCHA is customized to use the dark theme, a flexible size, and Spanish as the display language.

  ```ts
// Filename: src/main.ts

  import Fastify from 'fastify'
  import { clerkPlugin } from '@clerk/fastify'

  const fastify = Fastify({ logger: true })

  fastify.register(clerkPlugin, {
    appearance: {
      captcha: {
        theme: 'dark',
        size: 'flexible',
        language: 'es-ES',
      },
    },
  })
  ```
