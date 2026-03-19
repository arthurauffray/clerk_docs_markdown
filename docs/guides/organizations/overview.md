# Organizations - Build multi-tenant B2B applications


> Learn what Clerk Organizations are, how they work, and how to build secure multi-tenant B2B applications with team workspaces, Role-Based Access Control, and streamlined enrollment.

Organizations let you group users with Roles and Permissions. This lets you build multi-tenant B2B apps like Slack (workspaces), Linear (teams), or Vercel (projects) where users switch between different team contexts.

Users can belong to multiple Organizations, and Clerk provides the Organization context (memberships, Roles, and the Active Organization) in each session. You can then use this context to control what data to show and what actions to allow.

> [!NOTE]
> To explore Organizations in Clerk, check out the [demo apps](https://github.com/clerk/orgs).

## How do Organizations work?

Organizations live within your Clerk application. Each application can contain multiple Organizations, and each Organization can have multiple users. You define [Roles and Permissions](/guides/organizations/control-access/roles-and-permissions) once at the application level, and they apply across all Organizations within that application.

![Relationship between Clerk Organization, users, Roles and Permissions](/images/orgs/relationship-diagram.jpg)

The Organization that a user is currently viewing is called the **Active Organization**. The Active Organization determines which Organization-specific data the user can access and which Role and related Permissions they have within the Organization.

Clerk measures Organization usage through **Monthly Retained Organizations (MROs)**. An MRO is an Organization with at least two members, where at least one member is a Monthly Retained User. Free plans include up to 50 MROs in development and 100 in production. To increase these limits, refer to the [pricing page](/pricing).

## Core workflow

The core workflow when working with Organizations can follow something along the lines of:

1. **Create**: You can create Organizations [in the Clerk Dashboard](https://dashboard.clerk.com/~/organizations), or end users can create them in your application through prebuilt components or APIs. Each Organization has a profile, settings, and [metadata](/guides/organizations/metadata). Users can belong to multiple Organizations and switch between them with the [``](/reference/components/organization/organization-switcher) component. Learn more about [creating and managing Organizations](/guides/organizations/create-and-manage).

1. **Add members**: You can add members to Organizations in different ways depending on your needs:

   - [**Invitations**](/guides/organizations/add-members/invitations) for bottom-up adoption, where individual users invite teammates with precise control over roles.
   - [**Verified Domains**](/guides/organizations/add-members/verified-domains) for company-wide rollouts, where Clerk automatically invites users with matching email domains (who can join immediately) or suggests they join (requiring admin approval).
   - [**Enterprise Connections**](/guides/organizations/add-members/sso) (SAML or OIDC) for top-down deployments managed by IT with centralized authentication through an Identity Provider (IdP).

   You can combine these approaches: use manual invitations for external contractors alongside domain-based enrollment for employees. The Active Organization determines which members and Roles apply to the current context.

1. **Control access**: You can manage access to content or entire pages using Roles and Permissions. Default admin and member Roles cover common cases, while custom Roles and Permissions provide fine-grained access for more complex needs. You can perform authorization checks in both frontend and backend code.

Beyond these core steps, you can also monitor Organization health and growth with analytics in the Clerk Dashboard. This helps you spot which Organizations are growing, staying active, or dropping off, so you know what's working and where you might need attention.

## Next steps

Now that you understand what Organizations are and how they work, you can:


  - [Configure Organization settings](/guides/organizations/configure)
  - Learn how to configure Organization settings.

  ---

  - [Create and manage Organizations](/guides/organizations/create-and-manage)
  - Learn how to create and manage Organizations to see metadata in action.

  ---

  - [Invite members to Organizations](/guides/organizations/add-members/invitations)
  - Learn how to invite members to Organizations.

  ---

  - [Set up Roles and Permissions](/guides/organizations/control-access/roles-and-permissions)
  - Learn how to set up Roles and Permissions to control what invited users can access.
