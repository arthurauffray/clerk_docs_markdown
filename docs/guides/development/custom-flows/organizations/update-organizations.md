# Build a custom flow for updating an Organization


> Learn how to use the Clerk API to build a custom flow for updating an Organization in your application.

> [!WARNING]
> This guide is for users who want to build a custom flow. To use a _prebuilt_ UI, use the [Account Portal pages](/guides/account-portal/overview) or [prebuilt components](/reference/components/overview).


Organization members with appropriate [Permissions](/guides/organizations/control-access/roles-and-permissions) can update an Organization.

This guide will demonstrate how to use Clerk's API to build a custom flow for updating an Organization.


  The following example:

  1. Uses the [`useOrganization()`](/reference/hooks/use-organization) hook to fetch the active `organization`.
  1. Uses `organization` to call the `update()` method with the desired name to update the Organization. To see what other attributes can be updated, see the [`update()` reference doc](/reference/javascript/organization#update).

  
    
      > [!TIP]
> Examples for this SDK aren't available yet. For now, try adapting the  available example to fit your SDK.

    

    ```tsx
// Filename: app/components/UpdateOrganization.tsx

    'use client'

    import { useState, useEffect } from 'react'
    import { useRouter } from 'next/navigation'
    import { useOrganization } from '@clerk/nextjs'

    export default function UpdateOrganization() {
      const [name, setName] = useState('')
      const router = useRouter()
      const { organization } = useOrganization()

      useEffect(() => {
        if (!organization) {
          return
        }
        setName(organization.name)
      }, [organization])

      if (!organization) {
        return null
      }

      async function submit(e: React.FormEvent) {
        e.preventDefault()
        try {
          await organization?.update({ name })
          router.push(`/organizations/${organization?.id}`)
        } catch (err) {
          console.error(err)
        }
      }

      return (
        <div>
          <h1>Update the current organization</h1>
          <form onSubmit={submit}>
            <div>
              <label htmlFor="name">Name</label>
              <input id="name" name="name" value={name} onChange={(e) => setName(e.target.value)} />
            </div>
            <button>Update</button>
          </form>
        </div>
      )
    }
    ```
  

  
    ```tsx
// Filename: app/components/update-organization.tsx

    import { ThemedText } from '@/components/themed-text'
    import { ThemedView } from '@/components/themed-view'
    import { useOrganization } from '@clerk/expo'
    import * as React from 'react'
    import { Pressable, StyleSheet, TextInput } from 'react-native'

    export const UpdateOrganization = () => {
      const { organization, isLoaded } = useOrganization()

      const [name, setName] = React.useState('')
      const [success, setSuccess] = React.useState(false)

      React.useEffect(() => {
        if (!organization) {
          return
        }
        setName(organization.name)
      }, [organization])

      if (!isLoaded || !organization) {
        return null
      }

      const handleSubmit = async () => {
        try {
          setSuccess(false)
          await organization?.update({ name })
          setSuccess(true)
        } catch (err) {
          console.error(err)
        }
      }

      return (
        
          
            Update the current organization
          
          Name
           setName(text)}
          />
           [styles.button, pressed && styles.buttonPressed]}
            onPress={handleSubmit}
            disabled={!name.trim()}
          >
            Update
          
          {success && Organization updated successfully}
        
      )
    }

    const styles = StyleSheet.create({
      container: {
        gap: 12,
      },
      title: {
        marginBottom: 8,
      },
      label: {
        fontWeight: '600',
        fontSize: 14,
      },
      input: {
        borderWidth: 1,
        borderColor: '#ccc',
        borderRadius: 8,
        padding: 12,
        fontSize: 16,
        backgroundColor: '#fff',
      },
      button: {
        backgroundColor: '#0a7ea4',
        paddingVertical: 12,
        paddingHorizontal: 24,
        borderRadius: 8,
        alignItems: 'center',
        marginTop: 8,
      },
      buttonPressed: {
        opacity: 0.7,
      },
      buttonText: {
        color: '#fff',
        fontWeight: '600',
      },
      success: {
        color: '#28a745',
        fontSize: 14,
        marginTop: 12,
        fontWeight: '600',
      },
    })
    ```
  


  The following example uses the `organization.update()` method to update the Active Organization's name. To see what other attributes can be updated, see the [`update()` reference doc](/reference/javascript/organization#update).

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

        <h1>Update the current organization</h1>
        <form id="update-organization">
          <label for="name">Name</label>
          <input id="name" name="name" />
          <button>Update</button>
        </form>

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
        const form = document.getElementById('update-organization')

        form.addEventListener('submit', function (e) {
          e.preventDefault()

          const inputEl = document.getElementById('name')

          if (!inputEl) {
            // ... handle empty input
            return
          }

          clerk.organization
            .update({ name: inputEl.value })
            .then((res) => console.log(`Updated org:`, res))
            .catch((error) => console.log('An error occurred:', error))
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
// Filename: UpdateOrganizationView.swift

  import SwiftUI
  import ClerkKit

  struct UpdateOrganizationView: View {
    @State private var name: String
    let organization: Organization

    init(organization: Organization) {
      self.organization = organization
      _name = State(initialValue: organization.name)
    }

    var body: some View {
      VStack {
        TextField("Enter organization name", text: $name)
        Button("Update organization") {
          Task { await updateOrganization(name: name) }
        }
      }
    }
  }

  extension UpdateOrganizationView {

    func updateOrganization(name: String) async {
      do {
        try await organization.update(name: name)
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
  import com.clerk.api.organizations.update
  import com.clerk.api.user.getOrganizationMemberships

  suspend fun updateActiveOrganization(name: String) {
    val activeOrganizationId = Clerk.session?.lastActiveOrganizationId ?: return
    val membershipsResult = Clerk.user?.getOrganizationMemberships() ?: return

    if (membershipsResult !is ClerkResult.Success) return

    val activeOrganization =
      membershipsResult.value.data.firstOrNull { it.organization.id == activeOrganizationId }?.organization
        ?: return

    activeOrganization.update(name = name)
  }
  ```
