# Component Reference


> A list of Clerk's comprehensive suite of components designed to seamlessly integrate authentication and multi-tenancy into your application.

Clerk offers a comprehensive suite of components designed to seamlessly integrate authentication and multi-tenancy into your application. With Clerk components, you can easily customize the appearance of authentication components and pages, manage the entire authentication flow to suit your specific needs, and even build robust SaaS applications.

## Authentication components

- [``](/reference/components/authentication/sign-in)
- [``](/reference/components/authentication/sign-up)
- [``](/reference/components/authentication/google-one-tap)
- [``](/reference/components/authentication/task-choose-organization)
- [``](/reference/components/authentication/task-reset-password)
- [``](/reference/components/authentication/task-setup-mfa)
- [``](/reference/components/authentication/waitlist)

## User components

- [``](/reference/components/user/user-avatar)
- [``](/reference/components/user/user-button)
- [``](/reference/components/user/user-profile)

## Organization components

- [``](/reference/components/organization/create-organization)
- [``](/reference/components/organization/organization-profile)
- [``](/reference/components/organization/organization-switcher)
- [``](/reference/components/organization/organization-list)

## Billing components

- [``](/reference/components/billing/pricing-table)
- [``](/reference/components/billing/checkout-button)
- [``](/reference/components/billing/plan-details-button)
- [``](/reference/components/billing/subscription-details-button)

## Control components

Control components manage authentication-related behaviors in your application. They handle tasks such as controlling content visibility based on user authentication status, managing loading states during authentication processes, and redirecting users to appropriate pages. Control components render at `` and `` states for assertions on the [`Clerk` object](/reference/javascript/clerk). A common example is the [``](/reference/components/control/show) component, which allows you to conditionally render content based on authentication and authorization state.

- [``](/reference/components/control/authenticate-with-redirect-callback)
- [``](/reference/components/control/clerk-degraded)
- [``](/reference/components/control/clerk-failed)
- [``](/reference/components/control/clerk-loaded)
- [``](/reference/components/control/clerk-loading)
- [``](/reference/components/control/redirect-to-create-organization)
- [``](/reference/components/control/redirect-to-organization-profile)
- [``](/reference/components/control/redirect-to-sign-in)
- [``](/reference/components/control/redirect-to-sign-up)
- [``](/reference/components/control/redirect-to-tasks)
- [``](/reference/components/control/redirect-to-user-profile)
- [``](/reference/components/control/show)

## Unstyled components

- [``](/reference/components/unstyled/sign-in-button)
- [``](/reference/components/unstyled/sign-in-with-metamask)
- [``](/reference/components/unstyled/sign-up-button)
- [``](/reference/components/unstyled/sign-out-button)

## Utilities components

- [``](/reference/components/utilities/portal-provider)

## Customization guides

- [Customize components with the `appearance` prop](/guides/customizing-clerk/appearance-prop/overview)
- [Localize components with the `localization` prop (experimental)](/guides/customizing-clerk/localization)
- [Add pages to the `` component](/guides/customizing-clerk/adding-items/user-profile)
- [Add pages to the `` component](/guides/customizing-clerk/adding-items/organization-profile)

### Secured by Clerk branding

> [!WARNING]
> This feature requires a [paid plan](/pricing) for production use, but all features are free to use in development mode so that you can try out what works for you. See the [pricing](/pricing) page for more information.


By default, Clerk displays a **Secured by Clerk** badge on Clerk components. You can remove this branding by following these steps:

1. In the Clerk Dashboard, navigate to your application's [**Settings**](https://dashboard.clerk.com/~/settings).
1. Under **Branding**, toggle on the **Remove "Secured by Clerk" branding** option.


  - [Join our Discord](https://clerk.com/discord 'Join Discord')
  - Join our official Discord server to chat with us directly and become a part of the Clerk community.
  - 

  ---

  - [Need help?](/support 'Get help')
  - Contact us through Discord, Twitter, or email to receive answers to your questions and learn more about Clerk.
  -
