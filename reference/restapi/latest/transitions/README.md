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

