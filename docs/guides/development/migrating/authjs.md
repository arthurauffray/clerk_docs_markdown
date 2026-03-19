# Migrate from Auth.js to Clerk


> Learn how to migrate an application using Auth.js to use Clerk for authentication.

This guide shows how to migrate an application using Auth.js (formerly NextAuth.js) to use Clerk for authentication.


  ## Install `@clerk/nextjs`

  Clerk's Next.js SDK gives you access to prebuilt [components](/reference/components/overview), [hooks](/reference/nextjs/overview#client-side-helpers), and [helpers](/reference/nextjs/overview) for Next.js Server Components, Route Handlers and Middleware. Run the following command to install it:

  ```npm
  npm install @clerk/nextjs
  ```

  ## Set environment variables

  Add the following code to your `.env` file to set your Publishable Key and Secret Key.

  ```env
// Filename: .env

  NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY={{pub_key}}
  CLERK_SECRET_KEY={{secret}}
  ```

  ## Wrap your Next.js app in ``

  Remove the `` provider from Auth.js and replace it with ``.

  The [``](/reference/components/clerk-provider) component provides session and user context to Clerk's hooks and components. It's recommended to wrap your entire app at the entry point with `` to make authentication globally accessible. See the [reference docs](/reference/components/clerk-provider) for other configuration options.


  
**App Router:**

```tsx
// Filename: app/layout.tsx

    import { ClerkProvider } from '@clerk/nextjs'
    import './globals.css'

    export default function RootLayout({ children }: { children: React.ReactNode }) {
      return (
        <html lang="en">
          <body>
            {children}
          </body>
        </html>
      )
    }
    ```


**Pages Router:**

```tsx
// Filename: pages/_app.tsx

    import '@/styles/globals.css'
    import { ClerkProvider } from '@clerk/nextjs'
    import type { AppProps } from 'next/app'
    function MyApp({ Component, pageProps }: AppProps) {
      return (
        
          
      )
    }
    export default MyApp
    ```


  ## Set up sign-up and sign-in UI

  ### Account Portal

  Account Portal is the fastest way to authenticate your app. Clerk's Account Portal hosts the ``, ``, ``, and other components for your application. Read more about [Account Portal](/guides/account-portal/overview).

  To use the Account Portal, remove the routes that mount the Auth.js sign-in and sign-up UI. Replace the links to those routes with the [``](/reference/components/unstyled/sign-in-button) or [``](/reference/components/unstyled/sign-out-button) components.

  ### Self-hosted UI

  If Clerk's Account Portal pages aren't a good fit your app, you can build a custom sign-in and sign-up UI in one of two ways:

  - use the [prebuilt components](/guides/development/custom-sign-in-or-up-page), such as the [``](/reference/components/authentication/sign-in) and [``](/reference/components/authentication/sign-up) components
  - build a [fully custom UI using the Clerk API](/guides/development/custom-flows/overview), leveraging Clerk's React hooks such as [`useSignIn()`](/reference/hooks/use-sign-in) and [`useSignUp()`](/reference/hooks/use-sign-up)

  ## Protect your app

  With Clerk, you can control access to your application in a few different ways. One way is to use Clerk's Middleware to protect your entire application, or specific routes. Another way is to use Clerk's components to conditionally render UI based on the user's authentication state. You can hide or show UI based on whether the user is signed in or not.

  ### Control access to your app with Clerk Middleware

  You will need to remove the Auth.js Middleware from your application, and replace it with the Clerk's Middleware helper, `clerkMiddleware()`.

  Auth.js's middleware always rejects unauthorized requests. You may have additionally configured the Next.js middleware config to protect specific private routes. You will need to make note of this configuration so you can recreate it.

  Clerk's Middleware gives you fine-grained control over handling the authenticated state and will, by default, run for your entire application.

  The example below is a basic configuration that does not protect any routes. All routes are public and you must opt-in to protection for routes. Read the [`clerkMiddleware()`](/reference/nextjs/clerk-middleware) documentation to learn more about how you can configure your Middleware.

  
  > [!IMPORTANT]
  >
  > If you're using Next.js ≤15, name your file `middleware.ts` instead of `proxy.ts`. The code itself remains the same; only the filename changes.


  ```tsx
// Filename: proxy.ts

  import { clerkMiddleware } from '@clerk/nextjs/server'

  export default clerkMiddleware()

  export const config = {
    matcher: [
      '/((?!.*\\..*|_next).*)', // Don't run middleware on static files
      '/', // Run middleware on index page
      '/(api|trpc)(.*)', // Run middleware on API routes
    ],
  }
  ```

  ### Control access to your app with Clerk's components

  To conditionally render UI when the user is signed in, wrap it with [``](/reference/components/control/show).

  To conditionally render UI when the user is _not_ signed in, wrap it with [``](/reference/components/control/show).

  ```tsx
// Filename: app/page.tsx

  import { Show } from '@clerk/nextjs'

  export default function Home() {
    return (
      <div>
        
          <p>This content is public. Only signed out users can see this.</p>
        
        
          <p>This content is private. Only signed in users can see this.</p>
        
      </div>
    )
  }
  ```

  ## Read user and session data

  ### Server-side

  Replace any Auth.js `getServerSession(req, res, authOptions)` with Clerk's helpers.

  
