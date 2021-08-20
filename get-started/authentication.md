# Authentication

The Cradl API requires you to authenticate using the [OAuth2 protocol](https://tools.ietf.org/html/rfc6749). Our CLI tool and SDKs will handle authentication automatically, but if you wish to use the REST API, you will need to authenticate manually. 

## Credentials

**You should acquire a client id and client secret by creating an App Client in the Cradl UI before continuing.** The client id and client secret are used to acquire access tokens for authorized API use.

The endpoint for authentication is [https://auth.cradl.ai](https://auth.cradl.ai) and the endpoint for the API is [https://api.cradl.ai](https://api.cradl.ai).

## Using the CLI or SDKs

Our CLI and SDKs will handle access tokens for you. The only thing you need to do is to put the credentials in a file in the correct location on your computer, and most Cradl SDKs will discover them. Alternatively, you may use environment variables.

#### credentials.json

The credentials file should be placed in the following location, depending on the OS:

| OS | Location |
| :--- | :--- |
| Linux/Mac | ~/.cradl/credentials.json or $HOME/.cradl/credentials.json |
| Windows | %USERPROFILE%.cradl\credentials.json _or_ %HOME%.cradl\credentials.json |

The credentials.json file should look like the following:

```javascript
{
  "default": {
    "client_id": "<your client id here>",
    "clientSecret": "<your client secret here>",
    "authEndpoint": "auth.cradl.ai",
    "apiEndpoint": "api.cradl.ai/v1"
  }
}
```

#### Environment variables

```bash
LAS_CLIENT_ID="<your client id here>"
LAS_CLIENT_SECRET="<your client secret here>"
LAS_AUTH_ENDPOINT="auth.cradl.ai"
LAS_API_ENDPOINT="api.cradl.ai/v1"
```

## Getting an access token manually

To acquire an access token, we query the auth endpoint for access using our client id and client secret. This is done by performing a HTTP POST request to the token endpoint /oauth2/token with two headers provided. One header is 'Authorization' with base64 encoded client\_id and client secret and one header is 'Content-Type' which will always contain the same value: `application/x-www-form-urlencoded`.

| Header name | Header value |
| :--- | :--- |
| Authorization | `Basic Base64Encode(client_id:client_secret)` |
| Content-Type | `application/x-www-form-urlencoded` |

{% hint style="info" %}
Read more about Base64Encode [here](https://en.wikipedia.org/wiki/Basic_access_authentication#Client_side).
{% endhint %}

Since we are dealing with `client_credentials` we need to specify this in the URL as a query parameter. The final URL to make the request to is [https://auth.cradl.ai/oauth2/token?grant\_type=client\_credentials](https://auth.cradl.ai/oauth2/token?grant_type=client_credentials)

Below is an example of getting an access token using cURL in bash.

```bash
$ credentials="<your client id here>:<your client secret here>"
$ base64_encoded_credentials=`echo -n $credentials | base64 -w 0`
$ curl -X POST https://auth.cradl.ai/oauth2/token?grant_type=client_credentials -H "Content-Type: application/x-www-form-urlencoded" -H "Authorization: Basic $base64_encoded_credentials"
```

If everything is working as expected, the response should look similar to the following:

```javascript
{
  "access_token":"eyJ...",
  "expires_in":3600,
  "token_type":"Bearer"
}
```

{% hint style="warning" %}
The access token will expire after some time, currently 3600 seconds \(1 hour\). When the token expires, you need to get a new access token using the same procedure.
{% endhint %}

## Calling the API

After successfully acquiring an access token from the previous step, we are ready to call the API. To do so we need to provide an 'Authorization' header with the newly acquired access token.

| Header name | Header value |
| :--- | :--- |
| Authorization | `Bearer <your access token here>` |

```bash
$ access_token="<you access token here>"
$ curl https://api.cradl.ai/v1/documents -H "Authorization: Bearer $access_token"
```

