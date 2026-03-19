# Waitlist


> The Waitlist object holds the state of a waitlist entry and provides methods to join the waitlist.

The `Waitlist` object provides methods and properties to manage waitlist entries in your application. It's useful for building a custom flow instead of using the prebuilt [``](/reference/components/authentication/waitlist) component.

## Properties

- **`id`** `string | undefined`

  The unique identifier for the waitlist entry. `undefined` if the user has not joined the waitlist yet.

    ---

- **`createdAt`** `Date | null`

  The date and time the waitlist entry was created. `null` if the user has not joined the waitlist yet.

    ---

- **`updatedAt`** `Date | null`

  The date and time the waitlist entry was last updated. `null` if the user has not joined the waitlist yet.


## Methods

### `join()`

Submits an email address to join the waitlist. This method creates a new waitlist entry for the provided email address.

```ts
function join(params: JoinWaitlistParams): Promise<{ error: unknown }>
```

#### `JoinWaitlistParams`

- **`emailAddress`** `string`

  The email address to add to the waitlist.


#### Example

```js
await clerk.waitlist.join({ emailAddress: 'test@example.com' })
```
