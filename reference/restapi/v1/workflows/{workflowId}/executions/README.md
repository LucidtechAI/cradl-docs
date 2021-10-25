#### GET /workflows/{workflowId}/executions


| Path name | Path value |
| --- | --- |
| workflowId | Id of workflow on the form las:workflow:&lt;hex&gt; |


| Header name | Header value |
| --- | --- |
| Authorization | Bearer &lt;your access token here&gt; |


| Query name | Query value |
| --- | --- |
| status | running \| succeeded \| failed \| rejected \| retry |
| nextToken | String value as returned by a previous list operation |
| maxResults | Integer representing maximum number of resources to list |
| sortBy | startTime \| endTime |
| order | ascending \| descending |





##### Response body JSON Schema
```json
{
  "title": "workflow-executions",
  "required": [
    "executions",
    "nextToken",
    "workflowId"
  ],
  "type": "object",
  "properties": {
    "executions": {
      "type": "array",
      "items": {
        "required": [
          "endTime",
          "executionId",
          "input",
          "output",
          "startTime",
          "status",
          "transitionExecutions",
          "workflowId"
        ],
        "type": "object",
        "properties": {
          "transitionExecutions": {
            "type": "object"
          },
          "output": {
            "type": "object"
          },
          "executionId": {
            "pattern": "^las:workflow-execution:[a-f0-9]{32}$",
            "type": "string"
          },
          "input": {
            "type": "object"
          },
          "logId": {
            "pattern": "^las:log:[a-f0-9]{32}$",
            "type": "string",
            "nullable": true
          },
          "startTime": {
            "pattern": "^[0-9]{4}-?[0-9]{2}-?[0-9]{2}( |T)?[0-9]{2}:?[0-9]{2}:?[0-9]{2}(.[0-9]{1,6})?(Z|[+][0-9]{2}(:|)[0-9]{2})$",
            "type": "string",
            "nullable": true
          },
          "completedTaskLogId": {
            "pattern": "^las:log:[a-f0-9]{32}$",
            "type": "string",
            "nullable": true
          },
          "endTime": {
            "pattern": "^[0-9]{4}-?[0-9]{2}-?[0-9]{2}( |T)?[0-9]{2}:?[0-9]{2}:?[0-9]{2}(.[0-9]{1,6})?(Z|[+][0-9]{2}(:|)[0-9]{2})$",
            "type": "string",
            "nullable": true
          },
          "workflowId": {
            "pattern": "^las:workflow:[a-f0-9]{32}$",
            "type": "string"
          },
          "completedBy": {
            "type": "array",
            "items": {
              "anyOf": [
                {
                  "pattern": "^las:user:[a-f0-9]{32}$",
                  "type": "string"
                },
                {
                  "pattern": "^las:app-client:[a-f0-9]{32}$",
                  "type": "string"
                }
              ]
            }
          },
          "events": {
            "type": "array",
            "items": {
              "type": "object"
            }
          },
          "status": {
            "type": "string",
            "enum": [
              "running",
              "succeeded",
              "failed",
              "rejected",
              "retry",
              "error"
            ]
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
    "sortBy": {
      "type": "string",
      "enum": [
        "startTime",
        "endTime"
      ]
    },
    "workflowId": {
      "pattern": "^las:workflow:[a-f0-9]{32}$",
      "type": "string"
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
          "retry",
          "error"
        ]
      }
    },
    "order": {
      "type": "string",
      "enum": [
        "ascending",
        "descending"
      ]
    }
  },
  "additionalProperties": false
}
```


#### POST /workflows/{workflowId}/executions


| Path name | Path value |
| --- | --- |
| workflowId | Id of workflow on the form las:workflow:&lt;hex&gt; |


| Header name | Header value |
| --- | --- |
| Content-Type | application/json |
| Authorization | Bearer &lt;your access token here&gt; |





##### Request body JSON Schema
```json
{
  "title": "POST /workflows/{workflowId}/executions",
  "required": [
    "input"
  ],
  "type": "object",
  "properties": {
    "input": {
      "type": "object"
    }
  },
  "additionalProperties": false
}
```


##### Response body JSON Schema
```json
{
  "title": "workflow-execution",
  "required": [
    "endTime",
    "executionId",
    "input",
    "output",
    "startTime",
    "status",
    "transitionExecutions",
    "workflowId"
  ],
  "type": "object",
  "properties": {
    "transitionExecutions": {
      "type": "object"
    },
    "output": {
      "type": "object"
    },
    "executionId": {
      "pattern": "^las:workflow-execution:[a-f0-9]{32}$",
      "type": "string"
    },
    "input": {
      "type": "object"
    },
    "logId": {
      "pattern": "^las:log:[a-f0-9]{32}$",
      "type": "string",
      "nullable": true
    },
    "startTime": {
      "pattern": "^[0-9]{4}-?[0-9]{2}-?[0-9]{2}( |T)?[0-9]{2}:?[0-9]{2}:?[0-9]{2}(.[0-9]{1,6})?(Z|[+][0-9]{2}(:|)[0-9]{2})$",
      "type": "string",
      "nullable": true
    },
    "completedTaskLogId": {
      "pattern": "^las:log:[a-f0-9]{32}$",
      "type": "string",
      "nullable": true
    },
    "endTime": {
      "pattern": "^[0-9]{4}-?[0-9]{2}-?[0-9]{2}( |T)?[0-9]{2}:?[0-9]{2}:?[0-9]{2}(.[0-9]{1,6})?(Z|[+][0-9]{2}(:|)[0-9]{2})$",
      "type": "string",
      "nullable": true
    },
    "workflowId": {
      "pattern": "^las:workflow:[a-f0-9]{32}$",
      "type": "string"
    },
    "completedBy": {
      "type": "array",
      "items": {
        "anyOf": [
          {
            "pattern": "^las:user:[a-f0-9]{32}$",
            "type": "string"
          },
          {
            "pattern": "^las:app-client:[a-f0-9]{32}$",
            "type": "string"
          }
        ]
      }
    },
    "events": {
      "type": "array",
      "items": {
        "type": "object"
      }
    },
    "status": {
      "type": "string",
      "enum": [
        "running",
        "succeeded",
        "failed",
        "rejected",
        "retry",
        "error"
      ]
    }
  },
  "additionalProperties": false
}
```

