# reject()


> Use Clerk's JS Backend SDK to reject a waitlist entry by ID.

Rejects a waitlist entry by ID. Returns a [`WaitlistEntry`](/reference/backend/types/backend-waitlist-entry) representing the rejected entry.

```ts
function reject(id: string): Promise
```

## Parameters

- **`id`** `string`

  The ID of the waitlist entry to reject.


## Example

> [!NOTE]
> Using `clerkClient` varies based on your framework. Refer to the [JS Backend SDK overview](/js-backend/getting-started/quickstart) for usage details, including guidance on [how to access the `userId` and other properties](/js-backend/getting-started/quickstart#get-the-user-id-and-other-properties).


```tsx
const waitlistId = 'waitlist_123'

const response = await clerkClient.waitlistEntries.reject(waitlistId)
```

## Backend API (BAPI) endpoint

This method in the SDK is a wrapper around the BAPI endpoint `POST/waitlist_entries/{waitlist_entry_id}/reject`. See the [BAPI reference](/reference/backend-api/tag/waitlist_entries/post/waitlist_entries/\{waitlist_entry_id}/reject) for more information.
