# deleteScope()


> Use Clerk's Backend SDK to delete a machine scope.

Deletes a machine scope, removing access between two machines.

```ts
function deleteScope(machineId: string, otherMachineId: string): Promise
```

## Parameters

- **`machineId`** `string`

  The ID of the machine that currently has access to the target machine.

    ---

- **`otherMachineId`** `string`

  The ID of the machine that will no longer be accessible by the source machine.


## Example

> [!NOTE]
> Using `clerkClient` varies based on your framework. Refer to the [JS Backend SDK overview](/js-backend/getting-started/quickstart) for usage details, including guidance on [how to access the `userId` and other properties](/js-backend/getting-started/quickstart#get-the-user-id-and-other-properties).


```ts
const machineId = 'mch_123'
const otherMachineId = 'mch_456'

const response = await clerkClient.machines.deleteScope(machineId, otherMachineId)
```

## Backend API (BAPI) endpoint

This method in the SDK is a wrapper around the BAPI endpoint `DELETE/machines/{machine_id}/scopes/{other_machine_id}`. See the [BAPI reference](/reference/backend-api/tag/machines/delete/machines/%7Bmachine_id%7D/scopes/%7Bother_machine_id%7D) for more information.
