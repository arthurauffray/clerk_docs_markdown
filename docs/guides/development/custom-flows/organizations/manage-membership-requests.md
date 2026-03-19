# Build a custom flow for managing Organization membership requests


> Learn how to use the Clerk API to build a custom flow for managing Organization membership requests.

> [!WARNING]
> This guide is for users who want to build a custom flow. To use a _prebuilt_ UI, use the [Account Portal pages](/guides/account-portal/overview) or [prebuilt components](/reference/components/overview).


This guide will demonstrate how to use the Clerk API to build a custom flow for managing [Organization membership requests](/guides/organizations/add-members/verified-domains#membership-requests).


  
    > [!TIP]
> Examples for this SDK aren't available yet. For now, try adapting the  available example to fit your SDK.

  

  The following example:

  1. Uses the [`useOrganization()`](/reference/hooks/use-organization) hook to get `membershipRequests`, which is a list of the Active Organization's membership requests.
     - `membershipRequests` is an object with `data` that contains an array of [`OrganizationMembershipRequest`](/reference/javascript/types/organization-membership-request) objects.
     - Each `OrganizationMembershipRequest` object has an [`accept()`](/reference/javascript/types/organization-membership-request#accept) and [`reject()`](/reference/javascript/types/organization-membership-request#reject) method to accept or reject the membership request, respectively.
  1. Maps over the `data` array to display the membership requests in a table, providing an "Accept" and "Reject" button for each request that calls the `accept()` and `reject()` methods, respectively.

  
    ```jsx
// Filename: app/components/MembershipRequests.tsx

    'use client'

    import { useOrganization } from '@clerk/nextjs'

    export const MembershipRequestsParams = {
      membershipRequests: {
        pageSize: 5,
        keepPreviousData: true,
      },
    }

    // List of organization membership requests.
    export const MembershipRequests = () => {
      const { isLoaded, membershipRequests } = useOrganization(MembershipRequestsParams)

      if (!isLoaded) {
        return <>Loading</>
      }

      return (
        <>
          <h1>Membership requests</h1>
          <table>
            <thead>
              <tr>
                <th>User</th>
                <th>Date requested</th>
                <th>Actions</th>
              </tr>
            </thead>
            <tbody>
              {membershipRequests?.data?.map((mem) => (
                <tr key={mem.id}>
                  <td>{mem.publicUserData.identifier}</td>
                  <td>{mem.createdAt.toLocaleDateString()}</td>
                  <td>
                    <button
                      onClick={async () => {
                        await mem.accept()
                      }}
                    >
                      Accept
                    </button>
                    <button
                      onClick={async () => {
                        await mem.reject()
                      }}
                    >
                      Reject
                    </button>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>

          <div>
            <button
              disabled={!membershipRequests?.hasPreviousPage || membershipRequests?.isFetching}
              onClick={() => membershipRequests?.fetchPrevious?.()}
            >
              Previous
            </button>

            <button
              disabled={!membershipRequests?.hasNextPage || membershipRequests?.isFetching}
              onClick={() => membershipRequests?.fetchNext?.()}
            >
              Next
            </button>
          </div>
        </>
      )
    }
    ```
  

  
    ```tsx
// Filename: app/components/manage-membership-requests.tsx

    import { ThemedText } from '@/components/themed-text'
    import { ThemedView } from '@/components/themed-view'
    import { useOrganization } from '@clerk/expo'
    import * as React from 'react'
    import { ActivityIndicator, Pressable, ScrollView, StyleSheet, View } from 'react-native'

    export const MembershipRequestsParams = {
      membershipRequests: {
        pageSize: 5,
        keepPreviousData: true,
      },
    }

    // List of organization membership requests.
    export const MembershipRequests = () => {
      const { isLoaded, membershipRequests } = useOrganization(MembershipRequestsParams)

      if (!isLoaded) {
        return (
          
            Loading
          
        )
      }

      return (
        
          
            Membership requests
          
          {membershipRequests?.data && membershipRequests.data.length > 0 ? (
            <>
              
                {membershipRequests?.data?.map((mem) => (
                  
                    User:
                    
                      {mem.publicUserData?.identifier || 'N/A'}
                    

                    Date requested:
                    {mem.createdAt.toLocaleDateString()}

                    
                       [styles.acceptButton, pressed && styles.buttonPressed]}
                        onPress={async () => {
                          await mem.accept()
                        }}
                      >
                        Accept
                      

                       [styles.rejectButton, pressed && styles.buttonPressed]}
                        onPress={async () => {
                          await mem.reject()
                        }}
                      >
                        Reject
                      
                    
                  
                ))}
              

              
                 [
                    styles.paginationButton,
                    (!membershipRequests?.hasPreviousPage || membershipRequests?.isFetching) &&
                      styles.buttonDisabled,
                    pressed && styles.buttonPressed,
                  ]}
                  disabled={!membershipRequests?.hasPreviousPage || membershipRequests?.isFetching}
                  onPress={() => membershipRequests?.fetchPrevious?.()}
                >
                  Previous
                

                 [
                    styles.paginationButton,
                    (!membershipRequests?.hasNextPage || membershipRequests?.isFetching) &&
                      styles.buttonDisabled,
                    pressed && styles.buttonPressed,
                  ]}
                  disabled={!membershipRequests?.hasNextPage || membershipRequests?.isFetching}
                  onPress={() => membershipRequests?.fetchNext?.()}
                >
                  Next
                
              
            </>
          ) : (
            No membership requests
          )}
        
      )
    }

    const styles = StyleSheet.create({
      container: {
        flex: 1,
        padding: 20,
        gap: 12,
      },
      center: {
        flex: 1,
        justifyContent: 'center',
        alignItems: 'center',
        gap: 16,
      },
      title: {
        marginBottom: 20,
      },
      label: {
        fontWeight: '600',
        fontSize: 14,
      },
      value: {
        fontSize: 16,
        marginBottom: 8,
      },
      scrollView: {
        flex: 1,
      },
      card: {
        backgroundColor: 'rgba(128, 128, 128, 0.1)',
        borderRadius: 8,
        padding: 16,
        marginBottom: 12,
        gap: 8,
      },
      buttonRow: {
        flexDirection: 'row',
        gap: 12,
        marginTop: 8,
      },
      acceptButton: {
        flex: 1,
        backgroundColor: '#0a7ea4',
        paddingVertical: 12,
        paddingHorizontal: 24,
        borderRadius: 8,
        alignItems: 'center',
      },
      rejectButton: {
        flex: 1,
        backgroundColor: '#dc3545',
        paddingVertical: 12,
        paddingHorizontal: 24,
        borderRadius: 8,
        alignItems: 'center',
      },
      buttonPressed: {
        opacity: 0.7,
      },
      buttonDisabled: {
        opacity: 0.5,
      },
      buttonText: {
        color: '#fff',
        fontWeight: '600',
      },
      pagination: {
        flexDirection: 'row',
        justifyContent: 'space-between',
        marginTop: 20,
        gap: 12,
      },
      paginationButton: {
        flex: 1,
        backgroundColor: '#0a7ea4',
        paddingVertical: 12,
        paddingHorizontal: 24,
        borderRadius: 8,
        alignItems: 'center',
      },
    })
    ```
  


  The following example:

  1. Calls the [`getMembershipRequests()`](/reference/javascript/organization#get-membership-requests) method to retrieve the list of membership requests for the Active Organization. This method returns `data`, which is an array of [`OrganizationMembershipRequest`](/reference/javascript/types/organization-membership-request) objects.
  1. Maps over the `data` array to display the membership requests in a table.
  1. Provides an "Accept" and "Reject" button for each request that calls the [`accept()`](/reference/javascript/types/organization-membership-request#accept) and [`reject()`](/reference/javascript/types/organization-membership-request#reject) methods, respectively.

  Use the following tabs to view the code necessary for the `index.html` and `main.js` files.

  
**index.html:**

```html
<!-- Filename: index.html -->

    <!doctype html>
    <html lang="en">
      <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>Clerk + JavaScript App</title>
      </head>
      <body>
        <div id="app"></div>

        <h1>Membership Requests</h1>
        <table>
          <thead>
            <tr>
              <th>User</th>
              <th>Date requested</th>
              <th>Accept</th>
              <th>Reject</th>
            </tr>
          </thead>
          <tbody id="requests-table-body"></tbody>
        </table>

        <script type="module" src="/src/main.js" async crossorigin="anonymous"></script>
      </body>
    </html>
    ```


**main.js:**

```js
// Filename: main.js

    import { Clerk } from '@clerk/clerk-js'

    const pubKey = import.meta.env.VITE_CLERK_PUBLISHABLE_KEY

    if (!pubKey) {
      throw new Error('Add your VITE_CLERK_PUBLISHABLE_KEY to .env file')
    }

    const clerk = new Clerk('{{pub_key}}')
    await clerk.load()

    if (clerk.isSignedIn) {
      // Check for an Active Organization
      if (clerk.organization) {
        const requestsTable = document.getElementById('requests-table-body')
        const { data } = await clerk.organization
          .getMembershipRequests()
          .then((res) => console.log(`Membership requests:`, data).catch((err) => console.error(err)))
        const requests = data

        requests.map((request) => {
          const row = requestsTable.insertRow()
          row.insertCell().textContent = request.publicUserData.identifier
          row.insertCell().textContent = request.createdAt.toLocaleDateString()

          // Accept request
          const acceptBtn = document.createElement('button')
          acceptBtn.textContent = 'Accept'
          acceptBtn.addEventListener('click', async function (e) {
            e.preventDefault()
            await request.accept()
          })
          row.insertCell().appendChild(acceptBtn)

          // Reject request
          const rejectBtn = document.createElement('button')
          rejectBtn.textContent = 'Reject'
          rejectBtn.addEventListener('click', async function (e) {
            e.preventDefault()
            await request.reject()
          })
          row.insertCell().appendChild(rejectBtn)
        })
      } else {
        // If there is no Active Organization,
        // mount Clerk's // to allow the user to set an organization as active
        document.getElementById('app').innerHTML = `
          <h2>Select an organization to set it as active</h2>
          <div id="org-switcher"></div>
        `

        const orgSwitcherDiv = document.getElementById('org-switcher')

        clerk.mountOrganizationSwitcher(orgSwitcherDiv)
      }
    } else {
      // If there is no active user, mount Clerk's document.getElementById('app').innerHTML = `
        <div id="sign-in"></div>
      `

      const signInDiv = document.getElementById('sign-in')

      clerk.mountSignIn(signInDiv)
    }
    ```


  ```swift
// Filename: ManageMembershipRequestsView.swift

  import SwiftUI
  import ClerkKit

  struct ManageMembershipRequestsView: View {
    @State private var membershipRequests: [OrganizationMembershipRequest] = []
    let organization: Organization

    var body: some View {
      VStack {
        ForEach(membershipRequests) { request in
          HStack {
            Text(request.publicUserData?.identifier ?? "Unknown user")
            Button("Accept") {
              Task {
                await acceptMembershipRequest(request)
                await fetchMembershipRequests()
              }
            }
            Button("Reject") {
              Task {
                await rejectMembershipRequest(request)
                await fetchMembershipRequests()
              }
            }
          }
        }
      }
      .task { await fetchMembershipRequests() }
    }
  }

  extension ManageMembershipRequestsView {

    func fetchMembershipRequests() async {
      do {
        membershipRequests = try await organization.getMembershipRequests(status: "pending").data
      } catch {
        // See https://clerk.com/docs/guides/development/custom-flows/error-handling
        // for more info on error handling
        dump(error)
        membershipRequests = []
      }
    }

    func acceptMembershipRequest(_ request: OrganizationMembershipRequest) async {
      do {
        try await request.accept()
      } catch {
        // See https://clerk.com/docs/guides/development/custom-flows/error-handling
        // for more info on error handling
        dump(error)
      }
    }

    func rejectMembershipRequest(_ request: OrganizationMembershipRequest) async {
      do {
        try await request.reject()
      } catch {
        // See https://clerk.com/docs/guides/development/custom-flows/error-handling
        // for more info on error handling
        dump(error)
      }
    }
  }
  ```


  ```kotlin
  import com.clerk.api.Clerk
  import com.clerk.api.network.serialization.ClerkResult
  import com.clerk.api.organizations.OrganizationMembershipRequest
  import com.clerk.api.organizations.accept
  import com.clerk.api.organizations.getMembershipRequests
  import com.clerk.api.organizations.reject
  import com.clerk.api.user.getOrganizationMemberships

  suspend fun fetchMembershipRequests(): List {
    val activeOrganizationId = Clerk.session?.lastActiveOrganizationId ?: return emptyList()
    val membershipsResult = Clerk.user?.getOrganizationMemberships() ?: return emptyList()

    if (membershipsResult !is ClerkResult.Success) return emptyList()

    val activeOrganization =
      membershipsResult.value.data.firstOrNull { it.organization.id == activeOrganizationId }?.organization
        ?: return emptyList()

    return when (val requestsResult = activeOrganization.getMembershipRequests(status = "pending")) {
      is ClerkResult.Success -> requestsResult.value.data
      is ClerkResult.Failure -> emptyList()
    }
  }

  suspend fun acceptMembershipRequest(request: OrganizationMembershipRequest) {
    request.accept()
  }

  suspend fun rejectMembershipRequest(request: OrganizationMembershipRequest) {
    request.reject()
  }
  ```
