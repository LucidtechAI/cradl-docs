---
title: REST API v1
language_tabs:
  - shell: Shell
  - http: HTTP
  - javascript: JavaScript
  - ruby: Ruby
  - python: Python
  - php: PHP
  - java: Java
  - go: Go
toc_footers: []
includes: []
search: true
highlight_theme: darkula
headingLevel: 2

---

Base URLs:

* https://api.lucidtech.ai/{basePath}

    * **basePath** -  Default: v1

# Authentication

* API Key (api_key)
    - Parameter Name: **x-api-key**, in: header. 

- oAuth2 authentication. 

    - Flow: clientCredentials

    - Token URL = [https://auth.lucidtech.ai/oauth2/token](https://auth.lucidtech.ai/oauth2/token)

|Scope|Scope Description|
|---|---|
|api.lucidtech.ai/logs:read|Scope for GET /logs/{logId}|
|api.lucidtech.ai/users:read|Scope for GET /users/{userId}|
|api.lucidtech.ai/transitions:write|Scope for DELETE /transitions/{transitionId}|
|api.lucidtech.ai/datasets:read|Scope for GET /datasets/{datasetId}|
|api.lucidtech.ai/organizations:write|Scope for PATCH /organizations/{organizationId}|
|api.lucidtech.ai/organizations:read|Scope for GET /organizations/{organizationId}|
|api.lucidtech.ai/signup:write|Scope for POST /signup|
|api.lucidtech.ai/assets:write|Scope for DELETE /assets/{assetId}|
|api.lucidtech.ai/transitions.executions.heartbeats:write|Scope for POST /transitions/{transitionId}/executions/{executionId}/heartbeats|
|api.lucidtech.ai/secrets:read|Scope for GET /secrets|
|api.lucidtech.ai/transitions:read|Scope for GET /transitions/{transitionId}|
|api.lucidtech.ai/predictions:read|Scope for GET /predictions|
|api.lucidtech.ai/users:write|Scope for PATCH /users/{userId}|
|api.lucidtech.ai/assets:read|Scope for GET /assets/{assetId}|
|api.lucidtech.ai/workflows.executions:write|Scope for PATCH /workflows/{workflowId}/executions/{executionId}|
|api.lucidtech.ai/transitions.executions:write|Scope for PATCH /transitions/{transitionId}/executions/{executionId}|
|api.lucidtech.ai/appclients:write|Scope for DELETE /appClients/{appClientId}|
|api.lucidtech.ai/databundles:read|Scope for GET /models/{modelId}/dataBundles|
|api.lucidtech.ai/workflows:write|Scope for PATCH /workflows/{workflowId}|
|api.lucidtech.ai/models:read|Scope for GET /models/{modelId}|
|api.lucidtech.ai/predictions:write|Scope for POST /predictions|
|api.lucidtech.ai/appclients:read|Scope for GET /appClients|
|api.lucidtech.ai/models:write|Scope for DELETE /models/{modelId}|
|api.lucidtech.ai/databundles:write|Scope for DELETE /models/{modelId}/dataBundles/{dataBundleId}|
|api.lucidtech.ai/secrets:write|Scope for DELETE /secrets/{secretId}|
|api.lucidtech.ai/documents:read|Scope for GET /documents/{documentId}|
|api.lucidtech.ai/documents:write|Scope for DELETE /documents/{documentId}|
|api.lucidtech.ai/workflows:read|Scope for GET /workflows/{workflowId}|
|api.lucidtech.ai/transitions.executions:read|Scope for GET /transitions/{transitionId}/executions/{executionId}|
|api.lucidtech.ai/datasets:write|Scope for DELETE /datasets/{datasetId}|
|api.lucidtech.ai/workflows.executions:read|Scope for GET /workflows/{workflowId}/executions/{executionId}|

<h1 id="lucidtech-api-default">Default</h1>

## get__appClients

`GET /appClients`

<h3 id="get__appclients-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|nextToken|query|string|false|none|
|maxResults|query|string|false|none|

> Example responses

> 200 Response

```json
{
  "nextToken": "string",
  "appClients": [
    {
      "hasSecret": true,
      "updatedTime": "string",
      "clientId": "string",
      "updatedBy": "string",
      "apiKey": "string",
      "logoutUrls": [
        "string"
      ],
      "description": "string",
      "callbackUrls": [
        "string"
      ],
      "loginUrls": [
        "string"
      ],
      "defaultLoginUrl": "string",
      "createdBy": "string",
      "name": "string",
      "createdTime": "string",
      "clientSecret": "string",
      "appClientId": "string"
    }
  ]
}
```

<h3 id="get__appclients-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|200 response|[AppClients](#schemaappclients)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|400 response|[Error](#schemaerror)|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|403 response|[Error](#schemaerror)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|404 response|[Error](#schemaerror)|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|415 response|[Error](#schemaerror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|500 response|[Error](#schemaerror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
None, api_key
</aside>

## options__appClients

`OPTIONS /appClients`

> Body parameter

```json
{}
```

<h3 id="options__appclients-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[Empty](#schemaempty)|true|none|

> Example responses

> 200 Response

```json
{}
```

<h3 id="options__appclients-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|200 response|[Empty](#schemaempty)|

<aside class="success">
This operation does not require authentication
</aside>

## post__appClients

`POST /appClients`

> Body parameter

```json
{
  "generateSecret": true,
  "logoutUrls": [
    "string"
  ],
  "name": "string",
  "callbackUrls": [
    "string"
  ],
  "description": "string",
  "loginUrls": [
    "string"
  ],
  "defaultLoginUrl": "string"
}
```

<h3 id="post__appclients-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Content-Type|header|string|true|none|
|body|body|[PostAppClients](#schemapostappclients)|true|none|

> Example responses

> 200 Response

```json
{
  "hasSecret": true,
  "updatedTime": "string",
  "clientId": "string",
  "updatedBy": "string",
  "apiKey": "string",
  "logoutUrls": [
    "string"
  ],
  "description": "string",
  "callbackUrls": [
    "string"
  ],
  "loginUrls": [
    "string"
  ],
  "defaultLoginUrl": "string",
  "createdBy": "string",
  "name": "string",
  "createdTime": "string",
  "clientSecret": "string",
  "appClientId": "string"
}
```

<h3 id="post__appclients-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|200 response|[AppClient](#schemaappclient)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|400 response|[Error](#schemaerror)|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|403 response|[Error](#schemaerror)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|404 response|[Error](#schemaerror)|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|415 response|[Error](#schemaerror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|500 response|[Error](#schemaerror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
None, api_key
</aside>

## delete__appClients_{appClientId}

`DELETE /appClients/{appClientId}`

<h3 id="delete__appclients_{appclientid}-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|appClientId|path|string|true|none|

> Example responses

> 200 Response

```json
{
  "hasSecret": true,
  "updatedTime": "string",
  "clientId": "string",
  "updatedBy": "string",
  "apiKey": "string",
  "logoutUrls": [
    "string"
  ],
  "description": "string",
  "callbackUrls": [
    "string"
  ],
  "loginUrls": [
    "string"
  ],
  "defaultLoginUrl": "string",
  "createdBy": "string",
  "name": "string",
  "createdTime": "string",
  "clientSecret": "string",
  "appClientId": "string"
}
```

<h3 id="delete__appclients_{appclientid}-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|200 response|[AppClient](#schemaappclient)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|400 response|[Error](#schemaerror)|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|403 response|[Error](#schemaerror)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|404 response|[Error](#schemaerror)|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|415 response|[Error](#schemaerror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|500 response|[Error](#schemaerror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
None, api_key
</aside>

## options__appClients_{appClientId}

`OPTIONS /appClients/{appClientId}`

> Body parameter

```json
{}
```

<h3 id="options__appclients_{appclientid}-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|appClientId|path|string|true|none|
|body|body|[Empty](#schemaempty)|true|none|

> Example responses

> 200 Response

```json
{}
```

<h3 id="options__appclients_{appclientid}-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|200 response|[Empty](#schemaempty)|

<aside class="success">
This operation does not require authentication
</aside>

## patch__appClients_{appClientId}

`PATCH /appClients/{appClientId}`

> Body parameter

```json
{
  "name": "string",
  "description": "string",
  "loginUrls": [
    "string"
  ],
  "defaultLoginUrl": "string"
}
```

<h3 id="patch__appclients_{appclientid}-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|appClientId|path|string|true|none|
|Content-Type|header|string|true|none|
|body|body|[PatchAppClientId](#schemapatchappclientid)|true|none|

> Example responses

> 200 Response

```json
{
  "hasSecret": true,
  "updatedTime": "string",
  "clientId": "string",
  "updatedBy": "string",
  "apiKey": "string",
  "logoutUrls": [
    "string"
  ],
  "description": "string",
  "callbackUrls": [
    "string"
  ],
  "loginUrls": [
    "string"
  ],
  "defaultLoginUrl": "string",
  "createdBy": "string",
  "name": "string",
  "createdTime": "string",
  "clientSecret": "string",
  "appClientId": "string"
}
```

<h3 id="patch__appclients_{appclientid}-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|200 response|[AppClient](#schemaappclient)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|400 response|[Error](#schemaerror)|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|403 response|[Error](#schemaerror)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|404 response|[Error](#schemaerror)|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|415 response|[Error](#schemaerror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|500 response|[Error](#schemaerror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
None, api_key
</aside>

## get__assets

`GET /assets`

<h3 id="get__assets-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|nextToken|query|string|false|none|
|maxResults|query|string|false|none|

> Example responses

> 200 Response

```json
{
  "assets": [
    {
      "updatedTime": "string",
      "updatedBy": "string",
      "createdBy": "string",
      "assetId": "string",
      "name": "string",
      "description": "string",
      "createdTime": "string",
      "content": "string"
    }
  ],
  "nextToken": "string"
}
```

<h3 id="get__assets-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|200 response|[Assets](#schemaassets)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|400 response|[Error](#schemaerror)|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|403 response|[Error](#schemaerror)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|404 response|[Error](#schemaerror)|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|415 response|[Error](#schemaerror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|500 response|[Error](#schemaerror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
None, api_key
</aside>

## options__assets

`OPTIONS /assets`

> Body parameter

```json
{}
```

<h3 id="options__assets-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[Empty](#schemaempty)|true|none|

> Example responses

> 200 Response

```json
{}
```

<h3 id="options__assets-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|200 response|[Empty](#schemaempty)|

<aside class="success">
This operation does not require authentication
</aside>

## post__assets

`POST /assets`

> Body parameter

```json
{
  "name": "string",
  "description": "string",
  "content": "string"
}
```

<h3 id="post__assets-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Content-Type|header|string|true|none|
|body|body|[PostAssets](#schemapostassets)|true|none|

> Example responses

> 200 Response

```json
{
  "updatedTime": "string",
  "updatedBy": "string",
  "createdBy": "string",
  "assetId": "string",
  "name": "string",
  "description": "string",
  "createdTime": "string",
  "content": "string"
}
```

<h3 id="post__assets-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|200 response|[Asset](#schemaasset)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|400 response|[Error](#schemaerror)|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|403 response|[Error](#schemaerror)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|404 response|[Error](#schemaerror)|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|415 response|[Error](#schemaerror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|500 response|[Error](#schemaerror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
None, api_key
</aside>

## delete__assets_{assetId}

`DELETE /assets/{assetId}`

<h3 id="delete__assets_{assetid}-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|assetId|path|string|true|none|

> Example responses

> 200 Response

```json
{
  "updatedTime": "string",
  "updatedBy": "string",
  "createdBy": "string",
  "assetId": "string",
  "name": "string",
  "description": "string",
  "createdTime": "string",
  "content": "string"
}
```

<h3 id="delete__assets_{assetid}-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|200 response|[Asset](#schemaasset)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|400 response|[Error](#schemaerror)|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|403 response|[Error](#schemaerror)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|404 response|[Error](#schemaerror)|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|415 response|[Error](#schemaerror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|500 response|[Error](#schemaerror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
None, api_key
</aside>

## get__assets_{assetId}

`GET /assets/{assetId}`

<h3 id="get__assets_{assetid}-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|assetId|path|string|true|none|

> Example responses

> 200 Response

```json
{
  "updatedTime": "string",
  "updatedBy": "string",
  "createdBy": "string",
  "assetId": "string",
  "name": "string",
  "description": "string",
  "createdTime": "string",
  "content": "string"
}
```

<h3 id="get__assets_{assetid}-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|200 response|[Asset](#schemaasset)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|400 response|[Error](#schemaerror)|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|403 response|[Error](#schemaerror)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|404 response|[Error](#schemaerror)|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|415 response|[Error](#schemaerror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|500 response|[Error](#schemaerror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
None, api_key
</aside>

## options__assets_{assetId}

`OPTIONS /assets/{assetId}`

> Body parameter

```json
{}
```

<h3 id="options__assets_{assetid}-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|assetId|path|string|true|none|
|body|body|[Empty](#schemaempty)|true|none|

> Example responses

> 200 Response

```json
{}
```

<h3 id="options__assets_{assetid}-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|200 response|[Empty](#schemaempty)|

<aside class="success">
This operation does not require authentication
</aside>

## patch__assets_{assetId}

`PATCH /assets/{assetId}`

> Body parameter

```json
{
  "name": "string",
  "description": "string",
  "content": "string"
}
```

<h3 id="patch__assets_{assetid}-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Content-Type|header|string|true|none|
|assetId|path|string|true|none|
|body|body|[PatchAssetId](#schemapatchassetid)|true|none|

> Example responses

> 200 Response

```json
{
  "updatedTime": "string",
  "updatedBy": "string",
  "createdBy": "string",
  "assetId": "string",
  "name": "string",
  "description": "string",
  "createdTime": "string",
  "content": "string"
}
```

<h3 id="patch__assets_{assetid}-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|200 response|[Asset](#schemaasset)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|400 response|[Error](#schemaerror)|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|403 response|[Error](#schemaerror)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|404 response|[Error](#schemaerror)|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|415 response|[Error](#schemaerror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|500 response|[Error](#schemaerror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
None, api_key
</aside>

## get__datasets

`GET /datasets`

<h3 id="get__datasets-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|nextToken|query|string|false|none|
|maxResults|query|string|false|none|

> Example responses

> 200 Response

```json
{
  "nextToken": "string",
  "datasets": [
    {
      "updatedTime": "string",
      "retentionInDays": 1825,
      "updatedBy": "string",
      "groundTruthSummary": {},
      "description": "string",
      "storageLocation": "EU",
      "version": 0,
      "createdBy": "string",
      "numberOfDocuments": 0,
      "name": "string",
      "datasetId": "string",
      "createdTime": "string",
      "containsPersonallyIdentifiableInformation": true
    }
  ]
}
```

<h3 id="get__datasets-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|200 response|[Datasets](#schemadatasets)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|400 response|[Error](#schemaerror)|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|403 response|[Error](#schemaerror)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|404 response|[Error](#schemaerror)|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|415 response|[Error](#schemaerror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|500 response|[Error](#schemaerror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
None, api_key
</aside>

## options__datasets

`OPTIONS /datasets`

> Body parameter

```json
{}
```

<h3 id="options__datasets-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[Empty](#schemaempty)|true|none|

> Example responses

> 200 Response

```json
{}
```

<h3 id="options__datasets-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|200 response|[Empty](#schemaempty)|

<aside class="success">
This operation does not require authentication
</aside>

## post__datasets

`POST /datasets`

> Body parameter

```json
{
  "retentionInDays": 1,
  "name": "string",
  "description": "string",
  "containsPersonallyIdentifiableInformation": true
}
```

<h3 id="post__datasets-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Content-Type|header|string|true|none|
|body|body|[PostDatasets](#schemapostdatasets)|true|none|

> Example responses

> 200 Response

```json
{
  "updatedTime": "string",
  "retentionInDays": 1825,
  "updatedBy": "string",
  "groundTruthSummary": {},
  "description": "string",
  "storageLocation": "EU",
  "version": 0,
  "createdBy": "string",
  "numberOfDocuments": 0,
  "name": "string",
  "datasetId": "string",
  "createdTime": "string",
  "containsPersonallyIdentifiableInformation": true
}
```

<h3 id="post__datasets-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|200 response|[Dataset](#schemadataset)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|400 response|[Error](#schemaerror)|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|403 response|[Error](#schemaerror)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|404 response|[Error](#schemaerror)|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|415 response|[Error](#schemaerror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|500 response|[Error](#schemaerror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
None, api_key
</aside>

## delete__datasets_{datasetId}

`DELETE /datasets/{datasetId}`

<h3 id="delete__datasets_{datasetid}-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|datasetId|path|string|true|none|

> Example responses

> 200 Response

```json
{
  "updatedTime": "string",
  "retentionInDays": 1825,
  "updatedBy": "string",
  "groundTruthSummary": {},
  "description": "string",
  "storageLocation": "EU",
  "version": 0,
  "createdBy": "string",
  "numberOfDocuments": 0,
  "name": "string",
  "datasetId": "string",
  "createdTime": "string",
  "containsPersonallyIdentifiableInformation": true
}
```

<h3 id="delete__datasets_{datasetid}-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|200 response|[Dataset](#schemadataset)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|400 response|[Error](#schemaerror)|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|403 response|[Error](#schemaerror)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|404 response|[Error](#schemaerror)|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|415 response|[Error](#schemaerror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|500 response|[Error](#schemaerror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
None, api_key
</aside>

## get__datasets_{datasetId}

`GET /datasets/{datasetId}`

<h3 id="get__datasets_{datasetid}-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|datasetId|path|string|true|none|

> Example responses

> 200 Response

```json
{
  "updatedTime": "string",
  "retentionInDays": 1825,
  "updatedBy": "string",
  "groundTruthSummary": {},
  "description": "string",
  "storageLocation": "EU",
  "version": 0,
  "createdBy": "string",
  "numberOfDocuments": 0,
  "name": "string",
  "datasetId": "string",
  "createdTime": "string",
  "containsPersonallyIdentifiableInformation": true
}
```

<h3 id="get__datasets_{datasetid}-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|200 response|[Dataset](#schemadataset)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|400 response|[Error](#schemaerror)|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|403 response|[Error](#schemaerror)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|404 response|[Error](#schemaerror)|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|415 response|[Error](#schemaerror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|500 response|[Error](#schemaerror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
None, api_key
</aside>

## options__datasets_{datasetId}

`OPTIONS /datasets/{datasetId}`

> Body parameter

```json
{}
```

<h3 id="options__datasets_{datasetid}-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|datasetId|path|string|true|none|
|body|body|[Empty](#schemaempty)|true|none|

> Example responses

> 200 Response

```json
{}
```

<h3 id="options__datasets_{datasetid}-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|200 response|[Empty](#schemaempty)|

<aside class="success">
This operation does not require authentication
</aside>

## patch__datasets_{datasetId}

`PATCH /datasets/{datasetId}`

> Body parameter

```json
{
  "name": "string",
  "description": "string"
}
```

<h3 id="patch__datasets_{datasetid}-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Content-Type|header|string|true|none|
|datasetId|path|string|true|none|
|body|body|[PatchDatasetId](#schemapatchdatasetid)|true|none|

> Example responses

> 200 Response

```json
{
  "updatedTime": "string",
  "retentionInDays": 1825,
  "updatedBy": "string",
  "groundTruthSummary": {},
  "description": "string",
  "storageLocation": "EU",
  "version": 0,
  "createdBy": "string",
  "numberOfDocuments": 0,
  "name": "string",
  "datasetId": "string",
  "createdTime": "string",
  "containsPersonallyIdentifiableInformation": true
}
```

<h3 id="patch__datasets_{datasetid}-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|200 response|[Dataset](#schemadataset)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|400 response|[Error](#schemaerror)|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|403 response|[Error](#schemaerror)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|404 response|[Error](#schemaerror)|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|415 response|[Error](#schemaerror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|500 response|[Error](#schemaerror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
None, api_key
</aside>

## delete__documents

`DELETE /documents`

<h3 id="delete__documents-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|consentId|query|string|false|none|
|datasetId|query|string|false|none|
|nextToken|query|string|false|none|
|maxResults|query|string|false|none|

> Example responses

> 200 Response

```json
{
  "consentId": [
    "string"
  ],
  "documents": [
    {
      "groundTruth": [
        {
          "label": "string",
          "value": "string"
        }
      ],
      "updatedTime": "string",
      "consentId": "string",
      "retentionInDays": 1,
      "updatedBy": "string",
      "createdBy": "string",
      "createdTime": "string",
      "datasetId": "string",
      "documentId": "string",
      "contentType": "application/pdf",
      "content": "string"
    }
  ],
  "nextToken": "string",
  "datasetId": [
    "string"
  ]
}
```

<h3 id="delete__documents-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|200 response|[Documents](#schemadocuments)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|400 response|[Error](#schemaerror)|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|403 response|[Error](#schemaerror)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|404 response|[Error](#schemaerror)|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|415 response|[Error](#schemaerror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|500 response|[Error](#schemaerror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
None, api_key
</aside>

## get__documents

`GET /documents`

<h3 id="get__documents-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|consentId|query|string|false|none|
|datasetId|query|string|false|none|
|nextToken|query|string|false|none|
|maxResults|query|string|false|none|

> Example responses

> 200 Response

```json
{
  "consentId": [
    "string"
  ],
  "documents": [
    {
      "groundTruth": [
        {
          "label": "string",
          "value": "string"
        }
      ],
      "updatedTime": "string",
      "consentId": "string",
      "retentionInDays": 1,
      "updatedBy": "string",
      "createdBy": "string",
      "createdTime": "string",
      "datasetId": "string",
      "documentId": "string",
      "contentType": "application/pdf",
      "content": "string"
    }
  ],
  "nextToken": "string",
  "datasetId": [
    "string"
  ]
}
```

<h3 id="get__documents-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|200 response|[Documents](#schemadocuments)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|400 response|[Error](#schemaerror)|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|403 response|[Error](#schemaerror)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|404 response|[Error](#schemaerror)|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|415 response|[Error](#schemaerror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|500 response|[Error](#schemaerror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
None, api_key
</aside>

## options__documents

`OPTIONS /documents`

> Body parameter

```json
{}
```

<h3 id="options__documents-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[Empty](#schemaempty)|true|none|

> Example responses

> 200 Response

```json
{}
```

<h3 id="options__documents-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|200 response|[Empty](#schemaempty)|

<aside class="success">
This operation does not require authentication
</aside>

## post__documents

`POST /documents`

> Body parameter

```json
{
  "groundTruth": [
    {
      "label": "string",
      "value": "string"
    }
  ],
  "consentId": "string",
  "retentionInDays": 1,
  "datasetId": "string",
  "contentType": "application/pdf",
  "content": "string"
}
```

<h3 id="post__documents-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Content-Type|header|string|true|none|
|body|body|[PostDocuments](#schemapostdocuments)|true|none|

> Example responses

> 200 Response

```json
{
  "groundTruth": [
    {
      "label": "string",
      "value": "string"
    }
  ],
  "updatedTime": "string",
  "consentId": "string",
  "retentionInDays": 1,
  "updatedBy": "string",
  "createdBy": "string",
  "createdTime": "string",
  "datasetId": "string",
  "documentId": "string",
  "contentType": "application/pdf",
  "content": "string"
}
```

<h3 id="post__documents-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|200 response|[Document](#schemadocument)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|400 response|[Error](#schemaerror)|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|403 response|[Error](#schemaerror)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|404 response|[Error](#schemaerror)|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|415 response|[Error](#schemaerror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|500 response|[Error](#schemaerror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
None, api_key
</aside>

## delete__documents_{documentId}

`DELETE /documents/{documentId}`

<h3 id="delete__documents_{documentid}-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|documentId|path|string|true|none|

> Example responses

> 200 Response

```json
{
  "groundTruth": [
    {
      "label": "string",
      "value": "string"
    }
  ],
  "updatedTime": "string",
  "consentId": "string",
  "retentionInDays": 1,
  "updatedBy": "string",
  "createdBy": "string",
  "createdTime": "string",
  "datasetId": "string",
  "documentId": "string",
  "contentType": "application/pdf",
  "content": "string"
}
```

<h3 id="delete__documents_{documentid}-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|200 response|[Document](#schemadocument)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|400 response|[Error](#schemaerror)|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|403 response|[Error](#schemaerror)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|404 response|[Error](#schemaerror)|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|415 response|[Error](#schemaerror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|500 response|[Error](#schemaerror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
None, api_key
</aside>

## get__documents_{documentId}

`GET /documents/{documentId}`

<h3 id="get__documents_{documentid}-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|documentId|path|string|true|none|

> Example responses

> 200 Response

```json
{
  "groundTruth": [
    {
      "label": "string",
      "value": "string"
    }
  ],
  "updatedTime": "string",
  "consentId": "string",
  "retentionInDays": 1,
  "updatedBy": "string",
  "createdBy": "string",
  "createdTime": "string",
  "datasetId": "string",
  "documentId": "string",
  "contentType": "application/pdf",
  "content": "string"
}
```

<h3 id="get__documents_{documentid}-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|200 response|[Document](#schemadocument)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|400 response|[Error](#schemaerror)|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|403 response|[Error](#schemaerror)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|404 response|[Error](#schemaerror)|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|415 response|[Error](#schemaerror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|500 response|[Error](#schemaerror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
None, api_key
</aside>

## options__documents_{documentId}

`OPTIONS /documents/{documentId}`

> Body parameter

```json
{}
```

<h3 id="options__documents_{documentid}-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|documentId|path|string|true|none|
|body|body|[Empty](#schemaempty)|true|none|

> Example responses

> 200 Response

```json
{}
```

<h3 id="options__documents_{documentid}-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|200 response|[Empty](#schemaempty)|

<aside class="success">
This operation does not require authentication
</aside>

## patch__documents_{documentId}

`PATCH /documents/{documentId}`

> Body parameter

```json
{
  "groundTruth": [
    {
      "label": "string",
      "value": "string"
    }
  ],
  "retentionInDays": 1,
  "datasetId": "string"
}
```

<h3 id="patch__documents_{documentid}-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Content-Type|header|string|true|none|
|documentId|path|string|true|none|
|body|body|[PatchDocumentId](#schemapatchdocumentid)|true|none|

> Example responses

> 200 Response

```json
{
  "groundTruth": [
    {
      "label": "string",
      "value": "string"
    }
  ],
  "updatedTime": "string",
  "consentId": "string",
  "retentionInDays": 1,
  "updatedBy": "string",
  "createdBy": "string",
  "createdTime": "string",
  "datasetId": "string",
  "documentId": "string",
  "contentType": "application/pdf",
  "content": "string"
}
```

<h3 id="patch__documents_{documentid}-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|200 response|[Document](#schemadocument)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|400 response|[Error](#schemaerror)|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|403 response|[Error](#schemaerror)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|404 response|[Error](#schemaerror)|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|415 response|[Error](#schemaerror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|500 response|[Error](#schemaerror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
None, api_key
</aside>

## get__logs

`GET /logs`

<h3 id="get__logs-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|workflowId|query|string|false|none|
|nextToken|query|string|false|none|
|order|query|string|false|none|
|transitionExecutionId|query|string|false|none|
|transitionId|query|string|false|none|
|maxResults|query|string|false|none|
|workflowExecutionId|query|string|false|none|

> Example responses

> 200 Response

```json
{
  "transitionId": "string",
  "nextToken": "string",
  "transitionExecutionId": "string",
  "workflowExecutionId": "string",
  "logs": [
    {
      "transitionId": "string",
      "transitionExecutionId": "string",
      "logId": "string",
      "workflowExecutionId": "string",
      "startTime": "string",
      "workflowId": "string",
      "events": [
        {}
      ]
    }
  ],
  "workflowId": "string",
  "order": "ascending"
}
```

<h3 id="get__logs-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|200 response|[Logs](#schemalogs)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|400 response|[Error](#schemaerror)|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|403 response|[Error](#schemaerror)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|404 response|[Error](#schemaerror)|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|415 response|[Error](#schemaerror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|500 response|[Error](#schemaerror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
None, api_key
</aside>

## options__logs

`OPTIONS /logs`

> Body parameter

```json
{}
```

<h3 id="options__logs-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[Empty](#schemaempty)|true|none|

> Example responses

> 200 Response

```json
{}
```

<h3 id="options__logs-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|200 response|[Empty](#schemaempty)|

<aside class="success">
This operation does not require authentication
</aside>

## get__logs_{logId}

`GET /logs/{logId}`

<h3 id="get__logs_{logid}-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|logId|path|string|true|none|

> Example responses

> 200 Response

```json
{
  "transitionId": "string",
  "transitionExecutionId": "string",
  "logId": "string",
  "workflowExecutionId": "string",
  "startTime": "string",
  "workflowId": "string",
  "events": [
    {}
  ]
}
```

<h3 id="get__logs_{logid}-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|200 response|[Log](#schemalog)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|400 response|[Error](#schemaerror)|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|403 response|[Error](#schemaerror)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|404 response|[Error](#schemaerror)|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|415 response|[Error](#schemaerror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|500 response|[Error](#schemaerror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
None, api_key
</aside>

## options__logs_{logId}

`OPTIONS /logs/{logId}`

> Body parameter

```json
{}
```

<h3 id="options__logs_{logid}-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|logId|path|string|true|none|
|body|body|[Empty](#schemaempty)|true|none|

> Example responses

> 200 Response

```json
{}
```

<h3 id="options__logs_{logid}-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|200 response|[Empty](#schemaempty)|

<aside class="success">
This operation does not require authentication
</aside>

## get__models

`GET /models`

<h3 id="get__models-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|nextToken|query|string|false|none|
|maxResults|query|string|false|none|

> Example responses

> 200 Response

```json
{
  "models": [
    {
      "updatedTime": "string",
      "updatedBy": "string",
      "modelId": "string",
      "description": "string",
      "fieldConfig": {
        "property1": {
          "description": "string",
          "type": "date",
          "maxLength": 1
        },
        "property2": {
          "description": "string",
          "type": "date",
          "maxLength": 1
        }
      },
      "preprocessConfig": {
        "maxPages": 1,
        "autoRotate": true,
        "imageQuality": "LOW"
      },
      "createdBy": "string",
      "name": "string",
      "width": 97,
      "numberOfDataBundles": 0,
      "createdTime": "string",
      "height": 97,
      "status": "active"
    }
  ],
  "nextToken": "string"
}
```

<h3 id="get__models-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|200 response|[Models](#schemamodels)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|400 response|[Error](#schemaerror)|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|403 response|[Error](#schemaerror)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|404 response|[Error](#schemaerror)|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|415 response|[Error](#schemaerror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|500 response|[Error](#schemaerror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
None, api_key
</aside>

## options__models

`OPTIONS /models`

> Body parameter

```json
{}
```

<h3 id="options__models-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[Empty](#schemaempty)|true|none|

> Example responses

> 200 Response

```json
{}
```

<h3 id="options__models-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|200 response|[Empty](#schemaempty)|

<aside class="success">
This operation does not require authentication
</aside>

## post__models

`POST /models`

> Body parameter

```json
{
  "preprocessConfig": {
    "maxPages": 1,
    "autoRotate": true,
    "imageQuality": "LOW"
  },
  "name": "string",
  "width": 97,
  "description": "string",
  "fieldConfig": {
    "property1": {
      "description": "string",
      "type": "date",
      "maxLength": 1
    },
    "property2": {
      "description": "string",
      "type": "date",
      "maxLength": 1
    }
  },
  "height": 97
}
```

<h3 id="post__models-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Content-Type|header|string|true|none|
|body|body|[PostModels](#schemapostmodels)|true|none|

> Example responses

> 200 Response

```json
{
  "updatedTime": "string",
  "updatedBy": "string",
  "modelId": "string",
  "description": "string",
  "fieldConfig": {
    "property1": {
      "description": "string",
      "type": "date",
      "maxLength": 1
    },
    "property2": {
      "description": "string",
      "type": "date",
      "maxLength": 1
    }
  },
  "preprocessConfig": {
    "maxPages": 1,
    "autoRotate": true,
    "imageQuality": "LOW"
  },
  "createdBy": "string",
  "name": "string",
  "width": 97,
  "numberOfDataBundles": 0,
  "createdTime": "string",
  "height": 97,
  "status": "active"
}
```

<h3 id="post__models-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|200 response|[Model](#schemamodel)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|400 response|[Error](#schemaerror)|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|403 response|[Error](#schemaerror)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|404 response|[Error](#schemaerror)|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|415 response|[Error](#schemaerror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|500 response|[Error](#schemaerror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
None, api_key
</aside>

## delete__models_{modelId}

`DELETE /models/{modelId}`

<h3 id="delete__models_{modelid}-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|modelId|path|string|true|none|

> Example responses

> 200 Response

```json
{
  "updatedTime": "string",
  "updatedBy": "string",
  "modelId": "string",
  "description": "string",
  "fieldConfig": {
    "property1": {
      "description": "string",
      "type": "date",
      "maxLength": 1
    },
    "property2": {
      "description": "string",
      "type": "date",
      "maxLength": 1
    }
  },
  "preprocessConfig": {
    "maxPages": 1,
    "autoRotate": true,
    "imageQuality": "LOW"
  },
  "createdBy": "string",
  "name": "string",
  "width": 97,
  "numberOfDataBundles": 0,
  "createdTime": "string",
  "height": 97,
  "status": "active"
}
```

<h3 id="delete__models_{modelid}-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|200 response|[Model](#schemamodel)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|400 response|[Error](#schemaerror)|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|403 response|[Error](#schemaerror)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|404 response|[Error](#schemaerror)|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|415 response|[Error](#schemaerror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|500 response|[Error](#schemaerror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
None, api_key
</aside>

## get__models_{modelId}

`GET /models/{modelId}`

<h3 id="get__models_{modelid}-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|modelId|path|string|true|none|

> Example responses

> 200 Response

```json
{
  "updatedTime": "string",
  "updatedBy": "string",
  "modelId": "string",
  "description": "string",
  "fieldConfig": {
    "property1": {
      "description": "string",
      "type": "date",
      "maxLength": 1
    },
    "property2": {
      "description": "string",
      "type": "date",
      "maxLength": 1
    }
  },
  "preprocessConfig": {
    "maxPages": 1,
    "autoRotate": true,
    "imageQuality": "LOW"
  },
  "createdBy": "string",
  "name": "string",
  "width": 97,
  "numberOfDataBundles": 0,
  "createdTime": "string",
  "height": 97,
  "status": "active"
}
```

<h3 id="get__models_{modelid}-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|200 response|[Model](#schemamodel)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|400 response|[Error](#schemaerror)|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|403 response|[Error](#schemaerror)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|404 response|[Error](#schemaerror)|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|415 response|[Error](#schemaerror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|500 response|[Error](#schemaerror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
None, api_key
</aside>

## options__models_{modelId}

`OPTIONS /models/{modelId}`

> Body parameter

```json
{}
```

<h3 id="options__models_{modelid}-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|modelId|path|string|true|none|
|body|body|[Empty](#schemaempty)|true|none|

> Example responses

> 200 Response

```json
{}
```

<h3 id="options__models_{modelid}-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|200 response|[Empty](#schemaempty)|

<aside class="success">
This operation does not require authentication
</aside>

## patch__models_{modelId}

`PATCH /models/{modelId}`

> Body parameter

```json
{
  "preprocessConfig": {
    "maxPages": 1,
    "autoRotate": true,
    "imageQuality": "LOW"
  },
  "width": 97,
  "name": "string",
  "description": "string",
  "fieldConfig": {
    "property1": {
      "description": "string",
      "type": "date",
      "maxLength": 1
    },
    "property2": {
      "description": "string",
      "type": "date",
      "maxLength": 1
    }
  },
  "height": 97,
  "status": "active"
}
```

<h3 id="patch__models_{modelid}-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Content-Type|header|string|true|none|
|modelId|path|string|true|none|
|body|body|[PatchModelId](#schemapatchmodelid)|true|none|

> Example responses

> 200 Response

```json
{
  "updatedTime": "string",
  "updatedBy": "string",
  "modelId": "string",
  "description": "string",
  "fieldConfig": {
    "property1": {
      "description": "string",
      "type": "date",
      "maxLength": 1
    },
    "property2": {
      "description": "string",
      "type": "date",
      "maxLength": 1
    }
  },
  "preprocessConfig": {
    "maxPages": 1,
    "autoRotate": true,
    "imageQuality": "LOW"
  },
  "createdBy": "string",
  "name": "string",
  "width": 97,
  "numberOfDataBundles": 0,
  "createdTime": "string",
  "height": 97,
  "status": "active"
}
```

<h3 id="patch__models_{modelid}-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|200 response|[Model](#schemamodel)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|400 response|[Error](#schemaerror)|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|403 response|[Error](#schemaerror)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|404 response|[Error](#schemaerror)|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|415 response|[Error](#schemaerror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|500 response|[Error](#schemaerror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
None, api_key
</aside>

## get__models_{modelId}_dataBundles

`GET /models/{modelId}/dataBundles`

<h3 id="get__models_{modelid}_databundles-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|modelId|path|string|true|none|
|status|query|string|false|none|
|nextToken|query|string|false|none|
|maxResults|query|string|false|none|

> Example responses

> 200 Response

```json
{
  "nextToken": "string",
  "dataBundles": [
    {
      "summary": {},
      "updatedTime": "string",
      "updatedBy": "string",
      "modelId": "string",
      "createdBy": "string",
      "dataBundleId": "string",
      "name": "string",
      "description": "string",
      "createdTime": "string",
      "datasets": [
        {
          "updatedTime": "string",
          "retentionInDays": 1825,
          "updatedBy": "string",
          "groundTruthSummary": {},
          "description": "string",
          "storageLocation": "EU",
          "version": 0,
          "createdBy": "string",
          "numberOfDocuments": 0,
          "name": "string",
          "datasetId": "string",
          "createdTime": "string",
          "containsPersonallyIdentifiableInformation": true
        }
      ],
      "status": "processing"
    }
  ],
  "status": [
    "processing"
  ]
}
```

<h3 id="get__models_{modelid}_databundles-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|200 response|[DataBundles](#schemadatabundles)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|400 response|[Error](#schemaerror)|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|403 response|[Error](#schemaerror)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|404 response|[Error](#schemaerror)|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|415 response|[Error](#schemaerror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|500 response|[Error](#schemaerror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
None, api_key
</aside>

## options__models_{modelId}_dataBundles

`OPTIONS /models/{modelId}/dataBundles`

> Body parameter

```json
{}
```

<h3 id="options__models_{modelid}_databundles-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|modelId|path|string|true|none|
|body|body|[Empty](#schemaempty)|true|none|

> Example responses

> 200 Response

```json
{}
```

<h3 id="options__models_{modelid}_databundles-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|200 response|[Empty](#schemaempty)|

<aside class="success">
This operation does not require authentication
</aside>

## post__models_{modelId}_dataBundles

`POST /models/{modelId}/dataBundles`

> Body parameter

```json
{
  "datasetIds": [
    "string"
  ],
  "name": "string",
  "description": "string"
}
```

<h3 id="post__models_{modelid}_databundles-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Content-Type|header|string|true|none|
|modelId|path|string|true|none|
|body|body|[PostDataBundles](#schemapostdatabundles)|true|none|

> Example responses

> 200 Response

```json
{
  "summary": {},
  "updatedTime": "string",
  "updatedBy": "string",
  "modelId": "string",
  "createdBy": "string",
  "dataBundleId": "string",
  "name": "string",
  "description": "string",
  "createdTime": "string",
  "datasets": [
    {
      "updatedTime": "string",
      "retentionInDays": 1825,
      "updatedBy": "string",
      "groundTruthSummary": {},
      "description": "string",
      "storageLocation": "EU",
      "version": 0,
      "createdBy": "string",
      "numberOfDocuments": 0,
      "name": "string",
      "datasetId": "string",
      "createdTime": "string",
      "containsPersonallyIdentifiableInformation": true
    }
  ],
  "status": "processing"
}
```

<h3 id="post__models_{modelid}_databundles-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|200 response|[DataBundle](#schemadatabundle)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|400 response|[Error](#schemaerror)|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|403 response|[Error](#schemaerror)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|404 response|[Error](#schemaerror)|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|415 response|[Error](#schemaerror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|500 response|[Error](#schemaerror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
None, api_key
</aside>

## delete__models_{modelId}_dataBundles_{dataBundleId}

`DELETE /models/{modelId}/dataBundles/{dataBundleId}`

<h3 id="delete__models_{modelid}_databundles_{databundleid}-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|dataBundleId|path|string|true|none|
|modelId|path|string|true|none|

> Example responses

> 200 Response

```json
{
  "summary": {},
  "updatedTime": "string",
  "updatedBy": "string",
  "modelId": "string",
  "createdBy": "string",
  "dataBundleId": "string",
  "name": "string",
  "description": "string",
  "createdTime": "string",
  "datasets": [
    {
      "updatedTime": "string",
      "retentionInDays": 1825,
      "updatedBy": "string",
      "groundTruthSummary": {},
      "description": "string",
      "storageLocation": "EU",
      "version": 0,
      "createdBy": "string",
      "numberOfDocuments": 0,
      "name": "string",
      "datasetId": "string",
      "createdTime": "string",
      "containsPersonallyIdentifiableInformation": true
    }
  ],
  "status": "processing"
}
```

<h3 id="delete__models_{modelid}_databundles_{databundleid}-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|200 response|[DataBundle](#schemadatabundle)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|400 response|[Error](#schemaerror)|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|403 response|[Error](#schemaerror)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|404 response|[Error](#schemaerror)|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|415 response|[Error](#schemaerror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|500 response|[Error](#schemaerror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
None, api_key
</aside>

## options__models_{modelId}_dataBundles_{dataBundleId}

`OPTIONS /models/{modelId}/dataBundles/{dataBundleId}`

> Body parameter

```json
{}
```

<h3 id="options__models_{modelid}_databundles_{databundleid}-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|dataBundleId|path|string|true|none|
|modelId|path|string|true|none|
|body|body|[Empty](#schemaempty)|true|none|

> Example responses

> 200 Response

```json
{}
```

<h3 id="options__models_{modelid}_databundles_{databundleid}-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|200 response|[Empty](#schemaempty)|

<aside class="success">
This operation does not require authentication
</aside>

## patch__models_{modelId}_dataBundles_{dataBundleId}

`PATCH /models/{modelId}/dataBundles/{dataBundleId}`

> Body parameter

```json
{
  "name": "string",
  "description": "string"
}
```

<h3 id="patch__models_{modelid}_databundles_{databundleid}-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|dataBundleId|path|string|true|none|
|Content-Type|header|string|true|none|
|modelId|path|string|true|none|
|body|body|[PatchDataBundleId](#schemapatchdatabundleid)|true|none|

> Example responses

> 200 Response

```json
{
  "summary": {},
  "updatedTime": "string",
  "updatedBy": "string",
  "modelId": "string",
  "createdBy": "string",
  "dataBundleId": "string",
  "name": "string",
  "description": "string",
  "createdTime": "string",
  "datasets": [
    {
      "updatedTime": "string",
      "retentionInDays": 1825,
      "updatedBy": "string",
      "groundTruthSummary": {},
      "description": "string",
      "storageLocation": "EU",
      "version": 0,
      "createdBy": "string",
      "numberOfDocuments": 0,
      "name": "string",
      "datasetId": "string",
      "createdTime": "string",
      "containsPersonallyIdentifiableInformation": true
    }
  ],
  "status": "processing"
}
```

<h3 id="patch__models_{modelid}_databundles_{databundleid}-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|200 response|[DataBundle](#schemadatabundle)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|400 response|[Error](#schemaerror)|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|403 response|[Error](#schemaerror)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|404 response|[Error](#schemaerror)|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|415 response|[Error](#schemaerror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|500 response|[Error](#schemaerror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
None, api_key
</aside>

## options__organizations

`OPTIONS /organizations`

> Body parameter

```json
{}
```

<h3 id="options__organizations-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[Empty](#schemaempty)|true|none|

> Example responses

> 200 Response

```json
{}
```

<h3 id="options__organizations-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|200 response|[Empty](#schemaempty)|

<aside class="success">
This operation does not require authentication
</aside>

## get__organizations_{organizationId}

`GET /organizations/{organizationId}`

<h3 id="get__organizations_{organizationid}-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|organizationId|path|string|true|none|

> Example responses

> 200 Response

```json
{
  "numberOfWorkflowsCreated": 0,
  "monthlyNumberOfWorkflowExecutionsCreated": 0,
  "description": "string",
  "numberOfUsersAllowed": 0,
  "monthlyNumberOfPredictionsAllowed": 0,
  "numberOfDatasetsAllowed": 0,
  "monthlyNumberOfDataBundlesAllowed": 0,
  "organizationId": "string",
  "numberOfModelsCreated": 0,
  "numberOfTransitionsCreated": 0,
  "monthlyNumberOfTransitionExecutionsAllowed": 0,
  "monthlyNumberOfDocumentsAllowed": 0,
  "numberOfSecretsAllowed": 0,
  "monthlyUsageSummary": {},
  "numberOfAppClientsCreated": 0,
  "numberOfAssetsCreated": 0,
  "updatedTime": "string",
  "numberOfWorkflowsAllowed": 0,
  "updatedBy": "string",
  "monthlyNumberOfWorkflowExecutionsAllowed": 0,
  "monthlyNumberOfDataBundlesCreated": 0,
  "numberOfUsersCreated": 0,
  "monthlyNumberOfPredictionsCreated": 0,
  "numberOfDatasetsCreated": 0,
  "numberOfTransitionsAllowed": 0,
  "monthlyNumberOfTransitionExecutionsCreated": 0,
  "numberOfModelsAllowed": 0,
  "monthlyNumberOfDocumentsCreated": 0,
  "numberOfSecretsCreated": 0,
  "name": "string",
  "numberOfAppClientsAllowed": 0,
  "numberOfAssetsAllowed": 0
}
```

<h3 id="get__organizations_{organizationid}-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|200 response|[Organization](#schemaorganization)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|400 response|[Error](#schemaerror)|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|403 response|[Error](#schemaerror)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|404 response|[Error](#schemaerror)|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|415 response|[Error](#schemaerror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|500 response|[Error](#schemaerror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
None, api_key
</aside>

## options__organizations_{organizationId}

`OPTIONS /organizations/{organizationId}`

> Body parameter

```json
{}
```

<h3 id="options__organizations_{organizationid}-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|organizationId|path|string|true|none|
|body|body|[Empty](#schemaempty)|true|none|

> Example responses

> 200 Response

```json
{}
```

<h3 id="options__organizations_{organizationid}-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|200 response|[Empty](#schemaempty)|

<aside class="success">
This operation does not require authentication
</aside>

## patch__organizations_{organizationId}

`PATCH /organizations/{organizationId}`

> Body parameter

```json
{
  "name": "string",
  "description": "string"
}
```

<h3 id="patch__organizations_{organizationid}-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Content-Type|header|string|true|none|
|organizationId|path|string|true|none|
|body|body|[PatchOrganizationId](#schemapatchorganizationid)|true|none|

> Example responses

> 200 Response

```json
{
  "numberOfWorkflowsCreated": 0,
  "monthlyNumberOfWorkflowExecutionsCreated": 0,
  "description": "string",
  "numberOfUsersAllowed": 0,
  "monthlyNumberOfPredictionsAllowed": 0,
  "numberOfDatasetsAllowed": 0,
  "monthlyNumberOfDataBundlesAllowed": 0,
  "organizationId": "string",
  "numberOfModelsCreated": 0,
  "numberOfTransitionsCreated": 0,
  "monthlyNumberOfTransitionExecutionsAllowed": 0,
  "monthlyNumberOfDocumentsAllowed": 0,
  "numberOfSecretsAllowed": 0,
  "monthlyUsageSummary": {},
  "numberOfAppClientsCreated": 0,
  "numberOfAssetsCreated": 0,
  "updatedTime": "string",
  "numberOfWorkflowsAllowed": 0,
  "updatedBy": "string",
  "monthlyNumberOfWorkflowExecutionsAllowed": 0,
  "monthlyNumberOfDataBundlesCreated": 0,
  "numberOfUsersCreated": 0,
  "monthlyNumberOfPredictionsCreated": 0,
  "numberOfDatasetsCreated": 0,
  "numberOfTransitionsAllowed": 0,
  "monthlyNumberOfTransitionExecutionsCreated": 0,
  "numberOfModelsAllowed": 0,
  "monthlyNumberOfDocumentsCreated": 0,
  "numberOfSecretsCreated": 0,
  "name": "string",
  "numberOfAppClientsAllowed": 0,
  "numberOfAssetsAllowed": 0
}
```

<h3 id="patch__organizations_{organizationid}-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|200 response|[Organization](#schemaorganization)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|400 response|[Error](#schemaerror)|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|403 response|[Error](#schemaerror)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|404 response|[Error](#schemaerror)|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|415 response|[Error](#schemaerror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|500 response|[Error](#schemaerror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
None, api_key
</aside>

## get__predictions

`GET /predictions`

<h3 id="get__predictions-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|nextToken|query|string|false|none|
|maxResults|query|string|false|none|

> Example responses

> 200 Response

```json
{
  "nextToken": "string",
  "predictions": [
    {
      "modelId": "string",
      "inferenceTime": 0,
      "documentId": "string",
      "predictionId": "string",
      "predictions": [
        {
          "confidence": 1,
          "label": "string",
          "value": "string"
        }
      ],
      "timestamp": 1
    }
  ]
}
```

<h3 id="get__predictions-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|200 response|[Predictions](#schemapredictions)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|400 response|[Error](#schemaerror)|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|403 response|[Error](#schemaerror)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|404 response|[Error](#schemaerror)|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|415 response|[Error](#schemaerror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|500 response|[Error](#schemaerror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
None, api_key
</aside>

## options__predictions

`OPTIONS /predictions`

> Body parameter

```json
{}
```

<h3 id="options__predictions-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[Empty](#schemaempty)|true|none|

> Example responses

> 200 Response

```json
{}
```

<h3 id="options__predictions-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|200 response|[Empty](#schemaempty)|

<aside class="success">
This operation does not require authentication
</aside>

## post__predictions

`POST /predictions`

> Body parameter

```json
{
  "modelId": "string",
  "maxPages": 1,
  "documentId": "string",
  "autoRotate": true,
  "imageQuality": "LOW"
}
```

<h3 id="post__predictions-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Content-Type|header|string|true|none|
|body|body|[PostPredictions](#schemapostpredictions)|true|none|

> Example responses

> 200 Response

```json
{
  "modelId": "string",
  "inferenceTime": 0,
  "documentId": "string",
  "predictionId": "string",
  "predictions": [
    {
      "confidence": 1,
      "label": "string",
      "value": "string"
    }
  ],
  "timestamp": 1
}
```

<h3 id="post__predictions-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|200 response|[Prediction](#schemaprediction)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|400 response|[Error](#schemaerror)|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|403 response|[Error](#schemaerror)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|404 response|[Error](#schemaerror)|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|415 response|[Error](#schemaerror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|500 response|[Error](#schemaerror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
None, api_key
</aside>

## get__secrets

`GET /secrets`

<h3 id="get__secrets-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|nextToken|query|string|false|none|
|maxResults|query|string|false|none|

> Example responses

> 200 Response

```json
{
  "nextToken": "string",
  "secrets": [
    {
      "updatedTime": "string",
      "updatedBy": "string",
      "createdBy": "string",
      "name": "string",
      "secretId": "string",
      "createdTime": "string",
      "description": "string"
    }
  ]
}
```

<h3 id="get__secrets-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|200 response|[Secrets](#schemasecrets)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|400 response|[Error](#schemaerror)|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|403 response|[Error](#schemaerror)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|404 response|[Error](#schemaerror)|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|415 response|[Error](#schemaerror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|500 response|[Error](#schemaerror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
None, api_key
</aside>

## options__secrets

`OPTIONS /secrets`

> Body parameter

```json
{}
```

<h3 id="options__secrets-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[Empty](#schemaempty)|true|none|

> Example responses

> 200 Response

```json
{}
```

<h3 id="options__secrets-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|200 response|[Empty](#schemaempty)|

<aside class="success">
This operation does not require authentication
</aside>

## post__secrets

`POST /secrets`

> Body parameter

```json
{
  "data": {},
  "name": "string",
  "description": "string"
}
```

<h3 id="post__secrets-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Content-Type|header|string|true|none|
|body|body|[PostSecrets](#schemapostsecrets)|true|none|

> Example responses

> 200 Response

```json
{
  "updatedTime": "string",
  "updatedBy": "string",
  "createdBy": "string",
  "name": "string",
  "secretId": "string",
  "createdTime": "string",
  "description": "string"
}
```

<h3 id="post__secrets-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|200 response|[Secret](#schemasecret)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|400 response|[Error](#schemaerror)|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|403 response|[Error](#schemaerror)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|404 response|[Error](#schemaerror)|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|415 response|[Error](#schemaerror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|500 response|[Error](#schemaerror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
None, api_key
</aside>

## delete__secrets_{secretId}

`DELETE /secrets/{secretId}`

<h3 id="delete__secrets_{secretid}-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|secretId|path|string|true|none|

> Example responses

> 200 Response

```json
{
  "updatedTime": "string",
  "updatedBy": "string",
  "createdBy": "string",
  "name": "string",
  "secretId": "string",
  "createdTime": "string",
  "description": "string"
}
```

<h3 id="delete__secrets_{secretid}-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|200 response|[Secret](#schemasecret)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|400 response|[Error](#schemaerror)|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|403 response|[Error](#schemaerror)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|404 response|[Error](#schemaerror)|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|415 response|[Error](#schemaerror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|500 response|[Error](#schemaerror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
None, api_key
</aside>

## options__secrets_{secretId}

`OPTIONS /secrets/{secretId}`

> Body parameter

```json
{}
```

<h3 id="options__secrets_{secretid}-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|secretId|path|string|true|none|
|body|body|[Empty](#schemaempty)|true|none|

> Example responses

> 200 Response

```json
{}
```

<h3 id="options__secrets_{secretid}-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|200 response|[Empty](#schemaempty)|

<aside class="success">
This operation does not require authentication
</aside>

## patch__secrets_{secretId}

`PATCH /secrets/{secretId}`

> Body parameter

```json
{
  "data": {},
  "name": "string",
  "description": "string"
}
```

<h3 id="patch__secrets_{secretid}-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Content-Type|header|string|true|none|
|secretId|path|string|true|none|
|body|body|[PatchSecretId](#schemapatchsecretid)|true|none|

> Example responses

> 200 Response

```json
{
  "updatedTime": "string",
  "updatedBy": "string",
  "createdBy": "string",
  "name": "string",
  "secretId": "string",
  "createdTime": "string",
  "description": "string"
}
```

<h3 id="patch__secrets_{secretid}-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|200 response|[Secret](#schemasecret)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|400 response|[Error](#schemaerror)|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|403 response|[Error](#schemaerror)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|404 response|[Error](#schemaerror)|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|415 response|[Error](#schemaerror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|500 response|[Error](#schemaerror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
None, api_key
</aside>

## options__signup

`OPTIONS /signup`

> Body parameter

```json
{}
```

<h3 id="options__signup-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[Empty](#schemaempty)|true|none|

> Example responses

> 200 Response

```json
{}
```

<h3 id="options__signup-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|200 response|[Empty](#schemaempty)|

<aside class="success">
This operation does not require authentication
</aside>

## post__signup

`POST /signup`

> Body parameter

```json
{
  "password": "string",
  "reCaptchaResponse": "string",
  "name": "string",
  "email": "string"
}
```

<h3 id="post__signup-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Content-Type|header|string|true|none|
|body|body|[PostSignUp](#schemapostsignup)|true|none|

> Example responses

> 200 Response

```json
{
  "clientId": "string",
  "username": "string"
}
```

<h3 id="post__signup-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|200 response|[SignUp](#schemasignup)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|400 response|[Error](#schemaerror)|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|403 response|[Error](#schemaerror)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|404 response|[Error](#schemaerror)|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|415 response|[Error](#schemaerror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|500 response|[Error](#schemaerror)|

<aside class="success">
This operation does not require authentication
</aside>

## get__transitions

`GET /transitions`

<h3 id="get__transitions-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|transitionType|query|string|false|none|
|nextToken|query|string|false|none|
|maxResults|query|string|false|none|

> Example responses

> 200 Response

```json
{
  "nextToken": "string",
  "transitions": [
    {
      "updatedTime": "string",
      "updatedBy": "string",
      "transitionId": "string",
      "description": "string",
      "inputJsonSchema": {},
      "timeoutInSeconds": 60,
      "outputJsonSchema": {},
      "assets": {
        "jsRemoteComponent": "string",
        "property1": "string",
        "property2": "string"
      },
      "createdBy": "string",
      "name": "string",
      "createdTime": "string",
      "transitionType": "docker",
      "parameters": {}
    }
  ],
  "transitionType": [
    "docker"
  ]
}
```

<h3 id="get__transitions-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|200 response|[Transitions](#schematransitions)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|400 response|[Error](#schemaerror)|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|403 response|[Error](#schemaerror)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|404 response|[Error](#schemaerror)|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|415 response|[Error](#schemaerror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|500 response|[Error](#schemaerror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
None, api_key
</aside>

## options__transitions

`OPTIONS /transitions`

> Body parameter

```json
{}
```

<h3 id="options__transitions-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[Empty](#schemaempty)|true|none|

> Example responses

> 200 Response

```json
{}
```

<h3 id="options__transitions-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|200 response|[Empty](#schemaempty)|

<aside class="success">
This operation does not require authentication
</aside>

## post__transitions

`POST /transitions`

> Body parameter

```json
{
  "outputJsonSchema": {},
  "name": "string",
  "description": "string",
  "transitionType": "docker",
  "inputJsonSchema": {},
  "parameters": {
    "environmentSecrets": [
      "string"
    ],
    "environment": {
      "property1": "string",
      "property2": "string"
    },
    "memory": 512,
    "imageUrl": "string",
    "secretId": "string",
    "cpu": 256
  },
  "timeoutInSeconds": 60
}
```

<h3 id="post__transitions-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Content-Type|header|string|true|none|
|body|body|[PostTransitions](#schemaposttransitions)|true|none|

> Example responses

> 200 Response

```json
{
  "updatedTime": "string",
  "updatedBy": "string",
  "transitionId": "string",
  "description": "string",
  "inputJsonSchema": {},
  "timeoutInSeconds": 60,
  "outputJsonSchema": {},
  "assets": {
    "jsRemoteComponent": "string",
    "property1": "string",
    "property2": "string"
  },
  "createdBy": "string",
  "name": "string",
  "createdTime": "string",
  "transitionType": "docker",
  "parameters": {}
}
```

<h3 id="post__transitions-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|200 response|[Transition](#schematransition)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|400 response|[Error](#schemaerror)|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|403 response|[Error](#schemaerror)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|404 response|[Error](#schemaerror)|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|415 response|[Error](#schemaerror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|500 response|[Error](#schemaerror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
None, api_key
</aside>

## delete__transitions_{transitionId}

`DELETE /transitions/{transitionId}`

<h3 id="delete__transitions_{transitionid}-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|transitionId|path|string|true|none|

> Example responses

> 200 Response

```json
{
  "updatedTime": "string",
  "updatedBy": "string",
  "transitionId": "string",
  "description": "string",
  "inputJsonSchema": {},
  "timeoutInSeconds": 60,
  "outputJsonSchema": {},
  "assets": {
    "jsRemoteComponent": "string",
    "property1": "string",
    "property2": "string"
  },
  "createdBy": "string",
  "name": "string",
  "createdTime": "string",
  "transitionType": "docker",
  "parameters": {}
}
```

<h3 id="delete__transitions_{transitionid}-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|200 response|[Transition](#schematransition)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|400 response|[Error](#schemaerror)|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|403 response|[Error](#schemaerror)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|404 response|[Error](#schemaerror)|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|415 response|[Error](#schemaerror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|500 response|[Error](#schemaerror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
None, api_key
</aside>

## get__transitions_{transitionId}

`GET /transitions/{transitionId}`

<h3 id="get__transitions_{transitionid}-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|transitionId|path|string|true|none|

> Example responses

> 200 Response

```json
{
  "updatedTime": "string",
  "updatedBy": "string",
  "transitionId": "string",
  "description": "string",
  "inputJsonSchema": {},
  "timeoutInSeconds": 60,
  "outputJsonSchema": {},
  "assets": {
    "jsRemoteComponent": "string",
    "property1": "string",
    "property2": "string"
  },
  "createdBy": "string",
  "name": "string",
  "createdTime": "string",
  "transitionType": "docker",
  "parameters": {}
}
```

<h3 id="get__transitions_{transitionid}-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|200 response|[Transition](#schematransition)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|400 response|[Error](#schemaerror)|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|403 response|[Error](#schemaerror)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|404 response|[Error](#schemaerror)|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|415 response|[Error](#schemaerror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|500 response|[Error](#schemaerror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
None, api_key
</aside>

## options__transitions_{transitionId}

`OPTIONS /transitions/{transitionId}`

> Body parameter

```json
{}
```

<h3 id="options__transitions_{transitionid}-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|transitionId|path|string|true|none|
|body|body|[Empty](#schemaempty)|true|none|

> Example responses

> 200 Response

```json
{}
```

<h3 id="options__transitions_{transitionid}-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|200 response|[Empty](#schemaempty)|

<aside class="success">
This operation does not require authentication
</aside>

## patch__transitions_{transitionId}

`PATCH /transitions/{transitionId}`

> Body parameter

```json
{
  "environmentSecrets": [
    "string"
  ],
  "environment": {
    "property1": "string",
    "property2": "string"
  },
  "outputJsonSchema": {},
  "assets": {
    "jsRemoteComponent": "string",
    "property1": "string",
    "property2": "string"
  },
  "name": "string",
  "description": "string",
  "inputJsonSchema": {}
}
```

<h3 id="patch__transitions_{transitionid}-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Content-Type|header|string|true|none|
|transitionId|path|string|true|none|
|body|body|[PatchTransitionId](#schemapatchtransitionid)|true|none|

> Example responses

> 200 Response

```json
{
  "updatedTime": "string",
  "updatedBy": "string",
  "transitionId": "string",
  "description": "string",
  "inputJsonSchema": {},
  "timeoutInSeconds": 60,
  "outputJsonSchema": {},
  "assets": {
    "jsRemoteComponent": "string",
    "property1": "string",
    "property2": "string"
  },
  "createdBy": "string",
  "name": "string",
  "createdTime": "string",
  "transitionType": "docker",
  "parameters": {}
}
```

<h3 id="patch__transitions_{transitionid}-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|200 response|[Transition](#schematransition)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|400 response|[Error](#schemaerror)|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|403 response|[Error](#schemaerror)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|404 response|[Error](#schemaerror)|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|415 response|[Error](#schemaerror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|500 response|[Error](#schemaerror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
None, api_key
</aside>

## get__transitions_{transitionId}_executions

`GET /transitions/{transitionId}/executions`

<h3 id="get__transitions_{transitionid}_executions-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|nextToken|query|string|false|none|
|order|query|string|false|none|
|executionId|query|string|false|none|
|transitionId|path|string|true|none|
|status|query|string|false|none|
|maxResults|query|string|false|none|
|sortBy|query|string|false|none|

> Example responses

> 200 Response

```json
{
  "executions": [
    {
      "executionId": "string",
      "input": {},
      "transitionId": "string",
      "startTime": "string",
      "logId": "string",
      "endTime": "string",
      "completedBy": "string",
      "status": "running"
    }
  ],
  "transitionId": "string",
  "nextToken": "string",
  "status": [
    "running"
  ]
}
```

<h3 id="get__transitions_{transitionid}_executions-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|200 response|[TransitionExecutions](#schematransitionexecutions)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|400 response|[Error](#schemaerror)|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|403 response|[Error](#schemaerror)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|404 response|[Error](#schemaerror)|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|415 response|[Error](#schemaerror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|500 response|[Error](#schemaerror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
None, api_key
</aside>

## options__transitions_{transitionId}_executions

`OPTIONS /transitions/{transitionId}/executions`

> Body parameter

```json
{}
```

<h3 id="options__transitions_{transitionid}_executions-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|transitionId|path|string|true|none|
|body|body|[Empty](#schemaempty)|true|none|

> Example responses

> 200 Response

```json
{}
```

<h3 id="options__transitions_{transitionid}_executions-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|200 response|[Empty](#schemaempty)|

<aside class="success">
This operation does not require authentication
</aside>

## post__transitions_{transitionId}_executions

`POST /transitions/{transitionId}/executions`

> Body parameter

```json
{}
```

<h3 id="post__transitions_{transitionid}_executions-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Content-Type|header|string|true|none|
|transitionId|path|string|true|none|
|body|body|[PostTransitionExecution](#schemaposttransitionexecution)|true|none|

> Example responses

> 200 Response

```json
{
  "executionId": "string",
  "input": {},
  "transitionId": "string",
  "startTime": "string",
  "logId": "string",
  "endTime": "string",
  "completedBy": "string",
  "status": "running"
}
```

<h3 id="post__transitions_{transitionid}_executions-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|200 response|[TransitionExecution](#schematransitionexecution)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|400 response|[Error](#schemaerror)|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|403 response|[Error](#schemaerror)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|404 response|[Error](#schemaerror)|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|415 response|[Error](#schemaerror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|500 response|[Error](#schemaerror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
None, api_key
</aside>

## get__transitions_{transitionId}_executions_{executionId}

`GET /transitions/{transitionId}/executions/{executionId}`

<h3 id="get__transitions_{transitionid}_executions_{executionid}-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|transitionId|path|string|true|none|
|executionId|path|string|true|none|

> Example responses

> 200 Response

```json
{
  "executionId": "string",
  "input": {},
  "transitionId": "string",
  "startTime": "string",
  "logId": "string",
  "endTime": "string",
  "completedBy": "string",
  "status": "running"
}
```

<h3 id="get__transitions_{transitionid}_executions_{executionid}-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|200 response|[TransitionExecution](#schematransitionexecution)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|400 response|[Error](#schemaerror)|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|403 response|[Error](#schemaerror)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|404 response|[Error](#schemaerror)|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|415 response|[Error](#schemaerror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|500 response|[Error](#schemaerror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
None, api_key
</aside>

## options__transitions_{transitionId}_executions_{executionId}

`OPTIONS /transitions/{transitionId}/executions/{executionId}`

> Body parameter

```json
{}
```

<h3 id="options__transitions_{transitionid}_executions_{executionid}-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|transitionId|path|string|true|none|
|executionId|path|string|true|none|
|body|body|[Empty](#schemaempty)|true|none|

> Example responses

> 200 Response

```json
{}
```

<h3 id="options__transitions_{transitionid}_executions_{executionid}-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|200 response|[Empty](#schemaempty)|

<aside class="success">
This operation does not require authentication
</aside>

## patch__transitions_{transitionId}_executions_{executionId}

`PATCH /transitions/{transitionId}/executions/{executionId}`

> Body parameter

```json
{
  "status": "succeeded"
}
```

<h3 id="patch__transitions_{transitionid}_executions_{executionid}-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Content-Type|header|string|true|none|
|transitionId|path|string|true|none|
|executionId|path|string|true|none|
|body|body|[PatchTransistionExecutionId](#schemapatchtransistionexecutionid)|true|none|

> Example responses

> 200 Response

```json
{
  "executionId": "string",
  "input": {},
  "transitionId": "string",
  "startTime": "string",
  "logId": "string",
  "endTime": "string",
  "completedBy": "string",
  "status": "running"
}
```

<h3 id="patch__transitions_{transitionid}_executions_{executionid}-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|200 response|[TransitionExecution](#schematransitionexecution)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|400 response|[Error](#schemaerror)|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|403 response|[Error](#schemaerror)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|404 response|[Error](#schemaerror)|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|415 response|[Error](#schemaerror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|500 response|[Error](#schemaerror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
None, api_key
</aside>

## options__transitions_{transitionId}_executions_{executionId}_heartbeats

`OPTIONS /transitions/{transitionId}/executions/{executionId}/heartbeats`

> Body parameter

```json
{}
```

<h3 id="options__transitions_{transitionid}_executions_{executionid}_heartbeats-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|transitionId|path|string|true|none|
|executionId|path|string|true|none|
|body|body|[Empty](#schemaempty)|true|none|

> Example responses

> 200 Response

```json
{}
```

<h3 id="options__transitions_{transitionid}_executions_{executionid}_heartbeats-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|200 response|[Empty](#schemaempty)|

<aside class="success">
This operation does not require authentication
</aside>

## post__transitions_{transitionId}_executions_{executionId}_heartbeats

`POST /transitions/{transitionId}/executions/{executionId}/heartbeats`

> Body parameter

```json
{}
```

<h3 id="post__transitions_{transitionid}_executions_{executionid}_heartbeats-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Content-Type|header|string|true|none|
|transitionId|path|string|true|none|
|executionId|path|string|true|none|
|body|body|[PostHeartbeats](#schemapostheartbeats)|true|none|

> Example responses

> 204 Response

```json
{}
```

<h3 id="post__transitions_{transitionid}_executions_{executionid}_heartbeats-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|204|[No Content](https://tools.ietf.org/html/rfc7231#section-6.3.5)|204 response|[Empty](#schemaempty)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|400 response|[Error](#schemaerror)|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|403 response|[Error](#schemaerror)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|404 response|[Error](#schemaerror)|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|415 response|[Error](#schemaerror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|500 response|[Error](#schemaerror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
None, api_key
</aside>

## get__users

`GET /users`

<h3 id="get__users-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|nextToken|query|string|false|none|
|maxResults|query|string|false|none|

> Example responses

> 200 Response

```json
{
  "nextToken": "string",
  "users": [
    {
      "updatedTime": "string",
      "updatedBy": "string",
      "createdBy": "string",
      "name": "string",
      "createdTime": "string",
      "avatar": "string",
      "userId": "string",
      "email": "string"
    }
  ]
}
```

<h3 id="get__users-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|200 response|[Users](#schemausers)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|400 response|[Error](#schemaerror)|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|403 response|[Error](#schemaerror)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|404 response|[Error](#schemaerror)|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|415 response|[Error](#schemaerror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|500 response|[Error](#schemaerror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
None, api_key
</aside>

## options__users

`OPTIONS /users`

> Body parameter

```json
{}
```

<h3 id="options__users-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[Empty](#schemaempty)|true|none|

> Example responses

> 200 Response

```json
{}
```

<h3 id="options__users-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|200 response|[Empty](#schemaempty)|

<aside class="success">
This operation does not require authentication
</aside>

## post__users

`POST /users`

> Body parameter

```json
{
  "name": "string",
  "avatar": "string",
  "email": "string",
  "appClientId": "string"
}
```

<h3 id="post__users-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Content-Type|header|string|true|none|
|body|body|[PostUsers](#schemapostusers)|true|none|

> Example responses

> 200 Response

```json
{
  "updatedTime": "string",
  "updatedBy": "string",
  "createdBy": "string",
  "name": "string",
  "createdTime": "string",
  "avatar": "string",
  "userId": "string",
  "email": "string"
}
```

<h3 id="post__users-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|200 response|[User](#schemauser)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|400 response|[Error](#schemaerror)|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|403 response|[Error](#schemaerror)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|404 response|[Error](#schemaerror)|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|415 response|[Error](#schemaerror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|500 response|[Error](#schemaerror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
None, api_key
</aside>

## delete__users_{userId}

`DELETE /users/{userId}`

<h3 id="delete__users_{userid}-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|userId|path|string|true|none|

> Example responses

> 200 Response

```json
{
  "updatedTime": "string",
  "updatedBy": "string",
  "createdBy": "string",
  "name": "string",
  "createdTime": "string",
  "avatar": "string",
  "userId": "string",
  "email": "string"
}
```

<h3 id="delete__users_{userid}-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|200 response|[User](#schemauser)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|400 response|[Error](#schemaerror)|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|403 response|[Error](#schemaerror)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|404 response|[Error](#schemaerror)|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|415 response|[Error](#schemaerror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|500 response|[Error](#schemaerror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
None, api_key
</aside>

## get__users_{userId}

`GET /users/{userId}`

<h3 id="get__users_{userid}-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|userId|path|string|true|none|

> Example responses

> 200 Response

```json
{
  "updatedTime": "string",
  "updatedBy": "string",
  "createdBy": "string",
  "name": "string",
  "createdTime": "string",
  "avatar": "string",
  "userId": "string",
  "email": "string"
}
```

<h3 id="get__users_{userid}-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|200 response|[User](#schemauser)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|400 response|[Error](#schemaerror)|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|403 response|[Error](#schemaerror)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|404 response|[Error](#schemaerror)|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|415 response|[Error](#schemaerror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|500 response|[Error](#schemaerror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
None, api_key
</aside>

## options__users_{userId}

`OPTIONS /users/{userId}`

> Body parameter

```json
{}
```

<h3 id="options__users_{userid}-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|userId|path|string|true|none|
|body|body|[Empty](#schemaempty)|true|none|

> Example responses

> 200 Response

```json
{}
```

<h3 id="options__users_{userid}-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|200 response|[Empty](#schemaempty)|

<aside class="success">
This operation does not require authentication
</aside>

## patch__users_{userId}

`PATCH /users/{userId}`

> Body parameter

```json
{
  "name": "string",
  "avatar": "string"
}
```

<h3 id="patch__users_{userid}-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Content-Type|header|string|true|none|
|userId|path|string|true|none|
|body|body|[PatchUserId](#schemapatchuserid)|true|none|

> Example responses

> 200 Response

```json
{
  "updatedTime": "string",
  "updatedBy": "string",
  "createdBy": "string",
  "name": "string",
  "createdTime": "string",
  "avatar": "string",
  "userId": "string",
  "email": "string"
}
```

<h3 id="patch__users_{userid}-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|200 response|[User](#schemauser)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|400 response|[Error](#schemaerror)|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|403 response|[Error](#schemaerror)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|404 response|[Error](#schemaerror)|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|415 response|[Error](#schemaerror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|500 response|[Error](#schemaerror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
None, api_key
</aside>

## get__workflows

`GET /workflows`

<h3 id="get__workflows-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|nextToken|query|string|false|none|
|maxResults|query|string|false|none|

> Example responses

> 200 Response

```json
{
  "nextToken": "string",
  "workflows": [
    {
      "updatedTime": "string",
      "updatedBy": "string",
      "numberOfRunningExecutions": 0,
      "createdBy": "string",
      "completedConfig": {
        "environmentSecrets": [
          "string"
        ],
        "environment": {
          "property1": "string",
          "property2": "string"
        },
        "imageUrl": "string",
        "secretId": "string"
      },
      "name": "string",
      "description": "string",
      "createdTime": "string",
      "workflowId": "string",
      "errorConfig": {
        "manualRetry": true,
        "email": "string"
      }
    }
  ]
}
```

<h3 id="get__workflows-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|200 response|[Workflows](#schemaworkflows)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|400 response|[Error](#schemaerror)|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|403 response|[Error](#schemaerror)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|404 response|[Error](#schemaerror)|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|415 response|[Error](#schemaerror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|500 response|[Error](#schemaerror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
None, api_key
</aside>

## options__workflows

`OPTIONS /workflows`

> Body parameter

```json
{}
```

<h3 id="options__workflows-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[Empty](#schemaempty)|true|none|

> Example responses

> 200 Response

```json
{}
```

<h3 id="options__workflows-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|200 response|[Empty](#schemaempty)|

<aside class="success">
This operation does not require authentication
</aside>

## post__workflows

`POST /workflows`

> Body parameter

```json
{
  "completedConfig": {
    "environmentSecrets": [
      "string"
    ],
    "environment": {
      "property1": "string",
      "property2": "string"
    },
    "imageUrl": "string",
    "secretId": "string"
  },
  "name": "string",
  "description": "string",
  "specification": {
    "language": "ASL",
    "definition": {},
    "version": "1.0.0"
  },
  "errorConfig": {
    "manualRetry": true,
    "email": "string"
  }
}
```

<h3 id="post__workflows-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Content-Type|header|string|true|none|
|body|body|[PostWorkflows](#schemapostworkflows)|true|none|

> Example responses

> 200 Response

```json
{
  "updatedTime": "string",
  "updatedBy": "string",
  "numberOfRunningExecutions": 0,
  "createdBy": "string",
  "completedConfig": {
    "environmentSecrets": [
      "string"
    ],
    "environment": {
      "property1": "string",
      "property2": "string"
    },
    "imageUrl": "string",
    "secretId": "string"
  },
  "name": "string",
  "description": "string",
  "createdTime": "string",
  "workflowId": "string",
  "errorConfig": {
    "manualRetry": true,
    "email": "string"
  }
}
```

<h3 id="post__workflows-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|200 response|[Workflow](#schemaworkflow)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|400 response|[Error](#schemaerror)|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|403 response|[Error](#schemaerror)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|404 response|[Error](#schemaerror)|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|415 response|[Error](#schemaerror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|500 response|[Error](#schemaerror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
None, api_key
</aside>

## delete__workflows_{workflowId}

`DELETE /workflows/{workflowId}`

<h3 id="delete__workflows_{workflowid}-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|workflowId|path|string|true|none|

> Example responses

> 200 Response

```json
{
  "updatedTime": "string",
  "updatedBy": "string",
  "numberOfRunningExecutions": 0,
  "createdBy": "string",
  "completedConfig": {
    "environmentSecrets": [
      "string"
    ],
    "environment": {
      "property1": "string",
      "property2": "string"
    },
    "imageUrl": "string",
    "secretId": "string"
  },
  "name": "string",
  "description": "string",
  "createdTime": "string",
  "workflowId": "string",
  "errorConfig": {
    "manualRetry": true,
    "email": "string"
  }
}
```

<h3 id="delete__workflows_{workflowid}-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|200 response|[Workflow](#schemaworkflow)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|400 response|[Error](#schemaerror)|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|403 response|[Error](#schemaerror)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|404 response|[Error](#schemaerror)|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|415 response|[Error](#schemaerror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|500 response|[Error](#schemaerror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
None, api_key
</aside>

## get__workflows_{workflowId}

`GET /workflows/{workflowId}`

<h3 id="get__workflows_{workflowid}-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|workflowId|path|string|true|none|

> Example responses

> 200 Response

```json
{
  "updatedTime": "string",
  "updatedBy": "string",
  "numberOfRunningExecutions": 0,
  "createdBy": "string",
  "completedConfig": {
    "environmentSecrets": [
      "string"
    ],
    "environment": {
      "property1": "string",
      "property2": "string"
    },
    "imageUrl": "string",
    "secretId": "string"
  },
  "name": "string",
  "description": "string",
  "createdTime": "string",
  "workflowId": "string",
  "errorConfig": {
    "manualRetry": true,
    "email": "string"
  }
}
```

<h3 id="get__workflows_{workflowid}-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|200 response|[Workflow](#schemaworkflow)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|400 response|[Error](#schemaerror)|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|403 response|[Error](#schemaerror)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|404 response|[Error](#schemaerror)|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|415 response|[Error](#schemaerror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|500 response|[Error](#schemaerror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
None, api_key
</aside>

## options__workflows_{workflowId}

`OPTIONS /workflows/{workflowId}`

> Body parameter

```json
{}
```

<h3 id="options__workflows_{workflowid}-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|workflowId|path|string|true|none|
|body|body|[Empty](#schemaempty)|true|none|

> Example responses

> 200 Response

```json
{}
```

<h3 id="options__workflows_{workflowid}-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|200 response|[Empty](#schemaempty)|

<aside class="success">
This operation does not require authentication
</aside>

## patch__workflows_{workflowId}

`PATCH /workflows/{workflowId}`

> Body parameter

```json
{
  "completedConfig": {
    "environmentSecrets": [
      "string"
    ],
    "environment": {
      "property1": "string",
      "property2": "string"
    },
    "imageUrl": "string",
    "secretId": "string"
  },
  "name": "string",
  "description": "string",
  "errorConfig": {
    "manualRetry": true,
    "email": "string"
  }
}
```

<h3 id="patch__workflows_{workflowid}-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Content-Type|header|string|true|none|
|workflowId|path|string|true|none|
|body|body|[PatchWorkflowId](#schemapatchworkflowid)|true|none|

> Example responses

> 200 Response

```json
{
  "updatedTime": "string",
  "updatedBy": "string",
  "numberOfRunningExecutions": 0,
  "createdBy": "string",
  "completedConfig": {
    "environmentSecrets": [
      "string"
    ],
    "environment": {
      "property1": "string",
      "property2": "string"
    },
    "imageUrl": "string",
    "secretId": "string"
  },
  "name": "string",
  "description": "string",
  "createdTime": "string",
  "workflowId": "string",
  "errorConfig": {
    "manualRetry": true,
    "email": "string"
  }
}
```

<h3 id="patch__workflows_{workflowid}-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|200 response|[Workflow](#schemaworkflow)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|400 response|[Error](#schemaerror)|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|403 response|[Error](#schemaerror)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|404 response|[Error](#schemaerror)|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|415 response|[Error](#schemaerror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|500 response|[Error](#schemaerror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
None, api_key
</aside>

## get__workflows_{workflowId}_executions

`GET /workflows/{workflowId}/executions`

<h3 id="get__workflows_{workflowid}_executions-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|status|query|string|false|none|
|workflowId|path|string|true|none|
|nextToken|query|string|false|none|
|maxResults|query|string|false|none|
|sortBy|query|string|false|none|
|order|query|string|false|none|

> Example responses

> 200 Response

```json
{
  "executions": [
    {
      "transitionExecutions": {},
      "output": {},
      "executionId": "string",
      "input": {},
      "logId": "string",
      "startTime": "string",
      "completedTaskLogId": "string",
      "endTime": "string",
      "workflowId": "string",
      "completedBy": [
        "string"
      ],
      "events": [
        {}
      ],
      "status": "running"
    }
  ],
  "nextToken": "string",
  "sortBy": "startTime",
  "workflowId": "string",
  "status": [
    "running"
  ],
  "order": "ascending"
}
```

<h3 id="get__workflows_{workflowid}_executions-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|200 response|[WorkflowExecutions](#schemaworkflowexecutions)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|400 response|[Error](#schemaerror)|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|403 response|[Error](#schemaerror)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|404 response|[Error](#schemaerror)|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|415 response|[Error](#schemaerror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|500 response|[Error](#schemaerror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
None, api_key
</aside>

## options__workflows_{workflowId}_executions

`OPTIONS /workflows/{workflowId}/executions`

> Body parameter

```json
{}
```

<h3 id="options__workflows_{workflowid}_executions-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|workflowId|path|string|true|none|
|body|body|[Empty](#schemaempty)|true|none|

> Example responses

> 200 Response

```json
{}
```

<h3 id="options__workflows_{workflowid}_executions-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|200 response|[Empty](#schemaempty)|

<aside class="success">
This operation does not require authentication
</aside>

## post__workflows_{workflowId}_executions

`POST /workflows/{workflowId}/executions`

> Body parameter

```json
{
  "input": {}
}
```

<h3 id="post__workflows_{workflowid}_executions-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Content-Type|header|string|true|none|
|workflowId|path|string|true|none|
|body|body|[PostWorkflowExecutions](#schemapostworkflowexecutions)|true|none|

> Example responses

> 200 Response

```json
{
  "transitionExecutions": {},
  "output": {},
  "executionId": "string",
  "input": {},
  "logId": "string",
  "startTime": "string",
  "completedTaskLogId": "string",
  "endTime": "string",
  "workflowId": "string",
  "completedBy": [
    "string"
  ],
  "events": [
    {}
  ],
  "status": "running"
}
```

<h3 id="post__workflows_{workflowid}_executions-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|200 response|[WorkflowExecution](#schemaworkflowexecution)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|400 response|[Error](#schemaerror)|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|403 response|[Error](#schemaerror)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|404 response|[Error](#schemaerror)|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|415 response|[Error](#schemaerror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|500 response|[Error](#schemaerror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
None, api_key
</aside>

## delete__workflows_{workflowId}_executions_{executionId}

`DELETE /workflows/{workflowId}/executions/{executionId}`

<h3 id="delete__workflows_{workflowid}_executions_{executionid}-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|executionId|path|string|true|none|
|workflowId|path|string|true|none|

> Example responses

> 200 Response

```json
{
  "transitionExecutions": {},
  "output": {},
  "executionId": "string",
  "input": {},
  "logId": "string",
  "startTime": "string",
  "completedTaskLogId": "string",
  "endTime": "string",
  "workflowId": "string",
  "completedBy": [
    "string"
  ],
  "events": [
    {}
  ],
  "status": "running"
}
```

<h3 id="delete__workflows_{workflowid}_executions_{executionid}-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|200 response|[WorkflowExecution](#schemaworkflowexecution)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|400 response|[Error](#schemaerror)|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|403 response|[Error](#schemaerror)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|404 response|[Error](#schemaerror)|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|415 response|[Error](#schemaerror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|500 response|[Error](#schemaerror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
None, api_key
</aside>

## get__workflows_{workflowId}_executions_{executionId}

`GET /workflows/{workflowId}/executions/{executionId}`

<h3 id="get__workflows_{workflowid}_executions_{executionid}-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|executionId|path|string|true|none|
|workflowId|path|string|true|none|

> Example responses

> 200 Response

```json
{
  "transitionExecutions": {},
  "output": {},
  "executionId": "string",
  "input": {},
  "logId": "string",
  "startTime": "string",
  "completedTaskLogId": "string",
  "endTime": "string",
  "workflowId": "string",
  "completedBy": [
    "string"
  ],
  "events": [
    {}
  ],
  "status": "running"
}
```

<h3 id="get__workflows_{workflowid}_executions_{executionid}-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|200 response|[WorkflowExecution](#schemaworkflowexecution)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|400 response|[Error](#schemaerror)|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|403 response|[Error](#schemaerror)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|404 response|[Error](#schemaerror)|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|415 response|[Error](#schemaerror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|500 response|[Error](#schemaerror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
None, api_key
</aside>

## options__workflows_{workflowId}_executions_{executionId}

`OPTIONS /workflows/{workflowId}/executions/{executionId}`

> Body parameter

```json
{}
```

<h3 id="options__workflows_{workflowid}_executions_{executionid}-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|executionId|path|string|true|none|
|workflowId|path|string|true|none|
|body|body|[Empty](#schemaempty)|true|none|

> Example responses

> 200 Response

```json
{}
```

<h3 id="options__workflows_{workflowid}_executions_{executionid}-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|200 response|[Empty](#schemaempty)|

<aside class="success">
This operation does not require authentication
</aside>

## patch__workflows_{workflowId}_executions_{executionId}

`PATCH /workflows/{workflowId}/executions/{executionId}`

> Body parameter

```json
{
  "nextTransitionId": "string"
}
```

<h3 id="patch__workflows_{workflowid}_executions_{executionid}-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Content-Type|header|string|true|none|
|executionId|path|string|true|none|
|workflowId|path|string|true|none|
|body|body|[PatchWorkflowExecutionId](#schemapatchworkflowexecutionid)|true|none|

> Example responses

> 200 Response

```json
{
  "transitionExecutions": {},
  "output": {},
  "executionId": "string",
  "input": {},
  "logId": "string",
  "startTime": "string",
  "completedTaskLogId": "string",
  "endTime": "string",
  "workflowId": "string",
  "completedBy": [
    "string"
  ],
  "events": [
    {}
  ],
  "status": "running"
}
```

<h3 id="patch__workflows_{workflowid}_executions_{executionid}-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|200 response|[WorkflowExecution](#schemaworkflowexecution)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|400 response|[Error](#schemaerror)|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|403 response|[Error](#schemaerror)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|404 response|[Error](#schemaerror)|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|415 response|[Error](#schemaerror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|500 response|[Error](#schemaerror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
None, api_key
</aside>

# Schemas

<h2 id="tocS_PostModels">PostModels</h2>
<a id="schemapostmodels"></a>
<a id="schema_PostModels"></a>
<a id="tocSpostmodels"></a>
<a id="tocspostmodels"></a>

```json
{
  "preprocessConfig": {
    "maxPages": 1,
    "autoRotate": true,
    "imageQuality": "LOW"
  },
  "name": "string",
  "width": 97,
  "description": "string",
  "fieldConfig": {
    "property1": {
      "description": "string",
      "type": "date",
      "maxLength": 1
    },
    "property2": {
      "description": "string",
      "type": "date",
      "maxLength": 1
    }
  },
  "height": 97
}

```

POST /models

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|preprocessConfig|object|false|none|none|
|» maxPages|integer|true|none|none|
|» autoRotate|boolean|true|none|none|
|» imageQuality|string|true|none|none|
|name|string¦null|false|none|none|
|width|integer|true|none|none|
|description|string¦null|false|none|none|
|fieldConfig|object|true|none|none|
|» **additionalProperties**|object|false|none|none|
|»» description|string¦null|false|none|none|
|»» type|string|true|none|none|
|»» maxLength|integer|true|none|none|
|height|integer|true|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|imageQuality|LOW|
|imageQuality|HIGH|
|type|date|
|type|amount|
|type|number|
|type|letter|
|type|phone|
|type|alphanum|
|type|alphanumext|
|type|all|
|type|string|
|type|digits|

<h2 id="tocS_PostWorkflowExecutions">PostWorkflowExecutions</h2>
<a id="schemapostworkflowexecutions"></a>
<a id="schema_PostWorkflowExecutions"></a>
<a id="tocSpostworkflowexecutions"></a>
<a id="tocspostworkflowexecutions"></a>

```json
{
  "input": {}
}

```

POST /workflows/{workflowId}/executions

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|input|object|true|none|none|

<h2 id="tocS_Secrets">Secrets</h2>
<a id="schemasecrets"></a>
<a id="schema_Secrets"></a>
<a id="tocSsecrets"></a>
<a id="tocssecrets"></a>

```json
{
  "nextToken": "string",
  "secrets": [
    {
      "updatedTime": "string",
      "updatedBy": "string",
      "createdBy": "string",
      "name": "string",
      "secretId": "string",
      "createdTime": "string",
      "description": "string"
    }
  ]
}

```

secrets

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|nextToken|string¦null|true|none|none|
|secrets|[object]|true|none|none|
|» updatedTime|string¦null|true|none|none|
|» updatedBy|string¦null|true|none|none|
|» createdBy|string¦null|true|none|none|
|» name|string¦null|true|none|none|
|» secretId|string|true|none|none|
|» createdTime|string¦null|true|none|none|
|» description|string¦null|true|none|none|

<h2 id="tocS_Transitions">Transitions</h2>
<a id="schematransitions"></a>
<a id="schema_Transitions"></a>
<a id="tocStransitions"></a>
<a id="tocstransitions"></a>

```json
{
  "nextToken": "string",
  "transitions": [
    {
      "updatedTime": "string",
      "updatedBy": "string",
      "transitionId": "string",
      "description": "string",
      "inputJsonSchema": {},
      "timeoutInSeconds": 60,
      "outputJsonSchema": {},
      "assets": {
        "jsRemoteComponent": "string",
        "property1": "string",
        "property2": "string"
      },
      "createdBy": "string",
      "name": "string",
      "createdTime": "string",
      "transitionType": "docker",
      "parameters": {}
    }
  ],
  "transitionType": [
    "docker"
  ]
}

```

transitions

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|nextToken|string¦null|true|none|none|
|transitions|[object]|true|none|none|
|» updatedTime|string¦null|true|none|none|
|» updatedBy|string¦null|true|none|none|
|» transitionId|any|true|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|string|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» description|string¦null|true|none|none|
|» inputJsonSchema|object|false|none|none|
|» timeoutInSeconds|integer|true|none|none|
|» outputJsonSchema|object|false|none|none|
|» assets|object|false|none|none|
|»» **additionalProperties**|string|false|none|none|
|»» jsRemoteComponent|string|false|none|none|
|» createdBy|string¦null|true|none|none|
|» name|string¦null|true|none|none|
|» createdTime|string¦null|true|none|none|
|» transitionType|string|true|none|none|
|» parameters|object|true|none|none|
|transitionType|[string]|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|transitionType|docker|
|transitionType|manual|

<h2 id="tocS_Users">Users</h2>
<a id="schemausers"></a>
<a id="schema_Users"></a>
<a id="tocSusers"></a>
<a id="tocsusers"></a>

```json
{
  "nextToken": "string",
  "users": [
    {
      "updatedTime": "string",
      "updatedBy": "string",
      "createdBy": "string",
      "name": "string",
      "createdTime": "string",
      "avatar": "string",
      "userId": "string",
      "email": "string"
    }
  ]
}

```

users

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|nextToken|string¦null|true|none|none|
|users|[object]|true|none|none|
|» updatedTime|string¦null|true|none|none|
|» updatedBy|string¦null|true|none|none|
|» createdBy|string¦null|true|none|none|
|» name|string¦null|false|none|none|
|» createdTime|string¦null|true|none|none|
|» avatar|string¦null|false|none|none|
|» userId|string|true|none|none|
|» email|string|true|none|none|

<h2 id="tocS_Document">Document</h2>
<a id="schemadocument"></a>
<a id="schema_Document"></a>
<a id="tocSdocument"></a>
<a id="tocsdocument"></a>

```json
{
  "groundTruth": [
    {
      "label": "string",
      "value": "string"
    }
  ],
  "updatedTime": "string",
  "consentId": "string",
  "retentionInDays": 1,
  "updatedBy": "string",
  "createdBy": "string",
  "createdTime": "string",
  "datasetId": "string",
  "documentId": "string",
  "contentType": "application/pdf",
  "content": "string"
}

```

document

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|groundTruth|[object]|false|none|none|
|» label|string|true|none|none|
|» value|any|true|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|string¦null|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|boolean|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|updatedTime|string¦null|true|none|none|
|consentId|string|false|none|none|
|retentionInDays|integer|true|none|none|
|updatedBy|string¦null|true|none|none|
|createdBy|string¦null|true|none|none|
|createdTime|string¦null|true|none|none|
|datasetId|string|false|none|none|
|documentId|string|true|none|none|
|contentType|string|true|none|none|
|content|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|contentType|application/pdf|
|contentType|image/jpeg|
|contentType|image/png|
|contentType|image/tiff|

<h2 id="tocS_PatchDocumentId">PatchDocumentId</h2>
<a id="schemapatchdocumentid"></a>
<a id="schema_PatchDocumentId"></a>
<a id="tocSpatchdocumentid"></a>
<a id="tocspatchdocumentid"></a>

```json
{
  "groundTruth": [
    {
      "label": "string",
      "value": "string"
    }
  ],
  "retentionInDays": 1,
  "datasetId": "string"
}

```

PATCH /documents/{documentId}

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|groundTruth|[object]|false|none|none|
|» label|string|true|none|none|
|» value|any|true|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|string¦null|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|boolean|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|retentionInDays|integer|false|none|none|
|datasetId|string|false|none|none|

<h2 id="tocS_PatchAppClientId">PatchAppClientId</h2>
<a id="schemapatchappclientid"></a>
<a id="schema_PatchAppClientId"></a>
<a id="tocSpatchappclientid"></a>
<a id="tocspatchappclientid"></a>

```json
{
  "name": "string",
  "description": "string",
  "loginUrls": [
    "string"
  ],
  "defaultLoginUrl": "string"
}

```

PATCH /appClients/{appClientId}

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|name|string¦null|false|none|none|
|description|string¦null|false|none|none|
|loginUrls|[string]|false|none|none|
|defaultLoginUrl|string|false|none|none|

<h2 id="tocS_Datasets">Datasets</h2>
<a id="schemadatasets"></a>
<a id="schema_Datasets"></a>
<a id="tocSdatasets"></a>
<a id="tocsdatasets"></a>

```json
{
  "nextToken": "string",
  "datasets": [
    {
      "updatedTime": "string",
      "retentionInDays": 1825,
      "updatedBy": "string",
      "groundTruthSummary": {},
      "description": "string",
      "storageLocation": "EU",
      "version": 0,
      "createdBy": "string",
      "numberOfDocuments": 0,
      "name": "string",
      "datasetId": "string",
      "createdTime": "string",
      "containsPersonallyIdentifiableInformation": true
    }
  ]
}

```

datasets

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|nextToken|string¦null|true|none|none|
|datasets|[object]|true|none|none|
|» updatedTime|string¦null|true|none|none|
|» retentionInDays|integer|true|none|none|
|» updatedBy|string¦null|true|none|none|
|» groundTruthSummary|object|true|none|none|
|» description|string¦null|true|none|none|
|» storageLocation|string|true|none|none|
|» version|integer|true|none|none|
|» createdBy|string¦null|true|none|none|
|» numberOfDocuments|integer|true|none|none|
|» name|string¦null|false|none|none|
|» datasetId|string|true|none|none|
|» createdTime|string¦null|true|none|none|
|» containsPersonallyIdentifiableInformation|boolean|true|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|storageLocation|EU|

<h2 id="tocS_DataBundle">DataBundle</h2>
<a id="schemadatabundle"></a>
<a id="schema_DataBundle"></a>
<a id="tocSdatabundle"></a>
<a id="tocsdatabundle"></a>

```json
{
  "summary": {},
  "updatedTime": "string",
  "updatedBy": "string",
  "modelId": "string",
  "createdBy": "string",
  "dataBundleId": "string",
  "name": "string",
  "description": "string",
  "createdTime": "string",
  "datasets": [
    {
      "updatedTime": "string",
      "retentionInDays": 1825,
      "updatedBy": "string",
      "groundTruthSummary": {},
      "description": "string",
      "storageLocation": "EU",
      "version": 0,
      "createdBy": "string",
      "numberOfDocuments": 0,
      "name": "string",
      "datasetId": "string",
      "createdTime": "string",
      "containsPersonallyIdentifiableInformation": true
    }
  ],
  "status": "processing"
}

```

dataBundle

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|summary|object|true|none|none|
|updatedTime|string¦null|true|none|none|
|updatedBy|string¦null|true|none|none|
|modelId|string|true|none|none|
|createdBy|string¦null|true|none|none|
|dataBundleId|string|true|none|none|
|name|string¦null|true|none|none|
|description|string¦null|true|none|none|
|createdTime|string¦null|true|none|none|
|datasets|[object]|true|none|none|
|» updatedTime|string¦null|false|none|none|
|» retentionInDays|integer|true|none|none|
|» updatedBy|string¦null|false|none|none|
|» groundTruthSummary|object|false|none|none|
|» description|string¦null|true|none|none|
|» storageLocation|string|true|none|none|
|» version|integer|true|none|none|
|» createdBy|string¦null|false|none|none|
|» numberOfDocuments|integer|true|none|none|
|» name|string¦null|false|none|none|
|» datasetId|string|true|none|none|
|» createdTime|string¦null|false|none|none|
|» containsPersonallyIdentifiableInformation|boolean|true|none|none|
|status|string|true|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|storageLocation|EU|
|status|processing|
|status|ready|
|status|failed|

<h2 id="tocS_Asset">Asset</h2>
<a id="schemaasset"></a>
<a id="schema_Asset"></a>
<a id="tocSasset"></a>
<a id="tocsasset"></a>

```json
{
  "updatedTime": "string",
  "updatedBy": "string",
  "createdBy": "string",
  "assetId": "string",
  "name": "string",
  "description": "string",
  "createdTime": "string",
  "content": "string"
}

```

asset

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|updatedTime|string¦null|true|none|none|
|updatedBy|string¦null|true|none|none|
|createdBy|string¦null|true|none|none|
|assetId|string|true|none|none|
|name|string¦null|true|none|none|
|description|string¦null|true|none|none|
|createdTime|string¦null|true|none|none|
|content|string|false|none|none|

<h2 id="tocS_DataBundles">DataBundles</h2>
<a id="schemadatabundles"></a>
<a id="schema_DataBundles"></a>
<a id="tocSdatabundles"></a>
<a id="tocsdatabundles"></a>

```json
{
  "nextToken": "string",
  "dataBundles": [
    {
      "summary": {},
      "updatedTime": "string",
      "updatedBy": "string",
      "modelId": "string",
      "createdBy": "string",
      "dataBundleId": "string",
      "name": "string",
      "description": "string",
      "createdTime": "string",
      "datasets": [
        {
          "updatedTime": "string",
          "retentionInDays": 1825,
          "updatedBy": "string",
          "groundTruthSummary": {},
          "description": "string",
          "storageLocation": "EU",
          "version": 0,
          "createdBy": "string",
          "numberOfDocuments": 0,
          "name": "string",
          "datasetId": "string",
          "createdTime": "string",
          "containsPersonallyIdentifiableInformation": true
        }
      ],
      "status": "processing"
    }
  ],
  "status": [
    "processing"
  ]
}

```

dataBundles

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|nextToken|string¦null|true|none|none|
|dataBundles|[object]|true|none|none|
|» summary|object|true|none|none|
|» updatedTime|string¦null|true|none|none|
|» updatedBy|string¦null|true|none|none|
|» modelId|string|true|none|none|
|» createdBy|string¦null|true|none|none|
|» dataBundleId|string|true|none|none|
|» name|string¦null|true|none|none|
|» description|string¦null|true|none|none|
|» createdTime|string¦null|true|none|none|
|» datasets|[object]|true|none|none|
|»» updatedTime|string¦null|false|none|none|
|»» retentionInDays|integer|true|none|none|
|»» updatedBy|string¦null|false|none|none|
|»» groundTruthSummary|object|false|none|none|
|»» description|string¦null|true|none|none|
|»» storageLocation|string|true|none|none|
|»» version|integer|true|none|none|
|»» createdBy|string¦null|false|none|none|
|»» numberOfDocuments|integer|true|none|none|
|»» name|string¦null|false|none|none|
|»» datasetId|string|true|none|none|
|»» createdTime|string¦null|false|none|none|
|»» containsPersonallyIdentifiableInformation|boolean|true|none|none|
|» status|string|true|none|none|
|status|[string]|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|storageLocation|EU|
|status|processing|
|status|ready|
|status|failed|

<h2 id="tocS_Log">Log</h2>
<a id="schemalog"></a>
<a id="schema_Log"></a>
<a id="tocSlog"></a>
<a id="tocslog"></a>

```json
{
  "transitionId": "string",
  "transitionExecutionId": "string",
  "logId": "string",
  "workflowExecutionId": "string",
  "startTime": "string",
  "workflowId": "string",
  "events": [
    {}
  ]
}

```

log

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|transitionId|any|true|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|transitionExecutionId|string¦null|true|none|none|
|logId|string|true|none|none|
|workflowExecutionId|string¦null|true|none|none|
|startTime|string¦null|true|none|none|
|workflowId|string¦null|true|none|none|
|events|[object]|false|none|none|

<h2 id="tocS_Workflows">Workflows</h2>
<a id="schemaworkflows"></a>
<a id="schema_Workflows"></a>
<a id="tocSworkflows"></a>
<a id="tocsworkflows"></a>

```json
{
  "nextToken": "string",
  "workflows": [
    {
      "updatedTime": "string",
      "updatedBy": "string",
      "numberOfRunningExecutions": 0,
      "createdBy": "string",
      "completedConfig": {
        "environmentSecrets": [
          "string"
        ],
        "environment": {
          "property1": "string",
          "property2": "string"
        },
        "imageUrl": "string",
        "secretId": "string"
      },
      "name": "string",
      "description": "string",
      "createdTime": "string",
      "workflowId": "string",
      "errorConfig": {
        "manualRetry": true,
        "email": "string"
      }
    }
  ]
}

```

workflows

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|nextToken|string¦null|true|none|none|
|workflows|[object]|true|none|none|
|» updatedTime|string¦null|true|none|none|
|» updatedBy|string¦null|true|none|none|
|» numberOfRunningExecutions|integer|true|none|none|
|» createdBy|string¦null|true|none|none|
|» completedConfig|object|true|none|none|
|»» environmentSecrets|[string]|false|none|none|
|»» environment|object|false|none|none|
|»»» **additionalProperties**|string|false|none|none|
|»» imageUrl|string|true|none|none|
|»» secretId|string|false|none|none|
|» name|string¦null|true|none|none|
|» description|string¦null|true|none|none|
|» createdTime|string¦null|true|none|none|
|» workflowId|string|true|none|none|
|» errorConfig|object|true|none|none|
|»» manualRetry|boolean|false|none|none|
|»» email|string|false|none|none|

<h2 id="tocS_Prediction">Prediction</h2>
<a id="schemaprediction"></a>
<a id="schema_Prediction"></a>
<a id="tocSprediction"></a>
<a id="tocsprediction"></a>

```json
{
  "modelId": "string",
  "inferenceTime": 0,
  "documentId": "string",
  "predictionId": "string",
  "predictions": [
    {
      "confidence": 1,
      "label": "string",
      "value": "string"
    }
  ],
  "timestamp": 1
}

```

prediction

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|modelId|string|true|none|none|
|inferenceTime|number|true|none|none|
|documentId|string|true|none|none|
|predictionId|string|true|none|none|
|predictions|[object]|true|none|none|
|» confidence|number|true|none|none|
|» label|string|true|none|none|
|» value|string¦null|true|none|none|
|timestamp|integer|true|none|none|

<h2 id="tocS_Workflow">Workflow</h2>
<a id="schemaworkflow"></a>
<a id="schema_Workflow"></a>
<a id="tocSworkflow"></a>
<a id="tocsworkflow"></a>

```json
{
  "updatedTime": "string",
  "updatedBy": "string",
  "numberOfRunningExecutions": 0,
  "createdBy": "string",
  "completedConfig": {
    "environmentSecrets": [
      "string"
    ],
    "environment": {
      "property1": "string",
      "property2": "string"
    },
    "imageUrl": "string",
    "secretId": "string"
  },
  "name": "string",
  "description": "string",
  "createdTime": "string",
  "workflowId": "string",
  "errorConfig": {
    "manualRetry": true,
    "email": "string"
  }
}

```

workflow

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|updatedTime|string¦null|true|none|none|
|updatedBy|string¦null|true|none|none|
|numberOfRunningExecutions|integer|true|none|none|
|createdBy|string¦null|true|none|none|
|completedConfig|object|true|none|none|
|» environmentSecrets|[string]|false|none|none|
|» environment|object|false|none|none|
|»» **additionalProperties**|string|false|none|none|
|» imageUrl|string|true|none|none|
|» secretId|string|false|none|none|
|name|string¦null|true|none|none|
|description|string¦null|true|none|none|
|createdTime|string¦null|true|none|none|
|workflowId|string|true|none|none|
|errorConfig|object|true|none|none|
|» manualRetry|boolean|false|none|none|
|» email|string|false|none|none|

<h2 id="tocS_PostSignUp">PostSignUp</h2>
<a id="schemapostsignup"></a>
<a id="schema_PostSignUp"></a>
<a id="tocSpostsignup"></a>
<a id="tocspostsignup"></a>

```json
{
  "password": "string",
  "reCaptchaResponse": "string",
  "name": "string",
  "email": "string"
}

```

POST /users

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|password|string|true|none|none|
|reCaptchaResponse|string|true|none|none|
|name|string¦null|false|none|none|
|email|string|true|none|none|

<h2 id="tocS_PostAppClients">PostAppClients</h2>
<a id="schemapostappclients"></a>
<a id="schema_PostAppClients"></a>
<a id="tocSpostappclients"></a>
<a id="tocspostappclients"></a>

```json
{
  "generateSecret": true,
  "logoutUrls": [
    "string"
  ],
  "name": "string",
  "callbackUrls": [
    "string"
  ],
  "description": "string",
  "loginUrls": [
    "string"
  ],
  "defaultLoginUrl": "string"
}

```

POST /appClients

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|generateSecret|boolean|false|none|none|
|logoutUrls|[string]|false|none|none|
|name|string¦null|false|none|none|
|callbackUrls|[string]|false|none|none|
|description|string¦null|false|none|none|
|loginUrls|[string]|false|none|none|
|defaultLoginUrl|string|false|none|none|

<h2 id="tocS_Secret">Secret</h2>
<a id="schemasecret"></a>
<a id="schema_Secret"></a>
<a id="tocSsecret"></a>
<a id="tocssecret"></a>

```json
{
  "updatedTime": "string",
  "updatedBy": "string",
  "createdBy": "string",
  "name": "string",
  "secretId": "string",
  "createdTime": "string",
  "description": "string"
}

```

secret

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|updatedTime|string¦null|true|none|none|
|updatedBy|string¦null|true|none|none|
|createdBy|string¦null|true|none|none|
|name|string¦null|true|none|none|
|secretId|string|true|none|none|
|createdTime|string¦null|true|none|none|
|description|string¦null|true|none|none|

<h2 id="tocS_PostTransitionExecution">PostTransitionExecution</h2>
<a id="schemaposttransitionexecution"></a>
<a id="schema_PostTransitionExecution"></a>
<a id="tocSposttransitionexecution"></a>
<a id="tocsposttransitionexecution"></a>

```json
{}

```

POST /transitions/{transitionId}/executions

### Properties

*None*

<h2 id="tocS_Documents">Documents</h2>
<a id="schemadocuments"></a>
<a id="schema_Documents"></a>
<a id="tocSdocuments"></a>
<a id="tocsdocuments"></a>

```json
{
  "consentId": [
    "string"
  ],
  "documents": [
    {
      "groundTruth": [
        {
          "label": "string",
          "value": "string"
        }
      ],
      "updatedTime": "string",
      "consentId": "string",
      "retentionInDays": 1,
      "updatedBy": "string",
      "createdBy": "string",
      "createdTime": "string",
      "datasetId": "string",
      "documentId": "string",
      "contentType": "application/pdf",
      "content": "string"
    }
  ],
  "nextToken": "string",
  "datasetId": [
    "string"
  ]
}

```

documents

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|consentId|[string]|false|none|none|
|documents|[object]|true|none|none|
|» groundTruth|[object]|false|none|none|
|»» label|string|true|none|none|
|»» value|any|true|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»»» *anonymous*|string¦null|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»»» *anonymous*|boolean|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» updatedTime|string¦null|true|none|none|
|» consentId|string|false|none|none|
|» retentionInDays|integer|true|none|none|
|» updatedBy|string¦null|true|none|none|
|» createdBy|string¦null|true|none|none|
|» createdTime|string¦null|true|none|none|
|» datasetId|string|false|none|none|
|» documentId|string|true|none|none|
|» contentType|string|true|none|none|
|» content|string|false|none|none|
|nextToken|string¦null|true|none|none|
|datasetId|[string]|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|contentType|application/pdf|
|contentType|image/jpeg|
|contentType|image/png|
|contentType|image/tiff|

<h2 id="tocS_Predictions">Predictions</h2>
<a id="schemapredictions"></a>
<a id="schema_Predictions"></a>
<a id="tocSpredictions"></a>
<a id="tocspredictions"></a>

```json
{
  "nextToken": "string",
  "predictions": [
    {
      "modelId": "string",
      "inferenceTime": 0,
      "documentId": "string",
      "predictionId": "string",
      "predictions": [
        {
          "confidence": 1,
          "label": "string",
          "value": "string"
        }
      ],
      "timestamp": 1
    }
  ]
}

```

predictions

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|nextToken|string¦null|true|none|none|
|predictions|[object]|true|none|none|
|» modelId|string|true|none|none|
|» inferenceTime|number|true|none|none|
|» documentId|string|true|none|none|
|» predictionId|string|true|none|none|
|» predictions|[object]|true|none|none|
|»» confidence|number|true|none|none|
|»» label|string|true|none|none|
|»» value|string¦null|true|none|none|
|» timestamp|integer|true|none|none|

<h2 id="tocS_AppClient">AppClient</h2>
<a id="schemaappclient"></a>
<a id="schema_AppClient"></a>
<a id="tocSappclient"></a>
<a id="tocsappclient"></a>

```json
{
  "hasSecret": true,
  "updatedTime": "string",
  "clientId": "string",
  "updatedBy": "string",
  "apiKey": "string",
  "logoutUrls": [
    "string"
  ],
  "description": "string",
  "callbackUrls": [
    "string"
  ],
  "loginUrls": [
    "string"
  ],
  "defaultLoginUrl": "string",
  "createdBy": "string",
  "name": "string",
  "createdTime": "string",
  "clientSecret": "string",
  "appClientId": "string"
}

```

appClient

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|hasSecret|boolean|true|none|none|
|updatedTime|string¦null|true|none|none|
|clientId|string|true|none|none|
|updatedBy|string¦null|true|none|none|
|apiKey|string¦null|true|none|none|
|logoutUrls|[string]|true|none|none|
|description|string¦null|true|none|none|
|callbackUrls|[string]|true|none|none|
|loginUrls|[string]|true|none|none|
|defaultLoginUrl|string¦null|true|none|none|
|createdBy|string¦null|true|none|none|
|name|string¦null|true|none|none|
|createdTime|string¦null|true|none|none|
|clientSecret|string|false|none|none|
|appClientId|string|true|none|none|

<h2 id="tocS_WorkflowExecution">WorkflowExecution</h2>
<a id="schemaworkflowexecution"></a>
<a id="schema_WorkflowExecution"></a>
<a id="tocSworkflowexecution"></a>
<a id="tocsworkflowexecution"></a>

```json
{
  "transitionExecutions": {},
  "output": {},
  "executionId": "string",
  "input": {},
  "logId": "string",
  "startTime": "string",
  "completedTaskLogId": "string",
  "endTime": "string",
  "workflowId": "string",
  "completedBy": [
    "string"
  ],
  "events": [
    {}
  ],
  "status": "running"
}

```

workflow-execution

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|transitionExecutions|object|true|none|none|
|output|object|true|none|none|
|executionId|string|true|none|none|
|input|object|true|none|none|
|logId|string¦null|false|none|none|
|startTime|string¦null|true|none|none|
|completedTaskLogId|string¦null|false|none|none|
|endTime|string¦null|true|none|none|
|workflowId|string|true|none|none|
|completedBy|[anyOf]|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|events|[object]|false|none|none|
|status|string|true|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|status|running|
|status|succeeded|
|status|failed|
|status|rejected|
|status|retry|
|status|error|

<h2 id="tocS_Models">Models</h2>
<a id="schemamodels"></a>
<a id="schema_Models"></a>
<a id="tocSmodels"></a>
<a id="tocsmodels"></a>

```json
{
  "models": [
    {
      "updatedTime": "string",
      "updatedBy": "string",
      "modelId": "string",
      "description": "string",
      "fieldConfig": {
        "property1": {
          "description": "string",
          "type": "date",
          "maxLength": 1
        },
        "property2": {
          "description": "string",
          "type": "date",
          "maxLength": 1
        }
      },
      "preprocessConfig": {
        "maxPages": 1,
        "autoRotate": true,
        "imageQuality": "LOW"
      },
      "createdBy": "string",
      "name": "string",
      "width": 97,
      "numberOfDataBundles": 0,
      "createdTime": "string",
      "height": 97,
      "status": "active"
    }
  ],
  "nextToken": "string"
}

```

models

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|models|[object]|true|none|none|
|» updatedTime|string¦null|true|none|none|
|» updatedBy|string¦null|true|none|none|
|» modelId|string|true|none|none|
|» description|string¦null|true|none|none|
|» fieldConfig|object|true|none|none|
|»» **additionalProperties**|object|false|none|none|
|»»» description|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»»»» *anonymous*|string|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»»» type|string|true|none|none|
|»»» maxLength|integer|true|none|none|
|» preprocessConfig|object|true|none|none|
|»» maxPages|integer|true|none|none|
|»» autoRotate|boolean|true|none|none|
|»» imageQuality|string|true|none|none|
|» createdBy|string¦null|true|none|none|
|» name|string¦null|true|none|none|
|» width|integer|true|none|none|
|» numberOfDataBundles|integer|true|none|none|
|» createdTime|string¦null|true|none|none|
|» height|integer|true|none|none|
|» status|string|true|none|none|
|nextToken|string¦null|true|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|type|date|
|type|amount|
|type|number|
|type|letter|
|type|phone|
|type|alphanum|
|type|alphanumext|
|type|all|
|type|string|
|type|digits|
|imageQuality|LOW|
|imageQuality|HIGH|
|status|active|
|status|training|
|status|inactive|

<h2 id="tocS_PatchTransistionExecutionId">PatchTransistionExecutionId</h2>
<a id="schemapatchtransistionexecutionid"></a>
<a id="schema_PatchTransistionExecutionId"></a>
<a id="tocSpatchtransistionexecutionid"></a>
<a id="tocspatchtransistionexecutionid"></a>

```json
{
  "status": "succeeded"
}

```

PATCH transitions/{transitionId}/executions/{executionId}

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|output|object|false|none|none|
|startTime|string¦null|false|none|none|
|error|object|false|none|none|
|» message|string|true|none|none|
|status|string|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|object|false|none|none|
|» status|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|object|false|none|none|
|» status|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|status|succeeded|
|status|failed|
|status|rejected|
|status|retry|

<h2 id="tocS_PatchTransitionId">PatchTransitionId</h2>
<a id="schemapatchtransitionid"></a>
<a id="schema_PatchTransitionId"></a>
<a id="tocSpatchtransitionid"></a>
<a id="tocspatchtransitionid"></a>

```json
{
  "environmentSecrets": [
    "string"
  ],
  "environment": {
    "property1": "string",
    "property2": "string"
  },
  "outputJsonSchema": {},
  "assets": {
    "jsRemoteComponent": "string",
    "property1": "string",
    "property2": "string"
  },
  "name": "string",
  "description": "string",
  "inputJsonSchema": {}
}

```

PATCH /transitions/{transitionId}

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|environmentSecrets|[string]|false|none|none|
|environment|object|false|none|none|
|» **additionalProperties**|string|false|none|none|
|outputJsonSchema|object|false|none|none|
|assets|object|false|none|none|
|» **additionalProperties**|string|false|none|none|
|» jsRemoteComponent|string|false|none|none|
|name|string¦null|false|none|none|
|description|string¦null|false|none|none|
|inputJsonSchema|object|false|none|none|

<h2 id="tocS_WorkflowExecutions">WorkflowExecutions</h2>
<a id="schemaworkflowexecutions"></a>
<a id="schema_WorkflowExecutions"></a>
<a id="tocSworkflowexecutions"></a>
<a id="tocsworkflowexecutions"></a>

```json
{
  "executions": [
    {
      "transitionExecutions": {},
      "output": {},
      "executionId": "string",
      "input": {},
      "logId": "string",
      "startTime": "string",
      "completedTaskLogId": "string",
      "endTime": "string",
      "workflowId": "string",
      "completedBy": [
        "string"
      ],
      "events": [
        {}
      ],
      "status": "running"
    }
  ],
  "nextToken": "string",
  "sortBy": "startTime",
  "workflowId": "string",
  "status": [
    "running"
  ],
  "order": "ascending"
}

```

workflow-executions

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|executions|[object]|true|none|none|
|» transitionExecutions|object|true|none|none|
|» output|object|true|none|none|
|» executionId|string|true|none|none|
|» input|object|true|none|none|
|» logId|string¦null|false|none|none|
|» startTime|string¦null|true|none|none|
|» completedTaskLogId|string¦null|false|none|none|
|» endTime|string¦null|true|none|none|
|» workflowId|string|true|none|none|
|» completedBy|[anyOf]|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|string|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» events|[object]|false|none|none|
|» status|string|true|none|none|
|nextToken|string¦null|true|none|none|
|sortBy|string|false|none|none|
|workflowId|string|true|none|none|
|status|[string]|false|none|none|
|order|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|status|running|
|status|succeeded|
|status|failed|
|status|rejected|
|status|retry|
|status|error|
|sortBy|startTime|
|sortBy|endTime|
|order|ascending|
|order|descending|

<h2 id="tocS_SignUp">SignUp</h2>
<a id="schemasignup"></a>
<a id="schema_SignUp"></a>
<a id="tocSsignup"></a>
<a id="tocssignup"></a>

```json
{
  "clientId": "string",
  "username": "string"
}

```

signup

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|clientId|string|true|none|none|
|username|string|true|none|none|

<h2 id="tocS_Organization">Organization</h2>
<a id="schemaorganization"></a>
<a id="schema_Organization"></a>
<a id="tocSorganization"></a>
<a id="tocsorganization"></a>

```json
{
  "numberOfWorkflowsCreated": 0,
  "monthlyNumberOfWorkflowExecutionsCreated": 0,
  "description": "string",
  "numberOfUsersAllowed": 0,
  "monthlyNumberOfPredictionsAllowed": 0,
  "numberOfDatasetsAllowed": 0,
  "monthlyNumberOfDataBundlesAllowed": 0,
  "organizationId": "string",
  "numberOfModelsCreated": 0,
  "numberOfTransitionsCreated": 0,
  "monthlyNumberOfTransitionExecutionsAllowed": 0,
  "monthlyNumberOfDocumentsAllowed": 0,
  "numberOfSecretsAllowed": 0,
  "monthlyUsageSummary": {},
  "numberOfAppClientsCreated": 0,
  "numberOfAssetsCreated": 0,
  "updatedTime": "string",
  "numberOfWorkflowsAllowed": 0,
  "updatedBy": "string",
  "monthlyNumberOfWorkflowExecutionsAllowed": 0,
  "monthlyNumberOfDataBundlesCreated": 0,
  "numberOfUsersCreated": 0,
  "monthlyNumberOfPredictionsCreated": 0,
  "numberOfDatasetsCreated": 0,
  "numberOfTransitionsAllowed": 0,
  "monthlyNumberOfTransitionExecutionsCreated": 0,
  "numberOfModelsAllowed": 0,
  "monthlyNumberOfDocumentsCreated": 0,
  "numberOfSecretsCreated": 0,
  "name": "string",
  "numberOfAppClientsAllowed": 0,
  "numberOfAssetsAllowed": 0
}

```

organization

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|numberOfWorkflowsCreated|integer|true|none|none|
|monthlyNumberOfWorkflowExecutionsCreated|integer|true|none|none|
|description|string¦null|true|none|none|
|numberOfUsersAllowed|integer|true|none|none|
|monthlyNumberOfPredictionsAllowed|integer|true|none|none|
|numberOfDatasetsAllowed|integer|false|none|none|
|monthlyNumberOfDataBundlesAllowed|integer|true|none|none|
|organizationId|string|true|none|none|
|numberOfModelsCreated|integer|true|none|none|
|numberOfTransitionsCreated|integer|true|none|none|
|monthlyNumberOfTransitionExecutionsAllowed|integer|true|none|none|
|monthlyNumberOfDocumentsAllowed|integer|true|none|none|
|numberOfSecretsAllowed|integer|true|none|none|
|monthlyUsageSummary|object|true|none|none|
|numberOfAppClientsCreated|integer|true|none|none|
|numberOfAssetsCreated|integer|true|none|none|
|updatedTime|string¦null|true|none|none|
|numberOfWorkflowsAllowed|integer|true|none|none|
|updatedBy|string¦null|true|none|none|
|monthlyNumberOfWorkflowExecutionsAllowed|integer|true|none|none|
|monthlyNumberOfDataBundlesCreated|integer|true|none|none|
|numberOfUsersCreated|integer|true|none|none|
|monthlyNumberOfPredictionsCreated|integer|true|none|none|
|numberOfDatasetsCreated|integer|false|none|none|
|numberOfTransitionsAllowed|integer|true|none|none|
|monthlyNumberOfTransitionExecutionsCreated|integer|true|none|none|
|numberOfModelsAllowed|integer|true|none|none|
|monthlyNumberOfDocumentsCreated|integer|true|none|none|
|numberOfSecretsCreated|integer|true|none|none|
|name|string¦null|true|none|none|
|numberOfAppClientsAllowed|integer|true|none|none|
|numberOfAssetsAllowed|integer|true|none|none|

<h2 id="tocS_User">User</h2>
<a id="schemauser"></a>
<a id="schema_User"></a>
<a id="tocSuser"></a>
<a id="tocsuser"></a>

```json
{
  "updatedTime": "string",
  "updatedBy": "string",
  "createdBy": "string",
  "name": "string",
  "createdTime": "string",
  "avatar": "string",
  "userId": "string",
  "email": "string"
}

```

user

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|updatedTime|string¦null|true|none|none|
|updatedBy|string¦null|true|none|none|
|createdBy|string¦null|true|none|none|
|name|string¦null|false|none|none|
|createdTime|string¦null|true|none|none|
|avatar|string¦null|false|none|none|
|userId|string|true|none|none|
|email|string|true|none|none|

<h2 id="tocS_PostHeartbeats">PostHeartbeats</h2>
<a id="schemapostheartbeats"></a>
<a id="schema_PostHeartbeats"></a>
<a id="tocSpostheartbeats"></a>
<a id="tocspostheartbeats"></a>

```json
{}

```

POST /transitions/{transitionId}/executions/{executionId}/heartbeats

### Properties

*None*

<h2 id="tocS_PatchDataBundleId">PatchDataBundleId</h2>
<a id="schemapatchdatabundleid"></a>
<a id="schema_PatchDataBundleId"></a>
<a id="tocSpatchdatabundleid"></a>
<a id="tocspatchdatabundleid"></a>

```json
{
  "name": "string",
  "description": "string"
}

```

PATCH /models/{modelId}/dataBundles/{dataBundleId}

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|name|string¦null|false|none|none|
|description|string¦null|false|none|none|

<h2 id="tocS_PostPredictions">PostPredictions</h2>
<a id="schemapostpredictions"></a>
<a id="schema_PostPredictions"></a>
<a id="tocSpostpredictions"></a>
<a id="tocspostpredictions"></a>

```json
{
  "modelId": "string",
  "maxPages": 1,
  "documentId": "string",
  "autoRotate": true,
  "imageQuality": "LOW"
}

```

POST /predictions

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|modelId|string|true|none|none|
|maxPages|integer|false|none|none|
|documentId|string|true|none|none|
|autoRotate|boolean|false|none|none|
|imageQuality|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|imageQuality|LOW|
|imageQuality|HIGH|

<h2 id="tocS_Empty">Empty</h2>
<a id="schemaempty"></a>
<a id="schema_Empty"></a>
<a id="tocSempty"></a>
<a id="tocsempty"></a>

```json
{}

```

Empty Schema

### Properties

*None*

<h2 id="tocS_Assets">Assets</h2>
<a id="schemaassets"></a>
<a id="schema_Assets"></a>
<a id="tocSassets"></a>
<a id="tocsassets"></a>

```json
{
  "assets": [
    {
      "updatedTime": "string",
      "updatedBy": "string",
      "createdBy": "string",
      "assetId": "string",
      "name": "string",
      "description": "string",
      "createdTime": "string",
      "content": "string"
    }
  ],
  "nextToken": "string"
}

```

assets

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|assets|[object]|true|none|none|
|» updatedTime|string¦null|true|none|none|
|» updatedBy|string¦null|true|none|none|
|» createdBy|string¦null|true|none|none|
|» assetId|string|true|none|none|
|» name|string¦null|true|none|none|
|» description|string¦null|true|none|none|
|» createdTime|string¦null|true|none|none|
|» content|string|false|none|none|
|nextToken|string¦null|true|none|none|

<h2 id="tocS_AppClients">AppClients</h2>
<a id="schemaappclients"></a>
<a id="schema_AppClients"></a>
<a id="tocSappclients"></a>
<a id="tocsappclients"></a>

```json
{
  "nextToken": "string",
  "appClients": [
    {
      "hasSecret": true,
      "updatedTime": "string",
      "clientId": "string",
      "updatedBy": "string",
      "apiKey": "string",
      "logoutUrls": [
        "string"
      ],
      "description": "string",
      "callbackUrls": [
        "string"
      ],
      "loginUrls": [
        "string"
      ],
      "defaultLoginUrl": "string",
      "createdBy": "string",
      "name": "string",
      "createdTime": "string",
      "clientSecret": "string",
      "appClientId": "string"
    }
  ]
}

```

appClients

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|nextToken|string¦null|true|none|none|
|appClients|[object]|true|none|none|
|» hasSecret|boolean|true|none|none|
|» updatedTime|string¦null|true|none|none|
|» clientId|string|true|none|none|
|» updatedBy|string¦null|true|none|none|
|» apiKey|string¦null|true|none|none|
|» logoutUrls|[string]|true|none|none|
|» description|string¦null|true|none|none|
|» callbackUrls|[string]|true|none|none|
|» loginUrls|[string]|true|none|none|
|» defaultLoginUrl|string¦null|true|none|none|
|» createdBy|string¦null|true|none|none|
|» name|string¦null|true|none|none|
|» createdTime|string¦null|true|none|none|
|» clientSecret|string|false|none|none|
|» appClientId|string|true|none|none|

<h2 id="tocS_PostSecrets">PostSecrets</h2>
<a id="schemapostsecrets"></a>
<a id="schema_PostSecrets"></a>
<a id="tocSpostsecrets"></a>
<a id="tocspostsecrets"></a>

```json
{
  "data": {},
  "name": "string",
  "description": "string"
}

```

POST /secrets

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|data|object|true|none|none|
|name|string¦null|false|none|none|
|description|string¦null|false|none|none|

<h2 id="tocS_PatchSecretId">PatchSecretId</h2>
<a id="schemapatchsecretid"></a>
<a id="schema_PatchSecretId"></a>
<a id="tocSpatchsecretid"></a>
<a id="tocspatchsecretid"></a>

```json
{
  "data": {},
  "name": "string",
  "description": "string"
}

```

PATCH /secrets/{secretId}

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|data|object|false|none|none|
|name|string¦null|false|none|none|
|description|string¦null|false|none|none|

<h2 id="tocS_PatchModelId">PatchModelId</h2>
<a id="schemapatchmodelid"></a>
<a id="schema_PatchModelId"></a>
<a id="tocSpatchmodelid"></a>
<a id="tocspatchmodelid"></a>

```json
{
  "preprocessConfig": {
    "maxPages": 1,
    "autoRotate": true,
    "imageQuality": "LOW"
  },
  "width": 97,
  "name": "string",
  "description": "string",
  "fieldConfig": {
    "property1": {
      "description": "string",
      "type": "date",
      "maxLength": 1
    },
    "property2": {
      "description": "string",
      "type": "date",
      "maxLength": 1
    }
  },
  "height": 97,
  "status": "active"
}

```

PATCH /models/modelId

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|preprocessConfig|object|false|none|none|
|» maxPages|integer|true|none|none|
|» autoRotate|boolean|true|none|none|
|» imageQuality|string|true|none|none|
|width|integer|false|none|none|
|name|string¦null|false|none|none|
|description|string¦null|false|none|none|
|fieldConfig|object|false|none|none|
|» **additionalProperties**|object|false|none|none|
|»» description|string¦null|false|none|none|
|»» type|string|true|none|none|
|»» maxLength|integer|true|none|none|
|height|integer|false|none|none|
|status|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|imageQuality|LOW|
|imageQuality|HIGH|
|type|date|
|type|amount|
|type|number|
|type|letter|
|type|phone|
|type|alphanum|
|type|alphanumext|
|type|all|
|type|string|
|type|digits|
|status|active|
|status|training|
|status|inactive|

<h2 id="tocS_PostDatasets">PostDatasets</h2>
<a id="schemapostdatasets"></a>
<a id="schema_PostDatasets"></a>
<a id="tocSpostdatasets"></a>
<a id="tocspostdatasets"></a>

```json
{
  "retentionInDays": 1,
  "name": "string",
  "description": "string",
  "containsPersonallyIdentifiableInformation": true
}

```

POST /datasets

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|retentionInDays|integer|false|none|none|
|name|string¦null|false|none|none|
|description|string¦null|false|none|none|
|containsPersonallyIdentifiableInformation|boolean|false|none|none|

<h2 id="tocS_Dataset">Dataset</h2>
<a id="schemadataset"></a>
<a id="schema_Dataset"></a>
<a id="tocSdataset"></a>
<a id="tocsdataset"></a>

```json
{
  "updatedTime": "string",
  "retentionInDays": 1825,
  "updatedBy": "string",
  "groundTruthSummary": {},
  "description": "string",
  "storageLocation": "EU",
  "version": 0,
  "createdBy": "string",
  "numberOfDocuments": 0,
  "name": "string",
  "datasetId": "string",
  "createdTime": "string",
  "containsPersonallyIdentifiableInformation": true
}

```

dataset

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|updatedTime|string¦null|true|none|none|
|retentionInDays|integer|true|none|none|
|updatedBy|string¦null|true|none|none|
|groundTruthSummary|object|true|none|none|
|description|string¦null|true|none|none|
|storageLocation|string|true|none|none|
|version|integer|true|none|none|
|createdBy|string¦null|true|none|none|
|numberOfDocuments|integer|true|none|none|
|name|string¦null|false|none|none|
|datasetId|string|true|none|none|
|createdTime|string¦null|true|none|none|
|containsPersonallyIdentifiableInformation|boolean|true|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|storageLocation|EU|

<h2 id="tocS_Error">Error</h2>
<a id="schemaerror"></a>
<a id="schema_Error"></a>
<a id="tocSerror"></a>
<a id="tocserror"></a>

```json
{
  "message": "string"
}

```

Error Schema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|message|string|false|none|none|

<h2 id="tocS_PatchWorkflowId">PatchWorkflowId</h2>
<a id="schemapatchworkflowid"></a>
<a id="schema_PatchWorkflowId"></a>
<a id="tocSpatchworkflowid"></a>
<a id="tocspatchworkflowid"></a>

```json
{
  "completedConfig": {
    "environmentSecrets": [
      "string"
    ],
    "environment": {
      "property1": "string",
      "property2": "string"
    },
    "imageUrl": "string",
    "secretId": "string"
  },
  "name": "string",
  "description": "string",
  "errorConfig": {
    "manualRetry": true,
    "email": "string"
  }
}

```

PATCH /workflows/{workflowId}

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|completedConfig|object|false|none|none|
|» environmentSecrets|[string]|false|none|none|
|» environment|object|false|none|none|
|»» **additionalProperties**|string|false|none|none|
|» imageUrl|string|true|none|none|
|» secretId|string|false|none|none|
|name|string¦null|false|none|none|
|description|string¦null|false|none|none|
|errorConfig|object|false|none|none|
|» manualRetry|boolean|false|none|none|
|» email|string|false|none|none|

<h2 id="tocS_Logs">Logs</h2>
<a id="schemalogs"></a>
<a id="schema_Logs"></a>
<a id="tocSlogs"></a>
<a id="tocslogs"></a>

```json
{
  "transitionId": "string",
  "nextToken": "string",
  "transitionExecutionId": "string",
  "workflowExecutionId": "string",
  "logs": [
    {
      "transitionId": "string",
      "transitionExecutionId": "string",
      "logId": "string",
      "workflowExecutionId": "string",
      "startTime": "string",
      "workflowId": "string",
      "events": [
        {}
      ]
    }
  ],
  "workflowId": "string",
  "order": "ascending"
}

```

logs

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|transitionId|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|nextToken|string¦null|true|none|none|
|transitionExecutionId|string|false|none|none|
|workflowExecutionId|string|false|none|none|
|logs|[object]|true|none|none|
|» transitionId|any|true|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|string|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» transitionExecutionId|string¦null|true|none|none|
|» logId|string|true|none|none|
|» workflowExecutionId|string¦null|true|none|none|
|» startTime|string¦null|true|none|none|
|» workflowId|string¦null|true|none|none|
|» events|[object]|false|none|none|
|workflowId|string|false|none|none|
|order|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|order|ascending|
|order|descending|

<h2 id="tocS_PostTransitions">PostTransitions</h2>
<a id="schemaposttransitions"></a>
<a id="schema_PostTransitions"></a>
<a id="tocSposttransitions"></a>
<a id="tocsposttransitions"></a>

```json
{
  "outputJsonSchema": {},
  "name": "string",
  "description": "string",
  "transitionType": "docker",
  "inputJsonSchema": {},
  "parameters": {
    "environmentSecrets": [
      "string"
    ],
    "environment": {
      "property1": "string",
      "property2": "string"
    },
    "memory": 512,
    "imageUrl": "string",
    "secretId": "string",
    "cpu": 256
  },
  "timeoutInSeconds": 60
}

```

POST /transitions

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|outputJsonSchema|object|false|none|none|
|name|string¦null|false|none|none|
|description|string¦null|false|none|none|
|transitionType|string|true|none|none|
|inputJsonSchema|object|false|none|none|
|parameters|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|object|false|none|none|
|»» environmentSecrets|[string]|false|none|none|
|»» environment|object|false|none|none|
|»»» **additionalProperties**|string|false|none|none|
|»» memory|integer|false|none|none|
|»» imageUrl|string|true|none|none|
|»» secretId|string|false|none|none|
|»» cpu|integer|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|object|false|none|none|
|»» assets|object|false|none|none|
|»»» **additionalProperties**|string|false|none|none|
|»»» jsRemoteComponent|string|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|timeoutInSeconds|integer|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|transitionType|docker|
|transitionType|manual|
|memory|512|
|memory|1024|
|memory|2048|
|cpu|256|

<h2 id="tocS_PostAssets">PostAssets</h2>
<a id="schemapostassets"></a>
<a id="schema_PostAssets"></a>
<a id="tocSpostassets"></a>
<a id="tocspostassets"></a>

```json
{
  "name": "string",
  "description": "string",
  "content": "string"
}

```

POST /assets

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|name|string¦null|false|none|none|
|description|string¦null|false|none|none|
|content|string|true|none|none|

<h2 id="tocS_PostUsers">PostUsers</h2>
<a id="schemapostusers"></a>
<a id="schema_PostUsers"></a>
<a id="tocSpostusers"></a>
<a id="tocspostusers"></a>

```json
{
  "name": "string",
  "avatar": "string",
  "email": "string",
  "appClientId": "string"
}

```

POST /users

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|name|string¦null|false|none|none|
|avatar|string¦null|false|none|none|
|email|string|true|none|none|
|appClientId|string|false|none|none|

<h2 id="tocS_PostDocuments">PostDocuments</h2>
<a id="schemapostdocuments"></a>
<a id="schema_PostDocuments"></a>
<a id="tocSpostdocuments"></a>
<a id="tocspostdocuments"></a>

```json
{
  "groundTruth": [
    {
      "label": "string",
      "value": "string"
    }
  ],
  "consentId": "string",
  "retentionInDays": 1,
  "datasetId": "string",
  "contentType": "application/pdf",
  "content": "string"
}

```

POST /documents

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|groundTruth|[object]|false|none|none|
|» label|string|true|none|none|
|» value|any|true|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|string¦null|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|boolean|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|consentId|string|false|none|none|
|retentionInDays|integer|false|none|none|
|datasetId|string|false|none|none|
|contentType|string|true|none|none|
|content|string|true|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|contentType|application/pdf|
|contentType|image/jpeg|
|contentType|image/png|
|contentType|image/tiff|

<h2 id="tocS_TransitionExecution">TransitionExecution</h2>
<a id="schematransitionexecution"></a>
<a id="schema_TransitionExecution"></a>
<a id="tocStransitionexecution"></a>
<a id="tocstransitionexecution"></a>

```json
{
  "executionId": "string",
  "input": {},
  "transitionId": "string",
  "startTime": "string",
  "logId": "string",
  "endTime": "string",
  "completedBy": "string",
  "status": "running"
}

```

transition-execution

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|executionId|string|true|none|none|
|input|object|true|none|none|
|transitionId|any|true|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|startTime|string¦null|false|none|none|
|logId|string¦null|false|none|none|
|endTime|string¦null|false|none|none|
|completedBy|string¦null|true|none|none|
|status|string|true|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|status|running|
|status|succeeded|
|status|failed|
|status|rejected|
|status|retry|

<h2 id="tocS_PatchUserId">PatchUserId</h2>
<a id="schemapatchuserid"></a>
<a id="schema_PatchUserId"></a>
<a id="tocSpatchuserid"></a>
<a id="tocspatchuserid"></a>

```json
{
  "name": "string",
  "avatar": "string"
}

```

PATCH /users/{userId}

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|name|string¦null|false|none|none|
|avatar|string¦null|false|none|none|

<h2 id="tocS_PatchWorkflowExecutionId">PatchWorkflowExecutionId</h2>
<a id="schemapatchworkflowexecutionid"></a>
<a id="schema_PatchWorkflowExecutionId"></a>
<a id="tocSpatchworkflowexecutionid"></a>
<a id="tocspatchworkflowexecutionid"></a>

```json
{
  "nextTransitionId": "string"
}

```

PATCH workflows/{workflowId}/executions/{executionId}

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|nextTransitionId|any|true|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

<h2 id="tocS_TransitionExecutions">TransitionExecutions</h2>
<a id="schematransitionexecutions"></a>
<a id="schema_TransitionExecutions"></a>
<a id="tocStransitionexecutions"></a>
<a id="tocstransitionexecutions"></a>

```json
{
  "executions": [
    {
      "executionId": "string",
      "input": {},
      "transitionId": "string",
      "startTime": "string",
      "logId": "string",
      "endTime": "string",
      "completedBy": "string",
      "status": "running"
    }
  ],
  "transitionId": "string",
  "nextToken": "string",
  "status": [
    "running"
  ]
}

```

transition-executions

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|executions|[object]|true|none|none|
|» executionId|string|true|none|none|
|» input|object|true|none|none|
|» transitionId|any|true|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|string|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» startTime|string¦null|false|none|none|
|» logId|string¦null|false|none|none|
|» endTime|string¦null|false|none|none|
|» completedBy|string¦null|true|none|none|
|» status|string|true|none|none|
|transitionId|any|true|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|nextToken|string¦null|true|none|none|
|status|[string]|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|status|running|
|status|succeeded|
|status|failed|
|status|rejected|
|status|retry|

<h2 id="tocS_Model">Model</h2>
<a id="schemamodel"></a>
<a id="schema_Model"></a>
<a id="tocSmodel"></a>
<a id="tocsmodel"></a>

```json
{
  "updatedTime": "string",
  "updatedBy": "string",
  "modelId": "string",
  "description": "string",
  "fieldConfig": {
    "property1": {
      "description": "string",
      "type": "date",
      "maxLength": 1
    },
    "property2": {
      "description": "string",
      "type": "date",
      "maxLength": 1
    }
  },
  "preprocessConfig": {
    "maxPages": 1,
    "autoRotate": true,
    "imageQuality": "LOW"
  },
  "createdBy": "string",
  "name": "string",
  "width": 97,
  "numberOfDataBundles": 0,
  "createdTime": "string",
  "height": 97,
  "status": "active"
}

```

model

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|updatedTime|string¦null|true|none|none|
|updatedBy|string¦null|true|none|none|
|modelId|string|true|none|none|
|description|string¦null|true|none|none|
|fieldConfig|object|true|none|none|
|» **additionalProperties**|object|false|none|none|
|»» description|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»»» *anonymous*|string|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» type|string|true|none|none|
|»» maxLength|integer|true|none|none|
|preprocessConfig|object|true|none|none|
|» maxPages|integer|true|none|none|
|» autoRotate|boolean|true|none|none|
|» imageQuality|string|true|none|none|
|createdBy|string¦null|true|none|none|
|name|string¦null|true|none|none|
|width|integer|true|none|none|
|numberOfDataBundles|integer|true|none|none|
|createdTime|string¦null|true|none|none|
|height|integer|true|none|none|
|status|string|true|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|type|date|
|type|amount|
|type|number|
|type|letter|
|type|phone|
|type|alphanum|
|type|alphanumext|
|type|all|
|type|string|
|type|digits|
|imageQuality|LOW|
|imageQuality|HIGH|
|status|active|
|status|training|
|status|inactive|

<h2 id="tocS_Transition">Transition</h2>
<a id="schematransition"></a>
<a id="schema_Transition"></a>
<a id="tocStransition"></a>
<a id="tocstransition"></a>

```json
{
  "updatedTime": "string",
  "updatedBy": "string",
  "transitionId": "string",
  "description": "string",
  "inputJsonSchema": {},
  "timeoutInSeconds": 60,
  "outputJsonSchema": {},
  "assets": {
    "jsRemoteComponent": "string",
    "property1": "string",
    "property2": "string"
  },
  "createdBy": "string",
  "name": "string",
  "createdTime": "string",
  "transitionType": "docker",
  "parameters": {}
}

```

transition

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|updatedTime|string¦null|true|none|none|
|updatedBy|string¦null|true|none|none|
|transitionId|any|true|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|description|string¦null|true|none|none|
|inputJsonSchema|object|false|none|none|
|timeoutInSeconds|integer|true|none|none|
|outputJsonSchema|object|false|none|none|
|assets|object|false|none|none|
|» **additionalProperties**|string|false|none|none|
|» jsRemoteComponent|string|false|none|none|
|createdBy|string¦null|true|none|none|
|name|string¦null|true|none|none|
|createdTime|string¦null|true|none|none|
|transitionType|string|true|none|none|
|parameters|object|true|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|transitionType|docker|
|transitionType|manual|

<h2 id="tocS_PatchAssetId">PatchAssetId</h2>
<a id="schemapatchassetid"></a>
<a id="schema_PatchAssetId"></a>
<a id="tocSpatchassetid"></a>
<a id="tocspatchassetid"></a>

```json
{
  "name": "string",
  "description": "string",
  "content": "string"
}

```

PATCH /assets/assetId

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|name|string¦null|false|none|none|
|description|string¦null|false|none|none|
|content|string|false|none|none|

<h2 id="tocS_PatchOrganizationId">PatchOrganizationId</h2>
<a id="schemapatchorganizationid"></a>
<a id="schema_PatchOrganizationId"></a>
<a id="tocSpatchorganizationid"></a>
<a id="tocspatchorganizationid"></a>

```json
{
  "name": "string",
  "description": "string"
}

```

PATCH /organizations/organizationId

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|name|string¦null|false|none|none|
|description|string¦null|false|none|none|

<h2 id="tocS_PostWorkflows">PostWorkflows</h2>
<a id="schemapostworkflows"></a>
<a id="schema_PostWorkflows"></a>
<a id="tocSpostworkflows"></a>
<a id="tocspostworkflows"></a>

```json
{
  "completedConfig": {
    "environmentSecrets": [
      "string"
    ],
    "environment": {
      "property1": "string",
      "property2": "string"
    },
    "imageUrl": "string",
    "secretId": "string"
  },
  "name": "string",
  "description": "string",
  "specification": {
    "language": "ASL",
    "definition": {},
    "version": "1.0.0"
  },
  "errorConfig": {
    "manualRetry": true,
    "email": "string"
  }
}

```

POST /workflows

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|completedConfig|object|false|none|none|
|» environmentSecrets|[string]|false|none|none|
|» environment|object|false|none|none|
|»» **additionalProperties**|string|false|none|none|
|» imageUrl|string|true|none|none|
|» secretId|string|false|none|none|
|name|string¦null|false|none|none|
|description|string¦null|false|none|none|
|specification|object|true|none|none|
|» language|string|false|none|none|
|» definition|object|true|none|none|
|» version|string|false|none|none|
|errorConfig|object|false|none|none|
|» manualRetry|boolean|false|none|none|
|» email|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|language|ASL|
|version|1.0.0|

<h2 id="tocS_PostDataBundles">PostDataBundles</h2>
<a id="schemapostdatabundles"></a>
<a id="schema_PostDataBundles"></a>
<a id="tocSpostdatabundles"></a>
<a id="tocspostdatabundles"></a>

```json
{
  "datasetIds": [
    "string"
  ],
  "name": "string",
  "description": "string"
}

```

POST /models/{modelId}/dataBundles

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|datasetIds|[string]|false|none|none|
|name|string¦null|false|none|none|
|description|string¦null|false|none|none|

<h2 id="tocS_PatchDatasetId">PatchDatasetId</h2>
<a id="schemapatchdatasetid"></a>
<a id="schema_PatchDatasetId"></a>
<a id="tocSpatchdatasetid"></a>
<a id="tocspatchdatasetid"></a>

```json
{
  "name": "string",
  "description": "string"
}

```

PATCH /datasets/{datasetId}

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|name|string¦null|false|none|none|
|description|string¦null|false|none|none|

