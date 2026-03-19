# Add custom pages and links to the `<UserProfile />` component


> Learn how to add custom pages and include external links within the navigation sidenav of the <UserProfile /> component.

The [``](/reference/components/user/user-profile) component supports the addition of custom pages and external links to the component's sidenav. It only accepts the following components as children:

- `` or `` to add a [custom page](#add-a-custom-page).
- `` or `` to add a [custom link](#add-a-custom-link).

You can also [reorder default routes](#reorder-default-routes).

## Before you start

Before you start, it's important to understand how the `` can be accessed:

- As a modal: When a user selects the [``](/reference/components/user/user-button) component and then selects the **Manage account** menu item, the `` will open as a modal by default.
- As a dedicated page: You can embed the `` component itself in a dedicated page.

This guide includes examples for both use cases. On the code examples, you can select one of the following two tabs to see the implementation for your preferred use case:

- `` tab: By default, the `` sets `userProfileMode='modal'`. If you are using the default settings, then you should select this tab.
- `Dedicated page` tab: If you do not want the `` to open as a modal, then you should select this tab. For these examples, on the `` component, you need to set `userProfileMode='navigation'` and `userProfileUrl='/user-profile'`.

## Add a custom page

To add a custom page to the `` component, you will need to use one of the following components, depending on the use case mentioned in the [Before you start](#before-you-start) section.

| Use case | Component to use |
| - | - |
| `` component | `` |
| Dedicated page with the `` component | `` |

### Props

`` and `` accept the following props, all of which are **required**:

- **`label`** `string`

  The name that will be displayed in the navigation sidenav for the custom page.

    ---

- **`labelIcon`** `React.ReactElement`

  An icon displayed next to the label in the navigation sidenav.

    ---

- **`url`** `string`

  The path segment that will be used to navigate to the custom page. For example, if the `` component is rendered at `/user`, then the custom page will be accessed at `/user/{url}` when using [path routing](/guides/how-clerk-works/routing).

    ---

- **`children`** `React.ReactElement`

  The content to be rendered inside the custom page.


### Example


  
    The following example demonstrates two ways that you can render content in a custom page: **as a component** or **as a direct child**.

    
**:**

```tsx
// Filename: components/Header.tsx

      const DotIcon = () => {
        return (
          
        )
      }

      const CustomPage = () => {
        return (
          <div>
            <h1>Custom page</h1>
            <p>This is the content of the custom page.</p>
          </div>
        )
      }

      const Header = () => (
        <header>
          
            
            
              </UserButton.UserProfilePage>

            
            
              <div>
                <h1>Custom Terms Page</h1>
                <p>This is the content of the custom terms page.</p>
              </div>
            </UserButton.UserProfilePage>
          
        </header>
      )

      export default Header
      ```


**Dedicated page:**

```tsx
// Filename: user-profile/page.tsx

      const DotIcon = () => {
        return (
          
        )
      }

      const CustomPage = () => {
        return (
          <div>
            <h1>Custom page</h1>
            <p>This is the content of the custom page.</p>
          </div>
        )
      }

      const UserProfilePage = () => (
        
          
          
            </UserProfile.Page>

          
          
            <div>
              <h1>Custom Terms Page</h1>
              <p>This is the content of the custom terms page.</p>
            </div>
          </UserProfile.Page>
        
      )

      export default UserProfilePage
      ```

  

  
    
**:**

```astro
// Filename: pages/index.astro

      ---
      import { UserButton } from '@clerk/astro/components'
      ---

      <header>
        
          
            
            <div>
              <h1>Custom page</h1>
              <p>This is the content of the custom page.</p>
            </div>
          </UserButton.UserProfilePage>
        
      </header>
      ```


**Dedicated page:**

```astro
// Filename: pages/user-profile.astro

      ---
      import { UserProfile } from '@clerk/astro/components'
      ---

      
        
          
          <div>
            <h1>Custom page</h1>
            <p>This is the content of the custom page.</p>
          </div>
        </UserProfile.Page>
      
      ```

  

  
    
**:**

```vue
// Filename: App.vue

      <script setup lang="ts">
      import { UserButton } from '@clerk/vue'
      </script>

      <template>
        <header>
          
            
              <template #labelIcon>
                
              </template>
              <div>
                <h1>Custom page</h1>
                <p>This is the content of the custom page.</p>
              </div>
            </UserButton.UserProfilePage>
          
        </header>
      </template>
      ```


**Dedicated page:**

```vue
// Filename: pages/user-profile.vue

      <script setup lang="ts">
      import { UserProfile } from '@clerk/vue'
      </script>

      <template>
        
          
            <template #labelIcon>
              
            </template>
            <div>
              <h1>Custom page</h1>
              <p>This is the content of the custom page.</p>
            </div>
          </UserProfile.Page>
        
      </template>
      ```

  

  
    
**:**

```vue
// Filename: App.vue

      <script setup lang="ts">
      // Components are automatically imported
      </script>

      <template>
        <header>
          
            
              <template #labelIcon>
                
              </template>
              <div>
                <h1>Custom page</h1>
                <p>This is the content of the custom page.</p>
              </div>
            </UserButton.UserProfilePage>
          
        </header>
      </template>
      ```


**Dedicated page:**

```vue
// Filename: pages/user-profile.vue

      <script setup lang="ts">
      // Components are automatically imported
      </script>

      <template>
        
          
            <template #labelIcon>
              
            </template>
            <div>
              <h1>Custom page</h1>
              <p>This is the content of the custom page.</p>
            </div>
          </UserProfile.Page>
        
      </template>
      ```

  


  To add custom pages to the `` component using the [JavaScript SDK](/reference/javascript/overview), pass the `customPages` property to the `mountUserProfile()` method, as shown in the following example:

  ```js
// Filename: main.js

  import { Clerk } from '@clerk/clerk-js'

  const pubKey = import.meta.env.VITE_CLERK_PUBLISHABLE_KEY

  const clerk = new Clerk(pubKey)
  await clerk.load()

  document.getElementById('app').innerHTML = `
      <div id="user-profile"></div>
    `

  const userProfileDiv = document.getElementById('user-profile')

  clerk.mountUserProfile(userProfileDiv, {
    customPages: [
      {
        url: 'custom-page',
        label: 'Custom Page',
        mountIcon: (el) => {
          el.innerHTML = '👋'
        },
        unmountIcon: (el) => {
          el.innerHTML = ''
        },
        mount: (el) => {
          el.innerHTML = `
              <h1><b>Custom Page</b></h1>
              <p>This is the content of the custom page.</p>
              `
        },
        unmount: (el) => {
          el.innerHTML = ''
        },
      },
      {
        url: '/other-page',
        label: 'Other Page',
        mountIcon: (el) => {
          el.innerHTML = '🌐'
        },
        unmountIcon: (el) => {
          el.innerHTML = ''
        },
      },
    ],
  })
  ```


## Add a custom link


  > [!IMPORTANT]
  > It is not possible to add custom links to the `` component when using the [JavaScript SDK](/reference/javascript/overview). The `mountUserProfile()` method does not have a property for adding custom links.


  To add a custom link to the `` component, you will need to use one of the following components, depending on the use case mentioned in the [Before you start](#before-you-start) section.

  | Use case | Component to use |
  | - | - |
  | `` component | `` |
  | Dedicated page with the `` component | `` |

  ### Props

  `` and `` accept the following props, all of which are **required**:

  - **`label`** `string`

  The name that will be displayed in the navigation sidenav for the link.

      ---

- **`labelIcon`** `React.ReactElement`

  An icon displayed next to the label in the navigation sidenav.

      ---

- **`url`** `string`

  The path segment that will be used to navigate to the custom page. For example, if the `` component is rendered at `/user`, then the custom link will be navigate to `/user/{url}` when using [path routing](/guides/how-clerk-works/routing).


  ### Example

  The following example adds a custom link to the `` sidenav that navigates to the homepage.

  
    
**:**

```tsx
// Filename: components/Header.tsx

      const DotIcon = () => {
        return (
          
        )
      }

      const Header = () => (
        <header>
          
            
          
        </header>
      )

      export default Header
      ```


**Dedicated page:**

```tsx
// Filename: user-profile/page.tsx

      const DotIcon = () => {
        return (
          
        )
      }

      const UserProfilePage = () => (
        
          
        
      )

      export default UserProfilePage
      ```

  

  
    
**:**

```astro
// Filename: pages/index.astro

      ---
      import { UserButton } from '@clerk/astro/components'
      ---

      <header>
        
          
            
          </UserButton.UserProfileLink>
        
      </header>
      ```


**Dedicated page:**

```astro
// Filename: pages/user-profile.astro

      ---
      import { UserProfile } from '@clerk/astro/components'
      ---

      
        
          
        </UserProfile.Link>
      
      ```

  

  
    
**:**

```vue
// Filename: App.vue

      <script setup lang="ts">
      import { UserButton } from '@clerk/vue'
      </script>

      <template>
        <header>
          
            
              <template #labelIcon>
                
              </template>
            </UserButton.UserProfileLink>
          
        </header>
      </template>
      ```


**Dedicated page:**

```vue
// Filename: pages/user-profile.vue

      <script setup lang="ts">
      import { UserProfile } from '@clerk/vue'
      </script>

      <template>
        
          
            <template #labelIcon>
              
            </template>
          </UserProfile.Link>
        
      </template>
      ```

  

  
    
**:**

```vue
// Filename: App.vue

      <script setup lang="ts">
      // Components are automatically imported
      </script>

      <template>
        <header>
          
            
              <template #labelIcon>
                
              </template>
            </UserButton.UserProfileLink>
          
        </header>
      </template>
      ```


**Dedicated page:**

```vue
// Filename: pages/user-profile.vue

      <script setup lang="ts">
      // Components are automatically imported
      </script>

      <template>
        
          
            <template #labelIcon>
              
            </template>
          </UserProfile.Link>
        
      </template>
      ```

  


## Reorder default routes

The `` component includes two default menu items: `Account` and `Security`, in that order. You can reorder these default items by setting the `label` prop to `'account'` or `'security'`. This will target the existing default item and allow you to rearrange it.

Note that when reordering default routes, the first item in the navigation sidenav cannot be a custom link.

### Example

The following example adds a custom page as the first item in the sidenav, followed by a custom link to the homepage, and then the default `Account` and `Security` pages.


  
**:**

```tsx
// Filename: components/Header.tsx

    const DotIcon = () => {
      return (
        
      )
    }

    const CustomPage = () => {
      return (
        <div>
          <h1>Custom page</h1>
          <p>This is the content of the custom page.</p>
        </div>
      )
    }

    const Header = () => (
      <header>
        
          
            </UserButton.UserProfilePage>
          
          
          
        
      </header>
    )

    export default Header
    ```


**Dedicated page:**

```tsx
// Filename: user-profile/page.tsx

    const DotIcon = () => {
      return (
        
      )
    }

    const CustomPage = () => {
      return (
        <div>
          <h1>Custom page</h1>
          <p>This is the content of the custom page.</p>
        </div>
      )
    }

    const UserProfilePage = () => (
      
        
          </UserProfile.Page>
        
        
        
      
    )

    export default UserProfilePage
    ```


  
**:**

```astro
// Filename: pages/index.astro

    ---
    import { UserButton } from '@clerk/astro/components'
    ---

    <header>
      
        
          
          <div>
            <h1>Custom page</h1>
            <p>This is the content of the custom page.</p>
          </div>
        </UserButton.UserProfilePage>
        
          
        </UserButton.UserProfileLink>
        
        
      
    </header>
    ```


**Dedicated page:**

```astro
// Filename: pages/user-profile.astro

    ---
    import { UserProfile } from '@clerk/astro/components'
    ---

    
      
        
        <div>
          <h1>Custom page</h1>
          <p>This is the content of the custom page.</p>
        </div>
      </UserProfile.Page>
      
        
      </UserProfile.Link>
      
      
    
    ```


  ```js
// Filename: main.js

  import { Clerk } from '@clerk/clerk-js'

  const pubKey = import.meta.env.VITE_CLERK_PUBLISHABLE_KEY

  const clerk = new Clerk(pubKey)
  await clerk.load()

  document.getElementById('app').innerHTML = `
    <div id="user-profile"></div>
  `

  const userProfileDiv = document.getElementById('user-profile')

  clerk.mountUserProfile(userProfileDiv, {
    customPages: [
      {
        url: 'custom-page',
        label: 'Custom Page',
        mountIcon: (el) => {
          el.innerHTML = '👋'
        },
        unmountIcon: (el) => {
          el.innerHTML = ''
        },
        mount: (el) => {
          el.innerHTML = `
            <h1><b>Custom Page</b></h1>
            <p>This is the content of the custom page.</p>
            `
        },
        unmount: (el) => {
          el.innerHTML = ''
        },
      },
      {
        label: 'account',
      },
      {
        label: 'security',
      },
    ],
  })
  ```


  
**:**

```vue
// Filename: App.vue

    <script setup lang="ts">
    import { UserButton } from '@clerk/vue'
    </script>

    <template>
      
        
          <template #labelIcon>
            
          </template>
          <div>
            <h1>Custom page</h1>
            <p>This is the content of the custom page.</p>
          </div>
        </UserButton.UserProfilePage>
        
          <template #labelIcon>
            
          </template>
        </UserButton.UserProfileLink>
        
        
      
    </template>
    ```


**Dedicated page:**

```vue
// Filename: pages/user-profile.vue

    <script setup lang="ts">
    import { UserProfile } from '@clerk/vue'
    </script>

    <template>
      
        
          <template #labelIcon>
            
          </template>
          <div>
            <h1>Custom page</h1>
            <p>This is the content of the custom page.</p>
          </div>
        </UserProfile.Page>
        
          <template #labelIcon>
            
          </template>
        </UserProfile.Link>
        
        
      
    </template>
    ```


  
**:**

```vue
// Filename: App.vue

    <script setup lang="ts">
    // Components are automatically imported
    </script>

    <template>
      
        
          <template #labelIcon>
            
          </template>
          <div>
            <h1>Custom page</h1>
            <p>This is the content of the custom page.</p>
          </div>
        </UserButton.UserProfilePage>
        
          <template #labelIcon>
            
          </template>
        </UserButton.UserProfileLink>
        
        
      
    </template>
    ```


**Dedicated page:**

```vue
// Filename: pages/user-profile.vue

    <script setup lang="ts">
    // Components are automatically imported
    </script>

    <template>
      
        
          <template #labelIcon>
            
          </template>
          <div>
            <h1>Custom page</h1>
            <p>This is the content of the custom page.</p>
          </div>
        </UserProfile.Page>
        
          <template #labelIcon>
            
          </template>
        </UserProfile.Link>
        
        
      
    </template>
    ```
