#### GET /organizations/{organizationId}


| Path name | Path value |
| --- | --- |
| organizationId | Id of organization on the form las:organization:&lt;hex&gt; |


| Header name | Header value |
| --- | --- |
| Authorization | Bearer &lt;your access token here&gt; |








##### Response body JSON Schema
```json
{
  "title": "organization",
  "required": [
    "description",
    "monthlyNumberOfDataBundlesAllowed",
    "monthlyNumberOfDataBundlesCreated",
    "monthlyNumberOfDocumentsAllowed",
    "monthlyNumberOfDocumentsCreated",
    "monthlyNumberOfPredictionsAllowed",
    "monthlyNumberOfPredictionsCreated",
    "monthlyNumberOfTransitionExecutionsAllowed",
    "monthlyNumberOfTransitionExecutionsCreated",
    "monthlyNumberOfWorkflowExecutionsAllowed",
    "monthlyNumberOfWorkflowExecutionsCreated",
    "monthlyUsageSummary",
    "name",
    "numberOfAppClientsAllowed",
    "numberOfAppClientsCreated",
    "numberOfAssetsAllowed",
    "numberOfAssetsCreated",
    "numberOfModelsAllowed",
    "numberOfModelsCreated",
    "numberOfSecretsAllowed",
    "numberOfSecretsCreated",
    "numberOfTransitionsAllowed",
    "numberOfTransitionsCreated",
    "numberOfUsersAllowed",
    "numberOfUsersCreated",
    "numberOfWorkflowsAllowed",
    "numberOfWorkflowsCreated",
    "organizationId",
    "updatedBy",
    "updatedTime"
  ],
  "type": "object",
  "properties": {
    "numberOfWorkflowsCreated": {
      "minimum": 0,
      "type": "integer"
    },
    "monthlyNumberOfWorkflowExecutionsCreated": {
      "minimum": 0,
      "type": "integer"
    },
    "description": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "numberOfUsersAllowed": {
      "minimum": 0,
      "type": "integer"
    },
    "monthlyNumberOfPredictionsAllowed": {
      "minimum": 0,
      "type": "integer"
    },
    "numberOfDatasetsAllowed": {
      "minimum": 0,
      "type": "integer"
    },
    "monthlyNumberOfDataBundlesAllowed": {
      "minimum": 0,
      "type": "integer"
    },
    "organizationId": {
      "pattern": "^las:organization:[a-f0-9]{32}$",
      "type": "string"
    },
    "numberOfModelsCreated": {
      "minimum": 0,
      "type": "integer"
    },
    "numberOfTransitionsCreated": {
      "minimum": 0,
      "type": "integer"
    },
    "monthlyNumberOfTransitionExecutionsAllowed": {
      "minimum": 0,
      "type": "integer"
    },
    "monthlyNumberOfDocumentsAllowed": {
      "minimum": 0,
      "type": "integer"
    },
    "numberOfSecretsAllowed": {
      "minimum": 0,
      "type": "integer"
    },
    "monthlyUsageSummary": {
      "type": "object"
    },
    "numberOfAppClientsCreated": {
      "minimum": 0,
      "type": "integer"
    },
    "numberOfAssetsCreated": {
      "minimum": 0,
      "type": "integer"
    },
    "updatedTime": {
      "pattern": "^[0-9]{4}-?[0-9]{2}-?[0-9]{2}( |T)?[0-9]{2}:?[0-9]{2}:?[0-9]{2}(.[0-9]{1,6})?(Z|[+][0-9]{2}(:|)[0-9]{2})$",
      "type": "string",
      "nullable": true
    },
    "numberOfWorkflowsAllowed": {
      "minimum": 0,
      "type": "integer"
    },
    "updatedBy": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "monthlyNumberOfWorkflowExecutionsAllowed": {
      "minimum": 0,
      "type": "integer"
    },
    "monthlyNumberOfDataBundlesCreated": {
      "minimum": 0,
      "type": "integer"
    },
    "numberOfUsersCreated": {
      "minimum": 0,
      "type": "integer"
    },
    "monthlyNumberOfPredictionsCreated": {
      "minimum": 0,
      "type": "integer"
    },
    "numberOfDatasetsCreated": {
      "minimum": 0,
      "type": "integer"
    },
    "numberOfTransitionsAllowed": {
      "minimum": 0,
      "type": "integer"
    },
    "monthlyNumberOfTransitionExecutionsCreated": {
      "minimum": 0,
      "type": "integer"
    },
    "numberOfModelsAllowed": {
      "minimum": 0,
      "type": "integer"
    },
    "monthlyNumberOfDocumentsCreated": {
      "minimum": 0,
      "type": "integer"
    },
    "numberOfSecretsCreated": {
      "minimum": 0,
      "type": "integer"
    },
    "name": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "numberOfAppClientsAllowed": {
      "minimum": 0,
      "type": "integer"
    },
    "numberOfAssetsAllowed": {
      "minimum": 0,
      "type": "integer"
    }
  },
  "additionalProperties": false
}
```


#### PATCH /organizations/{organizationId}


