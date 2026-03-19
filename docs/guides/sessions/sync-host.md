# Sync auth status between your Chrome Extension and web app


> Learn how to configure your Chrome Extension to sync user authentication with your web application.

Clerk allows you to sync the authentication state from your web app to your Chrome Extension using Clerk's Sync Host feature. When a user authenticates in your web app, they will also be authenticated in your Chrome Extension.

> [!WARNING]
> Our Chrome Extension SDK currently does not fully support Sync Host on side panels. Currently, if a user authenticates in your web app, they need to close and reopen the side panel to update their auth status.

> [!WARNING]
> This guide assumes assumes that you have followed the [Chrome Extension Quickstart](/chrome-extension/getting-started/quickstart) and then the [Add React Router](/guides/development/add-react-router) guide.


  ## Add `PLASMO_PUBLIC_CLERK_SYNC_HOST` to your environment variables

  The `PLASMO_PUBLIC_CLERK_SYNC_HOST` environment variable defines the host that the Chrome Extension will sync with.

  The values for `PLASMO_PUBLIC_CLERK_SYNC_HOST` will differ between development and production environments. Using separate `.env.development` and `.env.production` files allows you to seamlessly pass the appropriate values to your builds.

  Use the following tabs to view the instructions for development versus production instances.

  
#### Development


      Add `PLASMO_PUBLIC_CLERK_SYNC_HOST` to your `.env.development` file. The value should be `http://localhost`.

      ```env
// Filename: .env.development

      PLASMO_PUBLIC_CLERK_PUBLISHABLE_KEY={{pub_key}}
      CLERK_FRONTEND_API=https://{{fapi_url}}
      PLASMO_PUBLIC_CLERK_SYNC_HOST=http://localhost
      ```
    

#### Production


      Add `PLASMO_PUBLIC_CLERK_SYNC_HOST` to your `.env.production` file. The value should be the [domain that your Clerk Frontend API](https://dashboard.clerk.com/~/domains) runs on. For example, `https://clerk.your-domain.com`.

      ```env
// Filename: .env.production

      PLASMO_PUBLIC_CLERK_PUBLISHABLE_KEY=pk_live_123
      CLERK_FRONTEND_API=https://clerk.your-domain.com
      PLASMO_PUBLIC_CLERK_SYNC_HOST=https://clerk.your-domain.com
      ```
    

  ## Add `syncHost` prop to your ``

  Add the `syncHost` prop to your Chrome Extension's `` component. This prop tells the `` which host to sync with.

  ```tsx
// Filename: src/popup/layouts/root-layout.tsx

  import { ClerkProvider, Show, UserButton } from '@clerk/chrome-extension'
  import { Link, Outlet, useNavigate } from 'react-router-dom'

  const PUBLISHABLE_KEY = process.env.PLASMO_PUBLIC_CLERK_PUBLISHABLE_KEY
  const SYNC_HOST = process.env.PLASMO_PUBLIC_CLERK_SYNC_HOST

  if (!PUBLISHABLE_KEY || !SYNC_HOST) {
    throw new Error(
      'Please add the PLASMO_PUBLIC_CLERK_PUBLISHABLE_KEY and PLASMO_PUBLIC_CLERK_SYNC_HOST to the .env.development file',
    )
  }

  export const RootLayout = () => {
    const navigate = useNavigate()

    return (
       navigate(to)}
        routerReplace={(to) => navigate(to, { replace: true })}
        publishableKey={PUBLISHABLE_KEY}
        afterSignOutUrl="/"
        syncHost={SYNC_HOST}
      >
        <div className="plasmo-w-[785px] plasmo-h-[600px]">
          <main>
            </main>
          <footer>
            
              Settings
              Home
              Sign In
              Sign Up
            
          </footer>
        </div>
      
    )
  }
  ```

  ### Hide unsupported authentication methods

  When using the Sync Host feature, authentication methods that you want to use in your web app [may not be fully supported in the Chrome Extension environment](/reference/chrome-extension/overview#authentication-options). To hide unsupported methods in your Chrome Extension, you can use the [`appearance`](/guides/customizing-clerk/appearance-prop/overview) prop with your extension's `` and `` components as demonstrated in the following examples.

  
**:**

```tsx
// Filename: src/popup/pages/sign-up.tsx

    ```


**:**

```tsx
// Filename: src/popup/pages/sign-in.tsx

    ```


  ## Configure `host_permissions`

  `host_permissions` specifies which hosts, or websites, will have permission to sync auth state with your app. It accepts an array, allowing you to add more than one host.

  In the `package.json` file, in the `manifest` object, update the `host_permissions` array. Remove `http://localhost/*` and replace with `$PLASMO_PUBLIC_CLERK_SYNC_HOST/*`, as shown in the following example:

  ```json
// Filename: package.json

  {
    // The rest of your package.json file
    "manifest": {
      "key": "$CRX_PUBLIC_KEY",
      "permissions": ["cookies", "storage"],
      "host_permissions": ["$PLASMO_PUBLIC_CLERK_SYNC_HOST/*", "$CLERK_FRONTEND_API/*"]
    }
  }
  ```

  ## Add the Extension's ID to your web app's `allowed_origins`

  To allow your Chrome Extension to sync with your web app, you must add the extension's ID to your web app's `allowed_origins`.

  > [!NOTE]
  > If you have not [configured a consistent key](/guides/development/configure-consistent-crx-id), you will have to repeat this step every time your extension's ID changes.

  1. In the Clerk Dashboard, navigate to the [**API keys**](https://dashboard.clerk.com/~/api-keys) page.
  1. Copy your Secret Key. It should start with `sk_test_` or `sk_live_` for your development and production instances, respectively.
  1. In your terminal, paste the following command. Replace `YOUR_SECRET_KEY` with your Clerk Secret Key and the `` with your extension's ID.

  The final result should resemble the following:

  ```bash
# Filename: terminal

  curl -X PATCH https://api.clerk.com/v1/instance \
    -H "Authorization: Bearer {{secret}}" \
    -H "Content-type: application/json" \
    -d '{"allowed_origins": ["chrome-extension://"]}'
  ```
