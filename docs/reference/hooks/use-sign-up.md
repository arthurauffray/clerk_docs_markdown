# useSignUp()


> Access and manage the current user's sign-up state in your React application with Clerk's useSignUp() hook.

The `useSignUp()` hook provides access to the [`SignUpFuture`](/reference/javascript/sign-up-future) object, which allows you to check the current state of a sign-up attempt and manage the sign-up flow. You can use this to create a custom sign-up flow.

## Returns

- **`signUp`** [`SignUpFuture`](/reference/javascript/sign-up-future)

  The current active `SignUpFuture` instance, for use in custom flows.

    > [!IMPORTANT]
    > The `SignUpFuture` instance referenced by `signUp` does not have a stable identity, and will change as the sign-up flow progresses. Make sure you provide it in dependency arrays when using hooks such as `useEffect`, `useCallback`, or `useMemo`.

    ---

- **`errors`** [`Errors`](/reference/javascript/types/errors)

  The errors that occurred during the last API request.

    ---

- **`fetchStatus`** `'idle' | 'fetching'`

  The fetch status of the underlying `SignUpFuture` resource.


## Examples

For example usage of the `useSignUp()` hook, see the [Build your own UI](/guides/development/custom-flows/overview) guide.
