# Add custom items and links to the `<UserButton />` component


> Learn how to add custom items and include external links within the <UserButton /> menu.

The [``](/reference/components/user/user-button) component supports _custom_ menu items, allowing the incorporation of app-specific settings or additional functionality.

There are two types of custom menu items available:

- [``](#user-button-action) - A menu item that triggers an action when clicked.
- [``](#user-button-link) - A menu item that navigates to a page when clicked.

You can also [reorder default items](#reorder-default-items) and [conditionally render menu items](#conditionally-render-menu-items).

## ``

`` allows you to add actions to the `` component, like opening a chat or triggering a modal.

### Props

`` accepts the following props:

- **`label`** `string`

  The name that will be displayed in the menu of the user button.

    ---

- **`labelIcon`** `React.ReactElement`

  An icon displayed next to the label in the menu.

    ---

- **`open?`** `string`

  The path segment that will be used to open the user profile modal to a specific page.

    ---

- **`onClick?`** `void`

  A function to be called when the menu item is clicked.


### Examples

#### Add an action

The following example adds an "Open chat" action to the `` component. When a user selects the ``, there will be an "Open chat" menu item.


  ```tsx
  const DotIcon = () => {
    return (
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" fill="currentColor">
        <path d="M256 512A256 256 0 1 0 256 0a256 256 0 1 0 0 512z" />
      </svg>
    )
  }

  const CustomUserButton = () => {
    return (
      <header>
        
          
             alert('init chat')}
            />
          </UserButton.MenuItems>
        
      </header>
    )
  }

  export default CustomUserButton
  ```


  In Astro components, props are converted to strings, so you can't use an `onClick` handler to handle click events. Instead, you can set an arbitrary prop, set up a custom event listener that will check for the value passed to that prop, and then execute a desired action based on that value.

  For example, `clickIdentifier` is the arbitrary prop being used to identify the click event. Two `` components are added to the menu, each with a different `clickIdentifier` prop. When the menu item is clicked, the custom event listener will check for the value passed to the `clickIdentifier` prop, either `"open_chat"` or `"open_cart"`, and then execute an action based on that value.

  ```astro
// Filename: pages/index.astro

  ---
  import { UserButton } from '@clerk/astro/components'
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
        </UserButton.Action>
        
          <svg
            slot="label-icon"
            xmlns="http://www.w3.org/2000/svg"
            viewBox="0 0 512 512"
            fill="currentColor"
          >
            <path d="M256 512A256 256 0 1 0 256 0a256 256 0 1 0 0 512z"></path>
          </svg>
        </UserButton.Action>
      </UserButton.MenuItems>
    
  </header>

  <script>
    document.addEventListener('clerk:menu-item-click', (e) => {
      if (e.detail === 'open_chat') {
        console.log('init chat')
      }
      if (e.detail === 'open_cart') {
        console.log('init cart')
      }
    })
  </script>
  ```


  To add custom menu items to the `` component using the [JavaScript SDK](/reference/javascript/overview), pass the `customMenuItems` property to the `mountUserButton()` method, as shown in the following example:

  ```js
// Filename: main.js

  import { Clerk } from '@clerk/clerk-js'

  const pubKey = import.meta.env.VITE_CLERK_PUBLISHABLE_KEY

  const clerk = new Clerk(pubKey)
  await clerk.load()

  document.getElementById('app').innerHTML = `
    <div id="user-button"></div>
  `

  const userButtonDiv = document.getElementById('user-button')

  clerk.mountUserButton(userButtonDiv, {
    customMenuItems: [
      {
        label: 'Open chat',
        onClick: () => {
          alert('init chat') // your custom event
        },
        mountIcon: (el) => {
          el.innerHTML = '👤'
        },
        unmountIcon: (el) => {},
      },
    ],
  })
  ```


  ```vue
// Filename: App.vue

  <script setup lang="ts">
  import { UserButton } from '@clerk/vue'

  function openChat() {
    alert('init chat')
  }
  </script>

  <template>
    <header>
      
        
          
            <template #labelIcon>
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" fill="currentColor">
                <path d="M256 512A256 256 0 1 0 256 0a256 256 0 1 0 0 512z"></path>
              </svg>
            </template>
          </UserButton.Action>
        </UserButton.MenuItems>
      
    </header>
  </template>
  ```


  ```vue
// Filename: App.vue

  <script setup lang="ts">
  // Components are automatically imported
  function openChat() {
    alert('init chat')
  }
  </script>

  <template>
    <header>
      
        
          
            <template #labelIcon>
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" fill="currentColor">
                <path d="M256 512A256 256 0 1 0 256 0a256 256 0 1 0 0 512z"></path>
              </svg>
            </template>
          </UserButton.Action>
        </UserButton.MenuItems>
      
    </header>
  </template>
  ```


#### Add an action and a custom page

The following example adds an "Open help" action to the `` component, as well as a [custom page](/guides/customizing-clerk/adding-items/user-profile) titled "Help". When a user selects the ``, there will be "Open help" and "Help" menu items.


  ```tsx
  const DotIcon = () => {
    return (
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" fill="currentColor">
        <path d="M256 512A256 256 0 1 0 256 0a256 256 0 1 0 0 512z" />
      </svg>
    )
  }

  const CustomUserButton = () => {
    return (
      <header>
        
          
            
          </UserButton.MenuItems>

          
            <div>
              <h1>Help Page</h1>
              <p>This is the custom help page</p>
            </div>
          </UserButton.UserProfilePage>
        
      </header>
    )
  }

  export default CustomUserButton
  ```


  ```astro
// Filename: pages/index.astro

  ---
  import { UserButton } from '@clerk/astro/components'
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
        </UserButton.Action>
      </UserButton.MenuItems>

      
        <svg
          slot="label-icon"
          xmlns="http://www.w3.org/2000/svg"
          viewBox="0 0 512 512"
          fill="currentColor"
        >
          <path d="M256 512A256 256 0 1 0 256 0a256 256 0 1 0 0 512z"></path>
        </svg>
        <div>
          <h1>Help Page</h1>
          <p>This is the custom help page</p>
        </div>
      </UserButton.UserProfilePage>
    
  </header>
  ```


  To add custom pages to the `` component using the [JavaScript SDK](/reference/javascript/overview), pass the `customPages` property to the `mountUserProfile()` method, as shown in the following example:

  ```js
// Filename: main.js

  import { Clerk } from '@clerk/clerk-js'

  const pubKey = import.meta.env.VITE_CLERK_PUBLISHABLE_KEY

  const clerk = new Clerk(pubKey)
  await clerk.load()

  document.getElementById('app').innerHTML = `
    <div id="user-button"></div>
    <div id="user-profile"></div>
  `

  const userButtonDiv = document.getElementById('user-button')
  const userProfileDiv = document.getElementById('user-profile')

  clerk.mountUserButton(userButtonDiv, {
    customMenuItems: [
      {
        label: 'Open help',
        onClick: () => {
          window.location.href = '/#/help'
        },
        mountIcon: (el) => {
          el.innerHTML = '👤'
        },
        unmountIcon: (el) => {},
      },
    ],
  })

  clerk.mountUserProfile(userProfileDiv, {
    customPages: [
      {
        url: '/help',
        label: 'Help',
        mountIcon: (el) => {
          el.innerHTML = '👤'
        },
        unmountIcon: (el) => {
          el.innerHTML = ''
        },
        mount: (el) => {
          el.innerHTML = `
            <h1>Help Page</h1>
            <p>This is the custom help page</p>
            `
        },
        unmount: (el) => {
          el.innerHTML = ''
        },
      },
    ],
  })
  ```


  ```vue
// Filename: App.vue

  <script setup lang="ts">
  import { UserButton } from '@clerk/vue'
  </script>

  <template>
    <header>
      
        
          
            <template #labelIcon>
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" fill="currentColor">
                <path d="M256 512A256 256 0 1 0 256 0a256 256 0 1 0 0 512z"></path>
              </svg>
            </template>
          </UserButton.Action>
        </UserButton.MenuItems>

        
          <template #labelIcon>
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" fill="currentColor">
              <path d="M256 512A256 256 0 1 0 256 0a256 256 0 1 0 0 512z"></path>
            </svg>
          </template>
          <div>
            <h1>Help Page</h1>
            <p>This is the custom help page</p>
          </div>
        </UserButton.UserProfilePage>
      
    </header>
  </template>
  ```


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
          </UserButton.Action>
        </UserButton.MenuItems>

        
          <template #labelIcon>
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" fill="currentColor">
              <path d="M256 512A256 256 0 1 0 256 0a256 256 0 1 0 0 512z"></path>
            </svg>
          </template>
          <div>
            <h1>Help Page</h1>
            <p>This is the custom help page</p>
          </div>
        </UserButton.UserProfilePage>
      
    </header>
  </template>
  ```


## ``

`` allows you to add links to the `` component, like custom pages or external URLs.

### Props

`` accept the following props, all of which are **required**:

- **`label`** `string`

  The name that will be displayed in the menu of the user button.

    ---

- **`labelIcon`** `React.ReactElement`

  An icon displayed next to the label in the menu.

    ---

- **`href`** `string`

  The path segment that will be used to navigate to the custom page.


### Example

The following example adds a "Create organization" link to the `` component. When a user selects the ``, there will be a "Create organization" menu item.


  ```tsx
  const DotIcon = () => {
    return (
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" fill="currentColor">
        <path d="M256 512A256 256 0 1 0 256 0a256 256 0 1 0 0 512z" />
      </svg>
    )
  }

  const CustomUserButton = () => {
    return (
      <header>
        
          
            
          </UserButton.MenuItems>
        
      </header>
    )
  }

  export default CustomUserButton
  ```


  ```astro
// Filename: pages/index.astro

  ---
  import { UserButton } from '@clerk/astro/components'
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
        </UserButton.Link>
      </UserButton.MenuItems>
    
  </header>
  ```


  To add custom menu items to the `` component using the [JavaScript SDK](/reference/javascript/overview), pass the `customMenuItems` property to the `mountUserButton()` method, as shown in the following example:

  ```js
// Filename: main.js

  import { Clerk } from '@clerk/clerk-js'

  const pubKey = import.meta.env.VITE_CLERK_PUBLISHABLE_KEY

  const clerk = new Clerk(pubKey)
  await clerk.load()

  document.getElementById('app').innerHTML = `
    <div id="user-button"></div>
  `

  const userButtonDiv = document.getElementById('user-button')

  clerk.mountUserButton(userButtonDiv, {
    customMenuItems: [
      {
        label: 'Create organization',
        href: '/create-organization',
        mountIcon: (el) => {
          el.innerHTML = '👤'
        },
        unmountIcon: (el) => {},
      },
    ],
  })
  ```


  ```vue
// Filename: App.vue

  <script setup lang="ts">
  import { UserButton } from '@clerk/vue'
  </script>

  <template>
    <header>
      
        
          
            <template #labelIcon>
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" fill="currentColor">
                <path d="M256 512A256 256 0 1 0 256 0a256 256 0 1 0 0 512z"></path>
              </svg>
            </template>
          </UserButton.Link>
        </UserButton.MenuItems>
      
    </header>
  </template>
  ```


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
          </UserButton.Link>
        </UserButton.MenuItems>
      
    </header>
  </template>
  ```


## Reorder default items

The `` component includes two default menu items: `Manage account` and `Sign out`, in that order. You can reorder these default items by setting the `label` prop to `'manageAccount'` or `'signOut'`. This will target the existing default item and allow you to rearrange it.

In the following example, the "Sign out" menu item is moved to the top of the menu, a custom "Create organization" link is added as the second menu item, and the "Manage account" menu item is moved to the bottom of the menu.


  ```tsx
  const DotIcon = () => {
    return (
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" fill="currentColor">
        <path d="M256 512A256 256 0 1 0 256 0a256 256 0 1 0 0 512z" />
      </svg>
    )
  }

  const CustomUserButton = () => {
    return (
      <header>
        
          
            
            
            
          </UserButton.MenuItems>
        
      </header>
    )
  }

  export default CustomUserButton
  ```


  ```astro
// Filename: pages/index.astro

  ---
  import { UserButton } from '@clerk/astro/components'
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
        </UserButton.Link>
        
      </UserButton.MenuItems>
    
  </header>
  ```


  ```js
// Filename: main.js

  import { Clerk } from '@clerk/clerk-js'

  const pubKey = import.meta.env.VITE_CLERK_PUBLISHABLE_KEY

  const clerk = new Clerk(pubKey)
  await clerk.load()

  document.getElementById('app').innerHTML = `
    <div id="user-button"></div>
  `

  const userButtonDiv = document.getElementById('user-button')

  clerk.mountUserButton(userButtonDiv, {
    customMenuItems: [
      {
        label: 'signOut',
      },
      {
        label: 'Create organization',
        href: '/create-organization',
        mountIcon: (el) => {
          el.innerHTML = '👤'
        },
        unmountIcon: (el) => {},
      },
      {
        label: 'manageAccount',
      },
    ],
  })
  ```


  ```vue
// Filename: App.vue

  <script setup lang="ts">
  import { UserButton } from '@clerk/vue'
  </script>

  <template>
    <header>
      
        
          
          
            <template #labelIcon>
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" fill="currentColor">
                <path d="M256 512A256 256 0 1 0 256 0a256 256 0 1 0 0 512z"></path>
              </svg>
            </template>
          </UserButton.Link>
          
        </UserButton.MenuItems>
      
    </header>
  </template>
  ```


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
          </UserButton.Link>
          
        </UserButton.MenuItems>
      
    </header>
  </template>
  ```


## Conditionally render menu items


  To conditionally render menu items based on a user's Role or Custom Permissions, you can use the [`has()`](/reference/backend/types/auth-object#has) helper function.


  To conditionally render menu items based on a user's Role or Custom Permissions, you can use the [`checkAuthorization()`](/reference/javascript/session#check-authorization) method to check if a user is authorized.


In the following example, the "Create organization" menu item will only render if the current user has the `org:app:admin` permission.


  ```tsx
  const DotIcon = () => {
    return (
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" fill="currentColor">
        <path d="M256 512A256 256 0 1 0 256 0a256 256 0 1 0 0 512z" />
      </svg>
    )
  }

  const CustomUserButton = () => {
    const { has, isLoaded } = useAuth()

    if (!isLoaded) {
      return <span>Loading...</span>
    }

    const isAdmin = has({ permission: 'org:app:admin' })

    return (
      <header>
        
          {isAdmin && (
            
              
            </UserButton.MenuItems>
          )}
        
      </header>
    )
  }

  export default CustomUserButton
  ```


  ```astro
// Filename: pages/index.astro

  ---
  import { UserButton } from '@clerk/astro/components'

  const { has } = Astro.locals.auth()

  const isAdmin = has({ permission: 'org:app:admin' })
  ---

  <header>
    
      {
        isAdmin && (
          
            
              <svg
                slot="label-icon"
                xmlns="http://www.w3.org/2000/svg"
                viewBox="0 0 512 512"
                fill="currentColor"
              >
                <path d="M256 512A256 256 0 1 0 256 0a256 256 0 1 0 0 512z" />
              </svg>
            </UserButton.Link>
          </UserButton.MenuItems>
        )
      }
    
  </header>
  ```


  ```js
// Filename: main.js

  import { Clerk } from '@clerk/clerk-js'

  const pubKey = import.meta.env.VITE_CLERK_PUBLISHABLE_KEY

  const clerk = new Clerk(pubKey)
  await clerk.load()

  document.getElementById('app').innerHTML = `
    <div id="user-button"></div>
  `

  const userButtonDiv = document.getElementById('user-button')
  // Check if the user is authenticated
  if (clerk.isSignedIn) {
    const hasAdminPermission = clerk.session.checkAuthorization({
      permission: 'org:app:admin',
    })

    if (hasAdminPermission) {
      clerk.mountUserButton(userButtonDiv, {
        customMenuItems: [
          {
            label: 'signOut',
          },
          {
            label: 'Create organization',
            href: '/create-organization',
            mountIcon: (el) => {
              el.innerHTML = '👤'
            },
            unmountIcon: (el) => {},
          },
          {
            label: 'manageAccount',
          },
        ],
      })
    } else {
      clerk.mountUserButton(userButtonDiv)
    }
  }
  ```


  ```vue
// Filename: App.vue

  <script setup lang="ts">
  import { UserButton, useAuth } from '@clerk/vue'
  import { computed } from 'vue'

  const { has, isLoaded } = useAuth()

  const isAdmin = computed(() => has.value?.({ permission: 'org:app:admin' }))
  </script>

  <template>
    <header v-if="isLoaded && isAdmin">
      
        
          
            <template #labelIcon>
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" fill="currentColor">
                <path d="M256 512A256 256 0 1 0 256 0a256 256 0 1 0 0 512z"></path>
              </svg>
            </template>
          </UserButton.Link>
        </UserButton.MenuItems>
      
    </header>
  </template>
  ```


  ```vue
// Filename: App.vue

  <script setup lang="ts">
  // Components are automatically imported
  import { useAuth } from '@clerk/vue'
  import { computed } from 'vue'

  const { has, isLoaded } = useAuth()

  const isAdmin = computed(() => has.value?.({ permission: 'org:app:admin' }))
  </script>

  <template>
    <header v-if="isLoaded && isAdmin">
      
        
          
            <template #labelIcon>
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" fill="currentColor">
                <path d="M256 512A256 256 0 1 0 256 0a256 256 0 1 0 0 512z"></path>
              </svg>
            </template>
          </UserButton.Link>
        </UserButton.MenuItems>
      
    </header>
  </template>
  ```
