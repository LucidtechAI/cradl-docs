#### GET /appClients





| Header name | Header value |
| --- | --- |
| Authorization | Bearer &lt;your access token here&gt; |
| x-api-key | &lt;your api key here&gt; |


| Query name | Query value |
| --- | --- |
| nextToken | String value as returned by a previous list operation |
| maxResults | Integer representing maximum number of resources to list |





##### Response body JSON Schema
```json
{
  "title": "appClients",
  "required": [
    "appClients",
    "nextToken"
  ],
  "type": "object",
  "properties": {
    "nextToken": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "appClients": {
      "type": "array",
      "items": {
        "required": [
          "apiKey",
          "appClientId",
          "callbackUrls",
          "clientId",
          "createdBy",
          "createdTime",
          "defaultLoginUrl",
          "description",
          "hasSecret",
          "loginUrls",
          "logoutUrls",
          "name",
          "updatedBy",
          "updatedTime"
        ],
        "type": "object",
        "properties": {
          "hasSecret": {
            "type": "boolean"
          },
          "updatedTime": {
            "pattern": "^[0-9]{4}-?[0-9]{2}-?[0-9]{2}( |T)?[0-9]{2}:?[0-9]{2}:?[0-9]{2}(.[0-9]{1,6})?(Z|[+][0-9]{2}(:|)[0-9]{2})$",
            "type": "string",
            "nullable": true
          },
          "clientId": {
            "type": "string"
          },
          "updatedBy": {
            "maxLength": 4096,
            "type": "string",
            "nullable": true
          },
          "apiKey": {
            "maxLength": 4096,
            "type": "string",
            "nullable": true
          },
          "logoutUrls": {
            "type": "array",
            "items": {
              "pattern": "^http://localhost.*|^https://.*",
              "type": "string"
            }
          },
          "description": {
            "maxLength": 4096,
            "type": "string",
            "nullable": true
          },
          "callbackUrls": {
            "type": "array",
            "items": {
              "pattern": "^http://localhost.*|^https://.*",
              "type": "string"
            }
          },
          "loginUrls": {
            "type": "array",
            "items": {
              "pattern": "^http://localhost.*|^https://.*",
              "type": "string"
            }
          },
          "defaultLoginUrl": {
            "pattern": "^http://localhost.*|^https://.*",
            "type": "string",
            "nullable": true
          },
          "createdBy": {
            "maxLength": 4096,
            "type": "string",
            "nullable": true
          },
          "name": {
            "maxLength": 4096,
            "type": "string",
            "nullable": true
          },
          "createdTime": {
            "pattern": "^[0-9]{4}-?[0-9]{2}-?[0-9]{2}( |T)?[0-9]{2}:?[0-9]{2}:?[0-9]{2}(.[0-9]{1,6})?(Z|[+][0-9]{2}(:|)[0-9]{2})$",
            "type": "string",
            "nullable": true
          },
          "clientSecret": {
            "type": "string"
          },
          "appClientId": {
            "pattern": "^las:app-client:[a-f0-9]{32}$",
            "type": "string"
          }
        },
        "additionalProperties": false
      }
    }
  },
  "additionalProperties": false
}
```


#### POST /appClients





| Header name | Header value |
| --- | --- |
| Content-Type | application/json |
| Authorization | Bearer &lt;your access token here&gt; |
| x-api-key | &lt;your api key here&gt; |





##### Request body JSON Schema
```json
{
  "title": "POST /appClients",
  "type": "object",
  "properties": {
    "generateSecret": {
      "type": "boolean",
      "default": true
    },
    "logoutUrls": {
      "type": "array",
      "items": {
        "pattern": "^http://localhost.*|^https://.*",
        "type": "string"
      }
    },
    "name": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "callbackUrls": {
      "type": "array",
      "items": {
        "pattern": "^http://localhost.*|^https://.*",
        "type": "string"
      }
    },
    "description": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "loginUrls": {
      "type": "array",
      "items": {
        "pattern": "^http://localhost.*|^https://.*",
        "type": "string"
      }
    },
    "defaultLoginUrl": {
      "pattern": "^http://localhost.*|^https://.*",
      "type": "string"
    }
  },
  "additionalProperties": false
}
```


##### Response body JSON Schema
```json
{
  "title": "appClient",
  "required": [
    "apiKey",
    "appClientId",
    "callbackUrls",
    "clientId",
    "createdBy",
    "createdTime",
    "defaultLoginUrl",
    "description",
    "hasSecret",
    "loginUrls",
    "logoutUrls",
    "name",
    "updatedBy",
    "updatedTime"
  ],
  "type": "object",
  "properties": {
    "hasSecret": {
      "type": "boolean"
    },
    "updatedTime": {
      "pattern": "^[0-9]{4}-?[0-9]{2}-?[0-9]{2}( |T)?[0-9]{2}:?[0-9]{2}:?[0-9]{2}(.[0-9]{1,6})?(Z|[+][0-9]{2}(:|)[0-9]{2})$",
      "type": "string",
      "nullable": true
    },
    "clientId": {
      "type": "string"
    },
    "updatedBy": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "apiKey": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "logoutUrls": {
      "type": "array",
      "items": {
        "pattern": "^http://localhost.*|^https://.*",
        "type": "string"
      }
    },
    "description": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "callbackUrls": {
      "type": "array",
      "items": {
        "pattern": "^http://localhost.*|^https://.*",
        "type": "string"
      }
    },
    "loginUrls": {
      "type": "array",
      "items": {
        "pattern": "^http://localhost.*|^https://.*",
        "type": "string"
      }
    },
    "defaultLoginUrl": {
      "pattern": "^http://localhost.*|^https://.*",
      "type": "string",
      "nullable": true
    },
    "createdBy": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "name": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "createdTime": {
      "pattern": "^[0-9]{4}-?[0-9]{2}-?[0-9]{2}( |T)?[0-9]{2}:?[0-9]{2}:?[0-9]{2}(.[0-9]{1,6})?(Z|[+][0-9]{2}(:|)[0-9]{2})$",
      "type": "string",
      "nullable": true
    },
    "clientSecret": {
      "type": "string"
    },
    "appClientId": {
      "pattern": "^las:app-client:[a-f0-9]{32}$",
      "type": "string"
    }
  },
  "additionalProperties": false
}
```


#### DELETE /appClients/{appClientId}


| Path name | Path value |
| --- | --- |
| appClientId | Id of appClient on the form las:appClient:&lt;hex&gt; |


| Header name | Header value |
| --- | --- |
| Authorization | Bearer &lt;your access token here&gt; |
| x-api-key | &lt;your api key here&gt; |








##### Response body JSON Schema
```json
{
  "title": "appClient",
  "required": [
    "apiKey",
    "appClientId",
    "callbackUrls",
    "clientId",
    "createdBy",
    "createdTime",
    "defaultLoginUrl",
    "description",
    "hasSecret",
    "loginUrls",
    "logoutUrls",
    "name",
    "updatedBy",
    "updatedTime"
  ],
  "type": "object",
  "properties": {
    "hasSecret": {
      "type": "boolean"
    },
    "updatedTime": {
      "pattern": "^[0-9]{4}-?[0-9]{2}-?[0-9]{2}( |T)?[0-9]{2}:?[0-9]{2}:?[0-9]{2}(.[0-9]{1,6})?(Z|[+][0-9]{2}(:|)[0-9]{2})$",
      "type": "string",
      "nullable": true
    },
    "clientId": {
      "type": "string"
    },
    "updatedBy": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "apiKey": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "logoutUrls": {
      "type": "array",
      "items": {
        "pattern": "^http://localhost.*|^https://.*",
        "type": "string"
      }
    },
    "description": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "callbackUrls": {
      "type": "array",
      "items": {
        "pattern": "^http://localhost.*|^https://.*",
        "type": "string"
      }
    },
    "loginUrls": {
      "type": "array",
      "items": {
        "pattern": "^http://localhost.*|^https://.*",
        "type": "string"
      }
    },
    "defaultLoginUrl": {
      "pattern": "^http://localhost.*|^https://.*",
      "type": "string",
      "nullable": true
    },
    "createdBy": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "name": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "createdTime": {
      "pattern": "^[0-9]{4}-?[0-9]{2}-?[0-9]{2}( |T)?[0-9]{2}:?[0-9]{2}:?[0-9]{2}(.[0-9]{1,6})?(Z|[+][0-9]{2}(:|)[0-9]{2})$",
      "type": "string",
      "nullable": true
    },
    "clientSecret": {
      "type": "string"
    },
    "appClientId": {
      "pattern": "^las:app-client:[a-f0-9]{32}$",
      "type": "string"
    }
  },
  "additionalProperties": false
}
```


#### PATCH /appClients/{appClientId}


| Path name | Path value |
| --- | --- |
| appClientId | Id of appClient on the form las:appClient:&lt;hex&gt; |


| Header name | Header value |
| --- | --- |
| Content-Type | application/json |
| Authorization | Bearer &lt;your access token here&gt; |
| x-api-key | &lt;your api key here&gt; |





##### Request body JSON Schema
```json
{
  "title": "PATCH /appClients/{appClientId}",
  "minProperties": 1,
  "type": "object",
  "properties": {
    "name": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "description": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "loginUrls": {
      "type": "array",
      "items": {
        "pattern": "^http://localhost.*|^https://.*",
        "type": "string"
      }
    },
    "defaultLoginUrl": {
      "pattern": "^http://localhost.*|^https://.*",
      "type": "string"
    }
  },
  "additionalProperties": false
}
```


##### Response body JSON Schema
```json
{
  "title": "appClient",
  "required": [
    "apiKey",
    "appClientId",
    "callbackUrls",
    "clientId",
    "createdBy",
    "createdTime",
    "defaultLoginUrl",
    "description",
    "hasSecret",
    "loginUrls",
    "logoutUrls",
    "name",
    "updatedBy",
    "updatedTime"
  ],
  "type": "object",
  "properties": {
    "hasSecret": {
      "type": "boolean"
    },
    "updatedTime": {
      "pattern": "^[0-9]{4}-?[0-9]{2}-?[0-9]{2}( |T)?[0-9]{2}:?[0-9]{2}:?[0-9]{2}(.[0-9]{1,6})?(Z|[+][0-9]{2}(:|)[0-9]{2})$",
      "type": "string",
      "nullable": true
    },
    "clientId": {
      "type": "string"
    },
    "updatedBy": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "apiKey": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "logoutUrls": {
      "type": "array",
      "items": {
        "pattern": "^http://localhost.*|^https://.*",
        "type": "string"
      }
    },
    "description": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "callbackUrls": {
      "type": "array",
      "items": {
        "pattern": "^http://localhost.*|^https://.*",
        "type": "string"
      }
    },
    "loginUrls": {
      "type": "array",
      "items": {
        "pattern": "^http://localhost.*|^https://.*",
        "type": "string"
      }
    },
    "defaultLoginUrl": {
      "pattern": "^http://localhost.*|^https://.*",
      "type": "string",
      "nullable": true
    },
    "createdBy": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "name": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "createdTime": {
      "pattern": "^[0-9]{4}-?[0-9]{2}-?[0-9]{2}( |T)?[0-9]{2}:?[0-9]{2}:?[0-9]{2}(.[0-9]{1,6})?(Z|[+][0-9]{2}(:|)[0-9]{2})$",
      "type": "string",
      "nullable": true
    },
    "clientSecret": {
      "type": "string"
    },
    "appClientId": {
      "pattern": "^las:app-client:[a-f0-9]{32}$",
      "type": "string"
    }
  },
  "additionalProperties": false
}
```


#### GET /assets





| Header name | Header value |
| --- | --- |
| Authorization | Bearer &lt;your access token here&gt; |
| x-api-key | &lt;your api key here&gt; |


| Query name | Query value |
| --- | --- |
| nextToken | String value as returned by a previous list operation |
| maxResults | Integer representing maximum number of resources to list |





##### Response body JSON Schema
```json
{
  "title": "assets",
  "required": [
    "assets",
    "nextToken"
  ],
  "type": "object",
  "properties": {
    "assets": {
      "type": "array",
      "items": {
        "required": [
          "assetId",
          "createdBy",
          "createdTime",
          "description",
          "name",
          "updatedBy",
          "updatedTime"
        ],
        "type": "object",
        "properties": {
          "updatedTime": {
            "pattern": "^[0-9]{4}-?[0-9]{2}-?[0-9]{2}( |T)?[0-9]{2}:?[0-9]{2}:?[0-9]{2}(.[0-9]{1,6})?(Z|[+][0-9]{2}(:|)[0-9]{2})$",
            "type": "string",
            "nullable": true
          },
          "updatedBy": {
            "maxLength": 4096,
            "type": "string",
            "nullable": true
          },
          "createdBy": {
            "maxLength": 4096,
            "type": "string",
            "nullable": true
          },
          "assetId": {
            "pattern": "^las:asset:[a-f0-9]{32}$",
            "type": "string"
          },
          "name": {
            "maxLength": 4096,
            "type": "string",
            "nullable": true
          },
          "description": {
            "maxLength": 4096,
            "type": "string",
            "nullable": true
          },
          "createdTime": {
            "pattern": "^[0-9]{4}-?[0-9]{2}-?[0-9]{2}( |T)?[0-9]{2}:?[0-9]{2}:?[0-9]{2}(.[0-9]{1,6})?(Z|[+][0-9]{2}(:|)[0-9]{2})$",
            "type": "string",
            "nullable": true
          },
          "content": {
            "minLength": 1,
            "type": "string"
          }
        },
        "additionalProperties": false
      }
    },
    "nextToken": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    }
  },
  "additionalProperties": false
}
```


#### POST /assets





| Header name | Header value |
| --- | --- |
| Content-Type | application/json |
| Authorization | Bearer &lt;your access token here&gt; |
| x-api-key | &lt;your api key here&gt; |





##### Request body JSON Schema
```json
{
  "title": "POST /assets",
  "required": [
    "content"
  ],
  "type": "object",
  "properties": {
    "name": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "description": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "content": {
      "maxLength": 6250000,
      "minLength": 1,
      "type": "string"
    }
  },
  "additionalProperties": false
}
```


##### Response body JSON Schema
```json
{
  "title": "asset",
  "required": [
    "assetId",
    "createdBy",
    "createdTime",
    "description",
    "name",
    "updatedBy",
    "updatedTime"
  ],
  "type": "object",
  "properties": {
    "updatedTime": {
      "pattern": "^[0-9]{4}-?[0-9]{2}-?[0-9]{2}( |T)?[0-9]{2}:?[0-9]{2}:?[0-9]{2}(.[0-9]{1,6})?(Z|[+][0-9]{2}(:|)[0-9]{2})$",
      "type": "string",
      "nullable": true
    },
    "updatedBy": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "createdBy": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "assetId": {
      "pattern": "^las:asset:[a-f0-9]{32}$",
      "type": "string"
    },
    "name": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "description": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "createdTime": {
      "pattern": "^[0-9]{4}-?[0-9]{2}-?[0-9]{2}( |T)?[0-9]{2}:?[0-9]{2}:?[0-9]{2}(.[0-9]{1,6})?(Z|[+][0-9]{2}(:|)[0-9]{2})$",
      "type": "string",
      "nullable": true
    },
    "content": {
      "minLength": 1,
      "type": "string"
    }
  },
  "additionalProperties": false
}
```


#### DELETE /assets/{assetId}


| Path name | Path value |
| --- | --- |
| assetId | Id of asset on the form las:asset:&lt;hex&gt; |


| Header name | Header value |
| --- | --- |
| Authorization | Bearer &lt;your access token here&gt; |
| x-api-key | &lt;your api key here&gt; |








##### Response body JSON Schema
```json
{
  "title": "asset",
  "required": [
    "assetId",
    "createdBy",
    "createdTime",
    "description",
    "name",
    "updatedBy",
    "updatedTime"
  ],
  "type": "object",
  "properties": {
    "updatedTime": {
      "pattern": "^[0-9]{4}-?[0-9]{2}-?[0-9]{2}( |T)?[0-9]{2}:?[0-9]{2}:?[0-9]{2}(.[0-9]{1,6})?(Z|[+][0-9]{2}(:|)[0-9]{2})$",
      "type": "string",
      "nullable": true
    },
    "updatedBy": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "createdBy": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "assetId": {
      "pattern": "^las:asset:[a-f0-9]{32}$",
      "type": "string"
    },
    "name": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "description": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "createdTime": {
      "pattern": "^[0-9]{4}-?[0-9]{2}-?[0-9]{2}( |T)?[0-9]{2}:?[0-9]{2}:?[0-9]{2}(.[0-9]{1,6})?(Z|[+][0-9]{2}(:|)[0-9]{2})$",
      "type": "string",
      "nullable": true
    },
    "content": {
      "minLength": 1,
      "type": "string"
    }
  },
  "additionalProperties": false
}
```


#### GET /assets/{assetId}


| Path name | Path value |
| --- | --- |
| assetId | Id of asset on the form las:asset:&lt;hex&gt; |


| Header name | Header value |
| --- | --- |
| Authorization | Bearer &lt;your access token here&gt; |
| x-api-key | &lt;your api key here&gt; |








##### Response body JSON Schema
```json
{
  "title": "asset",
  "required": [
    "assetId",
    "createdBy",
    "createdTime",
    "description",
    "name",
    "updatedBy",
    "updatedTime"
  ],
  "type": "object",
  "properties": {
    "updatedTime": {
      "pattern": "^[0-9]{4}-?[0-9]{2}-?[0-9]{2}( |T)?[0-9]{2}:?[0-9]{2}:?[0-9]{2}(.[0-9]{1,6})?(Z|[+][0-9]{2}(:|)[0-9]{2})$",
      "type": "string",
      "nullable": true
    },
    "updatedBy": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "createdBy": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "assetId": {
      "pattern": "^las:asset:[a-f0-9]{32}$",
      "type": "string"
    },
    "name": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "description": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "createdTime": {
      "pattern": "^[0-9]{4}-?[0-9]{2}-?[0-9]{2}( |T)?[0-9]{2}:?[0-9]{2}:?[0-9]{2}(.[0-9]{1,6})?(Z|[+][0-9]{2}(:|)[0-9]{2})$",
      "type": "string",
      "nullable": true
    },
    "content": {
      "minLength": 1,
      "type": "string"
    }
  },
  "additionalProperties": false
}
```


#### PATCH /assets/{assetId}


| Path name | Path value |
| --- | --- |
| assetId | Id of asset on the form las:asset:&lt;hex&gt; |


| Header name | Header value |
| --- | --- |
| Content-Type | application/json |
| Authorization | Bearer &lt;your access token here&gt; |
| x-api-key | &lt;your api key here&gt; |





##### Request body JSON Schema
```json
{
  "title": "PATCH /assets/assetId",
  "minProperties": 1,
  "type": "object",
  "properties": {
    "name": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "description": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "content": {
      "minLength": 1,
      "type": "string"
    }
  },
  "additionalProperties": false
}
```


##### Response body JSON Schema
```json
{
  "title": "asset",
  "required": [
    "assetId",
    "createdBy",
    "createdTime",
    "description",
    "name",
    "updatedBy",
    "updatedTime"
  ],
  "type": "object",
  "properties": {
    "updatedTime": {
      "pattern": "^[0-9]{4}-?[0-9]{2}-?[0-9]{2}( |T)?[0-9]{2}:?[0-9]{2}:?[0-9]{2}(.[0-9]{1,6})?(Z|[+][0-9]{2}(:|)[0-9]{2})$",
      "type": "string",
      "nullable": true
    },
    "updatedBy": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "createdBy": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "assetId": {
      "pattern": "^las:asset:[a-f0-9]{32}$",
      "type": "string"
    },
    "name": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "description": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "createdTime": {
      "pattern": "^[0-9]{4}-?[0-9]{2}-?[0-9]{2}( |T)?[0-9]{2}:?[0-9]{2}:?[0-9]{2}(.[0-9]{1,6})?(Z|[+][0-9]{2}(:|)[0-9]{2})$",
      "type": "string",
      "nullable": true
    },
    "content": {
      "minLength": 1,
      "type": "string"
    }
  },
  "additionalProperties": false
}
```


#### GET /batches





| Header name | Header value |
| --- | --- |
| Authorization | Bearer &lt;your access token here&gt; |
| x-api-key | &lt;your api key here&gt; |


| Query name | Query value |
| --- | --- |
| nextToken | String value as returned by a previous list operation |
| maxResults | Integer representing maximum number of resources to list |





##### Response body JSON Schema
```json
{
  "title": "batches",
  "required": [
    "batches",
    "nextToken"
  ],
  "type": "object",
  "properties": {
    "batches": {
      "type": "array",
      "items": {
        "required": [
          "batchId",
          "containsPersonallyIdentifiableInformation",
          "createdTime",
          "description",
          "numDocuments",
          "retentionInDays",
          "storageLocation"
        ],
        "type": "object",
        "properties": {
          "retentionInDays": {
            "maximum": 1825,
            "minimum": 0,
            "type": "integer"
          },
          "name": {
            "maxLength": 4096,
            "type": "string",
            "nullable": true
          },
          "description": {
            "maxLength": 4096,
            "type": "string",
            "nullable": true
          },
          "createdTime": {
            "pattern": "^[0-9]{4}-?[0-9]{2}-?[0-9]{2}( |T)?[0-9]{2}:?[0-9]{2}:?[0-9]{2}(.[0-9]{1,6})?(Z|[+][0-9]{2}(:|)[0-9]{2})$",
            "type": "string",
            "nullable": true
          },
          "storageLocation": {
            "type": "string",
            "enum": [
              "EU"
            ]
          },
          "containsPersonallyIdentifiableInformation": {
            "type": "boolean"
          },
          "batchId": {
            "pattern": "^las:batch:[a-f0-9]{32}$",
            "type": "string"
          },
          "numDocuments": {
            "minimum": 0,
            "type": "integer"
          }
        },
        "additionalProperties": false
      }
    },
    "nextToken": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    }
  },
  "additionalProperties": false
}
```


#### POST /batches





| Header name | Header value |
| --- | --- |
| Content-Type | application/json |
| Authorization | Bearer &lt;your access token here&gt; |
| x-api-key | &lt;your api key here&gt; |





##### Request body JSON Schema
```json
{
  "title": "POST /batches",
  "type": "object",
  "properties": {
    "name": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "description": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "containsPersonallyIdentifiableInformation": {
      "type": "boolean"
    }
  },
  "additionalProperties": false
}
```


##### Response body JSON Schema
```json
{
  "title": "batch",
  "required": [
    "batchId",
    "containsPersonallyIdentifiableInformation",
    "createdTime",
    "description",
    "numDocuments",
    "retentionInDays",
    "storageLocation"
  ],
  "type": "object",
  "properties": {
    "retentionInDays": {
      "maximum": 1825,
      "minimum": 0,
      "type": "integer"
    },
    "name": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "description": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "createdTime": {
      "pattern": "^[0-9]{4}-?[0-9]{2}-?[0-9]{2}( |T)?[0-9]{2}:?[0-9]{2}:?[0-9]{2}(.[0-9]{1,6})?(Z|[+][0-9]{2}(:|)[0-9]{2})$",
      "type": "string",
      "nullable": true
    },
    "storageLocation": {
      "type": "string",
      "enum": [
        "EU"
      ]
    },
    "containsPersonallyIdentifiableInformation": {
      "type": "boolean"
    },
    "batchId": {
      "pattern": "^las:batch:[a-f0-9]{32}$",
      "type": "string"
    },
    "numDocuments": {
      "minimum": 0,
      "type": "integer"
    }
  },
  "additionalProperties": false
}
```


