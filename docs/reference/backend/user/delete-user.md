# deleteUser()


> Use Clerk's JS Backend SDK to delete a user.

Deletes a [`User`](/reference/backend/types/backend-user) given a valid ID.

```ts
function deleteUser(userId: string): Promise
```

## Parameters

- **`userId`** `string`

  The ID of the user to delete.


## Usage

> [!NOTE]
> Using `clerkClient` varies based on your framework. Refer to the [JS Backend SDK overview](/js-backend/getting-started/quickstart) for usage details, including guidance on [how to access the `userId` and other properties](/js-backend/getting-started/quickstart#get-the-user-id-and-other-properties).


```tsx
const userId = 'user_123'

const response = await clerkClient.users.deleteUser(userId)
```

## Example


#### Next.js


    ```ts
// Filename: app/api/example/route.ts

    import { clerkClient } from '@clerk/nextjs/server'
    import { NextResponse } from 'next/server'

    export async function POST() {
      await clerkClient.users.deleteUser('user_123')

      return NextResponse.json({ success: true })
    }
    ```
  

#### Astro


    ```tsx
// Filename: src/api/example.ts

    import type { APIRoute } from 'astro'
    import { clerkClient } from '@clerk/astro/server'

    export const POST: APIRoute = async (context) => {
      await clerkClient(context).users.deleteUser('user_123')

      return new Response(JSON.stringify({ success: true }), { status: 200 })
    }
    ```
  

#### Express


    ```ts
// Filename: public.ts

    import { clerkClient } from '@clerk/express'

    app.post('/deleteUser', async (req, res) => {
      await clerkClient.users.deleteUser('user_123')

      res.status(200).json({ success: true })
    })
    ```
  

#### React Router


    ```tsx
// Filename: app/routes/example.tsx

    import { clerkClient } from '@clerk/react-router/server'
    import type { Route } from './+types/example'
    import { json, redirect } from 'react-router-dom'

    export async function action({ request }: Route.ActionArgs) {
      const formData = await request.formData()
      const userId = formData.get('userId')

      await clerkClient.users.deleteUser(userId)

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
            await clerkClient().users.deleteUser('user_123')

            return json({ success: true })
          },
        },
      },
    })
    ```
  


## Backend API (BAPI) endpoint

This method in the SDK is a wrapper around the BAPI endpoint `DELETE/users/{user_id}`. See the [BAPI reference](/reference/backend-api/tag/users/delete/users/\{user_id}) for more information.

Here's an example of making a request directly to the endpoint using cURL.


  Replace `YOUR_SECRET_KEY` with your Clerk Secret Key.


```bash
# Filename: terminal

  curl 'https://api.clerk.com/v1/users/{user_id}' -X DELETE -H 'Authorization:Bearer {{secret}}' -H 'Content-Type:application/json'
```
