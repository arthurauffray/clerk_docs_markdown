# updateClerkOptions()


> The updateClerkOptions() function allows you to update Clerk's options at runtime.

The `updateClerkOptions()` function is used to update Clerk's options at runtime. It can be called at any time after [Clerk has been initialized](/reference/astro/integration).

## Usage

```tsx
import { useState } from 'react'
import { updateClerkOptions } from '@clerk/astro/client'
import { dark } from '@clerk/ui/themes'

export function ThemeToggler() {
  const [isDark, setIsDark] = useState(false)
  const { setActive } = useClerk()

  const toggleTheme = () => {
    const theme = !isDark
    setIsDark(theme)

    updateClerkOptions({
      appearance: {
        theme: theme ? dark : undefined,
      },
    })
  }

  return <button onClick={toggleTheme}>Toggle Theme</button>
}
```

## Properties

- **`appearance`** <code>[Appearance](/guides/customizing-clerk/appearance-prop/overview) | undefined</code>

  Optional object to style your components. Will only affect [Clerk components][components-ref] and not [Account Portal][ap-ref] pages.

    ---

- **`localization`** <code>[Localization](/guides/customizing-clerk/localization) | undefined</code>

  Optional object to localize your components. Will only affect [Clerk components][components-ref] and not [Account Portal][ap-ref] pages.


[components-ref]: /docs/reference/components/overview

[ap-ref]: /docs/guides/account-portal/overview
