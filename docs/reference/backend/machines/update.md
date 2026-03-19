# update()


> Use Clerk's Backend SDK to update a machine.

Updates a machine by its ID.

```ts
function update(params: UpdateMachineParams): Promise
```

## `UpdateMachineParams`

- **`machineId`** `string`

  The ID of the machine to update.

    ---

- **`name?`** `string`

  The name of the machine.

    ---

- **`defaultTokenTtl?`** `number`

  The default time-to-live (TTL) in seconds for tokens created by this machine.


## Example

> [!NOTE]
> Using `clerkClient` varies based on your framework. Refer to the [JS Backend SDK overview](/js-backend/getting-started/quickstart) for usage details, including guidance on [how to access the `userId` and other properties](/js-backend/getting-started/quickstart#get-the-user-id-and-other-properties).


```ts
const machineId = 'mch_123'

const response = await clerkClient.machines.update({
  machineId,
  name: 'New Machine Name',
  defaultTokenTtl: 3600,
})
```

## Backend API (BAPI) endpoint

This method in the SDK is a wrapper around the BAPI endpoint `PATCH/machines/{machine_id}`. See the [BAPI reference](/reference/backend-api/tag/machines/patch/machines/%7Bmachine_id%7D) for more information.
