# useOrganizationList()


> Access and manage the current user's Organization list in your React application with Clerk's useOrganizationList() hook.

The `useOrganizationList()` hook provides access to the current user's Organization memberships, invitations, and suggestions. It also includes methods for creating new Organizations and managing the Active Organization.

## Parameters

`useOrganizationList()` accepts a single object with the following properties:

> [!WARNING]
> By default, the `userMemberships`, `userInvitations`, and `userSuggestions` attributes are not populated. To fetch and paginate the data, you must pass `true` or an object with the desired properties.

### Shared properties

Optional properties that are shared across the `userMemberships`, `userInvitations`, and `userSuggestions` properties.

## Returns

### `CreateOrganizationParams`

### `PaginatedResources`

To see the different Organization features integrated into one application, take a look at our [Organizations demo repository](https://github.com/clerk/organizations-demo).

## Examples

### Expanding and paginating attributes

To keep network usage to a minimum, developers are required to opt-in by specifying which resource they need to fetch and paginate through. So by default, the `userMemberships`, `userInvitations`, and `userSuggestions` attributes are not populated. You must pass `true` or an object with the desired [properties](#shared-properties) to fetch and paginate the data.

```jsx
// userMemberships.data will never be populated
const { userMemberships } = useOrganizationList()

// Use default values to fetch userMemberships, such as initialPage = 1 and pageSize = 10
const { userMemberships } = useOrganizationList({
  userMemberships: true,
})

// Pass your own values to fetch userMemberships
const { userMemberships } = useOrganizationList({
  userMemberships: {
    pageSize: 20,
    initialPage: 2, // skips the first page
  },
})

// Aggregate pages in order to render an infinite list
const { userMemberships } = useOrganizationList({
  userMemberships: {
    infinite: true,
  },
})
```

### Infinite pagination

The following example demonstrates how to use the `infinite` property to fetch and append new data to the existing list. The `userMemberships` attribute will be populated with the first page of the user's Organization memberships. When the "Load more" button is clicked, the `fetchNext` helper function will be called to append the next page of memberships to the list.


  ```tsx
// Filename: src/components/JoinedOrganizations.tsx

  import { useOrganizationList } from '@clerk/react'
  import React from 'react'

  const JoinedOrganizations = () => {
    const { isLoaded, setActive, userMemberships } = useOrganizationList({
      userMemberships: {
        infinite: true,
      },
    })

    // Handle loading state
    if (!isLoaded) return <div>Loading...</div>

    return (
      <>
        <ul>
          {userMemberships.data?.map((mem) => (
            <li key={mem.id}>
              <span>{mem.organization.name}</span>
              <button onClick={() => setActive({ organization: mem.organization.id })}>Select</button>
            </li>
          ))}
        </ul>

        <button disabled={!userMemberships.hasNextPage} onClick={() => userMemberships.fetchNext()}>
          Load more
        </button>
      </>
    )
  }

  export default JoinedOrganizations
  ```


  ```tsx
// Filename: components/JoinedOrganizations.tsx

  'use client'

  import { useOrganizationList } from '@clerk/nextjs'

  export const JoinedOrganizations = () => {
    const { isLoaded, setActive, userMemberships } = useOrganizationList({
      userMemberships: {
        infinite: true,
      },
    })

    // Handle loading state
    if (!isLoaded) return <div>Loading...</div>

    return (
      <>
        <ul>
          {userMemberships.data?.map((mem) => (
            <li key={mem.id}>
              <span>{mem.organization.name}</span>
              <button onClick={() => setActive({ organization: mem.organization.id })}>Select</button>
            </li>
          ))}
        </ul>

        <button disabled={!userMemberships.hasNextPage} onClick={() => userMemberships.fetchNext()}>
          Load more
        </button>
      </>
    )
  }
  ```


  ```tsx
// Filename: components/JoinedOrganizations.tsx

  import { useOrganizationList } from '@clerk/react-router'

  export function JoinedOrganizations() {
    const { isLoaded, setActive, userMemberships } = useOrganizationList({
      userMemberships: {
        infinite: true,
      },
    })

    // Handle loading state
    if (!isLoaded) return <div>Loading...</div>

    return (
      <>
        <ul>
          {userMemberships.data?.map((mem) => (
            <li key={mem.id}>
              <span>{mem.organization.name}</span>
              <button onClick={() => setActive({ organization: mem.organization.id })}>Select</button>
            </li>
          ))}
        </ul>

        <button disabled={!userMemberships.hasNextPage} onClick={() => userMemberships.fetchNext()}>
          Load more
        </button>
      </>
    )
  }
  ```


  ```jsx
// Filename: components/JoinedOrganizations.tsx

  import { useOrganizationList } from '@clerk/chrome-extension'

  export function JoinedOrganizations() {
    const { isLoaded, setActive, userMemberships } = useOrganizationList({
      userMemberships: {
        infinite: true,
      },
    })

    // Handle loading state
    if (!isLoaded) return <div>Loading...</div>

    return (
      <>
        <ul>
          {userMemberships.data?.map((mem) => (
            <li key={mem.id}>
              <span>{mem.organization.name}</span>
              <button onClick={() => setActive({ organization: mem.organization.id })}>Select</button>
            </li>
          ))}
        </ul>

        <button disabled={!userMemberships.hasNextPage} onClick={() => userMemberships.fetchNext()}>
          Load more
        </button>
      </>
    )
  }
  ```


  ```tsx
// Filename: components/JoinedOrganizations.tsx

  import { useOrganizationList } from '@clerk/tanstack-react-start'

  export function JoinedOrganizations() {
    const { isLoaded, setActive, userMemberships } = useOrganizationList({
      userMemberships: {
        infinite: true,
      },
    })

    // Handle loading state
    if (!isLoaded) return <div>Loading...</div>

    return (
      <>
        <ul>
          {userMemberships.data?.map((mem) => (
            <li key={mem.id}>
              <span>{mem.organization.name}</span>
              <button onClick={() => setActive({ organization: mem.organization.id })}>Select</button>
            </li>
          ))}
        </ul>

        <button disabled={!userMemberships.hasNextPage} onClick={() => userMemberships.fetchNext()}>
          Load more
        </button>
      </>
    )
  }
  ```


  ```tsx
// Filename: components/JoinedOrganizations.tsx

  import { useOrganizationList } from '@clerk/expo'
  import { Text, View, TouchableOpacity, ScrollView } from 'react-native'

  export function JoinedOrganizations() {
    const { isLoaded, setActive, userMemberships } = useOrganizationList({
      userMemberships: {
        infinite: true,
      },
    })

    // Handle loading state
    if (!isLoaded) return Loading...

    return (
      
        
          {userMemberships.data?.map((mem) => (
            
              {mem.organization.name}
               setActive({ organization: mem.organization.id })}>
                Select
              
            
          ))}
        

         userMemberships.fetchNext()}
        >
          Load more
        
      
    )
  }
  ```


### Simple pagination

The following example demonstrates how to use the `fetchPrevious` and `fetchNext` helper functions to paginate through the data. The `userInvitations` attribute will be populated with the first page of invitations. When the "Previous page" or "Next page" button is clicked, the `fetchPrevious` or `fetchNext` helper function will be called to fetch the previous or next page of invitations.

Notice the difference between this example's pagination and the infinite pagination example above.


  ```tsx
// Filename: src/components/UserInvitationsTable.tsx

  import { useOrganizationList } from '@clerk/react'
  import React from 'react'

  const UserInvitationsTable = () => {
    const { isLoaded, userInvitations } = useOrganizationList({
      userInvitations: {
        infinite: true,
        keepPreviousData: true,
      },
    })

    // Handle loading state
    if (!isLoaded || userInvitations.isLoading) return <div>Loading...</div>

    return (
      <>
        <table>
          <thead>
            <tr>
              <th>Email</th>
              <th>Org name</th>
            </tr>
          </thead>

          <tbody>
            {userInvitations.data?.map((inv) => (
              <tr key={inv.id}>
                <th>{inv.emailAddress}</th>
                <th>{inv.publicOrganizationData.name}</th>
              </tr>
            ))}
          </tbody>
        </table>

        <button disabled={!userInvitations.hasPreviousPage} onClick={userInvitations.fetchPrevious}>
          Prev
        </button>
        <button disabled={!userInvitations.hasNextPage} onClick={userInvitations.fetchNext}>
          Next
        </button>
      </>
    )
  }

  export default UserInvitationsTable
  ```


  ```tsx
// Filename: components/UserInvitationsTable.tsx

  'use client'

  import { useOrganizationList } from '@clerk/nextjs'

  export const UserInvitationsTable = () => {
    const { isLoaded, userInvitations } = useOrganizationList({
      userInvitations: {
        infinite: true,
        keepPreviousData: true,
      },
    })

    // Handle loading state
    if (!isLoaded || userInvitations.isLoading) return <div>Loading...</div>

    return (
      <>
        <table>
          <thead>
            <tr>
              <th>Email</th>
              <th>Org name</th>
            </tr>
          </thead>

          <tbody>
            {userInvitations.data?.map((inv) => (
              <tr key={inv.id}>
                <th>{inv.emailAddress}</th>
                <th>{inv.publicOrganizationData.name}</th>
              </tr>
            ))}
          </tbody>
        </table>

        <button disabled={!userInvitations.hasPreviousPage} onClick={userInvitations.fetchPrevious}>
          Prev
        </button>
        <button disabled={!userInvitations.hasNextPage} onClick={userInvitations.fetchNext}>
          Next
        </button>
      </>
    )
  }
  ```


  ```tsx
// Filename: components/UserInvitationsTable.tsx

  import { useOrganizationList } from '@clerk/react-router'

  export function UserInvitationsTable() {
    const { isLoaded, userInvitations } = useOrganizationList({
      userInvitations: {
        infinite: true,
        keepPreviousData: true,
      },
    })

    // Handle loading state
    if (!isLoaded || userInvitations.isLoading) return <div>Loading...</div>

    return (
      <>
        <table>
          <thead>
            <tr>
              <th>Email</th>
              <th>Org name</th>
            </tr>
          </thead>

          <tbody>
            {userInvitations.data?.map((inv) => (
              <tr key={inv.id}>
                <th>{inv.emailAddress}</th>
                <th>{inv.publicOrganizationData.name}</th>
              </tr>
            ))}
          </tbody>
        </table>

        <button disabled={!userInvitations.hasPreviousPage} onClick={userInvitations.fetchPrevious}>
          Prev
        </button>
        <button disabled={!userInvitations.hasNextPage} onClick={userInvitations.fetchNext}>
          Next
        </button>
      </>
    )
  }
  ```


  ```jsx
// Filename: components/UserInvitationsTable.tsx

  import { useOrganizationList } from '@clerk/chrome-extension'

  export function UserInvitationsTable() {
    const { isLoaded, userInvitations } = useOrganizationList({
      userInvitations: {
        infinite: true,
        keepPreviousData: true,
      },
    })

    // Handle loading state
    if (!isLoaded || userInvitations.isLoading) return <div>Loading...</div>

    return (
      <>
        <table>
          <thead>
            <tr>
              <th>Email</th>
              <th>Org name</th>
            </tr>
          </thead>

          <tbody>
            {userInvitations.data?.map((inv) => (
              <tr key={inv.id}>
                <th>{inv.emailAddress}</th>
                <th>{inv.publicOrganizationData.name}</th>
              </tr>
            ))}
          </tbody>
        </table>

        <button disabled={!userInvitations.hasPreviousPage} onClick={userInvitations.fetchPrevious}>
          Prev
        </button>
        <button disabled={!userInvitations.hasNextPage} onClick={userInvitations.fetchNext}>
          Next
        </button>
      </>
    )
  }
  ```


  ```tsx
// Filename: components/UserInvitationsTable.tsx

  import { useOrganizationList } from '@clerk/tanstack-react-start'

  export function UserInvitationsTable() {
    const { isLoaded, userInvitations } = useOrganizationList({
      userInvitations: {
        infinite: true,
        keepPreviousData: true,
      },
    })

    // Handle loading state
    if (!isLoaded || userInvitations.isLoading) return <div>Loading...</div>

    return (
      <>
        <table>
          <thead>
            <tr>
              <th>Email</th>
              <th>Org name</th>
            </tr>
          </thead>

          <tbody>
            {userInvitations.data?.map((inv) => (
              <tr key={inv.id}>
                <th>{inv.emailAddress}</th>
                <th>{inv.publicOrganizationData.name}</th>
              </tr>
            ))}
          </tbody>
        </table>

        <button disabled={!userInvitations.hasPreviousPage} onClick={userInvitations.fetchPrevious}>
          Prev
        </button>
        <button disabled={!userInvitations.hasNextPage} onClick={userInvitations.fetchNext}>
          Next
        </button>
      </>
    )
  }
  ```


  ```tsx
// Filename: components/UserInvitationsTable.tsx

  import { useOrganizationList } from '@clerk/expo'
  import { Text, View, TouchableOpacity, ScrollView } from 'react-native'

  export function UserInvitationsTable() {
    const { isLoaded, userInvitations } = useOrganizationList({
      userInvitations: {
        keepPreviousData: true,
      },
    })

    // Handle loading state
    if (!isLoaded || userInvitations.isLoading) return Loading...

    return (
      
        
          
            Email
            Org name
          

          {userInvitations.data?.map((inv) => (
            
              {inv.emailAddress}
              {inv.publicOrganizationData.name}
            
          ))}
        

        
          Prev
        
        
          Next
        
      
    )
  }
  ```


## Next steps


  - [Build a custom Organization switcher](/guides/development/custom-flows/organizations/organization-switcher)
  - Learn how to build a custom flow for switching between Organizations.

  ---

  - [Create Organizations](/guides/development/custom-flows/organizations/create-organizations)
  - Learn how to build a custom flow for creating Organizations.

  ---

  - [Manage a user's Organization invitations](/guides/development/custom-flows/organizations/manage-user-org-invitations)
  - Learn how to build a custom flow for managing a user's Organization invitations.
