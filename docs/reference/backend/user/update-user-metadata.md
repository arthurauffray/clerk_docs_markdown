# updateUserMetadata()


> Use Clerk's JS Backend SDK to update the metadata associated with the specified user.

Updates the metadata associated with the specified user by merging existing values with the provided parameters.

A "deep" merge will be performed - "deep" means that any nested JSON objects will be merged as well. You can remove metadata keys at any level by setting their value to `null`.

Returns a [`User`](/reference/backend/types/backend-user) object.

```ts
function updateUserMetadata(userId: string, params: UpdateUserMetadataParams): Promise
```

## `UpdateUserMetadataParams`

- **`userId`** `string`

  The ID of the user to update.

    ---

- **`publicMetadata?`** [`UserPublicMetadata`](/reference/javascript/types/metadata#user-public-metadata)

  Metadata that can be read from the Frontend API and [Backend API](/reference/backend-api) and can be set only from the Backend API.

    ---

- **`privateMetadata?`** [`UserPrivateMetadata`](/reference/javascript/types/metadata#user-private-metadata)

  Metadata that can be read and set only from the [Backend API](/reference/backend-api).


## Usage

> [!NOTE]
> Using `clerkClient` varies based on your framework. Refer to the [JS Backend SDK overview](/js-backend/getting-started/quickstart) for usage details, including guidance on [how to access the `userId` and other properties](/js-backend/getting-started/quickstart#get-the-user-id-and-other-properties).


```tsx
const userId = 'user_123'

const response = await clerkClient.users.updateUserMetadata(userId, {
  publicMetadata: {
    example: 'metadata',
  },
})
```

## Example

This example updates the user's public metadata to include a birthday, but you can update the public, private, or unsafe metadata to include any information you want.


#### Next.js


    ```ts
// Filename: app/api/example/route.ts

    import { auth, clerkClient } from '@clerk/nextjs/server'
    import { NextResponse } from 'next/server'

    export async function POST() {
      const { userId } = await auth()
      const client = await clerkClient()

      await client.users.updateUserMetadata(userId, {
        publicMetadata: {
          birthday: '1990-01-01',
        },
      })

      return NextResponse.json({ success: true })
    }
    ```
  

#### Astro


    ```tsx
// Filename: src/api/example.ts

    import type { APIRoute } from 'astro'
    import { clerkClient } from '@clerk/astro/server'

    export const POST: APIRoute = async (context) => {
      const { userId } = context.locals.auth()

      await clerkClient(context).users.updateUserMetadata(userId, {
        publicMetadata: {
          birthday: '1990-01-01',
        },
      })

      return new Response(JSON.stringify({ success: true }), { status: 200 })
    }
    ```
  

#### Express


    ```ts
// Filename: public.ts

    import { getAuth, clerkClient } from '@clerk/express'

    app.post('/updateBirthday', async (req, res) => {
      const { userId } = getAuth(req)

      await clerkClient.users.updateUserMetadata(userId, {
        publicMetadata: {
          birthday: '1990-01-01',
        },
      })
      res.status(200).json({ success: true })
    })
    ```
  

#### React Router


    ```tsx
// Filename: app/routes/example.tsx

    import { clerkClient, getAuth } from '@clerk/react-router/server'
    import type { Route } from './+types/example'

    export async function action({ request }: Route.ActionArgs) {
      const { userId } = await getAuth(request)

      await clerkClient.users.updateUserMetadata(userId, {
        publicMetadata: {
          birthday: '1990-01-01',
        },
      })

      return json({ success: true })
    }
    ```
  

#### TanStack React Start


    ```tsx
// Filename: app/routes/api/example.tsx

    import { json } from '@tanstack/react-start'
    import { createFileRoute } from '@tanstack/react-router'
    import { auth, clerkClient } from '@clerk/tanstack-react-start/server'

    export const ServerRoute = createFileRoute('/api/example')({
      server: {
        handlers: {
          POST: async () => {
            const { userId } = await auth()

            await clerkClient().users.updateUserMetadata(userId, {
              publicMetadata: {
                birthday: '1990-01-01',
              },
            })

            return json({ success: true })
          },
        },
      },
    })
    ```
  

## Backend API (BAPI) endpoint

This method in the SDK is a wrapper around the BAPI endpoint `PATCH/users/{user_id}/metadata`. See the [BAPI reference](/reference/backend-api/tag/users/patch/users/\{user_id}/metadata) for more information.

Here's an example of making a request directly to the endpoint using cURL.


  Replace `YOUR_SECRET_KEY` with your Clerk Secret Key. You can find your Secret Key on the [**API keys**](https://dashboard.clerk.com/~/api-keys) page in the Clerk Dashboard.


```bash
# Filename: curl.sh

curl -XPATCH -H 'Authorization: Bearer {{secret}}' -H "Content-type: application/json" -d '{
  "public_metadata": {
    "birthday": "1990-01-01"
  }
}' 'https://api.clerk.com/v1/users/{user_id}/metadata'
```
