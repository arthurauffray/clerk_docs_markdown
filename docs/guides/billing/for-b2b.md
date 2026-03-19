# Clerk Billing for B2B SaaS


> Clerk Billing is a feature that allows you to create and manage Plans and Features for your application.

> [!WARNING]
>
> Billing is currently in Beta and its APIs are experimental and may undergo breaking changes. To mitigate potential disruptions, we recommend [pinning](/pinning) your SDK and `clerk-js` package versions.


Clerk Billing for B2B SaaS allows you to create Plans and manage Subscriptions **for companies or organizations** in your application. If you'd like to charge individual users, see [Billing for B2C SaaS](/guides/billing/for-b2c). You can also combine both B2C and B2B Billing in the same application.

## Enable Billing

To enable Billing for your application, navigate to the [**Billing Settings**](https://dashboard.clerk.com/~/billing/settings) page in the Clerk Dashboard. This page will guide you through enabling Billing for your application.

Clerk Billing costs the same as using Stripe Billing directly, just 0.7% per transaction, plus transaction fees which are paid directly to Stripe. Clerk Billing is **not** the same as Stripe Billing. Plans and pricing are managed directly through the Clerk Dashboard and won't sync with your existing Stripe products or plans. Clerk uses Stripe **only** for payment processing, so you don't need to set up Stripe Billing.

### Payment gateway

Once you have enabled Billing, you will see the following **Payment gateway** options for collecting payments via Stripe:

- **Clerk development gateway**: A shared **test** Stripe account used for development instances. This allows developers to test and build Billing flows **in development** without needing to create and configure a Stripe account.
- **Stripe account**: Use your own Stripe account for production. **A Stripe account created for a development instance cannot be used for production**. You will need to create a separate Stripe account for your production environment.


## Create a Plan

Subscription Plans are what your customers subscribe to. There is no limit to the number of Plans you can create. If your Clerk instance has existing [Custom Permissions](/guides/organizations/control-access/roles-and-permissions), the corresponding Features from those Permissions will automatically be added to the Free Plan for Organizations. This ensures that Organization members get the same set of Custom Permissions when Billing is enabled, because all Organizations start on the Free Plan.

To create a Plan, navigate to the [**Subscription plans**](https://dashboard.clerk.com/~/billing/plans) page in the Clerk Dashboard. Here, you can create, edit, and delete Plans. To setup B2B Billing, select the **Plans for Organizations** tab and select **Add Plan**. When creating a Plan, you can also create [Features](/guides/secure/features) for the Plan; see the next section for more information.

> [!TIP]
> What is the **Publicly available** option?
>
> ---
>
> Plans appear in some Clerk components depending on what kind of Plan it is. All Plans can appear in the `` component. If it's an Organization Plan, it can appear in the `` component. When creating or editing a Plan, if you'd like to hide it from appearing in Clerk components, you can toggle the **Publicly available** option off.

## Add Features to a Plan

[Features](/guides/secure/features) make it easy to give entitlements to your Plans. You can add any number of Features to a Plan.

You can add a Feature to a Plan when you are creating a Plan. To add it after a Plan is created:

1. Navigate to the [**Subscription plans**](https://dashboard.clerk.com/~/billing/plans) page in the Clerk Dashboard.
1. Select the Plan you'd like to add a Feature to.
1. In the **Features** section, select **Add Feature**.

> [!TIP]
> What is the **Publicly available** option?
>
> ---
>
> Plans appear in some Clerk components depending on what kind of Plan it is. All Plans can appear in the `` component. If it's an Organization Plan, it can appear in the `` component. When adding a Feature to a Plan, it will also automatically appear in the corresponding Plan. When creating or editing a Feature, if you'd like to hide it from appearing in Clerk components, you can toggle the **Publicly available** option off.

## Create a pricing page

You can create a pricing page by using the [``](/reference/components/billing/pricing-table) component. This component displays a table of Plans and Features that customers can subscribe to. **It's recommended to create a dedicated page**, as shown in the following example.


  ```astro
// Filename: src/pages/pricing.astro

  ---
  import { PricingTable } from '@clerk/astro/components'
  ---

  <html>
    <body>
      <div style="max-width: 800px; margin: 0 auto; padding: 0 1rem;">
        </div>
    </body>
  </html>
  ```


  ```js
// Filename: main.js

  import { Clerk } from '@clerk/clerk-js'

  const clerkPubKey = import.meta.env.VITE_CLERK_PUBLISHABLE_KEY

  const clerk = new Clerk(clerkPubKey)
  await clerk.load()

  document.getElementById('app').innerHTML = `
    <div id="pricing-table"></div>
  `

  const pricingTableDiv = document.getElementById('pricing-table')

  clerk.mountPricingTable(pricingTableDiv, { for: 'organization' })
  ```


  ```tsx
// Filename: app/pricing/page.tsx

  import { PricingTable } from '@clerk/nextjs'

  export default function PricingPage() {
    return (
      <div style={{ maxWidth: '800px', margin: '0 auto', padding: '0 1rem' }}>
        </div>
    )
  }
  ```


  ```vue
// Filename: pages/pricing.vue

  <script setup lang="ts">
  // Components are automatically imported
  </script>

  <template>
    <main>
      </main>
  </template>
  ```


  ```vue
// Filename: pages/pricing.vue

  <script setup lang="ts">
  import { PricingTable } from '@clerk/vue'
  </script>

  <template>
    <main>
      </main>
  </template>
  ```


  ```tsx
// Filename: src/screens/pricing.tsx

  import { PricingTable } from '@clerk/react'

  export default function PricingScreen() {
    return (
      <div style={{ maxWidth: '800px', margin: '0 auto', padding: '0 1rem' }}>
        </div>
    )
  }
  ```


  ```tsx
// Filename: app/routes/pricing.tsx

  import type { Route } from './+types/pricing'
  import { PricingTable } from '@clerk/react-router'

  export function meta({}: Route.MetaArgs) {
    return [{ title: 'Pricing' }]
  }

  export default function PricingPage() {
    return (
      <div style={{ maxWidth: '800px', margin: '0 auto', padding: '0 1rem' }}>
        </div>
    )
  }
  ```


  ```tsx
// Filename: app/routes/pricing.tsx

  import { PricingTable } from '@clerk/remix'

  export default function PricingPage() {
    return (
      <div style={{ maxWidth: '800px', margin: '0 auto', padding: '0 1rem' }}>
        </div>
    )
  }
  ```


  ```tsx
// Filename: app/routes/pricing.tsx

  import { PricingTable } from '@clerk/tanstack-react-start'
  import { createFileRoute } from '@tanstack/react-router'

  export const Route = createFileRoute('/')({
    component: PricingPage,
  })

  function PricingPage() {
    return (
      <div style={{ maxWidth: '800px', margin: '0 auto', padding: '0 1rem' }}>
        </div>
    )
  }
  ```


  > [!NOTE]
  > Expo only supports the `` component on the **web**.

  ```tsx
// Filename: app/(home)/pricing.tsx

  import { PricingTable } from '@clerk/expo/web'
  import { View } from 'react-native'

  export default function PricingPage() {
    return (
      
        
    )
  }
  ```


  > [!NOTE]
  > To see an example of how to create a pricing table page, please select one of the frontend SDKs on the sidebar.


## Control access with Features, Plans, and Permissions

You can use Clerk's Features, Plans, and Permissions to gate access to content using authorization checks. There are a few ways to do this, but the recommended approach is to either use the [`has()`](/reference/backend/types/auth-object#has) method or the [``](/reference/components/control/show) component.

> [!IMPORTANT]
> Permission-based authorization checks link with Feature-based authorization checks. This means that if you are checking a Custom Permission, it will only work if the Feature part of the Permission key (`org:<feature>:<permission>`) **is a Feature included in the Organization's active Plan**. For example, say you want to check if an Organization member has the Custom Permission `org:teams:manage`, where `teams` is the Feature. Before performing the authorization check, you need to ensure that the user's Organization is subscribed to a Plan that has the `teams` Feature. If the user's Organization is not subscribed to a Plan that has the `teams` Feature, the authorization check will always return `false`, _even if the user has the Custom Permission_.

### Example: Using `has()`

Use the `has()` method to test if the Organization has access to a **Plan**:

```jsx
const hasPremiumAccess = has({ plan: 'gold' })
```

Or a **Feature**:

```jsx
const hasPremiumAccess = has({ feature: 'widgets' })
```

The [`has()`](/reference/backend/types/auth-object#has) method is a server-side helper that checks if the Organization has been granted a specific type of access control (Role, Permission, Feature, or Plan) and returns a boolean value. `has()` is available on the [`auth` object](/reference/backend/types/auth-object), which you will access differently [depending on the framework you are using](/reference/backend/types/auth-object#how-to-access-the-auth-object).

> [!TIP]
> Why aren't Custom Permissions appearing in the session token (JWT) or in API responses (including the result of the `has()` check)?
>
> ---
>
> Custom Permissions will only appear in the session token (JWT) and in API responses (including the result of the `has()` check) if the Feature part of the Permission key (`org:<feature>:<permission>`) **is a Feature included in the Organization's active Plan**. If the Feature is not part of the Plan, the `has()` check for Permissions using that Feature will return `false`, and those Permissions will not be represented in the session token.
>
> For example, say you want to check if an Organization member has the Custom Permission `org:teams:manage`, where `teams` is the Feature. The user's Organization must be subscribed to a Plan that has the `teams` Feature for authorization checks to work. If the user's Organization is not subscribed to a Plan that has the `teams` Feature, the authorization check will always return `false`, _even if the user has the Custom Permission_.


#### Plan


    The following example demonstrates how to use `has()` to check if an Organization has a Plan.

    
  ```tsx
// Filename: src/components/bronze-content.tsx

  import { useAuth } from '@clerk/astro/react'

  export function BronzeContent() {
    const { isLoaded, has } = useAuth()

    if (!isLoaded) return <div>Loading...</div>

    const hasBronzePlan = has({ plan: 'bronze' })

    if (!hasBronzePlan) return <h1>Only subscribers to the Bronze plan can access this content.</h1>

    return <h1>For Bronze subscribers only</h1>
  }
  ```

  ```astro
// Filename: src/pages/content.astro

  ---
  import { BronzeContent } from '../components/bronze-content'
  ---

  <!doctype html>
  <html>
    <body>
      </body>
  </html>
  ```


  ```js
// Filename: main.js

  import { Clerk } from '@clerk/clerk-js'

  const clerkPubKey = import.meta.env.VITE_CLERK_PUBLISHABLE_KEY

  const clerk = new Clerk(clerkPubKey)
  await clerk.load()

  document.getElementById('app').innerHTML = `
    <div id="bronze-content"></div>
  `

  const bronzeContentDiv = document.getElementById('bronze-content')

  const hasBronzePlan = clerk.session.checkAuthorization({ plan: 'bronze' })

  if (!hasBronzePlan) {
    bronzeContentDiv.innerHTML = `
      <h1>Only subscribers to the Bronze plan can access this content.</h1>
    `
  } else {
    bronzeContentDiv.innerHTML = `
      <h1>For Bronze subscribers only</h1>
    `
  }
  ```


  ```tsx
// Filename: app/bronze-content/page.tsx

  import { auth } from '@clerk/nextjs/server'

  export default async function BronzeContentPage() {
    const { has } = await auth()

    const hasBronzePlan = has({ plan: 'bronze' })

    if (!hasBronzePlan) return <h1>Only subscribers to the Bronze plan can access this content.</h1>

    return <h1>For Bronze subscribers only</h1>
  }
  ```


  ```vue
// Filename: pages/bronze-content.vue

  <script setup lang="ts">
  import { computed } from 'vue'
  import { useAuth } from '@clerk/nuxt/composables'

  const { isLoaded, has } = useAuth()
  const hasBronzePlan = computed(() => has.value?.({ plan: 'bronze' }))
  </script>

  <template>
    <main>
      <div v-if="!isLoaded">Loading...</div>
      <h1 v-else-if="!hasBronzePlan">Only subscribers to the Bronze plan can access this content.</h1>
      <h1 v-else>For Bronze subscribers only</h1>
    </main>
  </template>
  ```


  ```vue
// Filename: src/bronze-content.vue

  <script setup lang="ts">
  import { useAuth } from '@clerk/vue'
  import { computed } from 'vue'

  const { isLoaded, has } = useAuth()
  const hasBronzePlan = computed(() => has.value?.({ plan: 'bronze' }))
  </script>

  <template>
    <main>
      <div v-if="!isLoaded">Loading...</div>
      <h1 v-else-if="!hasBronzePlan">Only subscribers to the Bronze plan can access this content.</h1>
      <h1 v-else>For Bronze subscribers only</h1>
    </main>
  </template>
  ```


  ```tsx
// Filename: src/pages/bronze-content.tsx

  import { useAuth } from '@clerk/react'

  export default function BronzeContentPage() {
    const { has, isLoaded } = useAuth()

    if (!isLoaded) return <div>Loading...</div>

    const hasBronzePlan = has({ plan: 'bronze' })

    if (!hasBronzePlan) return <h1>Only subscribers to the Bronze plan can access this content.</h1>

    return <h1>For Bronze subscribers only</h1>
  }
  ```


  ```tsx
// Filename: app/routes/bronze-content.tsx

  import type { Route } from './+types/bronze-content'
  import { useAuth } from '@clerk/react-router'

  export function meta({}: Route.MetaArgs) {
    return [{ title: 'Bronze Content' }]
  }

  export default function BronzeContentPage() {
    const { has, isLoaded } = useAuth()

    if (!isLoaded) return <div>Loading...</div>

    const hasBronzePlan = has({ plan: 'bronze' })

    if (!hasBronzePlan) return <h1>Only subscribers to the Bronze plan can access this content.</h1>

    return <h1>For Bronze subscribers only</h1>
  }
  ```


  ```tsx
// Filename: app/routes/bronze-content.tsx

  import { getAuth } from '@clerk/remix/ssr.server'
  import { useLoaderData } from '@remix-run/react'
  import type { LoaderFunctionArgs } from '@remix-run/node'

  export const loader = async (args: LoaderFunctionArgs) => {
    const { has } = await getAuth(args)
    return { hasBronzePlan: has({ plan: 'bronze' }) }
  }

  export default function BronzeContentPage() {
    const { hasBronzePlan } = useLoaderData<typeof loader>()

    if (!hasBronzePlan) return <h1>Only subscribers to the Bronze plan can access this content.</h1>

    return <h1>For Bronze subscribers only</h1>
  }
  ```


  ```tsx
// Filename: app/routes/bronze-content.tsx

  import { createFileRoute } from '@tanstack/react-router'
  import { createServerFn } from '@tanstack/react-start'
  import { auth } from '@clerk/tanstack-react-start/server'

  export const authStateFn = createServerFn().handler(async () => {
    const { has, userId } = await auth()

    return {
      userId,
      hasBronzePlan: has({ plan: 'bronze' }),
    }
  })

  export const Route = createFileRoute('/bronze-content')({
    component: BronzeContentPage,
    beforeLoad: async () => {
      const authObject = await authStateFn()
      return {
        userId: authObject.userId,
        hasBronzePlan: authObject.hasBronzePlan,
      }
    },
  })

  function BronzeContentPage() {
    const { hasBronzePlan } = Route.useRouteContext()

    if (!hasBronzePlan) return <h1>Only subscribers to the Bronze plan can access this content.</h1>

    return <h1>For Bronze subscribers only</h1>
  }
  ```


  ```tsx
// Filename: app/(home)/bronze-content.tsx

  import { useAuth } from '@clerk/expo'
  import { Text } from 'react-native'

  export default function BronzeContentPage() {
    const { isLoaded, has } = useAuth()

    if (!isLoaded) return <div>Loading...</div>

    const hasBronzePlan = has({ plan: 'bronze' })

    if (!hasBronzePlan)
      return Only subscribers to the Bronze plan can access this content.

    return For Bronze subscribers only
  }
  ```


  ```tsx
// Filename: src/routes/bronze-content.ts

  import { getAuth, requireAuth } from '@clerk/express'
  import { Router } from 'express'

  const router = Router()

  router.get('/bronze-content', requireAuth(), async (req, res) => {
    const { has } = getAuth(req)

    const hasBronzePlan = has({ plan: 'bronze' })

    if (hasBronzePlan) {
      res.send('For Bronze subscribers only')
    } else {
      res.send('Only subscribers to the Bronze plan can access this content.')
    }
  })

  export default router
  ```


  ```tsx
// Filename: src/routes/bronze-content.ts

  import type { FastifyInstance, FastifyReply, FastifyRequest } from 'fastify'
  import { getAuth } from '@clerk/fastify'

  export const bronzeContentRoutes = (fastify: FastifyInstance) => {
    fastify.get('/bronze-content', async (request: FastifyRequest, reply: FastifyReply) => {
      const { has } = getAuth(request)

      const hasBronzePlan = has({ plan: 'bronze' })

      if (hasBronzePlan) {
        reply.send('For Bronze subscribers only')
      } else {
        reply.send('Only subscribers to the Bronze plan can access this content.')
      }
    })
  }
  ```


  ```ts
// Filename: src/routes/bronze-content.ts

  import { createClerkClient } from '@clerk/backend'

  const clerkClient = createClerkClient({
    publishableKey: process.env.CLERK_PUBLISHABLE_KEY,
    secretKey: process.env.CLERK_SECRET_KEY,
  })

  const domain =
    process.env.NODE_ENV === 'production' ? 'https://example.com' : 'http://localhost:3000'

  export async function GET(request: Request) {
    const authenticatedRequest = await clerkClient.authenticateRequest(request, {
      authorizedParties: [domain],
    })

    const user = authenticatedRequest.toAuth()

    if (user === null || user.userId === null) {
      return new Response('Unauthorized', { status: 401 })
    }

    const hasBronzePlan = user.has({ plan: 'bronze' })

    if (!hasBronzePlan) {
      return new Response('For Bronze subscribers only')
    }

    return new Response('Only subscribers to the Bronze plan can access this content.')
  }
  ```


  

#### Feature


    The following example demonstrates how to use `has()` to check if an Organization has a Feature.

    
  ```tsx
// Filename: src/components/premium-content.tsx

  import { useAuth } from '@clerk/astro/react'

  export function PremiumContent() {
    const { isLoaded, has } = useAuth()

    if (!isLoaded) return <div>Loading...</div>

    const hasPremiumAccess = has({ feature: 'premium_access' })

    if (!hasPremiumAccess)
      return <h1>Only subscribers with the Premium Access feature can access this content.</h1>

    return <h1>Our Exclusive Content</h1>
  }
  ```

  ```astro
// Filename: src/pages/page.astro

  ---
  import { PremiumContent } from '../components/premium-content'
  ---

  <!doctype html>
  <html>
    <body>
      </body>
  </html>
  ```


  ```js
// Filename: main.js

  import { Clerk } from '@clerk/clerk-js'

  const clerkPubKey = import.meta.env.VITE_CLERK_PUBLISHABLE_KEY
  const clerk = new Clerk(clerkPubKey)
  await clerk.load()

  document.getElementById('app').innerHTML = `
    <div id="page-content"></div>
  `

  const pageContentDiv = document.getElementById('page-content')
  const hasPremiumAccess = clerk.session.checkAuthorization({ feature: 'premium_access' })

  if (!hasPremiumAccess) {
    pageContentDiv.innerHTML = `
      <h1>Only subscribers with the Premium Access feature can access this content.</h1>
    `
  } else {
    pageContentDiv.innerHTML = `
      <h1>Our Exclusive Content</h1>
    `
  }
  ```


  ```tsx
// Filename: app/premium-content/page.tsx

  import { auth } from '@clerk/nextjs/server'

  export default async function PremiumContentPage() {
    const { has } = await auth()

    const hasPremiumAccess = has({ feature: 'premium_access' })

    if (!hasPremiumAccess)
      return <h1>Only subscribers with the Premium Access feature can access this content.</h1>

    return <h1>Our Exclusive Content</h1>
  }
  ```


  ```vue
// Filename: pages/premium-content.vue

  <script setup lang="ts">
  import { computed } from 'vue'
  import { useAuth } from '@clerk/nuxt/composables'

  const { isLoaded, has } = useAuth()
  const hasPremiumAccess = computed(() => has.value?.({ feature: 'premium_access' }))
  </script>

  <template>
    <main>
      <div v-if="!isLoaded">Loading...</div>
      <h1 v-else-if="!hasPremiumAccess">
        Only subscribers with the Premium Access feature can access this content.
      </h1>
      <h1 v-else>Our Exclusive Content</h1>
    </main>
  </template>
  ```


  ```vue
// Filename: src/premium-content.vue

  <script setup lang="ts">
  import { useAuth } from '@clerk/vue'
  import { computed } from 'vue'

  const { isLoaded, has } = useAuth()
  const hasPremiumAccess = computed(() => has.value?.({ feature: 'premium_access' }))
  </script>

  <template>
    <main>
      <div v-if="!isLoaded">Loading...</div>
      <h1 v-else-if="!hasPremiumAccess">
        Only subscribers with the Premium Access feature can access this content.
      </h1>
      <h1 v-else>Our Exclusive Content</h1>
    </main>
  </template>
  ```


  ```tsx
// Filename: src/pages/premium-content.tsx

  import { useAuth } from '@clerk/react'

  export default function PremiumContentPage() {
    const { isLoaded, has } = useAuth()

    if (!isLoaded) return <div>Loading...</div>

    const hasPremiumAccess = has({ feature: 'premium_access' })

    if (!hasPremiumAccess)
      return <h1>Only subscribers with the Premium Access feature can access this content.</h1>

    return <h1>Our Exclusive Content</h1>
  }
  ```


  ```tsx
// Filename: app/routes/premium-content.tsx

  import type { Route } from './+types/premium-content'
  import { useAuth } from '@clerk/react-router'

  export function meta({}: Route.MetaArgs) {
    return [{ title: 'Page' }]
  }

  export default function PremiumContentPage() {
    const { isLoaded, has } = useAuth()

    if (!isLoaded) return <div>Loading...</div>

    const hasPremiumAccess = has({ feature: 'premium_access' })

    if (!hasPremiumAccess)
      return <h1>Only subscribers with the Premium Access feature can access this content.</h1>

    return <h1>Our Exclusive Content</h1>
  }
  ```


  ```tsx
// Filename: app/routes/premium-content.tsx

  import { getAuth } from '@clerk/remix/ssr.server'
  import { useLoaderData } from '@remix-run/react'
  import type { LoaderFunctionArgs } from '@remix-run/node'

  export const loader = async (args: LoaderFunctionArgs) => {
    const { has } = await getAuth(args)
    return { hasPremiumAccess: has({ feature: 'premium_access' }) }
  }

  export default function PremiumContentPage() {
    const { hasPremiumAccess } = useLoaderData<typeof loader>()

    if (!hasPremiumAccess)
      return <h1>Only subscribers with the Premium Access feature can access this content.</h1>

    return <h1>Our Exclusive Content</h1>
  }
  ```


  ```tsx
// Filename: app/routes/premium-content.tsx

  import { createFileRoute } from '@tanstack/react-router'
  import { createServerFn } from '@tanstack/react-start'
  import { auth } from '@clerk/tanstack-react-start/server'

  export const authStateFn = createServerFn().handler(async () => {
    const { has, userId } = await auth()

    return {
      userId,
      hasPremiumAccess: has({ feature: 'premium_access' }),
    }
  })

  export const Route = createFileRoute('/premium-content')({
    component: PremiumContentPage,
    beforeLoad: async () => {
      const authObject = await authStateFn()
      return {
        userId: authObject.userId,
        hasPremiumAccess: authObject.hasPremiumAccess,
      }
    },
  })

  function PremiumContentPage() {
    const { hasPremiumAccess } = Route.useRouteContext()

    if (!hasPremiumAccess)
      return <h1>Only subscribers with the Premium Access feature can access this content.</h1>

    return <h1>Our Exclusive Content</h1>
  }
  ```


  ```tsx
// Filename: app/(home)/premium-content.tsx

  import { useAuth } from '@clerk/expo'
  import { Text } from 'react-native'

  export default function PremiumContentPage() {
    const { isLoaded, has } = useAuth()

    if (!isLoaded) return <div>Loading...</div>

    const hasPremiumAccess = has({ feature: 'premium_access' })

    if (!hasPremiumAccess)
      return Only subscribers with the Premium Access feature can access this content.

    return Our Exclusive Content
  }
  ```


  ```ts
// Filename: src/routes/premium-content.ts

  import { getAuth, requireAuth } from '@clerk/express'
  import { Router } from 'express'

  const router = Router()

  router.get('/premium-content', requireAuth(), async (req, res) => {
    const { has } = getAuth(req)
    const hasPremiumAccess = has({ feature: 'premium_access' })

    if (!hasPremiumAccess) {
      res.send('Only subscribers with the Premium Access feature can access this content.')
    } else {
      res.send('Our Exclusive Content')
    }
  })

  export default router
  ```


  ```ts
// Filename: src/routes/premium-content.ts

  import type { FastifyInstance, FastifyReply, FastifyRequest } from 'fastify'
  import { getAuth } from '@clerk/fastify'

  export const premiumContentRoutes = (fastify: FastifyInstance) => {
    fastify.get('/premium-content', async (request: FastifyRequest, reply: FastifyReply) => {
      const { has } = getAuth(request)
      const hasPremiumAccess = has({ feature: 'premium_access' })

      if (!hasPremiumAccess) {
        reply.send('Only subscribers with the Premium Access feature can access this content.')
      } else {
        reply.send('Our Exclusive Content')
      }
    })
  }
  ```


  ```ts
// Filename: src/routes/premium-content.ts

  import { createClerkClient } from '@clerk/backend'

  const clerkClient = createClerkClient({
    publishableKey: process.env.CLERK_PUBLISHABLE_KEY,
    secretKey: process.env.CLERK_SECRET_KEY,
  })

  const domain =
    process.env.NODE_ENV === 'production' ? 'https://example.com' : 'http://localhost:3000'

  export async function GET(request: Request) {
    const authenticatedRequest = await clerkClient.authenticateRequest(request, {
      authorizedParties: [domain],
    })

    const user = authenticatedRequest.toAuth()

    if (user === null || user.userId === null) {
      return new Response('Unauthorized', { status: 401 })
    }

    const hasPremiumAccess = user.has({ feature: 'premium_access' })

    if (!hasPremiumAccess) {
      return new Response('Only subscribers with the Premium Access feature can access this content.')
    }

    return new Response('Our Exclusive Content')
  }
  ```


  

#### Permission


    The following example demonstrates how to use `has()` to check if an Organization has a Permission.

    
  ```tsx
// Filename: src/components/manage-premium-content.tsx

  import { useAuth } from '@clerk/astro/react'

  export function ManagePremiumContent() {
    const { isLoaded, has } = useAuth()

    if (!isLoaded) return <div>Loading...</div>

    const hasPremiumAccessManage = has({ permission: 'org:premium_access:manage' })

    if (!hasPremiumAccessManage)
      return (
        <h1>Only subscribers with the Premium Access Manage permission can access this content.</h1>
      )

    return <h1>Our Exclusive Content</h1>
  }
  ```

  ```astro
// Filename: src/pages/manage-premium-content.astro

  ---
  import { ManagePremiumContent } from '../components/manage-premium-content'
  ---

  <!doctype html>
  <html>
    <body>
      </body>
  </html>
  ```


  ```js
// Filename: main.js

  import { Clerk } from '@clerk/clerk-js'

  const clerkPubKey = import.meta.env.VITE_CLERK_PUBLISHABLE_KEY

  const clerk = new Clerk(clerkPubKey)
  await clerk.load()

  document.getElementById('app').innerHTML = `
    <div id="manage-premium-content"></div>
  `

  const managePremiumContentDiv = document.getElementById('manage-premium-content')

  const hasPremiumAccessManage = clerk.session.checkAuthorization({
    permission: 'org:premium_access:manage',
  })

  if (!hasPremiumAccessManage) {
    managePremiumContentDiv.innerHTML = `
      <h1>Only subscribers with the Premium Access Manage permission can access this content.</h1>
    `
  } else {
    managePremiumContentDiv.innerHTML = `
      <h1>Our Exclusive Content</h1>
    `
  }
  ```


  ```tsx
// Filename: app/manage-premium-content/page.tsx

  import { auth } from '@clerk/nextjs/server'

  export default async function ManagePremiumContentPage() {
    const { has } = await auth()

    const hasPremiumAccessManage = has({ permission: 'org:premium_access:manage' })

    if (!hasPremiumAccessManage)
      return (
        <h1>Only subscribers with the Premium Access Manage permission can access this content.</h1>
      )

    return <h1>Our Exclusive Content</h1>
  }
  ```


  ```vue
// Filename: pages/manage-premium-content.vue

  <script setup lang="ts">
  import { computed } from 'vue'
  import { useAuth } from '@clerk/nuxt/composables'

  const { isLoaded, has } = useAuth()
  const hasPremiumAccessManage = computed(() =>
    has.value?.({ permission: 'org:premium_access:manage' }),
  )
  </script>

  <template>
    <main>
      <div v-if="!isLoaded">Loading...</div>
      <h1 v-else-if="!hasPremiumAccessManage">
        Only subscribers with the Premium Access Manage permission can access this content.
      </h1>
      <h1 v-else>Our Exclusive Content</h1>
    </main>
  </template>
  ```


  ```vue
// Filename: src/manage-premium-content.vue

  <script setup lang="ts">
  import { useAuth } from '@clerk/vue'
  import { computed } from 'vue'

  const { isLoaded, has } = useAuth()
  const hasPremiumAccessManage = computed(() =>
    has.value?.({ permission: 'org:premium_access:manage' }),
  )
  </script>

  <template>
    <main>
      <div v-if="!isLoaded">Loading...</div>
      <h1 v-else-if="!hasPremiumAccessManage">
        Only subscribers with the Premium Access Manage permission can access this content.
      </h1>
      <h1 v-else>Our Exclusive Content</h1>
    </main>
  </template>
  ```


  ```tsx
// Filename: src/pages/manage-premium-content.tsx

  import { useAuth } from '@clerk/react'

  export default function ManagePremiumContentPage() {
    const { has, isLoaded } = useAuth()

    if (!isLoaded) return <div>Loading...</div>

    const hasPremiumAccessManage = has({ permission: 'org:premium_access:manage' })

    if (!hasPremiumAccessManage)
      return (
        <h1>Only subscribers with the Premium Access Manage permission can access this content.</h1>
      )

    return <h1>Our Exclusive Content</h1>
  }
  ```


  ```tsx
// Filename: app/routes/manage-premium-content.tsx

  import type { Route } from './+types/manage-premium-content'
  import { useAuth } from '@clerk/react-router'

  export function meta({}: Route.MetaArgs) {
    return [{ title: 'Manage Premium Content' }]
  }

  export default function ManagePremiumContentPage() {
    const { has, isLoaded } = useAuth()

    if (!isLoaded) return <div>Loading...</div>

    const hasPremiumAccessManage = has({ permission: 'org:premium_access:manage' })

    if (!hasPremiumAccessManage)
      return (
        <h1>Only subscribers with the Premium Access Manage permission can access this content.</h1>
      )

    return <h1>Our Exclusive Content</h1>
  }
  ```


  ```tsx
// Filename: app/routes/manage-premium-content.tsx

  import { getAuth } from '@clerk/remix/ssr.server'
  import { useLoaderData } from '@remix-run/react'
  import type { LoaderFunctionArgs } from '@remix-run/node'

  export const loader = async (args: LoaderFunctionArgs) => {
    const { has } = await getAuth(args)
    return { hasPremiumAccessManage: has({ permission: 'org:premium_access:manage' }) }
  }

  export default function ManagePremiumContentPage() {
    const { hasPremiumAccessManage } = useLoaderData<typeof loader>()

    if (!hasPremiumAccessManage)
      return (
        <h1>Only subscribers with the Premium Access Manage permission can access this content.</h1>
      )

    return <h1>Our Exclusive Content</h1>
  }
  ```


  ```tsx
// Filename: app/routes/manage-premium-content.tsx

  import { createFileRoute } from '@tanstack/react-router'
  import { createServerFn } from '@tanstack/react-start'
  import { auth } from '@clerk/tanstack-react-start/server'

  export const authStateFn = createServerFn().handler(async () => {
    const { has, userId } = await auth()

    return {
      userId,
      hasPremiumAccessManage: has({ permission: 'org:premium_access:manage' }),
    }
  })

  export const Route = createFileRoute('/manage-premium-content')({
    component: ManagePremiumContentPage,
    beforeLoad: async () => {
      const authObject = await authStateFn()
      return {
        userId: authObject.userId,
        hasPremiumAccessManage: authObject.hasPremiumAccessManage,
      }
    },
  })

  function ManagePremiumContentPage() {
    const { hasPremiumAccessManage } = Route.useRouteContext()

    if (!hasPremiumAccessManage)
      return (
        <h1>Only subscribers with the Premium Access Manage permission can access this content.</h1>
      )

    return <h1>Our Exclusive Content</h1>
  }
  ```


  ```tsx
// Filename: app/(home)/manage-premium-content.tsx

  import { useAuth } from '@clerk/expo'
  import { Text } from 'react-native'

  export default function ManagePremiumContentPage() {
    const { isLoaded, has } = useAuth()

    if (!isLoaded) return <div>Loading...</div>

    const hasPremiumAccessManage = has({ permission: 'org:premium_access:manage' })

    if (!hasPremiumAccessManage)
      return (
        
          Only subscribers with the Premium Access Manage permission can access this content.
        
      )

    return Our Exclusive Content
  }
  ```


  ```tsx
// Filename: src/routes/manage-premium-content.ts

  import { getAuth, requireAuth } from '@clerk/express'
  import { Router } from 'express'

  const router = Router()

  router.get('/manage-premium-content', requireAuth(), async (req, res) => {
    const { has } = getAuth(req)

    const hasPremiumAccessManage = has({ permission: 'org:premium_access:manage' })

    if (hasPremiumAccessManage) {
      res.send('Our Exclusive Content')
    } else {
      res.send('Only subscribers with the Premium Access Manage permission can access this content.')
    }
  })

  export default router
  ```


  ```tsx
// Filename: src/routes/manage-premium-content.ts

  import type { FastifyInstance, FastifyReply, FastifyRequest } from 'fastify'
  import { getAuth } from '@clerk/fastify'

  export const managePremiumContentRoutes = (fastify: FastifyInstance) => {
    fastify.get('/manage-premium-content', async (request: FastifyRequest, reply: FastifyReply) => {
      const { has } = getAuth(request)

      const hasPremiumAccessManage = has({ permission: 'org:premium_access:manage' })

      if (hasPremiumAccessManage) {
        reply.send('Our Exclusive Content')
      } else {
        reply.send(
          'Only subscribers with the Premium Access Manage permission can access this content.',
        )
      }
    })
  }
  ```


  ```ts
// Filename: src/routes/manage-premium-content.ts

  import { createClerkClient } from '@clerk/backend'

  const clerkClient = createClerkClient({
    publishableKey: process.env.CLERK_PUBLISHABLE_KEY,
    secretKey: process.env.CLERK_SECRET_KEY,
  })

  const domain =
    process.env.NODE_ENV === 'production' ? 'https://example.com' : 'http://localhost:3000'

  export async function GET(request: Request) {
    const authenticatedRequest = await clerkClient.authenticateRequest(request, {
      authorizedParties: [domain],
    })

    const user = authenticatedRequest.toAuth()

    if (user === null || user.userId === null) {
      return new Response('Unauthorized', { status: 401 })
    }

    const hasPremiumAccessManage = user.has({ permission: 'org:premium_access:manage' })

    if (!hasPremiumAccessManage) {
      return new Response(
        'Only subscribers with the Premium Access Manage permission can access this content.',
      )
    }

    return new Response('Our Exclusive Content')
  }
  ```


  

### Example: Using ``

The [``](/reference/components/control/show) component can be used to protect content or even entire routes by checking if the Organization has been granted a specific type of access control (Role, Permission, Feature, or Plan). You can pass a `fallback` prop to `` that will be rendered if the Organization does not have the access control.


#### Plan


    The following example demonstrates how to use `` to protect a page by checking if the Organization has a Plan.

    
  ```astro
// Filename: src/pages/bronze-content.astro

  ---
  import { Show } from '@clerk/astro/components'
  ---

  <!doctype html>
  <html>
    <body>
      
        <p slot="fallback">Only subscribers to the Bronze plan can access this content.</p>
        <h1>Exclusive Bronze Content</h1>
        <p>This content is only visible to Bronze subscribers.</p>
      
    </body>
  </html>
  ```


  > [!WARNING]
  > JS Frontend SDK doesn't support the `` component.


  ```tsx
// Filename: app/protected-content/page.tsx

  import { Show } from '@clerk/nextjs'

  export default function ProtectedContentPage() {
    return (
      Only subscribers to the Bronze plan can access this content.</p>}
      >
        <h1>Exclusive Bronze Content</h1>
        <p>This content is only visible to Bronze subscribers.</p>
      
    )
  }
  ```


  ```vue
// Filename: pages/protected-content.vue

  <script setup lang="ts">
  // Components are automatically imported
  </script>

  <template>
    <main>
      
        <h1>Exclusive Bronze Content</h1>
        <p>This content is only visible to Bronze subscribers.</p>
      
    </main>
  </template>
  ```


  ```vue
// Filename: src/protected-content.vue

  <script setup lang="ts">
  import { Show } from '@clerk/vue'
  </script>

  <template>
    <main>
      
        <h1>Exclusive Bronze Content</h1>
        <p>This content is only visible to Bronze subscribers.</p>
      
    </main>
  </template>
  ```


  ```tsx
// Filename: src/pages/protected-content.tsx

  import { Show } from '@clerk/react'

  export default function ProtectedContentPage() {
    return (
      Only subscribers to the Bronze plan can access this content.</p>}
      >
        <h1>Exclusive Bronze Content</h1>
        <p>This content is only visible to Bronze subscribers.</p>
      
    )
  }
  ```


  ```tsx
// Filename: app/routes/protected-content.tsx

  import type { Route } from './+types/protected-content'
  import { Show } from '@clerk/react-router'

  export function meta({}: Route.MetaArgs) {
    return [{ title: 'Protected Content' }]
  }

  export default function ProtectedContentPage() {
    return (
      Only subscribers to the Bronze plan can access this content.</p>}
      >
        <h1>Exclusive Bronze Content</h1>
        <p>This content is only visible to Bronze subscribers.</p>
      
    )
  }
  ```


  ```tsx
// Filename: app/routes/protected-content.tsx

  import { Show } from '@clerk/remix'

  export default function ProtectedContentPage() {
    return (
      Only subscribers to the Bronze plan can access this content.</p>}
      >
        <h1>Exclusive Bronze Content</h1>
        <p>This content is only visible to Bronze subscribers.</p>
      
    )
  }
  ```


  ```tsx
// Filename: app/routes/protected-content.tsx

  import { Show } from '@clerk/tanstack-react-start'
  import { createFileRoute } from '@tanstack/react-router'

  export const Route = createFileRoute('/protected-content')({
    component: ProtectedContentPage,
  })

  function ProtectedContentPage() {
    return (
      Only subscribers to the Bronze plan can access this content.</p>}
      >
        <h1>Exclusive Bronze Content</h1>
        <p>This content is only visible to Bronze subscribers.</p>
      
    )
  }
  ```


  ```tsx
// Filename: app/(home)/protected-content.tsx

  import { Show } from '@clerk/expo'
  import { Text } from 'react-native'

  export default function ProtectedContentPage() {
    return (
      Only subscribers to the Bronze plan can access this content.}
      >
        Exclusive Bronze Content
        This content is only visible to Bronze subscribers.
      
    )
  }
  ```


  > [!NOTE]
  > To see an example of how to use the `` component, please select one of the frontend SDKs on the sidebar.


  

#### Feature


    The following example demonstrates how to use `` to protect a page by checking if the Organization has a Feature.

    
  ```astro
// Filename: src/pages/protected-premium-content.astro

  ---
  import { Show } from '@clerk/astro/components'
  ---

  <!doctype html>
  <html>
    <body>
      
        <p slot="fallback">
          Only subscribers with the Premium Access feature can access this content.
        </p>
        <h1>Exclusive Premium Content</h1>
        <p>This content is only visible to users with Premium Access feature.</p>
      
    </body>
  </html>
  ```


  > [!WARNING]
  > JS Frontend SDK doesn't support the `` component.


  ```tsx
// Filename: app/protected-premium-content/page.tsx

  import { Show } from '@clerk/nextjs'

  export default function ProtectedPremiumContentPage() {
    return (
      Only subscribers with the Premium Access feature can access this content.</p>}
      >
        <h1>Exclusive Premium Content</h1>
        <p>This content is only visible to users with Premium Access feature.</p>
      
    )
  }
  ```


  ```vue
// Filename: pages/protected-premium-content.vue

  <script setup lang="ts">
  // Components are automatically imported
  </script>

  <template>
    <main>
      
        <h1>Exclusive Premium Content</h1>
        <p>This content is only visible to users with Premium Access feature.</p>
      
    </main>
  </template>
  ```


  ```vue
// Filename: src/protected-premium-content.vue

  <script setup lang="ts">
  import { Show } from '@clerk/vue'
  </script>

  <template>
    <main>
      
        <h1>Exclusive Premium Content</h1>
        <p>This content is only visible to users with Premium Access feature.</p>
      
    </main>
  </template>
  ```


  ```tsx
// Filename: src/pages/protected-premium-content.tsx

  import { Show } from '@clerk/react'

  export default function ProtectedPremiumContentPage() {
    return (
      
        <h1>Exclusive Premium Content</h1>
        <p>This content is only visible to users with Premium Access feature.</p>
      
    )
  }
  ```


  ```tsx
// Filename: app/routes/protected-premium-content.tsx

  import type { Route } from './+types/protected-premium-content'
  import { Show } from '@clerk/react-router'

  export function meta({}: Route.MetaArgs) {
    return [{ title: 'Protected Premium Content' }]
  }

  export default function ProtectedPremiumContentPage() {
    return (
      Only subscribers with the Premium Access feature can access this content.</p>}
      >
        <h1>Exclusive Premium Content</h1>
        <p>This content is only visible to users with Premium Access feature.</p>
      
    )
  }
  ```


  ```tsx
// Filename: app/routes/protected-premium-content.tsx

  import { Show } from '@clerk/remix'

  export default function ProtectedPremiumContentPage() {
    return (
      Only subscribers with the Premium Access feature can access this content.</p>}
      >
        <h1>Exclusive Premium Content</h1>
        <p>This content is only visible to users with Premium Access feature.</p>
      
    )
  }
  ```


  ```tsx
// Filename: app/routes/protected-premium-content.tsx

  import { Show } from '@clerk/tanstack-react-start'
  import { createFileRoute } from '@tanstack/react-router'

  export const Route = createFileRoute('/protected-premium-content')({
    component: ProtectedPremiumContentPage,
  })

  function ProtectedPremiumContentPage() {
    return (
      Only subscribers with the Premium Access feature can access this content.</p>}
      >
        <h1>Exclusive Premium Content</h1>
        <p>This content is only visible to users with Premium Access feature.</p>
      
    )
  }
  ```


  ```tsx
// Filename: app/(home)/protected-premium-content.tsx

  import { Show } from '@clerk/expo'
  import { Text, View } from 'react-native'

  export default function ProtectedPremiumContentPage() {
    return (
      Only subscribers with the Premium Access feature can access this content.
        }
      >
        
          Exclusive Premium Content
          This content is only visible to users with Premium Access feature.
        
      
    )
  }
  ```


  > [!NOTE]
  > To see an example of how to use the `` component, please select one of the frontend SDKs on the sidebar.


  

#### Permission


    The following example demonstrates how to use `` to protect a page by checking if the Organization has a Permission.

    
  ```astro
// Filename: src/pages/protected-manage-content.astro

  ---
  import { Show } from '@clerk/astro/components'
  ---

  <!doctype html>
  <html>
    <body>
      
        <p slot="fallback">
          Only subscribers with the Premium Access Manage permission can access this content.
        </p>
        <h1>Exclusive Management Content</h1>
        <p>This content is only visible to users with Premium Access Manage permission.</p>
      
    </body>
  </html>
  ```


  > [!WARNING]
  > JS Frontend SDK doesn't support the `` component.


  ```tsx
// Filename: app/protected-manage-content/page.tsx

  import { Show } from '@clerk/nextjs'

  export default function ProtectedManageContentPage() {
    return (
      Only subscribers with the Premium Access Manage permission can access this content.</p>
        }
      >
        <h1>Exclusive Management Content</h1>
        <p>This content is only visible to users with Premium Access Manage permission.</p>
      
    )
  }
  ```


  ```vue
// Filename: pages/protected-manage-content.vue

  <script setup lang="ts">
  // Components are automatically imported
  </script>

  <template>
    <main>
      
        <h1>Exclusive Management Content</h1>
        <p>This content is only visible to users with Premium Access Manage permission.</p>
      
    </main>
  </template>
  ```


  ```vue
// Filename: src/protected-manage-content.vue

  <script setup lang="ts">
  import { Show } from '@clerk/vue'
  </script>

  <template>
    <main>
      
        <h1>Exclusive Management Content</h1>
        <p>This content is only visible to users with Premium Access Manage permission.</p>
      
    </main>
  </template>
  ```


  ```tsx
// Filename: src/pages/protected-manage-content.tsx

  import { Show } from '@clerk/react'

  export default function ProtectedManageContentPage() {
    return (
      Only subscribers with the Premium Access Manage permission can access this content.</p>
        }
      >
        <h1>Exclusive Management Content</h1>
        <p>This content is only visible to users with Premium Access Manage permission.</p>
      
    )
  }
  ```


  ```tsx
// Filename: app/routes/protected-manage-content.tsx

  import type { Route } from './+types/protected-manage-content'
  import { Show } from '@clerk/react-router'

  export function meta({}: Route.MetaArgs) {
    return [{ title: 'Protected Manage Content' }]
  }

  export default function ProtectedManageContentPage() {
    return (
      Only subscribers with the Premium Access Manage permission can access this content.</p>
        }
      >
        <h1>Exclusive Management Content</h1>
        <p>This content is only visible to users with Premium Access Manage permission.</p>
      
    )
  }
  ```


  ```tsx
// Filename: app/routes/protected-manage-content.tsx

  import { Show } from '@clerk/remix'

  export default function ProtectedManageContentPage() {
    return (
      Only subscribers with the Premium Access Manage permission can access this content.</p>
        }
      >
        <h1>Exclusive Management Content</h1>
        <p>This content is only visible to users with Premium Access Manage permission.</p>
      
    )
  }
  ```


  ```tsx
// Filename: app/routes/protected-manage-content.tsx

  import { Show } from '@clerk/tanstack-react-start'
  import { createFileRoute } from '@tanstack/react-router'

  export const Route = createFileRoute('/protected-manage-content')({
    component: ProtectedManageContentPage,
  })

  function ProtectedManageContentPage() {
    return (
      Only subscribers with the Premium Access Manage permission can access this content.</p>
        }
      >
        <h1>Exclusive Management Content</h1>
        <p>This content is only visible to users with Premium Access Manage permission.</p>
      
    )
  }
  ```


  ```tsx
// Filename: app/(home)/protected-manage-content.tsx

  import { Show } from '@clerk/expo'
  import { Text, View } from 'react-native'

  export default function ProtectedManageContentPage() {
    return (
      
            Only subscribers with the Premium Access Manage permission can access this content.
          
        }
      >
        
          Exclusive Management Content
          This content is only visible to users with Premium Access Manage permission.
        
      
    )
  }
  ```


  > [!NOTE]
  > To see an example of how to use the `` component, please select one of the frontend SDKs on the sidebar.
