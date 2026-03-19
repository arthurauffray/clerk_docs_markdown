# <GoogleOneTap />` component


> Clerk's <GoogleOneTap /> component renders a UI for authenticating users with Google's One Tap API.

> [!IMPORTANT]
> To use Google One Tap with Clerk, you must [enable Google as a social connection in the Clerk Dashboard](/guides/configure/auth-strategies/social-connections/google#configure-for-your-production-instance) and make sure to use custom credentials.

The `` component renders the [Google One Tap](https://developers.google.com/identity/gsi/web/guides/features) UI so that users can use a single button to sign-up or sign-in to your Clerk application with their Google accounts.

By default, this component will redirect users back to the page where the authentication flow started. However, you can override this with [force redirect URL props](#properties) or [force redirect URL environment variables](/guides/development/clerk-environment-variables#sign-in-and-sign-up-redirects).

> [!TIP]
> `` does not render if the user is already signed into your Clerk application, so there's no need to manually check if a user is signed in yourself before rendering it.


  ## Example

  The following example includes a basic implementation of the `` component. You can use this as a starting point for your own implementation.

  
    ```tsx
// Filename: app/sign-in/[[...sign-in]]/page.tsx

    import { GoogleOneTap } from '@clerk/nextjs'

    export default function Page() {
      return }
    ```
  

  
    ```jsx
// Filename: src/App.tsx

    import { GoogleOneTap } from '@clerk/react'

    function App() {
      return }

    export default App
    ```
  

  
    ```tsx
// Filename: app/routes/sign-in.tsx

    import { GoogleOneTap } from '@clerk/react-router'

    export default function Page() {
      return }
    ```
  

  
    ```astro
// Filename: pages/sign-in.astro

    ---
    import { GoogleOneTap } from '@clerk/astro/components'
    ---

    ```
  

  
    > [!NOTE]
> This component is for Expo web projects. For native iOS and Android apps, use the [native components](/reference/expo/native-components/overview) from `@clerk/expo/native` instead.


    ```jsx
// Filename: /app/sign-in-google.web.tsx

    import { GoogleOneTap } from '@clerk/expo/web'

    export default function Page() {
      return }
    ```
  

  
    ```tsx
// Filename: app/routes/sign-in.tsx

    import { GoogleOneTap } from '@clerk/remix'

    export default function Page() {
      return }
    ```
  

  
    ```tsx
// Filename: app/routes/sign-in.tsx

    import { GoogleOneTap } from '@clerk/tanstack-react-start'
    import { createFileRoute } from '@tanstack/react-router'

    export const Route = createFileRoute('/sign-in')({
      component: SignIn,
    })

    function SignIn() {
      return }
    ```
  

  
    ```vue
// Filename: sign-in.vue

    <script setup lang="ts">
    import { GoogleOneTap } from '@clerk/vue'
    </script>

    <template>
      </template>
    ```
  

  
    ```vue
// Filename: sign-in.vue

    <script setup lang="ts">
    // Components are automatically imported
    </script>

    <template>
      </template>
    ```
  


  ## Usage with JavaScript

  The methods in this section are available on instances of the [`Clerk`](/reference/javascript/clerk) class and are used to render and control the `` component.

  ### `openGoogleOneTap()`

  Opens the `` component.

  ```typescript
  function openGoogleOneTap(params: GoogleOneTapProps): void
  ```

  - See [`GoogleOneTapProps`](#properties)

  #### `openGoogleOneTap()` usage

  ```js
// Filename: main.js

  import { Clerk } from '@clerk/clerk-js'

  // Initialize Clerk with your Clerk Publishable Key
  const clerkPubKey = import.meta.env.VITE_CLERK_PUBLISHABLE_KEY

  const clerk = new Clerk(clerkPubKey)
  await clerk.load()

  const params = {
    cancelOnTapOutside: false,
    itpSupport: false,
    fedCmSupport: false,
  }
  clerk.openGoogleOneTap(params)
  ```

  ### `closeGoogleOneTap()`

  Closes the `` component.

  ```typescript
  function closeGoogleOneTap(): void
  ```

  #### `closeGoogleOneTap()` usage

  ```js
// Filename: main.js

  import { Clerk } from '@clerk/clerk-js'

  // Initialize Clerk with your Clerk Publishable Key
  const clerkPubKey = import.meta.env.VITE_CLERK_PUBLISHABLE_KEY

  const clerk = new Clerk(clerkPubKey)
  await clerk.load()

  const params = {
    cancelOnTapOutside: false,
    itpSupport: false,
    fedCmSupport: false,
  }
  clerk.openGoogleOneTap(params)

  // Do something else

  clerk.closeGoogleOneTap()
  ```

  ### `authenticateWithGoogleOneTap()`

  Authenticates the user with a token generated from Google identity services. Also sets the user's current session to active.

  ```typescript
  function authenticateWithGoogleOneTap(
    props?: AuthenticateWithGoogleOneTapParams,
  ): Promise
  ```

  #### `AuthenticateWithGoogleOneTapParams`

  - **`token?`** `string`

  A Google authentication token from Google identity services.


  #### `authenticateWithGoogleOneTap()` usage

  ```js
// Filename: main.js

  import { Clerk } from '@clerk/clerk-js'

  // Initialize Clerk with your Clerk Publishable Key
  const clerkPubKey = import.meta.env.VITE_CLERK_PUBLISHABLE_KEY

  const clerk = new Clerk(clerkPubKey)
  await clerk.load()

  // Optionally, you can set redirect URLs.
  const customUrls = {
    signInUrl: '/sign-in',
    signUpUrl: '/sign-up',
  }
  // Initiate the authentication flow.
  const signInOrUp = await clerk.authenticateWithGoogleOneTap({ token: 'xxxx' })
  // Set the session as active, and handle any navigation or redirects
  await clerk.handleGoogleOneTapCallback(signInOrUp, customUrls)
  ```

  ### `handleGoogleOneTapCallback()`

  Completes a Google One Tap redirection flow started by [`authenticateWithGoogleOneTap()`](#authenticate-with-google-one-tap). Also calls [`Clerk.setActive()`](/reference/javascript/clerk#set-active) and performs a custom navigation if given a custom navigation function.

  ```typescript
  function handleGoogleOneTapCallback(
    signInOrUp: SignInResource | SignUpResource,
    params: HandleOAuthCallbackParams,
    customNavigate?: (to: string) => Promise<unknown>,
  ): Promise<unknown>
  ```

  See [`authenticateWithGoogleOneTap()` usage](#authenticate-with-google-one-tap-usage) for an example of how to use `handleGoogleOneTapCallback()`.

  #### `handleGoogleOneTapCallback()` params

  - **`signInOrUp`** <code>[SignInResource](/reference/javascript/sign-in) | [SignUpResource](/reference/javascript/sign-up)</code>

  The `SignIn` or `SignUp` object returned from `authenticateWithGoogleOneTap()`.

      ---

- **`params`** [`HandleOAuthCallbackParams`](/reference/javascript/clerk#handle-o-auth-callback-params)

  An object containing redirect URLs. Useful if you want to set URLs specific to Google One Tap. Otherwise, consider using [environment variables](/guides/development/clerk-environment-variables) to set redirect URLs.

      ---

- **`customNavigate?`** `(to: string) => Promise<unknown>`

  A function that overrides Clerk's default navigation behavior, allowing custom handling of navigation during sign-up and sign-in flows.


## Properties

- **`cancelOnTapOutside?`** `boolean`

  If `true`, the One Tap prompt closes automatically if the user clicks outside of the prompt. Defaults to `true`.

    ---

- **`itpSupport?`** `boolean`

  If `true`, enables the [ITP-specific UX](https://developers.google.com/identity/gsi/web/guides/itp) when One Tap is rendered on ITP browsers such as Chrome on iOS, Safari, and FireFox. Defaults to `true`.

    ---

- **`fedCmSupport?`** `boolean`

  If `true`, enables Google One Tap to use [the FedCM API](https://developers.google.com/privacy-sandbox/3pcd/fedcm) to sign users in. See Google's docs on [best practices when disabling FedCM support](https://developers.google.com/identity/gsi/web/guides/display-google-one-tap#do_not_cover_google_one_tap). Defaults to `true`

    ---

- **`signInForceRedirectUrl?`** `string`

  Useful if you want to redirect to a path specific to Google One Tap users. If provided, this URL will **always** be redirected to after the user signs in, overriding any [`` redirect URL props](/reference/components/clerk-provider#properties) or [redirect URL environment variables](/guides/development/clerk-environment-variables#sign-in-and-sign-up-redirects).

    ---

- **`signUpForceRedirectUrl?`** `string`

  Useful if you want to redirect to a path specific to Google One Tap users. If provided, this URL will **always** be redirected to after the user signs up, overriding any [`` redirect URL props](/reference/components/clerk-provider#properties) or [redirect URL environment variables](/guides/development/clerk-environment-variables#sign-in-and-sign-up-redirects).


## Limitations

- If your application will use the Google API on behalf of your users, the `` component is not recommended, as Google does not provide Clerk with an access or refresh token that you can use.
- Users with the 1Password browser extension may not be able to render the Google One Tap UI. They must disable this extension.
- When testing in development, if you select the `X` button to close the Google One Tap UI, you may encounter [a cooldown](https://developers.google.com/identity/gsi/web/guides/features#exponential_cooldown) that prevents you from rendering it again for a period of time. To bypass the cooldown, remove the `g_state` cookie.
