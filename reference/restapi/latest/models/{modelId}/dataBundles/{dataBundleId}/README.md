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

