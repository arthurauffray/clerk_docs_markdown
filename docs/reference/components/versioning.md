# Component Versioning


> Learn how Clerk versions its components, and how to specify a specific version if necessary.

Clerk's components are versioned independently from the core Clerk JavaScript SDK, and updates are pushed out when a new release is triggered. This allows most applications to receive regular component updates and refinements without needing to manually update dependencies.

For users that rely on advanced customization of Clerk's components, it is recommended that you specify an explicit component version. This ensures your application is not impacted by component updates that might change the DOM structure in a way that breaks custom CSS.

## `@clerk/ui` package

Clerk's components are published under the `@clerk/ui` npm package. While this package is published separately to npm, it is intended to be used in combination with Clerk's core JavaScript SDK, where it provides the implementation for Clerk's prebuilt components.

## Specifying a component version

To pin Clerk's components to a specific version in your application, install the `@clerk/ui` package using your preferred package manager.

```npm
npm install @clerk/ui@latest
```

Next, import `ui` from the `@clerk/ui` package and pass it to your Clerk configuration. The setup varies by SDK:


#### Next.js / React


Pass `ui` to the `` component.

```tsx
import { ClerkProvider } from '@clerk/nextjs' // or '@clerk/react'
import { ui } from '@clerk/ui'

export default function Layout({ children }) {
  return {children}
}
```
  

#### Astro


    Pass `ui` to the `clerk()` integration in your Astro config.

    ```ts
// Filename: astro.config.mjs

    import { defineConfig } from 'astro/config'
    import clerk from '@clerk/astro'
    import { ui } from '@clerk/ui'

    export default defineConfig({
      integrations: [clerk({ ui })],
    })
    ```
  

#### Vue


    Pass `ui` to the `clerkPlugin` options.

    ```ts
// Filename: src/main.ts

    import { createApp } from 'vue'
    import App from './App.vue'
    import { clerkPlugin } from '@clerk/vue'
    import { ui } from '@clerk/ui'

    const app = createApp(App)
    app.use(clerkPlugin, {
      publishableKey: import.meta.env.VITE_CLERK_PUBLISHABLE_KEY,
      ui,
    })
    app.mount('#app')
    ```
  

#### Nuxt


    Pass `ui` to the `clerk` property in your Nuxt config.

    ```ts
// Filename: nuxt.config.ts

    import { ui } from '@clerk/ui'

    export default defineNuxtConfig({
      modules: ['@clerk/nuxt'],
      clerk: {
        ui,
      },
    })
    ```
  

#### JavaScript


Pass `ui` to `clerk.load()`.

```js
import { Clerk } from '@clerk/clerk-js'
import { ui } from '@clerk/ui'

const clerk = new Clerk('{{pub_key}}')
await clerk.load({ ui })
```