#### DELETE /batches/{batchId}


| Path name | Path value |
| --- | --- |
| batchId | Id of batch on the form las:batch:&lt;hex&gt; |


| Header name | Header value |
| --- | --- |
| Authorization | Bearer &lt;your access token here&gt; |
| x-api-key | &lt;your api key here&gt; |








##### Response body JSON Schema
```json
{
  "title": "batch",
  "required": [
    "batchId",
    "containsPersonallyIdentifiableInformation",
    "createdTime",
    "description",
    "numDocuments",
    "retentionInDays",
    "storageLocation"
  ],
  "type": "object",
  "properties": {
    "retentionInDays": {
      "maximum": 1825,
      "minimum": 0,
      "type": "integer"
    },
    "name": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "description": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "createdTime": {
      "pattern": "^[0-9]{4}-?[0-9]{2}-?[0-9]{2}( |T)?[0-9]{2}:?[0-9]{2}:?[0-9]{2}(.[0-9]{1,6})?(Z|[+][0-9]{2}(:|)[0-9]{2})$",
      "type": "string",
      "nullable": true
    },
    "storageLocation": {
      "type": "string",
      "enum": [
        "EU"
      ]
    },
    "containsPersonallyIdentifiableInformation": {
      "type": "boolean"
    },
    "batchId": {
      "pattern": "^las:batch:[a-f0-9]{32}$",
      "type": "string"
    },
    "numDocuments": {
      "minimum": 0,
      "type": "integer"
    }
  },
  "additionalProperties": false
}
```


#### PATCH /batches/{batchId}


| Path name | Path value |
| --- | --- |
| batchId | Id of batch on the form las:batch:&lt;hex&gt; |


| Header name | Header value |
| --- | --- |
| Content-Type | application/json |
| Authorization | Bearer &lt;your access token here&gt; |
| x-api-key | &lt;your api key here&gt; |





##### Request body JSON Schema
```json
{
  "title": "PATCH /batches/{batchId}",
  "minProperties": 1,
  "type": "object",
  "properties": {
    "name": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "description": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    }
  },
  "additionalProperties": false
}
```


##### Response body JSON Schema
```json
{
  "title": "batch",
  "required": [
    "batchId",
    "containsPersonallyIdentifiableInformation",
    "createdTime",
    "description",
    "numDocuments",
    "retentionInDays",
    "storageLocation"
  ],
  "type": "object",
  "properties": {
    "retentionInDays": {
      "maximum": 1825,
      "minimum": 0,
      "type": "integer"
    },
    "name": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "description": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "createdTime": {
      "pattern": "^[0-9]{4}-?[0-9]{2}-?[0-9]{2}( |T)?[0-9]{2}:?[0-9]{2}:?[0-9]{2}(.[0-9]{1,6})?(Z|[+][0-9]{2}(:|)[0-9]{2})$",
      "type": "string",
      "nullable": true
    },
    "storageLocation": {
      "type": "string",
      "enum": [
        "EU"
      ]
    },
    "containsPersonallyIdentifiableInformation": {
      "type": "boolean"
    },
    "batchId": {
      "pattern": "^las:batch:[a-f0-9]{32}$",
      "type": "string"
    },
    "numDocuments": {
      "minimum": 0,
      "type": "integer"
    }
  },
  "additionalProperties": false
}
```


#### GET /datasets





| Header name | Header value |
| --- | --- |
| Authorization | Bearer &lt;your access token here&gt; |
| x-api-key | &lt;your api key here&gt; |


| Query name | Query value |
| --- | --- |
| nextToken | String value as returned by a previous list operation |
| maxResults | Integer representing maximum number of resources to list |





##### Response body JSON Schema
```json
{
  "title": "datasets",
  "required": [
    "datasets",
    "nextToken"
  ],
  "type": "object",
  "properties": {
    "nextToken": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "datasets": {
      "type": "array",
      "items": {
        "required": [
          "containsPersonallyIdentifiableInformation",
          "createdBy",
          "createdTime",
          "datasetId",
          "description",
          "groundTruthSummary",
          "numberOfDocuments",
          "retentionInDays",
          "storageLocation",
          "updatedBy",
          "updatedTime",
          "version"
        ],
        "type": "object",
        "properties": {
          "updatedTime": {
            "pattern": "^[0-9]{4}-?[0-9]{2}-?[0-9]{2}( |T)?[0-9]{2}:?[0-9]{2}:?[0-9]{2}(.[0-9]{1,6})?(Z|[+][0-9]{2}(:|)[0-9]{2})$",
            "type": "string",
            "nullable": true
          },
          "retentionInDays": {
            "maximum": 1825,
            "minimum": 0,
            "type": "integer"
          },
          "updatedBy": {
            "maxLength": 4096,
            "type": "string",
            "nullable": true
          },
          "groundTruthSummary": {
            "type": "object"
          },
          "description": {
            "maxLength": 4096,
            "type": "string",
            "nullable": true
          },
          "storageLocation": {
            "type": "string",
            "enum": [
              "EU"
            ]
          },
          "version": {
            "minimum": 0,
            "type": "integer"
          },
          "createdBy": {
            "maxLength": 4096,
            "type": "string",
            "nullable": true
          },
          "numberOfDocuments": {
            "minimum": 0,
            "type": "integer"
          },
          "name": {
            "maxLength": 4096,
            "type": "string",
            "nullable": true
          },
          "datasetId": {
            "pattern": "^las:dataset:[a-f0-9]{32}$",
            "type": "string"
          },
          "createdTime": {
            "pattern": "^[0-9]{4}-?[0-9]{2}-?[0-9]{2}( |T)?[0-9]{2}:?[0-9]{2}:?[0-9]{2}(.[0-9]{1,6})?(Z|[+][0-9]{2}(:|)[0-9]{2})$",
            "type": "string",
            "nullable": true
          },
          "containsPersonallyIdentifiableInformation": {
            "type": "boolean"
          }
        },
        "additionalProperties": false
      }
    }
  },
  "additionalProperties": false
}
```


#### POST /datasets





| Header name | Header value |
| --- | --- |
| Content-Type | application/json |
| Authorization | Bearer &lt;your access token here&gt; |
| x-api-key | &lt;your api key here&gt; |





##### Request body JSON Schema
```json
{
  "title": "POST /datasets",
  "type": "object",
  "properties": {
    "retentionInDays": {
      "minimum": 1,
      "type": "integer"
    },
    "name": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "description": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "containsPersonallyIdentifiableInformation": {
      "type": "boolean"
    }
  },
  "additionalProperties": false
}
```


##### Response body JSON Schema
```json
{
  "title": "dataset",
  "required": [
    "containsPersonallyIdentifiableInformation",
    "createdBy",
    "createdTime",
    "datasetId",
    "description",
    "groundTruthSummary",
    "numberOfDocuments",
    "retentionInDays",
    "storageLocation",
    "updatedBy",
    "updatedTime",
    "version"
  ],
  "type": "object",
  "properties": {
    "updatedTime": {
      "pattern": "^[0-9]{4}-?[0-9]{2}-?[0-9]{2}( |T)?[0-9]{2}:?[0-9]{2}:?[0-9]{2}(.[0-9]{1,6})?(Z|[+][0-9]{2}(:|)[0-9]{2})$",
      "type": "string",
      "nullable": true
    },
    "retentionInDays": {
      "maximum": 1825,
      "minimum": 0,
      "type": "integer"
    },
    "updatedBy": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "groundTruthSummary": {
      "type": "object"
    },
    "description": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "storageLocation": {
      "type": "string",
      "enum": [
        "EU"
      ]
    },
    "version": {
      "minimum": 0,
      "type": "integer"
    },
    "createdBy": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "numberOfDocuments": {
      "minimum": 0,
      "type": "integer"
    },
    "name": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "datasetId": {
      "pattern": "^las:dataset:[a-f0-9]{32}$",
      "type": "string"
    },
    "createdTime": {
      "pattern": "^[0-9]{4}-?[0-9]{2}-?[0-9]{2}( |T)?[0-9]{2}:?[0-9]{2}:?[0-9]{2}(.[0-9]{1,6})?(Z|[+][0-9]{2}(:|)[0-9]{2})$",
      "type": "string",
      "nullable": true
    },
    "containsPersonallyIdentifiableInformation": {
      "type": "boolean"
    }
  },
  "additionalProperties": false
}
```


#### DELETE /datasets/{datasetId}


| Path name | Path value |
| --- | --- |
| datasetId | Id of dataset on the form las:dataset:&lt;hex&gt; |


| Header name | Header value |
| --- | --- |
| Authorization | Bearer &lt;your access token here&gt; |
| x-api-key | &lt;your api key here&gt; |








##### Response body JSON Schema
```json
{
  "title": "dataset",
  "required": [
    "containsPersonallyIdentifiableInformation",
    "createdBy",
    "createdTime",
    "datasetId",
    "description",
    "groundTruthSummary",
    "numberOfDocuments",
    "retentionInDays",
    "storageLocation",
    "updatedBy",
    "updatedTime",
    "version"
  ],
  "type": "object",
  "properties": {
    "updatedTime": {
      "pattern": "^[0-9]{4}-?[0-9]{2}-?[0-9]{2}( |T)?[0-9]{2}:?[0-9]{2}:?[0-9]{2}(.[0-9]{1,6})?(Z|[+][0-9]{2}(:|)[0-9]{2})$",
      "type": "string",
      "nullable": true
    },
    "retentionInDays": {
      "maximum": 1825,
      "minimum": 0,
      "type": "integer"
    },
    "updatedBy": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "groundTruthSummary": {
      "type": "object"
    },
    "description": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "storageLocation": {
      "type": "string",
      "enum": [
        "EU"
      ]
    },
    "version": {
      "minimum": 0,
      "type": "integer"
    },
    "createdBy": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "numberOfDocuments": {
      "minimum": 0,
      "type": "integer"
    },
    "name": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "datasetId": {
      "pattern": "^las:dataset:[a-f0-9]{32}$",
      "type": "string"
    },
    "createdTime": {
      "pattern": "^[0-9]{4}-?[0-9]{2}-?[0-9]{2}( |T)?[0-9]{2}:?[0-9]{2}:?[0-9]{2}(.[0-9]{1,6})?(Z|[+][0-9]{2}(:|)[0-9]{2})$",
      "type": "string",
      "nullable": true
    },
    "containsPersonallyIdentifiableInformation": {
      "type": "boolean"
    }
  },
  "additionalProperties": false
}
```


#### GET /datasets/{datasetId}


| Path name | Path value |
| --- | --- |
| datasetId | Id of dataset on the form las:dataset:&lt;hex&gt; |


| Header name | Header value |
| --- | --- |
| Authorization | Bearer &lt;your access token here&gt; |
| x-api-key | &lt;your api key here&gt; |








##### Response body JSON Schema
```json
{
  "title": "dataset",
  "required": [
    "containsPersonallyIdentifiableInformation",
    "createdBy",
    "createdTime",
    "datasetId",
    "description",
    "groundTruthSummary",
    "numberOfDocuments",
    "retentionInDays",
    "storageLocation",
    "updatedBy",
    "updatedTime",
    "version"
  ],
  "type": "object",
  "properties": {
    "updatedTime": {
      "pattern": "^[0-9]{4}-?[0-9]{2}-?[0-9]{2}( |T)?[0-9]{2}:?[0-9]{2}:?[0-9]{2}(.[0-9]{1,6})?(Z|[+][0-9]{2}(:|)[0-9]{2})$",
      "type": "string",
      "nullable": true
    },
    "retentionInDays": {
      "maximum": 1825,
      "minimum": 0,
      "type": "integer"
    },
    "updatedBy": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "groundTruthSummary": {
      "type": "object"
    },
    "description": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "storageLocation": {
      "type": "string",
      "enum": [
        "EU"
      ]
    },
    "version": {
      "minimum": 0,
      "type": "integer"
    },
    "createdBy": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "numberOfDocuments": {
      "minimum": 0,
      "type": "integer"
    },
    "name": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "datasetId": {
      "pattern": "^las:dataset:[a-f0-9]{32}$",
      "type": "string"
    },
    "createdTime": {
      "pattern": "^[0-9]{4}-?[0-9]{2}-?[0-9]{2}( |T)?[0-9]{2}:?[0-9]{2}:?[0-9]{2}(.[0-9]{1,6})?(Z|[+][0-9]{2}(:|)[0-9]{2})$",
      "type": "string",
      "nullable": true
    },
    "containsPersonallyIdentifiableInformation": {
      "type": "boolean"
    }
  },
  "additionalProperties": false
}
```


#### PATCH /datasets/{datasetId}


| Path name | Path value |
| --- | --- |
| datasetId | Id of dataset on the form las:dataset:&lt;hex&gt; |


| Header name | Header value |
| --- | --- |
| Content-Type | application/json |
| Authorization | Bearer &lt;your access token here&gt; |
| x-api-key | &lt;your api key here&gt; |





##### Request body JSON Schema
```json
{
  "title": "PATCH /datasets/{datasetId}",
  "minProperties": 1,
  "type": "object",
  "properties": {
    "name": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "description": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    }
  },
  "additionalProperties": false
}
```


##### Response body JSON Schema
```json
{
  "title": "dataset",
  "required": [
    "containsPersonallyIdentifiableInformation",
    "createdBy",
    "createdTime",
    "datasetId",
    "description",
    "groundTruthSummary",
    "numberOfDocuments",
    "retentionInDays",
    "storageLocation",
    "updatedBy",
    "updatedTime",
    "version"
  ],
  "type": "object",
  "properties": {
    "updatedTime": {
      "pattern": "^[0-9]{4}-?[0-9]{2}-?[0-9]{2}( |T)?[0-9]{2}:?[0-9]{2}:?[0-9]{2}(.[0-9]{1,6})?(Z|[+][0-9]{2}(:|)[0-9]{2})$",
      "type": "string",
      "nullable": true
    },
    "retentionInDays": {
      "maximum": 1825,
      "minimum": 0,
      "type": "integer"
    },
    "updatedBy": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "groundTruthSummary": {
      "type": "object"
    },
    "description": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "storageLocation": {
      "type": "string",
      "enum": [
        "EU"
      ]
    },
    "version": {
      "minimum": 0,
      "type": "integer"
    },
    "createdBy": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "numberOfDocuments": {
      "minimum": 0,
      "type": "integer"
    },
    "name": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "datasetId": {
      "pattern": "^las:dataset:[a-f0-9]{32}$",
      "type": "string"
    },
    "createdTime": {
      "pattern": "^[0-9]{4}-?[0-9]{2}-?[0-9]{2}( |T)?[0-9]{2}:?[0-9]{2}:?[0-9]{2}(.[0-9]{1,6})?(Z|[+][0-9]{2}(:|)[0-9]{2})$",
      "type": "string",
      "nullable": true
    },
    "containsPersonallyIdentifiableInformation": {
      "type": "boolean"
    }
  },
  "additionalProperties": false
}
```


#### DELETE /documents





| Header name | Header value |
| --- | --- |
| Authorization | Bearer &lt;your access token here&gt; |
| x-api-key | &lt;your api key here&gt; |


| Query name | Query value |
| --- | --- |
| batchId | Id of batch on the form las:batch:&lt;hex&gt; |
| consentId | Id of consent on the form las:consent:&lt;hex&gt; |
| datasetId | String |
| nextToken | String value as returned by a previous list operation |
| maxResults | Integer representing maximum number of resources to list |





##### Response body JSON Schema
```json
{
  "title": "documents",
  "required": [
    "documents",
    "nextToken"
  ],
  "type": "object",
  "properties": {
    "consentId": {
      "type": "array",
      "items": {
        "pattern": "^las:consent:[a-f0-9]{32}$",
        "type": "string"
      }
    },
    "documents": {
      "type": "array",
      "items": {
        "required": [
          "contentType",
          "createdBy",
          "createdTime",
          "documentId",
          "retentionInDays",
          "updatedBy",
          "updatedTime"
        ],
        "type": "object",
        "properties": {
          "groundTruth": {
            "type": "array",
            "items": {
              "required": [
                "label",
                "value"
              ],
              "type": "object",
              "properties": {
                "label": {
                  "maxLength": 36,
                  "minLength": 1,
                  "pattern": "^[0-9A-Za-z_]+$",
                  "type": "string"
                },
                "value": {
                  "anyOf": [
                    {
                      "maxLength": 64,
                      "minLength": 1,
                      "type": "string",
                      "nullable": true
                    },
                    {
                      "type": "boolean"
                    }
                  ]
                }
              },
              "additionalProperties": false
            }
          },
          "updatedTime": {
            "pattern": "^[0-9]{4}-?[0-9]{2}-?[0-9]{2}( |T)?[0-9]{2}:?[0-9]{2}:?[0-9]{2}(.[0-9]{1,6})?(Z|[+][0-9]{2}(:|)[0-9]{2})$",
            "type": "string",
            "nullable": true
          },
          "consentId": {
            "pattern": "^las:consent:[a-f0-9]{32}$",
            "type": "string"
          },
          "retentionInDays": {
            "minimum": 1,
            "type": "integer"
          },
          "updatedBy": {
            "maxLength": 4096,
            "type": "string",
            "nullable": true
          },
          "createdBy": {
            "maxLength": 4096,
            "type": "string",
            "nullable": true
          },
          "createdTime": {
            "pattern": "^[0-9]{4}-?[0-9]{2}-?[0-9]{2}( |T)?[0-9]{2}:?[0-9]{2}:?[0-9]{2}(.[0-9]{1,6})?(Z|[+][0-9]{2}(:|)[0-9]{2})$",
            "type": "string",
            "nullable": true
          },
          "datasetId": {
            "pattern": "^las:dataset:[a-f0-9]{32}$",
            "type": "string"
          },
          "documentId": {
            "pattern": "^las:document:[a-f0-9]{32}$",
            "type": "string"
          },
          "batchId": {
            "pattern": "^las:batch:[a-f0-9]{32}$",
            "type": "string"
          },
          "contentType": {
            "type": "string",
            "enum": [
              "application/pdf",
              "image/jpeg",
              "image/png",
              "image/tiff"
            ]
          },
          "content": {
            "minLength": 1,
            "type": "string"
          }
        },
        "additionalProperties": false
      }
    },
    "nextToken": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "datasetId": {
      "type": "array",
      "items": {
        "pattern": "^las:dataset:[a-f0-9]{32}$",
        "type": "string"
      }
    },
    "batchId": {
      "type": "array",
      "items": {
        "pattern": "^las:batch:[a-f0-9]{32}$",
        "type": "string"
      }
    }
  },
  "additionalProperties": false
}
```


#### GET /documents





| Header name | Header value |
| --- | --- |
| Authorization | Bearer &lt;your access token here&gt; |
| x-api-key | &lt;your api key here&gt; |


| Query name | Query value |
| --- | --- |
| batchId | Id of batch on the form las:batch:&lt;hex&gt; |
| consentId | Id of consent on the form las:consent:&lt;hex&gt; |
| datasetId | String |
| nextToken | String value as returned by a previous list operation |
| maxResults | Integer representing maximum number of resources to list |





##### Response body JSON Schema
```json
{
  "title": "documents",
  "required": [
    "documents",
    "nextToken"
  ],
  "type": "object",
  "properties": {
    "consentId": {
      "type": "array",
      "items": {
        "pattern": "^las:consent:[a-f0-9]{32}$",
        "type": "string"
      }
    },
    "documents": {
      "type": "array",
      "items": {
        "required": [
          "contentType",
          "createdBy",
          "createdTime",
          "documentId",
          "retentionInDays",
          "updatedBy",
          "updatedTime"
        ],
        "type": "object",
        "properties": {
          "groundTruth": {
            "type": "array",
            "items": {
              "required": [
                "label",
                "value"
              ],
              "type": "object",
              "properties": {
                "label": {
                  "maxLength": 36,
                  "minLength": 1,
                  "pattern": "^[0-9A-Za-z_]+$",
                  "type": "string"
                },
                "value": {
                  "anyOf": [
                    {
                      "maxLength": 64,
                      "minLength": 1,
                      "type": "string",
                      "nullable": true
                    },
                    {
                      "type": "boolean"
                    }
                  ]
                }
              },
              "additionalProperties": false
            }
          },
          "updatedTime": {
            "pattern": "^[0-9]{4}-?[0-9]{2}-?[0-9]{2}( |T)?[0-9]{2}:?[0-9]{2}:?[0-9]{2}(.[0-9]{1,6})?(Z|[+][0-9]{2}(:|)[0-9]{2})$",
            "type": "string",
            "nullable": true
          },
          "consentId": {
            "pattern": "^las:consent:[a-f0-9]{32}$",
            "type": "string"
          },
          "retentionInDays": {
            "minimum": 1,
            "type": "integer"
          },
          "updatedBy": {
            "maxLength": 4096,
            "type": "string",
            "nullable": true
          },
          "createdBy": {
            "maxLength": 4096,
            "type": "string",
            "nullable": true
          },
          "createdTime": {
            "pattern": "^[0-9]{4}-?[0-9]{2}-?[0-9]{2}( |T)?[0-9]{2}:?[0-9]{2}:?[0-9]{2}(.[0-9]{1,6})?(Z|[+][0-9]{2}(:|)[0-9]{2})$",
            "type": "string",
            "nullable": true
          },
          "datasetId": {
            "pattern": "^las:dataset:[a-f0-9]{32}$",
            "type": "string"
          },
          "documentId": {
            "pattern": "^las:document:[a-f0-9]{32}$",
            "type": "string"
          },
          "batchId": {
            "pattern": "^las:batch:[a-f0-9]{32}$",
            "type": "string"
          },
          "contentType": {
            "type": "string",
            "enum": [
              "application/pdf",
              "image/jpeg",
              "image/png",
              "image/tiff"
            ]
          },
          "content": {
            "minLength": 1,
            "type": "string"
          }
        },
        "additionalProperties": false
      }
    },
    "nextToken": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "datasetId": {
      "type": "array",
      "items": {
        "pattern": "^las:dataset:[a-f0-9]{32}$",
        "type": "string"
      }
    },
    "batchId": {
      "type": "array",
      "items": {
        "pattern": "^las:batch:[a-f0-9]{32}$",
        "type": "string"
      }
    }
  },
  "additionalProperties": false
}
```


#### POST /documents





| Header name | Header value |
| --- | --- |
| Content-Type | application/json |
| Authorization | Bearer &lt;your access token here&gt; |
| x-api-key | &lt;your api key here&gt; |





##### Request body JSON Schema
```json
{
  "title": "POST /documents",
  "required": [
    "content",
    "contentType"
  ],
  "type": "object",
  "properties": {
    "groundTruth": {
      "type": "array",
      "items": {
        "required": [
          "label",
          "value"
        ],
        "type": "object",
        "properties": {
          "label": {
            "maxLength": 36,
            "minLength": 1,
            "pattern": "^[0-9A-Za-z_]+$",
            "type": "string"
          },
          "value": {
            "anyOf": [
              {
                "maxLength": 64,
                "minLength": 1,
                "type": "string",
                "nullable": true
              },
              {
                "type": "boolean"
              }
            ]
          }
        },
        "additionalProperties": false
      }
    },
    "consentId": {
      "pattern": "^las:consent:[a-f0-9]{32}$",
      "type": "string"
    },
    "retentionInDays": {
      "minimum": 1,
      "type": "integer"
    },
    "datasetId": {
      "pattern": "^las:dataset:[a-f0-9]{32}$",
      "type": "string"
    },
    "batchId": {
      "pattern": "^las:batch:[a-f0-9]{32}$",
      "type": "string"
    },
    "contentType": {
      "type": "string",
      "enum": [
        "application/pdf",
        "image/jpeg",
        "image/png",
        "image/tiff"
      ]
    },
    "content": {
      "maxLength": 6250000,
      "minLength": 1,
      "type": "string"
    }
  },
  "additionalProperties": false
}
```


