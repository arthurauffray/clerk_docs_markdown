# Testing with Postman or Insomnia


> Learn about generating and using a long-lived JWT Token with Postman or Insomnia.

Postman and Insomnia are powerful tools used to test API's, validate their behavior, and automate testing tasks. Basic testing with these tools is similar, and this guide will help you get started with either option.

## Generate long-lived JWT template

The standard token issued by Clerk expires after 60 seconds. Clerk SDKs handle refreshing the token regularly so that the authentication state is kept up to date. Because this token expires quickly, it isn't very useful when trying to test with Postman or Insomnia.

You will want to create a long-lived [JWT Template](/guides/sessions/jwt-templates) to be used in Postman or Insomnia. To do so, navigate to the [**JWT templates**](https://dashboard.clerk.com/~/jwt-templates) page in the Clerk Dashboard. Select **New template** then choose the **Blank** template.


Give your template a unique name, such as _'testing-template'_. Set the **Token Lifetime** to a value that suits your needs, or use the maximum of 315360000 seconds (10 years). If you added custom claims to the normal session token, then you should add the same claims to your JWT template.


## Fetch long-lived token

Visit your frontend that is using the same Clerk Application and instance that you want to test. Sign in as a user. The user that you sign in as will be the user you test with in Postman or Insomnia. You can create several tokens for several different users. Once you have signed in, open your Dev Tools and go to the **Console** tab. Enter the following command:

```js
await window.Clerk.session.getToken({ template: '<the template name you chose above>' })
```


## Using Postman or Insomnia


#### Postman


Open Postman and create a new request.


Configure Postman with the method and URL for the API Route you want to test. This example uses the `POST` method and the `/api/protected-route` route.


Navigate to the **Authorization** tab and for token type, select **Bearer Token**. Paste the token you copied from the console as the Bearer Token. Your request will now authenticate as the user you created the token with.


  

#### Insomnia


Open Insomnia and create a new request.


Configure Insomnia with the method and URL for the API Route you want to test. This example uses the `POST` method and the `/api/protected-route` route.


Navigate to the **Auth** tab and select **Auth** again to show a menu of auth types. Choose the **Bearer token** option. Paste the token you copied from the console. Your request will now authenticate as the user you created the token with.


  

## Grouping requests

Postman and Insomnia both provide a **Collections** feature, which allows you to group requests together. Inside that collection, you can add **[Variables](https://learning.postman.com/docs/sending-requests/variables/)** (Postman) or **[Environment Variables](https://docs.insomnia.rest/insomnia/environment-variables)** (Insomnia). These features enable you to use a single token across multiple requests and also allow you to store tokens for multiple users. This is great for testing different features in your application by conveniently changing the token/user you are testing with. You can read more about Postman **Variables** [here](https://learning.postman.com/docs/sending-requests/variables/) and Insomnia **Environment Variables** [here](https://docs.insomnia.rest/insomnia/environment-variables).
