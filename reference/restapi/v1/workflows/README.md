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

