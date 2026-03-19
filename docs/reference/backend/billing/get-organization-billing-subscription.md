# getOrganizationBillingSubscription()


> Use Clerk's JS Backend SDK to retrieve an Organization's Billing Subscription.

> [!WARNING]
>
> Billing is currently in Beta and its APIs are experimental and may undergo breaking changes. To mitigate potential disruptions, we recommend [pinning](/pinning) your SDK and `clerk-js` package versions.


Retrieves an Organization's Billing Subscription. Returns a [`CommerceSubscription`](/reference/backend/types/commerce-subscription).

```ts
function getOrganizationBillingSubscription(organizationId: string): Promise
```

## Example

> [!NOTE]
> Using `clerkClient` varies based on your framework. Refer to the [JS Backend SDK overview](/js-backend/getting-started/quickstart) for usage details, including guidance on [how to access the `userId` and other properties](/js-backend/getting-started/quickstart#get-the-user-id-and-other-properties).


```tsx
const organizationId = 'org_123'

const subscription = await clerkClient.billing.getOrganizationBillingSubscription(organizationId)
```

## Backend API (BAPI) endpoint

This method in the SDK is a wrapper around the BAPI endpoint `GET /organizations/{organization_id}/billing/subscription`. See the [BAPI reference](/reference/backend-api/tag/billing/get/organizations/%7Borganization_id%7D/billing/subscription) for more information.
