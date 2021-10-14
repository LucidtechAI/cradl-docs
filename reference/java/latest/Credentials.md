# class `ai::lucidtech::las::sdk::Credentials` 

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public  `[`Credentials`]`(String clientId,String clientSecret,String apiKey,String authEndpoint,String apiEndpoint)` | Used to fetch and store credentials.
`public String `[`getAccessToken`]`(HttpClient httpClient)` | #### Parameters
`public String `[`getApiKey`]`()` | 
`public String `[`getApiEndpoint`]`()` | 

## Members

#### `public  `[`Credentials`]`(String clientId,String clientSecret,String apiKey,String authEndpoint,String apiEndpoint)` 

Used to fetch and store credentials.

#### Parameters
* `clientId` [Client](docs/ai::lucidtech::las::sdk::Client.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_client) id 

* `clientSecret` [Client](docs/ai::lucidtech::las::sdk::Client.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_client) secret 

* `apiKey` API key 

* `authEndpoint` Auth endpoint 

* `apiEndpoint` Domain endpoint of the api, e.g. [https://{prefix}.api.lucidtech.ai/{version}](https://{prefix}.api.lucidtech.ai/{version})

#### Exceptions
* `[MissingCredentialsException](docs/ai::lucidtech::las::sdk::MissingCredentialsException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_missing_credentials_exception)` Raised if some of credentials are missing

#### `public String `[`getAccessToken`]`(HttpClient httpClient)` 

#### Parameters
* `httpClient` Instance of HttpClient used to access the authentication endpoint 

#### Returns
Access token, downloading it if necessary 

#### Exceptions
* `[MissingAccessTokenException](docs/ai::lucidtech::las::sdk::MissingAccessTokenException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_missing_access_token_exception)` Raised if access token cannot be obtained

#### `public String `[`getApiKey`]`()` 

#### `public String `[`getApiEndpoint`]`()` 

