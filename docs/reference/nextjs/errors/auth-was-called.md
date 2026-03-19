# Clerk: auth() was called but Clerk can't detect usage of clerkMiddleware()


> Learn how to handle auth() was called but Clerk can't detect usage of clerkMiddleware() when getting 404 errors in Next.js.

This error occurs when a request that is not covered by `clerkMiddleware()` gets a 404 return in a Clerk + Next.js App Router setup.

## Why this error occurs

This error commonly appears when using Clerk with Next.js and the [`clerkMiddleware()`](/reference/nextjs/clerk-middleware) helper is configured _not_ to run on static asset routes, which is part of the default setup. It can happen for the following reasons:

- [Missing ``](#missing-clerk-provider): The `` is not wrapped around the component tree where Clerk components are used.
- [Incorrect path](#incorrect-path): A typo or incorrect path is used in a static asset request.

### Missing ``

The most common cause of this error is when [`auth()`](/reference/nextjs/app-router/auth) is called **without** a [``](/reference/components/clerk-provider) wrapping the component tree where Clerk components are used.

The [``](/reference/components/clerk-provider) component provides session and user context to Clerk's hooks and components. It's recommended to wrap your entire app at the entry point with `` to make authentication globally accessible. See the [reference docs](/reference/components/clerk-provider) for other configuration options.


#### Solution

Ensure that `` is set up at a higher level in your component hierarchy than any Clerk components like [``](/reference/components/user/user-button), [``](/reference/components/control/show), or others. [The Next.js quickstart](/nextjs/getting-started/quickstart) shows how you can do this in your root layout.

```tsx
// Filename: app/layout.tsx

import { ClerkProvider } from '@clerk/nextjs'
import './globals.css'

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode
}>) {
  return (
    <html lang="en">
      <body className={`${geistSans.variable} ${geistMono.variable} antialiased`}>
        {children}
      </body>
    </html>
  )
}
```

### Incorrect path

If `` is correctly configured, it's possible this error is happening because when `auth()` was called, `clerkMiddleware()` didn't run on the request. This can occur if a request is made to a **non-existent static asset.** Static asset requests are excluded by the matcher Clerk provides and often from other `proxy.ts` matchers, so `clerkMiddleware()` doesn't run for them. A typo or incorrect path is usually the problem in these cases.

For example,

1. A user accesses `/dashboard`, which is a **valid page and matched route**.
1. That page includes an `` tag with a `src` pointing to an invalid path.
1. A 404 error is triggered because of the invalid static asset request.
1. Next.js serves the 404 response.
1. The 404 page is rendered **within the root layout** — that's where Next.js injects their 404 page/component.
1. Since `` is usually placed in the root layout, it runs, but because the request didn't match the middleware matcher, `clerkMiddleware()` never executed. As a result, `` attempts to call `auth()` **without context**, leading to one of these outcomes:
   - A `500` or `404` error in your browser's network tab.
   - `GET /{non-existing-path}.{static-asset-extension} 500 | 404` in your terminal or logs.
   - The following Clerk error in the console:
     ```text
     x [Error: Clerk: auth() was called but Clerk can't detect usage of clerkMiddleware(). Please ensure the following:
      Your Middleware exists at ./src/middleware.(ts|js)
      clerkMiddleware() is used in your Next.js Middleware.
      Your Middleware matcher is configured to match this route or page.
      If you are using the src directory, make sure the Middleware file is inside of it.

     For more details, see https://clerk.com/docs/quickstarts/nextjs
     ] {
       digest: '3346914516'
     }
     ```

#### Solution

Select the appropriate solution based on your use case:


#### Correct the static asset paths (recommended)

to a sub-layout"]}>
 

#### Scope the  to a sub-layout


The ideal solution is to fix any incorrect asset paths, as this is the **root cause** of the error and the cleanest fix. Ensure that all images, icons, or files are requested using valid URLs. When these requests succeed, no 404 is triggered, and the Clerk provider context works as expected.
  

#### Tab 3


    This fix will prevent _the Clerk error_, as it moves `` from the root layout. However, it does not resolve the underlying issue, which is a reference to a missing static asset. Your app will still have a 404 network request for the missing asset.

    If you want to protect your app against similar issues in the future or want to ensure that system-level errors (like 404s) don't rely on Clerk, you can refactor your layout structure.

    By moving `` into a subfolder layout, you allow 404 pages and other global error routes to render without needing Clerk's context.

    **Before**

    ```bash
    app/
      layout.ts  // includes ```

    **After**

    ```bash
    app/
      layout.ts       // base layout without Clerk
      (in-app)        // virtual folder - doesn't impact routing
        layout.ts     // includes page.tsx
    ```

    Here's an example of what the new Clerk layout would look like in this case:

    ```tsx
// Filename: app/(in-app)/layout.tsx

    import { ClerkProvider } from '@clerk/nextjs'

    export default function AppLayout({ children }: { children: React.ReactNode }) {
      return {children}
    }
    ```

    Or loading Clerk built-in components:

    ```tsx
// Filename: app/(in-app)/layout.tsx

    import { ClerkProvider, Show, SignInButton, SignUpButton, UserButton } from '@clerk/nextjs'

    export default function AppLayout({ children }: { children: React.ReactNode }) {
      return (
        
          <header className="flex justify-end items-center p-4 gap-4 h-16">
            
              </header>
          {children}
        
      )
    }
    ```

    This ensures the root layout (which handles top-level errors like 404s) does not rely on Clerk, avoiding the middleware mismatch error entirely.
