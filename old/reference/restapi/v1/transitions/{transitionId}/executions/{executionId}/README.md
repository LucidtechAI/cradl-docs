#### GET /transitions/{transitionId}/executions/{executionId}


| Path name | Path value |
| --- | --- |
| transitionId | Id of transition on the form las:transition:&lt;hex&gt; |
| executionId | Id of execution on the form las:transition-execution:&lt;hex&gt; |


| Header name | Header value |
| --- | --- |
| Authorization | Bearer &lt;your access token here&gt; |








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


#### PATCH /transitions/{transitionId}/executions/{executionId}


| Path name | Path value |
| --- | --- |
| transitionId | Id of transition on the form las:transition:&lt;hex&gt; |
| executionId | Id of execution on the form las:transition-execution:&lt;hex&gt; |


| Header name | Header value |
| --- | --- |
| Content-Type | application/json |
| Authorization | Bearer &lt;your access token here&gt; |





##### Request body JSON Schema
```json
{
  "title": "PATCH transitions/{transitionId}/executions/{executionId}",
  "type": "object",
  "properties": {
    "output": {
      "type": "object"
    },
    "startTime": {
      "pattern": "^[0-9]{4}-?[0-9]{2}-?[0-9]{2}( |T)?[0-9]{2}:?[0-9]{2}:?[0-9]{2}(.[0-9]{1,6})?(Z|[+][0-9]{2}(:|)[0-9]{2})$",
      "type": "string",
      "nullable": true
    },
    "error": {
      "required": [
        "message"
      ],
      "type": "object",
      "properties": {
        "message": {
          "type": "string"
        }
      },
      "additionalProperties": false
    },
    "status": {
      "type": "string"
    }
  },
  "additionalProperties": false,
  "anyOf": [
    {
      "type": "object",
      "properties": {
        "status": {
          "type": "string",
          "enum": [
            "succeeded"
          ]
        }
      }
    },
    {
      "type": "object",
      "properties": {
        "status": {
          "type": "string",
          "enum": [
            "failed",
            "rejected",
            "retry"
          ]
        }
      }
    }
  ]
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

