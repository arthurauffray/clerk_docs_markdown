# User metadata


> Learn how to store information about a user that Clerk doesn't collect and extend the User object.

To store information about a user that Clerk doesn't collect, you can use metadata, which will get stored on the user's [`User` object](/reference/javascript/user).

## Types of metadata

There are three types of metadata: "public", "private", and "unsafe".

| Metadata | Frontend API | Backend API |
| - | - | - |
| Public | Read access | Read & write access |
| Private | No read or write access | Read & write access |
| Unsafe | Read & write access | Read & write access |

> [!WARNING]
> Metadata is limited to **8KB** maximum. If you're storing metadata as a custom claim in the session token, it's highly recommended to keep it under **1.2KB**. [Learn more about the session token size limitations](/guides/sessions/session-tokens#size-limitations).
>
> If you use Clerk metadata and modify it server-side, the changes won't appear in the session token until the next refresh. To avoid race conditions, either [force a JWT refresh](/guides/sessions/force-token-refresh) after metadata changes or handle the delay in your application logic.


### Public metadata

Public metadata can be read by both the frontend and the backend, but can only be set on the backend. This is useful for storing data that you want to expose to the frontend, but don't want the user to be able to modify. For example, you could store a user's birthday.

#### Access public metadata

To access public metadata on the frontend, it's available on the [`User`](/reference/javascript/user) object, which can be accessed using the [`useUser()`](/reference/hooks/use-user) hook.

To access public metadata on the backend, it's available on the [Backend `User`](/reference/backend/types/backend-user) object which can be accessed using the [`getUser()`](/reference/backend/user/get-user) method. This method will return the `User` object which contains the public metadata. However, this method is subject to [rate limits](/guides/how-clerk-works/system-limits#backend-api-requests), so _if you are accessing the metadata frequently_, it's recommended to [attach it to the user's session token](#metadata-in-the-session-token).

#### Set public metadata

To set public metadata, see the [`updateUserMetadata()`](/reference/backend/user/update-user-metadata) reference.

### Private metadata

Private metadata can only be read and set by the backend and webhook handlers, which makes this useful for storing sensitive data that you don't want to expose to the frontend. For example, you could store a user's Stripe customer ID.

#### Access private metadata

To access private metadata on the backend, it's available on the [Backend `User`](/reference/backend/types/backend-user) object which can be accessed using the [`getUser()`](/reference/backend/user/get-user) method. This method will return the `User` object which contains the private metadata. However, this method is subject to [rate limits](/guides/how-clerk-works/system-limits#backend-api-requests), so _if you are accessing the metadata frequently_, it's recommended to [attach it to the user's session token](#metadata-in-the-session-token).

#### Set private metadata

To set private metadata, see the [`updateUserMetadata()`](/reference/backend/user/update-user-metadata) reference.

### Unsafe metadata

Unsafe metadata can be both read and set from the frontend and the backend. It's called "unsafe" metadata because it can be modified directly from the frontend, which means malicious users could potentially tamper with these values.

Unsafe metadata is the only metadata property that can be set during sign-up, so a common use case is to use it in [custom onboarding flows](/guides/development/add-onboarding-flow). Custom data collected during the onboarding (sign-up) flow can be stored in the [`SignUp`](/reference/javascript/sign-up) object. After a successful sign-up, `SignUp.unsafeMetadata` is copied to the `User` object as `User.unsafeMetadata`. From that point on, the unsafe metadata is accessible as a direct attribute of the `User` object.

#### Access unsafe metadata

To access unsafe metadata on the frontend, it's available on the [`User`](/reference/javascript/user) object, which can be accessed using the [`useUser()`](/reference/hooks/use-user) hook.

To access unsafe metadata on the backend, it's available on the [Backend `User`](/reference/backend/types/backend-user) object which can be accessed using the [`getUser()`](/reference/backend/user/get-user) method. This method will return the `User` object which contains the unsafe metadata. However, this method is subject to [rate limits](/guides/how-clerk-works/system-limits#backend-api-requests), so _if you are accessing the metadata frequently_, it's recommended to [attach it to the user's session token](#metadata-in-the-session-token).

#### Set unsafe metadata

See the following examples to see how to set unsafe metadata on the frontend (client-side) and backend (server-side).


#### Client-side


        For React-based SDKs, such as Next.js, use the [`useUser()`](/reference/hooks/use-user) hook to update unsafe metadata.

        ```tsx
// Filename: page.tsx

        export default function Page() {
          const { user } = useUser()
          const [birthday, setBirthday] = useState('')

          return (
            <div>
              <input type="text" value={birthday} onChange={(e) => setBirthday(e.target.value)} />

              <button
                onClick={() => {
                  user?.update({
                    unsafeMetadata: { birthday },
                  })
                }}
              >
                Update birthday
              </button>
            </div>
          )
        }
        ```
      

#### Server-side


        When using the JavaScript SDK, use the [`User.update()`](/reference/javascript/user#update) method to update unsafe metadata.

        ```js
// Filename: main.js

        import { Clerk } from '@clerk/clerk-js'

        // Initialize Clerk with your Clerk Publishable Key
        const pubKey = import.meta.env.VITE_CLERK_PUBLISHABLE_KEY

        const clerk = new Clerk(pubKey)
        await clerk.load()

        if (clerk.isSignedIn) {
          await clerk.user
            .update({
              unsafeMetadata: {
                birthday: '01-01-2000',
              },
            })
            .then((res) => console.log(res))
            .catch((error) => console.log('An error occurred:', error.errors))
        } else {
          document.getElementById('app').innerHTML = `
            <div id="sign-in"></div>
          `

          const signInDiv = document.getElementById('sign-in')

          clerk.mountSignIn(signInDiv)
        }
        ```
      
  

  
    To update unsafe metadata on the server-side, see the [`updateUserMetadata()`](/reference/backend/user/update-user-metadata) reference.
  


## Metadata in the session token

Retrieving metadata from the `User` object on the server-side requires making an API request to Clerk's Backend API, which is slower and is subject to [rate limits](/guides/how-clerk-works/system-limits#backend-api-requests). You can store it in the user's session token, which doesn't require making an API request as it's available on the user's authentication context. **However, there is a size limitation to keep in mind.** Clerk stores the session token in a cookie, and most browsers cap cookie size at [**4KB**](https://datatracker.ietf.org/doc/html/rfc2109#section-6.3). After accounting for the size of Clerk's default claims, the cookie can support **up to 1.2KB** of custom claims. **Exceeding this limit will cause the cookie to not be set, which will break your app as Clerk depends on cookies to work properly.**

If you need to store more than 1.2KB of metadata, you should [store the extra data in your own database](/guides/development/webhooks/syncing#storing-extra-user-data) instead. If this isn't an option, you can [move particularly large claims out of the token](/guides/sessions/session-tokens#example) and fetch them using a separate API call from your backend, but this approach brings back the issue of making an API request to Clerk's Backend API, which is slower and is subject to rate limits.

Another limitation of storing metadata in the session token is that when you modify metadata server-side, the changes won't appear in the session token until the next refresh. To avoid race conditions, either [force a JWT refresh](/guides/sessions/force-token-refresh) after metadata changes or handle the delay in your application logic.

If you've considered the limitations, and you still want to store metadata in the session token:

1. In the Clerk Dashboard, navigate to the [**Sessions**](https://dashboard.clerk.com/~/sessions) page.
1. Under **Customize session token**, in the **Claims** editor, you can add any claim to your session token that you need and select **Save**. To avoid exceeding the session token's 1.2KB limit, it's not recommended to add the entire `user.public_metadata` object. Instead, add individual fields as claims, like `user.public_metadata.birthday`. When doing this, it's recommended to leave particularly large claims out of the token to avoid exceeding the session token's size limit. See the [example](/guides/sessions/session-tokens#example) for more information.
