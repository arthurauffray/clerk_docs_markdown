# Configure the SDK


> Configure the Clerk Android SDK with your publishable key.

Initialize [`Clerk`](/reference/native-mobile/clerk) once at app launch in your `Application` class before accessing any Clerk features.

## Basic configuration

```kotlin
// Filename: app/src/main/java/com/example/myclerkapp/MyClerkApp.kt

  package com.example.myclerkapp

  import android.app.Application
  import com.clerk.api.Clerk

  class MyClerkApp: Application() {
      override fun onCreate() {
        super.onCreate()
        Clerk.initialize(
            this,
            publishableKey = "{{pub_key}}"
        )
      }
  }
```


Register your Application class in `AndroidManifest.xml`:

```xml
<application android:name=".MyClerkApp">
    ...
</application>
```

## Wait for initialization

The Clerk SDK initialization is non-blocking. Listen for the SDK to be ready before using Clerk features:

```kotlin
import com.clerk.api.Clerk
import kotlinx.coroutines.flow.first

// Wait for initialization
Clerk.isInitialized.first { it }

// Now safe to use Clerk
val user = Clerk.userFlow.value
```

## Next steps


  - [Clerk](/android/reference/native-mobile/clerk)
  - Learn how to access Clerk in your app.

  ---

  - [Android Quickstart](/android/getting-started/quickstart)
  - Follow the end-to-end setup guide for a Clerk-powered Android app.
