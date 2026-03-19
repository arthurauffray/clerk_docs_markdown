# createScope()


> Use Clerk's Backend SDK to create a machine scope.

Creates a new machine scope, allowing the specified machine to access another machine.

```ts
function createScope(machineId: string, toMachineId: string): Promise
```

## Parameters

- **`machineId`** `string`

  The ID of the machine that will have access to the target machine.

    ---

- **`toMachineId`** `string`

  The ID of the machine that will be accessible by the source machine.


## Example

> [!NOTE]
> Using `clerkClient` varies based on your framework. Refer to the [JS Backend SDK overview](/js-backend/getting-started/quickstart) for usage details, including guidance on [how to access the `userId` and other properties](/js-backend/getting-started/quickstart#get-the-user-id-and-other-properties).


```ts
const machineId = 'mch_123'
const toMachineId = 'mch_456'

const response = await clerkClient.machines.createScope(machineId, toMachineId)
```

## Backend API (BAPI) endpoint

This method in the SDK is a wrapper around the BAPI endpoint `POST/machines/{machine_id}/scopes`. See the [BAPI reference](/reference/backend-api/tag/machines/post/machines/%7Bmachine_id%7D/scopes) for more information.
