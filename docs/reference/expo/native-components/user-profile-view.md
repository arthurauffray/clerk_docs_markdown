# <UserProfileView />` component


> A native profile management component providing complete account settings for iOS and Android.

> [!NOTE]
> This documents the native `` from `@clerk/expo/native`. For web projects, use the [web `` component](/reference/components/user/user-profile).

The `` component renders a fully native profile management interface using SwiftUI on iOS and Jetpack Compose on Android. It allows users to manage:

- Profile details
- Email addresses
- Phone numbers
- Multi-factor authentication (MFA)
- Passkeys
- Connected accounts
- Active sessions

> [!IMPORTANT]
> Before using this component, ensure you meet the [Expo requirements](/reference/expo/native-components/overview#requirements).


## Usage

There are **three ways** to render the profile view in an Expo app:

1. **Native modal (recommended):** Use the `useUserProfileModal()` hook to present the profile view as a native modal (SwiftUI/Jetpack Compose). This uses a native `X` button for dismissal.
1. **React Native Modal:** Wrap the inline `` in a React Native `` component. You must provide your own close button to dismiss the modal.
1. **Inline:** Render `` directly in your layout without a modal.

If you need to react to sign-out, use `useAuth()` inside a `useEffect`.

Use the following tabs to select your preferred approach.


#### Using Native modal (recommended)


    The `useUserProfileModal()` hook provides an imperative `presentUserProfile()` function that opens the native profile modal directly from a button press. No component is needed.

    ```tsx
// Filename: app/(home)/index.tsx

    import { useUserProfileModal } from '@clerk/expo'
    import { Text, TouchableOpacity, View } from 'react-native'

    export default function HomeScreen() {
      const { presentUserProfile } = useUserProfileModal()

      return (
        
          
            Manage Profile
          
        
      )
    }
    ```

    #### `useUserProfileModal()` return values

    - **`presentUserProfile`** `() => Promise<void>`

  Opens the native profile modal. The promise resolves when the modal is dismissed. If the user signs out from within the modal, the JS SDK session is automatically cleared.

        ---

- **`isAvailable`** `boolean`

  Whether the native module supports presenting the profile modal. Returns `false` on web or when the `@clerk/expo` plugin is not installed.

        ---

- **`sessions`** <code>Ref\<[Session](/reference/javascript/session)></code>

  A list of sessions that have been registered on the client device.

  

#### Using a React Native Modal


    When rendering inside a React Native ``, ensure `isDismissable` is set to `false` (the default) and provide your own close button to dismiss the modal.

    > [!IMPORTANT]
    > Do not use `useUserProfileModal()` when rendering inside a React Native ``. The native modal system and React Native Modal are separate presentation layers and cannot coordinate dismissal. Use one approach or the other, not both.

    ```tsx
// Filename: app/(home)/index.tsx

    import { useState } from 'react'
    import { View, Text, TouchableOpacity, Modal, StyleSheet } from 'react-native'
    import { UserProfileView } from '@clerk/expo/native'

    export default function HomeScreen() {
      const [showProfile, setShowProfile] = useState(false)

      return (
        
           setShowProfile(true)}>
            Open Profile
          

          
            
               setShowProfile(false)}>
                Close
              
            
            
        
      )
    }

    const styles = StyleSheet.create({
      modalHeader: {
        paddingTop: 60,
        paddingHorizontal: 20,
        paddingBottom: 8,
        alignItems: 'flex-end',
        backgroundColor: '#fff',
      },
      closeButton: {
        color: '#007AFF',
        fontSize: 17,
        fontWeight: '600',
      },
    })
    ```
  

#### Inline


    You can render `` directly in your layout without a modal. This is useful for dedicated profile screens.

    ```tsx
// Filename: app/(home)/profile.tsx

    import { UserProfileView } from '@clerk/expo/native'
    import { useAuth } from '@clerk/expo'
    import { useRouter } from 'expo-router'
    import { useEffect } from 'react'

    export default function ProfileScreen() {
      const { isSignedIn } = useAuth()
      const router = useRouter()

      useEffect(() => {
        if (!isSignedIn) {
          router.replace('/(auth)/sign-in')
        }
      }, [isSignedIn])

      return }
    ```

    ## Properties

    - **`isDismissable`** `boolean`

  Whether the inline profile view can be dismissed by the user. When `true`, a dismiss button appears. This does not present a modal — to present a native modal, use the `useUserProfileModal()` hook instead. Defaults to `false`.

        > [!IMPORTANT]
        > Do not set `isDismissable={true}` when rendering inside a React Native ``. The native dismiss button relies on SwiftUI (iOS) or Jetpack Compose (Android) to close the view, which cannot dismiss a React Native ``. Tapping the native dismiss button will not close the modal and may leave the screen unresponsive.

        ---

- **`style`** `StyleProp`

  Style applied to the container view.

  

## Platform support

| Platform | Status |
| - | - |
| iOS | Supported (SwiftUI) |
| Android | Supported (Jetpack Compose) |
| Web | Use [``](/reference/components/user/user-profile) from `@clerk/expo/web` |
