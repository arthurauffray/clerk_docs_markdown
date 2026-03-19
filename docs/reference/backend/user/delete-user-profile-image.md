# deleteUserProfileImage()


> Use Clerk's JS Backend SDK to delete a user's profile image.

Deletes a user's profile image. Returns a [`User`](/reference/backend/types/backend-user) object.

```ts
function deleteUserProfileImage(userId: string): Promise
```

## Example

> [!NOTE]
> Using `clerkClient` varies based on your framework. Refer to the [JS Backend SDK overview](/js-backend/getting-started/quickstart) for usage details, including guidance on [how to access the `userId` and other properties](/js-backend/getting-started/quickstart#get-the-user-id-and-other-properties).


> [!WARNING]
> Using JS Backend SDK methods can contribute towards rate limiting. To remove a user's profile image, it's recommended to use the frontend [`user.setProfileImage({ file: null })`](/reference/javascript/user#set-profile-image-params) method instead.

```tsx
const userId = 'user_123'

const response = await clerkClient.users.deleteUserProfileImage(userId)
```

## Backend API (BAPI) endpoint

This method in the SDK is a wrapper around the BAPI endpoint `DELETE/users/{user_id}/profile_image`. See the [BAPI reference](/reference/backend-api/tag/users/delete/users/\{user_id}/profile_image) for more information.
