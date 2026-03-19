# Styling for Clerk Elements


> Learn how to style Clerk Elements.

> [!WARNING]
> Clerk Elements is no longer in development and will not receive any updates. We're actively building a replacement for Clerk Elements with a different approach to customization, and we'll share more details soon.


> [!NOTE]
>
> - Clerk Elements is for [advanced use-cases](/guides/customizing-clerk/elements/overview#why-use-clerk-elements) that require a high-level of customization. The easiest way to implement Clerk is with our [all-in-one UI components](/reference/components/overview).
> - Clerk Elements currently only works with Next.js App Router and [Clerk Core 2](/changelog/2024-04-19).

You can style Clerk Elements components with the following props:

- `className` – Can be used on any Clerk Elements component that renders markup.
- `asChild` – Can be used to change the rendered element entirely.

This guide will demonstrate multiple different styling approaches using the following basic sign-in flow as a starting point:

```tsx
// Filename: app/sign-in/[[...sign-in]]/page.tsx

'use client'

import * as Clerk from '@clerk/elements/common'
import * as SignIn from '@clerk/elements/sign-in'

export default function SignInPage() {
  return (
    
      
        Sign in with Google</Clerk.Connection>
        
          Email</Clerk.Label>
          
          
        </Clerk.Field>
        Continue</SignIn.Action>
      </SignIn.Step>
      
        
          
            Code</Clerk.Label>
            
            
          </Clerk.Field>
          Verify</SignIn.Action>
        </SignIn.Strategy>
      </SignIn.Step>
    </SignIn.Root>
  )
}
```

## Tailwind CSS

If you are already using [Tailwind CSS](https://tailwindcss.com/), no additional setup is required. Classes from Tailwind can be applied to most Clerk Elements components. Use your editor's IntelliSense to see if `className` is a valid prop on a component you want to style.

```tsx
// Filename: app/sign-in/[[...sign-in]]/page.tsx

'use client'

import * as Clerk from '@clerk/elements/common'
import * as SignIn from '@clerk/elements/sign-in'

export default function SignInPage() {
  return (
    
      
        <div className="grid grid-cols-2 gap-x-4">
          
            
            Google
          </Clerk.Connection>
          
            
            GitHub
          </Clerk.Connection>
        </div>
        
          Email</Clerk.Label>
          
          
        </Clerk.Field>
        
          Continue
        </SignIn.Action>
      </SignIn.Step>
    </SignIn.Root>
  )
}
```

## With existing components via `asChild`

Many of the Clerk Elements components accept an `asChild` prop that allows you to swap out the rendered element. This is useful if you have an existing design system or component library that you wish to use with Clerk Elements.

```tsx
// Filename: app/sign-in/[[...sign-in]]/page.tsx

'use client'

import * as Clerk from '@clerk/elements/common'
import * as SignIn from '@clerk/elements/sign-in'

import { Button } from '@components/button'
import { Input } from '@components/input'

export default function SignInPage() {
  return (
    
      
        
          Sign in with Google
        </Clerk.Connection>
        
          Email</Clerk.Label>
          
            </Clerk.Input>
          
        </Clerk.Field>
        
          Continue
        </SignIn.Action>
      </SignIn.Step>
      
        
          
            Code</Clerk.Label>
            
              </Clerk.Input>
            
          </Clerk.Field>
          
            Continue
          </SignIn.Action>
        </SignIn.Strategy>
      </SignIn.Step>
    </SignIn.Root>
  )
}
```

Notice how the Clerk Elements components are wrapping the rendered `` and `` when `asChild` is used. This ensures the underlying event handlers and necessary props are passed along automatically.

### Configure your components for `asChild`

To use the `asChild` prop, your component must spread its incoming props and return [`forwardRef()`](https://react.dev/reference/react/forwardRef). Here's an example of how you might implement a custom `` component:

```tsx
import { forwardRef } from 'react'

const CustomInput = forwardRef(function CustomInput(props, forwardedRef) {
  return <input ref={forwardedRef} {...props} className="custom-class" />
})
```

## CSS Modules

Classes from an imported CSS module can be applied to most Clerk Elements components with `className`.

```tsx
// Filename: app/sign-in/[[...sign-in]]/page.tsx

'use client'

import * as Clerk from '@clerk/elements/common'
import * as SignIn from '@clerk/elements/sign-in'
import styles from './sign-in.module.css'

export default function SignInPage() {
  return (
    
      
        
          Sign in with Google
        </Clerk.Connection>
        
          Email</Clerk.Label>
          
          
        </Clerk.Field>
        
          Continue
        </SignIn.Action>
      </SignIn.Step>
      
        
          
            Code</Clerk.Label>
            
            
          </Clerk.Field>
          
            Verify
          </SignIn.Action>
        </SignIn.Strategy>
      </SignIn.Step>
    </SignIn.Root>
  )
}
```

### Inline styles

You can also use inline styles with Clerk Elements. This is useful when you need to apply styles conditionally or  avoid creating a separate CSS file.

```tsx
// Filename: app/sign-in/[[...sign-in]]/page.tsx

'use client'

import * as Clerk from '@clerk/elements/common'
import * as SignIn from '@clerk/elements/sign-in'

export default function SignInPage() {
  return (
    
      
        
          
            Email
          </Clerk.Label>
          
        </Clerk.Field>
        
          Continue
        </SignIn.Action>
      </SignIn.Step>
    </SignIn.Root>
  )
}
```

## State-based styling

In some cases you might want to style components based on their state. Clerk Elements exposes data attributes for this purpose, as well as components that expose the state programmatically to support more complex logic.

### Data attributes

`` and `` can be styled based on their validity state by targeting the `data-valid` or `data-invalid` attributes:

```css
/* Filename: style.css */

.input {
  --border-color: gray;
  border: 1px solid var(--border-color);

  &[data-invalid] {
    --border-color: red;
  }
}
```

```tsx
// Filename: page.tsx


```

### Function as children

If you need programmatic access to state for more complex styling, several components accept a function as children. This is useful when dealing with animations, or for conditionally rendering elements based on state.

For example, to access a field's state, use ``.

```tsx
// Filename: page.tsx


  {(state) => state === 'invalid' && }</Clerk.FieldState>
  Email</Clerk.Label>
  
  
</Clerk.Field>
```
