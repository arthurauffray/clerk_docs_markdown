# updateClerkOptions()


> The updateClerkOptions() function allows you to update Clerk's options at runtime.

The `updateClerkOptions()` function is used to update Clerk's options at runtime. It can be called at any time after [Clerk has been initialized](/reference/vue/clerk-plugin).

## Usage

```vue
<script setup>
import { updateClerkOptions } from '@clerk/vue'
import { dark } from '@clerk/ui/themes'

const isDark = ref(false)

function toggleTheme() {
  isDark.value = !isDark.value
  updateClerkOptions({
    appearance: {
      theme: isDark.value ? dark : undefined,
    },
  })
}
</script>

<template>
  <button @click="toggleTheme">Toggle Theme</button>
</template>
```

## Properties

- **`appearance`** <code>[Appearance](/guides/customizing-clerk/appearance-prop/overview) | undefined</code>

  Optional object to style your components. Will only affect [Clerk components][components-ref] and not [Account Portal][ap-ref] pages.

    ---

- **`localization`** <code>[Localization](/guides/customizing-clerk/localization) | undefined</code>

  Optional object to localize your components. Will only affect [Clerk components][components-ref] and not [Account Portal][ap-ref] pages.


[components-ref]: /docs/reference/components/overview

[ap-ref]: /docs/guides/account-portal/overview
