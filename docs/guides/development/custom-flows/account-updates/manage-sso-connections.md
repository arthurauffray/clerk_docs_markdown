# Build a custom flow for managing SSO connections


> Learn how to use the Clerk API to build a custom flow for adding and managing SSO connections

> [!WARNING]
> This guide is for users who want to build a custom flow. To use a _prebuilt_ UI, use the [Account Portal pages](/guides/account-portal/overview) or [prebuilt components](/reference/components/overview).


This guide demonstrates how to build a custom user interface that allows users to add, delete, and reverify their SSO connections.

## Before you start

You must configure your application instance through the Clerk Dashboard for the SSO connections that you want to use.

- For social (OAuth) connection(s), see [the appropriate guide for your platform](/guides/configure/auth-strategies/social-connections/overview).
- For enterprise connection(s), see [the appropriate guide for your platform](/guides/configure/auth-strategies/enterprise-connections/overview).

This guide uses Discord, Google, and GitHub as examples.

## Build the custom flow

1. The [`useUser()`](/reference/hooks/use-user) hook is used to get the current user's [`User`](/reference/javascript/user) object. The `isLoaded` boolean is used to ensure that Clerk is loaded.
1. The `options` array is used to create a list of supported SSO connections. This example uses [OAuth strategies](/guides/configure/auth-strategies/social-connections/overview). You can edit this array to include all of the SSO connections that you've enabled for your app in the Clerk Dashboard. You can also add [custom SSO connections](/guides/configure/auth-strategies/social-connections/custom-provider) by using the `oauth_custom_<name>` strategy.
1. The `addSSO()` function is used to add a new external account using the `strategy` that is passed in.
   - It uses the `user` object to access the [`createExternalAccount()`](/reference/javascript/user#create-external-account) method.
   - The `createExternalAccount()` method is used to create a new external account using the `strategy` that is passed in. It's passed to the [`useReverification()`](/reference/hooks/use-reverification) hook to require the user to reverify their credentials before being able to add an external account to their account.
1. The `unconnectedOptions` array is used to filter out any existing external accounts from the `options` array.
1. The `normalizeProvider()` function is used to strip the `oauth` prefix from each strategy so it can be matched with the provider field in the user's existing external accounts.
1. In the UI, the `unconnectedOptions` array is used to create a list of buttons for the user to add new external accounts.
1. In the UI, the `User` object is used to access the `externalAccounts` property, which is mapped through to create a list of the user's existing external accounts. If there is an error, it is displayed to the user in the 'Status' column. If the account didn't verify when the user added it, a 'Reverify' button is displayed, which will redirect the user to the provider in order to verify their account.


  
    
      > [!TIP]
> Examples for this SDK aren't available yet. For now, try adapting the  available example to fit your SDK.

    

    ```tsx
// Filename: app/account/manage-external-accounts/page.tsx

    'use client'

    import { useUser, useReverification } from '@clerk/nextjs'
    import {
      CreateExternalAccountParams,
      ExternalAccountResource,
      OAuthStrategy,
    } from '@clerk/shared/types'
    import { useRouter } from 'next/navigation'

    // Capitalize the first letter of the provider name
    // E.g. 'discord' -> 'Discord'
    const capitalize = (provider: string) => {
      return `${provider.slice(0, 1).toUpperCase()}${provider.slice(1)}`
    }

    // Remove the 'oauth' prefix from the strategy string
    // E.g. 'oauth_discord' -> 'discord'
    // Used to match the strategy with the 'provider' field in externalAccounts
    const normalizeProvider = (provider: string) => {
      return provider.split('_')[1]
    }

    export default function AddAccount() {
      const router = useRouter()
      // Use Clerk's `useUser()` hook to get the current user's `User` object
      const { isLoaded, user } = useUser()
      const createExternalAccount = useReverification((params: CreateExternalAccountParams) =>
        user?.createExternalAccount(params),
      )
      const accountDestroy = useReverification((account: ExternalAccountResource) => account.destroy())

      // List the options the user can select when adding a new external account
      // Edit this array to include all of your enabled SSO connections
      const options: OAuthStrategy[] = ['oauth_discord', 'oauth_google', 'oauth_github']

      // Handle adding the new external account
      const addSSO = async (strategy: OAuthStrategy) => {
        await createExternalAccount({
          strategy,
          redirectUrl: '/account/manage-external-accounts',
        })
          .then((res) => {
            if (res?.verification?.externalVerificationRedirectURL) {
              router.push(res.verification.externalVerificationRedirectURL.href)
            }
          })
          .catch((err) => {
            console.log('ERROR', err)
          })
          .finally(() => {
            console.log('Redirected user to oauth provider')
          })
      }

      // Show a loading message until Clerk loads
      if (!isLoaded) return <p>Loading...</p>

      // Find the external accounts from the options array that the user has not yet added to their account
      // This prevents showing an 'add' button for existing external account types
      const unconnectedOptions = options.filter(
        (option) =>
          !user?.externalAccounts.some((account) => account.provider === normalizeProvider(option)),
      )

      return (
        <>
          <div>
            <p>Connected accounts</p>
            {user?.externalAccounts.map((account) => {
              return (
                <ul key={account.id}>
                  <li>Provider: {capitalize(account.provider)}</li>
                  <li>Scopes: {account.approvedScopes}</li>
                  <li>
                    Status:{' '}
                    
                    {account.verification?.status === 'verified'
                      ? capitalize(account.verification?.status)
                      : account.verification?.error?.longMessage}
                  </li>
                  {account.verification?.status !== 'verified' &&
                    account.verification?.externalVerificationRedirectURL && (
                      <li>
                        <a href={account.verification?.externalVerificationRedirectURL?.href}>
                          Reverify {capitalize(account.provider)}
                        </a>
                      </li>
                    )}
                  <li>
                    <button onClick={() => accountDestroy(account)}>
                      Remove {capitalize(account.provider)}
                    </button>
                  </li>
                </ul>
              )
            })}
          </div>
          {unconnectedOptions.length > 0 && (
            <div>
              <p>Add a new external account</p>
              <ul>
                {unconnectedOptions.map((strategy) => {
                  return (
                    <li key={strategy}>
                      <button onClick={() => addSSO(strategy)}>
                        Add {capitalize(normalizeProvider(strategy))}
                      </button>
                    </li>
                  )
                })}
              </ul>
            </div>
          )}
        </>
      )
    }
    ```
  

  
    ```tsx
// Filename: app/(account)/manage-external-accounts/page.tsx

    import { ThemedText } from '@/components/themed-text'
    import { ThemedView } from '@/components/themed-view'
    import { useUser } from '@clerk/expo'
    import { ExternalAccountResource, OAuthStrategy } from '@clerk/shared/types'
    import { Redirect } from 'expo-router'
    import { FlatList, Linking, Pressable, ScrollView, StyleSheet, View } from 'react-native'

    // Capitalize the first letter of the provider name
    // E.g. 'discord' -> 'Discord'
    const capitalize = (provider: string) => {
      return `${provider.slice(0, 1).toUpperCase()}${provider.slice(1)}`
    }

    // Remove the 'oauth' prefix from the strategy string
    // E.g. 'oauth_discord' -> 'discord'
    // Used to match the strategy with the 'provider' field in externalAccounts
    const normalizeProvider = (provider: string) => {
      return provider.split('_')[1]
    }

    export default function AddAccount() {
      const { isLoaded, isSignedIn, user } = useUser()

      // List the options the user can select when adding a new external account
      // Edit this array to include all of your enabled SSO connections
      const options: OAuthStrategy[] = ['oauth_discord', 'oauth_google', 'oauth_github']

      // Handle adding the new external account
      const addSSO = async (strategy: OAuthStrategy) => {
        await user
          ?.createExternalAccount({
            strategy,
            redirectUrl: '/account/manage-external-accounts',
          })
          .then((res) => {
            if (res?.verification?.externalVerificationRedirectURL) {
              Linking.openURL(res.verification.externalVerificationRedirectURL.href)
            }
          })
          .catch((err) => {
            console.log('ERROR', err)
          })
          .finally(() => {
            console.log('Redirected user to oauth provider')
          })
      }

      // Handle removing an external account
      const removeAccount = async (account: ExternalAccountResource) => {
        try {
          await account.destroy()
          await user?.reload()
        } catch (err) {
          console.error('Error removing account:', err)
        }
      }

      // Handle loading state
      if (!isLoaded) {
        return (
          
            Loading...
          
        )
      }

      // Handle signed-out state
      if (!isSignedIn) return // Find the external accounts from the options array that the user has not yet added to their account
      // This prevents showing an 'add' button for existing external account types
      const unconnectedOptions = options.filter(
        (option) =>
          !user?.externalAccounts.some((account) => account.provider === normalizeProvider(option)),
      )

      return (
        
          
            
              Manage External Accounts
            

            
              
                Connected accounts
              

              {user?.externalAccounts.length === 0 ? (
                No external accounts connected
              ) : (
                 item.id}
                  renderItem={({ item: account }) => (
                    
                      
                        
                          {capitalize(account.provider)}
                        
                        
                          Scopes: {account.approvedScopes}
                        
                        
                          Status: 
                          {account.verification?.status === 'verified' ? (
                            
                              {capitalize(account.verification?.status)}
                            
                          ) : (
                            
                              {account.verification?.error?.longMessage}
                            
                          )}
                        
                      

                      
                        {account.verification?.status !== 'verified' &&
                          account.verification?.externalVerificationRedirectURL && (
                             [
                                styles.smallButton,
                                pressed && styles.buttonPressed,
                              ]}
                              onPress={() =>
                                Linking.openURL(
                                  account.verification?.externalVerificationRedirectURL?.href || '',
                                )
                              }
                            >
                              
                                Reverify {capitalize(account.provider)}
                              
                            
                          )}

                         [
                            styles.smallButton,
                            styles.dangerButton,
                            pressed && styles.buttonPressed,
                          ]}
                          onPress={() => removeAccount(account)}
                        >
                          
                            Remove {capitalize(account.provider)}
                          
                        
                      
                    
                  )}
                />
              )}
            

            {unconnectedOptions.length > 0 && (
              
                
                  Add a new external account
                

                
                  {unconnectedOptions.map((strategy) => (
                     [styles.optionButton, pressed && styles.buttonPressed]}
                      onPress={() => addSSO(strategy)}
                    >
                      
                        Add {capitalize(normalizeProvider(strategy))}
                      
                    
                  ))}
                
              
            )}
          
        
      )
    }

    const styles = StyleSheet.create({
      container: {
        flex: 1,
        padding: 20,
      },
      title: {
        marginBottom: 16,
      },
      section: {
        marginBottom: 24,
      },
      sectionTitle: {
        fontWeight: '600',
        fontSize: 16,
        marginBottom: 12,
      },
      infoText: {
        fontSize: 14,
        opacity: 0.8,
      },
      accountCard: {
        padding: 16,
        backgroundColor: '#f5f5f5',
        borderRadius: 8,
        marginBottom: 12,
        gap: 12,
      },
      accountInfo: {
        gap: 6,
      },
      accountProvider: {
        fontSize: 18,
        fontWeight: '600',
      },
      accountDetail: {
        fontSize: 14,
        opacity: 0.8,
      },
      statusRow: {
        flexDirection: 'row',
        alignItems: 'center',
      },
      verifiedText: {
        fontSize: 14,
        color: '#2e7d32',
        fontWeight: '500',
      },
      errorText: {
        fontSize: 14,
        color: '#c62828',
        fontWeight: '500',
        flex: 1,
      },
      accountActions: {
        flexDirection: 'row',
        flexWrap: 'wrap',
        gap: 8,
      },
      smallButton: {
        backgroundColor: '#0a7ea4',
        paddingVertical: 8,
        paddingHorizontal: 16,
        borderRadius: 6,
        alignItems: 'center',
      },
      dangerButton: {
        backgroundColor: '#c62828',
      },
      buttonPressed: {
        opacity: 0.7,
      },
      smallButtonText: {
        color: '#fff',
        fontWeight: '600',
        fontSize: 13,
      },
      dangerButtonText: {
        color: '#fff',
        fontWeight: '600',
        fontSize: 13,
      },
      optionsList: {
        gap: 8,
      },
      optionButton: {
        backgroundColor: '#0a7ea4',
        paddingVertical: 12,
        paddingHorizontal: 24,
        borderRadius: 8,
        alignItems: 'center',
      },
      optionButtonText: {
        color: '#fff',
        fontWeight: '600',
      },
    })
    ```
  


  ```swift
// Filename: ManageSSOConnectionsView.swift

  import SwiftUI
  import ClerkKit

  struct ManageSSOConnectionsView: View {
    @Environment(Clerk.self) private var clerk

    // Edit this array to include all of your enabled SSO connections.
    let options: [OAuthProvider] = [.discord, .google, .github]

    var unconnectedOptions: [OAuthProvider] {
      let connectedProviders = Set((clerk.user?.externalAccounts ?? []).map(provider(for:)))
      return options.filter { !connectedProviders.contains($0) }
    }

    var body: some View {
      VStack {
        Text("Connected accounts")

        ForEach(clerk.user?.externalAccounts ?? []) { account in
          let provider = provider(for: account)

          VStack(alignment: .leading) {
            Text("Provider: \(provider.name)")
            Text("Scopes: \(account.approvedScopes)")
            Text("Status: \(account.verification?.status == .verified ? "Verified" : (account.verification?.error?.longMessage ?? "Unverified"))")

            if account.verification?.status != .verified,
               account.verification?.externalVerificationRedirectUrl != nil {
              Button("Reverify \(provider.name)") {
                Task { await reverifyExternalAccount(account: account) }
              }
            }

            Button("Remove \(provider.name)") {
              Task { await removeExternalAccount(account: account) }
            }
          }
        }

        if !unconnectedOptions.isEmpty {
          Text("Add a new external account")

          ForEach(unconnectedOptions) { provider in
            Button("Add \(provider.name)") {
              Task { await addExternalAccount(provider: provider) }
            }
          }
        }
      }
    }
  }

  extension ManageSSOConnectionsView {

    func addExternalAccount(provider: OAuthProvider) async {
      guard let user = clerk.user else { return }

      do {
        let account = try await user.createExternalAccount(
          provider: provider,
          redirectUrl: "/account/manage-external-accounts"
        )

        // Complete provider verification if needed.
        if account.verification?.externalVerificationRedirectUrl != nil {
          try await account.reauthorize()
        }

        try await user.reload()
      } catch {
        // See https://clerk.com/docs/guides/development/custom-flows/error-handling
        // for more info on error handling
        dump(error)
      }
    }

    func removeExternalAccount(account: ExternalAccount) async {
      do {
        try await account.destroy()
        try await clerk.user?.reload()
      } catch {
        // See https://clerk.com/docs/guides/development/custom-flows/error-handling
        // for more info on error handling
        dump(error)
      }
    }

    func reverifyExternalAccount(account: ExternalAccount) async {
      do {
        try await account.reauthorize()
        try await clerk.user?.reload()
      } catch {
        // See https://clerk.com/docs/guides/development/custom-flows/error-handling
        // for more info on error handling
        dump(error)
      }
    }

    func provider(for account: ExternalAccount) -> OAuthProvider {
      let strategy = account.provider.hasPrefix("oauth_") ? account.provider : "oauth_\(account.provider)"
      return OAuthProvider(strategy: strategy)
    }
  }
  ```


  ```kotlin
  import com.clerk.api.Clerk
  import com.clerk.api.externalaccount.ExternalAccount
  import com.clerk.api.externalaccount.delete
  import com.clerk.api.network.serialization.onFailure
  import com.clerk.api.network.serialization.onSuccess
  import com.clerk.api.sso.OAuthProvider
  import com.clerk.api.user.User
  import com.clerk.api.user.createExternalAccount

  suspend fun addExternalAccount(user: User, provider: OAuthProvider) {
    user
      .createExternalAccount(
        User.CreateExternalAccountParams(
          provider = provider,
          redirectUrl = "/account/manage-external-accounts",
        )
      )
      .onSuccess { account ->
        account.verification?.externalVerificationRedirectUrl?.let { redirectUrl ->
          // Open `redirectUrl` in your browser / web auth flow.
          println(redirectUrl)
        }
      }
      .onFailure {
        // See https://clerk.com/docs/guides/development/custom-flows/error-handling
        // for more info on error handling
      }
  }

  suspend fun removeExternalAccount(account: ExternalAccount) {
    account
      .delete()
      .onFailure {
        // See https://clerk.com/docs/guides/development/custom-flows/error-handling
        // for more info on error handling
      }
  }
  ```
