# delete()


> Use Clerk's JS Backend SDK to delete a pending waitlist entry by ID.

Deletes a pending waitlist entry by ID. Returns a [`DeletedObjectResource`](/reference/javascript/types/deleted-object-resource).

```ts

function delete(
  id: string,
): Promise
```

## Parameters

- **`id`** `string`

  The ID of the waitlist entry to delete.


## Example

> [!NOTE]
> Using `clerkClient` varies based on your framework. Refer to the [JS Backend SDK overview](/js-backend/getting-started/quickstart) for usage details, including guidance on [how to access the `userId` and other properties](/js-backend/getting-started/quickstart#get-the-user-id-and-other-properties).


```tsx
const waitlistId = 'waitlist_123'

const response = await clerkClient.waitlistEntries.delete(waitlistId)
```

## Backend API (BAPI) endpoint

This method in the SDK is a wrapper around the BAPI endpoint `DELETE/waitlist_entries/{waitlist_entry_id}`. See the [BAPI reference](/reference/backend-api/tag/waitlist_entries/delete/waitlist_entries/\{waitlist_entry_id}) for more information.
