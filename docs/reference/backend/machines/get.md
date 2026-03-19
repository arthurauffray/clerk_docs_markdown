# get()


> Use Clerk's Backend SDK to retrieve a machine.

Retrieves a machine by its ID.

```ts
function get(machineId: string): Promise
```

## Parameters

- **`machineId`** `string`

  The ID of the machine to retrieve.


## Example

> [!NOTE]
> Using `clerkClient` varies based on your framework. Refer to the [JS Backend SDK overview](/js-backend/getting-started/quickstart) for usage details, including guidance on [how to access the `userId` and other properties](/js-backend/getting-started/quickstart#get-the-user-id-and-other-properties).


```ts
const machineId = 'mch_123'

const response = await clerkClient.machines.get(machineId)
```

## Backend API (BAPI) endpoint

This method in the SDK is a wrapper around the BAPI endpoint `GET/machines/{machine_id}`. See the [BAPI reference](/reference/backend-api/tag/machines/get/machines/%7Bmachine_id%7D) for more information.
