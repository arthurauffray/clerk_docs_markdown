# Verify OAuth tokens with Clerk


> Learn how to verify OAuth tokens in your applications.

If you are building an application that uses Clerk and would like to incorporate OAuth, you'll want to ensure that after the client gets an OAuth access token, they can use it to make authenticated requests into your app (the resource service) using the token.

> [!NOTE]
> OAuth tokens are machine tokens. Machine token usage is free during our public beta period but will be subject to pricing once generally available. Pricing is expected to be competitive and below market averages.


Clerk's SDKs support this through the `acceptsToken` parameter that can be used in Clerk's route protection functions, such as [`auth()`](/reference/nextjs/app-router/auth), [`auth.protect()`](/reference/nextjs/app-router/auth#auth-protect), and [`authenticateRequest()`](/reference/backend/authenticate-request). The SDKs automatically handle verification for both [JWT and opaque token formats](/guides/development/machine-auth/token-formats) - no code changes are required regardless of which format you've configured.

If you need to verify JWT-formatted OAuth tokens outside of Clerk's SDKs, you can use the same approach as [manual JWT verification](/guides/sessions/manual-jwt-verification) using your instance's public key.

For examples and best practices on verifying OAuth tokens with Clerk SDKs, see our framework-specific guides for:

- [Next.js](/guides/development/verifying-oauth-access-tokens)
- [React Router](/guides/development/verifying-oauth-access-tokens)
- [TanStack React Start](/guides/development/verifying-oauth-access-tokens)

You can also verify tokens manually via the [Clerk REST API](/reference/backend-api/tag/oauth-access-tokens/post/oauth_applications/access_tokens/verify). Ensure you have your Clerk Secret Key on hand as you'll need to include it in the `Authorization` header.

```sh
# Filename: terminal

curl https://api.clerk.com/oauth_applications/access_tokens/verify \
  -X POST \
  -H 'Authorization: Bearer your-clerk-secret-key-here' \
  -H 'Content-Type: application/json' \
  -d '{ "access_token": "your-oauth-token-here" }'
```
