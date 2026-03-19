# createSamlConnection()


> Use Clerk's JS Backend SDK to create a SAML connection.

Creates a new [`SamlConnection`](/reference/backend/types/backend-saml-connection).

```ts
function createSamlConnection(params: CreateSamlConnectionParams): Promise
```

## `CreateSamlConnectionParams`

- **`name`** `string`

  The name to use as a label for this SAML Connection.

    ---

- **`provider`** `'saml_custom' | 'saml_okta' | 'saml_google' | 'saml_microsoft'`

  The Identity Provider (IdP) provider of the connection.

    ---

- **`domain`** `string`

  The domain of your Organization. Sign in flows using an email with this domain will use this SAML Connection. For example: `'clerk.dev'`

    ---

- **`organizationId?`** `string`

  The ID of the Organization to which users of this SAML Connection will be added

    ---

- **`idpEntityId?`** `string`

  The Entity ID as provided by the Identity Provider (IdP).

    ---

- **`idpSsoUrl?`** `string`

  The Single-Sign On URL as provided by the Identity Provider (IdP).

    ---

- **`idpCertificate?`** `string`

  The X.509 certificate as provided by the Identity Provider (IdP).

    ---

- **`idpMetadataUrl?`** `string`

  The URL which serves the Identity Provider (IdP) metadata. If present, it takes priority over the corresponding individual properties.

    ---

- **`idpMetadata?`** `string`

  The XML content of the Identity Provider (IdP) metadata file. If present, it takes priority over the corresponding individual properties.

    ---

- **`attributeMapping?`** `{ emailAddress?: string, firstName?: string, lastName?: string, userId?: string }`

  The attribute mapping for the SAML connection.


## Example

> [!NOTE]
> Using `clerkClient` varies based on your framework. Refer to the [JS Backend SDK overview](/js-backend/getting-started/quickstart) for usage details, including guidance on [how to access the `userId` and other properties](/js-backend/getting-started/quickstart#get-the-user-id-and-other-properties).


```tsx
const response = await clerkClient.samlConnections.createSamlConnection({
  name: 'test-okta',
  provider: 'saml_okta',
  domain: 'clerk.dev',
  idpMetadataUrl: 'https://trial-000000.okta.com/app/exk...',
  attributeMapping: {
    emailAddress: 'user.email',
    firstName: 'user.firstName',
    lastName: 'user.lastName',
  },
})
```

## Backend API (BAPI) endpoint

This method in the SDK is a wrapper around the BAPI endpoint `POST/saml_connections`. See the [BAPI reference](/reference/backend-api/tag/saml-connections/post/saml_connections) for more information.
