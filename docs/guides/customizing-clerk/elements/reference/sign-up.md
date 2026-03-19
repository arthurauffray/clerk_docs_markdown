# Sign-up components


> Reference documentation for Clerk Elements sign-up components.

> [!WARNING]
> Clerk Elements is no longer in development and will not receive any updates. We're actively building a replacement for Clerk Elements with a different approach to customization, and we'll share more details soon.


The following components are used when creating sign-up flows. They are imported from `@clerk/elements/sign-up`. It is recommended to import them all under the `SignUp` namespace to make discovery easier and reduce naming conflicts with other components throughout your application. The code snippets on this page assume you have imported the components this way.

```tsx
// Filename: Anatomy

import * as SignUp from '@clerk/elements/sign-up'

export default function SignUpPage() {
  return (
    
      
      
      
    </SignUp.Root>
  )
}
```

## ``

The root sign-up component. Sets up providers and state management for the sign-up flow. Must wrap all other sign-up components. `` will validate your built sign-up flow to ensure the implementation is correct based on instance settings and best practices.

### Properties {{ toc: false }}

- **`path?`** `string`

  The root path the sign-up flow is mounted at. If not provided, will be automatically inferred (either through the current pathname or [environment variables](/guides/development/clerk-environment-variables#sign-in-and-sign-up-redirects)). Fallback: `/sign-up`

    ---

- **`fallback?`** `React.ReactNode`

  Fallback markup to render while Clerk is loading. Default: `null`

    ---

- **`routing?`** `'path' | 'virtual'`

  If you want to render Clerk Elements in e.g. a modal, use the `'virtual'` routing mode. Default: `'path'`


The following data attributes are also added to the underlying element:

- `data-global-error` - Refers to the [``](/guides/customizing-clerk/elements/reference/common#global-error) status

## ``

A step in the sign-up flow. Controls conditionally rendering its children based on the status of the current sign up attempt. `start` is the initial step.

### Properties {{ toc: false }}

- **`name`** `'start' | 'continue' | 'verifications'`

  The `name` of the step for which its children will be rendered.


### ``

Renders the beginning sign-up form. Once a sign up attempt has been created from this step, the `continue` or `verification` step will be rendered. The exact fields that should be rendered depend on your instance configuration.

#### Usage

```tsx
// Filename: page.tsx


  Sign up with Google</Clerk.Connection>
  
    Email</Clerk.Label>
    
    
  </Clerk.Field>

  

  Sign up</SignUp.Action>
</SignUp.Step>
```

### ``

Collects additional required fields from the user during a sign up attempt. This step will be rendered if a user initiates a sign up, but does not provide all required fields (e.g. through social connection).

#### Usage

```tsx
// Filename: page.tsx


  
    Username</Clerk.Label>
    
    
  </Clerk.Field>

  Sign up</SignUp.Action>
</SignUp.Step>
```

### ``

Verifies certain fields provided during sign up. Will render if your instance is configured to require verification of emails or phone numbers.

#### Usage

```tsx
// Filename: page.tsx


  
    
      Email code</Clerk.Label>
      
      
    </Clerk.Field>

    Verify email</SignUp.Action>
  </SignUp.Strategy>
</SignUp.Step>
```

## ``

Conditionally renders its children depending on the authentication strategy that needs to be verified. Does not render any markup on its own.

### Properties {{ toc: false }}

- **`name`** `'code' | 'email_code' | 'email_link' | 'phone_code'`

  The name of the strategy for which its children will be rendered.


### Usage {{ toc: false }}

```tsx
// Filename: page.tsx


  
    Code</Clerk.Label>
    
    
  </Clerk.Field>

  Verify</SignUp.Action>
</SignUp.Strategy>
```

## ``

Exposes various flow-related actions. It can be used to submit forms, navigate between steps, and re-trigger sending of verification codes. By default, renders a `<button>`.

### Properties {{ toc: false }}

- **`submit?`** `boolean`

  If `true`, the action will submit the form. Default: `false`

    ---

- **`navigate?`** `'start' | 'previous'`

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

  Sign up</SignUp.Action>
</SignUp.Step>
```

#### ``

```tsx
// Filename: page.tsx


  
    Username</Clerk.Label>
    
    
  </Clerk.Field>

  Sign up</SignUp.Action>
  Go back</SignUp.Action>
</SignUp.Step>
```

#### ``

```tsx
// Filename: page.tsx


  
    
      Code</Clerk.Label>
      
      
    </Clerk.Field>

    Verify</SignUp.Action>
     <p>Resend code in {resendableAfter} second(s)</p>}
    >
      Resend code
    </SignUp.Action>
  </SignUp.Strategy>
</SignUp.Step>
```

## ``

Renders the Cloudflare Turnstile widget. It must be used within the `` component. By default, renders a `<div>`.

### Properties {{ toc: false }}

- **`asChild?`** `boolean`

  If `true`, `` will render as its child element. The element must be a self-closing element or component. Any children passed to the immediate child component of `` will be ignored. Default: `false`


### `` usage

```tsx
// Filename: page.tsx


  

  Sign up</SignUp.Action>
</SignUp.Step>
```

#### With `asChild`

```tsx
// Filename: page.tsx


  
    <aside />
  </SignUp.Captcha>

  Sign up</SignUp.Action>
</SignUp.Step>
```
