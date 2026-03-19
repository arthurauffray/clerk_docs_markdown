# Build a sign-in flow with Clerk Elements


> Learn how to build a complete sign-in form with Clerk Elements.

> [!WARNING]
> Clerk Elements is no longer in development and will not receive any updates. We're actively building a replacement for Clerk Elements with a different approach to customization, and we'll share more details soon.


> [!NOTE]
>
> - Clerk Elements is for [advanced use-cases](/guides/customizing-clerk/elements/overview#why-use-clerk-elements) that require a high-level of customization. The easiest way to implement Clerk is with our [all-in-one UI components](/reference/components/overview).
> - Clerk Elements currently only works with Next.js App Router and [Clerk Core 2](/changelog/2024-04-19).


  ## Add a sign-in route

  Create a new route in your Next.js application. The route needs to be an [optional catch-all route](https://nextjs.org/docs/pages/building-your-application/routing/dynamic-routes#optional-catch-all-segments) so the sign-in flow can handled nested paths, as shown in the following example:

  ```tsx
// Filename: app/sign-in/[[...sign-in]]/page.tsx

  'use client'

  import * as Clerk from '@clerk/elements/common'
  import * as SignIn from '@clerk/elements/sign-in'

  export default function SignInPage() {
    return [Sign In Root]</SignIn.Root>
  }
  ```

  You will use these two imports to build out the rest of the flow. `` manages the sign-in state and handles connecting the components to Clerk's APIs.

  > [!TIP]
  > If you're getting TypeScript errors on the `@clerk/elements` imports you probably have forgotten to set your [`moduleResolution`](https://www.typescriptlang.org/tsconfig/#moduleResolution) in `tsconfig.json` to `bundler`.

  ## Add the start step

  The Clerk authentication flows are made up of **steps**. Steps handle rendering the UI for each part of the flow. To allow users to create a sign-in attempt, the `start` step needs to be rendered. The following example does so with the `` component:

  ```tsx
// Filename: app/sign-in/[[...sign-in]]/page.tsx

  'use client'

  import * as Clerk from '@clerk/elements/common'
  import * as SignIn from '@clerk/elements/sign-in'

  export default function SignInPage() {
    return (
      
        
          <h1>Sign in to your account</h1>
        </SignIn.Step>
      </SignIn.Root>
    )
  }
  ```

  ## Add form fields

  Make it functional by adding input fields. The following example uses the `` component to render an `identifier` field, as well as the `` component to allow users to sign in with a social connection, like Google:

  ```tsx
// Filename: app/sign-in/[[...sign-in]]/page.tsx

  'use client'

  import * as Clerk from '@clerk/elements/common'
  import * as SignIn from '@clerk/elements/sign-in'

  export default function SignInPage() {
    return (
      
        
          <h1>Sign in to your account</h1>

          Sign in with Google</Clerk.Connection>

          
            Email</Clerk.Label>
            
            
          </Clerk.Field>

          Continue</SignIn.Action>
        </SignIn.Step>
      </SignIn.Root>
    )
  }
  ```

  `` takes care of wiring up the input with the label element, and `` will render any field-specific errors that get returned from Clerk's API. The `` component provides common actions that are used throughout the flows. In this case, using the `submit` action to render a submit button for the start form.

  > [!NOTE]
  > If your Clerk instance supports signing in with Google and doesn't require multi-factor authentication (MFA), you should be able to complete a sign-in with the components rendered so far.

  ## Add verification

  As users progress through a sign-in attempt, they may be asked to **verify** a number of authentication factors in the `verifications` step. You can render a form for the user to complete verification, but each [verification strategy](/guides/customizing-clerk/elements/reference/sign-in#strategy) requires different fields. You must render the form fields conditionally for each authentication strategy your instance supports using the `` component.

  The following example demonstrates how to conditionally render a form for the `email_code` strategy:

  ```tsx
// Filename: app/sign-in/[[...sign-in]]/page.tsx

  'use client'

  import * as Clerk from '@clerk/elements/common'
  import * as SignIn from '@clerk/elements/sign-in'

  export default function SignInPage() {
    return (
      
        
          <h1>Sign in to your account</h1>

          Sign in with Google</Clerk.Connection>

          
            Email</Clerk.Label>
            
            
          </Clerk.Field>

          Continue</SignIn.Action>
        </SignIn.Step>

        
          
            <h1>Check your email</h1>
            <p>
              We sent a code to .
            </p>

            
              Email code</Clerk.Label>
              
              
            </Clerk.Field>

            Continue</SignIn.Action>
          </SignIn.Strategy>
        </SignIn.Step>
      </SignIn.Root>
    )
  }
  ```

  Verification is the final step in the sign-in flow. When a user has verified all required factors, the sign-in attempt will be complete and they will be signed in.

  ## Add password support

  If your instance is configured to support authenticating with passwords, you must add a few additional steps and verification strategies. You can choose if you want to support providing a password in the `start` step with an additional field, or as an additional verification strategy. For this guide, add it as a standalone verification strategy.

  ```tsx
// Filename: app/sign-in/[[...sign-in]]/page.tsx

  'use client'

  import * as Clerk from '@clerk/elements/common'
  import * as SignIn from '@clerk/elements/sign-in'

  export default function SignInPage() {
    return (
      
        
          <h1>Sign in to your account</h1>

          Sign in with Google</Clerk.Connection>

          
            Email</Clerk.Label>
            
            
          </Clerk.Field>

          Continue</SignIn.Action>
        </SignIn.Step>

        
          
            <h1>Check your email</h1>
            <p>
              We sent a code to .
            </p>

            
              Email code</Clerk.Label>
              
              
            </Clerk.Field>

            Continue</SignIn.Action>
          </SignIn.Strategy>

          
            <h1>Enter your password</h1>

            
              Password</Clerk.Label>
              
              
            </Clerk.Field>

            Continue</SignIn.Action>
            Forgot password?</SignIn.Action>
          </SignIn.Strategy>

          
            <h1>Check your email</h1>
            <p>
              We sent a code to .
            </p>

            
              Email code</Clerk.Label>
              
              
            </Clerk.Field>

            Continue</SignIn.Action>
          </SignIn.Strategy>
        </SignIn.Step>

        
          <h1>Forgot your password?</h1>

          
            Reset password
          </SignIn.SupportedStrategy>

          Go back</SignIn.Action>
        </SignIn.Step>

        
          <h1>Reset your password</h1>

          
            New password</Clerk.Label>
            
            
          </Clerk.Field>

          
            Confirm password</Clerk.Label>
            
            
          </Clerk.Field>

          Reset password</SignIn.Action>
        </SignIn.Step>
      </SignIn.Root>
    )
  }
  ```

  To enable users to reset their passwords, you can add the following additional steps:

  1. `forgot-password` –  Renders [``](/guides/customizing-clerk/elements/reference/sign-in#supported-strategy), which initiates the reset process, whereby an email code is sent to the user for verification.
     - `` is also used in the `forgot-password` and `choose-strategy` steps to trigger verification of a supported strategy.
  1. `reset-password` – Allows a verified user to input a new password. If your instance has been set up to accept SMS codes, you can also use `reset_password_phone_code`.

  > [!NOTE]
  > If your instance isn't configured to use passwords, or any of the strategies outlined here, Clerk Elements will log a warning to the console during development.

  ## Customize and add styling

  Learn how to style your Clerk Elements components with the [styling guide](/guides/customizing-clerk/elements/guides/styling).

  For more extensive customization of the UI, see the additional Clerk Elements components such as [``](/guides/customizing-clerk/elements/reference/common#loading) and [``](/guides/customizing-clerk/elements/reference/common#field-state).
