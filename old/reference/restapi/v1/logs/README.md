#### GET /logs





| Header name | Header value |
| --- | --- |
| Authorization | Bearer &lt;your access token here&gt; |


| Query name | Query value |
| --- | --- |
| workflowId | String |
| nextToken | String value as returned by a previous list operation |
| order | ascending \| descending |
| transitionExecutionId | String |
| transitionId | String |
| maxResults | Integer representing maximum number of resources to list |
| workflowExecutionId | String |





##### Response body JSON Schema
```json
{
  "title": "logs",
  "required": [
    "logs",
    "nextToken"
  ],
  "type": "object",
  "properties": {
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
    "transitionExecutionId": {
      "pattern": "^las:transition-execution:[a-f0-9]{32}$",
      "type": "string"
    },
    "workflowExecutionId": {
      "pattern": "^las:workflow-execution:[a-f0-9]{32}$",
      "type": "string"
    },
    "logs": {
      "type": "array",
      "items": {
        "required": [
          "logId",
          "startTime",
          "transitionExecutionId",
          "transitionId",
          "workflowExecutionId",
          "workflowId"
        ],
        "type": "object",
        "properties": {
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
          "transitionExecutionId": {
            "pattern": "^las:transition-execution:[a-f0-9]{32}$",
            "type": "string",
            "nullable": true
          },
          "logId": {
            "pattern": "^las:log:[a-f0-9]{32}$",
            "type": "string"
          },
          "workflowExecutionId": {
            "pattern": "^las:workflow-execution:[a-f0-9]{32}$",
            "type": "string",
            "nullable": true
          },
          "startTime": {
            "pattern": "^[0-9]{4}-?[0-9]{2}-?[0-9]{2}( |T)?[0-9]{2}:?[0-9]{2}:?[0-9]{2}(.[0-9]{1,6})?(Z|[+][0-9]{2}(:|)[0-9]{2})$",
            "type": "string",
            "nullable": true
          },
          "workflowId": {
            "pattern": "^las:workflow:[a-f0-9]{32}$",
            "type": "string",
            "nullable": true
          },
          "events": {
            "type": "array",
            "items": {
              "type": "object"
            }
          }
        },
        "additionalProperties": false
      }
    },
    "workflowId": {
      "pattern": "^las:workflow:[a-f0-9]{32}$",
      "type": "string"
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

