# createInvitation()


> Use Clerk's JS Backend SDK to create a new invitation for the given email address, and send the invitation email.

Creates a new [`Invitation`](/reference/backend/types/backend-invitation) for the given email address and sends the invitation email.

If an email address has already been invited or already exists in your application, trying to create a new invitation will return an error. To bypass this error and create a new invitation anyways, set `ignoreExisting` to `true`.

> [!CAUTION]
>
> This endpoint is [rate limited](/guides/how-clerk-works/system-limits#backend-api-requests) to **100 requests per hour** per application instance.

```ts
function createInvitation(params: CreateParams): Promise
```

## `CreateParams`

- **`emailAddress`** `string`

  The email address of the user to invite.

    ---

- **`redirectUrl?`** `string`

  The full URL or path where the user is redirected upon visiting the invitation link, where they can accept the invitation. Required if you have implemented a [custom flow for handling application invitations](/guides/development/custom-flows/authentication/application-invitations).

    ---

- **`publicMetadata?`** [`UserPublicMetadata`](/reference/javascript/types/metadata#user-public-metadata)

  Metadata that can be read from both the Frontend API and [Backend API](/reference/backend-api), but can be set only from the Backend API. Once the user accepts the invitation and signs up, these metadata will end up in the user's public metadata.

    ---

- **`notify?`** `boolean`

  Whether an email invitation should be sent to the given email address. Defaults to `true`.

    ---

- **`ignoreExisting?`** `boolean`

  Whether an invitation should be created if there is already an existing invitation for this email address, or if the email address already exists in the application. Defaults to `false`.

    ---

- **`expiresInDays?`** `number`

  The number of days the invitation will be valid for. By default, the invitation expires after 30 days.

    ---

- **`templateSlug?`** `'invitation' | 'waitlist_invitation'`

  The slug of the email template to use for the invitation email. Defaults to `invitation`.


## Usage

> [!NOTE]
> Using `clerkClient` varies based on your framework. Refer to the [JS Backend SDK overview](/js-backend/getting-started/quickstart) for usage details, including guidance on [how to access the `userId` and other properties](/js-backend/getting-started/quickstart#get-the-user-id-and-other-properties).


```tsx
const response = await clerkClient.invitations.createInvitation({
  emailAddress: 'invite@example.com',
  redirectUrl: 'https://www.example.com/my-sign-up',
  publicMetadata: {
    example: 'metadata',
    example_nested: {
      nested: 'metadata',
    },
  },
})
```

## Example


#### Next.js


    ```ts
// Filename: app/api/example/route.ts

    import { clerkClient } from '@clerk/nextjs/server'
    import { NextResponse } from 'next/server'

    export async function POST() {
      const client = await clerkClient()
      const invitation = await client.invitations.createInvitation({
        emailAddress: 'invite@example.com',
        redirectUrl: 'https://www.example.com/my-sign-up',
        publicMetadata: {
          example: 'metadata',
          example_nested: {
            nested: 'metadata',
          },
        },
      })

      return NextResponse.json({ message: 'Invitation created', invitation })
    }
    ```
  

#### Astro


    ```tsx
// Filename: src/api/example.ts

    import type { APIRoute } from 'astro'
    import { clerkClient } from '@clerk/astro/server'

    export const POST: APIRoute = async (context) => {
      await clerkClient(context).invitations.createInvitation({
        emailAddress: 'invite@example.com',
        redirectUrl: 'https://www.example.com/my-sign-up',
        publicMetadata: {
          example: 'metadata',
          example_nested: {
            nested: 'metadata',
          },
        },
      })

      return new Response(JSON.stringify({ success: true }), { status: 200 })
    }
    ```
  

#### Express


    ```ts
// Filename: public.ts

    import { getAuth, clerkClient } from '@clerk/express'

    app.post('/createUser', async (req, res) => {
      await clerkClient.invitations.createInvitation({
        emailAddress: 'invite@example.com',
        redirectUrl: 'https://www.example.com/my-sign-up',
        publicMetadata: {
          example: 'metadata',
          example_nested: {
            nested: 'metadata',
          },
        },
        password: 'password',
      })

      res.status(200).json({ success: true })
    })
    ```
  

#### React Router


    ```tsx
// Filename: app/routes/example.tsx

    import { clerkClient } from '@clerk/react-router/server'
    import type { Route } from './+types/example'
    import { json } from 'react-router-dom'

    export async function action({ request }: Route.ActionArgs) {
      const formData = await request.formData()
      const emailAddress = formData.get('emailAddress')
      const redirectUrl = formData.get('redirectUrl')
      const publicMetadata = formData.get('publicMetadata')

      await clerkClient.invitations.createInvitation({
        emailAddress: emailAddress,
        redirectUrl: redirectUrl,
        publicMetadata: publicMetadata,
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
            await clerkClient().invitations.createInvitation({
              emailAddress: 'invite@example.com',
              redirectUrl: 'https://www.example.com/my-sign-up',
              publicMetadata: {
                example: 'metadata',
                example_nested: {
                  nested: 'metadata',
                },
              },
            })

            return json({ success: true })
          },
        },
      },
    })
    ```
  


## Backend API (BAPI) endpoint

This method in the SDK is a wrapper around the BAPI endpoint `POST/invitations`. See the [BAPI reference](/reference/backend-api/tag/invitations/post/invitations) for more information.

Here's an example of making a request directly to the endpoint using cURL.


  Replace the email address with the email address you want to invite. Your Clerk Secret Key is already injected into the code snippet.


  Replace the email address with the email address you want to invite. Update `YOUR_SECRET_KEY` with your Clerk Secret Key.


```bash
# Filename: terminal

curl https://api.clerk.com/v1/invitations -X POST -d '{"email_address": "email@example.com"}' -H "Authorization:Bearer {{secret}}" -H 'Content-Type:application/json'
```