| Path name | Path value |
| --- | --- |
| organizationId | Id of organization on the form las:organization:&lt;hex&gt; |


| Header name | Header value |
| --- | --- |
| Content-Type | application/json |
| Authorization | Bearer &lt;your access token here&gt; |





##### Request body JSON Schema
```json
{
  "title": "PATCH /organizations/organizationId",
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
  "title": "organization",
  "required": [
    "description",
    "monthlyNumberOfDataBundlesAllowed",
    "monthlyNumberOfDataBundlesCreated",
    "monthlyNumberOfDocumentsAllowed",
    "monthlyNumberOfDocumentsCreated",
    "monthlyNumberOfPredictionsAllowed",
    "monthlyNumberOfPredictionsCreated",
    "monthlyNumberOfTransitionExecutionsAllowed",
    "monthlyNumberOfTransitionExecutionsCreated",
    "monthlyNumberOfWorkflowExecutionsAllowed",
    "monthlyNumberOfWorkflowExecutionsCreated",
    "monthlyUsageSummary",
    "name",
    "numberOfAppClientsAllowed",
    "numberOfAppClientsCreated",
    "numberOfAssetsAllowed",
    "numberOfAssetsCreated",
    "numberOfModelsAllowed",
    "numberOfModelsCreated",
    "numberOfSecretsAllowed",
    "numberOfSecretsCreated",
    "numberOfTransitionsAllowed",
    "numberOfTransitionsCreated",
    "numberOfUsersAllowed",
    "numberOfUsersCreated",
    "numberOfWorkflowsAllowed",
    "numberOfWorkflowsCreated",
    "organizationId",
    "updatedBy",
    "updatedTime"
  ],
  "type": "object",
  "properties": {
    "numberOfWorkflowsCreated": {
      "minimum": 0,
      "type": "integer"
    },
    "monthlyNumberOfWorkflowExecutionsCreated": {
      "minimum": 0,
      "type": "integer"
    },
    "description": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "numberOfUsersAllowed": {
      "minimum": 0,
      "type": "integer"
    },
    "monthlyNumberOfPredictionsAllowed": {
      "minimum": 0,
      "type": "integer"
    },
    "numberOfDatasetsAllowed": {
      "minimum": 0,
      "type": "integer"
    },
    "monthlyNumberOfDataBundlesAllowed": {
      "minimum": 0,
      "type": "integer"
    },
    "organizationId": {
      "pattern": "^las:organization:[a-f0-9]{32}$",
      "type": "string"
    },
    "numberOfModelsCreated": {
      "minimum": 0,
      "type": "integer"
    },
    "numberOfTransitionsCreated": {
      "minimum": 0,
      "type": "integer"
    },
    "monthlyNumberOfTransitionExecutionsAllowed": {
      "minimum": 0,
      "type": "integer"
    },
    "monthlyNumberOfDocumentsAllowed": {
      "minimum": 0,
      "type": "integer"
    },
    "numberOfSecretsAllowed": {
      "minimum": 0,
      "type": "integer"
    },
    "monthlyUsageSummary": {
      "type": "object"
    },
    "numberOfAppClientsCreated": {
      "minimum": 0,
      "type": "integer"
    },
    "numberOfAssetsCreated": {
      "minimum": 0,
      "type": "integer"
    },
    "updatedTime": {
      "pattern": "^[0-9]{4}-?[0-9]{2}-?[0-9]{2}( |T)?[0-9]{2}:?[0-9]{2}:?[0-9]{2}(.[0-9]{1,6})?(Z|[+][0-9]{2}(:|)[0-9]{2})$",
      "type": "string",
      "nullable": true
    },
    "numberOfWorkflowsAllowed": {
      "minimum": 0,
      "type": "integer"
    },
    "updatedBy": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "monthlyNumberOfWorkflowExecutionsAllowed": {
      "minimum": 0,
      "type": "integer"
    },
    "monthlyNumberOfDataBundlesCreated": {
      "minimum": 0,
      "type": "integer"
    },
    "numberOfUsersCreated": {
      "minimum": 0,
      "type": "integer"
    },
    "monthlyNumberOfPredictionsCreated": {
      "minimum": 0,
      "type": "integer"
    },
    "numberOfDatasetsCreated": {
      "minimum": 0,
      "type": "integer"
    },
    "numberOfTransitionsAllowed": {
      "minimum": 0,
      "type": "integer"
    },
    "monthlyNumberOfTransitionExecutionsCreated": {
      "minimum": 0,
      "type": "integer"
    },
    "numberOfModelsAllowed": {
      "minimum": 0,
      "type": "integer"
    },
    "monthlyNumberOfDocumentsCreated": {
      "minimum": 0,
      "type": "integer"
    },
    "numberOfSecretsCreated": {
      "minimum": 0,
      "type": "integer"
    },
    "name": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "numberOfAppClientsAllowed": {
      "minimum": 0,
      "type": "integer"
    },
    "numberOfAssetsAllowed": {
      "minimum": 0,
      "type": "integer"
    }
  },
  "additionalProperties": false
}
```

