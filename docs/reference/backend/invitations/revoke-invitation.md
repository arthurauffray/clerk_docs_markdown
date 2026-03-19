# revokeInvitation()


> Use Clerk's JS Backend SDK to revoke an invitation.

Revokes an [`Invitation`](/reference/backend/types/backend-invitation).

Revoking an invitation makes the invitation email link unusable. However, it doesn't prevent the user from signing up if they follow the sign up flow.

Only active (i.e. non-revoked) invitations can be revoked.

```ts
function revokeInvitation(invitationId: string): Promise
```

## Parameters

- **`invitationId`** `string`

  The ID of the invitation to revoke.


## Usage

> [!NOTE]
> Using `clerkClient` varies based on your framework. Refer to the [JS Backend SDK overview](/js-backend/getting-started/quickstart) for usage details, including guidance on [how to access the `userId` and other properties](/js-backend/getting-started/quickstart#get-the-user-id-and-other-properties).


```tsx
const invitationId = 'inv_123'

const response = await clerkClient.invitations.revokeInvitation(invitationId)
```

## Example


#### Next.js


    ```ts
// Filename: app/api/example/route.ts

    import { clerkClient } from '@clerk/nextjs/server'
    import { NextResponse } from 'next/server'

    export async function POST() {
      const client = await clerkClient()
      const invitation = await client.invitations.revokeInvitation({
        invitationId: 'invitation_123',
      })

      return NextResponse.json({ message: 'Invitation revoked' })
    }
    ```
  

#### Astro


    ```tsx
// Filename: src/api/example.ts

    import type { APIRoute } from 'astro'
    import { clerkClient } from '@clerk/astro/server'

    export const POST: APIRoute = async (context) => {
      await clerkClient(context).invitations.revokeInvitation({
        invitationId: 'invitation_123',
      })

      return new Response(JSON.stringify({ success: true }), { status: 200 })
    }
    ```
  

#### Express


    ```ts
// Filename: public.ts

    import { getAuth, clerkClient } from '@clerk/express'

    app.post('/revokeInvitation', async (req, res) => {
      await clerkClient.invitations.revokeInvitation({
        invitationId: 'invitation_123',
      })

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
      const invitationId = formData.get('invitationId')

      await clerkClient.invitations.revokeInvitation({
        invitationId: invitationId,
      })

      return json({ success: true })
    }
    ```
  

#### TanStack React Start


    ```tsx
// Filename: app/routes/api/example.tsx

    import { json } from '@tanstack/react-start'
    import { createFileRoute } from '@tanstack/react-router'
    import { clerkClient } from '@clerk/tanstack-react-start/server'

    export const ServerRoute = createFileRoute('/api/example')({
      server: {
        handlers: {
          POST: async () => {
            await clerkClient().invitations.revokeInvitation({
              invitationId: 'invitation_123',
            })

            return json({ success: true })
          },
        },
      },
    })
    ```
  


## Backend API (BAPI) endpoint

This method in the SDK is a wrapper around the BAPI endpoint `POST/invitations/{invitation_id}/revoke`. See the [BAPI reference](/reference/backend-api/tag/invitations/post/invitations/\{invitation_id}/revoke) for more information.

Here's an example of making a request directly to the endpoint using cURL.


  Replace the `<invitation_id>` with the ID of the invitation you want to revoke. Your Secret Key is already injected into the code snippet.


  Replace the `<invitation_id>` with the ID of the invitation you want to revoke and replace `YOUR_SECRET_KEY` with your Clerk Secret Key.


```bash
# Filename: terminal

curl https://api.clerk.com/v1/invitations/<invitation_id>/revoke -X POST -H "Authorization:Bearer {{secret}}" -H 'Content-Type:application/json'
```
