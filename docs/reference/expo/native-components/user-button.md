# <UserButton />


> A native avatar button component that displays the user's profile image and opens a profile management interface.

> [!NOTE]
> This documents the native `` from `@clerk/expo/native`. For web projects, use the [web `` component](/reference/components/user/user-button).

The `` component renders an avatar that displays the user's profile image or initials. When tapped, it opens a native profile management modal powered by [``](/reference/expo/native-components/user-profile-view).

Sign-out is handled automatically and synced with the JavaScript SDK. If you need to react to sign-out, use `useAuth()` inside a `useEffect`.

The component fills its parent container - use the parent's styles to control size, shape, border radius, and clipping.

## Requirements

> [!IMPORTANT]
> Before using this component, ensure you meet the [Expo requirements](/reference/expo/native-components/overview#requirements).


In addition to these requirements, this component requires the user to be signed in. The following example demonstrates how to use the [``](/reference/components/control/show) component to check if the user is signed in and render the `` or `` accordingly.

```tsx
// Filename: app/(home)/index.tsx

import { Show } from '@clerk/expo'
import { AuthView, UserButton } from '@clerk/expo/native'
import { View } from 'react-native'

export default function Screen() {
  return (
    <>
      
        
          
      
      
        </>
  )
}
```

## Usage

The following examples show how to use the `` in your Expo app.

### Basic usage

```tsx
// Filename: app/(home)/index.tsx

import { View, Text } from 'react-native'
import { UserButton } from '@clerk/expo/native'
import { useUser } from '@clerk/expo'

export default function HomeScreen() {
  const { user } = useUser()

  return (
    
      
        Welcome, {user?.fullName}
        
          
      
    
  )
}
```

### In a header

```tsx
// Filename: app/(home)/_layout.tsx

import { View } from 'react-native'
import { Stack } from 'expo-router'
import { UserButton } from '@clerk/expo/native'

export default function HomeLayout() {
  return (
     (
          
            
        ),
      }}
    >
      
    
  )
}
```

## Properties

The `` component does not accept any props. It fills its parent container — use the parent's style to control size, shape, border radius, and clipping.

## Platform support

| Platform | Status |
| - | - |
| iOS | Supported (SwiftUI) |
| Android | Supported (Jetpack Compose) |
| Web | Use [``](/reference/components/user/user-button) from `@clerk/expo/web` |