##### Response body JSON Schema
```json
{
  "title": "document",
  "required": [
    "contentType",
    "createdBy",
    "createdTime",
    "documentId",
    "retentionInDays",
    "updatedBy",
    "updatedTime"
  ],
  "type": "object",
  "properties": {
    "groundTruth": {
      "type": "array",
      "items": {
        "required": [
          "label",
          "value"
        ],
        "type": "object",
        "properties": {
          "label": {
            "maxLength": 36,
            "minLength": 1,
            "pattern": "^[0-9A-Za-z_]+$",
            "type": "string"
          },
          "value": {
            "anyOf": [
              {
                "maxLength": 64,
                "minLength": 1,
                "type": "string",
                "nullable": true
              },
              {
                "type": "boolean"
              }
            ]
          }
        },
        "additionalProperties": false
      }
    },
    "updatedTime": {
      "pattern": "^[0-9]{4}-?[0-9]{2}-?[0-9]{2}( |T)?[0-9]{2}:?[0-9]{2}:?[0-9]{2}(.[0-9]{1,6})?(Z|[+][0-9]{2}(:|)[0-9]{2})$",
      "type": "string",
      "nullable": true
    },
    "consentId": {
      "pattern": "^las:consent:[a-f0-9]{32}$",
      "type": "string"
    },
    "retentionInDays": {
      "minimum": 1,
      "type": "integer"
    },
    "updatedBy": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "createdBy": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "createdTime": {
      "pattern": "^[0-9]{4}-?[0-9]{2}-?[0-9]{2}( |T)?[0-9]{2}:?[0-9]{2}:?[0-9]{2}(.[0-9]{1,6})?(Z|[+][0-9]{2}(:|)[0-9]{2})$",
      "type": "string",
      "nullable": true
    },
    "datasetId": {
      "pattern": "^las:dataset:[a-f0-9]{32}$",
      "type": "string"
    },
    "documentId": {
      "pattern": "^las:document:[a-f0-9]{32}$",
      "type": "string"
    },
    "batchId": {
      "pattern": "^las:batch:[a-f0-9]{32}$",
      "type": "string"
    },
    "contentType": {
      "type": "string",
      "enum": [
        "application/pdf",
        "image/jpeg",
        "image/png",
        "image/tiff"
      ]
    },
    "content": {
      "minLength": 1,
      "type": "string"
    }
  },
  "additionalProperties": false
}
```


#### DELETE /documents/{documentId}


| Path name | Path value |
| --- | --- |
| documentId | Id of document on the form las:document:&lt;hex&gt; |


| Header name | Header value |
| --- | --- |
| Authorization | Bearer &lt;your access token here&gt; |
| x-api-key | &lt;your api key here&gt; |








##### Response body JSON Schema
```json
{
  "title": "document",
  "required": [
    "contentType",
    "createdBy",
    "createdTime",
    "documentId",
    "retentionInDays",
    "updatedBy",
    "updatedTime"
  ],
  "type": "object",
  "properties": {
    "groundTruth": {
      "type": "array",
      "items": {
        "required": [
          "label",
          "value"
        ],
        "type": "object",
        "properties": {
          "label": {
            "maxLength": 36,
            "minLength": 1,
            "pattern": "^[0-9A-Za-z_]+$",
            "type": "string"
          },
          "value": {
            "anyOf": [
              {
                "maxLength": 64,
                "minLength": 1,
                "type": "string",
                "nullable": true
              },
              {
                "type": "boolean"
              }
            ]
          }
        },
        "additionalProperties": false
      }
    },
    "updatedTime": {
      "pattern": "^[0-9]{4}-?[0-9]{2}-?[0-9]{2}( |T)?[0-9]{2}:?[0-9]{2}:?[0-9]{2}(.[0-9]{1,6})?(Z|[+][0-9]{2}(:|)[0-9]{2})$",
      "type": "string",
      "nullable": true
    },
    "consentId": {
      "pattern": "^las:consent:[a-f0-9]{32}$",
      "type": "string"
    },
    "retentionInDays": {
      "minimum": 1,
      "type": "integer"
    },
    "updatedBy": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "createdBy": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "createdTime": {
      "pattern": "^[0-9]{4}-?[0-9]{2}-?[0-9]{2}( |T)?[0-9]{2}:?[0-9]{2}:?[0-9]{2}(.[0-9]{1,6})?(Z|[+][0-9]{2}(:|)[0-9]{2})$",
      "type": "string",
      "nullable": true
    },
    "datasetId": {
      "pattern": "^las:dataset:[a-f0-9]{32}$",
      "type": "string"
    },
    "documentId": {
      "pattern": "^las:document:[a-f0-9]{32}$",
      "type": "string"
    },
    "batchId": {
      "pattern": "^las:batch:[a-f0-9]{32}$",
      "type": "string"
    },
    "contentType": {
      "type": "string",
      "enum": [
        "application/pdf",
        "image/jpeg",
        "image/png",
        "image/tiff"
      ]
    },
    "content": {
      "minLength": 1,
      "type": "string"
    }
  },
  "additionalProperties": false
}
```


#### GET /documents/{documentId}


| Path name | Path value |
| --- | --- |
| documentId | Id of document on the form las:document:&lt;hex&gt; |


| Header name | Header value |
| --- | --- |
| Authorization | Bearer &lt;your access token here&gt; |
| x-api-key | &lt;your api key here&gt; |








##### Response body JSON Schema
```json
{
  "title": "document",
  "required": [
    "contentType",
    "createdBy",
    "createdTime",
    "documentId",
    "retentionInDays",
    "updatedBy",
    "updatedTime"
  ],
  "type": "object",
  "properties": {
    "groundTruth": {
      "type": "array",
      "items": {
        "required": [
          "label",
          "value"
        ],
        "type": "object",
        "properties": {
          "label": {
            "maxLength": 36,
            "minLength": 1,
            "pattern": "^[0-9A-Za-z_]+$",
            "type": "string"
          },
          "value": {
            "anyOf": [
              {
                "maxLength": 64,
                "minLength": 1,
                "type": "string",
                "nullable": true
              },
              {
                "type": "boolean"
              }
            ]
          }
        },
        "additionalProperties": false
      }
    },
    "updatedTime": {
      "pattern": "^[0-9]{4}-?[0-9]{2}-?[0-9]{2}( |T)?[0-9]{2}:?[0-9]{2}:?[0-9]{2}(.[0-9]{1,6})?(Z|[+][0-9]{2}(:|)[0-9]{2})$",
      "type": "string",
      "nullable": true
    },
    "consentId": {
      "pattern": "^las:consent:[a-f0-9]{32}$",
      "type": "string"
    },
    "retentionInDays": {
      "minimum": 1,
      "type": "integer"
    },
    "updatedBy": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "createdBy": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "createdTime": {
      "pattern": "^[0-9]{4}-?[0-9]{2}-?[0-9]{2}( |T)?[0-9]{2}:?[0-9]{2}:?[0-9]{2}(.[0-9]{1,6})?(Z|[+][0-9]{2}(:|)[0-9]{2})$",
      "type": "string",
      "nullable": true
    },
    "datasetId": {
      "pattern": "^las:dataset:[a-f0-9]{32}$",
      "type": "string"
    },
    "documentId": {
      "pattern": "^las:document:[a-f0-9]{32}$",
      "type": "string"
    },
    "batchId": {
      "pattern": "^las:batch:[a-f0-9]{32}$",
      "type": "string"
    },
    "contentType": {
      "type": "string",
      "enum": [
        "application/pdf",
        "image/jpeg",
        "image/png",
        "image/tiff"
      ]
    },
    "content": {
      "minLength": 1,
      "type": "string"
    }
  },
  "additionalProperties": false
}
```


#### PATCH /documents/{documentId}


| Path name | Path value |
| --- | --- |
| documentId | Id of document on the form las:document:&lt;hex&gt; |


| Header name | Header value |
| --- | --- |
| Content-Type | application/json |
| Authorization | Bearer &lt;your access token here&gt; |
| x-api-key | &lt;your api key here&gt; |





##### Request body JSON Schema
```json
{
  "title": "PATCH /documents/{documentId}",
  "minProperties": 1,
  "type": "object",
  "properties": {
    "groundTruth": {
      "type": "array",
      "items": {
        "required": [
          "label",
          "value"
        ],
        "type": "object",
        "properties": {
          "label": {
            "maxLength": 36,
            "minLength": 1,
            "pattern": "^[0-9A-Za-z_]+$",
            "type": "string"
          },
          "value": {
            "anyOf": [
              {
                "maxLength": 64,
                "minLength": 1,
                "type": "string",
                "nullable": true
              },
              {
                "type": "boolean"
              }
            ]
          }
        },
        "additionalProperties": false
      }
    },
    "retentionInDays": {
      "minimum": 1,
      "type": "integer"
    },
    "datasetId": {
      "pattern": "^las:dataset:[a-f0-9]{32}$",
      "type": "string"
    }
  },
  "additionalProperties": false
}
```


##### Response body JSON Schema
```json
{
  "title": "document",
  "required": [
    "contentType",
    "createdBy",
    "createdTime",
    "documentId",
    "retentionInDays",
    "updatedBy",
    "updatedTime"
  ],
  "type": "object",
  "properties": {
    "groundTruth": {
      "type": "array",
      "items": {
        "required": [
          "label",
          "value"
        ],
        "type": "object",
        "properties": {
          "label": {
            "maxLength": 36,
            "minLength": 1,
            "pattern": "^[0-9A-Za-z_]+$",
            "type": "string"
          },
          "value": {
            "anyOf": [
              {
                "maxLength": 64,
                "minLength": 1,
                "type": "string",
                "nullable": true
              },
              {
                "type": "boolean"
              }
            ]
          }
        },
        "additionalProperties": false
      }
    },
    "updatedTime": {
      "pattern": "^[0-9]{4}-?[0-9]{2}-?[0-9]{2}( |T)?[0-9]{2}:?[0-9]{2}:?[0-9]{2}(.[0-9]{1,6})?(Z|[+][0-9]{2}(:|)[0-9]{2})$",
      "type": "string",
      "nullable": true
    },
    "consentId": {
      "pattern": "^las:consent:[a-f0-9]{32}$",
      "type": "string"
    },
    "retentionInDays": {
      "minimum": 1,
      "type": "integer"
    },
    "updatedBy": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "createdBy": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "createdTime": {
      "pattern": "^[0-9]{4}-?[0-9]{2}-?[0-9]{2}( |T)?[0-9]{2}:?[0-9]{2}:?[0-9]{2}(.[0-9]{1,6})?(Z|[+][0-9]{2}(:|)[0-9]{2})$",
      "type": "string",
      "nullable": true
    },
    "datasetId": {
      "pattern": "^las:dataset:[a-f0-9]{32}$",
      "type": "string"
    },
    "documentId": {
      "pattern": "^las:document:[a-f0-9]{32}$",
      "type": "string"
    },
    "batchId": {
      "pattern": "^las:batch:[a-f0-9]{32}$",
      "type": "string"
    },
    "contentType": {
      "type": "string",
      "enum": [
        "application/pdf",
        "image/jpeg",
        "image/png",
        "image/tiff"
      ]
    },
    "content": {
      "minLength": 1,
      "type": "string"
    }
  },
  "additionalProperties": false
}
```


#### GET /logs





| Header name | Header value |
| --- | --- |
| Authorization | Bearer &lt;your access token here&gt; |
| x-api-key | &lt;your api key here&gt; |


| Query name | Query value |
| --- | --- |
| workflowId | String |
| nextToken | String value as returned by a previous list operation |
| order | ascending \| descending |
| transitionExecutionId | String |
| transitionId | String |
| maxResults | Integer representing maximum number of resources to list |
| workflowExecutionId | String |





##### Response body JSON Schema
```json
{
  "title": "logs",
  "required": [
    "logs",
    "nextToken"
  ],
  "type": "object",
  "properties": {
    "transitionId": {
      "anyOf": [
        {
          "pattern": "^las:transition:[a-f0-9]{32}$",
          "type": "string"
        },
        {
          "pattern": "^las:transition:commons-[0-9A-Za-z-]+$",
          "type": "string"
        }
      ]
    },
    "nextToken": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "transitionExecutionId": {
      "pattern": "^las:transition-execution:[a-f0-9]{32}$",
      "type": "string"
    },
    "workflowExecutionId": {
      "pattern": "^las:workflow-execution:[a-f0-9]{32}$",
      "type": "string"
    },
    "logs": {
      "type": "array",
      "items": {
        "required": [
          "logId",
          "startTime",
          "transitionExecutionId",
          "transitionId",
          "workflowExecutionId",
          "workflowId"
        ],
        "type": "object",
        "properties": {
          "transitionId": {
            "anyOf": [
              {
                "pattern": "^las:transition:[a-f0-9]{32}$",
                "type": "string"
              },
              {
                "pattern": "^las:transition:commons-[0-9A-Za-z-]+$",
                "type": "string"
              }
            ]
          },
          "transitionExecutionId": {
            "pattern": "^las:transition-execution:[a-f0-9]{32}$",
            "type": "string",
            "nullable": true
          },
          "logId": {
            "pattern": "^las:log:[a-f0-9]{32}$",
            "type": "string"
          },
          "workflowExecutionId": {
            "pattern": "^las:workflow-execution:[a-f0-9]{32}$",
            "type": "string",
            "nullable": true
          },
          "startTime": {
            "pattern": "^[0-9]{4}-?[0-9]{2}-?[0-9]{2}( |T)?[0-9]{2}:?[0-9]{2}:?[0-9]{2}(.[0-9]{1,6})?(Z|[+][0-9]{2}(:|)[0-9]{2})$",
            "type": "string",
            "nullable": true
          },
          "workflowId": {
            "pattern": "^las:workflow:[a-f0-9]{32}$",
            "type": "string",
            "nullable": true
          },
          "events": {
            "type": "array",
            "items": {
              "type": "object"
            }
          }
        },
        "additionalProperties": false
      }
    },
    "workflowId": {
      "pattern": "^las:workflow:[a-f0-9]{32}$",
      "type": "string"
    },
    "order": {
      "type": "string",
      "enum": [
        "ascending",
        "descending"
      ]
    }
  },
  "additionalProperties": false
}
```


#### GET /logs/{logId}


| Path name | Path value |
| --- | --- |
| logId | Id of log on the form las:log:&lt;hex&gt; |


| Header name | Header value |
| --- | --- |
| Authorization | Bearer &lt;your access token here&gt; |
| x-api-key | &lt;your api key here&gt; |








##### Response body JSON Schema
```json
{
  "title": "log",
  "required": [
    "logId",
    "startTime",
    "transitionExecutionId",
    "transitionId",
    "workflowExecutionId",
    "workflowId"
  ],
  "type": "object",
  "properties": {
    "transitionId": {
      "anyOf": [
        {
          "pattern": "^las:transition:[a-f0-9]{32}$",
          "type": "string"
        },
        {
          "pattern": "^las:transition:commons-[0-9A-Za-z-]+$",
          "type": "string"
        }
      ]
    },
    "transitionExecutionId": {
      "pattern": "^las:transition-execution:[a-f0-9]{32}$",
      "type": "string",
      "nullable": true
    },
    "logId": {
      "pattern": "^las:log:[a-f0-9]{32}$",
      "type": "string"
    },
    "workflowExecutionId": {
      "pattern": "^las:workflow-execution:[a-f0-9]{32}$",
      "type": "string",
      "nullable": true
    },
    "startTime": {
      "pattern": "^[0-9]{4}-?[0-9]{2}-?[0-9]{2}( |T)?[0-9]{2}:?[0-9]{2}:?[0-9]{2}(.[0-9]{1,6})?(Z|[+][0-9]{2}(:|)[0-9]{2})$",
      "type": "string",
      "nullable": true
    },
    "workflowId": {
      "pattern": "^las:workflow:[a-f0-9]{32}$",
      "type": "string",
      "nullable": true
    },
    "events": {
      "type": "array",
      "items": {
        "type": "object"
      }
    }
  },
  "additionalProperties": false
}
```


#### GET /models





| Header name | Header value |
| --- | --- |
| Authorization | Bearer &lt;your access token here&gt; |
| x-api-key | &lt;your api key here&gt; |


| Query name | Query value |
| --- | --- |
| nextToken | String value as returned by a previous list operation |
| maxResults | Integer representing maximum number of resources to list |





##### Response body JSON Schema
```json
{
  "title": "models",
  "required": [
    "models",
    "nextToken"
  ],
  "type": "object",
  "properties": {
    "models": {
      "type": "array",
      "items": {
        "required": [
          "createdBy",
          "createdTime",
          "description",
          "fieldConfig",
          "height",
          "modelId",
          "name",
          "numberOfDataBundles",
          "preprocessConfig",
          "status",
          "updatedBy",
          "updatedTime",
          "width"
        ],
        "type": "object",
        "properties": {
          "updatedTime": {
            "pattern": "^[0-9]{4}-?[0-9]{2}-?[0-9]{2}( |T)?[0-9]{2}:?[0-9]{2}:?[0-9]{2}(.[0-9]{1,6})?(Z|[+][0-9]{2}(:|)[0-9]{2})$",
            "type": "string",
            "nullable": true
          },
          "updatedBy": {
            "maxLength": 4096,
            "type": "string",
            "nullable": true
          },
          "modelId": {
            "pattern": "^las:model:[a-f0-9]{32}$",
            "type": "string"
          },
          "description": {
            "maxLength": 4096,
            "type": "string",
            "nullable": true
          },
          "fieldConfig": {
            "type": "object",
            "additionalProperties": {
              "required": [
                "maxLength",
                "type"
              ],
              "type": "object",
              "properties": {
                "description": {
                  "anyOf": [
                    {
                      "maxLength": 4096,
                      "type": "string"
                    },
                    null
                  ]
                },
                "type": {
                  "type": "string",
                  "enum": [
                    "date",
                    "amount",
                    "number",
                    "letter",
                    "phone",
                    "alphanum",
                    "alphanumext",
                    "all"
                  ]
                },
                "maxLength": {
                  "maximum": 100,
                  "minimum": 1,
                  "type": "integer"
                }
              }
            }
          },
          "preprocessConfig": {
            "required": [
              "autoRotate",
              "imageQuality",
              "maxPages"
            ],
            "type": "object",
            "properties": {
              "maxPages": {
                "type": "integer"
              },
              "autoRotate": {
                "type": "boolean"
              },
              "imageQuality": {
                "type": "string",
                "enum": [
                  "LOW",
                  "HIGH"
                ]
              }
            },
            "additionalProperties": false
          },
          "createdBy": {
            "maxLength": 4096,
            "type": "string",
            "nullable": true
          },
          "name": {
            "maxLength": 4096,
            "type": "string",
            "nullable": true
          },
          "width": {
            "maximum": 1921,
            "minimum": 97,
            "type": "integer"
          },
          "numberOfDataBundles": {
            "minimum": 0,
            "type": "integer"
          },
          "createdTime": {
            "pattern": "^[0-9]{4}-?[0-9]{2}-?[0-9]{2}( |T)?[0-9]{2}:?[0-9]{2}:?[0-9]{2}(.[0-9]{1,6})?(Z|[+][0-9]{2}(:|)[0-9]{2})$",
            "type": "string",
            "nullable": true
          },
          "height": {
            "maximum": 1921,
            "minimum": 97,
            "type": "integer"
          },
          "status": {
            "type": "string",
            "enum": [
              "active",
              "training",
              "inactive"
            ]
          }
        },
        "additionalProperties": false
      }
    },
    "nextToken": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    }
  },
  "additionalProperties": false
}
```


#### POST /models





| Header name | Header value |
| --- | --- |
| Content-Type | application/json |
| Authorization | Bearer &lt;your access token here&gt; |
| x-api-key | &lt;your api key here&gt; |





##### Request body JSON Schema
```json
{
  "title": "POST /models",
  "required": [
    "fieldConfig",
    "height",
    "width"
  ],
  "type": "object",
  "properties": {
    "preprocessConfig": {
      "required": [
        "autoRotate",
        "imageQuality",
        "maxPages"
      ],
      "type": "object",
      "properties": {
        "maxPages": {
          "type": "integer"
        },
        "autoRotate": {
          "type": "boolean"
        },
        "imageQuality": {
          "type": "string",
          "enum": [
            "LOW",
            "HIGH"
          ]
        }
      },
      "additionalProperties": false
    },
    "name": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "width": {
      "maximum": 1921,
      "minimum": 97,
      "type": "integer"
    },
    "description": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "fieldConfig": {
      "type": "object",
      "additionalProperties": {
        "required": [
          "maxLength",
          "type"
        ],
        "type": "object",
        "properties": {
          "description": {
            "maxLength": 4096,
            "type": "string",
            "nullable": true
          },
          "type": {
            "type": "string",
            "enum": [
              "date",
              "amount",
              "number",
              "letter",
              "phone",
              "alphanum",
              "alphanumext",
              "all"
            ]
          },
          "maxLength": {
            "maximum": 100,
            "minimum": 1,
            "type": "integer"
          }
        }
      }
    },
    "height": {
      "maximum": 1921,
      "minimum": 97,
      "type": "integer"
    }
  },
  "additionalProperties": false
}
```


##### Response body JSON Schema
```json
{
  "title": "model",
  "required": [
    "createdBy",
    "createdTime",
    "description",
    "fieldConfig",
    "height",
    "modelId",
    "name",
    "numberOfDataBundles",
    "preprocessConfig",
    "status",
    "updatedBy",
    "updatedTime",
    "width"
  ],
  "type": "object",
  "properties": {
    "updatedTime": {
      "pattern": "^[0-9]{4}-?[0-9]{2}-?[0-9]{2}( |T)?[0-9]{2}:?[0-9]{2}:?[0-9]{2}(.[0-9]{1,6})?(Z|[+][0-9]{2}(:|)[0-9]{2})$",
      "type": "string",
      "nullable": true
    },
    "updatedBy": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "modelId": {
      "pattern": "^las:model:[a-f0-9]{32}$",
      "type": "string"
    },
    "description": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "fieldConfig": {
      "type": "object",
      "additionalProperties": {
        "required": [
          "maxLength",
          "type"
        ],
        "type": "object",
        "properties": {
          "description": {
            "anyOf": [
              {
                "maxLength": 4096,
                "type": "string"
              },
              null
            ]
          },
          "type": {
            "type": "string",
            "enum": [
              "date",
              "amount",
              "number",
              "letter",
              "phone",
              "alphanum",
              "alphanumext",
              "all"
            ]
          },
          "maxLength": {
            "maximum": 100,
            "minimum": 1,
            "type": "integer"
          }
        }
      }
    },
    "preprocessConfig": {
      "required": [
        "autoRotate",
        "imageQuality",
        "maxPages"
      ],
      "type": "object",
      "properties": {
        "maxPages": {
          "type": "integer"
        },
        "autoRotate": {
          "type": "boolean"
        },
        "imageQuality": {
          "type": "string",
          "enum": [
            "LOW",
            "HIGH"
          ]
        }
      },
      "additionalProperties": false
    },
    "createdBy": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "name": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "width": {
      "maximum": 1921,
      "minimum": 97,
      "type": "integer"
    },
    "numberOfDataBundles": {
      "minimum": 0,
      "type": "integer"
    },
    "createdTime": {
      "pattern": "^[0-9]{4}-?[0-9]{2}-?[0-9]{2}( |T)?[0-9]{2}:?[0-9]{2}:?[0-9]{2}(.[0-9]{1,6})?(Z|[+][0-9]{2}(:|)[0-9]{2})$",
      "type": "string",
      "nullable": true
    },
    "height": {
      "maximum": 1921,
      "minimum": 97,
      "type": "integer"
    },
    "status": {
      "type": "string",
      "enum": [
        "active",
        "training",
        "inactive"
      ]
    }
  },
  "additionalProperties": false
}
```


