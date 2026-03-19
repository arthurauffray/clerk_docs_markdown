# Locals


> Learn how to authenticate your Astro application with Clerk using locals.

Through Astro [`locals`](https://docs.astro.build/en/guides/middleware/#storing-data-in-contextlocals), Clerk's [`Auth`](/reference/backend/types/auth-object) and current [`User`](/reference/backend/types/backend-user) objects can be accessed between middlewares and pages. These locals are injected when you configure the provided [middleware](/reference/astro/clerk-middleware).

## `locals.auth()`

`Astro.locals.auth()` returns an `Auth` object. This JavaScript object contains important information like session data, your user's ID, as well as the ID of the Active Organization. Learn more about the `Auth` object [here](/reference/backend/types/auth-object).

### `locals.auth()` options

- **`opts?`** `{acceptsToken: TokenType, treatPendingAsSignedOut: boolean }`

  An optional object that can be used to configure the behavior of the `locals.auth()` function. It accepts the following properties:

- **`acceptsToken?`: The type of authentication token(s) to accept. Valid values are:**

- **`'session_token'` - authenticates a user session.** `'oauth_token'` - authenticates a machine request using OAuth. `'m2m_token'` - authenticates a machine to machine request. `'api_key'` - authenticates a machine request using API keys.

  Can be set to:

    - A single token type.
    - An array of token types.

- **`'any'` to accept all available token types.**

  Defaults to `'session_token'`.

- **`treatPendingAsSignedOut?`: A boolean that indicates whether to treat [`pending` session status](/reference/javascript/types/session-status#properties) as signed out. Defaults to `true`.**


### Example: Protect a page or form

You can use the `isAuthenticated` property from the `auth()` local to protect your pages and forms.


**Protect a page:**

```astro
// Filename: src/pages/protected.astro

  ---
  const { isAuthenticated, userId, redirectToSignIn } = Astro.locals.auth()

  if (!isAuthenticated) {
    return redirectToSignIn()
  }
  ---

  <div>Protected page</div>
  ```


**Protect a form:**

```astro
// Filename: src/pages/form.astro

  ---
  if (Astro.request.method === 'POST') {
    if (!Astro.locals.auth().isAuthenticated) {
      throw new Error('You must be signed in to add an item to your cart')
    }

    const data = await Astro.request.formData()
    console.log('add item action', data)
  }
  ---

  <form method="POST">
    <input value="test" type="text" name="name" />
    <button type="submit">Add to Cart</button>
  </form>
  ```


### Example: Protect a route based on token type

The following example uses `locals.auth()` to protect the route based on token type:

- It accepts any token type `(acceptsToken: 'any')` from the request.
- If the token is a `session_token`, it logs that the request is from a user session.
- Otherwise, it logs that the request uses a machine token and specifies its type.

```ts
export const GET: APIRoute = ({ locals }) => {
  // Use `locals.auth()` to protect a route based on token type
  const authObject = locals.auth({ acceptsToken: 'any' })

  if (authObject.tokenType === 'session_token') {
    console.log('This is a session token from a user')
  } else {
    console.log(`This is a ${authObject.tokenType} token`)
  }

  return new Response(JSON.stringify({}))
}
```

## `locals.currentUser()`

The `currentUser()` local returns the [`Backend User`](/reference/backend/types/backend-user) object of the currently active user.

Under the hood, this local:

- calls `fetch()`, so it is automatically deduped per request.
- uses the [`GET /v1/users/{user_id}`](/reference/backend-api/tag/users/get/users/\{user_id}) endpoint.
- counts towards the [Backend API request rate limit](/guides/how-clerk-works/system-limits).

> [!WARNING]
> The [`Backend User`](/reference/backend/types/backend-user) object includes a `privateMetadata` field that should not be exposed to the frontend. Avoid passing the full user object returned by `currentUser()` to the frontend. Instead, pass only the specified fields you need.


```astro
// Filename: src/pages/form.astro

---
if (Astro.request.method === 'POST') {
  const user = await Astro.locals.currentUser()

  if (!user) {
    throw new Error('You must be signed in to use this feature')
  }

  const data = await Astro.request.formData()
  const serverData = {
    usersHobby: data.get('hobby'),
    userId: user.id,
    profileImage: user.imageUrl,
  }

  console.log('add item action completed with user details ', serverData)
}
---

<form method="POST">
  <input value="soccer" type="text" name="hobby" />
  <button type="submit">Submit your hobby</button>
</form>
```
