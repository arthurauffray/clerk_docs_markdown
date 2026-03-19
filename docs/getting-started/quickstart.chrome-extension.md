# Chrome Extension Quickstart (Plasmo)


> Add authentication and user management to your Chrome Extension with Clerk using Plasmo.

## Enable Native API

  In the Clerk Dashboard, navigate to the [**Native applications**](https://dashboard.clerk.com/~/native-applications) page and ensure that the Native API is enabled. This is required to integrate Clerk in your native application.


  ## Configure your authentication options

  When creating your Clerk application in the Clerk Dashboard, your authentication options will depend on how you configure your Chrome Extension. Chrome Extensions can be used as a popup, a side panel, or in conjunction with a web app. Popups and side panels have limited authentication options. [Learn more about what options are available.](/reference/chrome-extension/overview#authentication-options)

  This guide will use a popup.

  ## Create a new Chrome Extension app

  [Plasmo](https://docs.plasmo.com/framework) is a browser extension framework that includes hot reloading and creating development and production extension builds easily from the same code.

  Plasmo strongly recommends using `pnpm`, so this guide will only use `pnpm`-based examples.

  If you don't already have a Chrome Extension app, run the following commands to create a new one using Plasmo. This sets up a new extension with Tailwind CSS preconfigured and a `src/` directory by default. You can remove either option if you don't need them.

  ```bash
# Filename: terminal

  pnpm create plasmo --with-tailwindcss --with-src clerk-chrome-extension
  cd clerk-chrome-extension
  ```

  ## Install `@clerk/chrome-extension`

  The [Clerk Chrome Extension SDK](/reference/chrome-extension/overview) gives you access to prebuilt components, hooks, and helpers to make user authentication easier.

  Run the following command to install the SDK:

  ```bash
# Filename: terminal

  pnpm add @clerk/chrome-extension
  ```

  ## Set your Clerk API keys

  Plasmo offers [several options](https://docs.plasmo.com/framework/env) for environment variable files, as the same codebase can be used for development and production builds, as well as for targeting different browsers. This guide uses `.env.development` and `.env.chrome` files.

  
    Add the following keys to your `.env.development` file. These keys can always be retrieved from the [**API keys**](https://dashboard.clerk.com/~/api-keys) page in the Clerk Dashboard.
  

  
    1. In the Clerk Dashboard, navigate to the [**API keys**](https://dashboard.clerk.com/~/api-keys) page.
    1. In the **Quick Copy** section, select **Chrome Extension** and copy your Clerk Publishable Key and Frontend API URL.
    1. Paste your keys into your `.env.development` file.

    The final result should resemble the following:
  

  ```env
// Filename: .env.development

  PLASMO_PUBLIC_CLERK_PUBLISHABLE_KEY={{pub_key}}
  CLERK_FRONTEND_API=https://{{fapi_url}}
  ```

  ## Add `` and Clerk components to your app

  The [``](/reference/components/clerk-provider) component provides session and user context to Clerk's hooks and components. It's recommended to wrap your entire app at the entry point with `` to make authentication globally accessible. See the [reference docs](/reference/components/clerk-provider) for other configuration options.


  Copy and paste the following code into your `popup.tsx` file. This:

  - Adds the `` to your app, providing Clerk's authentication context to your app.
  - Creates a header with Clerk's [prebuilt components](/reference/components/overview) to allow users to sign in and out, and display different content for signed-in and signed-out users.

  ```tsx
// Filename: src/popup.tsx

  import {
    ClerkProvider,
    Show,
    SignInButton,
    SignUpButton,
    UserButton,
  } from '@clerk/chrome-extension'

  import { CountButton } from '~features/count-button'

  import '~style.css'

  const PUBLISHABLE_KEY = process.env.PLASMO_PUBLIC_CLERK_PUBLISHABLE_KEY

  if (!PUBLISHABLE_KEY) {
    throw new Error('Please add the PLASMO_PUBLIC_CLERK_PUBLISHABLE_KEY to the .env.development file')
  }

  function IndexPopup() {
    return (
      
        <div className="plasmo-flex plasmo-items-center plasmo-justify-center plasmo-h-[600px] plasmo-w-[800px] plasmo-flex-col">
          <header className="plasmo-w-full">
            
              </header>
          <main className="plasmo-grow">
            </main>
        </div>
      
    )
  }

  export default IndexPopup
  ```

  This example uses the following components:

  - [``](/reference/components/control/show): Children of this component can only be seen while **signed in**.
- [``](/reference/components/control/show): Children of this component can only be seen while **signed out**.
- [``](/reference/components/user/user-button): Shows the signed-in user's avatar. Selecting it opens a dropdown menu with account management options.
- [``](/reference/components/unstyled/sign-in-button): An unstyled component that links to the sign-in page. In this example, since no props or [environment variables](/guides/development/clerk-environment-variables) are set for the sign-in URL, this component links to the [Account Portal sign-in page](/guides/account-portal/overview#sign-in).
- [``](/reference/components/unstyled/sign-up-button): An unstyled component that links to the sign-up page. In this example, since no props or [environment variables](/guides/development/clerk-environment-variables) are set for the sign-up URL, this component links to the [Account Portal sign-up page](/guides/account-portal/overview#sign-up).


  ## Update `` props for Chrome Extension navigation

  To avoid navigation errors, set the `afterSignOutUrl`, `signInFallbackRedirectUrl` and `signUpFallbackRedirectUrl` props for ``. Chrome Extensions don't use an `http` URL, such as `http://localhost:3000`. Instead, they use a `chrome-extension://` URL appended with an unique extension ID called a CRX ID. This URL is what you will pass to these props.

  ```tsx
// Filename: src/popup.tsx

  import {
    ClerkProvider,
    Show,
    SignInButton,
    SignUpButton,
    UserButton,
  } from '@clerk/chrome-extension'

  import { CountButton } from '~features/count-button'

  import '~style.css'

  const PUBLISHABLE_KEY = process.env.PLASMO_PUBLIC_CLERK_PUBLISHABLE_KEY
  const EXTENSION_URL = chrome.runtime.getURL('.')

  if (!PUBLISHABLE_KEY) {
    throw new Error('Please add the PLASMO_PUBLIC_CLERK_PUBLISHABLE_KEY to the .env.development file')
  }

  function IndexPopup() {
    return (
      
        <div className="plasmo-flex plasmo-items-center plasmo-justify-center plasmo-h-[600px] plasmo-w-[800px] plasmo-flex-col">
          <header className="plasmo-w-full">
            
              </header>
          <main className="plasmo-grow">
            </main>
        </div>
      
    )
  }

  export default IndexPopup
  ```

  ## Create a consistent CRX ID for your extension

  Chrome Extensions have a unique CRX ID that rotates by default, which can cause errors with the Clerk integration. To avoid these problems, ensure that you have a **consistent** CRX ID in both development and production for your extension by following these steps:

  1. Visit Plasmo Itero's [Generate Keypairs](https://itero.plasmo.com/tools/generate-keypairs) tool.
  1. Select **Generate KeyPairs**.
  1. Save the **Private Key** somewhere secure in case you need it in the future. Save the **Public Key** and the **CRX ID** for the next steps.

  ## Create an `.env.chrome` file to store your public key

  Create an `.env.chrome` file and add your public key to it, as shown in the following example:

  ```env
// Filename: .env.chrome

  CRX_PUBLIC_KEY=
  ```

  ## Edit your `package.json` to use the new public key

  Plasmo [uses the `package.json` to generate a `manifest.json` on build](https://docs.plasmo.com/framework#where-is-the-manifestjson-file), and allows for the use of environment variables in `package.json`.

  In your `package.json`, in the `manifest` object:

  - Set the `key` value to `"$CRX_PUBLIC_KEY"`. This helps configure the consistent CRX ID for your extension.
  - Set the `permissions` array to include `"cookies"` and `"storage"`. `permissions` specifies which permissions your extension requires.
  - Set or update the `host_permissions` array to include `"http://localhost/*"` and `"$CLERK_FRONTEND_API/*"`. `host_permissions` specifies which hosts, or websites, have permission to sync auth state with your app.

  ```json
// Filename: package.json

  {
    // The rest of your package.json file
    "manifest": {
      "key": "$CRX_PUBLIC_KEY",
      "permissions": ["cookies", "storage"],
      "host_permissions": ["http://localhost/*", "$CLERK_FRONTEND_API/*"]
    }
  }
  ```

  ## Use `pnpm dev` to start your development server and create a build

  Plasmo facilitates Chrome Extension development by automatically "hot loading" the app whenever you save a changed file in the project. This ensures the `build/chrome-mv3-dev` folder remains up to date. Without the plugin, you would need to manually execute the build command and reload your Chrome Extension after each change. Plasmo automates this process, streamlining development.

  Run the following command to start your development environment. This also creates the build in `build/chrome-mv3-dev`, and rebuilds when you make changes to the extension.

  ```bash
# Filename: terminal

  pnpm dev
  ```

  ## Load your Chrome Extension into your Chromium-based browser

  To load your Chrome Extension, follow these steps:

  1. Open Chrome or a Chromium-based browser and navigate to `chrome://extensions`.
  1. In the top-right, enable **Developer mode**.
  1. In the top-left, select **Load unpacked**.
  1. Navigate to where your project is located and select the `build/chrome-mv3-dev` folder. Then select **Select**. Your extension will now be loaded and shown in the list of extensions.
  1. Confirm that the ID shown in your extension matches the CRX ID you saved [earlier](#create-a-consistent-crx-id-for-your-extension).

  ## Test your Chrome Extension

  In your Chrome browser, open the extension popup. Ensure that the `` appears, and that selecting it opens the `` modal. Sign in and ensure that the `` appears in the header.

  > [!WARNING]
  > After signing up or signing in, your popup may appear to crash. Closing and reopening the popup should restart the extension and you should be signed in.
  >
  > Your extension does not yet have anything to handle routing, and by default, the Clerk components attempt to redirect the user. See [the guide on adding React Router to your Chrome Extension](/guides/development/add-react-router) to add routing to your extension.


## Next steps

Learn how to add routing to your Chrome Extension, keep user sessions in sync, and how to use Clerk's client-side helpers using the following guides.


  - [Add React Router](/guides/development/add-react-router)
  - Learn how to add React Router to your Chrome Extension.

  ---

  - [Sync your Chrome Extension with your web app](/guides/sessions/sync-host)
  - Learn how to configure your Chrome Extension to sync user authentication with your web app.

  ---

  - [createClerkClient()](/reference/chrome-extension/create-clerk-client)
  - Learn how to use Clerk's `createClerkClient()` function in a background service worker to ensure that the user's session is always fresh.

  ---

  - [Deploy a Chrome Extension to production](/guides/development/deployment/chrome-extension)
  - Learn how to deploy your Clerk Chrome Extension to production.

  ---

  - [Configure a consistent CRX ID](/guides/development/configure-consistent-crx-id)
  - Learn how to configure a consistent CRX ID to ensure your extension has a stable, unchanging key.

  ---

  - [Clerk Chrome Extension SDK Reference](/reference/chrome-extension/overview)
  - Learn about the Clerk Chrome Extension SDK and how to integrate it into your app.
