# <PlanDetailsButton />` component


> Clerk's <PlanDetailsButton /> component renders a button that opens the Plan details drawer.

![The \component renders a button that opens the Plan details drawer.](/images/ui-components/plan-details.svg){{ style: { maxWidth: '460px' } }}

The `` component renders a button that opens the Plan details drawer, allowing users to view detailed information about a specific Plan, including pricing, Features, and other Plan-specific details.

> [!WARNING]
>
> Billing is currently in Beta and its APIs are experimental and may undergo breaking changes. To mitigate potential disruptions, we recommend [pinning](/pinning) your SDK and `clerk-js` package versions.


## Usage

`` preserves any click handlers attached to custom button elements, while maintaining the Plan details drawer functionality.

```tsx

  <button onClick={() => console.log('Button clicked')} className="custom-button">
    View Plan
  </button>

```

`` supports rendering the Plan details drawer in a custom portal container.

```tsx

const portalRoot = document.getElementById('custom-portal')

```

### Examples


  ```tsx
// Filename: app/pricing/page.tsx

  'use client'

  import { PlanDetailsButton } from '@clerk/nextjs/experimental'

  export default function PricingPage() {
    return (
      <div>
        
        
          <button className="custom-button">
            View Plan Features
          </button>
        
      </div>
    )
  }
  ```


  ```tsx
// Filename: src/components/PricingSection.tsx

  import { PlanDetailsButton } from '@clerk/react'

  const PricingSection = () => {
    return (
      <div>
        
        
          <button className="custom-button">
            View Plan Features
          </button>
        
      </div>
    )
  }

  export default PricingSection
  ```


  ```vue
// Filename: pricing.vue

  <script setup lang="ts">
  import { PlanDetailsButton } from '@clerk/vue/experimental'
  </script>

  <template>
    <div>
      <!-- Basic usage with Plan ID -->
      <!-- Customizes the appearance of the Plan details drawer -->
      <!-- Custom button -->
      
        <button class="custom-button">View Plan Features</button>
      
    </div>
  </template>
  ```


## Properties

- **`planId?`** `string`

  The ID of the Plan to display details for. It is required if `plan` is not provided.

    ---

- **`plan?`** [`BillingPlanResource`](/reference/javascript/types/billing-plan-resource)

  The Plan to display details for. It is used as initial data until the Plan is fetched from the server.

    ---

- **`children?`** `React.ReactNode`

  Optional custom button element. If not provided, defaults to a button with the text "Plan details".

    ---

- **`initialPlanPeriod?`** `'month' | 'annual'`

  Optional prop to set the initial billing period view when the Plan details drawer opens.

    ---

- **`planDetailsProps?`** `{ appearance: Appearance }`

  Options for the Plan details drawer. Accepts the following properties:

    - [`appearance`](/guides/customizing-clerk/appearance-prop/overview): an object used to style your components. For example: ``.
