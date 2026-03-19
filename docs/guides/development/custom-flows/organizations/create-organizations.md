# Build a custom flow for creating Organizations


> Learn how to use the Clerk API to build a custom flow for creating Organizations.

> [!WARNING]
> This guide is for users who want to build a custom flow. To use a _prebuilt_ UI, use the [Account Portal pages](/guides/account-portal/overview) or [prebuilt components](/reference/components/overview).


This guide demonstrates how to use Clerk's API to build a custom flow for creating Organizations.


  The following example uses these hooks:

  - The [`useOrganizationList()`](/reference/hooks/use-organization-list) hook to access the `createOrganization()` method. This method is used to create a new Organization with the provided name.
  - The [`useOrganizationCreationDefaults()`](/reference/hooks/use-organization-creation-defaults) hook to pre-populate the form with a suggested organization name based on your application's [default naming rules](/guides/organizations/configure#default-naming-rules), and to display a warning if an organization with that name or domain already exists.

  
  ```tsx
// Filename: src/components/CreateOrganizationWithWarning.tsx

  import { useOrganizationCreationDefaults, useOrganizationList } from '@clerk/react'
  import { FormEventHandler, useEffect, useState } from 'react'

  export default function CreateOrganizationWithWarning() {
    const { isLoaded, createOrganization } = useOrganizationList()
    const { data: defaults, isLoading } = useOrganizationCreationDefaults()
    const [organizationName, setOrganizationName] = useState('')

    useEffect(() => {
      if (defaults?.form.name) {
        setOrganizationName(defaults.form.name)
      }
    }, [defaults?.form.name])

    if (!isLoaded || isLoading) return <div>Loading...</div>

    // Check if an organization with this name/domain already exists
    const advisory = defaults?.advisory
    const showWarning = advisory?.code === 'organization_already_exists'
    const existingOrgName = advisory?.meta?.organization_name
    const existingOrgDomain = advisory?.meta?.organization_domain

    const handleSubmit: FormEventHandler = async (e) => {
      e.preventDefault()
      try {
        await createOrganization?.({ name: organizationName })
      } catch (err) {
        // See https://clerk.com/docs/guides/development/custom-flows/error-handling
        // for more info on error handling
        console.error(JSON.stringify(err, null, 2))
      }
    }

    return (
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          value={organizationName}
          onChange={(e) => setOrganizationName(e.target.value)}
          placeholder="Organization name"
        />
        {showWarning && (
          <p style={{ color: 'orange' }}>
            An organization "{existingOrgName}" already exists for the domain "{existingOrgDomain}".
          </p>
        )}
        <button type="submit">Create organization</button>
      </form>
    )
  }
  ```


  ```tsx
// Filename: app/components/CreateOrganizationWithWarning.tsx

  import { useOrganizationCreationDefaults, useOrganizationList } from '@clerk/react-router'
  import { FormEventHandler, useEffect, useState } from 'react'

  export default function CreateOrganizationWithWarning() {
    const { isLoaded, createOrganization, setActive } = useOrganizationList()
    const { data: defaults, isLoading } = useOrganizationCreationDefaults()
    const [organizationName, setOrganizationName] = useState('')

    useEffect(() => {
      if (defaults?.form.name) {
        setOrganizationName(defaults.form.name)
      }
    }, [defaults?.form.name])

    if (!isLoaded || isLoading) return <div>Loading...</div>

    // Check if an organization with this name/domain already exists
    const advisory = defaults?.advisory
    const showWarning = advisory?.code === 'organization_already_exists'
    const existingOrgName = advisory?.meta?.organization_name
    const existingOrgDomain = advisory?.meta?.organization_domain

    const handleSubmit: FormEventHandler = async (e) => {
      e.preventDefault()
      try {
        const newOrganization = await createOrganization?.({ name: organizationName })
        // Set the created Organization as the Active Organization
        if (newOrganization) setActive({ organization: newOrganization.id })
      } catch (err) {
        // See https://clerk.com/docs/guides/development/custom-flows/error-handling
        // for more info on error handling
        console.error(JSON.stringify(err, null, 2))
      }
    }

    return (
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          value={organizationName}
          onChange={(e) => setOrganizationName(e.target.value)}
          placeholder="Organization name"
        />
        {showWarning && (
          <p style={{ color: 'orange' }}>
            An organization "{existingOrgName}" already exists for the domain "{existingOrgDomain}".
          </p>
        )}
        <button type="submit">Create organization</button>
      </form>
    )
  }
  ```


  ```tsx
// Filename: src/components/CreateOrganizationWithWarning.tsx

  import { useOrganizationCreationDefaults, useOrganizationList } from '@clerk/chrome-extension'
  import { FormEventHandler, useEffect, useState } from 'react'

  export default function CreateOrganizationWithWarning() {
    const { isLoaded, createOrganization, setActive } = useOrganizationList()
    const { data: defaults, isLoading } = useOrganizationCreationDefaults()
    const [organizationName, setOrganizationName] = useState('')

    useEffect(() => {
      if (defaults?.form.name) {
        setOrganizationName(defaults.form.name)
      }
    }, [defaults?.form.name])

    if (!isLoaded || isLoading) return <div>Loading...</div>

    // Check if an organization with this name/domain already exists
    const advisory = defaults?.advisory
    const showWarning = advisory?.code === 'organization_already_exists'
    const existingOrgName = advisory?.meta?.organization_name
    const existingOrgDomain = advisory?.meta?.organization_domain

    const handleSubmit: FormEventHandler = async (e) => {
      e.preventDefault()
      try {
        const newOrganization = await createOrganization?.({ name: organizationName })
        // Set the created Organization as the Active Organization
        if (newOrganization) setActive({ organization: newOrganization.id })
      } catch (err) {
        // See https://clerk.com/docs/guides/development/custom-flows/error-handling
        // for more info on error handling
        console.error(JSON.stringify(err, null, 2))
      }
    }

    return (
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          value={organizationName}
          onChange={(e) => setOrganizationName(e.target.value)}
          placeholder="Organization name"
        />
        {showWarning && (
          <p style={{ color: 'orange' }}>
            An organization "{existingOrgName}" already exists for the domain "{existingOrgDomain}".
          </p>
        )}
        <button type="submit">Create organization</button>
      </form>
    )
  }
  ```


  ```tsx
// Filename: app/components/CreateOrganizationWithWarning.tsx

  import { useOrganizationCreationDefaults, useOrganizationList } from '@clerk/tanstack-react-start'
  import { FormEventHandler, useEffect, useState } from 'react'

  export default function CreateOrganizationWithWarning() {
    const { isLoaded, createOrganization, setActive } = useOrganizationList()
    const { data: defaults, isLoading } = useOrganizationCreationDefaults()
    const [organizationName, setOrganizationName] = useState('')

    useEffect(() => {
      if (defaults?.form.name) {
        setOrganizationName(defaults.form.name)
      }
    }, [defaults?.form.name])

    if (!isLoaded || isLoading) return <div>Loading...</div>

    // Check if an organization with this name/domain already exists
    const advisory = defaults?.advisory
    const showWarning = advisory?.code === 'organization_already_exists'
    const existingOrgName = advisory?.meta?.organization_name
    const existingOrgDomain = advisory?.meta?.organization_domain

    const handleSubmit: FormEventHandler = async (e) => {
      e.preventDefault()
      try {
        const newOrganization = await createOrganization?.({ name: organizationName })
        // Set the created Organization as the Active Organization
        if (newOrganization) setActive({ organization: newOrganization.id })
      } catch (err) {
        // See https://clerk.com/docs/guides/development/custom-flows/error-handling
        // for more info on error handling
        console.error(JSON.stringify(err, null, 2))
      }
    }

    return (
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          value={organizationName}
          onChange={(e) => setOrganizationName(e.target.value)}
          placeholder="Organization name"
        />
        {showWarning && (
          <p style={{ color: 'orange' }}>
            An organization "{existingOrgName}" already exists for the domain "{existingOrgDomain}".
          </p>
        )}
        <button type="submit">Create organization</button>
      </form>
    )
  }
  ```


  ```tsx
// Filename: components/CreateOrganizationWithWarning.tsx

  import { ThemedText } from '@/components/themed-text'
  import { ThemedView } from '@/components/themed-view'
  import { useOrganizationCreationDefaults, useOrganizationList } from '@clerk/expo'
  import { useEffect, useState } from 'react'
  import { Pressable, StyleSheet, TextInput } from 'react-native'

  export default function CreateOrganizationWithWarning() {
    const { isLoaded, createOrganization, setActive } = useOrganizationList()
    const { data: defaults, isLoading } = useOrganizationCreationDefaults()
    const [organizationName, setOrganizationName] = useState('')

    useEffect(() => {
      if (defaults?.form.name) {
        setOrganizationName(defaults.form.name)
      }
    }, [defaults?.form.name])

    if (!isLoaded || isLoading) {
      return (
        
          Loading...
        
      )
    }

    // Check if an organization with this name/domain already exists
    const advisory = defaults?.advisory
    const showWarning = advisory?.code === 'organization_already_exists'
    const existingOrgName = advisory?.meta?.organization_name
    const existingOrgDomain = advisory?.meta?.organization_domain

    const handleSubmit = async () => {
      try {
        const newOrganization = await createOrganization?.({ name: organizationName })
        // Set the created Organization as the Active Organization
        if (newOrganization) setActive({ organization: newOrganization.id })
      } catch (err) {
        // See https://clerk.com/docs/guides/development/custom-flows/error-handling
        // for more info on error handling
        console.error(JSON.stringify(err, null, 2))
      }
    }

    return (
      
        Organization name
        {showWarning && (
          
            An organization "{existingOrgName}" already exists for the domain "{existingOrgDomain}".
          
        )}
         [
            styles.button,
            !organizationName && styles.buttonDisabled,
            pressed && styles.buttonPressed,
          ]}
          onPress={handleSubmit}
          disabled={!organizationName}
        >
          Create organization
        
      
    )
  }

  const styles = StyleSheet.create({
    container: {
      gap: 12,
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
    buttonDisabled: {
      opacity: 0.5,
    },
    buttonText: {
      color: '#fff',
      fontWeight: '600',
    },
    warning: {
      color: '#f57c00',
      fontSize: 14,
      marginTop: -4,
    },
  })
  ```


  ```tsx
// Filename: app/components/CreateOrganization.tsx

  'use client'

  import { useOrganizationCreationDefaults, useOrganizationList } from '@clerk/nextjs'
  import { FormEventHandler, useEffect, useState } from 'react'

  export default function CreateOrganization() {
    const { isLoaded, createOrganization, setActive } = useOrganizationList()
    const { data: defaults, isLoading: isLoadingDefaults } = useOrganizationCreationDefaults()
    const [organizationName, setOrganizationName] = useState('')

    // Pre-populate the form with suggested organization name
    useEffect(() => {
      if (defaults?.form.name) {
        setOrganizationName(defaults.form.name)
      }
    }, [defaults?.form.name])

    if (!isLoaded || isLoadingDefaults) return <p>Loading...</p>

    // Check if an organization with this name/domain already exists
    const advisory = defaults?.advisory
    const showWarning = advisory?.code === 'organization_already_exists'
    const existingOrgName = advisory?.meta?.organization_name
    const existingOrgDomain = advisory?.meta?.organization_domain

    const handleSubmit: FormEventHandler = async (e) => {
      e.preventDefault()
      try {
        const newOrganization = await createOrganization?.({ name: organizationName })
        // Set the created Organization as the Active Organization
        if (newOrganization) setActive({ organization: newOrganization.id })
      } catch (err) {
        // See https://clerk.com/docs/guides/development/custom-flows/error-handling
        // for more info on error handling
        console.error(JSON.stringify(err, null, 2))
      }
      setOrganizationName('')
    }

    return (
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          value={organizationName}
          onChange={(e) => setOrganizationName(e.currentTarget.value)}
          placeholder="Organization name"
        />
        {showWarning && (
          <p style={{ color: 'orange' }}>
            An organization "{existingOrgName}" already exists for the domain "{existingOrgDomain}".
          </p>
        )}
        <button type="submit">Create organization</button>
      </form>
    )
  }
  ```


  The following example uses the [`clerk.createOrganization()`](/reference/javascript/clerk#create-organization) method to create a new Organization with the provided name.

  Use the tabs to view the code necessary for the `index.html` and `main.js` files.

  
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

        <h1>Create an organization</h1>
        <form id="create-organization">
          <label for="name">Name</label>
          <input id="name" name="name" />
          <button>Create organization</button>
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

    const clerk = new Clerk(pubKey)
    await clerk.load()

    if (clerk.isSignedIn) {
      const form = document.getElementById('create-organization')

      form.addEventListener('submit', async (e) => {
        e.preventDefault()

        const inputEl = document.getElementById('name')

        if (!inputEl) {
          // ... handle empty input
          return
        }

        try {
          await clerk.createOrganization({ name: inputEl.value })
          if (newOrganization) clerk.setActive({ organization: newOrganization.id })
        } catch (error) {
          console.log('An error occurred:', error)
        }
      })
    } else {
      // If there is no active user, mount Clerk's document.getElementById('app').innerHTML = `
        <div id="sign-in"></div>
      `

      const signInDiv = document.getElementById('sign-in')

      clerk.mountSignIn(signInDiv)
    }
    ```


  ```swift
// Filename: OrganizationView.swift

  import ClerkKit
  import SwiftUI

  struct OrganizationView: View {
    @Environment(Clerk.self) private var clerk
    @State private var organizationName = ""
    @State private var createdOrganization: Organization?

    var body: some View {
      VStack(alignment: .leading, spacing: 16) {
        HStack(spacing: 10) {
          TextField("Organization name", text: $organizationName)
            .textFieldStyle(.roundedBorder)

          Button("Submit") {
            Task { await createOrganization() }
          }
        }

        if let createdOrganization = createdOrganization {
          Text("Successfully Created: \(createdOrganization.name)")
        }
      }
      .padding()
    }

    @MainActor
    private func createOrganization() async {
      guard let user = clerk.user else { return }

      do {
        createdOrganization = try await user.createOrganization(name: organizationName)
        organizationName = ""
      } catch {
        dump(error)
      }
    }
  }
  ```


  ```kotlin
// Filename: OrganizationView.kt

  import androidx.compose.foundation.layout.Arrangement
  import androidx.compose.foundation.layout.Column
  import androidx.compose.foundation.layout.Row
  import androidx.compose.foundation.layout.fillMaxWidth
  import androidx.compose.foundation.layout.padding
  import androidx.compose.material3.Button
  import androidx.compose.material3.OutlinedTextField
  import androidx.compose.material3.Text
  import androidx.compose.runtime.Composable
  import androidx.compose.runtime.getValue
  import androidx.compose.runtime.mutableStateOf
  import androidx.compose.runtime.remember
  import androidx.compose.runtime.rememberCoroutineScope
  import androidx.compose.runtime.setValue
  import androidx.compose.ui.Alignment
  import androidx.compose.ui.Modifier
  import androidx.compose.ui.unit.dp
  import com.clerk.api.Clerk
  import com.clerk.api.network.serialization.onFailure
  import com.clerk.api.network.serialization.onSuccess
  import com.clerk.api.organizations.Organization
  import kotlinx.coroutines.launch

  @Composable
  fun OrganizationView() {
    var organizationName by remember { mutableStateOf("") }
    var createdOrganization by remember { mutableStateOf(null) }
    val coroutineScope = rememberCoroutineScope()

    Column(
      modifier = Modifier.padding(16.dp),
      verticalArrangement = Arrangement.spacedBy(16.dp),
    ) {
      Row(
        modifier = Modifier.fillMaxWidth(),
        horizontalArrangement = Arrangement.spacedBy(10.dp),
        verticalAlignment = Alignment.CenterVertically,
      ) {
        OutlinedTextField(
          modifier = Modifier.weight(1f),
          value = organizationName,
          onValueChange = { organizationName = it },
          label = { Text("Organization name") },
        )

        Button(
          onClick = {
            coroutineScope.launch {
              val organization = createOrganization(organizationName) ?: return@launch
              createdOrganization = organization
              organizationName = ""
            }
          },
        ) {
          Text("Submit")
        }
      }

      createdOrganization?.let { organization ->
        Text("Successfully Created: ${organization.name}")
      }
    }
  }

  private suspend fun createOrganization(organizationName: String): Organization? {
    if (Clerk.user == null) return null

    var createdOrganization: Organization? = null
    Organization.create(name = organizationName)
      .onSuccess { organization ->
        createdOrganization = organization
      }
      .onFailure {
        // See https://clerk.com/docs/guides/development/custom-flows/error-handling
        // for more info on error handling
      }

    return createdOrganization
  }
  ```
