# create()


> Use Clerk's Backend SDK to create a machine.

Creates a new machine.

```ts
function create(params: CreateMachineParams): Promise
```

## `CreateMachineParams`

- **`name`** `string`

  The name of the machine.

    ---

- **`scopedMachines?`** `string[]`

  Array of machine IDs that this machine will have access to.

    ---

- **`defaultTokenTtl?`** `number`

  The default time-to-live (TTL) in seconds for tokens created by this machine.


## Example

> [!NOTE]
> Using `clerkClient` varies based on your framework. Refer to the [JS Backend SDK overview](/js-backend/getting-started/quickstart) for usage details, including guidance on [how to access the `userId` and other properties](/js-backend/getting-started/quickstart#get-the-user-id-and-other-properties).


### Basic machine creation

```ts
const response = await clerkClient.machines.create({
  name: 'Email Server',
})
```

### Machine with scoped access

```ts
const response = await clerkClient.machines.create({
  name: 'API Gateway',
  scopedMachines: ['mch_123', 'mch_456'],
  defaultTokenTtl: 3600,
})
```

## Backend API (BAPI) endpoint

This method in the SDK is a wrapper around the BAPI endpoint `POST/machines`. See the [BAPI reference](/reference/backend-api/tag/machines/post/machines) for more information.
