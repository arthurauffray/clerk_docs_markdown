# delete()


> Use Clerk's Backend SDK to delete a machine.

Deletes a machine by its ID.

```ts

function delete(machineId: string): Promise
```

## Parameters

- **`machineId`** `string`

  The ID of the machine to delete.


## Example

> [!NOTE]
> Using `clerkClient` varies based on your framework. Refer to the [JS Backend SDK overview](/js-backend/getting-started/quickstart) for usage details, including guidance on [how to access the `userId` and other properties](/js-backend/getting-started/quickstart#get-the-user-id-and-other-properties).


```ts
const machineId = 'mch_123'

const response = await clerkClient.machines.delete(machineId)
```

## Backend API (BAPI) endpoint

This method in the SDK is a wrapper around the BAPI endpoint `DELETE/machines/{machine_id}`. See the [BAPI reference](/reference/backend-api/tag/machines/delete/machines/%7Bmachine_id%7D) for more information.
