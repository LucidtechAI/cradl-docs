#### GET /predictions





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

