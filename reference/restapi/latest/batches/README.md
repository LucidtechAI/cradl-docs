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

