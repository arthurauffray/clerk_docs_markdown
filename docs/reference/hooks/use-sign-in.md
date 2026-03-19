# useSignIn()


> Access and manage the current user's sign-in state in your React application with Clerk's useSignIn() hook.

The `useSignIn()` hook provides access to the [`SignInFuture`](/reference/javascript/sign-in-future) object, which allows you to check the current state of a sign-in attempt and manage the sign-in flow. You can use this to create a custom sign-in flow.

## Returns

- **`signIn`** [`SignInFuture`](/reference/javascript/sign-in-future)

  The current active `SignInFuture` instance, for use in custom flows.

    > [!IMPORTANT]
    > The `SignInFuture` instance referenced by `signIn` does not have a stable identity, and will change as the sign-in flow progresses. Make sure you provide it in dependency arrays when using hooks such as `useEffect`, `useCallback`, or `useMemo`.

    ---

- **`errors`** [`Errors`](/reference/javascript/types/errors)

  The errors that occurred during the last API request.

    ---

- **`fetchStatus`** `'idle' | 'fetching'`

  The fetch status of the underlying `SignInFuture` resource.


## Examples

For example usage of the `useSignIn()` hook, see the [Build your own UI](/guides/development/custom-flows/overview) guide.