#### DELETE /models/{modelId}


| Path name | Path value |
| --- | --- |
| modelId | Id of model on the form las:model:&lt;hex&gt; |


| Header name | Header value |
| --- | --- |
| Authorization | Bearer &lt;your access token here&gt; |
| x-api-key | &lt;your api key here&gt; |








##### Response body JSON Schema
```json
{
  "title": "model",
  "required": [
    "createdBy",
    "createdTime",
    "description",
    "fieldConfig",
    "height",
    "modelId",
    "name",
    "numberOfDataBundles",
    "preprocessConfig",
    "status",
    "updatedBy",
    "updatedTime",
    "width"
  ],
  "type": "object",
  "properties": {
    "updatedTime": {
      "pattern": "^[0-9]{4}-?[0-9]{2}-?[0-9]{2}( |T)?[0-9]{2}:?[0-9]{2}:?[0-9]{2}(.[0-9]{1,6})?(Z|[+][0-9]{2}(:|)[0-9]{2})$",
      "type": "string",
      "nullable": true
    },
    "updatedBy": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "modelId": {
      "pattern": "^las:model:[a-f0-9]{32}$",
      "type": "string"
    },
    "description": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "fieldConfig": {
      "type": "object",
      "additionalProperties": {
        "required": [
          "maxLength",
          "type"
        ],
        "type": "object",
        "properties": {
          "description": {
            "anyOf": [
              {
                "maxLength": 4096,
                "type": "string"
              },
              null
            ]
          },
          "type": {
            "type": "string",
            "enum": [
              "date",
              "amount",
              "number",
              "letter",
              "phone",
              "alphanum",
              "alphanumext",
              "all"
            ]
          },
          "maxLength": {
            "maximum": 100,
            "minimum": 1,
            "type": "integer"
          }
        }
      }
    },
    "preprocessConfig": {
      "required": [
        "autoRotate",
        "imageQuality",
        "maxPages"
      ],
      "type": "object",
      "properties": {
        "maxPages": {
          "type": "integer"
        },
        "autoRotate": {
          "type": "boolean"
        },
        "imageQuality": {
          "type": "string",
          "enum": [
            "LOW",
            "HIGH"
          ]
        }
      },
      "additionalProperties": false
    },
    "createdBy": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "name": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "width": {
      "maximum": 1921,
      "minimum": 97,
      "type": "integer"
    },
    "numberOfDataBundles": {
      "minimum": 0,
      "type": "integer"
    },
    "createdTime": {
      "pattern": "^[0-9]{4}-?[0-9]{2}-?[0-9]{2}( |T)?[0-9]{2}:?[0-9]{2}:?[0-9]{2}(.[0-9]{1,6})?(Z|[+][0-9]{2}(:|)[0-9]{2})$",
      "type": "string",
      "nullable": true
    },
    "height": {
      "maximum": 1921,
      "minimum": 97,
      "type": "integer"
    },
    "status": {
      "type": "string",
      "enum": [
        "active",
        "training",
        "inactive"
      ]
    }
  },
  "additionalProperties": false
}
```


#### GET /models/{modelId}


| Path name | Path value |
| --- | --- |
| modelId | Id of model on the form las:model:&lt;hex&gt; |


| Header name | Header value |
| --- | --- |
| Authorization | Bearer &lt;your access token here&gt; |
| x-api-key | &lt;your api key here&gt; |








##### Response body JSON Schema
```json
{
  "title": "model",
  "required": [
    "createdBy",
    "createdTime",
    "description",
    "fieldConfig",
    "height",
    "modelId",
    "name",
    "numberOfDataBundles",
    "preprocessConfig",
    "status",
    "updatedBy",
    "updatedTime",
    "width"
  ],
  "type": "object",
  "properties": {
    "updatedTime": {
      "pattern": "^[0-9]{4}-?[0-9]{2}-?[0-9]{2}( |T)?[0-9]{2}:?[0-9]{2}:?[0-9]{2}(.[0-9]{1,6})?(Z|[+][0-9]{2}(:|)[0-9]{2})$",
      "type": "string",
      "nullable": true
    },
    "updatedBy": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "modelId": {
      "pattern": "^las:model:[a-f0-9]{32}$",
      "type": "string"
    },
    "description": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "fieldConfig": {
      "type": "object",
      "additionalProperties": {
        "required": [
          "maxLength",
          "type"
        ],
        "type": "object",
        "properties": {
          "description": {
            "anyOf": [
              {
                "maxLength": 4096,
                "type": "string"
              },
              null
            ]
          },
          "type": {
            "type": "string",
            "enum": [
              "date",
              "amount",
              "number",
              "letter",
              "phone",
              "alphanum",
              "alphanumext",
              "all"
            ]
          },
          "maxLength": {
            "maximum": 100,
            "minimum": 1,
            "type": "integer"
          }
        }
      }
    },
    "preprocessConfig": {
      "required": [
        "autoRotate",
        "imageQuality",
        "maxPages"
      ],
      "type": "object",
      "properties": {
        "maxPages": {
          "type": "integer"
        },
        "autoRotate": {
          "type": "boolean"
        },
        "imageQuality": {
          "type": "string",
          "enum": [
            "LOW",
            "HIGH"
          ]
        }
      },
      "additionalProperties": false
    },
    "createdBy": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "name": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "width": {
      "maximum": 1921,
      "minimum": 97,
      "type": "integer"
    },
    "numberOfDataBundles": {
      "minimum": 0,
      "type": "integer"
    },
    "createdTime": {
      "pattern": "^[0-9]{4}-?[0-9]{2}-?[0-9]{2}( |T)?[0-9]{2}:?[0-9]{2}:?[0-9]{2}(.[0-9]{1,6})?(Z|[+][0-9]{2}(:|)[0-9]{2})$",
      "type": "string",
      "nullable": true
    },
    "height": {
      "maximum": 1921,
      "minimum": 97,
      "type": "integer"
    },
    "status": {
      "type": "string",
      "enum": [
        "active",
        "training",
        "inactive"
      ]
    }
  },
  "additionalProperties": false
}
```


#### PATCH /models/{modelId}


| Path name | Path value |
| --- | --- |
| modelId | Id of model on the form las:model:&lt;hex&gt; |


| Header name | Header value |
| --- | --- |
| Content-Type | application/json |
| Authorization | Bearer &lt;your access token here&gt; |
| x-api-key | &lt;your api key here&gt; |





##### Request body JSON Schema
```json
{
  "title": "PATCH /models/modelId",
  "minProperties": 1,
  "type": "object",
  "properties": {
    "preprocessConfig": {
      "required": [
        "autoRotate",
        "imageQuality",
        "maxPages"
      ],
      "type": "object",
      "properties": {
        "maxPages": {
          "type": "integer"
        },
        "autoRotate": {
          "type": "boolean"
        },
        "imageQuality": {
          "type": "string",
          "enum": [
            "LOW",
            "HIGH"
          ]
        }
      },
      "additionalProperties": false
    },
    "width": {
      "maximum": 1921,
      "minimum": 97,
      "type": "integer"
    },
    "name": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "description": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "fieldConfig": {
      "type": "object",
      "additionalProperties": {
        "required": [
          "maxLength",
          "type"
        ],
        "type": "object",
        "properties": {
          "description": {
            "maxLength": 4096,
            "type": "string",
            "nullable": true
          },
          "type": {
            "type": "string",
            "enum": [
              "date",
              "amount",
              "number",
              "letter",
              "phone",
              "alphanum",
              "alphanumext",
              "all"
            ]
          },
          "maxLength": {
            "maximum": 100,
            "minimum": 1,
            "type": "integer"
          }
        }
      }
    },
    "height": {
      "maximum": 1921,
      "minimum": 97,
      "type": "integer"
    },
    "status": {
      "type": "string",
      "enum": [
        "active",
        "training",
        "inactive"
      ]
    }
  },
  "additionalProperties": false
}
```


##### Response body JSON Schema
```json
{
  "title": "model",
  "required": [
    "createdBy",
    "createdTime",
    "description",
    "fieldConfig",
    "height",
    "modelId",
    "name",
    "numberOfDataBundles",
    "preprocessConfig",
    "status",
    "updatedBy",
    "updatedTime",
    "width"
  ],
  "type": "object",
  "properties": {
    "updatedTime": {
      "pattern": "^[0-9]{4}-?[0-9]{2}-?[0-9]{2}( |T)?[0-9]{2}:?[0-9]{2}:?[0-9]{2}(.[0-9]{1,6})?(Z|[+][0-9]{2}(:|)[0-9]{2})$",
      "type": "string",
      "nullable": true
    },
    "updatedBy": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "modelId": {
      "pattern": "^las:model:[a-f0-9]{32}$",
      "type": "string"
    },
    "description": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "fieldConfig": {
      "type": "object",
      "additionalProperties": {
        "required": [
          "maxLength",
          "type"
        ],
        "type": "object",
        "properties": {
          "description": {
            "anyOf": [
              {
                "maxLength": 4096,
                "type": "string"
              },
              null
            ]
          },
          "type": {
            "type": "string",
            "enum": [
              "date",
              "amount",
              "number",
              "letter",
              "phone",
              "alphanum",
              "alphanumext",
              "all"
            ]
          },
          "maxLength": {
            "maximum": 100,
            "minimum": 1,
            "type": "integer"
          }
        }
      }
    },
    "preprocessConfig": {
      "required": [
        "autoRotate",
        "imageQuality",
        "maxPages"
      ],
      "type": "object",
      "properties": {
        "maxPages": {
          "type": "integer"
        },
        "autoRotate": {
          "type": "boolean"
        },
        "imageQuality": {
          "type": "string",
          "enum": [
            "LOW",
            "HIGH"
          ]
        }
      },
      "additionalProperties": false
    },
    "createdBy": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "name": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "width": {
      "maximum": 1921,
      "minimum": 97,
      "type": "integer"
    },
    "numberOfDataBundles": {
      "minimum": 0,
      "type": "integer"
    },
    "createdTime": {
      "pattern": "^[0-9]{4}-?[0-9]{2}-?[0-9]{2}( |T)?[0-9]{2}:?[0-9]{2}:?[0-9]{2}(.[0-9]{1,6})?(Z|[+][0-9]{2}(:|)[0-9]{2})$",
      "type": "string",
      "nullable": true
    },
    "height": {
      "maximum": 1921,
      "minimum": 97,
      "type": "integer"
    },
    "status": {
      "type": "string",
      "enum": [
        "active",
        "training",
        "inactive"
      ]
    }
  },
  "additionalProperties": false
}
```


#### GET /models/{modelId}/dataBundles


| Path name | Path value |
| --- | --- |
| modelId | Id of model on the form las:model:&lt;hex&gt; |


| Header name | Header value |
| --- | --- |
| Authorization | Bearer &lt;your access token here&gt; |
| x-api-key | &lt;your api key here&gt; |


| Query name | Query value |
| --- | --- |
| status | running \| succeeded \| failed \| rejected \| retry |
| nextToken | String value as returned by a previous list operation |
| maxResults | Integer representing maximum number of resources to list |





##### Response body JSON Schema
```json
{
  "title": "dataBundles",
  "required": [
    "dataBundles",
    "nextToken"
  ],
  "type": "object",
  "properties": {
    "nextToken": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "dataBundles": {
      "type": "array",
      "items": {
        "required": [
          "createdBy",
          "createdTime",
          "dataBundleId",
          "datasets",
          "description",
          "modelId",
          "name",
          "status",
          "summary",
          "updatedBy",
          "updatedTime"
        ],
        "type": "object",
        "properties": {
          "summary": {
            "type": "object"
          },
          "updatedTime": {
            "pattern": "^[0-9]{4}-?[0-9]{2}-?[0-9]{2}( |T)?[0-9]{2}:?[0-9]{2}:?[0-9]{2}(.[0-9]{1,6})?(Z|[+][0-9]{2}(:|)[0-9]{2})$",
            "type": "string",
            "nullable": true
          },
          "updatedBy": {
            "maxLength": 4096,
            "type": "string",
            "nullable": true
          },
          "modelId": {
            "pattern": "^las:model:[a-f0-9]{32}$",
            "type": "string"
          },
          "createdBy": {
            "maxLength": 4096,
            "type": "string",
            "nullable": true
          },
          "dataBundleId": {
            "pattern": "^las:model-data-bundle:[a-f0-9]{32}$",
            "type": "string"
          },
          "name": {
            "maxLength": 4096,
            "type": "string",
            "nullable": true
          },
          "description": {
            "maxLength": 4096,
            "type": "string",
            "nullable": true
          },
          "createdTime": {
            "pattern": "^[0-9]{4}-?[0-9]{2}-?[0-9]{2}( |T)?[0-9]{2}:?[0-9]{2}:?[0-9]{2}(.[0-9]{1,6})?(Z|[+][0-9]{2}(:|)[0-9]{2})$",
            "type": "string",
            "nullable": true
          },
          "datasets": {
            "type": "array",
            "items": {
              "required": [
                "containsPersonallyIdentifiableInformation",
                "datasetId",
                "description",
                "numberOfDocuments",
                "retentionInDays",
                "storageLocation",
                "version"
              ],
              "type": "object",
              "properties": {
                "updatedTime": {
                  "pattern": "^[0-9]{4}-?[0-9]{2}-?[0-9]{2}( |T)?[0-9]{2}:?[0-9]{2}:?[0-9]{2}(.[0-9]{1,6})?(Z|[+][0-9]{2}(:|)[0-9]{2})$",
                  "type": "string",
                  "nullable": true
                },
                "retentionInDays": {
                  "maximum": 1825,
                  "minimum": 0,
                  "type": "integer"
                },
                "updatedBy": {
                  "maxLength": 4096,
                  "type": "string",
                  "nullable": true
                },
                "groundTruthSummary": {
                  "type": "object"
                },
                "description": {
                  "maxLength": 4096,
                  "type": "string",
                  "nullable": true
                },
                "storageLocation": {
                  "type": "string",
                  "enum": [
                    "EU"
                  ]
                },
                "version": {
                  "minimum": 0,
                  "type": "integer"
                },
                "createdBy": {
                  "maxLength": 4096,
                  "type": "string",
                  "nullable": true
                },
                "numberOfDocuments": {
                  "minimum": 0,
                  "type": "integer"
                },
                "name": {
                  "maxLength": 4096,
                  "type": "string",
                  "nullable": true
                },
                "datasetId": {
                  "pattern": "^las:dataset:[a-f0-9]{32}$",
                  "type": "string"
                },
                "createdTime": {
                  "pattern": "^[0-9]{4}-?[0-9]{2}-?[0-9]{2}( |T)?[0-9]{2}:?[0-9]{2}:?[0-9]{2}(.[0-9]{1,6})?(Z|[+][0-9]{2}(:|)[0-9]{2})$",
                  "type": "string",
                  "nullable": true
                },
                "containsPersonallyIdentifiableInformation": {
                  "type": "boolean"
                }
              },
              "additionalProperties": false
            }
          },
          "status": {
            "type": "string",
            "enum": [
              "processing",
              "ready",
              "failed"
            ]
          }
        },
        "additionalProperties": false
      }
    },
    "status": {
      "type": "array",
      "items": {
        "type": "string",
        "enum": [
          "processing",
          "ready",
          "failed"
        ]
      }
    }
  },
  "additionalProperties": false
}
```


#### POST /models/{modelId}/dataBundles


| Path name | Path value |
| --- | --- |
| modelId | Id of model on the form las:model:&lt;hex&gt; |


| Header name | Header value |
| --- | --- |
| Content-Type | application/json |
| Authorization | Bearer &lt;your access token here&gt; |
| x-api-key | &lt;your api key here&gt; |





##### Request body JSON Schema
```json
{
  "title": "POST /models/{modelId}/dataBundles",
  "type": "object",
  "properties": {
    "datasetIds": {
      "minItems": 1,
      "type": "array",
      "items": {
        "pattern": "^las:dataset:[a-f0-9]{32}$",
        "type": "string"
      }
    },
    "name": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "description": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    }
  },
  "additionalProperties": false
}
```


##### Response body JSON Schema
```json
{
  "title": "dataBundle",
  "required": [
    "createdBy",
    "createdTime",
    "dataBundleId",
    "datasets",
    "description",
    "modelId",
    "name",
    "status",
    "summary",
    "updatedBy",
    "updatedTime"
  ],
  "type": "object",
  "properties": {
    "summary": {
      "type": "object"
    },
    "updatedTime": {
      "pattern": "^[0-9]{4}-?[0-9]{2}-?[0-9]{2}( |T)?[0-9]{2}:?[0-9]{2}:?[0-9]{2}(.[0-9]{1,6})?(Z|[+][0-9]{2}(:|)[0-9]{2})$",
      "type": "string",
      "nullable": true
    },
    "updatedBy": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "modelId": {
      "pattern": "^las:model:[a-f0-9]{32}$",
      "type": "string"
    },
    "createdBy": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "dataBundleId": {
      "pattern": "^las:model-data-bundle:[a-f0-9]{32}$",
      "type": "string"
    },
    "name": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "description": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "createdTime": {
      "pattern": "^[0-9]{4}-?[0-9]{2}-?[0-9]{2}( |T)?[0-9]{2}:?[0-9]{2}:?[0-9]{2}(.[0-9]{1,6})?(Z|[+][0-9]{2}(:|)[0-9]{2})$",
      "type": "string",
      "nullable": true
    },
    "datasets": {
      "type": "array",
      "items": {
        "required": [
          "containsPersonallyIdentifiableInformation",
          "datasetId",
          "description",
          "numberOfDocuments",
          "retentionInDays",
          "storageLocation",
          "version"
        ],
        "type": "object",
        "properties": {
          "updatedTime": {
            "pattern": "^[0-9]{4}-?[0-9]{2}-?[0-9]{2}( |T)?[0-9]{2}:?[0-9]{2}:?[0-9]{2}(.[0-9]{1,6})?(Z|[+][0-9]{2}(:|)[0-9]{2})$",
            "type": "string",
            "nullable": true
          },
          "retentionInDays": {
            "maximum": 1825,
            "minimum": 0,
            "type": "integer"
          },
          "updatedBy": {
            "maxLength": 4096,
            "type": "string",
            "nullable": true
          },
          "groundTruthSummary": {
            "type": "object"
          },
          "description": {
            "maxLength": 4096,
            "type": "string",
            "nullable": true
          },
          "storageLocation": {
            "type": "string",
            "enum": [
              "EU"
            ]
          },
          "version": {
            "minimum": 0,
            "type": "integer"
          },
          "createdBy": {
            "maxLength": 4096,
            "type": "string",
            "nullable": true
          },
          "numberOfDocuments": {
            "minimum": 0,
            "type": "integer"
          },
          "name": {
            "maxLength": 4096,
            "type": "string",
            "nullable": true
          },
          "datasetId": {
            "pattern": "^las:dataset:[a-f0-9]{32}$",
            "type": "string"
          },
          "createdTime": {
            "pattern": "^[0-9]{4}-?[0-9]{2}-?[0-9]{2}( |T)?[0-9]{2}:?[0-9]{2}:?[0-9]{2}(.[0-9]{1,6})?(Z|[+][0-9]{2}(:|)[0-9]{2})$",
            "type": "string",
            "nullable": true
          },
          "containsPersonallyIdentifiableInformation": {
            "type": "boolean"
          }
        },
        "additionalProperties": false
      }
    },
    "status": {
      "type": "string",
      "enum": [
        "processing",
        "ready",
        "failed"
      ]
    }
  },
  "additionalProperties": false
}
```


#### DELETE /models/{modelId}/dataBundles/{dataBundleId}


| Path name | Path value |
| --- | --- |
| dataBundleId | Id of dataBundle on the form las:dataBundle:&lt;hex&gt; |
| modelId | Id of model on the form las:model:&lt;hex&gt; |


| Header name | Header value |
| --- | --- |
| Authorization | Bearer &lt;your access token here&gt; |
| x-api-key | &lt;your api key here&gt; |








##### Response body JSON Schema
```json
{
  "title": "dataBundle",
  "required": [
    "createdBy",
    "createdTime",
    "dataBundleId",
    "datasets",
    "description",
    "modelId",
    "name",
    "status",
    "summary",
    "updatedBy",
    "updatedTime"
  ],
  "type": "object",
  "properties": {
    "summary": {
      "type": "object"
    },
    "updatedTime": {
      "pattern": "^[0-9]{4}-?[0-9]{2}-?[0-9]{2}( |T)?[0-9]{2}:?[0-9]{2}:?[0-9]{2}(.[0-9]{1,6})?(Z|[+][0-9]{2}(:|)[0-9]{2})$",
      "type": "string",
      "nullable": true
    },
    "updatedBy": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "modelId": {
      "pattern": "^las:model:[a-f0-9]{32}$",
      "type": "string"
    },
    "createdBy": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "dataBundleId": {
      "pattern": "^las:model-data-bundle:[a-f0-9]{32}$",
      "type": "string"
    },
    "name": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "description": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "createdTime": {
      "pattern": "^[0-9]{4}-?[0-9]{2}-?[0-9]{2}( |T)?[0-9]{2}:?[0-9]{2}:?[0-9]{2}(.[0-9]{1,6})?(Z|[+][0-9]{2}(:|)[0-9]{2})$",
      "type": "string",
      "nullable": true
    },
    "datasets": {
      "type": "array",
      "items": {
        "required": [
          "containsPersonallyIdentifiableInformation",
          "datasetId",
          "description",
          "numberOfDocuments",
          "retentionInDays",
          "storageLocation",
          "version"
        ],
        "type": "object",
        "properties": {
          "updatedTime": {
            "pattern": "^[0-9]{4}-?[0-9]{2}-?[0-9]{2}( |T)?[0-9]{2}:?[0-9]{2}:?[0-9]{2}(.[0-9]{1,6})?(Z|[+][0-9]{2}(:|)[0-9]{2})$",
            "type": "string",
            "nullable": true
          },
          "retentionInDays": {
            "maximum": 1825,
            "minimum": 0,
            "type": "integer"
          },
          "updatedBy": {
            "maxLength": 4096,
            "type": "string",
            "nullable": true
          },
          "groundTruthSummary": {
            "type": "object"
          },
          "description": {
            "maxLength": 4096,
            "type": "string",
            "nullable": true
          },
          "storageLocation": {
            "type": "string",
            "enum": [
              "EU"
            ]
          },
          "version": {
            "minimum": 0,
            "type": "integer"
          },
          "createdBy": {
            "maxLength": 4096,
            "type": "string",
            "nullable": true
          },
          "numberOfDocuments": {
            "minimum": 0,
            "type": "integer"
          },
          "name": {
            "maxLength": 4096,
            "type": "string",
            "nullable": true
          },
          "datasetId": {
            "pattern": "^las:dataset:[a-f0-9]{32}$",
            "type": "string"
          },
          "createdTime": {
            "pattern": "^[0-9]{4}-?[0-9]{2}-?[0-9]{2}( |T)?[0-9]{2}:?[0-9]{2}:?[0-9]{2}(.[0-9]{1,6})?(Z|[+][0-9]{2}(:|)[0-9]{2})$",
            "type": "string",
            "nullable": true
          },
          "containsPersonallyIdentifiableInformation": {
            "type": "boolean"
          }
        },
        "additionalProperties": false
      }
    },
    "status": {
      "type": "string",
      "enum": [
        "processing",
        "ready",
        "failed"
      ]
    }
  },
  "additionalProperties": false
}
```


