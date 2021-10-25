#### GET /appClients





| Header name | Header value |
| --- | --- |
| Authorization | Bearer &lt;your access token here&gt; |


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

