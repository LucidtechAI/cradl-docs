#### DELETE /documents





| Header name | Header value |
| --- | --- |
| Authorization | Bearer &lt;your access token here&gt; |
| x-api-key | &lt;your api key here&gt; |


| Query name | Query value |
| --- | --- |
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

