# rotateSecretKey()


> Use Clerk's Backend SDK to rotate a machine's secret key.

Rotates the machine secret key for a given machine by its ID.

```ts
function rotateSecretKey(params: RotateMachineSecretKeyParams): Promise
```

## Parameters

- **`machineId`** `string`

  The ID of the machine for which to rotate the secret key.

    ---

- **`previousTokenTtl`** `number`

  The time in seconds that the previous secret key will remain valid after rotation.


## Example

> [!NOTE]
> Using `clerkClient` varies based on your framework. Refer to the [JS Backend SDK overview](/js-backend/getting-started/quickstart) for usage details, including guidance on [how to access the `userId` and other properties](/js-backend/getting-started/quickstart#get-the-user-id-and-other-properties).


```ts
const machineId = 'mch_123'

const response = await clerkClient.machines.rotateSecretKey({
  machineId,
  previousTokenTtl: 3600,
})
```

## Backend API (BAPI) endpoint

This method in the SDK is a wrapper around the BAPI endpoint `POST/machines/{machine_id}/secret_key/rotate`. See the [BAPI reference](/reference/backend-api/tag/machines/post/machines/%7Bmachine_id%7D/secret_key/rotate) for more information.
