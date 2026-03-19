# Sign-in


> Examples of prebuilt sign-in flows with Clerk Elements.

> [!WARNING]
> Clerk Elements is no longer in development and will not receive any updates. We're actively building a replacement for Clerk Elements with a different approach to customization, and we'll share more details soon.


## Username/password

The following example demonstrates a simple username/password sign-in flow.

Before you build your sign-in flow, you need to configure the appropriate settings in Clerk:

1. In the Clerk Dashboard, navigate to the [**User & authentication**](https://dashboard.clerk.com/~/user-authentication/user-and-authentication) page.
1. Select the **Username** tab and enable **Sign-up with username** and **Sign-in with username**.
   > [!IMPORTANT]
> Usernames only support Latin-based characters. This restriction helps protect against Unicode spoofing and homograph attacks, where characters from non-Latin scripts can be used to impersonate users.

1. Select the **Password** tab and enable **Sign-up with password**.

```tsx
// Filename: app/sign-in/[[...sign-in]]/page.tsx

'use client'

import * as Clerk from '@clerk/elements/common'
import * as SignIn from '@clerk/elements/sign-in'

export default function SignInPage() {
  return (
    <div className="grid w-full flex-grow items-center bg-zinc-100 px-4 sm:justify-center">
      
        
          <header className="text-center">
            
            <h1 className="mt-4 text-xl font-medium tracking-tight text-zinc-950">
              Sign in to Clover
            </h1>
          </header>
          
          <div className="space-y-4">
            
              Username</Clerk.Label>
              
              
            </Clerk.Field>
            
              Password</Clerk.Label>
              
              
            </Clerk.Field>
          </div>
          
            Sign In
          </SignIn.Action>
          <p className="text-center text-sm text-zinc-500">
            No account?{' '}
            
              Create an account
            </Clerk.Link>
          </p>
        </SignIn.Step>
      </SignIn.Root>
    </div>
  )
}
```

## Google OAuth

The following example demonstrates a simple Google OAuth sign-in flow.

Before you build your sign-in flow, you need to configure the appropriate settings in Clerk:

1. In the Clerk Dashboard, navigate to the [**User & authentication**](https://dashboard.clerk.com/~/user-authentication/user-and-authentication) page.
1. Ensure that all settings are disabled.
1. In the navigation sidenav, select [**SSO connections**](https://dashboard.clerk.com/~/user-authentication/sso-connections).
1. Ensure that _only_ **Google** is enabled.

```tsx
// Filename: app/sign-in/[[...sign-in]]/page.tsx

'use client'

import * as Clerk from '@clerk/elements/common'
import * as SignIn from '@clerk/elements/sign-in'

export default function SignInPage() {
  return (
    <div className="grid w-full flex-grow items-center bg-black px-4 sm:justify-center">
      
        
          <header className="text-center">
            
            <h1 className="mt-4 text-xl font-medium tracking-tight text-white">
              Sign in to Clover
            </h1>
          </header>
          
          <div className="space-y-2">
            
              
              Login with Google
            </Clerk.Connection>
          </div>
          <p className="text-center text-sm text-neutral-400">
            No account?{' '}
            
              Create an account
            </Clerk.Link>
          </p>
        </SignIn.Step>
      </SignIn.Root>
    </div>
  )
}
```

## Multi-factor authentication (MFA)

The following example demonstrates a simple multi-factor authentication (MFA) sign-in flow. The user can sign in with their email and password. If they have two-factor authentication enabled, they will need to verify their sign-in attempt with an SMS code.

Before you build your sign-in flow, you need to configure the appropriate settings in Clerk:

1. In the Clerk Dashboard, navigate to the [**User & authentication**](https://dashboard.clerk.com/~/user-authentication/user-and-authentication) page.
1. Ensure that **Email**, **Phone**, and **Password** are enabled.
1. In the navigation sidenav, select [**Multi-factor**](https://dashboard.clerk.com/~/user-authentication/multi-factor).
1. Ensure that _only_ **SMS verification code** is enabled.

```tsx
// Filename: app/sign-in/[[...sign-in]]/page.tsx

'use client'

import * as Clerk from '@clerk/elements/common'
import * as SignIn from '@clerk/elements/sign-in'

export default function SignInPage() {
  return (
    <div className="relative grid w-full flex-grow items-center bg-black px-4 sm:justify-center">
      
        
          <header className="text-center">
            
            <h1 className="mt-4 text-xl font-medium tracking-tight text-white">
              Sign in to Clover
            </h1>
          </header>
          
          
            
              Email address
            </Clerk.Label>
            
            
          </Clerk.Field>
          
            
              Password
            </Clerk.Label>
            
            
          </Clerk.Field>
          
            Sign In
          </SignIn.Action>
          <p className="text-center text-sm text-white/60">
            No account?{' '}
            
              Create an account
            </Clerk.Link>
          </p>
        </SignIn.Step>
        
          <header className="text-center">
            
            <h1 className="mt-4 text-xl font-medium tracking-tight text-white">
              Verify phone code
            </h1>
          </header>
          
          
            
              
                Phone code
              </Clerk.Label>
              
              
            </Clerk.Field>
            
              Continue
            </SignIn.Action>
          </SignIn.Strategy>
          <p className="text-center text-sm text-white/60">
            No account?{' '}
            
              Create an account
            </Clerk.Link>
          </p>
        </SignIn.Step>
      </SignIn.Root>
    </div>
  )
}
```

## Email + Google + MFA

The following example demonstrates a simple sign-in flow that combines email, Google OAuth, and multi-factor authentication (MFA). The user can sign in with their email and an email code, or with Google OAuth. If they have two-factor authentication enabled, they will need to verify their sign-in attempt with an SMS code.

Before you build your sign-in flow, you need to configure the appropriate settings in Clerk:

1. In the Clerk Dashboard, navigate to the [**User & authentication**](https://dashboard.clerk.com/~/user-authentication/user-and-authentication) page.
1. Enable **Sign-up with email** and **Sign-in with email**.
1. Select the **Phone** tab and enable **Sign-up with phone** and **Sign-in with phone** and keep the default settings.
1. In the navigation sidenav, select [**SSO connections**](https://dashboard.clerk.com/~/user-authentication/sso-connections).
1. Ensure that _only_ **Google** is enabled.
1. In the navigation sidenav, select [**Multi-factor**](https://dashboard.clerk.com/~/user-authentication/multi-factor).
1. Ensure that _only_ **SMS verification code** is enabled.

```tsx
// Filename: app/sign-in/[[...sign-in]]/page.tsx

'use client'

import * as Clerk from '@clerk/elements/common'
import * as SignIn from '@clerk/elements/sign-in'

export default function SignInPage() {
  return (
    <div className="grid w-full flex-grow items-center bg-white px-4 sm:justify-center">
      
        
          <header className="text-center">
            
            <h1 className="mt-4 text-xl font-medium tracking-tight text-neutral-950">
              Sign in to Clover
            </h1>
          </header>
          
          
            Email</Clerk.Label>
            
            
          </Clerk.Field>
          
            Sign In
          </SignIn.Action>
          <div className="rounded-xl bg-neutral-100 p-5">
            <p className="mb-4 text-center text-sm/5 text-neutral-500">
              Alternatively, sign in with these platforms
            </p>
            <div className="space-y-2">
              
                
                Login with Google
              </Clerk.Connection>
            </div>
          </div>
          <p className="text-center text-sm text-neutral-500">
            Don&apos;t have an account?{' '}
            
              Sign up
            </Clerk.Link>
          </p>
        </SignIn.Step>
        
          
            <header className="text-center">
              
              <h1 className="mt-4 text-xl font-medium tracking-tight text-neutral-950">
                Verify email code
              </h1>
            </header>
            
            
              Email code</Clerk.Label>
              
              
            </Clerk.Field>
            
              Continue
            </SignIn.Action>
          </SignIn.Strategy>
          
            <header className="text-center">
              
              <h1 className="mt-4 text-xl font-medium tracking-tight text-neutral-950">
                Verify phone code
              </h1>
            </header>
            
            
              Phone code</Clerk.Label>
              
              
            </Clerk.Field>
            
              Login
            </SignIn.Action>
          </SignIn.Strategy>
          <p className="text-center text-sm text-neutral-500">
            Don&apos;t have an account?{' '}
            
              Sign up
            </Clerk.Link>
          </p>
        </SignIn.Step>
      </SignIn.Root>
    </div>
  )
}
```
