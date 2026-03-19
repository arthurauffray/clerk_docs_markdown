# SetActiveParams


> The parameters for the setActive() method.

The parameters for the `setActive()` method.

- **`session`** <code>[Session](/reference/javascript/session) | string | null</code>

  The session resource or session ID (string version) to be set as active. If `null`, the current session is deleted.

    ---

- **`organization`** <code>[Organization](/reference/javascript/organization) | string | null</code>

  The Organization resource or Organization ID/slug (string version) to be set as active in the current session. If `null`, the currently Active Organization is removed as active.

    ---

- **`redirectUrl?`** `string`

  The full URL or path to redirect to just before the active session and/or Organization is set.

    ---

- **`navigate?`** `(opts: { session: SessionResource; decorateUrl: (url: string) => string }) => Promise<unknown>`

  A custom navigation function to be called just before the session and/or Organization is set. When provided, it takes precedence over the `redirectUrl` parameter for navigation.

    The callback receives:

- **`session`: The new active session** `decorateUrl`: A function that wraps your destination URL to enable Safari ITP cookie refresh when needed. **Always use this to wrap your destination URLs.** [Learn more about this function and Safari ITP cookie refresh](/reference/javascript/clerk#using-the-navigate-parameter).