#### PATCH /models/{modelId}/dataBundles/{dataBundleId}


| Path name | Path value |
| --- | --- |
| dataBundleId | Id of dataBundle on the form las:dataBundle:&lt;hex&gt; |
| modelId | Id of model on the form las:model:&lt;hex&gt; |


| Header name | Header value |
| --- | --- |
| Content-Type | application/json |
| Authorization | Bearer &lt;your access token here&gt; |
| x-api-key | &lt;your api key here&gt; |





##### Request body JSON Schema
```json
{
  "title": "PATCH /models/{modelId}/dataBundles/{dataBundleId}",
  "type": "object",
  "properties": {
    "name": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "description": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    }
  },
  "additionalProperties": false
}
```


##### Response body JSON Schema
```json
{
  "title": "dataBundle",
  "required": [
    "createdBy",
    "createdTime",
    "dataBundleId",
    "datasets",
    "description",
    "modelId",
    "name",
    "status",
    "summary",
    "updatedBy",
    "updatedTime"
  ],
  "type": "object",
  "properties": {
    "summary": {
      "type": "object"
    },
    "updatedTime": {
      "pattern": "^[0-9]{4}-?[0-9]{2}-?[0-9]{2}( |T)?[0-9]{2}:?[0-9]{2}:?[0-9]{2}(.[0-9]{1,6})?(Z|[+][0-9]{2}(:|)[0-9]{2})$",
      "type": "string",
      "nullable": true
    },
    "updatedBy": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "modelId": {
      "pattern": "^las:model:[a-f0-9]{32}$",
      "type": "string"
    },
    "createdBy": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "dataBundleId": {
      "pattern": "^las:model-data-bundle:[a-f0-9]{32}$",
      "type": "string"
    },
    "name": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "description": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "createdTime": {
      "pattern": "^[0-9]{4}-?[0-9]{2}-?[0-9]{2}( |T)?[0-9]{2}:?[0-9]{2}:?[0-9]{2}(.[0-9]{1,6})?(Z|[+][0-9]{2}(:|)[0-9]{2})$",
      "type": "string",
      "nullable": true
    },
    "datasets": {
      "type": "array",
      "items": {
        "required": [
          "containsPersonallyIdentifiableInformation",
          "datasetId",
          "description",
          "numberOfDocuments",
          "retentionInDays",
          "storageLocation",
          "version"
        ],
        "type": "object",
        "properties": {
          "updatedTime": {
            "pattern": "^[0-9]{4}-?[0-9]{2}-?[0-9]{2}( |T)?[0-9]{2}:?[0-9]{2}:?[0-9]{2}(.[0-9]{1,6})?(Z|[+][0-9]{2}(:|)[0-9]{2})$",
            "type": "string",
            "nullable": true
          },
          "retentionInDays": {
            "maximum": 1825,
            "minimum": 0,
            "type": "integer"
          },
          "updatedBy": {
            "maxLength": 4096,
            "type": "string",
            "nullable": true
          },
          "groundTruthSummary": {
            "type": "object"
          },
          "description": {
            "maxLength": 4096,
            "type": "string",
            "nullable": true
          },
          "storageLocation": {
            "type": "string",
            "enum": [
              "EU"
            ]
          },
          "version": {
            "minimum": 0,
            "type": "integer"
          },
          "createdBy": {
            "maxLength": 4096,
            "type": "string",
            "nullable": true
          },
          "numberOfDocuments": {
            "minimum": 0,
            "type": "integer"
          },
          "name": {
            "maxLength": 4096,
            "type": "string",
            "nullable": true
          },
          "datasetId": {
            "pattern": "^las:dataset:[a-f0-9]{32}$",
            "type": "string"
          },
          "createdTime": {
            "pattern": "^[0-9]{4}-?[0-9]{2}-?[0-9]{2}( |T)?[0-9]{2}:?[0-9]{2}:?[0-9]{2}(.[0-9]{1,6})?(Z|[+][0-9]{2}(:|)[0-9]{2})$",
            "type": "string",
            "nullable": true
          },
          "containsPersonallyIdentifiableInformation": {
            "type": "boolean"
          }
        },
        "additionalProperties": false
      }
    },
    "status": {
      "type": "string",
      "enum": [
        "processing",
        "ready",
        "failed"
      ]
    }
  },
  "additionalProperties": false
}
```


#### GET /organizations/{organizationId}


| Path name | Path value |
| --- | --- |
| organizationId | Id of organization on the form las:organization:&lt;hex&gt; |


| Header name | Header value |
| --- | --- |
| Authorization | Bearer &lt;your access token here&gt; |
| x-api-key | &lt;your api key here&gt; |








##### Response body JSON Schema
```json
{
  "title": "organization",
  "required": [
    "description",
    "monthlyNumberOfDataBundlesAllowed",
    "monthlyNumberOfDataBundlesCreated",
    "monthlyNumberOfDocumentsAllowed",
    "monthlyNumberOfDocumentsCreated",
    "monthlyNumberOfPredictionsAllowed",
    "monthlyNumberOfPredictionsCreated",
    "monthlyNumberOfTransitionExecutionsAllowed",
    "monthlyNumberOfTransitionExecutionsCreated",
    "monthlyNumberOfWorkflowExecutionsAllowed",
    "monthlyNumberOfWorkflowExecutionsCreated",
    "monthlyUsageSummary",
    "name",
    "numberOfAppClientsAllowed",
    "numberOfAppClientsCreated",
    "numberOfAssetsAllowed",
    "numberOfAssetsCreated",
    "numberOfBatchesAllowed",
    "numberOfBatchesCreated",
    "numberOfModelsAllowed",
    "numberOfModelsCreated",
    "numberOfSecretsAllowed",
    "numberOfSecretsCreated",
    "numberOfTransitionsAllowed",
    "numberOfTransitionsCreated",
    "numberOfUsersAllowed",
    "numberOfUsersCreated",
    "numberOfWorkflowsAllowed",
    "numberOfWorkflowsCreated",
    "organizationId",
    "updatedBy",
    "updatedTime"
  ],
  "type": "object",
  "properties": {
    "numberOfWorkflowsCreated": {
      "minimum": 0,
      "type": "integer"
    },
    "monthlyNumberOfWorkflowExecutionsCreated": {
      "minimum": 0,
      "type": "integer"
    },
    "description": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "numberOfBatchesAllowed": {
      "minimum": 0,
      "type": "integer"
    },
    "numberOfUsersAllowed": {
      "minimum": 0,
      "type": "integer"
    },
    "monthlyNumberOfPredictionsAllowed": {
      "minimum": 0,
      "type": "integer"
    },
    "numberOfDatasetsAllowed": {
      "minimum": 0,
      "type": "integer"
    },
    "monthlyNumberOfDataBundlesAllowed": {
      "minimum": 0,
      "type": "integer"
    },
    "organizationId": {
      "pattern": "^las:organization:[a-f0-9]{32}$",
      "type": "string"
    },
    "numberOfModelsCreated": {
      "minimum": 0,
      "type": "integer"
    },
    "numberOfTransitionsCreated": {
      "minimum": 0,
      "type": "integer"
    },
    "monthlyNumberOfTransitionExecutionsAllowed": {
      "minimum": 0,
      "type": "integer"
    },
    "monthlyNumberOfDocumentsAllowed": {
      "minimum": 0,
      "type": "integer"
    },
    "numberOfSecretsAllowed": {
      "minimum": 0,
      "type": "integer"
    },
    "monthlyUsageSummary": {
      "type": "object"
    },
    "numberOfAppClientsCreated": {
      "minimum": 0,
      "type": "integer"
    },
    "numberOfAssetsCreated": {
      "minimum": 0,
      "type": "integer"
    },
    "updatedTime": {
      "pattern": "^[0-9]{4}-?[0-9]{2}-?[0-9]{2}( |T)?[0-9]{2}:?[0-9]{2}:?[0-9]{2}(.[0-9]{1,6})?(Z|[+][0-9]{2}(:|)[0-9]{2})$",
      "type": "string",
      "nullable": true
    },
    "numberOfWorkflowsAllowed": {
      "minimum": 0,
      "type": "integer"
    },
    "updatedBy": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "monthlyNumberOfWorkflowExecutionsAllowed": {
      "minimum": 0,
      "type": "integer"
    },
    "numberOfBatchesCreated": {
      "minimum": 0,
      "type": "integer"
    },
    "monthlyNumberOfDataBundlesCreated": {
      "minimum": 0,
      "type": "integer"
    },
    "numberOfUsersCreated": {
      "minimum": 0,
      "type": "integer"
    },
    "monthlyNumberOfPredictionsCreated": {
      "minimum": 0,
      "type": "integer"
    },
    "numberOfDatasetsCreated": {
      "minimum": 0,
      "type": "integer"
    },
    "numberOfTransitionsAllowed": {
      "minimum": 0,
      "type": "integer"
    },
    "monthlyNumberOfTransitionExecutionsCreated": {
      "minimum": 0,
      "type": "integer"
    },
    "numberOfModelsAllowed": {
      "minimum": 0,
      "type": "integer"
    },
    "monthlyNumberOfDocumentsCreated": {
      "minimum": 0,
      "type": "integer"
    },
    "numberOfSecretsCreated": {
      "minimum": 0,
      "type": "integer"
    },
    "name": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "numberOfAppClientsAllowed": {
      "minimum": 0,
      "type": "integer"
    },
    "numberOfAssetsAllowed": {
      "minimum": 0,
      "type": "integer"
    }
  },
  "additionalProperties": false
}
```


#### PATCH /organizations/{organizationId}


| Path name | Path value |
| --- | --- |
| organizationId | Id of organization on the form las:organization:&lt;hex&gt; |


| Header name | Header value |
| --- | --- |
| Content-Type | application/json |
| Authorization | Bearer &lt;your access token here&gt; |
| x-api-key | &lt;your api key here&gt; |





##### Request body JSON Schema
```json
{
  "title": "PATCH /organizations/organizationId",
  "minProperties": 1,
  "type": "object",
  "properties": {
    "name": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "description": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    }
  },
  "additionalProperties": false
}
```


##### Response body JSON Schema
```json
{
  "title": "organization",
  "required": [
    "description",
    "monthlyNumberOfDataBundlesAllowed",
    "monthlyNumberOfDataBundlesCreated",
    "monthlyNumberOfDocumentsAllowed",
    "monthlyNumberOfDocumentsCreated",
    "monthlyNumberOfPredictionsAllowed",
    "monthlyNumberOfPredictionsCreated",
    "monthlyNumberOfTransitionExecutionsAllowed",
    "monthlyNumberOfTransitionExecutionsCreated",
    "monthlyNumberOfWorkflowExecutionsAllowed",
    "monthlyNumberOfWorkflowExecutionsCreated",
    "monthlyUsageSummary",
    "name",
    "numberOfAppClientsAllowed",
    "numberOfAppClientsCreated",
    "numberOfAssetsAllowed",
    "numberOfAssetsCreated",
    "numberOfBatchesAllowed",
    "numberOfBatchesCreated",
    "numberOfModelsAllowed",
    "numberOfModelsCreated",
    "numberOfSecretsAllowed",
    "numberOfSecretsCreated",
    "numberOfTransitionsAllowed",
    "numberOfTransitionsCreated",
    "numberOfUsersAllowed",
    "numberOfUsersCreated",
    "numberOfWorkflowsAllowed",
    "numberOfWorkflowsCreated",
    "organizationId",
    "updatedBy",
    "updatedTime"
  ],
  "type": "object",
  "properties": {
    "numberOfWorkflowsCreated": {
      "minimum": 0,
      "type": "integer"
    },
    "monthlyNumberOfWorkflowExecutionsCreated": {
      "minimum": 0,
      "type": "integer"
    },
    "description": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "numberOfBatchesAllowed": {
      "minimum": 0,
      "type": "integer"
    },
    "numberOfUsersAllowed": {
      "minimum": 0,
      "type": "integer"
    },
    "monthlyNumberOfPredictionsAllowed": {
      "minimum": 0,
      "type": "integer"
    },
    "numberOfDatasetsAllowed": {
      "minimum": 0,
      "type": "integer"
    },
    "monthlyNumberOfDataBundlesAllowed": {
      "minimum": 0,
      "type": "integer"
    },
    "organizationId": {
      "pattern": "^las:organization:[a-f0-9]{32}$",
      "type": "string"
    },
    "numberOfModelsCreated": {
      "minimum": 0,
      "type": "integer"
    },
    "numberOfTransitionsCreated": {
      "minimum": 0,
      "type": "integer"
    },
    "monthlyNumberOfTransitionExecutionsAllowed": {
      "minimum": 0,
      "type": "integer"
    },
    "monthlyNumberOfDocumentsAllowed": {
      "minimum": 0,
      "type": "integer"
    },
    "numberOfSecretsAllowed": {
      "minimum": 0,
      "type": "integer"
    },
    "monthlyUsageSummary": {
      "type": "object"
    },
    "numberOfAppClientsCreated": {
      "minimum": 0,
      "type": "integer"
    },
    "numberOfAssetsCreated": {
      "minimum": 0,
      "type": "integer"
    },
    "updatedTime": {
      "pattern": "^[0-9]{4}-?[0-9]{2}-?[0-9]{2}( |T)?[0-9]{2}:?[0-9]{2}:?[0-9]{2}(.[0-9]{1,6})?(Z|[+][0-9]{2}(:|)[0-9]{2})$",
      "type": "string",
      "nullable": true
    },
    "numberOfWorkflowsAllowed": {
      "minimum": 0,
      "type": "integer"
    },
    "updatedBy": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "monthlyNumberOfWorkflowExecutionsAllowed": {
      "minimum": 0,
      "type": "integer"
    },
    "numberOfBatchesCreated": {
      "minimum": 0,
      "type": "integer"
    },
    "monthlyNumberOfDataBundlesCreated": {
      "minimum": 0,
      "type": "integer"
    },
    "numberOfUsersCreated": {
      "minimum": 0,
      "type": "integer"
    },
    "monthlyNumberOfPredictionsCreated": {
      "minimum": 0,
      "type": "integer"
    },
    "numberOfDatasetsCreated": {
      "minimum": 0,
      "type": "integer"
    },
    "numberOfTransitionsAllowed": {
      "minimum": 0,
      "type": "integer"
    },
    "monthlyNumberOfTransitionExecutionsCreated": {
      "minimum": 0,
      "type": "integer"
    },
    "numberOfModelsAllowed": {
      "minimum": 0,
      "type": "integer"
    },
    "monthlyNumberOfDocumentsCreated": {
      "minimum": 0,
      "type": "integer"
    },
    "numberOfSecretsCreated": {
      "minimum": 0,
      "type": "integer"
    },
    "name": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "numberOfAppClientsAllowed": {
      "minimum": 0,
      "type": "integer"
    },
    "numberOfAssetsAllowed": {
      "minimum": 0,
      "type": "integer"
    }
  },
  "additionalProperties": false
}
```


#### GET /predictions





| Header name | Header value |
| --- | --- |
| Authorization | Bearer &lt;your access token here&gt; |
| x-api-key | &lt;your api key here&gt; |


| Query name | Query value |
| --- | --- |
| nextToken | String value as returned by a previous list operation |
| maxResults | Integer representing maximum number of resources to list |





##### Response body JSON Schema
```json
{
  "title": "predictions",
  "required": [
    "nextToken",
    "predictions"
  ],
  "type": "object",
  "properties": {
    "nextToken": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "predictions": {
      "type": "array",
      "items": {
        "required": [
          "documentId",
          "inferenceTime",
          "modelId",
          "predictionId",
          "predictions",
          "timestamp"
        ],
        "type": "object",
        "properties": {
          "modelId": {
            "pattern": "^las:model:[a-f0-9]{32}$",
            "type": "string"
          },
          "inferenceTime": {
            "minimum": 0,
            "type": "number"
          },
          "documentId": {
            "pattern": "^las:document:[a-f0-9]{32}$",
            "type": "string"
          },
          "predictionId": {
            "pattern": "^las:prediction:[a-f0-9]{32}$",
            "type": "string"
          },
          "predictions": {
            "type": "array",
            "items": {
              "required": [
                "confidence",
                "label",
                "value"
              ],
              "type": "object",
              "properties": {
                "confidence": {
                  "maximum": 1,
                  "minimum": 0,
                  "type": "number"
                },
                "label": {
                  "maxLength": 36,
                  "minLength": 1,
                  "pattern": "^[0-9A-Za-z_]+$",
                  "type": "string"
                },
                "value": {
                  "maxLength": 64,
                  "minLength": 1,
                  "type": "string",
                  "nullable": true
                }
              },
              "additionalProperties": false
            }
          },
          "timestamp": {
            "minimum": 1,
            "type": "integer"
          }
        },
        "additionalProperties": false
      }
    }
  },
  "additionalProperties": false
}
```


#### POST /predictions





| Header name | Header value |
| --- | --- |
| Content-Type | application/json |
| Authorization | Bearer &lt;your access token here&gt; |
| x-api-key | &lt;your api key here&gt; |





##### Request body JSON Schema
```json
{
  "title": "POST /predictions",
  "required": [
    "documentId",
    "modelId"
  ],
  "type": "object",
  "properties": {
    "modelId": {
      "pattern": "^las:model:[a-f0-9]{32}$",
      "type": "string"
    },
    "maxPages": {
      "maximum": 3,
      "minimum": 1,
      "type": "integer"
    },
    "documentId": {
      "pattern": "^las:document:[a-f0-9]{32}$",
      "type": "string"
    },
    "autoRotate": {
      "type": "boolean"
    },
    "imageQuality": {
      "type": "string",
      "enum": [
        "LOW",
        "HIGH"
      ]
    }
  },
  "additionalProperties": false
}
```


##### Response body JSON Schema
```json
{
  "title": "prediction",
  "required": [
    "documentId",
    "inferenceTime",
    "modelId",
    "predictionId",
    "predictions",
    "timestamp"
  ],
  "type": "object",
  "properties": {
    "modelId": {
      "pattern": "^las:model:[a-f0-9]{32}$",
      "type": "string"
    },
    "inferenceTime": {
      "minimum": 0,
      "type": "number"
    },
    "documentId": {
      "pattern": "^las:document:[a-f0-9]{32}$",
      "type": "string"
    },
    "predictionId": {
      "pattern": "^las:prediction:[a-f0-9]{32}$",
      "type": "string"
    },
    "predictions": {
      "type": "array",
      "items": {
        "required": [
          "confidence",
          "label",
          "value"
        ],
        "type": "object",
        "properties": {
          "confidence": {
            "maximum": 1,
            "minimum": 0,
            "type": "number"
          },
          "label": {
            "maxLength": 36,
            "minLength": 1,
            "pattern": "^[0-9A-Za-z_]+$",
            "type": "string"
          },
          "value": {
            "maxLength": 64,
            "minLength": 1,
            "type": "string",
            "nullable": true
          }
        },
        "additionalProperties": false
      }
    },
    "timestamp": {
      "minimum": 1,
      "type": "integer"
    }
  },
  "additionalProperties": false
}
```


#### GET /secrets





| Header name | Header value |
| --- | --- |
| Authorization | Bearer &lt;your access token here&gt; |
| x-api-key | &lt;your api key here&gt; |


| Query name | Query value |
| --- | --- |
| nextToken | String value as returned by a previous list operation |
| maxResults | Integer representing maximum number of resources to list |





##### Response body JSON Schema
```json
{
  "title": "secrets",
  "required": [
    "nextToken",
    "secrets"
  ],
  "type": "object",
  "properties": {
    "nextToken": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "secrets": {
      "type": "array",
      "items": {
        "required": [
          "createdBy",
          "createdTime",
          "description",
          "name",
          "secretId",
          "updatedBy",
          "updatedTime"
        ],
        "type": "object",
        "properties": {
          "updatedTime": {
            "pattern": "^[0-9]{4}-?[0-9]{2}-?[0-9]{2}( |T)?[0-9]{2}:?[0-9]{2}:?[0-9]{2}(.[0-9]{1,6})?(Z|[+][0-9]{2}(:|)[0-9]{2})$",
            "type": "string",
            "nullable": true
          },
          "updatedBy": {
            "maxLength": 4096,
            "type": "string",
            "nullable": true
          },
          "createdBy": {
            "maxLength": 4096,
            "type": "string",
            "nullable": true
          },
          "name": {
            "maxLength": 4096,
            "type": "string",
            "nullable": true
          },
          "secretId": {
            "pattern": "^las:secret:[a-f0-9]{32}$",
            "type": "string"
          },
          "createdTime": {
            "pattern": "^[0-9]{4}-?[0-9]{2}-?[0-9]{2}( |T)?[0-9]{2}:?[0-9]{2}:?[0-9]{2}(.[0-9]{1,6})?(Z|[+][0-9]{2}(:|)[0-9]{2})$",
            "type": "string",
            "nullable": true
          },
          "description": {
            "maxLength": 4096,
            "type": "string",
            "nullable": true
          }
        },
        "additionalProperties": false
      }
    }
  },
  "additionalProperties": false
}
```


#### POST /secrets





| Header name | Header value |
| --- | --- |
| Content-Type | application/json |
| Authorization | Bearer &lt;your access token here&gt; |
| x-api-key | &lt;your api key here&gt; |





##### Request body JSON Schema
```json
{
  "title": "POST /secrets",
  "required": [
    "data"
  ],
  "type": "object",
  "properties": {
    "data": {
      "type": "object"
    },
    "name": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "description": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    }
  },
  "additionalProperties": false
}
```


##### Response body JSON Schema
```json
{
  "title": "secret",
  "required": [
    "createdBy",
    "createdTime",
    "description",
    "name",
    "secretId",
    "updatedBy",
    "updatedTime"
  ],
  "type": "object",
  "properties": {
    "updatedTime": {
      "pattern": "^[0-9]{4}-?[0-9]{2}-?[0-9]{2}( |T)?[0-9]{2}:?[0-9]{2}:?[0-9]{2}(.[0-9]{1,6})?(Z|[+][0-9]{2}(:|)[0-9]{2})$",
      "type": "string",
      "nullable": true
    },
    "updatedBy": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "createdBy": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "name": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "secretId": {
      "pattern": "^las:secret:[a-f0-9]{32}$",
      "type": "string"
    },
    "createdTime": {
      "pattern": "^[0-9]{4}-?[0-9]{2}-?[0-9]{2}( |T)?[0-9]{2}:?[0-9]{2}:?[0-9]{2}(.[0-9]{1,6})?(Z|[+][0-9]{2}(:|)[0-9]{2})$",
      "type": "string",
      "nullable": true
    },
    "description": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    }
  },
  "additionalProperties": false
}
```


