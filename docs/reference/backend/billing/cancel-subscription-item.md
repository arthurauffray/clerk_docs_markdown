# cancelSubscriptionItem()


> Use Clerk's JS Backend SDK to cancel a Subscription Item.

> [!WARNING]
>
> Billing is currently in Beta and its APIs are experimental and may undergo breaking changes. To mitigate potential disruptions, we recommend [pinning](/pinning) your SDK and `clerk-js` package versions.


Cancels a Subscription Item. Returns the updated [`CommerceSubscriptionItem`](/reference/backend/types/commerce-subscription-item).

```ts
function cancelSubscriptionItem(
  subscriptionItemId: string,
  params?: CancelSubscriptionItemParams,
): Promise
```

## `CancelSubscriptionItemParams`

- **`endNow?`** `boolean`

  If `true`, the Subscription Item will be canceled immediately. If `false` or omitted, it will be canceled at the end of the current billing period.


## Example

> [!NOTE]
> Using `clerkClient` varies based on your framework. Refer to the [JS Backend SDK overview](/js-backend/getting-started/quickstart) for usage details, including guidance on [how to access the `userId` and other properties](/js-backend/getting-started/quickstart#get-the-user-id-and-other-properties).


```tsx
const response = await clerkClient.billing.cancelSubscriptionItem('subi_123', { endNow: true })
```

## Backend API (BAPI) endpoint

This method in the SDK is a wrapper around the BAPI endpoint `DELETE /commerce/subscription_items/{id}`. See the [BAPI reference](/reference/backend-api/tag/commerce/delete/commerce/subscription_items/%7Bsubscription_item_id%7D) for more information.
