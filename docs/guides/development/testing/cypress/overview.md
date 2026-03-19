# Testing with Cypress


> Use Cypress to write end-to-end tests with Clerk.

> [!WARNING]
> Our `@clerk/testing` package only supports end-to-end testing. Unit tests are not supported.

Testing with Cypress requires the use of [Testing Tokens](/guides/development/testing/overview#testing-tokens) to bypass various bot detection mechanisms that typically safeguard Clerk apps against malicious bots. Without Testing Tokens, you might encounter "Bot traffic detected" errors in your requests.

This guide will help you set up your environment for creating Clerk-authenticated tests with Cypress.

> [!IMPORTANT]
> Check out the [demo repo](https://github.com/clerk/clerk-cypress-nextjs) that tests a Clerk-powered application using [Testing Tokens](/guides/development/testing/overview#testing-tokens).


  ## Install `@clerk/testing`

  Clerk's testing package provides integration helpers for popular testing frameworks. Run the following command to install it:

  
**npm:**

```sh
# Filename: terminal

    npm install @clerk/testing --save-dev
    ```


**yarn:**

```sh
# Filename: terminal

    yarn add -D @clerk/testing
    ```


**pnpm:**

```sh
# Filename: terminal

    pnpm add @clerk/testing -D
    ```


  ## Set your API keys

  In your test runner, set your Publishable Key and Secret Key as the `CLERK_PUBLISHABLE_KEY` and `CLERK_SECRET_KEY` environment variables, respectively.

  > [!WARNING]
  > Ensure you provide the Secret Key in a secure manner, to avoid leaking it to third parties. For example, if you are using GitHub Actions, refer to [_Using secrets in GitHub Actions_](https://docs.github.com/en/actions/security-guides/using-secrets-in-github-actions).

  ## Global setup

  To set up Clerk with Cypress, call the `clerkSetup()` function in your [`cypress.config.ts`](https://docs.cypress.io/guides/references/configuration) file.

  ```tsx
// Filename: cypress.config.ts

  import { clerkSetup } from '@clerk/testing/cypress'
  import { defineConfig } from 'cypress'

  export default defineConfig({
    e2e: {
      setupNodeEvents(on, config) {
        return clerkSetup({ config })
      },
      baseUrl: 'http://localhost:3000', // your app's URL
    },
  })
  ```

  `clerkSetup()` will retrieve a [Testing Token](/guides/development/testing/overview#testing-tokens) once the test suite starts, making it available for all subsequent tests.

  ## Use Clerk Testing Tokens

  Now that Cypress is configured with Clerk, use the `setupClerkTestingToken()` function in your tests to integrate the Testing Token. See the following example:

  ```tsx
// Filename: testing-tokens.cy.ts

  import { setupClerkTestingToken } from '@clerk/testing/cypress'

  it('sign up', () => {
    setupClerkTestingToken()

    cy.visit('/sign-up')
    // Add any other actions to test
  })
  ```
