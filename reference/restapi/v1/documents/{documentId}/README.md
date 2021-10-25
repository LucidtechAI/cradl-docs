#### DELETE /documents/{documentId}


| Path name | Path value |
| --- | --- |
| documentId | Id of document on the form las:document:&lt;hex&gt; |


| Header name | Header value |
| --- | --- |
| Authorization | Bearer &lt;your access token here&gt; |








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


#### GET /documents/{documentId}


| Path name | Path value |
| --- | --- |
| documentId | Id of document on the form las:document:&lt;hex&gt; |


| Header name | Header value |
| --- | --- |
| Authorization | Bearer &lt;your access token here&gt; |








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


#### PATCH /documents/{documentId}


| Path name | Path value |
| --- | --- |
| documentId | Id of document on the form las:document:&lt;hex&gt; |


| Header name | Header value |
| --- | --- |
| Content-Type | application/json |
| Authorization | Bearer &lt;your access token here&gt; |





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

