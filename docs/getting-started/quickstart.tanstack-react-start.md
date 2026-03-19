# TanStack React Start Quickstart


> Learn how to use Clerk to quickly and easily add secure authentication and user management to your TanStack React Start application.

## Create a new TanStack React Start app

  If you don't already have a TanStack React Start app, run the following commands to [create a new one](https://tanstack.com/start/latest/docs/framework/react/quick-start).

  ```npm
  npm create @tanstack/start@latest clerk-tanstack-react-start
  cd clerk-tanstack-react-start
  npm install
  ```

  ## Install `@clerk/tanstack-react-start`

  The [Clerk TanStack React Start SDK](/reference/tanstack-react-start/overview) gives you access to prebuilt components, hooks, and helpers to make user authentication easier.

  Run the following command to install the SDK:

  ```npm
// Filename: terminal

  npm install @clerk/tanstack-react-start
  ```

  
    ## Set your Clerk API keys

    Add the following keys to your `.env` file. These keys can always be retrieved from the [**API keys**](https://dashboard.clerk.com/~/api-keys) page in the Clerk Dashboard.

    ```sh
# Filename: .env

    CLERK_PUBLISHABLE_KEY={{pub_key}}
    CLERK_SECRET_KEY={{secret}}
    ```
  

  ## Add `clerkMiddleware()` to your app

  [`clerkMiddleware()`](/reference/tanstack-react-start/clerk-middleware) grants you access to user authentication state throughout your app. It also allows you to protect specific routes from unauthenticated users. To add `clerkMiddleware()` to your app, follow these steps:

  1. Create a `src/start.ts` file with the following code:

     ```tsx
// Filename: src/start.ts

     import { clerkMiddleware } from '@clerk/tanstack-react-start/server'
     import { createStart } from '@tanstack/react-start'

     export const startInstance = createStart(() => {
       return {
         requestMiddleware: [clerkMiddleware()],
       }
     })
     ```

  1. By default, `clerkMiddleware()` will not protect any routes. All routes are public and you must opt-in to protection for routes. See the [`clerkMiddleware()` reference](/reference/tanstack-react-start/clerk-middleware) to learn how to require authentication for specific routes.

  ## Add `` to your app

  The [``](/reference/components/clerk-provider) component provides session and user context to Clerk's hooks and components. It's recommended to wrap your entire app at the entry point with `` to make authentication globally accessible. See the [reference docs](/reference/components/clerk-provider) for other configuration options.


  Add the `` component to your app's root route, as shown in the following example:

  ```tsx
// Filename: src/routes/__root.tsx

  import { ClerkProvider } from '@clerk/tanstack-react-start'
  import { HeadContent, Scripts, createRootRoute } from '@tanstack/react-router'
  import { TanStackRouterDevtools } from '@tanstack/react-router-devtools'

  import Header from '../components/Header'

  import appCss from '../styles.css?url'

  export const Route = createRootRoute({
    head: () => ({
      meta: [
        {
          charSet: 'utf-8',
        },
        {
          name: 'viewport',
          content: 'width=device-width, initial-scale=1',
        },
        {
          title: 'TanStack Start Starter',
        },
      ],
      links: [
        {
          rel: 'stylesheet',
          href: appCss,
        },
      ],
    }),

    shellComponent: RootDocument,
  })

  function RootDocument({ children }: { children: React.ReactNode }) {
    return (
      <html lang="en">
        <head>
          </head>
        <body>
          
            {children}
          
          </body>
      </html>
    )
  }
  ```

  ## Protect your pages

  ### Client-side

  To protect your pages on the client-side, you can use Clerk's [prebuilt control components](/reference/components/overview#control-components) that control the visibility of content based on the user's authentication state.

  The following example uses the following components:

  - [``](/reference/components/control/show): Children of this component can only be seen while **signed in**.
- [``](/reference/components/control/show): Children of this component can only be seen while **signed out**.
- [``](/reference/components/user/user-button): Shows the signed-in user's avatar. Selecting it opens a dropdown menu with account management options.
- [``](/reference/components/unstyled/sign-in-button): An unstyled component that links to the sign-in page. In this example, since no props or [environment variables](/guides/development/clerk-environment-variables) are set for the sign-in URL, this component links to the [Account Portal sign-in page](/guides/account-portal/overview#sign-in).
- [``](/reference/components/unstyled/sign-up-button): An unstyled component that links to the sign-up page. In this example, since no props or [environment variables](/guides/development/clerk-environment-variables) are set for the sign-up URL, this component links to the [Account Portal sign-up page](/guides/account-portal/overview#sign-up).


  ```tsx
// Filename: src/routes/index.tsx

  import { UserButton, Show, SignInButton, SignUpButton } from '@clerk/tanstack-react-start'
  import { createFileRoute } from '@tanstack/react-router'

  export const Route = createFileRoute('/')({
    component: Home,
  })

  function Home() {
    return (
      <div>
        <h1>Index Route</h1>
        
          </div>
    )
  }
  ```

  ### Server-side

  To protect your routes, create a [server function](https://tanstack.com/start/latest/docs/framework/react/guide/server-functions) that checks the user's authentication state via the [`auth()`](/reference/tanstack-react-start/auth) method. If the user is not authenticated, they are redirected to a sign-in page. If authenticated, the user's `userId` is passed to the route, allowing access to the `` component, which welcomes the user and displays their `userId`. The [`beforeLoad()`](https://tanstack.com/router/latest/docs/framework/react/api/router/RouteOptionsType#beforeload-method) method ensures authentication is checked before loading the page, and the [`loader()`](https://tanstack.com/router/latest/docs/framework/react/api/router/RouteOptionsType#loader-method) method returns the user data for use in the component.

  > [!TIP]
  > Ensure that your app has the [TanStack Start server handler](https://tanstack.com/start/latest/docs/framework/react/guide/server-routes#handling-server-route-requests) configured in order for your server routes to work.

  ```tsx
// Filename: src/routes/index.tsx

  import { createFileRoute, redirect } from '@tanstack/react-router'
  import { createServerFn } from '@tanstack/react-start'
  import { auth } from '@clerk/tanstack-react-start/server'

  const authStateFn = createServerFn().handler(async () => {
    const { isAuthenticated, userId } = await auth()

    if (!isAuthenticated) {
      // This will error because you're redirecting to a path that doesn't exist yet
      // You can create a sign-in route to handle this
      // See https://clerk.com/docs/tanstack-react-start/guides/development/custom-sign-in-or-up-page
      throw redirect({
        to: '/sign-in',
      })
    }

    return { userId }
  })

  export const Route = createFileRoute('/')({
    component: Home,
    beforeLoad: async () => await authStateFn(),
    loader: async ({ context }) => {
      return { userId: context.userId }
    },
  })

  function Home() {
    const state = Route.useLoaderData()

    return <h1>Welcome! Your ID is {state.userId}!</h1>
  }
  ```

  ## Run your project

Run your project with the following command:

```npm
npm run dev
```


  ## Create your first user

1. Visit your app's homepage at [http://localhost:3000](http://localhost:3000).
1. Select "Sign up" on the page and authenticate to create your first user.


  
    > [!IMPORTANT]
    > To make configuration changes to your Clerk development instance, claim the Clerk keys that were generated for you by selecting **Configure your application** in the bottom right of your app. This will associate the application with your Clerk account.
  


## Next steps

Learn more about Clerk components, how to customize them, and how to use Clerk's client-side helpers using the following guides.


  - [Prebuilt components](/reference/components/overview)
  - Learn how to quickly add authentication to your app using Clerk's suite of components.

  ---

  - [Customization & localization](/guides/customizing-clerk/appearance-prop/overview)
  - Learn how to customize and localize Clerk components.

  ---

  - [Create a custom sign-in-or-up page](/tanstack-react-start/guides/development/custom-sign-in-or-up-page)
  - Learn how to create a custom sign-in-or-up page with Clerk components.

  ---

  - [Protect content and read user data](/tanstack-react-start/guides/users/reading)
  - Learn how to use Clerk's hooks and helpers to protect content and read user data in your TanStack React Start app.

  ---

  - [Client-side helpers (hooks)](/reference/tanstack-react-start/overview#client-side-helpers)
  - Learn more about Clerk's client-side helpers and how to use them.

  ---

  - [Clerk TanStack React Start SDK Reference](/reference/tanstack-react-start/overview)
  - Learn about the Clerk TanStack React Start SDK and how to integrate it into your app.
