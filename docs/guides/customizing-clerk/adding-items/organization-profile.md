# Add custom pages and links to the `<OrganizationProfile />` component


> Learn how to add custom pages and include external links within the navigation sidenav of the <OrganizationProfile /> component.

The [``](/reference/components/organization/organization-profile) component supports the addition of custom pages and external links to the component's sidenav. It only accepts the following components as children:

- `` or `` to add a [custom page](#add-a-custom-page).
- `` or `` to add a [custom link](#add-a-custom-link).

You can also [reorder default routes](#reorder-default-routes).

## Before you start

Before you start, it's important to understand how the `` can be accessed:

- As a modal: When a user selects the [``](/reference/components/organization/organization-switcher) component and then selects the **Manage Organization** option, the `` will open as a modal by default.
- As a dedicated page: You can embed the `` component itself in a dedicated page.

This guide includes examples for both use cases. On the code examples, you can select one of the following two tabs to see the implementation for your preferred use case:

- `` tab: By default, the `` sets `organizationProfileMode='modal'`. If you are using the default settings, then you should select this tab.
- `Dedicated page` tab: If you do not want the `` to open as a modal, then you should select this tab. For these examples, on the `` component, you need to set `organizationProfileMode='navigation'` and `organizationProfileUrl='/organization-profile'`.

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

  The path segment that will be used to navigate to the custom page. For example, if the `` component is rendered at `/organization`, then the custom page will be accessed at `/organization/{url}` when using [path routing](/guides/how-clerk-works/routing).

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
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" fill="currentColor">
            <path d="M256 512A256 256 0 1 0 256 0a256 256 0 1 0 0 512z" />
          </svg>
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
          
            
            
              </OrganizationSwitcher.OrganizationProfilePage>

            
            
              <div>
                <h1>Custom Terms Page</h1>
                <p>This is the content of the custom terms page.</p>
              </div>
            </OrganizationSwitcher.OrganizationProfilePage>
          
        </header>
      )

      export default Header
      ```


**Dedicated page:**

```tsx
// Filename: organization-profile/page.tsx

      const DotIcon = () => {
        return (
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" fill="currentColor">
            <path d="M256 512A256 256 0 1 0 256 0a256 256 0 1 0 0 512z" />
          </svg>
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

      const OrganizationProfilePage = () => (
        
          
          
            </OrganizationProfile.Page>

          
          
            <div>
              <h1>Custom Terms Page</h1>
              <p>This is the content of the custom terms page.</p>
            </div>
          </OrganizationProfile.Page>
        
      )

      export default OrganizationProfilePage
      ```

  

  
    
**:**

```astro
// Filename: pages/index.astro

      ---
      import { OrganizationSwitcher } from '@clerk/astro/components'
      ---

      <header>
        
          
            <svg
              slot="label-icon"
              xmlns="http://www.w3.org/2000/svg"
              viewBox="0 0 512 512"
              fill="currentColor"
            >
              <path d="M256 512A256 256 0 1 0 256 0a256 256 0 1 0 0 512z"></path>
            </svg>
            <div>
              <h1>Custom page</h1>
              <p>This is the content of the custom page.</p>
            </div>
          </OrganizationSwitcher.OrganizationProfilePage>
        
      </header>
      ```


**Dedicated page:**

```astro
// Filename: pages/organization-profile.astro

      ---
      import { OrganizationProfile } from '@clerk/astro/components'
      ---

      
        
          <svg
            slot="label-icon"
            xmlns="http://www.w3.org/2000/svg"
            viewBox="0 0 512 512"
            fill="currentColor"
          >
            <path d="M256 512A256 256 0 1 0 256 0a256 256 0 1 0 0 512z"></path>
          </svg>
          <div>
            <h1>Custom page</h1>
            <p>This is the content of the custom page.</p>
          </div>
        </OrganizationProfile.Page>
      
      ```

  

  
    
**:**

```vue
// Filename: App.vue

      <script setup lang="ts">
      import { OrganizationSwitcher } from '@clerk/vue'
      </script>

      <template>
        <header>
          
            
              <template #labelIcon>
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" fill="currentColor">
                  <path d="M256 512A256 256 0 1 0 256 0a256 256 0 1 0 0 512z"></path>
                </svg>
              </template>
              <div>
                <h1>Custom page</h1>
                <p>This is the content of the custom page.</p>
              </div>
            </OrganizationSwitcher.OrganizationProfilePage>
          
        </header>
      </template>
      ```


**Dedicated page:**

```vue
// Filename: pages/organization-profile.vue

      <script setup lang="ts">
      import { OrganizationProfile } from '@clerk/vue'
      </script>

      <template>
        
          
            <template #labelIcon>
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" fill="currentColor">
                <path d="M256 512A256 256 0 1 0 256 0a256 256 0 1 0 0 512z"></path>
              </svg>
            </template>
            <div>
              <h1>Custom page</h1>
              <p>This is the content of the custom page.</p>
            </div>
          </OrganizationProfile.Page>
        
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
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" fill="currentColor">
                  <path d="M256 512A256 256 0 1 0 256 0a256 256 0 1 0 0 512z"></path>
                </svg>
              </template>
              <div>
                <h1>Custom page</h1>
                <p>This is the content of the custom page.</p>
              </div>
            </OrganizationSwitcher.OrganizationProfilePage>
          
        </header>
      </template>
      ```


**Dedicated page:**

```vue
// Filename: pages/organization-profile.vue

      <script setup lang="ts">
      // Components are automatically imported
      </script>

      <template>
        
          
            <template #labelIcon>
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" fill="currentColor">
                <path d="M256 512A256 256 0 1 0 256 0a256 256 0 1 0 0 512z"></path>
              </svg>
            </template>
            <div>
              <h1>Custom page</h1>
              <p>This is the content of the custom page.</p>
            </div>
          </OrganizationProfile.Page>
        
      </template>
      ```

  


  To add custom pages to the `` component using the [JavaScript SDK](/reference/javascript/overview), pass the `customPages` property to the `mountOrganizationProfile()` method, as shown in the following example:

  ```js
// Filename: main.js

  import { Clerk } from '@clerk/clerk-js'

  const pubKey = import.meta.env.VITE_CLERK_PUBLISHABLE_KEY

  const clerk = new Clerk(pubKey)
  await clerk.load()

  document.getElementById('app').innerHTML = `
    <div id="organization-profile"></div>
  `

  const orgProfileDiv = document.getElementById('organization-profile')

  clerk.mountOrganizationProfile(orgProfileDiv, {
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
  > It is not possible to add custom links to the `` component when using the [JavaScript SDK](/reference/javascript/overview). The `mountOrganizationProfile()` method does not have a property for adding custom links.


  To add a custom link to the `` navigation sidenav, you will need to use one of the following components, depending on the use case mentioned in the [Before you start](#before-you-start) section.

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

  The full URL or path that will be used to navigate to the external link. For path segments, if the `` component is rendered at `/organization`, then the external link will be accessed at `/organization/{url}` when using [path routing](/guides/how-clerk-works/routing).


  ### Example

  The following example adds a custom link to the `` sidenav that navigates to the homepage.

  
    
**:**

```tsx
// Filename: components/Header.tsx

      const DotIcon = () => {
        return (
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" fill="currentColor">
            <path d="M256 512A256 256 0 1 0 256 0a256 256 0 1 0 0 512z" />
          </svg>
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
// Filename: organization-profile/page.tsx

      const DotIcon = () => {
        return (
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" fill="currentColor">
            <path d="M256 512A256 256 0 1 0 256 0a256 256 0 1 0 0 512z" />
          </svg>
        )
      }

      const OrganizationProfilePage = () => (
        
          
        
      )

      export default OrganizationProfilePage
      ```

  

  
    
**:**

```astro
// Filename: pages/index.astro

      ---
      import { OrganizationSwitcher } from '@clerk/astro/components'
      ---

      <header>
        
          
            <svg
              slot="label-icon"
              xmlns="http://www.w3.org/2000/svg"
              viewBox="0 0 512 512"
              fill="currentColor"
            >
              <path d="M256 512A256 256 0 1 0 256 0a256 256 0 1 0 0 512z"></path>
            </svg>
          </OrganizationSwitcher.OrganizationProfileLink>
        
      </header>
      ```


**Dedicated page:**

```astro
// Filename: pages/organization-profile.astro

      ---
      import { OrganizationProfile } from '@clerk/astro/components'
      ---

      
        
          <svg
            slot="label-icon"
            xmlns="http://www.w3.org/2000/svg"
            viewBox="0 0 512 512"
            fill="currentColor"
          >
            <path d="M256 512A256 256 0 1 0 256 0a256 256 0 1 0 0 512z"></path>
          </svg>
        </OrganizationProfile.Link>
      
      ```

  

  
    
**:**

```vue
// Filename: App.vue

      <script setup lang="ts">
      import { OrganizationSwitcher } from '@clerk/vue'
      </script>

      <template>
        <header>
          
            
              <template #labelIcon>
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" fill="currentColor">
                  <path d="M256 512A256 256 0 1 0 256 0a256 256 0 1 0 0 512z"></path>
                </svg>
              </template>
            </OrganizationSwitcher.OrganizationProfileLink>
          
        </header>
      </template>
      ```


**Dedicated page:**

```vue
// Filename: pages/organization-profile.vue

      <script setup lang="ts">
      import { OrganizationProfile } from '@clerk/vue'
      </script>

      <template>
        
          
            <template #labelIcon>
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" fill="currentColor">
                <path d="M256 512A256 256 0 1 0 256 0a256 256 0 1 0 0 512z"></path>
              </svg>
            </template>
          </OrganizationProfile.Link>
        
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
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" fill="currentColor">
                  <path d="M256 512A256 256 0 1 0 256 0a256 256 0 1 0 0 512z"></path>
                </svg>
              </template>
            </OrganizationSwitcher.OrganizationProfileLink>
          
        </header>
      </template>
      ```


**Dedicated page:**

```vue
// Filename: pages/organization-profile.vue

      <script setup lang="ts">
      // Components are automatically imported
      </script>

      <template>
        
          
            <template #labelIcon>
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" fill="currentColor">
                <path d="M256 512A256 256 0 1 0 256 0a256 256 0 1 0 0 512z"></path>
              </svg>
            </template>
          </OrganizationProfile.Link>
        
      </template>
      ```

  


## Reorder default routes

The `` component includes two default menu items: `Members` and `General`, in that order. You can reorder these default items by setting the `label` prop to `'members'` or `'general'`. This will target the existing default item and allow you to rearrange it.

Note that when reordering default routes, the first item in the navigation sidenav cannot be a custom link.

### Example

The following example adds a custom page as the first item in the sidenav, followed by a custom link to the homepage, and then the default `Members` and `General` pages.


  
**:**

```tsx
// Filename: components/Header.tsx

    const DotIcon = () => {
      return (
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" fill="currentColor">
          <path d="M256 512A256 256 0 1 0 256 0a256 256 0 1 0 0 512z" />
        </svg>
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
        
          
            </OrganizationSwitcher.OrganizationProfilePage>
          
          
          
        
      </header>
    )

    export default Header
    ```


**Dedicated Page:**

```tsx
// Filename: organization-profile/page.tsx

    const DotIcon = () => {
      return (
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" fill="currentColor">
          <path d="M256 512A256 256 0 1 0 256 0a256 256 0 1 0 0 512z" />
        </svg>
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

    const OrganizationProfilePage = () => (
      
        
          </OrganizationProfile.Page>
        
        
        
      
    )

    export default OrganizationProfilePage
    ```


  
**:**

```astro
// Filename: pages/index.astro

    ---
    import { OrganizationSwitcher } from '@clerk/astro/components'
    ---

    <header>
      
        
          <svg
            slot="label-icon"
            xmlns="http://www.w3.org/2000/svg"
            viewBox="0 0 512 512"
            fill="currentColor"
          >
            <path d="M256 512A256 256 0 1 0 256 0a256 256 0 1 0 0 512z"></path>
          </svg>
          <div>
            <h1>Custom page</h1>
            <p>This is the content of the custom page.</p>
          </div>
        </OrganizationSwitcher.OrganizationProfilePage>
        
          <svg
            slot="label-icon"
            xmlns="http://www.w3.org/2000/svg"
            viewBox="0 0 512 512"
            fill="currentColor"
          >
            <path d="M256 512A256 256 0 1 0 256 0a256 256 0 1 0 0 512z"></path>
          </svg>
        </OrganizationSwitcher.OrganizationProfileLink>
        
        
      
    </header>
    ```


**Dedicated page:**

```astro
// Filename: pages/organization-profile.astro

    ---
    import { OrganizationProfile } from '@clerk/astro/components'
    ---

    
      
        <svg
          slot="label-icon"
          xmlns="http://www.w3.org/2000/svg"
          viewBox="0 0 512 512"
          fill="currentColor"
        >
          <path d="M256 512A256 256 0 1 0 256 0a256 256 0 1 0 0 512z"></path>
        </svg>
        <div>
          <h1>Custom page</h1>
          <p>This is the content of the custom page.</p>
        </div>
      </OrganizationProfile.Page>
      
        <svg
          slot="label-icon"
          xmlns="http://www.w3.org/2000/svg"
          viewBox="0 0 512 512"
          fill="currentColor"
        >
          <path d="M256 512A256 256 0 1 0 256 0a256 256 0 1 0 0 512z"></path>
        </svg>
      </OrganizationProfile.Link>
      
      
    
    ```


  ```js
// Filename: main.js

  import { Clerk } from '@clerk/clerk-js'

  const pubKey = import.meta.env.VITE_CLERK_PUBLISHABLE_KEY

  const clerk = new Clerk(pubKey)
  await clerk.load()

  document.getElementById('app').innerHTML = `
    <div id="organization-profile"></div>
  `

  const orgProfileDiv = document.getElementById('organization-profile')

  clerk.mountOrganizationProfile(orgProfileDiv, {
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
        label: 'members',
      },
      {
        label: 'general',
      },
    ],
  })
  ```


  
**:**

```vue
// Filename: App.vue

    <script setup lang="ts">
    import { OrganizationSwitcher } from '@clerk/vue'
    </script>

    <template>
      <header>
        
          
            <template #labelIcon>
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" fill="currentColor">
                <path d="M256 512A256 256 0 1 0 256 0a256 256 0 1 0 0 512z"></path>
              </svg>
            </template>
            <div>
              <h1>Custom page</h1>
              <p>This is the content of the custom page.</p>
            </div>
          </OrganizationSwitcher.OrganizationProfilePage>
          
            <template #labelIcon>
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" fill="currentColor">
                <path d="M256 512A256 256 0 1 0 256 0a256 256 0 1 0 0 512z"></path>
              </svg>
            </template>
          </OrganizationSwitcher.OrganizationProfileLink>
          
          
        
      </header>
    </template>
    ```


**Dedicated page:**

```vue
// Filename: pages/organization-profile.vue

    <script setup lang="ts">
    import { OrganizationProfile } from '@clerk/vue'
    </script>

    <template>
      
        
          <template #labelIcon>
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" fill="currentColor">
              <path d="M256 512A256 256 0 1 0 256 0a256 256 0 1 0 0 512z"></path>
            </svg>
          </template>
          <div>
            <h1>Custom page</h1>
            <p>This is the content of the custom page.</p>
          </div>
        </OrganizationProfile.Page>
        
          <template #labelIcon>
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" fill="currentColor">
              <path d="M256 512A256 256 0 1 0 256 0a256 256 0 1 0 0 512z"></path>
            </svg>
          </template>
        </OrganizationProfile.Link>
        
        
      
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
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" fill="currentColor">
                <path d="M256 512A256 256 0 1 0 256 0a256 256 0 1 0 0 512z"></path>
              </svg>
            </template>
            <div>
              <h1>Custom page</h1>
              <p>This is the content of the custom page.</p>
            </div>
          </OrganizationSwitcher.OrganizationProfilePage>
          
            <template #labelIcon>
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" fill="currentColor">
                <path d="M256 512A256 256 0 1 0 256 0a256 256 0 1 0 0 512z"></path>
              </svg>
            </template>
          </OrganizationSwitcher.OrganizationProfileLink>
          
          
        
      </header>
    </template>
    ```


**Dedicated page:**

```vue
// Filename: pages/organization-profile.vue

    <script setup lang="ts">
    // Components are automatically imported
    </script>

    <template>
      
        
          <template #labelIcon>
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" fill="currentColor">
              <path d="M256 512A256 256 0 1 0 256 0a256 256 0 1 0 0 512z"></path>
            </svg>
          </template>
          <div>
            <h1>Custom page</h1>
            <p>This is the content of the custom page.</p>
          </div>
        </OrganizationProfile.Page>
        
          <template #labelIcon>
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" fill="currentColor">
              <path d="M256 512A256 256 0 1 0 256 0a256 256 0 1 0 0 512z"></path>
            </svg>
          </template>
        </OrganizationProfile.Link>
        
        
      
    </template>
    ```
