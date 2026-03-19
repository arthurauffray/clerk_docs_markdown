# updateUserProfileImage()


> Use Clerk's JS Backend SDK to update a user's profile image.

Updates a user's profile image. Returns a [`User`](/reference/backend/types/backend-user) object.

```ts
function updateUserProfileImage(userId: string, params: { file: Blob | File }): Promise
```

## Example

> [!NOTE]
> Using `clerkClient` varies based on your framework. Refer to the [JS Backend SDK overview](/js-backend/getting-started/quickstart) for usage details, including guidance on [how to access the `userId` and other properties](/js-backend/getting-started/quickstart#get-the-user-id-and-other-properties).


> [!WARNING]
> Using JS Backend SDK methods can contribute towards rate limiting. To set a user's profile image, it's recommended to use the frontend [`user.setProfileImage()`](/reference/javascript/user#set-profile-image) method instead.

```tsx
const userId = 'user_123'
const fileBits = ['profile-pic-content']
const fileName = 'profile-pic.png'
const file = new File(fileBits, fileName, { type: 'image/png' })

const params = {
  file,
}

const response = await clerkClient.users.updateUserProfileImage(userId, params)
```

## Backend API (BAPI) endpoint

This method in the SDK is a wrapper around the BAPI endpoint `POST/users/{user_id}/profile_image`. See the [BAPI reference](/reference/backend-api/tag/users/post/users/\{user_id}/profile_image) for more information.
