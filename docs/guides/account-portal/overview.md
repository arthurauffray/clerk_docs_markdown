# Account Portal overview


> The Account Portal offers a comprehensive solution for managing user authentication and profile management in your web application and is the fastest way to add Clerk's authentication to your application with minimal code required.

The Account Portal in Clerk is a powerful feature that allows you to streamline the sign-in, sign-up, and profile management experience for your users, without having to build your own components or host your own pages. **To integrate the Account Portal with your application, see the [setup guide](/guides/account-portal/getting-started).**


## Why use the Account Portal?

The Account Portal provides the pages necessary for your users to sign-up, sign-in, and manage their accounts, all while maintaining seamless integration with your application. These pages are hosted on Clerk servers for you and they require minimal setup to get started. If you're looking for the fastest way to add authentication and user management to your application, then this is a great choice.

However, if you require more precise customization or prefer having your application self-contained, then you can use Clerk's fully customizable [prebuilt components](/reference/components/overview), or you can build your own [custom user interface using the Clerk API](/guides/development/custom-flows/overview).

## How the Account Portal works

The Account Portal uses Clerk's [prebuilt components](/reference/components/overview), which are embedded into dedicated pages hosted on Clerk servers.


After a user has finished their flow in an Account Portal page, Clerk automatically redirects them back to your application along with the required authentication context. This way, users are automatically redirected to and from your application for a seamless experience.

For each application environment, Clerk provides pages for sign-up, sign-in, user profile, organization profile, and organization creation flow. To integrate the Account Portal into your application, see the [setup guide](/guides/account-portal/getting-started).

### Customizing your pages

These pages cannot be customized beyond the options provided in the [Clerk Dashboard](https://dashboard.clerk.com). If you need more customization such as [localization](/guides/customizing-clerk/localization), consider using [prebuilt components](/reference/components/overview) or building your own [custom user interface](/guides/development/custom-flows/overview).

## Available Account Portal pages

### Sign-in

The sign-in page hosts the prebuilt [``](/reference/components/authentication/sign-in) component, which renders a UI for signing in users. The functionality of the `` component is controlled by the instance settings you specify in the [Clerk Dashboard](https://dashboard.clerk.com), such as [sign-up and sign-in options](/guides/configure/auth-strategies/sign-up-sign-in-options) and [social connections](/guides/configure/auth-strategies/social-connections/overview). The `` component also displays any session tasks that are required for the user to complete after signing in.


Redirect users to the sign-in page using the [``](/reference/components/control/redirect-to-sign-in) control component.

### Sign-up

The sign-up page hosts the prebuilt [``](/reference/components/authentication/sign-up) component, which renders a UI for signing up users. The functionality of the `` component is controlled by the instance settings you specify in the [Clerk Dashboard](https://dashboard.clerk.com), such as [sign-up and sign-in options](/guides/configure/auth-strategies/sign-up-sign-in-options) and [social connections](/guides/configure/auth-strategies/social-connections/overview). The `` component also displays any session tasks that are required for the user to complete after signing up.


Redirect users to the sign-up page using the [``](/reference/components/control/redirect-to-sign-up) control component.

### User profile

The user profile page hosts the prebuilt [``](/reference/components/user/user-profile) component, which renders a beautiful, full-featured account management UI that allows users to manage their profile and security settings.


Redirect your authenticated users to their user profile page using the [``](/reference/components/control/redirect-to-user-profile) control component.

### Unauthorized sign-in

The unauthorized sign-in page doesn't host any prebuilt Clerk component. It displays a UI confirming that a session from an unrecognized device was successfully revoked. For more information, see the [Unauthorized sign-in](/guides/secure/best-practices/unauthorized-sign-in) feature.

The unauthorized sign-in page displays a UI confirming that a session from an unrecognized device was successfully revoked. For more information, refer to [the reference.](/guides/secure/best-practices/unauthorized-sign-in)


### Create Organization

The create Organization page hosts the prebuilt [``](/reference/components/organization/create-organization) component, which provides a streamlined interface for users to create new Organizations within your application.


Redirect your authenticated users to the create Organization page using the [``](/reference/components/control/redirect-to-create-organization) control component.

### Organization Profile

The Organization profile page hosts the prebuilt [``](/reference/components/organization/organization-profile) component, which renders a beautiful, full-featured Organization management UI that allows users to manage their Organization profile and security settings.


Redirect your authenticated users to their Organization Profile page using the [``](/reference/components/control/redirect-to-organization-profile) control component.

### Waitlist

The waitlist page hosts the prebuilt [``](/reference/components/authentication/waitlist) component which renders a form that allows users to join for early access to your app.
