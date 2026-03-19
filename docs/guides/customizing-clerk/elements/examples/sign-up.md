# Sign-up


> Examples of prebuilt sign-up flows with Clerk Elements.

> [!WARNING]
> Clerk Elements is no longer in development and will not receive any updates. We're actively building a replacement for Clerk Elements with a different approach to customization, and we'll share more details soon.


## Email/password + email verification

The following example demonstrates a sign-up flow with email and password fields. After the user submits their email and password, they are prompted to verify their email address.

Before you build your sign-up flow, you need to configure the appropriate settings in Clerk:

1. In the Clerk Dashboard, navigate to the [**User & authentication**](https://dashboard.clerk.com/~/user-authentication/user-and-authentication) page.
1. Enable **Sign-up with email** and **Sign-in with email**.
1. Select the **Password** tab and enable **Sign-up with password**.

```tsx
// Filename: app/sign-up/[[...sign-up]]/page.tsx

'use client'

import * as Clerk from '@clerk/elements/common'
import * as SignUp from '@clerk/elements/sign-up'

export default function SignUpPage() {
  return (
    <div className="grid w-full flex-grow items-center bg-black px-4 sm:justify-center">
      
        
          <header className="text-center">
            
            <h1 className="mt-4 text-xl font-medium tracking-tight text-white">
              Create an account
            </h1>
          </header>
          
          <div className="space-y-4">
            
              Email address</Clerk.Label>
              
              
            </Clerk.Field>
            
              Password</Clerk.Label>
              
              
            </Clerk.Field>
          </div>
          
          
            Sign Up
          </SignUp.Action>
          <p className="text-center text-sm text-zinc-400">
            Have an account?{' '}
            
              Sign in
            </Clerk.Link>
          </p>
        </SignUp.Step>
        
          <header className="text-center">
            
            <h1 className="mt-4 text-xl font-medium tracking-tight text-white">
              Verify email code
            </h1>
          </header>
          
          
            
              Email code</Clerk.Label>
              
              
            </Clerk.Field>
            
              Finish registration
            </SignUp.Action>
          </SignUp.Strategy>
          <p className="text-center text-sm text-zinc-400">
            Have an account?{' '}
            
              Sign in
            </Clerk.Link>
          </p>
        </SignUp.Step>
      </SignUp.Root>
    </div>
  )
}
```

## Email/password + username + email verification

The following example demonstrates a sign-up flow with email, password, and username fields. After the user submits their email, password, and username, they are prompted to verify their email address.

Before you build your sign-up flow, you need to configure the appropriate settings in Clerk:

1. In the Clerk Dashboard, navigate to the [**User & authentication**](https://dashboard.clerk.com/~/user-authentication/user-and-authentication) page.
1. Enable **Sign-up with email** and **Sign-in with email**.
1. Select the **Username** tab and enable **Sign-up with username** and **Sign-in with username**.
   > [!IMPORTANT]
> Usernames only support Latin-based characters. This restriction helps protect against Unicode spoofing and homograph attacks, where characters from non-Latin scripts can be used to impersonate users.

1. Select the **Password** tab and enable **Sign-up with password**.

```tsx
// Filename: app/sign-up/[[...sign-up]]/page.tsx

'use client'

import * as Clerk from '@clerk/elements/common'
import * as SignUp from '@clerk/elements/sign-up'

export default function SignUpPage() {
  return (
    <div className="grid w-full flex-grow items-center bg-zinc-100 px-4 sm:justify-center">
      
        
          <header className="text-center">
            
            <h1 className="mt-4 text-xl font-medium tracking-tight text-zinc-950">
              Create an account
            </h1>
          </header>
          
          <div className="space-y-4">
            
              Email</Clerk.Label>
              
              
            </Clerk.Field>
            
              Password</Clerk.Label>
              
              
            </Clerk.Field>
          </div>
          
            Sign Up
          </SignUp.Action>

          <p className="text-center text-sm text-zinc-500">
            Already have an account?{' '}
            
              Sign in
            </Clerk.Link>
          </p>
        </SignUp.Step>
        
          <header className="text-center">
            
            <h1 className="mt-4 text-xl font-medium tracking-tight text-zinc-950">
              Verify email code
            </h1>
          </header>
          
          
            
              Email code</Clerk.Label>
              
              
            </Clerk.Field>
            
              Verify
            </SignUp.Action>
          </SignUp.Strategy>
          <p className="text-center text-sm text-zinc-500">
            Already have an account?{' '}
            
              Sign in
            </Clerk.Link>
          </p>
        </SignUp.Step>
        
          <header className="text-center">
            
            <h1 className="mt-4 text-xl font-medium tracking-tight text-zinc-950">
              Continue registration
            </h1>
          </header>
          
          
            Username</Clerk.Label>
            
            
          </Clerk.Field>
          
            Continue
          </SignUp.Action>
          <p className="text-center text-sm text-zinc-500">
            Already have an account?{' '}
            
              Sign in
            </Clerk.Link>
          </p>
        </SignUp.Step>
      </SignUp.Root>
    </div>
  )
}
```
