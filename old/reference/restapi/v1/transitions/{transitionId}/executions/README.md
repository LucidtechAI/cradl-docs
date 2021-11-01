#### GET /transitions/{transitionId}/executions


| Path name | Path value |
| --- | --- |
| transitionId | Id of transition on the form las:transition:&lt;hex&gt; |


| Header name | Header value |
| --- | --- |
| Authorization | Bearer &lt;your access token here&gt; |


| Query name | Query value |
| --- | --- |
| nextToken | String value as returned by a previous list operation |
| order | ascending \| descending |
| executionId | String |
| status | running \| succeeded \| failed \| rejected \| retry |
| maxResults | Integer representing maximum number of resources to list |
| sortBy | startTime \| endTime |





##### Response body JSON Schema
```json
{
  "title": "transition-executions",
  "required": [
    "executions",
    "nextToken",
    "transitionId"
  ],
  "type": "object",
  "properties": {
    "executions": {
      "type": "array",
      "items": {
        "required": [
          "completedBy",
          "executionId",
          "input",
          "status",
          "transitionId"
        ],
        "type": "object",
        "properties": {
          "executionId": {
            "pattern": "^las:transition-execution:[a-f0-9]{32}$",
            "type": "string"
          },
          "input": {
            "type": "object"
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
          "startTime": {
            "pattern": "^[0-9]{4}-?[0-9]{2}-?[0-9]{2}( |T)?[0-9]{2}:?[0-9]{2}:?[0-9]{2}(.[0-9]{1,6})?(Z|[+][0-9]{2}(:|)[0-9]{2})$",
            "type": "string",
            "nullable": true
          },
          "logId": {
            "pattern": "^las:log:[a-f0-9]{32}$",
            "type": "string",
            "nullable": true
          },
          "endTime": {
            "pattern": "^[0-9]{4}-?[0-9]{2}-?[0-9]{2}( |T)?[0-9]{2}:?[0-9]{2}:?[0-9]{2}(.[0-9]{1,6})?(Z|[+][0-9]{2}(:|)[0-9]{2})$",
            "type": "string",
            "nullable": true
          },
          "completedBy": {
            "maxLength": 4096,
            "type": "string",
            "nullable": true
          },
          "status": {
            "type": "string",
            "enum": [
              "running",
              "succeeded",
              "failed",
              "rejected",
              "retry"
            ]
          }
        },
        "additionalProperties": false
      }
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
    "nextToken": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "status": {
      "type": "array",
      "items": {
        "type": "string",
        "enum": [
          "running",
          "succeeded",
          "failed",
          "rejected",
          "retry"
        ]
      }
    }
  },
  "additionalProperties": false
}
```


#### POST /transitions/{transitionId}/executions


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
  "title": "POST /transitions/{transitionId}/executions",
  "type": "object"
}
```


##### Response body JSON Schema
```json
{
  "title": "transition-execution",
  "required": [
    "completedBy",
    "executionId",
    "input",
    "status",
    "transitionId"
  ],
  "type": "object",
  "properties": {
    "executionId": {
      "pattern": "^las:transition-execution:[a-f0-9]{32}$",
      "type": "string"
    },
    "input": {
      "type": "object"
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
    "startTime": {
      "pattern": "^[0-9]{4}-?[0-9]{2}-?[0-9]{2}( |T)?[0-9]{2}:?[0-9]{2}:?[0-9]{2}(.[0-9]{1,6})?(Z|[+][0-9]{2}(:|)[0-9]{2})$",
      "type": "string",
      "nullable": true
    },
    "logId": {
      "pattern": "^las:log:[a-f0-9]{32}$",
      "type": "string",
      "nullable": true
    },
    "endTime": {
      "pattern": "^[0-9]{4}-?[0-9]{2}-?[0-9]{2}( |T)?[0-9]{2}:?[0-9]{2}:?[0-9]{2}(.[0-9]{1,6})?(Z|[+][0-9]{2}(:|)[0-9]{2})$",
      "type": "string",
      "nullable": true
    },
    "completedBy": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "status": {
      "type": "string",
      "enum": [
        "running",
        "succeeded",
        "failed",
        "rejected",
        "retry"
      ]
    }
  },
  "additionalProperties": false
}
```

