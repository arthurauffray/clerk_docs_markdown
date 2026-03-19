# invite()


> Use Clerk's JS Backend SDK to invite a waitlist entry by ID.

Invites a waitlist entry by ID. Returns a [`WaitlistEntry`](/reference/backend/types/backend-waitlist-entry) representing the invited entry.

```ts
function invite(id: string, params: WaitlistEntryInviteParams): Promise
```

## Parameters

`invite()` accepts the following parameters:

- **`id`** `string`

  The ID of the waitlist entry to invite.

    ---

- **`params`** [`WaitlistEntryInviteParams`](#waitlist-entry-invite-params)

  An object representing additional parameters for the invitation.


## `WaitlistEntryInviteParams`

- **`ignoreExisting?`** `boolean`

  Whether an invitation should be created if there is already an existing invitation for this email address, or has been claimed by another user. Defaults to `false`.


## Example

> [!NOTE]
> Using `clerkClient` varies based on your framework. Refer to the [JS Backend SDK overview](/js-backend/getting-started/quickstart) for usage details, including guidance on [how to access the `userId` and other properties](/js-backend/getting-started/quickstart#get-the-user-id-and-other-properties).


```tsx
const waitlistId = 'waitlist_123'

const response = await clerkClient.waitlistEntries.invite(waitlistId)
```

## Backend API (BAPI) endpoint

This method in the SDK is a wrapper around the BAPI endpoint `POST/waitlist_entries/{waitlist_entry_id}/invite`. See the [BAPI reference](/reference/backend-api/tag/waitlist_entries/post/waitlist_entries/\{waitlist_entry_id}/invite) for more information.
