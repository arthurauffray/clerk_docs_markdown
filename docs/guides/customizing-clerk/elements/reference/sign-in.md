# Sign-in components


> Reference documentation for Clerk Elements sign-in components.

> [!WARNING]
> Clerk Elements is no longer in development and will not receive any updates. We're actively building a replacement for Clerk Elements with a different approach to customization, and we'll share more details soon.


The following components are used when creating sign-in flows. They are imported from `@clerk/elements/sign-in`. It is recommended to import them all under the `SignIn` namespace to make discovery easier and reduce naming conflicts with other components throughout your application. The code snippets on this page assume you have imported the components this way.

```tsx
// Filename: Anatomy

import * as SignIn from '@clerk/elements/sign-in'

export default function SignInPage() {
  return (
    
      
      
      
      
      
    </SignIn.Root>
  )
}
```

## ``

The root sign-in component. Sets up providers and state management for the sign-in flow. Must wrap all other sign-in components.

`` will validate your sign-in flow to ensure the implementation is correct based on instance settings and best practices. In development instances, if the flow is invalid, it will throw an error.

### Properties {{ toc: false }}

- **`path?`** `string`

  The root path the sign-in flow is mounted at. If not provided, will be automatically inferred (either through the current pathname or [environment variables](/guides/development/clerk-environment-variables#sign-in-and-sign-up-redirects)). Fallback: `/sign-in`

    ---

- **`fallback?`** `React.ReactNode`

  Fallback markup to render while Clerk is loading. Default: `null`

    ---

- **`routing?`** `'path' | 'virtual'`

  If you want to render Clerk Elements in e.g. a modal, use the `'virtual'` routing mode. Default: `'path'`


The following data attributes are also added to the underlying element:

- `data-global-error` - Refers to the [``](/guides/customizing-clerk/elements/reference/common#global-error) status

## ``

A step in the sign-in flow. Conditionally renders its children based on the status of the current sign-in attempt. `start` is the initial step.

### Properties {{ toc: false }}

- **`name`** `'start' | 'verifications' | 'choose-strategy' | 'forgot-password' | 'reset-password'`

  The `name` of the step for which its children will be rendered.


### ``

Renders the beginning sign-in form. Once a sign-in attempt has been created from this step, `` will be rendered.

Typically, this step will contain an `identifier` field and social connection buttons to create a sign-in attempt, however the exact fields that should be rendered depend on your instance configuration.

#### Usage {{ toc: false }}

```tsx
// Filename: page.tsx


  
    Email</Clerk.Label>
    
    
  </Clerk.Field>
  Sign In with Email</SignIn.Action>
</SignIn.Step>
```

### ``

Will render its children if a sign-in attempt is in progress. Any nested `` components will conditionally render based on the status of the sign-in attempt.

You'll typically also want to link to `choose-strategy` to allow for alternative login methods.

#### Usage {{ toc: false }}

```tsx
// Filename: page.tsx


  
    
      password</Clerk.Label>
      
      
    </Clerk.Field>
    Sign In</SignIn.Action>
  </SignIn.Strategy>
  Use another method</SignIn.Action>
</SignIn.Step>
```

### ``

Allows a user to pick a new strategy to verify. This step can be rendered by navigating to `choose-strategy` using ``.

#### Usage {{ toc: false }}

```tsx
// Filename: page.tsx


  Send a code to your phone</SignIn.SupportedStrategy>
</SignIn.Step>
```

### ``

If the currently requested strategy is `password`, but a user can't remember their password, you can navigate them to the `forgot-password` step. They can begin the reset password flow or choose a new strategy. This step can be rendered by navigating to `forgot-password` using ``.

#### Usage {{ toc: false }}

```tsx
// Filename: page.tsx


  
    Reset your password via Email
  </SignIn.SupportedStrategy>
  <p>or</p>
  Sign in with Google</SignIn.SupportedStrategy>
</SignIn.Step>
```

### ``

If a user has requested a password reset and verified their identity, they will be navigated to `reset-password`. A password field should be rendered in this step to allow the user to set a new password.

#### Usage {{ toc: false }}

```tsx
// Filename: page.tsx


  
    New password</Clerk.Label>
    
    
  </Clerk.Field>
  
    Confirm password</Clerk.Label>
    
    
  </Clerk.Field>
  Update password</SignIn.Action>
</SignIn.Step>
```

## ``

Conditionally renders its children depending on the authentication strategy that needs to be verified. Does not render any markup on its own.

### Properties {{ toc: false }}

- **`name`** <code>'enterprise\_sso' | 'ticket' | 'password' | 'passkey' | 'phone\_code' | 'email\_code' | 'web3\_base\_signature' | 'web3\_metamask\_signature' | 'web3\_coinbase\_wallet\_signature' | 'web3\_okx\_wallet\_signature' | 'reset\_password\_email\_code' | 'reset\_password\_phone\_code' | 'email\_link' | 'totp' | 'backup\_code' | 'oauth' | 'web3' | [OAuthStrategy](https://github.com/clerk/javascript/blob/956d8792fefe9d6a89022f1e938149b25503ec7f/packages/types/src/strategies.ts#L15)</code>

  The name of the strategy for which its children will be rendered.


### Usage {{ toc: false }}

```tsx
// Filename: page.tsx


  
    Code</Clerk.Label>
    
    
  </Clerk.Field>
  Verify</SignIn.Action>
</SignIn.Strategy>
```

#### ``

```tsx
// Filename: page.tsx


  Continue with Passkey</SignIn.Action>
</SignIn.Strategy>
```

## ``

Renders a button that will change the current strategy that needs to be verified when in the `choose-strategy` or `forgot-password` steps.

### Properties {{ toc: false }}

- **`name`** `'email_code' | 'email_link' | 'password' | 'passkey' | 'phone_code' | 'reset_password_email_code' | 'reset_password_phone_code' | 'web3_base_signature' | 'web3_metamask_signature' | 'web3_coinbase_wallet_signature' | 'web3_okx_wallet_signature'`

  The name of the strategy to switch to.


### Usage {{ toc: false }}

```tsx
// Filename: page.tsx


  Sign in with password</SignIn.SupportedStrategy>
</SignIn.Step>
```

## ``

Exposes various flow-related actions. It can be used to submit forms, navigate between steps, and re-trigger sending of verification codes. By default, renders a `<button>`.

### Properties {{ toc: false }}

- **`submit?`** `boolean`

  If `true`, the action will submit the form. Default: `false`

    ---

- **`navigate?`** `'choose-strategy' | 'forgot-password' | 'previous' | 'start'`

  The name of the step to navigate to. Default: `undefined`

    ---

- **`resend?`** `boolean`

  If `true`, the action will resend the verification code for the currently active strategy, if applicable. Default: `false`

    ---

- **`fallback?`** `({ resendableAfter: number }) => React.ReactNode`

  Only used when `resend` is `true`. If provided, the fallback markup will be rendered before the resend delay has expired. Default: `null`


### Usage {{ toc: false }}

#### ``

```tsx
// Filename: page.tsx


  
    Email</Clerk.Label>
    
    
  </Clerk.Field>
  Sign in</SignIn.Action>
</SignIn.Step>
```

#### ``

```tsx
// Filename: page.tsx


  
    
      Password</Clerk.Label>
      
      
    </Clerk.Field>
    Sign in</SignIn.Action>
    Forgot password?</SignIn.Action>
  </SignIn.Strategy>
</SignIn.Step>
```

#### ``

```tsx
// Filename: page.tsx


  
    
      Code</Clerk.Label>
      
      
    </Clerk.Field>
    Verify</SignIn.Action>
     <p>Resend code in {resendableAfter} second(s)</p>}
    >
      Resend code
    </SignIn.Action>
  </SignIn.Strategy>
</SignIn.Step>
```

## ``

Renders a masked identifier corresponding to the parent `Strategy` or `SupportedStrategy`, falling back to the identifier that has been provided by the user during a sign-in attempt. Renders a `string` (or empty string if it can't find an identifier). Must be a child of either `` or ``.

### Properties {{ toc: false }}

- **`transform?`** `(identifier: string) => string`

  If provided, modify the supplied `identifier` string before rendering. Useful when interpolating the identifier into localized strings.


### Usage {{ toc: false }}

```tsx
// Filename: page.tsx


  <h1>Check your email</h1>
  <p>
    We sent a code to .
  </p>
</SignIn.Strategy>
```

```tsx
// Filename: page.tsx


  <h1>{t('checkEmail')}</h1>
  <p>
     t('sentCodeTo', { identifier })} />
  </p>
</SignIn.Strategy>
```

## ``

Renders a salutation for the user during a sign-in attempt. It attempts to resolve these values in this specific order:

1. First name
1. Last name
1. Identifier

Renders a `string` (or empty string if it can't find an identifier).

### Usage {{ toc: false }}

```tsx
// Filename: page.tsx


  <p>
    Welcome back !
  </p>
</SignIn.Strategy>
```

## ``

Trigger an autofill suggestion dialog with the stored passkeys. After selecting a passkey a sign-in attempt will be created. By default, renders a `<button>`.

### Usage {{ toc: false }}

```tsx
// Filename: page.tsx


  Continue with Passkey</SignIn.Passkey>
</SignIn.Step>
```
