# createTestingToken()


> Use Clerk's JS Backend SDK to create a testing token for the instance.

Creates a [Testing Token](/guides/development/testing/overview#testing-tokens) for the instance.

```ts
function createTestingToken(): Promise
```

## Example

> [!NOTE]
> Using `clerkClient` varies based on your framework. Refer to the [JS Backend SDK overview](/js-backend/getting-started/quickstart) for usage details, including guidance on [how to access the `userId` and other properties](/js-backend/getting-started/quickstart#get-the-user-id-and-other-properties).


```tsx
const response = await clerk.testingTokens.createTestingToken()
```

## Backend API (BAPI) endpoint

This method in the SDK is a wrapper around the BAPI endpoint `POST/testing_tokens`. See the [BAPI reference](/reference/backend-api/tag/testing-tokens/post/testing_tokens) for more information.
