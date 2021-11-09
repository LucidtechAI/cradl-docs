---
sidebar_position: 3
---

# Authentication

Cradl requires you to authenticate using the [OAuth2 protocol](https://tools.ietf.org/html/rfc6749). Our CLI and SDKs will handle authentication automatically, but if you wish to use the REST API directly, you will need to authenticate manually.

## Credentials

**You should acquire a client id and client secret by creating an App client in the Cradl UI before continuing.** The client id and client secret are used to acquire access tokens for authorizing usage of Cradl.

The endpoint for authentication is [https://auth.lucidtech.ai](https://auth.lucidtech.ai) and the endpoint for the API is [https://api.lucidtech.ai/v1](https://api.lucidtech.ai/v1).

## Using the CLI or SDKs

Our CLI and SDKs will handle access tokens for us. The only thing we need to do is to put the credentials in a file as specified below, and our SDKs will use them automatically. Alternatively, you may use environment variables.

### credentials.cfg

The credentials file should be placed in the following location, depending on the OS:

| OS | Location |
| :--- | :--- |
| Linux/Mac | ~/.lucidtech/credentials.cfg or $HOME/.lucidtech/credentials.cfg |
| Windows | %USERPROFILE%\\.lucidtech\credentials.cfg _or_ %HOME%\\.lucidtech\credentials.cfg |

The credentials.cfg file should look like the following:

```ini
[default]
client_id = <your client id here>
client_secret = <your client secret here>
auth_endpoint = auth.lucidtech.ai
api_endpoint = https://api.lucidtech.ai/v1
```

### Environment variables

```bash
export LAS_CLIENT_ID="<your client id here>"
export LAS_CLIENT_SECRET="<your client secret here>"
export LAS_AUTH_ENDPOINT="auth.lucidtech.ai"
export LAS_API_ENDPOINT="https://api.lucidtech.ai/v1"
```

:::info

Only the api endpoint should have protocol (https) defined.

:::

## Getting an access token manually

To acquire an access token, we query the auth endpoint for access using our client id and client secret. This is done by performing an HTTP POST request to the token endpoint /oauth2/token with two headers provided. One header is 'Authorization' with base64 encoded client\_id and client secret and one header is 'Content-Type' which will always contain the same value: `application/x-www-form-urlencoded`.

| Header name | Header value |
| :--- | :--- |
| Authorization | `Basic Base64Encode(client_id:client_secret)` |
| Content-Type | `application/x-www-form-urlencoded` |

:::info

Read more about Base64Encode [here](https://en.wikipedia.org/wiki/Basic_access_authentication#Client_side).

:::

Since we are dealing with `client_credentials` we need to specify this in the URL as a query parameter. The final URL to make the request to is [https://auth.lucidtech.ai/oauth2/token?grant\_type=client\_credentials](https://auth.lucidtech.ai/oauth2/token?grant_type=client_credentials)

Below is an example of getting an access token using cURL in bash.

```bash
credentials="<your client id here>:<your client secret here>"
base64_encoded_credentials=`echo -n $credentials | base64 -w 0`
curl -X POST https://auth.lucidtech.ai/oauth2/token?grant_type=client_credentials -H "Content-Type: application/x-www-form-urlencoded" -H "Authorization: Basic $base64_encoded_credentials"
```

If everything is working as expected, the response should look similar to the following:

```json
{
  "access_token": "eyJ...",
  "expires_in": 3600,
  "token_type": "Bearer"
}
```

:::caution

The access token will expire after some time, currently after one hour \(3600 seconds \). When the token expires, you need to get a new access token using the same procedure.

:::

## Calling the API

After successfully acquiring an access token from the previous step, we are ready to call the API. To do so we need to provide an 'Authorization' header with the newly acquired access token.

| Header name | Header value |
| :--- | :--- |
| Authorization | `Bearer <your access token here>` |

```bash
access_token="<you access token here>"
curl https://api.lucidtech.ai/v1/documents -H "Authorization: Bearer $access_token"
```