#### App Router


      You can replace Auth.js's `setServerSession()` with Clerk's [`auth()`](/reference/nextjs/app-router/auth) helper in order to read your user data.

      ```tsx
// Filename: app/page.tsx

      import { auth, currentUser } from '@clerk/nextjs/server'

      export default async function Page() {
        const { userId } = await auth()
        console.log(userId)

        return <p>Home Page</p>
      }
      ```
    

#### Pages Router


      You can replace Auth.js's `setServerSession()` with Clerk's [`getAuth()`](/reference/nextjs/pages-router/get-auth) helper in order to read your user data.

      ```tsx
// Filename: pages/index.tsx

      export async function getServerSideProps(context) {
        const session = getAuth(context.req)

        return { props: { ...buildClerkProps(ctx.req) } }
      }
      ```
    

  ### Client Side

  Replace Auth.js's `useSession()` hook with Clerk's hooks.

  The [`useAuth()`](/reference/hooks/use-auth) hook can be used to retrieve basic authentication information. The [`useUser()`](/reference/hooks/use-user) hook can be used to retrieve the full [`User`](/reference/javascript/user) object, which includes information about the user, such as their first name, emails, phone numbers, and more.

  ```tsx
// Filename: app/page.tsx

  'use client'
  import { useAuth, useUser } from '@clerk/nextjs'

  export default function Home() {
    const { userId, sessionId } = useAuth()
    const { isSignedIn, user } = useUser()
    console.log(userId, sessionId, isSignedIn, user)

    return <p>Home Page</p>
  }
  ```

  ## User IDs as Foreign Keys

  When you migrate to Clerk, you will likely need to resolve the foreign key that you used in your database. If you used the `userId` from NextAuth.js, you could resolve this issue with one of the following two options:

  - [Use Clerk's `externalId` field](#use-clerks-external-id-field)
  - [Update your Auth.js database](#update-your-database)

  ### Use Clerk's `externalId` field

  When you migrate user data from Auth.js to Clerk, Clerk generates new user IDs for each user. If you are using existing user IDs as foreign keys in your database (e.g. in a `user_id` column), you can save those IDs as the user's `externalId` in Clerk. This `externalId` can be included in the session token by adding the following [customization](/guides/sessions/customize-session-tokens). The following example will set the user's ID to be `externalId` if one is present, otherwise, it will use the Clerk's user ID.

  ```json
  {
    "userId": "{{user.external_id || user.id}}"
  }
  ```

  
#### App Router


      To access the `userId` from the session claims, you can use the `auth()` helper.

      ```tsx
// Filename: app/page.tsx

      import { auth } from '@clerk/nextjs/server'

      export default async function Page() {
        const { sessionClaims } = await auth()

        if (!sessionClaims) {
          return <p>Not signed in</p>
        }

        const userId = sessionClaims.sub

        return <p>Welcome user {userId}</p>
      }
      ```
    

#### Pages Router


      To access the `userId` from the session claims, you can use the `getAuth()` helper.

      ```tsx
// Filename: pages/index.tsx

      import { getAuth, buildClerkProps } from '@clerk/nextjs/server'
      import { GetServerSideProps } from 'next'

      export const getServerSideProps: GetServerSideProps = async (ctx) => {
        const { isAuthenticated, userId } = getAuth(ctx.req)

        if (!isAuthenticated) {
          // handle user is not signed in.
        }

        const {
          sessionClaims: { userId },
        } = getAuth(req)
        console.log(userId)

        return { props: { ...buildClerkProps(ctx.req) } }
      }
      ```
    

  > [!NOTE]
  > You can not access the above from the client-side. If you are using one of Clerk's hooks, then you will need to check if `externalID` exists. If it doesn't, then read the `userId`.

  ### Update your database

  Alternatively, after the data migration, you can update all the user IDs stored in your database as a foreign key to the new Clerk user IDs.

  You can read more about user IDs and user data migration in the [Migration tool README](https://github.com/clerk/migration-tool#handle-existing-user-ids-and-foreign-key-constraints).

  ## Create a Clerk production instance

  Every Clerk application has a `Development` and a `Production` instance. Before you start migrating user data, you need to configure your Clerk `Production` instance and migrate your Auth.js users directly into that instance. The [Deploying to Production](/guides/development/deployment/production) page covers creating a `Production` instance.

  You can migrate a small set of users on the `Development` instance for testing/staging. To enable importing users to your `Development` instance, add `IMPORT_TO_DEV_INSTANCE=true` to the `.env` for the migration tool.

  ## Migrate user data from Auth.js to Clerk

  This walkthrough will help you move user data from your existing database to Clerk.

  To retain the user data in your database for easy querying, see the [guide on data synchronization with webhooks](/guides/development/webhooks/syncing).

  1. Clone `github.com/clerk/migration-tool`

  1. Create an `.env` file in the root of the cloned repository with the `CLERK_SECRET_KEY` **of your `Production` instance**.

  1. Export all the user data from your database into a `users.json` file. The file should be in the following format:

     ```json
// Filename: users.json

     [
       {
         "userId": "string",
         "email": "email",
         "firstName": "string (optional)",
         "lastName": "string (optional)",
         "password": "string (optional)",
         "passwordHasher": "argon2 | argon | bcrypt | md5 | pbkdf2_sha256 | pbkdf2_sha256_django | pbkdf2_sha1 | scrypt_firebase"
       }
     ]
     ```

  1. If you already have an API endpoint in your Auth.js app that returns a list of users, you can use that. Otherwise, you will need to query your database to obtain the user information, or use an export function from a database management tool.

     The example below is a SQL query that would return the user information in the correct format for the migration tool.

     ```sql
     SELECT id as userId, email, name FROM users
     ```

  1. Edit the `.env` file in the migration tool, and add your Clerk Secret Key as `CLERK_SECRET_KEY`.

  1. Run the tool with `npm start`

  1. Check that your users are listed on the [**Users**](https://dashboard.clerk.com/~/users) page in the Clerk Dashboard. If the users appear to have imported correctly, verify by signing in to your application secured by Clerk with your user account.

  1. Check for an error log for any users that were not migrated successfully.

  ## Finding further support for migrating from Auth.js to Clerk

  This guide covers the most common steps that you would take for the migration. If you have more complex integrations with Auth.js that are not covered here, don't hesitate to reach out in the [Clerk Discord](https://clerk.com/discord) by creating a post in the [Support channel](https://discord.gg/bmPVkeqKzZ).