#### DELETE /secrets/{secretId}


| Path name | Path value |
| --- | --- |
| secretId | Id of secret on the form las:secret:&lt;hex&gt; |


| Header name | Header value |
| --- | --- |
| Authorization | Bearer &lt;your access token here&gt; |
| x-api-key | &lt;your api key here&gt; |








##### Response body JSON Schema
```json
{
  "title": "secret",
  "required": [
    "createdBy",
    "createdTime",
    "description",
    "name",
    "secretId",
    "updatedBy",
    "updatedTime"
  ],
  "type": "object",
  "properties": {
    "updatedTime": {
      "pattern": "^[0-9]{4}-?[0-9]{2}-?[0-9]{2}( |T)?[0-9]{2}:?[0-9]{2}:?[0-9]{2}(.[0-9]{1,6})?(Z|[+][0-9]{2}(:|)[0-9]{2})$",
      "type": "string",
      "nullable": true
    },
    "updatedBy": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "createdBy": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "name": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "secretId": {
      "pattern": "^las:secret:[a-f0-9]{32}$",
      "type": "string"
    },
    "createdTime": {
      "pattern": "^[0-9]{4}-?[0-9]{2}-?[0-9]{2}( |T)?[0-9]{2}:?[0-9]{2}:?[0-9]{2}(.[0-9]{1,6})?(Z|[+][0-9]{2}(:|)[0-9]{2})$",
      "type": "string",
      "nullable": true
    },
    "description": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    }
  },
  "additionalProperties": false
}
```


#### PATCH /secrets/{secretId}


| Path name | Path value |
| --- | --- |
| secretId | Id of secret on the form las:secret:&lt;hex&gt; |


| Header name | Header value |
| --- | --- |
| Content-Type | application/json |
| Authorization | Bearer &lt;your access token here&gt; |
| x-api-key | &lt;your api key here&gt; |





##### Request body JSON Schema
```json
{
  "title": "PATCH /secrets/{secretId}",
  "minProperties": 1,
  "type": "object",
  "properties": {
    "data": {
      "type": "object"
    },
    "name": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "description": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    }
  },
  "additionalProperties": false
}
```


##### Response body JSON Schema
```json
{
  "title": "secret",
  "required": [
    "createdBy",
    "createdTime",
    "description",
    "name",
    "secretId",
    "updatedBy",
    "updatedTime"
  ],
  "type": "object",
  "properties": {
    "updatedTime": {
      "pattern": "^[0-9]{4}-?[0-9]{2}-?[0-9]{2}( |T)?[0-9]{2}:?[0-9]{2}:?[0-9]{2}(.[0-9]{1,6})?(Z|[+][0-9]{2}(:|)[0-9]{2})$",
      "type": "string",
      "nullable": true
    },
    "updatedBy": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "createdBy": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "name": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "secretId": {
      "pattern": "^las:secret:[a-f0-9]{32}$",
      "type": "string"
    },
    "createdTime": {
      "pattern": "^[0-9]{4}-?[0-9]{2}-?[0-9]{2}( |T)?[0-9]{2}:?[0-9]{2}:?[0-9]{2}(.[0-9]{1,6})?(Z|[+][0-9]{2}(:|)[0-9]{2})$",
      "type": "string",
      "nullable": true
    },
    "description": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    }
  },
  "additionalProperties": false
}
```


#### GET /transitions





| Header name | Header value |
| --- | --- |
| Authorization | Bearer &lt;your access token here&gt; |
| x-api-key | &lt;your api key here&gt; |


| Query name | Query value |
| --- | --- |
| transitionType | manual \| docker |
| nextToken | String value as returned by a previous list operation |
| maxResults | Integer representing maximum number of resources to list |





##### Response body JSON Schema
```json
{
  "title": "transitions",
  "required": [
    "nextToken",
    "transitions"
  ],
  "type": "object",
  "properties": {
    "nextToken": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "transitions": {
      "type": "array",
      "items": {
        "required": [
          "createdBy",
          "createdTime",
          "description",
          "name",
          "parameters",
          "timeoutInSeconds",
          "transitionId",
          "transitionType",
          "updatedBy",
          "updatedTime"
        ],
        "type": "object",
        "properties": {
          "updatedTime": {
            "pattern": "^[0-9]{4}-?[0-9]{2}-?[0-9]{2}( |T)?[0-9]{2}:?[0-9]{2}:?[0-9]{2}(.[0-9]{1,6})?(Z|[+][0-9]{2}(:|)[0-9]{2})$",
            "type": "string",
            "nullable": true
          },
          "updatedBy": {
            "maxLength": 4096,
            "type": "string",
            "nullable": true
          },
          "transitionId": {
            "anyOf": [
              {
                "pattern": "^las:transition:[a-f0-9]{32}$",
                "type": "string"
              },
              {
                "pattern": "^las:transition:commons-[0-9A-Za-z-]+$",
                "type": "string"
              }
            ]
          },
          "description": {
            "maxLength": 4096,
            "type": "string",
            "nullable": true
          },
          "inputJsonSchema": {
            "type": "object"
          },
          "timeoutInSeconds": {
            "maximum": 1800,
            "minimum": 60,
            "type": "integer"
          },
          "outputJsonSchema": {
            "type": "object"
          },
          "assets": {
            "type": "object",
            "properties": {
              "jsRemoteComponent": {
                "pattern": "^las:asset:[a-f0-9]{32}$",
                "type": "string"
              }
            },
            "additionalProperties": {
              "pattern": "^las:asset:[a-f0-9]{32}$",
              "type": "string"
            }
          },
          "createdBy": {
            "maxLength": 4096,
            "type": "string",
            "nullable": true
          },
          "name": {
            "maxLength": 4096,
            "type": "string",
            "nullable": true
          },
          "createdTime": {
            "pattern": "^[0-9]{4}-?[0-9]{2}-?[0-9]{2}( |T)?[0-9]{2}:?[0-9]{2}:?[0-9]{2}(.[0-9]{1,6})?(Z|[+][0-9]{2}(:|)[0-9]{2})$",
            "type": "string",
            "nullable": true
          },
          "transitionType": {
            "type": "string",
            "enum": [
              "docker",
              "manual"
            ]
          },
          "parameters": {
            "type": "object"
          }
        },
        "additionalProperties": false
      }
    },
    "transitionType": {
      "type": "array",
      "items": {
        "type": "string",
        "enum": [
          "docker",
          "manual"
        ]
      }
    }
  },
  "additionalProperties": false
}
```


#### POST /transitions





| Header name | Header value |
| --- | --- |
| Content-Type | application/json |
| Authorization | Bearer &lt;your access token here&gt; |
| x-api-key | &lt;your api key here&gt; |





##### Request body JSON Schema
```json
{
  "title": "POST /transitions",
  "required": [
    "transitionType"
  ],
  "type": "object",
  "properties": {
    "outputJsonSchema": {
      "type": "object"
    },
    "name": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "description": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "transitionType": {
      "type": "string",
      "enum": [
        "docker",
        "manual"
      ]
    },
    "inputJsonSchema": {
      "type": "object"
    },
    "parameters": {
      "anyOf": [
        {
          "required": [
            "imageUrl"
          ],
          "type": "object",
          "properties": {
            "environmentSecrets": {
              "type": "array",
              "items": {
                "pattern": "^las:secret:[a-f0-9]{32}$",
                "type": "string"
              }
            },
            "environment": {
              "type": "object",
              "additionalProperties": {
                "type": "string"
              }
            },
            "memory": {
              "type": "integer",
              "enum": [
                512,
                1024,
                2048
              ]
            },
            "imageUrl": {
              "type": "string"
            },
            "secretId": {
              "pattern": "^las:secret:[a-f0-9]{32}$",
              "type": "string"
            },
            "cpu": {
              "type": "integer",
              "enum": [
                256
              ]
            }
          },
          "additionalProperties": false
        },
        {
          "type": "object",
          "properties": {
            "assets": {
              "type": "object",
              "properties": {
                "jsRemoteComponent": {
                  "pattern": "^las:asset:[a-f0-9]{32}$",
                  "type": "string"
                }
              },
              "additionalProperties": {
                "pattern": "^las:asset:[a-f0-9]{32}$",
                "type": "string"
              }
            }
          },
          "additionalProperties": false
        }
      ]
    },
    "timeoutInSeconds": {
      "maximum": 1800,
      "minimum": 60,
      "type": "integer"
    }
  },
  "additionalProperties": false
}
```


##### Response body JSON Schema
```json
{
  "title": "transition",
  "required": [
    "createdBy",
    "createdTime",
    "description",
    "name",
    "parameters",
    "timeoutInSeconds",
    "transitionId",
    "transitionType",
    "updatedBy",
    "updatedTime"
  ],
  "type": "object",
  "properties": {
    "updatedTime": {
      "pattern": "^[0-9]{4}-?[0-9]{2}-?[0-9]{2}( |T)?[0-9]{2}:?[0-9]{2}:?[0-9]{2}(.[0-9]{1,6})?(Z|[+][0-9]{2}(:|)[0-9]{2})$",
      "type": "string",
      "nullable": true
    },
    "updatedBy": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "transitionId": {
      "anyOf": [
        {
          "pattern": "^las:transition:[a-f0-9]{32}$",
          "type": "string"
        },
        {
          "pattern": "^las:transition:commons-[0-9A-Za-z-]+$",
          "type": "string"
        }
      ]
    },
    "description": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "inputJsonSchema": {
      "type": "object"
    },
    "timeoutInSeconds": {
      "maximum": 1800,
      "minimum": 60,
      "type": "integer"
    },
    "outputJsonSchema": {
      "type": "object"
    },
    "assets": {
      "type": "object",
      "properties": {
        "jsRemoteComponent": {
          "pattern": "^las:asset:[a-f0-9]{32}$",
          "type": "string"
        }
      },
      "additionalProperties": {
        "pattern": "^las:asset:[a-f0-9]{32}$",
        "type": "string"
      }
    },
    "createdBy": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "name": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "createdTime": {
      "pattern": "^[0-9]{4}-?[0-9]{2}-?[0-9]{2}( |T)?[0-9]{2}:?[0-9]{2}:?[0-9]{2}(.[0-9]{1,6})?(Z|[+][0-9]{2}(:|)[0-9]{2})$",
      "type": "string",
      "nullable": true
    },
    "transitionType": {
      "type": "string",
      "enum": [
        "docker",
        "manual"
      ]
    },
    "parameters": {
      "type": "object"
    }
  },
  "additionalProperties": false
}
```


#### DELETE /transitions/{transitionId}


| Path name | Path value |
| --- | --- |
| transitionId | Id of transition on the form las:transition:&lt;hex&gt; |


| Header name | Header value |
| --- | --- |
| Authorization | Bearer &lt;your access token here&gt; |
| x-api-key | &lt;your api key here&gt; |








##### Response body JSON Schema
```json
{
  "title": "transition",
  "required": [
    "createdBy",
    "createdTime",
    "description",
    "name",
    "parameters",
    "timeoutInSeconds",
    "transitionId",
    "transitionType",
    "updatedBy",
    "updatedTime"
  ],
  "type": "object",
  "properties": {
    "updatedTime": {
      "pattern": "^[0-9]{4}-?[0-9]{2}-?[0-9]{2}( |T)?[0-9]{2}:?[0-9]{2}:?[0-9]{2}(.[0-9]{1,6})?(Z|[+][0-9]{2}(:|)[0-9]{2})$",
      "type": "string",
      "nullable": true
    },
    "updatedBy": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "transitionId": {
      "anyOf": [
        {
          "pattern": "^las:transition:[a-f0-9]{32}$",
          "type": "string"
        },
        {
          "pattern": "^las:transition:commons-[0-9A-Za-z-]+$",
          "type": "string"
        }
      ]
    },
    "description": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "inputJsonSchema": {
      "type": "object"
    },
    "timeoutInSeconds": {
      "maximum": 1800,
      "minimum": 60,
      "type": "integer"
    },
    "outputJsonSchema": {
      "type": "object"
    },
    "assets": {
      "type": "object",
      "properties": {
        "jsRemoteComponent": {
          "pattern": "^las:asset:[a-f0-9]{32}$",
          "type": "string"
        }
      },
      "additionalProperties": {
        "pattern": "^las:asset:[a-f0-9]{32}$",
        "type": "string"
      }
    },
    "createdBy": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "name": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "createdTime": {
      "pattern": "^[0-9]{4}-?[0-9]{2}-?[0-9]{2}( |T)?[0-9]{2}:?[0-9]{2}:?[0-9]{2}(.[0-9]{1,6})?(Z|[+][0-9]{2}(:|)[0-9]{2})$",
      "type": "string",
      "nullable": true
    },
    "transitionType": {
      "type": "string",
      "enum": [
        "docker",
        "manual"
      ]
    },
    "parameters": {
      "type": "object"
    }
  },
  "additionalProperties": false
}
```


#### GET /transitions/{transitionId}


| Path name | Path value |
| --- | --- |
| transitionId | Id of transition on the form las:transition:&lt;hex&gt; |


| Header name | Header value |
| --- | --- |
| Authorization | Bearer &lt;your access token here&gt; |
| x-api-key | &lt;your api key here&gt; |








##### Response body JSON Schema
```json
{
  "title": "transition",
  "required": [
    "createdBy",
    "createdTime",
    "description",
    "name",
    "parameters",
    "timeoutInSeconds",
    "transitionId",
    "transitionType",
    "updatedBy",
    "updatedTime"
  ],
  "type": "object",
  "properties": {
    "updatedTime": {
      "pattern": "^[0-9]{4}-?[0-9]{2}-?[0-9]{2}( |T)?[0-9]{2}:?[0-9]{2}:?[0-9]{2}(.[0-9]{1,6})?(Z|[+][0-9]{2}(:|)[0-9]{2})$",
      "type": "string",
      "nullable": true
    },
    "updatedBy": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "transitionId": {
      "anyOf": [
        {
          "pattern": "^las:transition:[a-f0-9]{32}$",
          "type": "string"
        },
        {
          "pattern": "^las:transition:commons-[0-9A-Za-z-]+$",
          "type": "string"
        }
      ]
    },
    "description": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "inputJsonSchema": {
      "type": "object"
    },
    "timeoutInSeconds": {
      "maximum": 1800,
      "minimum": 60,
      "type": "integer"
    },
    "outputJsonSchema": {
      "type": "object"
    },
    "assets": {
      "type": "object",
      "properties": {
        "jsRemoteComponent": {
          "pattern": "^las:asset:[a-f0-9]{32}$",
          "type": "string"
        }
      },
      "additionalProperties": {
        "pattern": "^las:asset:[a-f0-9]{32}$",
        "type": "string"
      }
    },
    "createdBy": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "name": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "createdTime": {
      "pattern": "^[0-9]{4}-?[0-9]{2}-?[0-9]{2}( |T)?[0-9]{2}:?[0-9]{2}:?[0-9]{2}(.[0-9]{1,6})?(Z|[+][0-9]{2}(:|)[0-9]{2})$",
      "type": "string",
      "nullable": true
    },
    "transitionType": {
      "type": "string",
      "enum": [
        "docker",
        "manual"
      ]
    },
    "parameters": {
      "type": "object"
    }
  },
  "additionalProperties": false
}
```


#### PATCH /transitions/{transitionId}


| Path name | Path value |
| --- | --- |
| transitionId | Id of transition on the form las:transition:&lt;hex&gt; |


| Header name | Header value |
| --- | --- |
| Content-Type | application/json |
| Authorization | Bearer &lt;your access token here&gt; |
| x-api-key | &lt;your api key here&gt; |





##### Request body JSON Schema
```json
{
  "title": "PATCH /transitions/{transitionId}",
  "minProperties": 1,
  "type": "object",
  "properties": {
    "environmentSecrets": {
      "type": "array",
      "items": {
        "pattern": "^las:secret:[a-f0-9]{32}$",
        "type": "string"
      }
    },
    "environment": {
      "type": "object",
      "additionalProperties": {
        "type": "string"
      }
    },
    "outputJsonSchema": {
      "type": "object"
    },
    "assets": {
      "type": "object",
      "properties": {
        "jsRemoteComponent": {
          "pattern": "^las:asset:[a-f0-9]{32}$",
          "type": "string"
        }
      },
      "additionalProperties": {
        "pattern": "^las:asset:[a-f0-9]{32}$",
        "type": "string"
      }
    },
    "name": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "description": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "inputJsonSchema": {
      "type": "object"
    }
  },
  "additionalProperties": false
}
```


##### Response body JSON Schema
```json
{
  "title": "transition",
  "required": [
    "createdBy",
    "createdTime",
    "description",
    "name",
    "parameters",
    "timeoutInSeconds",
    "transitionId",
    "transitionType",
    "updatedBy",
    "updatedTime"
  ],
  "type": "object",
  "properties": {
    "updatedTime": {
      "pattern": "^[0-9]{4}-?[0-9]{2}-?[0-9]{2}( |T)?[0-9]{2}:?[0-9]{2}:?[0-9]{2}(.[0-9]{1,6})?(Z|[+][0-9]{2}(:|)[0-9]{2})$",
      "type": "string",
      "nullable": true
    },
    "updatedBy": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "transitionId": {
      "anyOf": [
        {
          "pattern": "^las:transition:[a-f0-9]{32}$",
          "type": "string"
        },
        {
          "pattern": "^las:transition:commons-[0-9A-Za-z-]+$",
          "type": "string"
        }
      ]
    },
    "description": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "inputJsonSchema": {
      "type": "object"
    },
    "timeoutInSeconds": {
      "maximum": 1800,
      "minimum": 60,
      "type": "integer"
    },
    "outputJsonSchema": {
      "type": "object"
    },
    "assets": {
      "type": "object",
      "properties": {
        "jsRemoteComponent": {
          "pattern": "^las:asset:[a-f0-9]{32}$",
          "type": "string"
        }
      },
      "additionalProperties": {
        "pattern": "^las:asset:[a-f0-9]{32}$",
        "type": "string"
      }
    },
    "createdBy": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "name": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "createdTime": {
      "pattern": "^[0-9]{4}-?[0-9]{2}-?[0-9]{2}( |T)?[0-9]{2}:?[0-9]{2}:?[0-9]{2}(.[0-9]{1,6})?(Z|[+][0-9]{2}(:|)[0-9]{2})$",
      "type": "string",
      "nullable": true
    },
    "transitionType": {
      "type": "string",
      "enum": [
        "docker",
        "manual"
      ]
    },
    "parameters": {
      "type": "object"
    }
  },
  "additionalProperties": false
}
```


#### GET /transitions/{transitionId}/executions


| Path name | Path value |
| --- | --- |
| transitionId | Id of transition on the form las:transition:&lt;hex&gt; |


| Header name | Header value |
| --- | --- |
| Authorization | Bearer &lt;your access token here&gt; |
| x-api-key | &lt;your api key here&gt; |


| Query name | Query value |
| --- | --- |
| nextToken | String value as returned by a previous list operation |
| order | ascending \| descending |
| executionId | String |
| status | running \| succeeded \| failed \| rejected \| retry |
| maxResults | Integer representing maximum number of resources to list |
| sortBy | startTime \| endTime |





##### Response body JSON Schema
```json
{
  "title": "transition-executions",
  "required": [
    "executions",
    "nextToken",
    "transitionId"
  ],
  "type": "object",
  "properties": {
    "executions": {
      "type": "array",
      "items": {
        "required": [
          "completedBy",
          "executionId",
          "input",
          "status",
          "transitionId"
        ],
        "type": "object",
        "properties": {
          "executionId": {
            "pattern": "^las:transition-execution:[a-f0-9]{32}$",
            "type": "string"
          },
          "input": {
            "type": "object"
          },
          "transitionId": {
            "anyOf": [
              {
                "pattern": "^las:transition:[a-f0-9]{32}$",
                "type": "string"
              },
              {
                "pattern": "^las:transition:commons-[0-9A-Za-z-]+$",
                "type": "string"
              }
            ]
          },
          "startTime": {
            "pattern": "^[0-9]{4}-?[0-9]{2}-?[0-9]{2}( |T)?[0-9]{2}:?[0-9]{2}:?[0-9]{2}(.[0-9]{1,6})?(Z|[+][0-9]{2}(:|)[0-9]{2})$",
            "type": "string",
            "nullable": true
          },
          "logId": {
            "pattern": "^las:log:[a-f0-9]{32}$",
            "type": "string",
            "nullable": true
          },
          "endTime": {
            "pattern": "^[0-9]{4}-?[0-9]{2}-?[0-9]{2}( |T)?[0-9]{2}:?[0-9]{2}:?[0-9]{2}(.[0-9]{1,6})?(Z|[+][0-9]{2}(:|)[0-9]{2})$",
            "type": "string",
            "nullable": true
          },
          "completedBy": {
            "maxLength": 4096,
            "type": "string",
            "nullable": true
          },
          "status": {
            "type": "string",
            "enum": [
              "running",
              "succeeded",
              "failed",
              "rejected",
              "retry"
            ]
          }
        },
        "additionalProperties": false
      }
    },
    "transitionId": {
      "anyOf": [
        {
          "pattern": "^las:transition:[a-f0-9]{32}$",
          "type": "string"
        },
        {
          "pattern": "^las:transition:commons-[0-9A-Za-z-]+$",
          "type": "string"
        }
      ]
    },
    "nextToken": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "status": {
      "type": "array",
      "items": {
        "type": "string",
        "enum": [
          "running",
          "succeeded",
          "failed",
          "rejected",
          "retry"
        ]
      }
    }
  },
  "additionalProperties": false
}
```


#### POST /transitions/{transitionId}/executions


| Path name | Path value |
| --- | --- |
| transitionId | Id of transition on the form las:transition:&lt;hex&gt; |


| Header name | Header value |
| --- | --- |
| Content-Type | application/json |
| Authorization | Bearer &lt;your access token here&gt; |
| x-api-key | &lt;your api key here&gt; |





##### Request body JSON Schema
```json
{
  "title": "POST /transitions/{transitionId}/executions",
  "type": "object"
}
```


##### Response body JSON Schema
```json
{
  "title": "transition-execution",
  "required": [
    "completedBy",
    "executionId",
    "input",
    "status",
    "transitionId"
  ],
  "type": "object",
  "properties": {
    "executionId": {
      "pattern": "^las:transition-execution:[a-f0-9]{32}$",
      "type": "string"
    },
    "input": {
      "type": "object"
    },
    "transitionId": {
      "anyOf": [
        {
          "pattern": "^las:transition:[a-f0-9]{32}$",
          "type": "string"
        },
        {
          "pattern": "^las:transition:commons-[0-9A-Za-z-]+$",
          "type": "string"
        }
      ]
    },
    "startTime": {
      "pattern": "^[0-9]{4}-?[0-9]{2}-?[0-9]{2}( |T)?[0-9]{2}:?[0-9]{2}:?[0-9]{2}(.[0-9]{1,6})?(Z|[+][0-9]{2}(:|)[0-9]{2})$",
      "type": "string",
      "nullable": true
    },
    "logId": {
      "pattern": "^las:log:[a-f0-9]{32}$",
      "type": "string",
      "nullable": true
    },
    "endTime": {
      "pattern": "^[0-9]{4}-?[0-9]{2}-?[0-9]{2}( |T)?[0-9]{2}:?[0-9]{2}:?[0-9]{2}(.[0-9]{1,6})?(Z|[+][0-9]{2}(:|)[0-9]{2})$",
      "type": "string",
      "nullable": true
    },
    "completedBy": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "status": {
      "type": "string",
      "enum": [
        "running",
        "succeeded",
        "failed",
        "rejected",
        "retry"
      ]
    }
  },
  "additionalProperties": false
}
```


