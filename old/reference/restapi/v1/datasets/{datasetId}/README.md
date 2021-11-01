#### DELETE /datasets/{datasetId}


| Path name | Path value |
| --- | --- |
| datasetId | Id of dataset on the form las:dataset:&lt;hex&gt; |


| Header name | Header value |
| --- | --- |
| Authorization | Bearer &lt;your access token here&gt; |








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

