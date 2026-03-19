# useOrganization()


> Access and manage the currently active Organization in your React application with Clerk's useOrganization() hook.

The `useOrganization()` hook retrieves attributes of the currently Active Organization.

## Parameters

`useOrganization()` accepts a single object with the following optional properties:

> [!WARNING]
> By default, the `memberships`, `invitations`, `membershipRequests`, and `domains` attributes aren't populated. To fetch and paginate the data, you must pass `true` or an object with the desired properties.

### Shared properties

Optional properties that are shared across the `invitations`, `membershipRequests`, `memberships`, and `domains` properties.

> [!NOTE]
> These attributes are updating automatically and will re-render their respective components whenever you set a different Organization using the [`setActive({ organization })`](/reference/javascript/clerk#set-active) method or update any of the memberships or invitations. No need for you to manage updating anything manually.

## Returns

### `PaginatedResources`

To see the different Organization features integrated into one application, take a look at our [Organizations demo repository](https://github.com/clerk/organizations-demo).

## Examples

### Expand and paginate attributes

To keep network usage to a minimum, developers are required to opt-in by specifying which resource they need to fetch and paginate through. By default, the `memberships`, `invitations`, `membershipRequests`, and `domains` attributes are not populated. You must pass `true` or an object with the desired [properties](#shared-properties) to fetch and paginate the data.

```jsx
// invitations.data will never be populated.
const { invitations } = useOrganization()

// Use default values to fetch invitations, such as initialPage = 1 and pageSize = 10
const { invitations } = useOrganization({
  invitations: true,
})

// Pass your own values to fetch invitations
const { invitations } = useOrganization({
  invitations: {
    pageSize: 20,
    initialPage: 2, // skips the first page
  },
})

// Aggregate pages in order to render an infinite list
const { invitations } = useOrganization({
  invitations: {
    infinite: true,
  },
})
```

### Infinite pagination

The following example demonstrates how to use the `infinite` property to fetch and append new data to the existing list. The `memberships` attribute will be populated with the first page of the Organization's memberships. When the "Load more" button is clicked, the `fetchNext` helper function will be called to append the next page of memberships to the list.


  ```jsx
// Filename: src/components/MemberList.tsx

  import { useOrganization } from '@clerk/react'

  export default function MemberList() {
    const { memberships } = useOrganization({
      memberships: {
        infinite: true, // Append new data to the existing list
        keepPreviousData: true, // Persist the cached data until the new data has been fetched
      },
    })

    // Handle loading state
    if (!memberships) return <div>Loading...</div>

    return (
      <div>
        <h2>Organization members</h2>
        <ul>
          {memberships.data?.map((membership) => (
            <li key={membership.id}>
              {membership.publicUserData?.firstName} {membership.publicUserData?.lastName} &lt;
              {membership.publicUserData?.identifier}&gt; :: {membership.role}
            </li>
          ))}
        </ul>

        <button
          disabled={!memberships.hasNextPage} // Disable the button if there are no more available pages to be fetched
          onClick={memberships.fetchNext}
        >
          Load more
        </button>
      </div>
    )
  }
  ```


  ```tsx
// Filename: app/organization/members/page.tsx

  'use client'

  import { useOrganization } from '@clerk/nextjs'

  export default function Page() {
    const { memberships } = useOrganization({
      memberships: {
        infinite: true, // Append new data to the existing list
        keepPreviousData: true, // Persist the cached data until the new data has been fetched
      },
    })

    // Handle loading state
    if (!memberships) return <div>Loading...</div>

    return (
      <div>
        <h2>Organization members</h2>
        <ul>
          {memberships.data?.map((membership) => (
            <li key={membership.id}>
              {membership.publicUserData?.firstName} {membership.publicUserData?.lastName} &lt;
              {membership.publicUserData?.identifier}&gt; :: {membership.role}
            </li>
          ))}
        </ul>

        <button
          disabled={!memberships.hasNextPage} // Disable the button if there are no more available pages to be fetched
          onClick={memberships.fetchNext}
        >
          Load more
        </button>
      </div>
    )
  }
  ```


  ```tsx
// Filename: app/routes/members.tsx

  import { useOrganization } from '@clerk/react-router'

  export default function MemberListPage() {
    const { memberships } = useOrganization({
      memberships: {
        infinite: true, // Append new data to the existing list
        keepPreviousData: true, // Persist the cached data until the new data has been fetched
      },
    })

    // Handle loading state
    if (!memberships) return <div>Loading...</div>

    return (
      <div>
        <h2>Organization members</h2>
        <ul>
          {memberships.data?.map((membership) => (
            <li key={membership.id}>
              {membership.publicUserData?.firstName} {membership.publicUserData?.lastName} &lt;
              {membership.publicUserData?.identifier}&gt; :: {membership.role}
            </li>
          ))}
        </ul>

        <button
          disabled={!memberships.hasNextPage} // Disable the button if there are no more available pages to be fetched
          onClick={memberships.fetchNext}
        >
          Load more
        </button>
      </div>
    )
  }
  ```


  ```jsx
// Filename: src/routes/members.tsx

  import { useOrganization } from '@clerk/chrome-extension'

  export default function MemberListPage() {
    const { memberships } = useOrganization({
      memberships: {
        infinite: true, // Append new data to the existing list
        keepPreviousData: true, // Persist the cached data until the new data has been fetched
      },
    })

    // Handle loading state
    if (!memberships) return <div>Loading...</div>

    return (
      <div>
        <h2>Organization members</h2>
        <ul>
          {memberships.data?.map((membership) => (
            <li key={membership.id}>
              {membership.publicUserData?.firstName} {membership.publicUserData?.lastName} &lt;
              {membership.publicUserData?.identifier}&gt; :: {membership.role}
            </li>
          ))}
        </ul>

        <button
          disabled={!memberships.hasNextPage} // Disable the button if there are no more available pages to be fetched
          onClick={memberships.fetchNext}
        >
          Load more
        </button>
      </div>
    )
  }
  ```


  ```tsx
// Filename: app/routes/members.tsx

  import { useOrganization } from '@clerk/tanstack-react-start'
  import { createFileRoute } from '@tanstack/react-router'

  export const Route = createFileRoute('/members')({
    component: MemberListPage,
  })

  export default function MemberListPage() {
    const { memberships } = useOrganization({
      memberships: {
        infinite: true, // Append new data to the existing list
        keepPreviousData: true, // Persist the cached data until the new data has been fetched
      },
    })

    // Handle loading state
    if (!memberships) return <div>Loading...</div>

    return (
      <div>
        <h2>Organization members</h2>
        <ul>
          {memberships.data?.map((membership) => (
            <li key={membership.id}>
              {membership.publicUserData?.firstName} {membership.publicUserData?.lastName} &lt;
              {membership.publicUserData?.identifier}&gt; :: {membership.role}
            </li>
          ))}
        </ul>

        <button
          disabled={!memberships.hasNextPage} // Disable the button if there are no more available pages to be fetched
          onClick={memberships.fetchNext}
        >
          Load more
        </button>
      </div>
    )
  }
  ```


  ```tsx
// Filename: screens/MemberList.tsx

  import { useOrganization } from '@clerk/expo'
  import { Text, View, TouchableOpacity, ScrollView } from 'react-native'

  export function MemberListScreen() {
    const { memberships } = useOrganization({
      memberships: {
        infinite: true, // Append new data to the existing list
        keepPreviousData: true, // Persist the cached data until the new data has been fetched
      },
    })

    // Handle loading state
    if (!memberships) return Loading...

    return (
      
        Organization members
        
          {memberships.data?.map((membership) => (
            
              
                {membership.publicUserData?.firstName} {membership.publicUserData?.lastName} &lt;
                {membership.publicUserData?.identifier}&gt; :: {membership.role}
              
            
          ))}
        

        
          Load more
        
      
    )
  }
  ```


### Simple pagination

The following example demonstrates how to use the `fetchPrevious` and `fetchNext` helper functions to paginate through the data. The `memberships` attribute will be populated with the first page of the Organization's memberships. When the "Previous page" or "Next page" button is clicked, the `fetchPrevious` or `fetchNext` helper function will be called to fetch the previous or next page of memberships.

Notice the difference between this example's pagination and the infinite pagination example above.


  ```jsx
// Filename: src/components/MemberList.tsx

  import { useOrganization } from '@clerk/react'

  export default function MemberList() {
    const { memberships } = useOrganization({
      memberships: {
        keepPreviousData: true, // Persist the cached data until the new data has been fetched
      },
    })

    // Handle loading state
    if (!memberships) return <div>Loading...</div>

    return (
      <div>
        <h2>Organization members</h2>
        <ul>
          {memberships.data?.map((membership) => (
            <li key={membership.id}>
              {membership.publicUserData?.firstName} {membership.publicUserData?.lastName} &lt;
              {membership.publicUserData?.identifier}&gt; :: {membership.role}
            </li>
          ))}
        </ul>

        <button disabled={!memberships.hasPreviousPage} onClick={memberships.fetchPrevious}>
          Previous page
        </button>

        <button disabled={!memberships.hasNextPage} onClick={memberships.fetchNext}>
          Next page
        </button>
      </div>
    )
  }
  ```


  ```tsx
// Filename: app/members/page.tsx

  'use client'

  import { useOrganization } from '@clerk/nextjs'

  export default function Page() {
    const { memberships } = useOrganization({
      memberships: {
        keepPreviousData: true, // Persist the cached data until the new data has been fetched
      },
    })

    // Handle loading state
    if (!memberships) return <div>Loading...</div>

    return (
      <div>
        <h2>Organization members</h2>
        <ul>
          {memberships.data?.map((membership) => (
            <li key={membership.id}>
              {membership.publicUserData?.firstName} {membership.publicUserData?.lastName} &lt;
              {membership.publicUserData?.identifier}&gt; :: {membership.role}
            </li>
          ))}
        </ul>

        <button disabled={!memberships.hasPreviousPage} onClick={memberships.fetchPrevious}>
          Previous page
        </button>

        <button disabled={!memberships.hasNextPage} onClick={memberships.fetchNext}>
          Next page
        </button>
      </div>
    )
  }
  ```


  ```tsx
// Filename: app/routes/members-paginated.tsx

  import { useOrganization } from '@clerk/react-router'

  export default function MemberListPage() {
    const { memberships } = useOrganization({
      memberships: {
        keepPreviousData: true, // Persist the cached data until the new data has been fetched
      },
    })

    // Handle loading state
    if (!memberships) return <div>Loading...</div>

    return (
      <div>
        <h2>Organization members</h2>
        <ul>
          {memberships.data?.map((membership) => (
            <li key={membership.id}>
              {membership.publicUserData?.firstName} {membership.publicUserData?.lastName} &lt;
              {membership.publicUserData?.identifier}&gt; :: {membership.role}
            </li>
          ))}
        </ul>

        <button disabled={!memberships.hasPreviousPage} onClick={memberships.fetchPrevious}>
          Previous page
        </button>

        <button disabled={!memberships.hasNextPage} onClick={memberships.fetchNext}>
          Next page
        </button>
      </div>
    )
  }
  ```


  ```jsx
// Filename: src/routes/members-paginated.tsx

  import { useOrganization } from '@clerk/chrome-extension'

  export default function MemberListPage() {
    const { memberships } = useOrganization({
      memberships: {
        keepPreviousData: true, // Persist the cached data until the new data has been fetched
      },
    })

    // Handle loading state
    if (!memberships) return <div>Loading...</div>

    return (
      <div>
        <h2>Organization members</h2>
        <ul>
          {memberships.data?.map((membership) => (
            <li key={membership.id}>
              {membership.publicUserData?.firstName} {membership.publicUserData?.lastName} &lt;
              {membership.publicUserData?.identifier}&gt; :: {membership.role}
            </li>
          ))}
        </ul>

        <button disabled={!memberships.hasPreviousPage} onClick={memberships.fetchPrevious}>
          Previous page
        </button>

        <button disabled={!memberships.hasNextPage} onClick={memberships.fetchNext}>
          Next page
        </button>
      </div>
    )
  }
  ```


  ```tsx
// Filename: app/routes/members-paginated.tsx

  import { useOrganization } from '@clerk/tanstack-react-start'
  import { createFileRoute } from '@tanstack/react-router'

  export const Route = createFileRoute('/members-paginated')({
    component: MemberListPage,
  })

  export default function MemberListPage() {
    const { memberships } = useOrganization({
      memberships: {
        keepPreviousData: true, // Persist the cached data until the new data has been fetched
      },
    })

    // Handle loading state
    if (!memberships) return <div>Loading...</div>

    return (
      <div>
        <h2>Organization members</h2>
        <ul>
          {memberships.data?.map((membership) => (
            <li key={membership.id}>
              {membership.publicUserData?.firstName} {membership.publicUserData?.lastName} &lt;
              {membership.publicUserData?.identifier}&gt; :: {membership.role}
            </li>
          ))}
        </ul>

        <button disabled={!memberships.hasPreviousPage} onClick={memberships.fetchPrevious}>
          Previous page
        </button>

        <button disabled={!memberships.hasNextPage} onClick={memberships.fetchNext}>
          Next page
        </button>
      </div>
    )
  }
  ```


  ```tsx
// Filename: screens/MemberList.tsx

  import { useOrganization } from '@clerk/expo'
  import { Text, View, TouchableOpacity, ScrollView } from 'react-native'

  export function MemberListScreen() {
    const { memberships } = useOrganization({
      memberships: {
        keepPreviousData: true, // Persist the cached data until the new data has been fetched
      },
    })

    // Handle loading state
    if (!memberships) return Loading...

    return (
      
        Organization members
        
          {memberships.data?.map((membership) => (
            
              
                {membership.publicUserData?.firstName} {membership.publicUserData?.lastName} &lt;
                {membership.publicUserData?.identifier}&gt; :: {membership.role}
              
            
          ))}
        

        
          Previous page
        

        
          Next page
        
      
    )
  }
  ```


## Next steps


  - [Update an Organization](/guides/development/custom-flows/organizations/update-organizations)
  - Learn how to build a custom flow for updating an Organization.

  ---

  - [Manage Roles in an Organization](/guides/development/custom-flows/organizations/manage-roles)
  - Learn how to build a custom flow for managing Roles in an Organization.

  ---

  - [Manage an Organization's membership requests](/guides/development/custom-flows/organizations/manage-membership-requests)
  - Learn how to build a custom flow for managing an Organization's membership requests.

  ---

  - [Manage a user's Organization invitations](/guides/development/custom-flows/organizations/manage-user-org-invitations)
  - Learn how to build a custom flow for managing a user's Organization invitations.