#### GET /transitions/{transitionId}/executions/{executionId}


| Path name | Path value |
| --- | --- |
| transitionId | Id of transition on the form las:transition:&lt;hex&gt; |
| executionId | Id of execution on the form las:transition-execution:&lt;hex&gt; |


| Header name | Header value |
| --- | --- |
| Authorization | Bearer &lt;your access token here&gt; |
| x-api-key | &lt;your api key here&gt; |








##### Response body JSON Schema
```json
{
  "title": "transition-execution",
  "required": [
    "completedBy",
    "executionId",
    "input",
    "status",
    "transitionId"
  ],
  "type": "object",
  "properties": {
    "executionId": {
      "pattern": "^las:transition-execution:[a-f0-9]{32}$",
      "type": "string"
    },
    "input": {
      "type": "object"
    },
    "transitionId": {
      "anyOf": [
        {
          "pattern": "^las:transition:[a-f0-9]{32}$",
          "type": "string"
        },
        {
          "pattern": "^las:transition:commons-[0-9A-Za-z-]+$",
          "type": "string"
        }
      ]
    },
    "startTime": {
      "pattern": "^[0-9]{4}-?[0-9]{2}-?[0-9]{2}( |T)?[0-9]{2}:?[0-9]{2}:?[0-9]{2}(.[0-9]{1,6})?(Z|[+][0-9]{2}(:|)[0-9]{2})$",
      "type": "string",
      "nullable": true
    },
    "logId": {
      "pattern": "^las:log:[a-f0-9]{32}$",
      "type": "string",
      "nullable": true
    },
    "endTime": {
      "pattern": "^[0-9]{4}-?[0-9]{2}-?[0-9]{2}( |T)?[0-9]{2}:?[0-9]{2}:?[0-9]{2}(.[0-9]{1,6})?(Z|[+][0-9]{2}(:|)[0-9]{2})$",
      "type": "string",
      "nullable": true
    },
    "completedBy": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "status": {
      "type": "string",
      "enum": [
        "running",
        "succeeded",
        "failed",
        "rejected",
        "retry"
      ]
    }
  },
  "additionalProperties": false
}
```


#### PATCH /transitions/{transitionId}/executions/{executionId}


| Path name | Path value |
| --- | --- |
| transitionId | Id of transition on the form las:transition:&lt;hex&gt; |
| executionId | Id of execution on the form las:transition-execution:&lt;hex&gt; |


| Header name | Header value |
| --- | --- |
| Content-Type | application/json |
| Authorization | Bearer &lt;your access token here&gt; |
| x-api-key | &lt;your api key here&gt; |





##### Request body JSON Schema
```json
{
  "title": "PATCH transitions/{transitionId}/executions/{executionId}",
  "type": "object",
  "properties": {
    "output": {
      "type": "object"
    },
    "startTime": {
      "pattern": "^[0-9]{4}-?[0-9]{2}-?[0-9]{2}( |T)?[0-9]{2}:?[0-9]{2}:?[0-9]{2}(.[0-9]{1,6})?(Z|[+][0-9]{2}(:|)[0-9]{2})$",
      "type": "string",
      "nullable": true
    },
    "error": {
      "required": [
        "message"
      ],
      "type": "object",
      "properties": {
        "message": {
          "type": "string"
        }
      },
      "additionalProperties": false
    },
    "status": {
      "type": "string"
    }
  },
  "additionalProperties": false,
  "anyOf": [
    {
      "type": "object",
      "properties": {
        "status": {
          "type": "string",
          "enum": [
            "succeeded"
          ]
        }
      }
    },
    {
      "type": "object",
      "properties": {
        "status": {
          "type": "string",
          "enum": [
            "failed",
            "rejected",
            "retry"
          ]
        }
      }
    }
  ]
}
```


##### Response body JSON Schema
```json
{
  "title": "transition-execution",
  "required": [
    "completedBy",
    "executionId",
    "input",
    "status",
    "transitionId"
  ],
  "type": "object",
  "properties": {
    "executionId": {
      "pattern": "^las:transition-execution:[a-f0-9]{32}$",
      "type": "string"
    },
    "input": {
      "type": "object"
    },
    "transitionId": {
      "anyOf": [
        {
          "pattern": "^las:transition:[a-f0-9]{32}$",
          "type": "string"
        },
        {
          "pattern": "^las:transition:commons-[0-9A-Za-z-]+$",
          "type": "string"
        }
      ]
    },
    "startTime": {
      "pattern": "^[0-9]{4}-?[0-9]{2}-?[0-9]{2}( |T)?[0-9]{2}:?[0-9]{2}:?[0-9]{2}(.[0-9]{1,6})?(Z|[+][0-9]{2}(:|)[0-9]{2})$",
      "type": "string",
      "nullable": true
    },
    "logId": {
      "pattern": "^las:log:[a-f0-9]{32}$",
      "type": "string",
      "nullable": true
    },
    "endTime": {
      "pattern": "^[0-9]{4}-?[0-9]{2}-?[0-9]{2}( |T)?[0-9]{2}:?[0-9]{2}:?[0-9]{2}(.[0-9]{1,6})?(Z|[+][0-9]{2}(:|)[0-9]{2})$",
      "type": "string",
      "nullable": true
    },
    "completedBy": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "status": {
      "type": "string",
      "enum": [
        "running",
        "succeeded",
        "failed",
        "rejected",
        "retry"
      ]
    }
  },
  "additionalProperties": false
}
```


#### POST /transitions/{transitionId}/executions/{executionId}/heartbeats


| Path name | Path value |
| --- | --- |
| transitionId | Id of transition on the form las:transition:&lt;hex&gt; |
| executionId | Id of execution on the form las:transition-execution:&lt;hex&gt; |


| Header name | Header value |
| --- | --- |
| Content-Type | application/json |
| Authorization | Bearer &lt;your access token here&gt; |
| x-api-key | &lt;your api key here&gt; |





##### Request body JSON Schema
```json
{
  "title": "POST /transitions/{transitionId}/executions/{executionId}/heartbeats",
  "type": "object"
}
```





#### GET /users





| Header name | Header value |
| --- | --- |
| Authorization | Bearer &lt;your access token here&gt; |
| x-api-key | &lt;your api key here&gt; |


| Query name | Query value |
| --- | --- |
| nextToken | String value as returned by a previous list operation |
| maxResults | Integer representing maximum number of resources to list |





##### Response body JSON Schema
```json
{
  "title": "users",
  "required": [
    "nextToken",
    "users"
  ],
  "type": "object",
  "properties": {
    "nextToken": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "users": {
      "type": "array",
      "items": {
        "required": [
          "createdBy",
          "createdTime",
          "email",
          "updatedBy",
          "updatedTime",
          "userId"
        ],
        "type": "object",
        "properties": {
          "updatedTime": {
            "pattern": "^[0-9]{4}-?[0-9]{2}-?[0-9]{2}( |T)?[0-9]{2}:?[0-9]{2}:?[0-9]{2}(.[0-9]{1,6})?(Z|[+][0-9]{2}(:|)[0-9]{2})$",
            "type": "string",
            "nullable": true
          },
          "updatedBy": {
            "maxLength": 4096,
            "type": "string",
            "nullable": true
          },
          "createdBy": {
            "maxLength": 4096,
            "type": "string",
            "nullable": true
          },
          "name": {
            "maxLength": 4096,
            "type": "string",
            "nullable": true
          },
          "createdTime": {
            "pattern": "^[0-9]{4}-?[0-9]{2}-?[0-9]{2}( |T)?[0-9]{2}:?[0-9]{2}:?[0-9]{2}(.[0-9]{1,6})?(Z|[+][0-9]{2}(:|)[0-9]{2})$",
            "type": "string",
            "nullable": true
          },
          "avatar": {
            "maxLength": 131072,
            "type": "string",
            "nullable": true
          },
          "userId": {
            "pattern": "^las:user:[a-f0-9]{32}$",
            "type": "string"
          },
          "email": {
            "pattern": "^[A-Za-z0-9][-+._A-Za-z0-9]*@([-_.A-Za-z0-9]+\\.)+[A-Za-z]{2,}$",
            "type": "string"
          }
        },
        "additionalProperties": false
      }
    }
  },
  "additionalProperties": false
}
```


#### POST /users





| Header name | Header value |
| --- | --- |
| Content-Type | application/json |
| Authorization | Bearer &lt;your access token here&gt; |
| x-api-key | &lt;your api key here&gt; |





##### Request body JSON Schema
```json
{
  "title": "POST /users",
  "required": [
    "email"
  ],
  "type": "object",
  "properties": {
    "name": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "avatar": {
      "maxLength": 131072,
      "type": "string",
      "nullable": true
    },
    "email": {
      "pattern": "^[A-Za-z0-9][-+._A-Za-z0-9]*@([-_.A-Za-z0-9]+\\.)+[A-Za-z]{2,}$",
      "type": "string"
    },
    "appClientId": {
      "pattern": "^las:app-client:[a-f0-9]{32}$",
      "type": "string"
    }
  },
  "additionalProperties": false
}
```


##### Response body JSON Schema
```json
{
  "title": "user",
  "required": [
    "createdBy",
    "createdTime",
    "email",
    "updatedBy",
    "updatedTime",
    "userId"
  ],
  "type": "object",
  "properties": {
    "updatedTime": {
      "pattern": "^[0-9]{4}-?[0-9]{2}-?[0-9]{2}( |T)?[0-9]{2}:?[0-9]{2}:?[0-9]{2}(.[0-9]{1,6})?(Z|[+][0-9]{2}(:|)[0-9]{2})$",
      "type": "string",
      "nullable": true
    },
    "updatedBy": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "createdBy": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "name": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "createdTime": {
      "pattern": "^[0-9]{4}-?[0-9]{2}-?[0-9]{2}( |T)?[0-9]{2}:?[0-9]{2}:?[0-9]{2}(.[0-9]{1,6})?(Z|[+][0-9]{2}(:|)[0-9]{2})$",
      "type": "string",
      "nullable": true
    },
    "avatar": {
      "maxLength": 131072,
      "type": "string",
      "nullable": true
    },
    "userId": {
      "pattern": "^las:user:[a-f0-9]{32}$",
      "type": "string"
    },
    "email": {
      "pattern": "^[A-Za-z0-9][-+._A-Za-z0-9]*@([-_.A-Za-z0-9]+\\.)+[A-Za-z]{2,}$",
      "type": "string"
    }
  },
  "additionalProperties": false
}
```


#### DELETE /users/{userId}


| Path name | Path value |
| --- | --- |
| userId | Id of user on the form las:user:&lt;hex&gt; |


| Header name | Header value |
| --- | --- |
| Authorization | Bearer &lt;your access token here&gt; |
| x-api-key | &lt;your api key here&gt; |








##### Response body JSON Schema
```json
{
  "title": "user",
  "required": [
    "createdBy",
    "createdTime",
    "email",
    "updatedBy",
    "updatedTime",
    "userId"
  ],
  "type": "object",
  "properties": {
    "updatedTime": {
      "pattern": "^[0-9]{4}-?[0-9]{2}-?[0-9]{2}( |T)?[0-9]{2}:?[0-9]{2}:?[0-9]{2}(.[0-9]{1,6})?(Z|[+][0-9]{2}(:|)[0-9]{2})$",
      "type": "string",
      "nullable": true
    },
    "updatedBy": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "createdBy": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "name": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "createdTime": {
      "pattern": "^[0-9]{4}-?[0-9]{2}-?[0-9]{2}( |T)?[0-9]{2}:?[0-9]{2}:?[0-9]{2}(.[0-9]{1,6})?(Z|[+][0-9]{2}(:|)[0-9]{2})$",
      "type": "string",
      "nullable": true
    },
    "avatar": {
      "maxLength": 131072,
      "type": "string",
      "nullable": true
    },
    "userId": {
      "pattern": "^las:user:[a-f0-9]{32}$",
      "type": "string"
    },
    "email": {
      "pattern": "^[A-Za-z0-9][-+._A-Za-z0-9]*@([-_.A-Za-z0-9]+\\.)+[A-Za-z]{2,}$",
      "type": "string"
    }
  },
  "additionalProperties": false
}
```


#### GET /users/{userId}


| Path name | Path value |
| --- | --- |
| userId | Id of user on the form las:user:&lt;hex&gt; |


| Header name | Header value |
| --- | --- |
| Authorization | Bearer &lt;your access token here&gt; |
| x-api-key | &lt;your api key here&gt; |








##### Response body JSON Schema
```json
{
  "title": "user",
  "required": [
    "createdBy",
    "createdTime",
    "email",
    "updatedBy",
    "updatedTime",
    "userId"
  ],
  "type": "object",
  "properties": {
    "updatedTime": {
      "pattern": "^[0-9]{4}-?[0-9]{2}-?[0-9]{2}( |T)?[0-9]{2}:?[0-9]{2}:?[0-9]{2}(.[0-9]{1,6})?(Z|[+][0-9]{2}(:|)[0-9]{2})$",
      "type": "string",
      "nullable": true
    },
    "updatedBy": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "createdBy": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "name": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "createdTime": {
      "pattern": "^[0-9]{4}-?[0-9]{2}-?[0-9]{2}( |T)?[0-9]{2}:?[0-9]{2}:?[0-9]{2}(.[0-9]{1,6})?(Z|[+][0-9]{2}(:|)[0-9]{2})$",
      "type": "string",
      "nullable": true
    },
    "avatar": {
      "maxLength": 131072,
      "type": "string",
      "nullable": true
    },
    "userId": {
      "pattern": "^las:user:[a-f0-9]{32}$",
      "type": "string"
    },
    "email": {
      "pattern": "^[A-Za-z0-9][-+._A-Za-z0-9]*@([-_.A-Za-z0-9]+\\.)+[A-Za-z]{2,}$",
      "type": "string"
    }
  },
  "additionalProperties": false
}
```


#### PATCH /users/{userId}


| Path name | Path value |
| --- | --- |
| userId | Id of user on the form las:user:&lt;hex&gt; |


| Header name | Header value |
| --- | --- |
| Content-Type | application/json |
| Authorization | Bearer &lt;your access token here&gt; |
| x-api-key | &lt;your api key here&gt; |





##### Request body JSON Schema
```json
{
  "title": "PATCH /users/{userId}",
  "minProperties": 1,
  "type": "object",
  "properties": {
    "name": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "avatar": {
      "maxLength": 131072,
      "type": "string",
      "nullable": true
    }
  },
  "additionalProperties": false
}
```


##### Response body JSON Schema
```json
{
  "title": "user",
  "required": [
    "createdBy",
    "createdTime",
    "email",
    "updatedBy",
    "updatedTime",
    "userId"
  ],
  "type": "object",
  "properties": {
    "updatedTime": {
      "pattern": "^[0-9]{4}-?[0-9]{2}-?[0-9]{2}( |T)?[0-9]{2}:?[0-9]{2}:?[0-9]{2}(.[0-9]{1,6})?(Z|[+][0-9]{2}(:|)[0-9]{2})$",
      "type": "string",
      "nullable": true
    },
    "updatedBy": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "createdBy": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "name": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "createdTime": {
      "pattern": "^[0-9]{4}-?[0-9]{2}-?[0-9]{2}( |T)?[0-9]{2}:?[0-9]{2}:?[0-9]{2}(.[0-9]{1,6})?(Z|[+][0-9]{2}(:|)[0-9]{2})$",
      "type": "string",
      "nullable": true
    },
    "avatar": {
      "maxLength": 131072,
      "type": "string",
      "nullable": true
    },
    "userId": {
      "pattern": "^las:user:[a-f0-9]{32}$",
      "type": "string"
    },
    "email": {
      "pattern": "^[A-Za-z0-9][-+._A-Za-z0-9]*@([-_.A-Za-z0-9]+\\.)+[A-Za-z]{2,}$",
      "type": "string"
    }
  },
  "additionalProperties": false
}
```


#### GET /workflows





| Header name | Header value |
| --- | --- |
| Authorization | Bearer &lt;your access token here&gt; |
| x-api-key | &lt;your api key here&gt; |


| Query name | Query value |
| --- | --- |
| nextToken | String value as returned by a previous list operation |
| maxResults | Integer representing maximum number of resources to list |





##### Response body JSON Schema
```json
{
  "title": "workflows",
  "required": [
    "nextToken",
    "workflows"
  ],
  "type": "object",
  "properties": {
    "nextToken": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "workflows": {
      "type": "array",
      "items": {
        "required": [
          "completedConfig",
          "createdBy",
          "createdTime",
          "description",
          "errorConfig",
          "name",
          "numberOfRunningExecutions",
          "updatedBy",
          "updatedTime",
          "workflowId"
        ],
        "type": "object",
        "properties": {
          "updatedTime": {
            "pattern": "^[0-9]{4}-?[0-9]{2}-?[0-9]{2}( |T)?[0-9]{2}:?[0-9]{2}:?[0-9]{2}(.[0-9]{1,6})?(Z|[+][0-9]{2}(:|)[0-9]{2})$",
            "type": "string",
            "nullable": true
          },
          "updatedBy": {
            "maxLength": 4096,
            "type": "string",
            "nullable": true
          },
          "numberOfRunningExecutions": {
            "type": "integer"
          },
          "createdBy": {
            "maxLength": 4096,
            "type": "string",
            "nullable": true
          },
          "completedConfig": {
            "required": [
              "imageUrl"
            ],
            "type": "object",
            "properties": {
              "environmentSecrets": {
                "type": "array",
                "items": {
                  "pattern": "^las:secret:[a-f0-9]{32}$",
                  "type": "string"
                }
              },
              "environment": {
                "type": "object",
                "additionalProperties": {
                  "type": "string"
                }
              },
              "imageUrl": {
                "type": "string"
              },
              "secretId": {
                "pattern": "^las:secret:[a-f0-9]{32}$",
                "type": "string"
              }
            },
            "additionalProperties": false
          },
          "name": {
            "maxLength": 4096,
            "type": "string",
            "nullable": true
          },
          "description": {
            "maxLength": 4096,
            "type": "string",
            "nullable": true
          },
          "createdTime": {
            "pattern": "^[0-9]{4}-?[0-9]{2}-?[0-9]{2}( |T)?[0-9]{2}:?[0-9]{2}:?[0-9]{2}(.[0-9]{1,6})?(Z|[+][0-9]{2}(:|)[0-9]{2})$",
            "type": "string",
            "nullable": true
          },
          "workflowId": {
            "pattern": "^las:workflow:[a-f0-9]{32}$",
            "type": "string"
          },
          "errorConfig": {
            "type": "object",
            "properties": {
              "manualRetry": {
                "type": "boolean"
              },
              "email": {
                "pattern": "^[A-Za-z0-9][-+._A-Za-z0-9]*@([-_.A-Za-z0-9]+\\.)+[A-Za-z]{2,}$",
                "type": "string"
              }
            },
            "additionalProperties": false
          }
        },
        "additionalProperties": false
      }
    }
  },
  "additionalProperties": false
}
```


#### POST /workflows





| Header name | Header value |
| --- | --- |
| Content-Type | application/json |
| Authorization | Bearer &lt;your access token here&gt; |
| x-api-key | &lt;your api key here&gt; |





##### Request body JSON Schema
```json
{
  "title": "POST /workflows",
  "required": [
    "specification"
  ],
  "type": "object",
  "properties": {
    "completedConfig": {
      "required": [
        "imageUrl"
      ],
      "type": "object",
      "properties": {
        "environmentSecrets": {
          "type": "array",
          "items": {
            "pattern": "^las:secret:[a-f0-9]{32}$",
            "type": "string"
          }
        },
        "environment": {
          "type": "object",
          "additionalProperties": {
            "type": "string"
          }
        },
        "imageUrl": {
          "type": "string"
        },
        "secretId": {
          "pattern": "^las:secret:[a-f0-9]{32}$",
          "type": "string"
        }
      },
      "additionalProperties": false
    },
    "name": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "description": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "specification": {
      "required": [
        "definition"
      ],
      "type": "object",
      "properties": {
        "language": {
          "type": "string",
          "enum": [
            "ASL"
          ]
        },
        "definition": {
          "type": "object"
        },
        "version": {
          "type": "string",
          "enum": [
            "1.0.0"
          ]
        }
      },
      "additionalProperties": false
    },
    "errorConfig": {
      "type": "object",
      "properties": {
        "manualRetry": {
          "type": "boolean"
        },
        "email": {
          "pattern": "^[A-Za-z0-9][-+._A-Za-z0-9]*@([-_.A-Za-z0-9]+\\.)+[A-Za-z]{2,}$",
          "type": "string"
        }
      },
      "additionalProperties": false
    }
  },
  "additionalProperties": false
}
```


##### Response body JSON Schema
```json
{
  "title": "workflow",
  "required": [
    "completedConfig",
    "createdBy",
    "createdTime",
    "description",
    "errorConfig",
    "name",
    "numberOfRunningExecutions",
    "updatedBy",
    "updatedTime",
    "workflowId"
  ],
  "type": "object",
  "properties": {
    "updatedTime": {
      "pattern": "^[0-9]{4}-?[0-9]{2}-?[0-9]{2}( |T)?[0-9]{2}:?[0-9]{2}:?[0-9]{2}(.[0-9]{1,6})?(Z|[+][0-9]{2}(:|)[0-9]{2})$",
      "type": "string",
      "nullable": true
    },
    "updatedBy": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "numberOfRunningExecutions": {
      "type": "integer"
    },
    "createdBy": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "completedConfig": {
      "required": [
        "imageUrl"
      ],
      "type": "object",
      "properties": {
        "environmentSecrets": {
          "type": "array",
          "items": {
            "pattern": "^las:secret:[a-f0-9]{32}$",
            "type": "string"
          }
        },
        "environment": {
          "type": "object",
          "additionalProperties": {
            "type": "string"
          }
        },
        "imageUrl": {
          "type": "string"
        },
        "secretId": {
          "pattern": "^las:secret:[a-f0-9]{32}$",
          "type": "string"
        }
      },
      "additionalProperties": false
    },
    "name": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "description": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "createdTime": {
      "pattern": "^[0-9]{4}-?[0-9]{2}-?[0-9]{2}( |T)?[0-9]{2}:?[0-9]{2}:?[0-9]{2}(.[0-9]{1,6})?(Z|[+][0-9]{2}(:|)[0-9]{2})$",
      "type": "string",
      "nullable": true
    },
    "workflowId": {
      "pattern": "^las:workflow:[a-f0-9]{32}$",
      "type": "string"
    },
    "errorConfig": {
      "type": "object",
      "properties": {
        "manualRetry": {
          "type": "boolean"
        },
        "email": {
          "pattern": "^[A-Za-z0-9][-+._A-Za-z0-9]*@([-_.A-Za-z0-9]+\\.)+[A-Za-z]{2,}$",
          "type": "string"
        }
      },
      "additionalProperties": false
    }
  },
  "additionalProperties": false
}
```


#### DELETE /workflows/{workflowId}


| Path name | Path value |
| --- | --- |
| workflowId | Id of workflow on the form las:workflow:&lt;hex&gt; |


