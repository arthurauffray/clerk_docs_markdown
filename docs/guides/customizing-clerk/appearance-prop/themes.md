# Themes


> Clerk currently offers six prebuilt themes for you to customize the overall appearance of your Clerk app.

Clerk currently offers [six prebuilt themes](#available-themes) for you to customize the overall appearance of your Clerk application.

## Installation

1. To get started, install the `@clerk/ui` package.

   ```npm
   npm install @clerk/ui
   ```
1. To use a theme, import it from `@clerk/ui` and apply it using the [`appearance` prop](/guides/customizing-clerk/appearance-prop/overview).

## Usage

You can apply themes at **different levels** depending on your needs:

- Across all Clerk components
- All instances of a Clerk component
- A single Clerk component

For more customization options, refer to the [Advanced usage](#advanced-usage) section.

### Apply a theme to all Clerk components


  To apply a theme to all Clerk components, pass the `appearance` prop to the [``](/reference/components/clerk-provider) component. The `appearance` prop accepts the property `theme`, which can be set to a theme.

  In the following example, the "Dark" theme is applied to all Clerk components.

  ```tsx

   import { dark } from '@clerk/ui/themes'

   
     
   
  ```


  To apply a theme to all Clerk components, pass the `appearance` prop to the [`clerk()`](/reference/astro/overview) integration. The `appearance` prop accepts the property `theme`, which can be set to a theme.

  In the following example, the "Dark" theme is applied to all Clerk components.

  ```js
// Filename: astro.config.mjs

  import clerk from '@clerk/astro'
  import { dark } from '@clerk/ui/themes'

  export default defineConfig({
    integrations: [
      clerk({
        appearance: {
          theme: dark,
        },
      }),
    ],
  })
  ```


  To apply a theme to all Clerk components, pass the `appearance` prop to the [`clerk.load()`](/reference/javascript/clerk#load) method. The `appearance` prop accepts the property `theme`, which can be set to a theme.

  In the following example, the "Dark" theme is applied to all Clerk components.

  Use the following tabs to view the code necessary for each file.

  
**main.js:**

```js

    import { Clerk } from '@clerk/clerk-js'
    import { dark } from '@clerk/ui/themes'

    const clerkPubKey = import.meta.env.VITE_CLERK_PUBLISHABLE_KEY

    const clerk = new Clerk(clerkPubKey)
    await clerk.load({
      appearance: {
        theme: dark,
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


  To apply a theme to all Clerk components, pass the `appearance` prop to the [`clerkPlugin()`](/reference/vue/overview) integration. The `appearance` prop accepts the property `theme`, which can be set to a theme.

  In the following example, the "Dark" theme is applied to all Clerk components.

  ```ts
// Filename: src/main.ts

  import { createApp } from 'vue'
  import App from './App.vue'
  import { clerkPlugin } from '@clerk/vue'
  import { dark } from '@clerk/ui/themes'

  const app = createApp(App)
  app.use(clerkPlugin, {
    appearance: {
      theme: dark,
    },
  })
  app.mount('#app')
  ```


  To apply a theme to all Clerk components, pass the `appearance` prop to the [`defineNuxtConfig()`](/reference/nuxt/clerk-middleware) integration. The `appearance` prop accepts the property `theme`, which can be set to a theme.

  In the following example, the "Dark" theme is applied to all Clerk components.

  ```ts
// Filename: nuxt.config.ts

  import { dark } from '@clerk/ui/themes'

  export default defineNuxtConfig({
    modules: ['@clerk/nuxt'],
    clerk: {
      appearance: {
        theme: dark,
      },
    },
  })
  ```


  To apply a theme to all Clerk components, pass the `appearance` prop to the [`clerkPlugin()`](/reference/fastify/clerk-plugin) integration. The `appearance` prop accepts the property `theme`, which can be set to a theme.

  In the following example, the "Dark" theme is applied to all Clerk components.

  ```ts
// Filename: src/main.ts

  import Fastify from 'fastify'
  import { clerkPlugin } from '@clerk/fastify'

  const fastify = Fastify({ logger: true })

  fastify.register(clerkPlugin, {
    appearance: {
      theme: dark,
    },
  })
  ```


### Apply a theme to all instances of a Clerk component

To apply a theme to all instances of a Clerk component, you can pass the name of the Clerk component itself to the `appearance` prop.

In the following example, the "Neobrutalism" theme is applied to all instances of the [``](/reference/components/authentication/sign-in) component.


  ```tsx

  import { dark, neobrutalism } from '@clerk/ui/themes'

  
    
  
  ```


  ```js
// Filename: astro.config.mjs

  import clerk from '@clerk/astro'
  import { dark, neobrutalism } from '@clerk/ui/themes'

  export default defineConfig({
    integrations: [
      clerk({
        appearance: {
          theme: dark,
          signIn: { theme: neobrutalism },
        },
      }),
    ],
  })
  ```


  Use the following tabs to view the code necessary for each file.

  
**main.js:**

```js

    import { Clerk } from '@clerk/clerk-js'
    import { dark, neobrutalism } from '@clerk/ui/themes'

    const clerkPubKey = import.meta.env.VITE_CLERK_PUBLISHABLE_KEY

    const clerk = new Clerk(clerkPubKey)
    await clerk.load({
      appearance: {
        theme: dark,
        signIn: { theme: neobrutalism },
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


  ```ts
// Filename: src/main.ts

  import { createApp } from 'vue'
  import App from './App.vue'
  import { clerkPlugin } from '@clerk/vue'
  import { dark, neobrutalism } from '@clerk/ui/themes'

  const app = createApp(App)
  app.use(clerkPlugin, {
    appearance: {
      theme: dark,
      signIn: { theme: neobrutalism },
    },
  })
  app.mount('#app')
  ```


  ```ts
// Filename: nuxt.config.ts

  import { dark, neobrutalism } from '@clerk/ui/themes'

  export default defineNuxtConfig({
    modules: ['@clerk/nuxt'],
    clerk: {
      appearance: {
        theme: dark,
        signIn: { theme: neobrutalism },
      },
    },
  })
  ```


  ```ts
// Filename: src/main.ts

  import Fastify from 'fastify'
  import { clerkPlugin } from '@clerk/fastify'
  import { dark, neobrutalism } from '@clerk/ui/themes'

  const fastify = Fastify({ logger: true })

  fastify.register(clerkPlugin, {
    appearance: {
      theme: dark,
      signIn: { theme: neobrutalism },
    },
  })
  ```


### Apply a theme to a single Clerk component

To apply a theme to a single Clerk component, pass the `theme` property to the `appearance` prop of the Clerk component.

In the following example, the "Dark" theme is applied to the [``](/reference/components/authentication/sign-in) component.


  ```tsx

  ```


  ```vue

  <script setup lang="ts">
  // Components are automatically imported
  </script>

  <template>
    </template>
  ```


## Advanced usage

### Apply multiple themes

You can also stack themes by passing an array of themes to the `theme` property of the `appearance` prop. The themes will be applied in the order they are listed. If styles overlap, the last defined theme will take precedence.

In the following example, the "Dark" theme is applied first, then the "Neobrutalism" theme is applied on top of it.


  ```tsx

   import { dark, neobrutalism } from '@clerk/ui/themes'

   
     
   
  ```


  ```js
// Filename: astro.config.mjs

  import clerk from '@clerk/astro'
  import { dark, neobrutalism } from '@clerk/ui/themes'

  export default defineConfig({
    integrations: [
      clerk({
        appearance: {
          theme: [dark, neobrutalism],
        },
      }),
    ],
  })
  ```


  Use the following tabs to view the code necessary for each file.

  
**main.js:**

```js

    import { Clerk } from '@clerk/clerk-js'
    import { dark, neobrutalism } from '@clerk/ui/themes'

    const clerkPubKey = import.meta.env.VITE_CLERK_PUBLISHABLE_KEY

    const clerk = new Clerk(clerkPubKey)
    await clerk.load({
      appearance: {
        theme: [dark, neobrutalism],
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


  ```ts
// Filename: src/main.ts

  import { createApp } from 'vue'
  import App from './App.vue'
  import { clerkPlugin } from '@clerk/vue'
  import { dark, neobrutalism } from '@clerk/ui/themes'

  const app = createApp(App)
  app.use(clerkPlugin, {
    appearance: {
      theme: [dark, neobrutalism],
    },
  })
  app.mount('#app')
  ```


  ```ts
// Filename: nuxt.config.ts

  import { dark, neobrutalism } from '@clerk/ui/themes'

  export default defineNuxtConfig({
    modules: ['@clerk/nuxt'],
    clerk: {
      appearance: {
        theme: [dark, neobrutalism],
      },
    },
  })
  ```


  ```ts
// Filename: src/main.ts

  import Fastify from 'fastify'
  import { clerkPlugin } from '@clerk/fastify'

  const fastify = Fastify({ logger: true })

  fastify.register(clerkPlugin, {
    appearance: {
      theme: [dark, neobrutalism],
    },
  })
  ```


### Customize a theme using variables

You can customize a theme by passing an object of variables to the `variables` property of the `appearance` prop. The `variables` property is used to adjust the general styles of the component's base theme, like colors, backgrounds, typography.

> [!IMPORTANT]
> For a list of all of the variables you can customize, and for more examples on how to use the `variables` property, see the [Variables](/guides/customizing-clerk/appearance-prop/variables) docs.

In the following example, the primary color of the themes are customized.


  ```tsx

  import { dark, neobrutalism, shadesOfPurple } from '@clerk/ui/themes'

  
    
  
  ```


  ```js
// Filename: astro.config.mjs

  import clerk from '@clerk/astro'
  import { dark, neobrutalism, shadesOfPurple } from '@clerk/ui/themes'

  export default defineConfig({
    integrations: [
      clerk({
        appearance: {
          theme: [dark, neobrutalism],
          variables: { colorPrimary: 'blue' },
          signIn: {
            theme: [shadesOfPurple],
            variables: { colorPrimary: 'blue' },
          },
        },
      }),
    ],
  })
  ```


  Use the following tabs to view the code necessary for each file.

  
**main.js:**

```js

    import { Clerk } from '@clerk/clerk-js'
    import { dark, neobrutalism, shadesOfPurple } from '@clerk/ui/themes'

    const clerkPubKey = import.meta.env.VITE_CLERK_PUBLISHABLE_KEY

    const clerk = new Clerk(clerkPubKey)
    await clerk.load({
      appearance: {
        theme: [dark, neobrutalism],
        variables: { colorPrimary: 'blue' },
        signIn: {
          theme: [shadesOfPurple],
          variables: { colorPrimary: 'blue' },
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


  ```ts
// Filename: src/main.ts

  import { createApp } from 'vue'
  import App from './App.vue'
  import { clerkPlugin } from '@clerk/vue'
  import { dark, neobrutalism, shadesOfPurple } from '@clerk/ui/themes'

  const app = createApp(App)
  app.use(clerkPlugin, {
    appearance: {
      theme: [dark, neobrutalism],
      variables: { colorPrimary: 'blue' },
      signIn: {
        theme: [shadesOfPurple],
        variables: { colorPrimary: 'blue' },
      },
    },
  })
  app.mount('#app')
  ```


  ```ts
// Filename: nuxt.config.ts

  import { dark, neobrutalism, shadesOfPurple } from '@clerk/ui/themes'

  export default defineNuxtConfig({
    modules: ['@clerk/nuxt'],
    clerk: {
      appearance: {
        theme: [dark, neobrutalism],
        variables: { colorPrimary: 'blue' },
        signIn: {
          theme: [shadesOfPurple],
          variables: { colorPrimary: 'blue' },
        },
      },
    },
  })
  ```


  ```ts
// Filename: src/main.ts

  import Fastify from 'fastify'
  import { clerkPlugin } from '@clerk/fastify'

  const fastify = Fastify({ logger: true })

  fastify.register(clerkPlugin, {
    appearance: {
      theme: [dark, neobrutalism],
      variables: { colorPrimary: 'blue' },
      signIn: {
        theme: [shadesOfPurple],
        variables: { colorPrimary: 'blue' },
      },
    },
  })
  ```


## Available themes

Clerk provides six prebuilt themes:

- [The default theme](#default-theme)
- [The "Simple" theme](#simple-theme)
- [The "shadcn" theme](#shadcn-theme)
- [The "Dark" theme](#dark-theme)
- [The "Shades of Purple" theme](#shades-of-purple-theme)
- [The "Neobrutalism" theme](#neobrutalism-theme)

To explore how each theme looks before integrating it into your application, use the [Clerk's theme editor](/components/theme-editor), which lets you preview and experiment with themes in real time.

### Default theme

Applied by default when no other theme is provided. The default theme supports both light and dark modes, with light mode displaying by default unless a `color-scheme` is defined. To enable dark mode support, you need to set the `color-scheme` property in your `global.css` file.

To enable both light and dark mode support (which will respect system preferences), set `color-scheme` to `light dark`:

```css
/* Filename: global.css */

:root {
  color-scheme: light dark;
}
```

You can also control dark mode via a class, data attribute, or media query by specifying `color-scheme: dark` in your `global.css` file:

```css
/* Filename: global.css */

:root {
  color-scheme: light;
}

/* Using a class */
.dark {
  color-scheme: dark;
}

/* Using a data attribute */
[data-theme='dark'] {
  color-scheme: dark;
}

/* Using a media query (respects system preferences) */
@media (prefers-color-scheme: dark) {
  :root {
    color-scheme: dark;
  }
}
```


#### Light mode


<div style={{padding: "1rem 0", filter: "drop-shadow(rgba(0, 0, 0, 0.16) 0px 12px 24px)"}}>
  
</div>

<div style={{padding: "1rem 0", filter: "drop-shadow(rgba(0, 0, 0, 0.16) 0px 12px 24px)"}}>
  
</div>


### "Simple" theme

This theme is a stripped down "Default" theme that removes some more advanced styling techniques, making it easier to apply your own custom styles.

To use the simple theme, set `theme` to `simple`:

```tsx

```

<div style={{padding: "1rem 0"}}>
  
</div>

### "shadcn" theme

To use the shadcn theme, set `theme` to `shadcn`:

```tsx

import { shadcn } from '@clerk/ui/themes'

```

> [!IMPORTANT]
> This theme is compatible with Tailwind CSS v4 usage. If you need support for Tailwind CSS v3, pass the shadcn variables manually to your ``'s [`variables`](/guides/customizing-clerk/appearance-prop/variables) object.

When using the [shadcn/ui](https://ui.shadcn.com/) library, you can use the `shadcn` theme to apply the shadcn/ui styles to your Clerk components. This will adapt to both light and dark mode automatically.

> [!IMPORTANT]
> It's recommended to also import the `shadcn.css` file within your `global.css` file. Tailwind scans source files as plain text to detect which classes to generate - classes that only exist in external configurations won't be included in the final CSS.
>
> ```css
> @import 'tailwindcss';
> @import '@clerk/ui/themes/shadcn.css';
> ```


#### Light mode


<div style={{padding: "1rem 0", filter: "drop-shadow(rgba(0, 0, 0, 0.16) 0px 12px 24px)"}}>
  
</div>

<div style={{padding: "1rem 0", filter: "drop-shadow(rgba(0, 0, 0, 0.16) 0px 12px 24px)"}}>
  
</div>


### "Dark" theme

To use the dark theme, set `theme` to `dark`:

```tsx

import { dark } from '@clerk/ui/themes'

```

<div style={{padding: "1rem 0", filter: "drop-shadow(rgba(0, 0, 0, 0.16) 0px 12px 24px)"}}>
  
</div>

### "Shades of purple" theme

To use the shades of purple theme, set `theme` to `shadesOfPurple`:

```tsx

import { shadesOfPurple } from '@clerk/ui/themes'

```

<div style={{padding: "1rem 0", filter: "drop-shadow(rgba(0, 0, 0, 0.16) 0px 12px 24px)"}}>
  
</div>

### "Neobrutalism" theme

To use the neobrutalism theme, set `theme` to `neobrutalism`:

```tsx

import { neobrutalism } from '@clerk/ui/themes'

```

<div style={{padding: "1rem 0", filter: "drop-shadow(rgba(0, 0, 0, 0.16) 0px 12px 24px)"}}>
  
</div>
