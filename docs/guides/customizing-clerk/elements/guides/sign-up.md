# Build a sign-up flow with Clerk Elements


> Learn how to build a complete sign-up form with Clerk Elements.

> [!WARNING]
> Clerk Elements is no longer in development and will not receive any updates. We're actively building a replacement for Clerk Elements with a different approach to customization, and we'll share more details soon.


> [!NOTE]
>
> - Clerk Elements is for [advanced use-cases](/guides/customizing-clerk/elements/overview#why-use-clerk-elements) that require a high-level of customization. The easiest way to implement Clerk is with our [all-in-one UI components](/reference/components/overview).
> - Clerk Elements currently only works with Next.js App Router and [Clerk Core 2](/changelog/2024-04-19).


  ## Add a sign-up route

  Create a new route in your Next.js application. The route needs to be an [optional catch-all route](https://nextjs.org/docs/pages/building-your-application/routing/dynamic-routes#optional-catch-all-segments) so the sign-up flow can handled nested paths, as shown in the following example:

  ```tsx
// Filename: app/sign-up/[[...sign-up]]/page.tsx

  'use client'

  import * as Clerk from '@clerk/elements/common'
  import * as SignUp from '@clerk/elements/sign-up'

  export default function SignUpPage() {
    return [Sign Up Root]</SignUp.Root>
  }
  ```

  You will use these two imports to build out the rest of the flow. `` manages the sign-up state and handles connecting the components to Clerk's APIs.

  > [!TIP]
  > If you're getting TypeScript errors on the `@clerk/elements` imports you probably have forgotten to set your [`moduleResolution`](https://www.typescriptlang.org/tsconfig/#moduleResolution) in `tsconfig.json` to `bundler`.

  ## Add the start step

  The Clerk authentication flows are made up of **steps**. Steps handle rendering the UI for each part of the flow. To allow users to create a sign-up attempt, the `start` step needs to be rendered. The following example does so with the `` component:

  ```tsx
// Filename: app/sign-up/[[...sign-up]]/page.tsx

  'use client'

  import * as Clerk from '@clerk/elements/common'
  import * as SignUp from '@clerk/elements/sign-up'

  export default function SignUpPage() {
    return (
      
        
          <h1>Create an account</h1>
        </SignUp.Step>
      </SignUp.Root>
    )
  }
  ```

  ## Add form fields

  Make it functional by adding input fields. The following example uses the `` component to render the `emailAddress` and `username` fields, as well as the `` component to allow users to sign up with a social connection, like Google:

  ```tsx
// Filename: app/sign-up/[[...sign-up]]/page.tsx

  'use client'

  import * as Clerk from '@clerk/elements/common'
  import * as SignUp from '@clerk/elements/sign-up'

  export default function SignUpPage() {
    return (
      
        
          <h1>Create an account</h1>

          Sign up with Google</Clerk.Connection>

          
            Username</Clerk.Label>
            
            
          </Clerk.Field>

          
            Email</Clerk.Label>
            
            
          </Clerk.Field>

          
            Password</Clerk.Label>
            
            
          </Clerk.Field>

          

          Sign up</SignUp.Action>
        </SignUp.Step>
      </SignUp.Root>
    )
  }
  ```

  `` takes care of wiring up the input with the label element, and `` will render any field-specific errors that get returned from Clerk's API. The `` component provides common actions that are used throughout the flows. In this case, using the `submit` action to render a submit button for the start form.

  ## Add verification

  As users progress through a sign-up attempt, they may be asked to **verify** a number of authentication factors in the `verifications` step. You can render a form for the user to complete verification, but each [verification strategy](/guides/customizing-clerk/elements/reference/sign-in#strategy) requires different fields. You must render the form fields conditionally for each authentication strategy your instance supports using the `` component.

  The following example demonstrates how to conditionally render a form for the `phone_code` and `email_code` strategies:

  ```tsx
// Filename: app/sign-up/[[...sign-up]]/page.tsx

  'use client'

  import * as Clerk from '@clerk/elements/common'
  import * as SignUp from '@clerk/elements/sign-up'

  export default function SignUpPage() {
    return (
      
        
          <h1>Create an account</h1>

          Sign up with Google</Clerk.Connection>

          
            Username</Clerk.Label>
            
            
          </Clerk.Field>

          
            Email</Clerk.Label>
            
            
          </Clerk.Field>

          
            Password</Clerk.Label>
            
            
          </Clerk.Field>

          Sign up</SignUp.Action>
        </SignUp.Step>

        
          
            <h1>Check your phone for an SMS</h1>

            
              Phone Code</Clerk.Label>
              
              
            </Clerk.Field>

            Verify</SignUp.Action>
          </SignUp.Strategy>

          
            <h1>Check your email</h1>

            
              Email Code</Clerk.Label>
              
              
            </Clerk.Field>

            Verify</SignUp.Action>
          </SignUp.Strategy>
        </SignUp.Step>
      </SignUp.Root>
    )
  }
  ```

  Verification is the final step in the sign-up flow. When a user has verified all required factors, the sign-up attempt will be complete, their account will be created, and they will be signed in.

  ## Accept additional fields

  Should a user attempt to sign up via Google while a username is a required field, the `continue` step will be necessary to accept the username. The `` component will display any additional required fields.

  ```tsx
// Filename: app/sign-up/[[...sign-up]]/page.tsx

  'use client'

  import * as Clerk from '@clerk/elements/common'
  import * as SignUp from '@clerk/elements/sign-up'

  export default function SignUpPage() {
    return (
      
        
          <h1>Create an account</h1>

          Sign up with Google</Clerk.Connection>

          
            Username</Clerk.Label>
            
            
          </Clerk.Field>

          
            Email</Clerk.Label>
            
            
          </Clerk.Field>

          
            Password</Clerk.Label>
            
            
          </Clerk.Field>

          Sign up</SignUp.Action>
        </SignUp.Step>

        
          <h1>Fill in missing fields</h1>

          
            Username</Clerk.Label>
            
            
          </Clerk.Field>

          Continue</SignUp.Action>
        </SignUp.Step>

        
          
            <h1>Check your phone for an SMS</h1>

            
              Phone Code</Clerk.Label>
              
              
            </Clerk.Field>

            Verify</SignUp.Action>
          </SignUp.Strategy>

          
            <h1>Check your email</h1>

            
              Email Code</Clerk.Label>
              
              
            </Clerk.Field>

            Verify</SignUp.Action>
          </SignUp.Strategy>
        </SignUp.Step>
      </SignUp.Root>
    )
  }
  ```

  If your instance has additional required fields, you can add them the same way you added the `username` field to the continue step.

  > [!NOTE]
  > Under the hood, Clerk Elements will conditionally render the fields that are necessary to complete the sign up attempt, so there's no need to check the state of the sign up attempt yourself.

  ## Customize and add styling

  Learn how to style your Clerk Elements components with the [styling guide](/guides/customizing-clerk/elements/guides/styling).

  For more extensive customization of the UI, see the additional Clerk Elements components such as [``](/guides/customizing-clerk/elements/reference/common#loading) and [``](/guides/customizing-clerk/elements/reference/common#field-state).
