# create()


> Use Clerk's JS Backend SDK to create a waitlist entry for the given email address.

Creates a [`WaitlistEntry`](/reference/backend/types/backend-waitlist-entry) for the given email address. If the email address is already on the waitlist, no new entry will be created and the existing waitlist entry will be returned.

```ts
function create(params: WaitlistEntryCreateParams): Promise
```

## `WaitlistEntryCreateParams`

- **`emailAddress`** `string`

  The email address to add to the waitlist.

    ---

- **`notify?`** `boolean`

  Whether to send an email notification to the user. Defaults to `false`.


## Example

> [!NOTE]
> Using `clerkClient` varies based on your framework. Refer to the [JS Backend SDK overview](/js-backend/getting-started/quickstart) for usage details, including guidance on [how to access the `userId` and other properties](/js-backend/getting-started/quickstart#get-the-user-id-and-other-properties).


```tsx
const params = {
  emailAddress: 'user2@example.com',
  notify: true,
}

const response = await clerkClient.waitlistEntries.create(params)
```

## Backend API (BAPI) endpoint

This method in the SDK is a wrapper around the BAPI endpoint `POST/waitlist_entries`. See the [BAPI reference](/reference/backend-api/tag/waitlist-entries/post/waitlist_entries) for more information.
