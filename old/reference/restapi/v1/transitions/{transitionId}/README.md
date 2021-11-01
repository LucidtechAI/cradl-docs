#### DELETE /transitions/{transitionId}


| Path name | Path value |
| --- | --- |
| transitionId | Id of transition on the form las:transition:&lt;hex&gt; |


| Header name | Header value |
| --- | --- |
| Authorization | Bearer &lt;your access token here&gt; |








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

