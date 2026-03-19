# UserOrganizationInvitation


> The UserOrganizationInvitation object is the model around a user's invitation to an Organization.

The `UserOrganizationInvitation` object is the model around a user's invitation to an Organization.

## Properties

- **`id`** `string`

  The unique identifier for this Organization invitation.

    ---

- **`emailAddress`** `string`

  The email address the invitation has been sent to.

    ---

- **`publicOrganizationData`** `{ hasImage: boolean; imageUrl: string; name: string; id: string; slug: string | null; }`

  The public data of the Organization.

- **`hasImage`: Whether the Organization has an image.** `imageUrl`: Holds the Organization logo. Compatible with Clerk's [Image Optimization](/guides/development/image-optimization). `name`: The name of the Organization. `id`: The ID of the Organization. `slug`: The slug of the Organization.

  ---

- **`publicMetadata`** [`UserOrganizationInvitationPublicMetadata`](/reference/javascript/types/metadata#user-organization-invitation-public-metadata)

  The public metadata of the Organization invitation.

    ---

- **`role`** [`OrganizationCustomRoleKey`](/reference/javascript/types/organization-custom-role-key)

  The [Role](/guides/organizations/control-access/roles-and-permissions) of the current user in the Organization.

    ---

- **`status`** `'pending' | 'accepted' | 'revoked'`

  The status of the invitation.

    ---

- **`createdAt`** `Date`

  The date when the invitation was created.

    ---

- **`updatedAt`** `Date`

  The date when the invitation was last updated.


## Methods

### `accept()`

Accepts the invitation to the Organization.

```typescript
function accept(): Promise
```

### Example

To see an example of how to use the `accept()` method, see the [custom flow guide for managing invitations](/guides/development/custom-flows/organizations/manage-user-org-invitations).