| Header name | Header value |
| --- | --- |
| Authorization | Bearer &lt;your access token here&gt; |
| x-api-key | &lt;your api key here&gt; |








##### Response body JSON Schema
```json
{
  "title": "workflow",
  "required": [
    "completedConfig",
    "createdBy",
    "createdTime",
    "description",
    "errorConfig",
    "name",
    "numberOfRunningExecutions",
    "updatedBy",
    "updatedTime",
    "workflowId"
  ],
  "type": "object",
  "properties": {
    "updatedTime": {
      "pattern": "^[0-9]{4}-?[0-9]{2}-?[0-9]{2}( |T)?[0-9]{2}:?[0-9]{2}:?[0-9]{2}(.[0-9]{1,6})?(Z|[+][0-9]{2}(:|)[0-9]{2})$",
      "type": "string",
      "nullable": true
    },
    "updatedBy": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "numberOfRunningExecutions": {
      "type": "integer"
    },
    "createdBy": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "completedConfig": {
      "required": [
        "imageUrl"
      ],
      "type": "object",
      "properties": {
        "environmentSecrets": {
          "type": "array",
          "items": {
            "pattern": "^las:secret:[a-f0-9]{32}$",
            "type": "string"
          }
        },
        "environment": {
          "type": "object",
          "additionalProperties": {
            "type": "string"
          }
        },
        "imageUrl": {
          "type": "string"
        },
        "secretId": {
          "pattern": "^las:secret:[a-f0-9]{32}$",
          "type": "string"
        }
      },
      "additionalProperties": false
    },
    "name": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "description": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "createdTime": {
      "pattern": "^[0-9]{4}-?[0-9]{2}-?[0-9]{2}( |T)?[0-9]{2}:?[0-9]{2}:?[0-9]{2}(.[0-9]{1,6})?(Z|[+][0-9]{2}(:|)[0-9]{2})$",
      "type": "string",
      "nullable": true
    },
    "workflowId": {
      "pattern": "^las:workflow:[a-f0-9]{32}$",
      "type": "string"
    },
    "errorConfig": {
      "type": "object",
      "properties": {
        "manualRetry": {
          "type": "boolean"
        },
        "email": {
          "pattern": "^[A-Za-z0-9][-+._A-Za-z0-9]*@([-_.A-Za-z0-9]+\\.)+[A-Za-z]{2,}$",
          "type": "string"
        }
      },
      "additionalProperties": false
    }
  },
  "additionalProperties": false
}
```


#### GET /workflows/{workflowId}


| Path name | Path value |
| --- | --- |
| workflowId | Id of workflow on the form las:workflow:&lt;hex&gt; |


| Header name | Header value |
| --- | --- |
| Authorization | Bearer &lt;your access token here&gt; |
| x-api-key | &lt;your api key here&gt; |








##### Response body JSON Schema
```json
{
  "title": "workflow",
  "required": [
    "completedConfig",
    "createdBy",
    "createdTime",
    "description",
    "errorConfig",
    "name",
    "numberOfRunningExecutions",
    "updatedBy",
    "updatedTime",
    "workflowId"
  ],
  "type": "object",
  "properties": {
    "updatedTime": {
      "pattern": "^[0-9]{4}-?[0-9]{2}-?[0-9]{2}( |T)?[0-9]{2}:?[0-9]{2}:?[0-9]{2}(.[0-9]{1,6})?(Z|[+][0-9]{2}(:|)[0-9]{2})$",
      "type": "string",
      "nullable": true
    },
    "updatedBy": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "numberOfRunningExecutions": {
      "type": "integer"
    },
    "createdBy": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "completedConfig": {
      "required": [
        "imageUrl"
      ],
      "type": "object",
      "properties": {
        "environmentSecrets": {
          "type": "array",
          "items": {
            "pattern": "^las:secret:[a-f0-9]{32}$",
            "type": "string"
          }
        },
        "environment": {
          "type": "object",
          "additionalProperties": {
            "type": "string"
          }
        },
        "imageUrl": {
          "type": "string"
        },
        "secretId": {
          "pattern": "^las:secret:[a-f0-9]{32}$",
          "type": "string"
        }
      },
      "additionalProperties": false
    },
    "name": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "description": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "createdTime": {
      "pattern": "^[0-9]{4}-?[0-9]{2}-?[0-9]{2}( |T)?[0-9]{2}:?[0-9]{2}:?[0-9]{2}(.[0-9]{1,6})?(Z|[+][0-9]{2}(:|)[0-9]{2})$",
      "type": "string",
      "nullable": true
    },
    "workflowId": {
      "pattern": "^las:workflow:[a-f0-9]{32}$",
      "type": "string"
    },
    "errorConfig": {
      "type": "object",
      "properties": {
        "manualRetry": {
          "type": "boolean"
        },
        "email": {
          "pattern": "^[A-Za-z0-9][-+._A-Za-z0-9]*@([-_.A-Za-z0-9]+\\.)+[A-Za-z]{2,}$",
          "type": "string"
        }
      },
      "additionalProperties": false
    }
  },
  "additionalProperties": false
}
```


#### PATCH /workflows/{workflowId}


| Path name | Path value |
| --- | --- |
| workflowId | Id of workflow on the form las:workflow:&lt;hex&gt; |


| Header name | Header value |
| --- | --- |
| Content-Type | application/json |
| Authorization | Bearer &lt;your access token here&gt; |
| x-api-key | &lt;your api key here&gt; |





##### Request body JSON Schema
```json
{
  "title": "PATCH /workflows/{workflowId}",
  "minProperties": 1,
  "type": "object",
  "properties": {
    "completedConfig": {
      "required": [
        "imageUrl"
      ],
      "type": "object",
      "properties": {
        "environmentSecrets": {
          "type": "array",
          "items": {
            "pattern": "^las:secret:[a-f0-9]{32}$",
            "type": "string"
          }
        },
        "environment": {
          "type": "object",
          "additionalProperties": {
            "type": "string"
          }
        },
        "imageUrl": {
          "type": "string"
        },
        "secretId": {
          "pattern": "^las:secret:[a-f0-9]{32}$",
          "type": "string"
        }
      },
      "additionalProperties": false
    },
    "name": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "description": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "errorConfig": {
      "type": "object",
      "properties": {
        "manualRetry": {
          "type": "boolean"
        },
        "email": {
          "pattern": "^[A-Za-z0-9][-+._A-Za-z0-9]*@([-_.A-Za-z0-9]+\\.)+[A-Za-z]{2,}$",
          "type": "string"
        }
      },
      "additionalProperties": false
    }
  },
  "additionalProperties": false
}
```


##### Response body JSON Schema
```json
{
  "title": "workflow",
  "required": [
    "completedConfig",
    "createdBy",
    "createdTime",
    "description",
    "errorConfig",
    "name",
    "numberOfRunningExecutions",
    "updatedBy",
    "updatedTime",
    "workflowId"
  ],
  "type": "object",
  "properties": {
    "updatedTime": {
      "pattern": "^[0-9]{4}-?[0-9]{2}-?[0-9]{2}( |T)?[0-9]{2}:?[0-9]{2}:?[0-9]{2}(.[0-9]{1,6})?(Z|[+][0-9]{2}(:|)[0-9]{2})$",
      "type": "string",
      "nullable": true
    },
    "updatedBy": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "numberOfRunningExecutions": {
      "type": "integer"
    },
    "createdBy": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "completedConfig": {
      "required": [
        "imageUrl"
      ],
      "type": "object",
      "properties": {
        "environmentSecrets": {
          "type": "array",
          "items": {
            "pattern": "^las:secret:[a-f0-9]{32}$",
            "type": "string"
          }
        },
        "environment": {
          "type": "object",
          "additionalProperties": {
            "type": "string"
          }
        },
        "imageUrl": {
          "type": "string"
        },
        "secretId": {
          "pattern": "^las:secret:[a-f0-9]{32}$",
          "type": "string"
        }
      },
      "additionalProperties": false
    },
    "name": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "description": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "createdTime": {
      "pattern": "^[0-9]{4}-?[0-9]{2}-?[0-9]{2}( |T)?[0-9]{2}:?[0-9]{2}:?[0-9]{2}(.[0-9]{1,6})?(Z|[+][0-9]{2}(:|)[0-9]{2})$",
      "type": "string",
      "nullable": true
    },
    "workflowId": {
      "pattern": "^las:workflow:[a-f0-9]{32}$",
      "type": "string"
    },
    "errorConfig": {
      "type": "object",
      "properties": {
        "manualRetry": {
          "type": "boolean"
        },
        "email": {
          "pattern": "^[A-Za-z0-9][-+._A-Za-z0-9]*@([-_.A-Za-z0-9]+\\.)+[A-Za-z]{2,}$",
          "type": "string"
        }
      },
      "additionalProperties": false
    }
  },
  "additionalProperties": false
}
```


#### GET /workflows/{workflowId}/executions


| Path name | Path value |
| --- | --- |
| workflowId | Id of workflow on the form las:workflow:&lt;hex&gt; |


| Header name | Header value |
| --- | --- |
| Authorization | Bearer &lt;your access token here&gt; |
| x-api-key | &lt;your api key here&gt; |


| Query name | Query value |
| --- | --- |
| status | running \| succeeded \| failed \| rejected \| retry |
| nextToken | String value as returned by a previous list operation |
| maxResults | Integer representing maximum number of resources to list |
| sortBy | startTime \| endTime |
| order | ascending \| descending |





##### Response body JSON Schema
```json
{
  "title": "workflow-executions",
  "required": [
    "executions",
    "nextToken",
    "workflowId"
  ],
  "type": "object",
  "properties": {
    "executions": {
      "type": "array",
      "items": {
        "required": [
          "endTime",
          "executionId",
          "input",
          "output",
          "startTime",
          "status",
          "transitionExecutions",
          "workflowId"
        ],
        "type": "object",
        "properties": {
          "transitionExecutions": {
            "type": "object"
          },
          "output": {
            "type": "object"
          },
          "executionId": {
            "pattern": "^las:workflow-execution:[a-f0-9]{32}$",
            "type": "string"
          },
          "input": {
            "type": "object"
          },
          "logId": {
            "pattern": "^las:log:[a-f0-9]{32}$",
            "type": "string",
            "nullable": true
          },
          "startTime": {
            "pattern": "^[0-9]{4}-?[0-9]{2}-?[0-9]{2}( |T)?[0-9]{2}:?[0-9]{2}:?[0-9]{2}(.[0-9]{1,6})?(Z|[+][0-9]{2}(:|)[0-9]{2})$",
            "type": "string",
            "nullable": true
          },
          "completedTaskLogId": {
            "pattern": "^las:log:[a-f0-9]{32}$",
            "type": "string",
            "nullable": true
          },
          "endTime": {
            "pattern": "^[0-9]{4}-?[0-9]{2}-?[0-9]{2}( |T)?[0-9]{2}:?[0-9]{2}:?[0-9]{2}(.[0-9]{1,6})?(Z|[+][0-9]{2}(:|)[0-9]{2})$",
            "type": "string",
            "nullable": true
          },
          "workflowId": {
            "pattern": "^las:workflow:[a-f0-9]{32}$",
            "type": "string"
          },
          "completedBy": {
            "type": "array",
            "items": {
              "anyOf": [
                {
                  "pattern": "^las:user:[a-f0-9]{32}$",
                  "type": "string"
                },
                {
                  "pattern": "^las:app-client:[a-f0-9]{32}$",
                  "type": "string"
                }
              ]
            }
          },
          "events": {
            "type": "array",
            "items": {
              "type": "object"
            }
          },
          "status": {
            "type": "string",
            "enum": [
              "running",
              "succeeded",
              "failed",
              "rejected",
              "retry",
              "error"
            ]
          }
        },
        "additionalProperties": false
      }
    },
    "nextToken": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "sortBy": {
      "type": "string",
      "enum": [
        "startTime",
        "endTime"
      ]
    },
    "workflowId": {
      "pattern": "^las:workflow:[a-f0-9]{32}$",
      "type": "string"
    },
    "status": {
      "type": "array",
      "items": {
        "type": "string",
        "enum": [
          "running",
          "succeeded",
          "failed",
          "rejected",
          "retry",
          "error"
        ]
      }
    },
    "order": {
      "type": "string",
      "enum": [
        "ascending",
        "descending"
      ]
    }
  },
  "additionalProperties": false
}
```


#### POST /workflows/{workflowId}/executions


| Path name | Path value |
| --- | --- |
| workflowId | Id of workflow on the form las:workflow:&lt;hex&gt; |


| Header name | Header value |
| --- | --- |
| Content-Type | application/json |
| Authorization | Bearer &lt;your access token here&gt; |
| x-api-key | &lt;your api key here&gt; |





##### Request body JSON Schema
```json
{
  "title": "POST /workflows/{workflowId}/executions",
  "required": [
    "input"
  ],
  "type": "object",
  "properties": {
    "input": {
      "type": "object"
    }
  },
  "additionalProperties": false
}
```


##### Response body JSON Schema
```json
{
  "title": "workflow-execution",
  "required": [
    "endTime",
    "executionId",
    "input",
    "output",
    "startTime",
    "status",
    "transitionExecutions",
    "workflowId"
  ],
  "type": "object",
  "properties": {
    "transitionExecutions": {
      "type": "object"
    },
    "output": {
      "type": "object"
    },
    "executionId": {
      "pattern": "^las:workflow-execution:[a-f0-9]{32}$",
      "type": "string"
    },
    "input": {
      "type": "object"
    },
    "logId": {
      "pattern": "^las:log:[a-f0-9]{32}$",
      "type": "string",
      "nullable": true
    },
    "startTime": {
      "pattern": "^[0-9]{4}-?[0-9]{2}-?[0-9]{2}( |T)?[0-9]{2}:?[0-9]{2}:?[0-9]{2}(.[0-9]{1,6})?(Z|[+][0-9]{2}(:|)[0-9]{2})$",
      "type": "string",
      "nullable": true
    },
    "completedTaskLogId": {
      "pattern": "^las:log:[a-f0-9]{32}$",
      "type": "string",
      "nullable": true
    },
    "endTime": {
      "pattern": "^[0-9]{4}-?[0-9]{2}-?[0-9]{2}( |T)?[0-9]{2}:?[0-9]{2}:?[0-9]{2}(.[0-9]{1,6})?(Z|[+][0-9]{2}(:|)[0-9]{2})$",
      "type": "string",
      "nullable": true
    },
    "workflowId": {
      "pattern": "^las:workflow:[a-f0-9]{32}$",
      "type": "string"
    },
    "completedBy": {
      "type": "array",
      "items": {
        "anyOf": [
          {
            "pattern": "^las:user:[a-f0-9]{32}$",
            "type": "string"
          },
          {
            "pattern": "^las:app-client:[a-f0-9]{32}$",
            "type": "string"
          }
        ]
      }
    },
    "events": {
      "type": "array",
      "items": {
        "type": "object"
      }
    },
    "status": {
      "type": "string",
      "enum": [
        "running",
        "succeeded",
        "failed",
        "rejected",
        "retry",
        "error"
      ]
    }
  },
  "additionalProperties": false
}
```


#### DELETE /workflows/{workflowId}/executions/{executionId}


| Path name | Path value |
| --- | --- |
| executionId | Id of execution on the form las:workflow-execution:&lt;hex&gt; |
| workflowId | Id of workflow on the form las:workflow:&lt;hex&gt; |


| Header name | Header value |
| --- | --- |
| Authorization | Bearer &lt;your access token here&gt; |
| x-api-key | &lt;your api key here&gt; |








##### Response body JSON Schema
```json
{
  "title": "workflow-execution",
  "required": [
    "endTime",
    "executionId",
    "input",
    "output",
    "startTime",
    "status",
    "transitionExecutions",
    "workflowId"
  ],
  "type": "object",
  "properties": {
    "transitionExecutions": {
      "type": "object"
    },
    "output": {
      "type": "object"
    },
    "executionId": {
      "pattern": "^las:workflow-execution:[a-f0-9]{32}$",
      "type": "string"
    },
    "input": {
      "type": "object"
    },
    "logId": {
      "pattern": "^las:log:[a-f0-9]{32}$",
      "type": "string",
      "nullable": true
    },
    "startTime": {
      "pattern": "^[0-9]{4}-?[0-9]{2}-?[0-9]{2}( |T)?[0-9]{2}:?[0-9]{2}:?[0-9]{2}(.[0-9]{1,6})?(Z|[+][0-9]{2}(:|)[0-9]{2})$",
      "type": "string",
      "nullable": true
    },
    "completedTaskLogId": {
      "pattern": "^las:log:[a-f0-9]{32}$",
      "type": "string",
      "nullable": true
    },
    "endTime": {
      "pattern": "^[0-9]{4}-?[0-9]{2}-?[0-9]{2}( |T)?[0-9]{2}:?[0-9]{2}:?[0-9]{2}(.[0-9]{1,6})?(Z|[+][0-9]{2}(:|)[0-9]{2})$",
      "type": "string",
      "nullable": true
    },
    "workflowId": {
      "pattern": "^las:workflow:[a-f0-9]{32}$",
      "type": "string"
    },
    "completedBy": {
      "type": "array",
      "items": {
        "anyOf": [
          {
            "pattern": "^las:user:[a-f0-9]{32}$",
            "type": "string"
          },
          {
            "pattern": "^las:app-client:[a-f0-9]{32}$",
            "type": "string"
          }
        ]
      }
    },
    "events": {
      "type": "array",
      "items": {
        "type": "object"
      }
    },
    "status": {
      "type": "string",
      "enum": [
        "running",
        "succeeded",
        "failed",
        "rejected",
        "retry",
        "error"
      ]
    }
  },
  "additionalProperties": false
}
```


#### GET /workflows/{workflowId}/executions/{executionId}


| Path name | Path value |
| --- | --- |
| executionId | Id of execution on the form las:workflow-execution:&lt;hex&gt; |
| workflowId | Id of workflow on the form las:workflow:&lt;hex&gt; |


| Header name | Header value |
| --- | --- |
| Authorization | Bearer &lt;your access token here&gt; |
| x-api-key | &lt;your api key here&gt; |








##### Response body JSON Schema
```json
{
  "title": "workflow-execution",
  "required": [
    "endTime",
    "executionId",
    "input",
    "output",
    "startTime",
    "status",
    "transitionExecutions",
    "workflowId"
  ],
  "type": "object",
  "properties": {
    "transitionExecutions": {
      "type": "object"
    },
    "output": {
      "type": "object"
    },
    "executionId": {
      "pattern": "^las:workflow-execution:[a-f0-9]{32}$",
      "type": "string"
    },
    "input": {
      "type": "object"
    },
    "logId": {
      "pattern": "^las:log:[a-f0-9]{32}$",
      "type": "string",
      "nullable": true
    },
    "startTime": {
      "pattern": "^[0-9]{4}-?[0-9]{2}-?[0-9]{2}( |T)?[0-9]{2}:?[0-9]{2}:?[0-9]{2}(.[0-9]{1,6})?(Z|[+][0-9]{2}(:|)[0-9]{2})$",
      "type": "string",
      "nullable": true
    },
    "completedTaskLogId": {
      "pattern": "^las:log:[a-f0-9]{32}$",
      "type": "string",
      "nullable": true
    },
    "endTime": {
      "pattern": "^[0-9]{4}-?[0-9]{2}-?[0-9]{2}( |T)?[0-9]{2}:?[0-9]{2}:?[0-9]{2}(.[0-9]{1,6})?(Z|[+][0-9]{2}(:|)[0-9]{2})$",
      "type": "string",
      "nullable": true
    },
    "workflowId": {
      "pattern": "^las:workflow:[a-f0-9]{32}$",
      "type": "string"
    },
    "completedBy": {
      "type": "array",
      "items": {
        "anyOf": [
          {
            "pattern": "^las:user:[a-f0-9]{32}$",
            "type": "string"
          },
          {
            "pattern": "^las:app-client:[a-f0-9]{32}$",
            "type": "string"
          }
        ]
      }
    },
    "events": {
      "type": "array",
      "items": {
        "type": "object"
      }
    },
    "status": {
      "type": "string",
      "enum": [
        "running",
        "succeeded",
        "failed",
        "rejected",
        "retry",
        "error"
      ]
    }
  },
  "additionalProperties": false
}
```


#### PATCH /workflows/{workflowId}/executions/{executionId}


| Path name | Path value |
| --- | --- |
| executionId | Id of execution on the form las:workflow-execution:&lt;hex&gt; |
| workflowId | Id of workflow on the form las:workflow:&lt;hex&gt; |


| Header name | Header value |
| --- | --- |
| Content-Type | application/json |
| Authorization | Bearer &lt;your access token here&gt; |
| x-api-key | &lt;your api key here&gt; |





##### Request body JSON Schema
```json
{
  "title": "PATCH workflows/{workflowId}/executions/{executionId}",
  "required": [
    "nextTransitionId"
  ],
  "type": "object",
  "properties": {
    "nextTransitionId": {
      "anyOf": [
        {
          "pattern": "^las:transition:[a-f0-9]{32}$",
          "type": "string"
        },
        {
          "pattern": "^las:transition:commons-[0-9A-Za-z-]+$",
          "type": "string"
        }
      ]
    }
  },
  "additionalProperties": false
}
```


##### Response body JSON Schema
```json
{
  "title": "workflow-execution",
  "required": [
    "endTime",
    "executionId",
    "input",
    "output",
    "startTime",
    "status",
    "transitionExecutions",
    "workflowId"
  ],
  "type": "object",
  "properties": {
    "transitionExecutions": {
      "type": "object"
    },
    "output": {
      "type": "object"
    },
    "executionId": {
      "pattern": "^las:workflow-execution:[a-f0-9]{32}$",
      "type": "string"
    },
    "input": {
      "type": "object"
    },
    "logId": {
      "pattern": "^las:log:[a-f0-9]{32}$",
      "type": "string",
      "nullable": true
    },
    "startTime": {
      "pattern": "^[0-9]{4}-?[0-9]{2}-?[0-9]{2}( |T)?[0-9]{2}:?[0-9]{2}:?[0-9]{2}(.[0-9]{1,6})?(Z|[+][0-9]{2}(:|)[0-9]{2})$",
      "type": "string",
      "nullable": true
    },
    "completedTaskLogId": {
      "pattern": "^las:log:[a-f0-9]{32}$",
      "type": "string",
      "nullable": true
    },
    "endTime": {
      "pattern": "^[0-9]{4}-?[0-9]{2}-?[0-9]{2}( |T)?[0-9]{2}:?[0-9]{2}:?[0-9]{2}(.[0-9]{1,6})?(Z|[+][0-9]{2}(:|)[0-9]{2})$",
      "type": "string",
      "nullable": true
    },
    "workflowId": {
      "pattern": "^las:workflow:[a-f0-9]{32}$",
      "type": "string"
    },
    "completedBy": {
      "type": "array",
      "items": {
        "anyOf": [
          {
            "pattern": "^las:user:[a-f0-9]{32}$",
            "type": "string"
          },
          {
            "pattern": "^las:app-client:[a-f0-9]{32}$",
            "type": "string"
          }
        ]
      }
    },
    "events": {
      "type": "array",
      "items": {
        "type": "object"
      }
    },
    "status": {
      "type": "string",
      "enum": [
        "running",
        "succeeded",
        "failed",
        "rejected",
        "retry",
        "error"
      ]
    }
  },
  "additionalProperties": false
}
```

