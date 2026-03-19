# shadcn/ui


> Learn how to compose Clerk Elements with shadcn/ui to build custom sign in and sign up flows.

> [!WARNING]
> Clerk Elements is no longer in development and will not receive any updates. We're actively building a replacement for Clerk Elements with a different approach to customization, and we'll share more details soon.


The following examples demonstrate how to compose Clerk Elements with shadcn/ui to build custom sign-in and sign-up flows.

## Before you start

To use these examples, you must first:

1. Complete the [shadcn/ui Next.js installation guide](https://ui.shadcn.com/docs/installation/next)
1. Install the [Button](https://ui.shadcn.com/docs/components/button), [Card](https://ui.shadcn.com/docs/components/card), [Input](https://ui.shadcn.com/docs/components/input), and [Label](https://ui.shadcn.com/docs/components/label) components within your project

```shell

npx shadcn@latest add button card input label
```

1. Add the [`Icons` component from the shadcn/ui docs](https://github.com/shadcn-ui/ui/blob/main/apps/www/components/icons.tsx) to an `icons.tsx` file within your `component/ui/` directory.
1. Add the following animations to your `tailwind.config.js` file:

```js
// Filename: tailwind.config.js

/** @type {import('tailwindcss').Config} */
module.exports = {
  theme: {
    extend: {
      keyframes: {
        'caret-blink': {
          '0%,70%,100%': { opacity: '1' },
          '20%,50%': { opacity: '0' },
        },
      },
      animation: {
        'caret-blink': 'caret-blink 1.25s ease-out infinite',
      },
    },
  },
}
```

You must also configure the appropriate settings in Clerk:

1. In the Clerk Dashboard, navigate to the [**SSO connections**](https://dashboard.clerk.com/~/user-authentication/sso-connections) page.
1. Ensure that **Google** and **GitHub** are enabled. If they are not in the list of connections, select the **Add connection** button, and select **For all users**. Enable **Google** and **GitHub**.
1. Make sure you have your sign in and sign up URLs set in your [environment variables](https://clerk.com/docs/guides/development/customize-redirect-urls#environment-variables).

## Sign up

```tsx
// Filename: app/sign-up/[[...sign-up]]/page.tsx

'use client'
import * as Clerk from '@clerk/elements/common'
import * as SignUp from '@clerk/elements/sign-up'
import { Button } from '@/components/ui/button'
import {
  Card,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from '@/components/ui/card'
import { Input } from '@/components/ui/input'
import { Label } from '@/components/ui/label'
import { Icons } from '@/components/ui/icons'
import { cn } from '@/lib/utils'

export default function SignUpPage() {
  return (
    <div className="grid w-full grow items-center px-4 sm:justify-center">
      
        
          {(isGlobalLoading) => (
            <>
              
                
                  
                    Create your account
                    
                      Welcome! Please fill in the details to get started.
                    
                  
                  
                    <div className="grid grid-cols-2 gap-x-4">
                      
                        
                          
                            {(isLoading) =>
                              isLoading ? (
                                
                              ) : (
                                <>
                                  
                                  GitHub
                                </>
                              )
                            }
                          </Clerk.Loading>
                        
                      </Clerk.Connection>
                      
                        
                          
                            {(isLoading) =>
                              isLoading ? (
                                
                              ) : (
                                <>
                                  
                                  Google
                                </>
                              )
                            }
                          </Clerk.Loading>
                        
                      </Clerk.Connection>
                    </div>
                    <p className="flex items-center gap-x-3 text-sm text-muted-foreground before:h-px before:flex-1 before:bg-border after:h-px after:flex-1 after:bg-border">
                      or
                    </p>
                    
                      
                        Email address
                      </Clerk.Label>
                      
                        </Clerk.Input>
                      
                    </Clerk.Field>
                    
                      
                        Password
                      </Clerk.Label>
                      
                        </Clerk.Input>
                      
                    </Clerk.Field>
                  
                  
                    <div className="grid w-full gap-y-4">
                      
                      
                        
                          
                            {(isLoading) => {
                              return isLoading ? (
                                
                              ) : (
                                'Continue'
                              )
                            }}
                          </Clerk.Loading>
                        
                      </SignUp.Action>
                      
                        Already have an account? Sign in</Clerk.Link>
                      
                    </div>
                  
                
              </SignUp.Step>

              
                
                  
                    Continue registration
                  
                  
                    
                      
                        Username
                      </Clerk.Label>
                      
                        </Clerk.Input>
                      
                    </Clerk.Field>
                  
                  
                    <div className="grid w-full gap-y-4">
                      
                        
                          
                            {(isLoading) => {
                              return isLoading ? (
                                
                              ) : (
                                'Continue'
                              )
                            }}
                          </Clerk.Loading>
                        
                      </SignUp.Action>
                    </div>
                  
                
              </SignUp.Step>

              
                
                  
                    
                      Verify your email
                      
                        Use the verification link sent to your email address
                      
                    
                    
                      <div className="grid items-center justify-center gap-y-2">
                        
                          Email address</Clerk.Label>
                          <div className="flex justify-center text-center">
                             {
                                return (
                                  <div
                                    data-status={status}
                                    className={cn(
                                      'relative flex size-10 items-center justify-center border-y border-r border-input text-sm transition-all first:rounded-l-md first:border-l last:rounded-r-md',
                                      {
                                        'z-10 ring-2 ring-ring ring-offset-background':
                                          status === 'cursor' || status === 'selected',
                                      },
                                    )}
                                  >
                                    {value}
                                    {status === 'cursor' && (
                                      <div className="pointer-events-none absolute inset-0 flex items-center justify-center">
                                        <div className="animate-caret-blink h-4 w-px bg-foreground duration-1000" />
                                      </div>
                                    )}
                                  </div>
                                )
                              }}
                            />
                          </div>
                          
                        </Clerk.Field>
                         (
                            
                              Didn&apos;t receive a code? Resend (
                              <span className="tabular-nums">{resendableAfter}</span>)
                            
                          )}
                        >
                          
                            Didn&apos;t receive a code? Resend
                          
                        </SignUp.Action>
                      </div>
                    
                    
                      <div className="grid w-full gap-y-4">
                        
                          
                            
                              {(isLoading) => {
                                return isLoading ? (
                                  
                                ) : (
                                  'Continue'
                                )
                              }}
                            </Clerk.Loading>
                          
                        </SignUp.Action>
                      </div>
                    
                  
                </SignUp.Strategy>
              </SignUp.Step>
            </>
          )}
        </Clerk.Loading>
      </SignUp.Root>
    </div>
  )
}
```

## Sign in

```tsx
// Filename: app/sign-in/[[...sign-in]]/page.tsx

'use client'
import * as Clerk from '@clerk/elements/common'
import * as SignIn from '@clerk/elements/sign-in'
import { Button } from '@/components/ui/button'
import {
  Card,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from '@/components/ui/card'
import { Input } from '@/components/ui/input'
import { Label } from '@/components/ui/label'
import { Icons } from '@/components/ui/icons'

export default function SignInPage() {
  return (
    <div className="grid w-full grow items-center px-4 sm:justify-center">
      
        
          {(isGlobalLoading) => (
            <>
              
                
                  
                    Sign in to Acme Co
                    Welcome back! Please sign in to continue
                  
                  
                    <div className="grid grid-cols-2 gap-x-4">
                      
                        
                          
                            {(isLoading) =>
                              isLoading ? (
                                
                              ) : (
                                <>
                                  
                                  GitHub
                                </>
                              )
                            }
                          </Clerk.Loading>
                        
                      </Clerk.Connection>
                      
                        
                          
                            {(isLoading) =>
                              isLoading ? (
                                
                              ) : (
                                <>
                                  
                                  Google
                                </>
                              )
                            }
                          </Clerk.Loading>
                        
                      </Clerk.Connection>
                    </div>
                    <p className="flex items-center gap-x-3 text-sm text-muted-foreground before:h-px before:flex-1 before:bg-border after:h-px after:flex-1 after:bg-border">
                      or
                    </p>
                    
                      
                        Email address
                      </Clerk.Label>
                      
                        </Clerk.Input>
                      
                    </Clerk.Field>
                  
                  
                    <div className="grid w-full gap-y-4">
                      
                        
                          
                            {(isLoading) => {
                              return isLoading ? (
                                
                              ) : (
                                'Continue'
                              )
                            }}
                          </Clerk.Loading>
                        
                      </SignIn.Action>

                      
                        
                          Don&apos;t have an account? Sign up
                        </Clerk.Link>
                      
                    </div>
                  
                
              </SignIn.Step>

              
                
                  
                    Use another method
                    
                      Facing issues? You can use any of these methods to sign in.
                    
                  
                  
                    
                      
                        Email code
                      
                    </SignIn.SupportedStrategy>
                    
                      
                        Password
                      
                    </SignIn.SupportedStrategy>
                  
                  
                    <div className="grid w-full gap-y-4">
                      
                        
                          
                            {(isLoading) => {
                              return isLoading ? (
                                
                              ) : (
                                'Go back'
                              )
                            }}
                          </Clerk.Loading>
                        
                      </SignIn.Action>
                    </div>
                  
                
              </SignIn.Step>

              
                
                  
                    
                      Enter your password
                      <p className="text-sm text-muted-foreground">
                        Welcome back 
                      </p>
                    
                    
                      
                        
                          Password
                        </Clerk.Label>
                        
                          </Clerk.Input>
                        
                      </Clerk.Field>
                    
                    
                      <div className="grid w-full gap-y-4">
                        
                          
                            
                              {(isLoading) => {
                                return isLoading ? (
                                  
                                ) : (
                                  'Continue'
                                )
                              }}
                            </Clerk.Loading>
                          
                        </SignIn.Action>
                        
                          
                            Use another method
                          
                        </SignIn.Action>
                      </div>
                    
                  
                </SignIn.Strategy>

                
                  
                    
                      Check your email
                      
                        Enter the verification code sent to your email
                      
                      <p className="text-sm text-muted-foreground">
                        Welcome back 
                      </p>
                    
                    
                      
                        Email verification code</Clerk.Label>
                        <div className="grid gap-y-2 items-center justify-center">
                          <div className="flex justify-center text-center">
                             {
                                return (
                                  <div
                                    data-status={status}
                                    className="relative flex h-9 w-9 items-center justify-center border-y border-r border-input text-sm shadow-sm transition-all first:rounded-l-md first:border-l last:rounded-r-md data-[status=selected]:ring-1 data-[status=selected]:ring-ring data-[status=cursor]:ring-1 data-[status=cursor]:ring-ring"
                                  >
                                    {value}
                                  </div>
                                )
                              }}
                            />
                          </div>
                          
                           (
                              
                                Didn&apos;t receive a code? Resend (
                                <span className="tabular-nums">{resendableAfter}</span>)
                              
                            )}
                          >
                            
                              Didn&apos;t receive a code? Resend
                            
                          </SignIn.Action>
                        </div>
                      </Clerk.Field>
                    
                    
                      <div className="grid w-full gap-y-4">
                        
                          
                            
                              {(isLoading) => {
                                return isLoading ? (
                                  
                                ) : (
                                  'Continue'
                                )
                              }}
                            </Clerk.Loading>
                          
                        </SignIn.Action>
                        
                          
                            Use another method
                          
                        </SignIn.Action>
                      </div>
                    
                  
                </SignIn.Strategy>
              </SignIn.Step>
            </>
          )}
        </Clerk.Loading>
      </SignIn.Root>
    </div>
  )
}
```

## OTP input

The following example demonstrates how to make a one-time password (OTP) input with Clerk Elements. This example will only work if placed within a `Step` in a sign-up or sign-in authentication flow, as shown in [the sign-in](#sign-in) and [sign-up](#sign-up) examples.

```tsx

 {
    return (
      <div
        data-status={status}
        className={cn(
          'relative flex size-10 items-center justify-center border-y border-r border-input text-sm transition-all first:rounded-l-md first:border-l last:rounded-r-md',
          {
            'z-10 ring-2 ring-ring ring-offset-background':
              status === 'cursor' || status === 'selected',
          },
        )}
      >
        {value}
        {status === 'cursor' && (
          <div className="pointer-events-none absolute inset-0 flex items-center justify-center">
            <div className="animate-caret-blink h-4 w-px bg-foreground duration-1000" />
          </div>
        )}
      </div>
    )
  }}
/>
```
