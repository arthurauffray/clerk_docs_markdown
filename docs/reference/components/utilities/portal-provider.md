# <UNSAFE_PortalProvider>` component


> Clerk's <UNSAFE_PortalProvider> component is used to render Clerk floating UI elements inside custom containers instead of document.body.

The `` component allows you to specify a custom container for Clerk floating UI elements (popovers, modals, tooltips, etc.) that use portals. Only Clerk components within the provider will be affected, components outside the provider will continue to use the default `document.body` for portals.

This is particularly useful when using Clerk components inside external UI libraries like [Radix Dialog](https://www.radix-ui.com/primitives/docs/components/dialog) or [React Aria Components](https://react-spectrum.adobe.com/react-aria/components.html), where portaled elements need to render within the dialog's container to remain interactable.

> [!CAUTION]
> This component is marked as `UNSAFE` because it is an escape hatch that modifies the portal behavior of Clerk components. Not all portal locations will work correctly - some may cause issues with styling, accessibility, or other functionality. Typically, it is best to portal to the root of your application (e.g., the `body` element), outside of any possible overflow or stacking contexts.
>
> Use `` **only when necessary**, such as When Clerk components are rendered inside external dialogs or popovers, or when you need to group all portaled elements into a single container at the root of your app.

## Example


  ### With Radix Dialog

  A common use case is rendering Clerk components inside a Radix Dialog. Without ``, the `` popover would render outside the dialog and may not be interactable.

  
    ```tsx
// Filename: app/components/UserDialog.tsx

    'use client'

    import { useRef } from 'react'
    import * as Dialog from '@radix-ui/react-dialog'
    import { UNSAFE_PortalProvider, UserButton } from '@clerk/nextjs'

    export default function UserDialog() {
      const containerRef = useRef(null)

      return (
        
          Open Dialog</Dialog.Trigger>
          
            
            
               containerRef.current}>
                
            </Dialog.Content>
          </Dialog.Portal>
        </Dialog.Root>
      )
    }
    ```
  

  
    ```tsx
// Filename: src/components/UserDialog.tsx

    import { useRef } from 'react'
    import * as Dialog from '@radix-ui/react-dialog'
    import { UNSAFE_PortalProvider, UserButton } from '@clerk/react'

    export default function UserDialog() {
      const containerRef = useRef(null)

      return (
        
          Open Dialog</Dialog.Trigger>
          
            
            
               containerRef.current}>
                
            </Dialog.Content>
          </Dialog.Portal>
        </Dialog.Root>
      )
    }
    ```
  

  
    > [!NOTE]
> This component is for Expo web projects. For native iOS and Android apps, use the [native components](/reference/expo/native-components/overview) from `@clerk/expo/native` instead.


    ```tsx
// Filename: app/components/UserDialog.web.tsx

    import { useRef } from 'react'
    import * as Dialog from '@radix-ui/react-dialog'
    import { UNSAFE_PortalProvider, UserButton } from '@clerk/expo/web'

    export default function UserDialog() {
      const containerRef = useRef(null)

      return (
        
          Open Dialog</Dialog.Trigger>
          
            
            
               containerRef.current}>
                
            </Dialog.Content>
          </Dialog.Portal>
        </Dialog.Root>
      )
    }
    ```
  

  
    ```tsx
// Filename: app/routes/user-dialog.tsx

    import { useRef } from 'react'
    import * as Dialog from '@radix-ui/react-dialog'
    import { UNSAFE_PortalProvider, UserButton } from '@clerk/react-router'

    export default function UserDialog() {
      const containerRef = useRef(null)

      return (
        
          Open Dialog</Dialog.Trigger>
          
            
            
               containerRef.current}>
                
            </Dialog.Content>
          </Dialog.Portal>
        </Dialog.Root>
      )
    }
    ```
  

  
    ```tsx
// Filename: app/routes/user-dialog.tsx

    import { useRef } from 'react'
    import * as Dialog from '@radix-ui/react-dialog'
    import { UNSAFE_PortalProvider, UserButton } from '@clerk/tanstack-react-start'
    import { createFileRoute } from '@tanstack/react-router'

    export const Route = createFileRoute('/user-dialog')({
      component: UserDialog,
    })

    function UserDialog() {
      const containerRef = useRef(null)

      return (
        
          Open Dialog</Dialog.Trigger>
          
            
            
               containerRef.current}>
                
            </Dialog.Content>
          </Dialog.Portal>
        </Dialog.Root>
      )
    }
    ```
  


  ### With Reka UI Dialog

  A common use case is rendering Clerk components inside a Reka UI Dialog. Without ``, the `` popover would render outside the dialog and may not be interactable.

  ```vue
// Filename: UserDialog.vue

  <script setup>
  import { useTemplateRef } from 'vue'
  import { DialogContent } from 'reka-ui'
  import { UNSAFE_PortalProvider, UserButton } from '@clerk/vue'
  const dialogContentRef = useTemplateRef('dialogContentRef')
  </script>

  <template>
    
       dialogContentRef?.$el">
        
    
  </template>
  ```


## Properties

- **`getContainer`** `() => HTMLElement | null`

  A function that returns the container element where portals should be rendered. This function is called each time a portal needs to be rendered, so it should return a stable reference to the container element.

    ---

- **`children`** `React.ReactNode`

  The Clerk components that should have their portals rendered into the custom container.
