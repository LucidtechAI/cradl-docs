# Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`namespace `[`ai::lucidtech::las::sdk`](#namespaceai_1_1lucidtech_1_1las_1_1sdk) | 

# namespace `ai::lucidtech::las::sdk` 

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`class `[`ai::lucidtech::las::sdk::APIException`] | 
`class `[`ai::lucidtech::las::sdk::Client`] | 
`class `[`ai::lucidtech::las::sdk::CreateAppClientOptions`] | 
`class `[`ai::lucidtech::las::sdk::CreateAssetOptions`] | 
`class `[`ai::lucidtech::las::sdk::CreateBatchOptions`] | 
`class `[`ai::lucidtech::las::sdk::CreateDocumentOptions`] | 
`class `[`ai::lucidtech::las::sdk::CreateModelOptions`] | 
`class `[`ai::lucidtech::las::sdk::CreatePredictionOptions`] | 
`class `[`ai::lucidtech::las::sdk::CreateSecretOptions`] | 
`class `[`ai::lucidtech::las::sdk::CreateTransitionOptions`] | 
`class `[`ai::lucidtech::las::sdk::CreateUserOptions`] | 
`class `[`ai::lucidtech::las::sdk::CreateWorkflowOptions`] | 
`class `[`ai::lucidtech::las::sdk::Credentials`] | 
`class `[`ai::lucidtech::las::sdk::DeleteDocumentsOptions`] | 
`class `[`ai::lucidtech::las::sdk::DeleteResourcesOptions`] | 
`class `[`ai::lucidtech::las::sdk::DockerTransitionParameters`] | 
`class `[`ai::lucidtech::las::sdk::Field`] | 
`class `[`ai::lucidtech::las::sdk::FieldConfig`] | 
`class `[`ai::lucidtech::las::sdk::ListAppClientsOptions`] | 
`class `[`ai::lucidtech::las::sdk::ListAssetsOptions`] | 
`class `[`ai::lucidtech::las::sdk::ListBatchesOptions`] | 
`class `[`ai::lucidtech::las::sdk::ListDocumentsOptions`] | 
`class `[`ai::lucidtech::las::sdk::ListLogsOptions`] | 
`class `[`ai::lucidtech::las::sdk::ListModelsOptions`] | 
`class `[`ai::lucidtech::las::sdk::ListPredictionsOptions`] | 
`class `[`ai::lucidtech::las::sdk::ListResourcesOptions`] | 
`class `[`ai::lucidtech::las::sdk::ListSecretsOptions`] | 
`class `[`ai::lucidtech::las::sdk::ListSortablesOptions`] | 
`class `[`ai::lucidtech::las::sdk::ListTransitionExecutionsOptions`] | 
`class `[`ai::lucidtech::las::sdk::ListTransitionsOptions`] | 
`class `[`ai::lucidtech::las::sdk::ListUsersOptions`] | 
`class `[`ai::lucidtech::las::sdk::ListWorkflowExecutionsOptions`] | 
`class `[`ai::lucidtech::las::sdk::ListWorkflowsOptions`] | 
`class `[`ai::lucidtech::las::sdk::ManualTransitionParameters`] | 
`class `[`ai::lucidtech::las::sdk::MissingAccessTokenException`] | 
`class `[`ai::lucidtech::las::sdk::MissingCredentialsException`] | 
`class `[`ai::lucidtech::las::sdk::NameAndDescriptionOptions`] | 
`class `[`ai::lucidtech::las::sdk::NullableString`] | 
`class `[`ai::lucidtech::las::sdk::Options`] | 
`class `[`ai::lucidtech::las::sdk::PreprocessConfig`] | 
`class `[`ai::lucidtech::las::sdk::TransitionParameters`] | 
`class `[`ai::lucidtech::las::sdk::UpdateAppClientOptions`] | 
`class `[`ai::lucidtech::las::sdk::UpdateAssetOptions`] | 
`class `[`ai::lucidtech::las::sdk::UpdateBatchOptions`] | 
`class `[`ai::lucidtech::las::sdk::UpdateModelOptions`] | 
`class `[`ai::lucidtech::las::sdk::UpdateSecretOptions`] | 
`class `[`ai::lucidtech::las::sdk::UpdateTransitionExecutionOptions`] | 
`class `[`ai::lucidtech::las::sdk::UpdateTransitionOptions`] | 
`class `[`ai::lucidtech::las::sdk::UpdateUserOptions`] | 
`class `[`ai::lucidtech::las::sdk::UpdateWorkflowOptions`] | 
`class `[`ai::lucidtech::las::sdk::UserOptions`] | 
`class `[`ai::lucidtech::las::sdk::WorkflowCompletedConfig`] | 
`class `[`ai::lucidtech::las::sdk::WorkflowErrorConfig`] | 

# class `ai::lucidtech::las::sdk::APIException` 

```
class ai::lucidtech::las::sdk::APIException
  : public Exception
```  

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public  `[`APIException`]`()` | 
`public  `[`APIException`]`(String message)` | 
`public  `[`APIException`]`(int code,String message)` | 

## Members

#### `public  `[`APIException`]`()` 

#### `public  `[`APIException`]`(String message)` 

#### `public  `[`APIException`]`(int code,String message)` 

# class `ai::lucidtech::las::sdk::Client` 

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public  `[`Client`]`(`[`Credentials`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_credentials)` credentials)` | A client to invoke api methods from Lucidtech AI Services.
`public JSONObject `[`createAppClient`]`(`[`CreateAppClientOptions`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_create_app_client_options)` options)` | Create an app client, calls the POST /appClients endpoint.
`public JSONObject `[`createAppClient`]`()` | Create an app client, calls the POST /appClients endpoint.
`public JSONObject `[`updateAppClient`]`(String appClientId,`[`UpdateAppClientOptions`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_update_app_client_options)` options)` | Update an appClient, calls the PATCH /appClients/{appClientId} endpoint.
`public JSONObject `[`listAppClients`]`(`[`ListAppClientsOptions`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_list_app_clients_options)` options)` | List appClients available, calls the GET /appClients endpoint.
`public JSONObject `[`listAppClients`]`()` | List appClients available, calls the GET /appClients endpoint.
`public JSONObject `[`deleteAppClient`]`(String appClientId)` | Delete an appClient, calls the DELETE /appClients/{appClientId} endpoint.
`public JSONObject `[`createAsset`]`(byte[] content,`[`CreateAssetOptions`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_create_asset_options)` options)` | Create an asset, calls the POST /assets endpoint.
`public JSONObject `[`createAsset`]`(InputStream content,`[`CreateAssetOptions`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_create_asset_options)` options)` | Create an asset, calls the POST /assets endpoint.
`public JSONObject `[`createAsset`]`(byte[] content)` | Create an asset, calls the POST /assets endpoint.
`public JSONObject `[`createAsset`]`(InputStream content)` | Create an asset, calls the POST /assets endpoint.
`public JSONObject `[`listAssets`]`(`[`ListAssetsOptions`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_list_assets_options)` options)` | List assets available, calls the GET /assets endpoint.
`public JSONObject `[`listAssets`]`()` | List assets available, calls the GET /assets endpoint.
`public JSONObject `[`getAsset`]`(String assetId)` | Get asset, calls the GET /assets/{assetId} endpoint.
`public JSONObject `[`updateAsset`]`(String assetId,`[`UpdateAssetOptions`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_update_asset_options)` options)` | Update an asset, calls the PATCH /assets/{assetId} endpoint.
`public JSONObject `[`deleteAsset`]`(String assetId)` | Delete an asset, calls the DELETE /assets/{assetId} endpoint.
`public JSONObject `[`createBatch`]`(`[`CreateBatchOptions`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_create_batch_options)` options)` | Create a batch, calls the POST /batches endpoint.
`public JSONObject `[`createBatch`]`()` | Create a batch, calls the POST /batches endpoint.
`public JSONObject `[`updateBatch`]`(String batchId,`[`UpdateBatchOptions`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_update_batch_options)` options)` | Update a batch, calls the PATCH /batches/{batchId} endpoint.
`public JSONObject `[`listBatches`]`(`[`ListBatchesOptions`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_list_batches_options)` options)` | List batches available, calls the GET /batches endpoint.
`public JSONObject `[`listBatches`]`()` | List batches available, calls the GET /batches endpoint.
`public JSONObject `[`deleteBatch`]`(String batchId,boolean deleteDocuments)` | Delete a batch, calls the DELETE /batches/{batchId} endpoint.
`public JSONObject `[`deleteBatch`]`(String batchId)` | Delete a batch, calls the DELETE /batches/{batchId} endpoint.
`public JSONObject `[`createDocument`]`(byte[] content,`[`ContentType`](#enumai_1_1lucidtech_1_1las_1_1sdk_1_1_content_type)` contentType,`[`CreateDocumentOptions`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_create_document_options)` options)` | Create a document, calls the POST /documents endpoint.
`public JSONObject `[`createDocument`]`(InputStream content,`[`ContentType`](#enumai_1_1lucidtech_1_1las_1_1sdk_1_1_content_type)` contentType,`[`CreateDocumentOptions`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_create_document_options)` options)` | Create a document, calls the POST /documents endpoint.
`public JSONObject `[`createDocument`]`(InputStream content,`[`ContentType`](#enumai_1_1lucidtech_1_1las_1_1sdk_1_1_content_type)` contentType)` | Create a document, calls the POST /documents endpoint.
`public JSONObject `[`createDocument`]`(byte[] content,`[`ContentType`](#enumai_1_1lucidtech_1_1las_1_1sdk_1_1_content_type)` contentType)` | Create a document, calls the POST /documents endpoint.
`public JSONObject `[`listDocuments`]`(`[`ListDocumentsOptions`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_list_documents_options)` options)` | List documents, calls the GET /documents endpoint.
`public JSONObject `[`listDocuments`]`()` | List documents, calls the GET /documents endpoint.
`public JSONObject `[`deleteDocuments`]`(`[`DeleteDocumentsOptions`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_delete_documents_options)` options)` | Delete documents, calls the DELETE /documents endpoint.
`public JSONObject `[`deleteDocuments`]`()` | Delete documents, calls the DELETE /documents endpoint.
`public JSONObject `[`getDocument`]`(String documentId)` | Get document, calls the GET /documents/{documentId} endpoint.
`public JSONObject `[`updateDocument`]`(String documentId,JSONArray groundTruth)` | Update document, calls the PATCH /documents/{documentId} endpoint.
`public JSONObject `[`getLog`]`(String logId)` | Get log, calls the GET /logs/{logId} endpoint.
`public JSONObject `[`listLogs`]`(`[`ListLogsOptions`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_list_logs_options)` options)` | List logs, calls the GET /logs endpoint.
`public JSONObject `[`listLogs`]`()` | List logs, calls the GET /logs endpoint.
`public JSONObject `[`createModel`]`(int width,int height,`[`FieldConfig`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_field_config)` fieldConfig,`[`CreateModelOptions`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_create_model_options)` options)` | Create a model, calls the POST /models endpoint.
`public JSONObject `[`createModel`]`(int width,int height,`[`FieldConfig`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_field_config)` fieldConfig)` | Create a model, calls the POST /models endpoint.
`public JSONObject `[`updateModel`]`(String modelId,`[`UpdateModelOptions`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_update_model_options)` options)` | Updates a model, calls the PATCH /models/{modelId} endpoint.
`public JSONObject `[`getModel`]`(String modelId)` | Get model, calls the GET /models/{modelId} endpoint.
`public JSONObject `[`listModels`]`(`[`ListModelsOptions`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_list_models_options)` options)` | List models, calls the GET /models endpoint.
`public JSONObject `[`listModels`]`()` | List models available, calls the GET /models endpoint.
`public JSONObject `[`createPrediction`]`(String documentId,String modelId,`[`CreatePredictionOptions`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_create_prediction_options)` options)` | Create a prediction on a document using specified model, calls the POST /predictions endpoint.
`public JSONObject `[`createPrediction`]`(String documentId,String modelId)` | Create a prediction on a document using specified model, calls the POST /predictions endpoint.
`public JSONObject `[`listPredictions`]`(`[`ListPredictionsOptions`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_list_predictions_options)` options)` | List predictions available, calls the GET /predictions endpoint.
`public JSONObject `[`listPredictions`]`()` | List predictions available, calls the GET /predictions endpoint.
`public JSONObject `[`createSecret`]`(JSONObject data,`[`CreateSecretOptions`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_create_secret_options)` options)` | Create secret, calls the POST /secrets endpoint.
`public JSONObject `[`createSecret`]`(Map< String, String > data,`[`CreateSecretOptions`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_create_secret_options)` options)` | Create a secret, calls the POST /secrets endpoint.
`public JSONObject `[`createSecret`]`(Map< String, String > data)` | Create a secret, calls the POST /secrets endpoint.
`public JSONObject `[`createSecret`]`(JSONObject data)` | Create a secret, calls the POST /secrets endpoint.
`public JSONObject `[`listSecrets`]`(`[`ListSecretsOptions`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_list_secrets_options)` options)` | List secrets, calls the GET /secrets endpoint.
`public JSONObject `[`listSecrets`]`()` | List secrets, calls the GET /secrets endpoint.
`public JSONObject `[`updateSecret`]`(String secretId,`[`UpdateSecretOptions`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_update_secret_options)` options)` | Update a secret, calls the PATCH /secrets/{secretId} endpoint.
`public JSONObject `[`deleteSecret`]`(String secretId)` | Delete a secret, calls the DELETE /secrets/{secretId} endpoint.
`public JSONObject `[`createTransition`]`(`[`TransitionType`](#enumai_1_1lucidtech_1_1las_1_1sdk_1_1_transition_type)` transitionType,`[`CreateTransitionOptions`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_create_transition_options)` options)` | Create a transition, calls the POST /transitions endpoint.
`public JSONObject `[`createTransition`]`(`[`TransitionType`](#enumai_1_1lucidtech_1_1las_1_1sdk_1_1_transition_type)` transitionType)` | Create a transition, calls the POST /transitions endpoint.
`public JSONObject `[`listTransitions`]`(`[`ListTransitionsOptions`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_list_transitions_options)` options)` | List transitions, calls the GET /transitions endpoint.
`public JSONObject `[`listTransitions`]`()` | List transitions, calls the GET /transitions endpoint.
`public JSONObject `[`getTransition`]`(String transitionId)` | Get transition, calls the GET /transitions/{transitionId} endpoint.
`public JSONObject `[`updateTransition`]`(String transitionId,`[`UpdateTransitionOptions`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_update_transition_options)` options)` | Updates a transition, calls the PATCH /transitions/{transitionId} endpoint.
`public JSONObject `[`executeTransition`]`(String transitionId)` | Start executing a manual transition, calls the POST /transitions/{transitionId}/executions endpoint.
`public JSONObject `[`deleteTransition`]`(String transitionId)` | Delete a transition, calls the DELETE /transitions/{transitionId} endpoint. Will fail if transition is in use by one or more workflows.
`public JSONObject `[`listTransitionExecutions`]`(String transitionId,`[`ListTransitionExecutionsOptions`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_list_transition_executions_options)` options)` | List executions in a transition, calls the GET /transitions/{transitionId}/executions endpoint.
`public JSONObject `[`listTransitionExecutions`]`(String transitionId)` | List executions in a transition, calls the GET /transitions/{transitionId}/executions endpoint.
`public JSONObject `[`getTransitionExecution`]`(String transitionId,String executionId)` | Get an execution of a transition, calls the GET /transitions/{transitionId}/executions/{executionId} endpoint
`public JSONObject `[`updateTransitionExecution`]`(String transitionId,String executionId,`[`TransitionExecutionStatus`](#enumai_1_1lucidtech_1_1las_1_1sdk_1_1_transition_execution_status)` status,`[`UpdateTransitionExecutionOptions`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_update_transition_execution_options)` options)` | Ends the processing of the transition execution, calls the PATCH /transitions/{transitionId}/executions/{executionId} endpoint.
`public JSONObject `[`sendHeartbeat`]`(String transitionId,String executionId)` | Send heartbeat for a manual execution to signal that we are still working on it. Must be done at minimum once every 60 seconds or the transition execution will time out, calls the POST /transitions/{transitionId}/executions/{executionId}/heartbeats endpoint.
`public JSONObject `[`createUser`]`(String email,`[`CreateUserOptions`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_create_user_options)` options)` | Create a user, calls the POST /users endpoint.
`public JSONObject `[`createUser`]`(String email)` | Create a user, calls the POST /users endpoint.
`public JSONObject `[`listUsers`]`(`[`ListUsersOptions`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_list_users_options)` options)` | List users, calls the GET /users endpoint.
`public JSONObject `[`listUsers`]`()` | List users, calls the GET /users endpoint.
`public JSONObject `[`getUser`]`(String userId)` | Get user, calls the GET /users/{userId} endpoint.
`public JSONObject `[`updateUser`]`(String userId,`[`UpdateUserOptions`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_update_user_options)` options)` | Updates a user, calls the PATCH /users/{userId} endpoint.
`public JSONObject `[`deleteUser`]`(String userId)` | Delete a user, calls the PATCH /users/{userId} endpoint.
`public JSONObject `[`createWorkflow`]`(JSONObject specification,`[`CreateWorkflowOptions`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_create_workflow_options)` options)` | Creates a new workflow, calls the POST /workflows endpoint. Check out Lucidtech's tutorials for more info on how to create a workflow. see [https://docs.lucidtech.ai/getting-started/tutorials/setup_predict_and_approve](https://docs.lucidtech.ai/getting-started/tutorials/setup_predict_and_approve)
`public JSONObject `[`createWorkflow`]`(JSONObject specification)` | Creates a new workflow, calls the POST /workflows endpoint. Check out Lucidtech's tutorials for more info on how to create a workflow. see [https://docs.lucidtech.ai/getting-started/tutorials/setup_predict_and_approve](https://docs.lucidtech.ai/getting-started/tutorials/setup_predict_and_approve)
`public JSONObject `[`listWorkflows`]`(`[`ListWorkflowsOptions`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_list_workflows_options)` options)` | List workflows, calls the GET /workflows endpoint.
`public JSONObject `[`listWorkflows`]`()` | List workflows, calls the GET /workflows endpoint.
`public JSONObject `[`getWorkflow`]`(String workflowId)` | Get workflow, calls the GET /workflows/{workflowId} endpoint.
`public JSONObject `[`updateWorkflow`]`(String workflowId,`[`UpdateWorkflowOptions`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_update_workflow_options)` options)` | Update a workflow, calls the PATCH /workflows/{workflowId} endpoint.
`public JSONObject `[`deleteWorkflow`]`(String workflowId)` | Delete a workflow, calls the DELETE /workflows/{workflowId} endpoint.
`public JSONObject `[`executeWorkflow`]`(String workflowId,JSONObject content)` | Start a workflow execution, calls the POST /workflows/{workflowId}/executions endpoint.
`public JSONObject `[`listWorkflowExecutions`]`(String workflowId,`[`ListWorkflowExecutionsOptions`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_list_workflow_executions_options)` options)` | List executions in a workflow, calls the GET /workflows/{workflowId}/executions endpoint.
`public JSONObject `[`listWorkflowExecutions`]`(String workflowId)` | List executions in a workflow, calls the GET /workflows/{workflowId}/executions endpoint.
`public JSONObject `[`deleteWorkflowExecution`]`(String workflowId,String executionId)` | Delete execution from workflow, calls the DELETE /workflows/{workflowId}/executions/{executionId} endpoint.

## Members

#### `public  `[`Client`]`(`[`Credentials`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_credentials)` credentials)` 

A client to invoke api methods from Lucidtech AI Services.

#### Parameters
* `credentials` [Credentials] to use 

**See also**: [Credentials]

#### `public JSONObject `[`createAppClient`]`(`[`CreateAppClientOptions`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_create_app_client_options)` options)` 

Create an app client, calls the POST /appClients endpoint.

**See also**: [CreateAppClientOptions]

#### Parameters
* `options` Additional options to include in request body 

#### Returns
Asset response from API 

#### Exceptions
* `IOException` General IOException 

* `[APIException]` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException]` Raised if access token cannot be obtained

#### `public JSONObject `[`createAppClient`]`()` 

Create an app client, calls the POST /appClients endpoint.

#### Returns
Asset response from API 

#### Exceptions
* `IOException` General IOException 

* `[APIException]` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException]` Raised if access token cannot be obtained

#### `public JSONObject `[`updateAppClient`]`(String appClientId,`[`UpdateAppClientOptions`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_update_app_client_options)` options)` 

Update an appClient, calls the PATCH /appClients/{appClientId} endpoint.

**See also**: [UpdateAppClientOptions]

#### Parameters
* `appClientId` Id of the appClient 

* `options` Additional options to include in request body 

#### Returns
AppClient response from REST API 

#### Exceptions
* `IOException` General IOException 

* `[APIException]` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException]` Raised if access token cannot be obtained

#### `public JSONObject `[`listAppClients`]`(`[`ListAppClientsOptions`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_list_app_clients_options)` options)` 

List appClients available, calls the GET /appClients endpoint.

**See also**: [ListAppClientsOptions]

#### Parameters
* `options` Additional options to pass along as query parameters 

#### Returns
AppClients response from REST API 

#### Exceptions
* `IOException` General IOException 

* `[APIException]` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException]` Raised if access token cannot be obtained

#### `public JSONObject `[`listAppClients`]`()` 

List appClients available, calls the GET /appClients endpoint.

#### Returns
AppClients response from REST API 

#### Exceptions
* `IOException` General IOException 

* `[APIException]` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException]` Raised if access token cannot be obtained

#### `public JSONObject `[`deleteAppClient`]`(String appClientId)` 

Delete an appClient, calls the DELETE /appClients/{appClientId} endpoint.

#### Parameters
* `appClientId` Id of the appClient 

#### Returns
AppClient response from REST API 

#### Exceptions
* `IOException` General IOException 

* `[APIException]` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException]` Raised if access token cannot be obtained

#### `public JSONObject `[`createAsset`]`(byte[] content,`[`CreateAssetOptions`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_create_asset_options)` options)` 

Create an asset, calls the POST /assets endpoint.

**See also**: [CreateAssetOptions]

#### Parameters
* `content` Binary data 

* `options` Additional options to include in request body 

#### Returns
Asset response from API 

#### Exceptions
* `IOException` General IOException 

* `[APIException]` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException]` Raised if access token cannot be obtained

#### `public JSONObject `[`createAsset`]`(InputStream content,`[`CreateAssetOptions`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_create_asset_options)` options)` 

Create an asset, calls the POST /assets endpoint.

**See also**: [CreateAssetOptions]

#### Parameters
* `content` Data from input stream 

* `options` Additional options to include in request body 

#### Returns
Asset response from API 

#### Exceptions
* `IOException` General IOException 

* `[APIException]` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException]` Raised if access token cannot be obtained

#### `public JSONObject `[`createAsset`]`(byte[] content)` 

Create an asset, calls the POST /assets endpoint.

#### Parameters
* `content` Binary data 

#### Returns
Asset response from API 

#### Exceptions
* `IOException` General IOException 

* `[APIException]` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException]` Raised if access token cannot be obtained

#### `public JSONObject `[`createAsset`]`(InputStream content)` 

Create an asset, calls the POST /assets endpoint.

#### Parameters
* `content` Data from input stream 

#### Returns
Asset response from API 

#### Exceptions
* `IOException` General IOException 

* `[APIException]` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException]` Raised if access token cannot be obtained

#### `public JSONObject `[`listAssets`]`(`[`ListAssetsOptions`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_list_assets_options)` options)` 

List assets available, calls the GET /assets endpoint.

**See also**: [ListAssetsOptions]

#### Parameters
* `options` Additional options to pass along as query parameters 

#### Returns
Assets response from REST API 

#### Exceptions
* `IOException` General IOException 

* `[APIException]` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException]` Raised if access token cannot be obtained

#### `public JSONObject `[`listAssets`]`()` 

List assets available, calls the GET /assets endpoint.

#### Returns
Assets response from REST API 

#### Exceptions
* `IOException` General IOException 

* `[APIException]` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException]` Raised if access token cannot be obtained

#### `public JSONObject `[`getAsset`]`(String assetId)` 

Get asset, calls the GET /assets/{assetId} endpoint.

#### Parameters
* `assetId` Id of the asset 

#### Returns
Asset response from REST API 

#### Exceptions
* `IOException` General IOException 

* `[APIException]` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException]` Raised if access token cannot be obtained

#### `public JSONObject `[`updateAsset`]`(String assetId,`[`UpdateAssetOptions`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_update_asset_options)` options)` 

Update an asset, calls the PATCH /assets/{assetId} endpoint.

**See also**: [UpdateAssetOptions]

#### Parameters
* `assetId` Id of the asset 

* `options` Additional options to include in request body 

#### Returns
Asset response from REST API 

#### Exceptions
* `IOException` General IOException 

* `[APIException]` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException]` Raised if access token cannot be obtained

#### `public JSONObject `[`deleteAsset`]`(String assetId)` 

Delete an asset, calls the DELETE /assets/{assetId} endpoint.

#### Parameters
* `assetId` Id of the asset 

#### Returns
Asset response from REST API 

#### Exceptions
* `IOException` General IOException 

* `[APIException]` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException]` Raised if access token cannot be obtained

#### `public JSONObject `[`createBatch`]`(`[`CreateBatchOptions`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_create_batch_options)` options)` 

Create a batch, calls the POST /batches endpoint.

**See also**: [CreateBatchOptions]

#### Parameters
* `options` Additional options to include in request body 

#### Returns
Batch response from REST API 

#### Exceptions
* `IOException` General IOException 

* `[APIException]` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException]` Raised if access token cannot be obtained

#### `public JSONObject `[`createBatch`]`()` 

Create a batch, calls the POST /batches endpoint.

#### Returns
Batch response from REST API 

#### Exceptions
* `IOException` General IOException 

* `[APIException]` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException]` Raised if access token cannot be obtained

#### `public JSONObject `[`updateBatch`]`(String batchId,`[`UpdateBatchOptions`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_update_batch_options)` options)` 

Update a batch, calls the PATCH /batches/{batchId} endpoint.

**See also**: [UpdateBatchOptions]

#### Parameters
* `batchId` Id of the batch 

* `options` Additional options to include in request body 

#### Returns
Batch response from REST API 

#### Exceptions
* `IOException` General IOException 

* `[APIException]` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException]` Raised if access token cannot be obtained

#### `public JSONObject `[`listBatches`]`(`[`ListBatchesOptions`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_list_batches_options)` options)` 

List batches available, calls the GET /batches endpoint.

**See also**: [ListBatchesOptions]

#### Parameters
* `options` Additional options to pass along as query parameters 

#### Returns
Batches response from REST API 

#### Exceptions
* `IOException` General IOException 

* `[APIException]` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException]` Raised if access token cannot be obtained

#### `public JSONObject `[`listBatches`]`()` 

List batches available, calls the GET /batches endpoint.

#### Returns
Batches response from REST API 

#### Exceptions
* `IOException` General IOException 

* `[APIException]` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException]` Raised if access token cannot be obtained

#### `public JSONObject `[`deleteBatch`]`(String batchId,boolean deleteDocuments)` 

Delete a batch, calls the DELETE /batches/{batchId} endpoint.

#### Parameters
* `batchId` Id of the batch 

* `deleteDocuments` Set to true to delete documents in batch before deleting batch 

#### Returns
Batch response from REST API 

#### Exceptions
* `IOException` General IOException 

* `[APIException]` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException]` Raised if access token cannot be obtained

#### `public JSONObject `[`deleteBatch`]`(String batchId)` 

Delete a batch, calls the DELETE /batches/{batchId} endpoint.

#### Parameters
* `batchId` Id of the batch 

#### Returns
Batch response from REST API 

#### Exceptions
* `IOException` General IOException 

* `[APIException]` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException]` Raised if access token cannot be obtained

#### `public JSONObject `[`createDocument`]`(byte[] content,`[`ContentType`](#enumai_1_1lucidtech_1_1las_1_1sdk_1_1_content_type)` contentType,`[`CreateDocumentOptions`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_create_document_options)` options)` 

Create a document, calls the POST /documents endpoint.

**See also**: [CreateDocumentOptions]

#### Parameters
* `content` Binary data 

* `contentType` A mime type for the document 

* `options` Additional options to include in request body 

#### Returns
Document response from REST API 

#### Exceptions
* `IOException` General IOException 

* `[APIException]` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException]` Raised if access token cannot be obtained

#### `public JSONObject `[`createDocument`]`(InputStream content,`[`ContentType`](#enumai_1_1lucidtech_1_1las_1_1sdk_1_1_content_type)` contentType,`[`CreateDocumentOptions`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_create_document_options)` options)` 

Create a document, calls the POST /documents endpoint.

**See also**: [CreateDocumentOptions]

#### Parameters
* `content` Data from input stream 

* `contentType` A mime type for the document 

* `options` Additional options to include in request body 

#### Returns
Document response from REST API 

#### Exceptions
* `IOException` General IOException 

* `[APIException]` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException]` Raised if access token cannot be obtained

#### `public JSONObject `[`createDocument`]`(InputStream content,`[`ContentType`](#enumai_1_1lucidtech_1_1las_1_1sdk_1_1_content_type)` contentType)` 

Create a document, calls the POST /documents endpoint.

**See also**: [CreateDocumentOptions]

#### Parameters
* `content` Data from input stream 

* `contentType` A mime type for the document 

#### Returns
Document response from REST API 

#### Exceptions
* `IOException` General IOException 

* `[APIException]` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException]` Raised if access token cannot be obtained

#### `public JSONObject `[`createDocument`]`(byte[] content,`[`ContentType`](#enumai_1_1lucidtech_1_1las_1_1sdk_1_1_content_type)` contentType)` 

Create a document, calls the POST /documents endpoint.

**See also**: [CreateDocumentOptions]

#### Parameters
* `content` Binary data 

* `contentType` A mime type for the document 

#### Returns
Document response from REST API 

#### Exceptions
* `IOException` General IOException 

* `[APIException]` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException]` Raised if access token cannot be obtained

#### `public JSONObject `[`listDocuments`]`(`[`ListDocumentsOptions`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_list_documents_options)` options)` 

List documents, calls the GET /documents endpoint.

**See also**: [ListDocumentsOptions]

#### Parameters
* `options` Additional options to pass along as query parameters 

#### Returns
Documents response from REST API 

#### Exceptions
* `IOException` General IOException 

* `[APIException]` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException]` Raised if access token cannot be obtained

#### `public JSONObject `[`listDocuments`]`()` 

List documents, calls the GET /documents endpoint.

#### Returns
Documents response from REST API 

#### Exceptions
* `IOException` General IOException 

* `[APIException]` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException]` Raised if access token cannot be obtained

#### `public JSONObject `[`deleteDocuments`]`(`[`DeleteDocumentsOptions`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_delete_documents_options)` options)` 

Delete documents, calls the DELETE /documents endpoint.

**See also**: [DeleteDocumentsOptions]

#### Parameters
* `options` Additional options to pass along as query parameters 

#### Returns
Documents response from REST API 

#### Exceptions
* `IOException` General IOException 

* `[APIException]` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException]` Raised if access token cannot be obtained

#### `public JSONObject `[`deleteDocuments`]`()` 

Delete documents, calls the DELETE /documents endpoint.

**See also**: [Client::createDocument]

#### Returns
Documents response from REST API 

#### Exceptions
* `IOException` General IOException 

* `[APIException]` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException]` Raised if access token cannot be obtained

#### `public JSONObject `[`getDocument`]`(String documentId)` 

Get document, calls the GET /documents/{documentId} endpoint.

#### Parameters
* `documentId` Id of the document 

#### Returns
Document response from REST API 

#### Exceptions
* `IOException` General IOException 

* `[APIException]` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException]` Raised if access token cannot be obtained

#### `public JSONObject `[`updateDocument`]`(String documentId,JSONArray groundTruth)` 

Update document, calls the PATCH /documents/{documentId} endpoint.

**See also**: [Client::createDocument]

#### Parameters
* `documentId` The document id to post groundTruth to. 

* `groundTruth` List of json objects containing label and value for the ground truth 

#### Returns
Document response from REST API 

#### Exceptions
* `IOException` General IOException 

* `[APIException]` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException]` Raised if access token cannot be obtained

#### `public JSONObject `[`getLog`]`(String logId)` 

Get log, calls the GET /logs/{logId} endpoint.

#### Parameters
* `logId` Id of the log 

#### Returns
Log response from REST API 

#### Exceptions
* `IOException` General IOException 

* `[APIException]` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException]` Raised if access token cannot be obtained

#### `public JSONObject `[`listLogs`]`(`[`ListLogsOptions`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_list_logs_options)` options)` 

List logs, calls the GET /logs endpoint.

**See also**: [ListLogsOptions]

#### Parameters
* `options` Additional options to pass along as query parameters 

#### Returns
Logs response from REST API 

#### Exceptions
* `IOException` General IOException 

* `[APIException]` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException]` Raised if access token cannot be obtained

#### `public JSONObject `[`listLogs`]`()` 

List logs, calls the GET /logs endpoint.

#### Returns
Logs response from REST API 

#### Exceptions
* `IOException` General IOException 

* `[APIException]` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException]` Raised if access token cannot be obtained

#### `public JSONObject `[`createModel`]`(int width,int height,`[`FieldConfig`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_field_config)` fieldConfig,`[`CreateModelOptions`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_create_model_options)` options)` 

Create a model, calls the POST /models endpoint.

**See also**: [CreateModelOptions]

**See also**: [FieldConfig]

#### Parameters
* `width` The number of pixels to be used for the input image width of your model 

* `height` The number of pixels to be used for the input image height of your model 

* `fieldConfig` Specification of the fields that the model is going to predict 

* `options` Additional options to include in request body 

#### Returns
Model response from API 

#### Exceptions
* `IOException` General IOException 

* `[APIException]` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException]` Raised if access token cannot be obtained

#### `public JSONObject `[`createModel`]`(int width,int height,`[`FieldConfig`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_field_config)` fieldConfig)` 

Create a model, calls the POST /models endpoint.

**See also**: [FieldConfig]

#### Parameters
* `width` The number of pixels to be used for the input image width of your model 

* `height` The number of pixels to be used for the input image height of your model 

* `fieldConfig` Specification of the fields that the model is going to predict 

#### Returns
Model response from API 

#### Exceptions
* `IOException` General IOException 

* `[APIException]` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException]` Raised if access token cannot be obtained

#### `public JSONObject `[`updateModel`]`(String modelId,`[`UpdateModelOptions`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_update_model_options)` options)` 

Updates a model, calls the PATCH /models/{modelId} endpoint.

**See also**: [UpdateModelOptions]

#### Parameters
* `modelId` Id of the model 

* `options` Additional options to include in request body 

#### Returns
Model response from REST API 

#### Exceptions
* `IOException` General IOException 

* `[APIException]` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException]` Raised if access token cannot be obtained

#### `public JSONObject `[`getModel`]`(String modelId)` 

Get model, calls the GET /models/{modelId} endpoint.

#### Parameters
* `modelId` Id of the model 

#### Returns
Model response from REST API 

#### Exceptions
* `IOException` General IOException 

* `[APIException]` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException]` Raised if access token cannot be obtained

#### `public JSONObject `[`listModels`]`(`[`ListModelsOptions`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_list_models_options)` options)` 

List models, calls the GET /models endpoint.

**See also**: [ListModelsOptions]

#### Parameters
* `options` Additional options to pass along as query parameters 

#### Returns
Models response from REST API 

#### Exceptions
* `IOException` General IOException 

* `[APIException]` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException]` Raised if access token cannot be obtained

#### `public JSONObject `[`listModels`]`()` 

List models available, calls the GET /models endpoint.

#### Returns
Models response from REST API 

#### Exceptions
* `IOException` General IOException 

* `[APIException]` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException]` Raised if access token cannot be obtained

#### `public JSONObject `[`createPrediction`]`(String documentId,String modelId,`[`CreatePredictionOptions`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_create_prediction_options)` options)` 

Create a prediction on a document using specified model, calls the POST /predictions endpoint.

**See also**: [Client::createDocument]

**See also**: [CreatePredictionOptions]

#### Parameters
* `documentId` The document id to run inference and create a prediction on. 

* `modelId` The id of the model to use for inference 

* `options` Additional options to include in request body 

#### Returns
Prediction response from REST API 

#### Exceptions
* `IOException` General IOException 

* `[APIException]` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException]` Raised if access token cannot be obtained

#### `public JSONObject `[`createPrediction`]`(String documentId,String modelId)` 

Create a prediction on a document using specified model, calls the POST /predictions endpoint.

**See also**: [Client::createDocument]

#### Parameters
* `documentId` The document id to run inference and create a prediction on. 

* `modelId` The id of the model to use for inference 

#### Returns
Prediction response from REST API 

#### Exceptions
* `IOException` General IOException 

* `[APIException]` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException]` Raised if access token cannot be obtained

#### `public JSONObject `[`listPredictions`]`(`[`ListPredictionsOptions`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_list_predictions_options)` options)` 

List predictions available, calls the GET /predictions endpoint.

**See also**: [ListPredictionsOptions]

#### Parameters
* `options` Additional options to pass along as query parameters 

#### Returns
Predictions response from REST API 

#### Exceptions
* `IOException` General IOException 

* `[APIException]` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException]` Raised if access token cannot be obtained

#### `public JSONObject `[`listPredictions`]`()` 

List predictions available, calls the GET /predictions endpoint.

#### Returns
Predictions response from REST API 

#### Exceptions
* `IOException` General IOException 

* `[APIException]` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException]` Raised if access token cannot be obtained

#### `public JSONObject `[`createSecret`]`(JSONObject data,`[`CreateSecretOptions`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_create_secret_options)` options)` 

Create secret, calls the POST /secrets endpoint.

**See also**: [CreateSecretOptions]

#### Parameters
* `data` Key-Value pairs to store secretly 

* `options` Additional options to include in request body 

#### Returns
Secret response from API 

#### Exceptions
* `IOException` General IOException 

* `[APIException]` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException]` Raised if access token cannot be obtained

#### `public JSONObject `[`createSecret`]`(Map< String, String > data,`[`CreateSecretOptions`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_create_secret_options)` options)` 

Create a secret, calls the POST /secrets endpoint.

**See also**: [CreateSecretOptions]

#### Parameters
* `data` Key-Value pairs to store secretly 

* `options` Additional options to include in request body 

#### Returns
Secret response from API 

#### Exceptions
* `IOException` General IOException 

* `[APIException]` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException]` Raised if access token cannot be obtained

#### `public JSONObject `[`createSecret`]`(Map< String, String > data)` 

Create a secret, calls the POST /secrets endpoint.

#### Parameters
* `data` Key-Value pairs to store secretly 

#### Returns
Secret response from API 

#### Exceptions
* `IOException` General IOException 

* `[APIException]` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException]` Raised if access token cannot be obtained

#### `public JSONObject `[`createSecret`]`(JSONObject data)` 

Create a secret, calls the POST /secrets endpoint.

#### Parameters
* `data` Key-Value pairs to store secretly 

#### Returns
Secret response from API 

#### Exceptions
* `IOException` General IOException 

* `[APIException]` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException]` Raised if access token cannot be obtained

#### `public JSONObject `[`listSecrets`]`(`[`ListSecretsOptions`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_list_secrets_options)` options)` 

List secrets, calls the GET /secrets endpoint.

**See also**: [ListSecretsOptions]

#### Parameters
* `options` Additional options to pass along as query parameters 

#### Returns
Secrets response from REST API 

#### Exceptions
* `IOException` General IOException 

* `[APIException]` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException]` Raised if access token cannot be obtained

#### `public JSONObject `[`listSecrets`]`()` 

List secrets, calls the GET /secrets endpoint.

#### Returns
Secrets response from REST API 

#### Exceptions
* `IOException` General IOException 

* `[APIException]` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException]` Raised if access token cannot be obtained

#### `public JSONObject `[`updateSecret`]`(String secretId,`[`UpdateSecretOptions`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_update_secret_options)` options)` 

Update a secret, calls the PATCH /secrets/{secretId} endpoint.

**See also**: [UpdateSecretOptions]

#### Parameters
* `secretId` Id of the secret 

* `options` Additional options to include in request body 

#### Returns
Secret response from REST API 

#### Exceptions
* `IOException` General IOException 

* `[APIException]` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException]` Raised if access token cannot be obtained

#### `public JSONObject `[`deleteSecret`]`(String secretId)` 

Delete a secret, calls the DELETE /secrets/{secretId} endpoint.

#### Parameters
* `secretId` Id of the secret 

#### Returns
Secret response from REST API 

#### Exceptions
* `IOException` General IOException 

* `[APIException]` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException]` Raised if access token cannot be obtained

#### `public JSONObject `[`createTransition`]`(`[`TransitionType`](#enumai_1_1lucidtech_1_1las_1_1sdk_1_1_transition_type)` transitionType,`[`CreateTransitionOptions`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_create_transition_options)` options)` 

Create a transition, calls the POST /transitions endpoint.

**See also**: [CreateTransitionOptions]

**See also**: [TransitionType](#enumai_1_1lucidtech_1_1las_1_1sdk_1_1_transition_type)

#### Parameters
* `transitionType` Type of transition 

* `options` Additional options to include in request body 

#### Returns
Transition response from API 

#### Exceptions
* `IOException` General IOException 

* `[APIException]` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException]` Raised if access token cannot be obtained

#### `public JSONObject `[`createTransition`]`(`[`TransitionType`](#enumai_1_1lucidtech_1_1las_1_1sdk_1_1_transition_type)` transitionType)` 

Create a transition, calls the POST /transitions endpoint.

**See also**: [TransitionType](#enumai_1_1lucidtech_1_1las_1_1sdk_1_1_transition_type)

#### Parameters
* `transitionType` Type of transition 

#### Returns
Transition response from API 

#### Exceptions
* `IOException` General IOException 

* `[APIException]` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException]` Raised if access token cannot be obtained

#### `public JSONObject `[`listTransitions`]`(`[`ListTransitionsOptions`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_list_transitions_options)` options)` 

List transitions, calls the GET /transitions endpoint.

**See also**: [ListTransitionsOptions]

#### Parameters
* `options` Additional options to pass along as query parameters 

#### Returns
Transitions response from REST API 

#### Exceptions
* `IOException` General IOException 

* `[APIException]` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException]` Raised if access token cannot be obtained

#### `public JSONObject `[`listTransitions`]`()` 

List transitions, calls the GET /transitions endpoint.

#### Returns
Transitions response from REST API 

#### Exceptions
* `IOException` General IOException 

* `[APIException]` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException]` Raised if access token cannot be obtained

#### `public JSONObject `[`getTransition`]`(String transitionId)` 

Get transition, calls the GET /transitions/{transitionId} endpoint.

#### Parameters
* `transitionId` Id of the transition 

#### Returns
Transition response from REST API 

#### Exceptions
* `IOException` General IOException 

* `[APIException]` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException]` Raised if access token cannot be obtained

#### `public JSONObject `[`updateTransition`]`(String transitionId,`[`UpdateTransitionOptions`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_update_transition_options)` options)` 

Updates a transition, calls the PATCH /transitions/{transitionId} endpoint.

**See also**: [UpdateTransitionOptions]

#### Parameters
* `transitionId` Id of the transition 

* `options` Additional options to include in request body 

#### Returns
Transition response from REST API 

#### Exceptions
* `IOException` General IOException 

* `[APIException]` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException]` Raised if access token cannot be obtained

#### `public JSONObject `[`executeTransition`]`(String transitionId)` 

Start executing a manual transition, calls the POST /transitions/{transitionId}/executions endpoint.

#### Parameters
* `transitionId` Id of the transition 

#### Returns
TransitionExecution response from REST API 

#### Exceptions
* `IOException` General IOException 

* `[APIException]` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException]` Raised if access token cannot be obtained

#### `public JSONObject `[`deleteTransition`]`(String transitionId)` 

Delete a transition, calls the DELETE /transitions/{transitionId} endpoint. Will fail if transition is in use by one or more workflows.

#### Parameters
* `transitionId` Id of the transition 

#### Returns
Transition response from REST API 

#### Exceptions
* `IOException` General IOException 

* `[APIException]` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException]` Raised if access token cannot be obtained

#### `public JSONObject `[`listTransitionExecutions`]`(String transitionId,`[`ListTransitionExecutionsOptions`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_list_transition_executions_options)` options)` 

List executions in a transition, calls the GET /transitions/{transitionId}/executions endpoint.

**See also**: [ListTransitionExecutionsOptions]

#### Parameters
* `transitionId` Id of the transition 

* `options` Additional options to pass along as query parameters 

#### Returns
Transition executions response from REST API 

#### Exceptions
* `IOException` General IOException 

* `[APIException]` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException]` Raised if access token cannot be obtained

#### `public JSONObject `[`listTransitionExecutions`]`(String transitionId)` 

List executions in a transition, calls the GET /transitions/{transitionId}/executions endpoint.

#### Parameters
* `transitionId` Id of the transition 

#### Returns
Transition executions response from REST API 

#### Exceptions
* `IOException` General IOException 

* `[APIException]` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException]` Raised if access token cannot be obtained

#### `public JSONObject `[`getTransitionExecution`]`(String transitionId,String executionId)` 

Get an execution of a transition, calls the GET /transitions/{transitionId}/executions/{executionId} endpoint

#### Parameters
* `transitionId` Id of the transition 

* `executionId` Id of the execution 

#### Returns
TransitionExecution response from REST API 

#### Exceptions
* `IOException` General IOException 

* `[APIException]` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException]` Raised if access token cannot be obtained

#### `public JSONObject `[`updateTransitionExecution`]`(String transitionId,String executionId,`[`TransitionExecutionStatus`](#enumai_1_1lucidtech_1_1las_1_1sdk_1_1_transition_execution_status)` status,`[`UpdateTransitionExecutionOptions`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_update_transition_execution_options)` options)` 

Ends the processing of the transition execution, calls the PATCH /transitions/{transitionId}/executions/{executionId} endpoint.

**See also**: [UpdateTransitionExecutionOptions]

**See also**: [TransitionExecutionStatus](#enumai_1_1lucidtech_1_1las_1_1sdk_1_1_transition_execution_status)

#### Parameters
* `transitionId` Id of the transition 

* `executionId` Id of the execution 

* `status` Status of the execution 

* `options` Additional options to include in request body 

#### Returns
Transition response from REST API 

#### Exceptions
* `IOException` General IOException 

* `[APIException]` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException]` Raised if access token cannot be obtained

#### `public JSONObject `[`sendHeartbeat`]`(String transitionId,String executionId)` 

Send heartbeat for a manual execution to signal that we are still working on it. Must be done at minimum once every 60 seconds or the transition execution will time out, calls the POST /transitions/{transitionId}/executions/{executionId}/heartbeats endpoint.

#### Parameters
* `transitionId` Id of the transition 

* `executionId` Id of the execution 

#### Returns
Empty response 

#### Exceptions
* `IOException` General IOException 

* `[APIException]` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException]` Raised if access token cannot be obtained

#### `public JSONObject `[`createUser`]`(String email,`[`CreateUserOptions`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_create_user_options)` options)` 

Create a user, calls the POST /users endpoint.

**See also**: [CreateUserOptions]

#### Parameters
* `email` Email of the new user 

* `options` Additional options to include in request body 

#### Returns
User response from API 

#### Exceptions
* `IOException` General IOException 

* `[APIException]` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException]` Raised if access token cannot be obtained

#### `public JSONObject `[`createUser`]`(String email)` 

Create a user, calls the POST /users endpoint.

#### Parameters
* `email` Email to the new user 

#### Returns
User response from API 

#### Exceptions
* `IOException` General IOException 

* `[APIException]` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException]` Raised if access token cannot be obtained

#### `public JSONObject `[`listUsers`]`(`[`ListUsersOptions`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_list_users_options)` options)` 

List users, calls the GET /users endpoint.

**See also**: [ListUsersOptions]

#### Parameters
* `options` Additional options to pass along as query parameters 

#### Returns
Users response from REST API 

#### Exceptions
* `IOException` General IOException 

* `[APIException]` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException]` Raised if access token cannot be obtained

#### `public JSONObject `[`listUsers`]`()` 

List users, calls the GET /users endpoint.

#### Returns
Users response from REST API 

#### Exceptions
* `IOException` General IOException 

* `[APIException]` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException]` Raised if access token cannot be obtained

#### `public JSONObject `[`getUser`]`(String userId)` 

Get user, calls the GET /users/{userId} endpoint.

#### Parameters
* `userId` Id of user 

#### Returns
User response 

#### Exceptions
* `IOException` General IOException 

* `[APIException]` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException]` Raised if access token cannot be obtained

#### `public JSONObject `[`updateUser`]`(String userId,`[`UpdateUserOptions`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_update_user_options)` options)` 

Updates a user, calls the PATCH /users/{userId} endpoint.

**See also**: [UpdateUserOptions]

#### Parameters
* `userId` Id of user 

* `options` Additional options to include in request body 

#### Returns
User response from REST API 

#### Exceptions
* `IOException` General IOException 

* `[APIException]` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException]` Raised if access token cannot be obtained

#### `public JSONObject `[`deleteUser`]`(String userId)` 

Delete a user, calls the PATCH /users/{userId} endpoint.

#### Parameters
* `userId` Id of user 

#### Returns
User response from REST API 

#### Exceptions
* `IOException` General IOException 

* `[APIException]` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException]` Raised if access token cannot be obtained

#### `public JSONObject `[`createWorkflow`]`(JSONObject specification,`[`CreateWorkflowOptions`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_create_workflow_options)` options)` 

Creates a new workflow, calls the POST /workflows endpoint. Check out Lucidtech's tutorials for more info on how to create a workflow. see [https://docs.lucidtech.ai/getting-started/tutorials/setup_predict_and_approve](https://docs.lucidtech.ai/getting-started/tutorials/setup_predict_and_approve)

**See also**: [CreateWorkflowOptions]

#### Parameters
* `specification` Specification of the workflow, currently supporting ASL: [https://states-language.net/spec.html](https://states-language.net/spec.html). Check out the tutorials for more information: see [https://docs.lucidtech.ai/getting-started/tutorials/setup_predict_and_approve#creating-the-workflow](https://docs.lucidtech.ai/getting-started/tutorials/setup_predict_and_approve#creating-the-workflow)

* `options` Additional options to include in request body 

#### Returns
Workflow response from API 

#### Exceptions
* `IOException` General IOException 

* `[APIException]` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException]` Raised if access token cannot be obtained

#### `public JSONObject `[`createWorkflow`]`(JSONObject specification)` 

Creates a new workflow, calls the POST /workflows endpoint. Check out Lucidtech's tutorials for more info on how to create a workflow. see [https://docs.lucidtech.ai/getting-started/tutorials/setup_predict_and_approve](https://docs.lucidtech.ai/getting-started/tutorials/setup_predict_and_approve)

#### Parameters
* `specification` Specification of the workflow, currently supporting ASL: [https://states-language.net/spec.html](https://states-language.net/spec.html). Check out the tutorials for more information: see [https://docs.lucidtech.ai/getting-started/tutorials/setup_predict_and_approve#creating-the-workflow](https://docs.lucidtech.ai/getting-started/tutorials/setup_predict_and_approve#creating-the-workflow)

#### Returns
Workflow response from API 

#### Exceptions
* `IOException` General IOException 

* `[APIException]` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException]` Raised if access token cannot be obtained

#### `public JSONObject `[`listWorkflows`]`(`[`ListWorkflowsOptions`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_list_workflows_options)` options)` 

List workflows, calls the GET /workflows endpoint.

**See also**: [ListWorkflowsOptions]

#### Parameters
* `options` Additional options to pass along as query parameters 

#### Returns
Workflows response from REST API 

#### Exceptions
* `IOException` General IOException 

* `[APIException]` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException]` Raised if access token cannot be obtained

#### `public JSONObject `[`listWorkflows`]`()` 

List workflows, calls the GET /workflows endpoint.

#### Returns
Workflows response from REST API 

#### Exceptions
* `IOException` General IOException 

* `[APIException]` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException]` Raised if access token cannot be obtained

#### `public JSONObject `[`getWorkflow`]`(String workflowId)` 

Get workflow, calls the GET /workflows/{workflowId} endpoint.

#### Parameters
* `workflowId` Id of the workflow 

#### Returns
Workflow response from REST API 

#### Exceptions
* `IOException` General IOException 

* `[APIException]` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException]` Raised if access token cannot be obtained

#### `public JSONObject `[`updateWorkflow`]`(String workflowId,`[`UpdateWorkflowOptions`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_update_workflow_options)` options)` 

Update a workflow, calls the PATCH /workflows/{workflowId} endpoint.

**See also**: [UpdateWorkflowOptions]

#### Parameters
* `workflowId` Id of the workflow 

* `options` Additional options to include in request body 

#### Returns
Workflow response from REST API 

#### Exceptions
* `IOException` General IOException 

* `[APIException]` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException]` Raised if access token cannot be obtained

#### `public JSONObject `[`deleteWorkflow`]`(String workflowId)` 

Delete a workflow, calls the DELETE /workflows/{workflowId} endpoint.

**See also**: [Client::createWorkflow]

#### Parameters
* `workflowId` Id of the workflow 

#### Returns
Workflow response from REST API 

#### Exceptions
* `IOException` General IOException 

* `[APIException]` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException]` Raised if access token cannot be obtained

#### `public JSONObject `[`executeWorkflow`]`(String workflowId,JSONObject content)` 

Start a workflow execution, calls the POST /workflows/{workflowId}/executions endpoint.

#### Parameters
* `workflowId` Id of the workflow 

* `content` Input to the first step of the workflow 

#### Returns
WorkflowExecution response from REST API 

#### Exceptions
* `IOException` General IOException 

* `[APIException]` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException]` Raised if access token cannot be obtained

#### `public JSONObject `[`listWorkflowExecutions`]`(String workflowId,`[`ListWorkflowExecutionsOptions`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_list_workflow_executions_options)` options)` 

List executions in a workflow, calls the GET /workflows/{workflowId}/executions endpoint.

**See also**: [ListWorkflowExecutionsOptions]

#### Parameters
* `workflowId` Id of the workflow 

* `options` Additional options to pass along as query parameters 

#### Returns
Workflow executions response from REST API 

#### Exceptions
* `IOException` General IOException 

* `[APIException]` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException]` Raised if access token cannot be obtained

#### `public JSONObject `[`listWorkflowExecutions`]`(String workflowId)` 

List executions in a workflow, calls the GET /workflows/{workflowId}/executions endpoint.

#### Parameters
* `workflowId` Id of the workflow 

#### Returns
Workflow executions response from REST API 

#### Exceptions
* `IOException` General IOException 

* `[APIException]` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException]` Raised if access token cannot be obtained

#### `public JSONObject `[`deleteWorkflowExecution`]`(String workflowId,String executionId)` 

Delete execution from workflow, calls the DELETE /workflows/{workflowId}/executions/{executionId} endpoint.

**See also**: [Client::executeWorkflow]

#### Parameters
* `workflowId` Id of the workflow 

* `executionId` Id of the execution 

#### Returns
WorkflowExecution response from REST API 

#### Exceptions
* `IOException` General IOException 

* `[APIException]` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException]` Raised if access token cannot be obtained

# class `ai::lucidtech::las::sdk::CreateAppClientOptions` 

```
class ai::lucidtech::las::sdk::CreateAppClientOptions
  : public ai.lucidtech.las.sdk.NameAndDescriptionOptions< CreateAppClientOptions >
```  

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public `[`CreateAppClientOptions`] [`setCallbackUrls`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_create_app_client_options_1a8bbf6466c0013be0d9a0e281abb5a431)`(String[] callbackUrls)` | 
`public `[`CreateAppClientOptions`] [`setLogoutUrls`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_create_app_client_options_1a688e2c5f76413c0a94bd58ded8031ad0)`(String[] logoutUrls)` | 
`public `[`CreateAppClientOptions`] [`setLoginUrls`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_create_app_client_options_1a9f60b0cec00958967603418b02b315e4)`(String[] loginUrls)` | 
`public `[`CreateAppClientOptions`] [`setDefaultLoginUrl`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_create_app_client_options_1a1257aa6a3bf68cd43fa42b86f4cbda79)`(String defaultLoginUrl)` | 
`public `[`CreateAppClientOptions`] [`setGenerateSecret`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_create_app_client_options_1ac2a6827e706591140ddbecf7b271b769)`(Boolean generateSecret)` | 
`public JSONObject `[`addOptions`]`(JSONObject body)` | 

## Members

#### `public `[`CreateAppClientOptions`] [`setCallbackUrls`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_create_app_client_options_1a8bbf6466c0013be0d9a0e281abb5a431)`(String[] callbackUrls)` 

#### `public `[`CreateAppClientOptions`] [`setLogoutUrls`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_create_app_client_options_1a688e2c5f76413c0a94bd58ded8031ad0)`(String[] logoutUrls)` 

#### `public `[`CreateAppClientOptions`] [`setLoginUrls`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_create_app_client_options_1a9f60b0cec00958967603418b02b315e4)`(String[] loginUrls)` 

#### `public `[`CreateAppClientOptions`] [`setDefaultLoginUrl`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_create_app_client_options_1a1257aa6a3bf68cd43fa42b86f4cbda79)`(String defaultLoginUrl)` 

#### `public `[`CreateAppClientOptions`] [`setGenerateSecret`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_create_app_client_options_1ac2a6827e706591140ddbecf7b271b769)`(Boolean generateSecret)` 

#### `public JSONObject `[`addOptions`]`(JSONObject body)` 

# class `ai::lucidtech::las::sdk::CreateAssetOptions` 

```
class ai::lucidtech::las::sdk::CreateAssetOptions
  : public ai.lucidtech.las.sdk.NameAndDescriptionOptions< CreateAssetOptions >
```  

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------

## Members

# class `ai::lucidtech::las::sdk::CreateBatchOptions` 

```
class ai::lucidtech::las::sdk::CreateBatchOptions
  : public ai.lucidtech.las.sdk.NameAndDescriptionOptions< CreateBatchOptions >
```  

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public `[`CreateBatchOptions`] [`setContainsPersonallyIdentifiableInformation`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_create_batch_options_1a0db395dc2d449ea24505793eb14b7945)`(Boolean containsPersonallyIdentifiableInformation)` | 
`public JSONObject `[`addOptions`]`(JSONObject body)` | 

## Members

#### `public `[`CreateBatchOptions`] [`setContainsPersonallyIdentifiableInformation`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_create_batch_options_1a0db395dc2d449ea24505793eb14b7945)`(Boolean containsPersonallyIdentifiableInformation)` 

#### `public JSONObject `[`addOptions`]`(JSONObject body)` 

# class `ai::lucidtech::las::sdk::CreateDocumentOptions` 

```
class ai::lucidtech::las::sdk::CreateDocumentOptions
  : public ai.lucidtech.las.sdk.Options
```  

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public `[`CreateDocumentOptions`] [`setConsentId`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_create_document_options_1aea843844d1cabdb367b6ef2fbad74763)`(String consentId)` | 
`public `[`CreateDocumentOptions`] [`setBatchId`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_create_document_options_1a6a4643ab2ab9ae0d195e95b6e5858abb)`(String batchId)` | 
`public `[`CreateDocumentOptions`] [`setGroundTruth`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_create_document_options_1a11e5ef2f36fa14e6e048d74d406881f5)`(JSONArray groundTruth)` | 
`public `[`CreateDocumentOptions`] [`setRetentionInDays`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_create_document_options_1aaf2f77a3677707090b71be74af54a826)`(Integer retentionInDays)` | 
`public JSONObject `[`addOptions`]`(JSONObject body)` | 

## Members

#### `public `[`CreateDocumentOptions`] [`setConsentId`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_create_document_options_1aea843844d1cabdb367b6ef2fbad74763)`(String consentId)` 

#### `public `[`CreateDocumentOptions`] [`setBatchId`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_create_document_options_1a6a4643ab2ab9ae0d195e95b6e5858abb)`(String batchId)` 

#### `public `[`CreateDocumentOptions`] [`setGroundTruth`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_create_document_options_1a11e5ef2f36fa14e6e048d74d406881f5)`(JSONArray groundTruth)` 

#### `public `[`CreateDocumentOptions`] [`setRetentionInDays`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_create_document_options_1aaf2f77a3677707090b71be74af54a826)`(Integer retentionInDays)` 

#### `public JSONObject `[`addOptions`]`(JSONObject body)` 

# class `ai::lucidtech::las::sdk::CreateModelOptions` 

```
class ai::lucidtech::las::sdk::CreateModelOptions
  : public ai.lucidtech.las.sdk.NameAndDescriptionOptions< CreateModelOptions >
```  

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public `[`CreateModelOptions`] [`setPreprocessConfig`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_create_model_options_1a66eece8a0b6ae4e500ae1d02798d6aa0)`(`[`PreprocessConfig`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_preprocess_config)` preprocessConfig)` | 
`public JSONObject `[`addOptions`]`(JSONObject body)` | 

## Members

#### `public `[`CreateModelOptions`] [`setPreprocessConfig`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_create_model_options_1a66eece8a0b6ae4e500ae1d02798d6aa0)`(`[`PreprocessConfig`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_preprocess_config)` preprocessConfig)` 

#### `public JSONObject `[`addOptions`]`(JSONObject body)` 

# class `ai::lucidtech::las::sdk::CreatePredictionOptions` 

```
class ai::lucidtech::las::sdk::CreatePredictionOptions
  : public ai.lucidtech.las.sdk.Options
```  

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public `[`CreatePredictionOptions`] [`setMaxPages`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_create_prediction_options_1af6a80e5477e27525a936bfa24404cdf0)`(int maxPages)` | 
`public `[`CreatePredictionOptions`] [`setAutoRotate`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_create_prediction_options_1a82d5ef3dd802caa5785475eeabbbf9dd)`(boolean autoRotate)` | 
`public `[`CreatePredictionOptions`] [`setImageQuality`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_create_prediction_options_1ad6b7016289238d2e664e6e968a6d59b2)`(`[`ImageQuality`](#enumai_1_1lucidtech_1_1las_1_1sdk_1_1_image_quality)` imageQuality)` | 
`public JSONObject `[`addOptions`]`(JSONObject body)` | 

## Members

#### `public `[`CreatePredictionOptions`] [`setMaxPages`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_create_prediction_options_1af6a80e5477e27525a936bfa24404cdf0)`(int maxPages)` 

#### `public `[`CreatePredictionOptions`] [`setAutoRotate`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_create_prediction_options_1a82d5ef3dd802caa5785475eeabbbf9dd)`(boolean autoRotate)` 

#### `public `[`CreatePredictionOptions`] [`setImageQuality`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_create_prediction_options_1ad6b7016289238d2e664e6e968a6d59b2)`(`[`ImageQuality`](#enumai_1_1lucidtech_1_1las_1_1sdk_1_1_image_quality)` imageQuality)` 

#### `public JSONObject `[`addOptions`]`(JSONObject body)` 

# class `ai::lucidtech::las::sdk::CreateSecretOptions` 

```
class ai::lucidtech::las::sdk::CreateSecretOptions
  : public ai.lucidtech.las.sdk.NameAndDescriptionOptions< CreateSecretOptions >
```  

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------

## Members

# class `ai::lucidtech::las::sdk::CreateTransitionOptions` 

```
class ai::lucidtech::las::sdk::CreateTransitionOptions
  : public ai.lucidtech.las.sdk.NameAndDescriptionOptions< CreateTransitionOptions >
```  

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public `[`CreateTransitionOptions`] [`setParameters`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_create_transition_options_1aa546f75e3898f4b779e860955822e77e)`(`[`TransitionParameters`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_transition_parameters)` parameters)` | 
`public `[`CreateTransitionOptions`] [`setInputJsonSchema`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_create_transition_options_1ab76486532b052a9dfdd434a6edf210c2)`(JSONObject inputJsonSchema)` | 
`public `[`CreateTransitionOptions`] [`setOutputJsonSchema`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_create_transition_options_1a1d77cbecb47c7f092befd51253ef8ed5)`(JSONObject outputJsonSchema)` | 
`public JSONObject `[`addOptions`]`(JSONObject body)` | 

## Members

#### `public `[`CreateTransitionOptions`] [`setParameters`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_create_transition_options_1aa546f75e3898f4b779e860955822e77e)`(`[`TransitionParameters`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_transition_parameters)` parameters)` 

#### `public `[`CreateTransitionOptions`] [`setInputJsonSchema`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_create_transition_options_1ab76486532b052a9dfdd434a6edf210c2)`(JSONObject inputJsonSchema)` 

#### `public `[`CreateTransitionOptions`] [`setOutputJsonSchema`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_create_transition_options_1a1d77cbecb47c7f092befd51253ef8ed5)`(JSONObject outputJsonSchema)` 

#### `public JSONObject `[`addOptions`]`(JSONObject body)` 

# class `ai::lucidtech::las::sdk::CreateUserOptions` 

```
class ai::lucidtech::las::sdk::CreateUserOptions
  : public ai.lucidtech.las.sdk.UserOptions< CreateUserOptions >
```  

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------

## Members

# class `ai::lucidtech::las::sdk::CreateWorkflowOptions` 

```
class ai::lucidtech::las::sdk::CreateWorkflowOptions
  : public ai.lucidtech.las.sdk.NameAndDescriptionOptions< CreateWorkflowOptions >
```  

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public `[`CreateWorkflowOptions`] [`setCompletedConfig`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_create_workflow_options_1adcf2b376dab782ce4b8f84e73132eb1f)`(`[`WorkflowCompletedConfig`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_workflow_completed_config)` completedConfig)` | 
`public `[`CreateWorkflowOptions`] [`setErrorConfig`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_create_workflow_options_1aa5f11590f30a23063349152742baedff)`(`[`WorkflowErrorConfig`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_workflow_error_config)` errorConfig)` | 
`public JSONObject `[`addOptions`]`(JSONObject body)` | 

## Members

#### `public `[`CreateWorkflowOptions`] [`setCompletedConfig`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_create_workflow_options_1adcf2b376dab782ce4b8f84e73132eb1f)`(`[`WorkflowCompletedConfig`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_workflow_completed_config)` completedConfig)` 

#### `public `[`CreateWorkflowOptions`] [`setErrorConfig`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_create_workflow_options_1aa5f11590f30a23063349152742baedff)`(`[`WorkflowErrorConfig`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_workflow_error_config)` errorConfig)` 

#### `public JSONObject `[`addOptions`]`(JSONObject body)` 

# class `ai::lucidtech::las::sdk::Credentials` 

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public  `[`Credentials`]`(String clientId,String clientSecret,String apiKey,String authEndpoint,String apiEndpoint)` | Used to fetch and store credentials.
`public String `[`getAccessToken`]`(HttpClient httpClient)` | #### Parameters
`public String `[`getApiKey`]`()` | 
`public String `[`getApiEndpoint`]`()` | 

## Members

#### `public  `[`Credentials`]`(String clientId,String clientSecret,String apiKey,String authEndpoint,String apiEndpoint)` 

Used to fetch and store credentials.

#### Parameters
* `clientId` [Client] id 

* `clientSecret` [Client] secret 

* `apiKey` API key 

* `authEndpoint` Auth endpoint 

* `apiEndpoint` Domain endpoint of the api, e.g. [https://{prefix}.api.lucidtech.ai/{version}](https://{prefix}.api.lucidtech.ai/{version})

#### Exceptions
* `[MissingCredentialsException]` Raised if some of credentials are missing

#### `public String `[`getAccessToken`]`(HttpClient httpClient)` 

#### Parameters
* `httpClient` Instance of HttpClient used to access the authentication endpoint 

#### Returns
Access token, downloading it if necessary 

#### Exceptions
* `[MissingAccessTokenException]` Raised if access token cannot be obtained

#### `public String `[`getApiKey`]`()` 

#### `public String `[`getApiEndpoint`]`()` 

# class `ai::lucidtech::las::sdk::DeleteDocumentsOptions` 

```
class ai::lucidtech::las::sdk::DeleteDocumentsOptions
  : public ai.lucidtech.las.sdk.DeleteResourcesOptions< DeleteDocumentsOptions >
```  

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public `[`DeleteDocumentsOptions`] [`setConsentId`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_delete_documents_options_1aaf5142e3fd86dbecf7a7993aa9321405)`(String[] consentId)` | 
`public `[`DeleteDocumentsOptions`] [`setDatasetId`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_delete_documents_options_1a39123acb8b4e7ec42e74ed508728576f)`(String[] datasetId)` | 
`public `[`DeleteDocumentsOptions`] [`setBatchId`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_delete_documents_options_1af8605c4bfd5d14e69d363f6805ca4459)`(String[] batchId)` | 
`public List< NameValuePair > `[`addOptions`]`(List< NameValuePair > parameters)` | 

## Members

#### `public `[`DeleteDocumentsOptions`] [`setConsentId`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_delete_documents_options_1aaf5142e3fd86dbecf7a7993aa9321405)`(String[] consentId)` 

#### `public `[`DeleteDocumentsOptions`] [`setDatasetId`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_delete_documents_options_1a39123acb8b4e7ec42e74ed508728576f)`(String[] datasetId)` 

#### `public `[`DeleteDocumentsOptions`] [`setBatchId`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_delete_documents_options_1af8605c4bfd5d14e69d363f6805ca4459)`(String[] batchId)` 

#### `public List< NameValuePair > `[`addOptions`]`(List< NameValuePair > parameters)` 

# class `ai::lucidtech::las::sdk::DeleteResourcesOptions` 

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public T `[`setMaxResults`]`(int maxResults)` | 
`public T `[`setNextToken`]`(String nextToken)` | 
`public List< NameValuePair > `[`addOptions`]`(List< NameValuePair > parameters)` | 
`protected Integer `[`maxResults`] | 
`protected String `[`nextToken`] | 
`protected void `[`addOption`]`(List< NameValuePair > parameters,String key,String value)` | 
`protected void `[`addOption`]`(List< NameValuePair > parameters,String key,String[] value)` | 
`protected void `[`addOption`]`(List< NameValuePair > parameters,String key,Integer value)` | 

## Members

#### `public T `[`setMaxResults`]`(int maxResults)` 

#### `public T `[`setNextToken`]`(String nextToken)` 

#### `public List< NameValuePair > `[`addOptions`]`(List< NameValuePair > parameters)` 

#### `protected Integer `[`maxResults`] 

#### `protected String `[`nextToken`] 

#### `protected void `[`addOption`]`(List< NameValuePair > parameters,String key,String value)` 

#### `protected void `[`addOption`]`(List< NameValuePair > parameters,String key,String[] value)` 

#### `protected void `[`addOption`]`(List< NameValuePair > parameters,String key,Integer value)` 

# class `ai::lucidtech::las::sdk::DockerTransitionParameters` 

```
class ai::lucidtech::las::sdk::DockerTransitionParameters
  : public ai.lucidtech.las.sdk.TransitionParameters
```  

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public `[`DockerTransitionParameters`] [`setImageUrl`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_docker_transition_parameters_1ac1a2e6105139a97ad1ee257644841af4)`(String imageUrl)` | 
`public `[`DockerTransitionParameters`] [`setSecretId`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_docker_transition_parameters_1a5177a815e7989b6e86001076464b14eb)`(String secretId)` | 
`public `[`DockerTransitionParameters`] [`setMemory`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_docker_transition_parameters_1ae6c2d6e74e8c5c4b383399c7e066dedc)`(Integer memory)` | 
`public `[`DockerTransitionParameters`] [`setCpu`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_docker_transition_parameters_1a4ba534d7a6abe5ae3e0509c5e0a2ca7d)`(Integer cpu)` | 
`public `[`DockerTransitionParameters`] [`setEnvironmentSecrets`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_docker_transition_parameters_1af8c88a8d63800aad3e7180b82b0f5c0a)`(String[] environmentSecrets)` | 
`public `[`DockerTransitionParameters`] [`setEnvironment`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_docker_transition_parameters_1a4d2b42a01536ab100771164bf094d72f)`(Map< String, String > environment)` | 
`public JSONObject `[`addOptions`]`(JSONObject body)` | 

## Members

#### `public `[`DockerTransitionParameters`] [`setImageUrl`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_docker_transition_parameters_1ac1a2e6105139a97ad1ee257644841af4)`(String imageUrl)` 

#### `public `[`DockerTransitionParameters`] [`setSecretId`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_docker_transition_parameters_1a5177a815e7989b6e86001076464b14eb)`(String secretId)` 

#### `public `[`DockerTransitionParameters`] [`setMemory`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_docker_transition_parameters_1ae6c2d6e74e8c5c4b383399c7e066dedc)`(Integer memory)` 

#### `public `[`DockerTransitionParameters`] [`setCpu`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_docker_transition_parameters_1a4ba534d7a6abe5ae3e0509c5e0a2ca7d)`(Integer cpu)` 

#### `public `[`DockerTransitionParameters`] [`setEnvironmentSecrets`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_docker_transition_parameters_1af8c88a8d63800aad3e7180b82b0f5c0a)`(String[] environmentSecrets)` 

#### `public `[`DockerTransitionParameters`] [`setEnvironment`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_docker_transition_parameters_1a4d2b42a01536ab100771164bf094d72f)`(Map< String, String > environment)` 

#### `public JSONObject `[`addOptions`]`(JSONObject body)` 

# class `ai::lucidtech::las::sdk::Field` 

```
class ai::lucidtech::las::sdk::Field
  : public ai.lucidtech.las.sdk.Options
```  

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public String `[`name`] | 
`public  `[`Field`]`(String name,`[`FieldType`](#enumai_1_1lucidtech_1_1las_1_1sdk_1_1_field_type)` fieldType,Integer maxLength)` | 
`public `[`Field`] [`setName`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_field_1a069d9673c20a97e833ca48e04e1620ed)`(String name)` | 
`public `[`Field`] [`setFieldType`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_field_1a0d8ffa4f63806111d97295a224dcc849)`(`[`FieldType`](#enumai_1_1lucidtech_1_1las_1_1sdk_1_1_field_type)` fieldType)` | 
`public `[`Field`] [`setMaxLength`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_field_1a562d537097a73eaec5ebda075cd7af7e)`(Integer maxLength)` | 
`public `[`Field`] [`setDescription`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_field_1a3069a2218f7dd0642782bacb97779446)`(String description)` | 
`public JSONObject `[`addOptions`]`(JSONObject body)` | 

## Members

#### `public String `[`name`] 

#### `public  `[`Field`]`(String name,`[`FieldType`](#enumai_1_1lucidtech_1_1las_1_1sdk_1_1_field_type)` fieldType,Integer maxLength)` 

#### `public `[`Field`] [`setName`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_field_1a069d9673c20a97e833ca48e04e1620ed)`(String name)` 

#### `public `[`Field`] [`setFieldType`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_field_1a0d8ffa4f63806111d97295a224dcc849)`(`[`FieldType`](#enumai_1_1lucidtech_1_1las_1_1sdk_1_1_field_type)` fieldType)` 

#### `public `[`Field`] [`setMaxLength`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_field_1a562d537097a73eaec5ebda075cd7af7e)`(Integer maxLength)` 

#### `public `[`Field`] [`setDescription`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_field_1a3069a2218f7dd0642782bacb97779446)`(String description)` 

#### `public JSONObject `[`addOptions`]`(JSONObject body)` 

# class `ai::lucidtech::las::sdk::FieldConfig` 

```
class ai::lucidtech::las::sdk::FieldConfig
  : public ai.lucidtech.las.sdk.Options
```  

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public `[`FieldConfig`] [`addField`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_field_config_1ad25b5131121d9554ad4e4811adb8ff62)`(`[`Field`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_field)` field)` | 
`public JSONObject `[`addOptions`]`(JSONObject body)` | 
`public JSONObject `[`toJson`]`()` | 

## Members

#### `public `[`FieldConfig`] [`addField`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_field_config_1ad25b5131121d9554ad4e4811adb8ff62)`(`[`Field`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_field)` field)` 

#### `public JSONObject `[`addOptions`]`(JSONObject body)` 

#### `public JSONObject `[`toJson`]`()` 

# class `ai::lucidtech::las::sdk::ListAppClientsOptions` 

```
class ai::lucidtech::las::sdk::ListAppClientsOptions
  : public ai.lucidtech.las.sdk.ListResourcesOptions< ListAppClientsOptions >
```  

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------

## Members

# class `ai::lucidtech::las::sdk::ListAssetsOptions` 

```
class ai::lucidtech::las::sdk::ListAssetsOptions
  : public ai.lucidtech.las.sdk.ListResourcesOptions< ListAssetsOptions >
```  

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------

## Members

# class `ai::lucidtech::las::sdk::ListBatchesOptions` 

```
class ai::lucidtech::las::sdk::ListBatchesOptions
  : public ai.lucidtech.las.sdk.ListResourcesOptions< ListBatchesOptions >
```  

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------

## Members

# class `ai::lucidtech::las::sdk::ListDocumentsOptions` 

```
class ai::lucidtech::las::sdk::ListDocumentsOptions
  : public ai.lucidtech.las.sdk.ListResourcesOptions< ListDocumentsOptions >
```  

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public `[`ListDocumentsOptions`] [`setConsentId`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_list_documents_options_1a60cbafbb5cb2443c0add044cf7b88abc)`(String consentId)` | 
`public `[`ListDocumentsOptions`] [`setDatasetId`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_list_documents_options_1ad11acdf5e0a5e815f217413a4dd17342)`(String datasetId)` | 
`public `[`ListDocumentsOptions`] [`setBatchId`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_list_documents_options_1ac52ae5b69f46e04451a645abce1e7ac7)`(String batchId)` | 
`public List< NameValuePair > `[`addOptions`]`(List< NameValuePair > parameters)` | 

## Members

#### `public `[`ListDocumentsOptions`] [`setConsentId`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_list_documents_options_1a60cbafbb5cb2443c0add044cf7b88abc)`(String consentId)` 

#### `public `[`ListDocumentsOptions`] [`setDatasetId`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_list_documents_options_1ad11acdf5e0a5e815f217413a4dd17342)`(String datasetId)` 

#### `public `[`ListDocumentsOptions`] [`setBatchId`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_list_documents_options_1ac52ae5b69f46e04451a645abce1e7ac7)`(String batchId)` 

#### `public List< NameValuePair > `[`addOptions`]`(List< NameValuePair > parameters)` 

# class `ai::lucidtech::las::sdk::ListLogsOptions` 

```
class ai::lucidtech::las::sdk::ListLogsOptions
  : public ai.lucidtech.las.sdk.ListResourcesOptions< ListLogsOptions >
```  

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public `[`ListLogsOptions`] [`setTransitionId`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_list_logs_options_1a0ba087cbe466b362eb0f88c7a01c54fd)`(String transitionId)` | 
`public `[`ListLogsOptions`] [`setTransitionExecutionId`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_list_logs_options_1a28aad7497a2818097a8026ee36146f6d)`(String transitionExecutionId)` | 
`public `[`ListLogsOptions`] [`setWorkflowId`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_list_logs_options_1a8640336f1d080459996287e1fdd3be23)`(String workflowId)` | 
`public `[`ListLogsOptions`] [`setWorkflowExecutionId`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_list_logs_options_1a57c6a3b3e889a2fd5511aeaf2f90497f)`(String workflowExecutionId)` | 
`public List< NameValuePair > `[`addOptions`]`(List< NameValuePair > parameters)` | 

## Members

#### `public `[`ListLogsOptions`] [`setTransitionId`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_list_logs_options_1a0ba087cbe466b362eb0f88c7a01c54fd)`(String transitionId)` 

#### `public `[`ListLogsOptions`] [`setTransitionExecutionId`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_list_logs_options_1a28aad7497a2818097a8026ee36146f6d)`(String transitionExecutionId)` 

#### `public `[`ListLogsOptions`] [`setWorkflowId`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_list_logs_options_1a8640336f1d080459996287e1fdd3be23)`(String workflowId)` 

#### `public `[`ListLogsOptions`] [`setWorkflowExecutionId`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_list_logs_options_1a57c6a3b3e889a2fd5511aeaf2f90497f)`(String workflowExecutionId)` 

#### `public List< NameValuePair > `[`addOptions`]`(List< NameValuePair > parameters)` 

# class `ai::lucidtech::las::sdk::ListModelsOptions` 

```
class ai::lucidtech::las::sdk::ListModelsOptions
  : public ai.lucidtech.las.sdk.ListResourcesOptions< ListModelsOptions >
```  

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------

## Members

# class `ai::lucidtech::las::sdk::ListPredictionsOptions` 

```
class ai::lucidtech::las::sdk::ListPredictionsOptions
  : public ai.lucidtech.las.sdk.ListResourcesOptions< ListPredictionsOptions >
```  

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------

## Members

# class `ai::lucidtech::las::sdk::ListResourcesOptions` 

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public T `[`setMaxResults`]`(int maxResults)` | 
`public T `[`setNextToken`]`(String nextToken)` | 
`public List< NameValuePair > `[`addOptions`]`(List< NameValuePair > parameters)` | 
`protected void `[`addOption`]`(List< NameValuePair > parameters,String key,String value)` | 
`protected void `[`addOption`]`(List< NameValuePair > parameters,String key,String[] value)` | 
`protected void `[`addOption`]`(List< NameValuePair > parameters,String key,List< String > value)` | 
`protected void `[`addOption`]`(List< NameValuePair > parameters,String key,Integer value)` | 

## Members

#### `public T `[`setMaxResults`]`(int maxResults)` 

#### `public T `[`setNextToken`]`(String nextToken)` 

#### `public List< NameValuePair > `[`addOptions`]`(List< NameValuePair > parameters)` 

#### `protected void `[`addOption`]`(List< NameValuePair > parameters,String key,String value)` 

#### `protected void `[`addOption`]`(List< NameValuePair > parameters,String key,String[] value)` 

#### `protected void `[`addOption`]`(List< NameValuePair > parameters,String key,List< String > value)` 

#### `protected void `[`addOption`]`(List< NameValuePair > parameters,String key,Integer value)` 

# class `ai::lucidtech::las::sdk::ListSecretsOptions` 

```
class ai::lucidtech::las::sdk::ListSecretsOptions
  : public ai.lucidtech.las.sdk.ListResourcesOptions< ListSecretsOptions >
```  

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------

## Members

# class `ai::lucidtech::las::sdk::ListSortablesOptions` 

```
class ai::lucidtech::las::sdk::ListSortablesOptions
  : public ai::lucidtech::las::sdk::ListResourcesOptions< T >
```  

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public T `[`setSortBy`]`(String sortBy)` | 
`public T `[`setOrder`]`(`[`Order`](#enumai_1_1lucidtech_1_1las_1_1sdk_1_1_order)` order)` | 
`public List< NameValuePair > `[`addOptions`]`(List< NameValuePair > parameters)` | 
`protected String `[`sortBy`] | 
`protected `[`Order`](#enumai_1_1lucidtech_1_1las_1_1sdk_1_1_order) [`order`] | 

## Members

#### `public T `[`setSortBy`]`(String sortBy)` 

#### `public T `[`setOrder`]`(`[`Order`](#enumai_1_1lucidtech_1_1las_1_1sdk_1_1_order)` order)` 

#### `public List< NameValuePair > `[`addOptions`]`(List< NameValuePair > parameters)` 

#### `protected String `[`sortBy`] 

#### `protected `[`Order`](#enumai_1_1lucidtech_1_1las_1_1sdk_1_1_order) [`order`] 

# class `ai::lucidtech::las::sdk::ListTransitionExecutionsOptions` 

```
class ai::lucidtech::las::sdk::ListTransitionExecutionsOptions
  : public ai.lucidtech.las.sdk.ListSortablesOptions< ListTransitionExecutionsOptions >
```  

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public `[`ListTransitionExecutionsOptions`] [`setExecutionId`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_list_transition_executions_options_1a17be680d06dd9eaaaf9c3d0df3519d9d)`(List< String > executionId)` | 
`public `[`ListTransitionExecutionsOptions`] [`setExecutionId`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_list_transition_executions_options_1a6fed26e978e0eec35e8a3dc4297010b7)`(String executionId)` | 
`public `[`ListTransitionExecutionsOptions`] [`setStatus`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_list_transition_executions_options_1aaffb59561c7c6f2ba7249948783b83f0)`(List< `[`TransitionExecutionStatus`](#enumai_1_1lucidtech_1_1las_1_1sdk_1_1_transition_execution_status)` > status)` | 
`public `[`ListTransitionExecutionsOptions`] [`setStatus`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_list_transition_executions_options_1af793df3ada1088f6dc7f83117ec02be1)`(`[`TransitionExecutionStatus`](#enumai_1_1lucidtech_1_1las_1_1sdk_1_1_transition_execution_status)` status)` | 
`public List< NameValuePair > `[`addOptions`]`(List< NameValuePair > parameters)` | 

## Members

#### `public `[`ListTransitionExecutionsOptions`] [`setExecutionId`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_list_transition_executions_options_1a17be680d06dd9eaaaf9c3d0df3519d9d)`(List< String > executionId)` 

#### `public `[`ListTransitionExecutionsOptions`] [`setExecutionId`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_list_transition_executions_options_1a6fed26e978e0eec35e8a3dc4297010b7)`(String executionId)` 

#### `public `[`ListTransitionExecutionsOptions`] [`setStatus`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_list_transition_executions_options_1aaffb59561c7c6f2ba7249948783b83f0)`(List< `[`TransitionExecutionStatus`](#enumai_1_1lucidtech_1_1las_1_1sdk_1_1_transition_execution_status)` > status)` 

#### `public `[`ListTransitionExecutionsOptions`] [`setStatus`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_list_transition_executions_options_1af793df3ada1088f6dc7f83117ec02be1)`(`[`TransitionExecutionStatus`](#enumai_1_1lucidtech_1_1las_1_1sdk_1_1_transition_execution_status)` status)` 

#### `public List< NameValuePair > `[`addOptions`]`(List< NameValuePair > parameters)` 

# class `ai::lucidtech::las::sdk::ListTransitionsOptions` 

```
class ai::lucidtech::las::sdk::ListTransitionsOptions
  : public ai.lucidtech.las.sdk.ListResourcesOptions< ListTransitionsOptions >
```  

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public `[`ListTransitionsOptions`] [`setTransitionType`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_list_transitions_options_1a63e360ea5c442b76317e5c0f01ed29d8)`(`[`TransitionType`](#enumai_1_1lucidtech_1_1las_1_1sdk_1_1_transition_type)` transitionType)` | 
`public List< NameValuePair > `[`addOptions`]`(List< NameValuePair > parameters)` | 

## Members

#### `public `[`ListTransitionsOptions`] [`setTransitionType`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_list_transitions_options_1a63e360ea5c442b76317e5c0f01ed29d8)`(`[`TransitionType`](#enumai_1_1lucidtech_1_1las_1_1sdk_1_1_transition_type)` transitionType)` 

#### `public List< NameValuePair > `[`addOptions`]`(List< NameValuePair > parameters)` 

# class `ai::lucidtech::las::sdk::ListUsersOptions` 

```
class ai::lucidtech::las::sdk::ListUsersOptions
  : public ai.lucidtech.las.sdk.ListResourcesOptions< ListUsersOptions >
```  

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------

## Members

# class `ai::lucidtech::las::sdk::ListWorkflowExecutionsOptions` 

```
class ai::lucidtech::las::sdk::ListWorkflowExecutionsOptions
  : public ai.lucidtech.las.sdk.ListSortablesOptions< ListWorkflowExecutionsOptions >
```  

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public `[`ListWorkflowExecutionsOptions`] [`setStatus`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_list_workflow_executions_options_1aaf7e9a62ee579d8949fd62d36d0e65db)`(List< `[`WorkflowExecutionStatus`](#enumai_1_1lucidtech_1_1las_1_1sdk_1_1_workflow_execution_status)` > status)` | 
`public `[`ListWorkflowExecutionsOptions`] [`setStatus`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_list_workflow_executions_options_1a0b2f966d52b2aeef2b37ac7c5e5eb520)`(`[`WorkflowExecutionStatus`](#enumai_1_1lucidtech_1_1las_1_1sdk_1_1_workflow_execution_status)` status)` | 
`public List< NameValuePair > `[`addOptions`]`(List< NameValuePair > parameters)` | 

## Members

#### `public `[`ListWorkflowExecutionsOptions`] [`setStatus`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_list_workflow_executions_options_1aaf7e9a62ee579d8949fd62d36d0e65db)`(List< `[`WorkflowExecutionStatus`](#enumai_1_1lucidtech_1_1las_1_1sdk_1_1_workflow_execution_status)` > status)` 

#### `public `[`ListWorkflowExecutionsOptions`] [`setStatus`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_list_workflow_executions_options_1a0b2f966d52b2aeef2b37ac7c5e5eb520)`(`[`WorkflowExecutionStatus`](#enumai_1_1lucidtech_1_1las_1_1sdk_1_1_workflow_execution_status)` status)` 

#### `public List< NameValuePair > `[`addOptions`]`(List< NameValuePair > parameters)` 

# class `ai::lucidtech::las::sdk::ListWorkflowsOptions` 

```
class ai::lucidtech::las::sdk::ListWorkflowsOptions
  : public ai.lucidtech.las.sdk.ListResourcesOptions< ListWorkflowsOptions >
```  

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------

## Members

# class `ai::lucidtech::las::sdk::ManualTransitionParameters` 

```
class ai::lucidtech::las::sdk::ManualTransitionParameters
  : public ai.lucidtech.las.sdk.TransitionParameters
```  

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public `[`ManualTransitionParameters`] [`setAssets`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_manual_transition_parameters_1ac6f32809496241e3a656aab6193cba2a)`(Map< String, String > assets)` | 
`public JSONObject `[`addOptions`]`(JSONObject body)` | 

## Members

#### `public `[`ManualTransitionParameters`] [`setAssets`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_manual_transition_parameters_1ac6f32809496241e3a656aab6193cba2a)`(Map< String, String > assets)` 

#### `public JSONObject `[`addOptions`]`(JSONObject body)` 

# class `ai::lucidtech::las::sdk::MissingAccessTokenException` 

```
class ai::lucidtech::las::sdk::MissingAccessTokenException
  : public Exception
```  

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------

## Members

# class `ai::lucidtech::las::sdk::MissingCredentialsException` 

```
class ai::lucidtech::las::sdk::MissingCredentialsException
  : public Exception
```  

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------

## Members

# class `ai::lucidtech::las::sdk::NameAndDescriptionOptions` 

```
class ai::lucidtech::las::sdk::NameAndDescriptionOptions
  : public ai.lucidtech.las.sdk.Options
```  

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public T `[`setName`]`(String name)` | 
`public T `[`setDescription`]`(String description)` | 
`public JSONObject `[`addOptions`]`(JSONObject body)` | 
`public JSONObject `[`toJson`]`()` | 

## Members

#### `public T `[`setName`]`(String name)` 

#### `public T `[`setDescription`]`(String description)` 

#### `public JSONObject `[`addOptions`]`(JSONObject body)` 

#### `public JSONObject `[`toJson`]`()` 

# class `ai::lucidtech::las::sdk::NullableString` 

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public Boolean `[`hasEditedValue`] | 
`public  `[`NullableString`]`()` | 
`public void `[`setValue`]`(String value)` | 

## Members

#### `public Boolean `[`hasEditedValue`] 

#### `public  `[`NullableString`]`()` 

#### `public void `[`setValue`]`(String value)` 

# class `ai::lucidtech::las::sdk::Options` 

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public abstract JSONObject `[`addOptions`]`(JSONObject body)` | 
`protected void `[`addOption`]`(JSONObject body,String key,NullableString value)` | 
`protected void `[`addOption`]`(JSONObject body,String key,String value)` | 
`protected void `[`addOption`]`(JSONObject body,String key,String[] value)` | 
`protected void `[`addOption`]`(JSONObject body,String key,Map< String, String > value)` | 
`protected void `[`addOption`]`(JSONObject body,String key,Boolean value)` | 
`protected void `[`addOption`]`(JSONObject body,String key,Integer value)` | 
`protected void `[`addOption`]`(JSONObject body,String key,JSONArray value)` | 
`protected void `[`addOption`]`(JSONObject body,String key,JSONObject value)` | 
`protected void `[`addOption`]`(JSONObject body,String key,`[`Options`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_options)` value)` | 

## Members

#### `public abstract JSONObject `[`addOptions`]`(JSONObject body)` 

#### `protected void `[`addOption`]`(JSONObject body,String key,NullableString value)` 

#### `protected void `[`addOption`]`(JSONObject body,String key,String value)` 

#### `protected void `[`addOption`]`(JSONObject body,String key,String[] value)` 

#### `protected void `[`addOption`]`(JSONObject body,String key,Map< String, String > value)` 

#### `protected void `[`addOption`]`(JSONObject body,String key,Boolean value)` 

#### `protected void `[`addOption`]`(JSONObject body,String key,Integer value)` 

#### `protected void `[`addOption`]`(JSONObject body,String key,JSONArray value)` 

#### `protected void `[`addOption`]`(JSONObject body,String key,JSONObject value)` 

#### `protected void `[`addOption`]`(JSONObject body,String key,`[`Options`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_options)` value)` 

# class `ai::lucidtech::las::sdk::PreprocessConfig` 

```
class ai::lucidtech::las::sdk::PreprocessConfig
  : public ai.lucidtech.las.sdk.Options
```  

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public `[`PreprocessConfig`] [`setImageQuality`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_preprocess_config_1a921565e7cd48714db772156cfa9d332a)`(`[`ImageQuality`](#enumai_1_1lucidtech_1_1las_1_1sdk_1_1_image_quality)` imageQuality)` | 
`public `[`PreprocessConfig`] [`setAutoRotate`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_preprocess_config_1a5a140a77bf7dec6c7ebde44973593be5)`(Boolean autoRotate)` | 
`public `[`PreprocessConfig`] [`setMaxPages`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_preprocess_config_1add6c7c76cb74a413dc3b79de09aa5af1)`(Integer maxPages)` | 
`public JSONObject `[`addOptions`]`(JSONObject body)` | 

## Members

#### `public `[`PreprocessConfig`] [`setImageQuality`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_preprocess_config_1a921565e7cd48714db772156cfa9d332a)`(`[`ImageQuality`](#enumai_1_1lucidtech_1_1las_1_1sdk_1_1_image_quality)` imageQuality)` 

#### `public `[`PreprocessConfig`] [`setAutoRotate`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_preprocess_config_1a5a140a77bf7dec6c7ebde44973593be5)`(Boolean autoRotate)` 

#### `public `[`PreprocessConfig`] [`setMaxPages`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_preprocess_config_1add6c7c76cb74a413dc3b79de09aa5af1)`(Integer maxPages)` 

#### `public JSONObject `[`addOptions`]`(JSONObject body)` 

# class `ai::lucidtech::las::sdk::TransitionParameters` 

```
class ai::lucidtech::las::sdk::TransitionParameters
  : public ai.lucidtech.las.sdk.Options
```  

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public abstract JSONObject `[`addOptions`]`(JSONObject body)` | 

## Members

#### `public abstract JSONObject `[`addOptions`]`(JSONObject body)` 

# class `ai::lucidtech::las::sdk::UpdateAppClientOptions` 

```
class ai::lucidtech::las::sdk::UpdateAppClientOptions
  : public ai.lucidtech.las.sdk.NameAndDescriptionOptions< UpdateAppClientOptions >
```  

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------

## Members

# class `ai::lucidtech::las::sdk::UpdateAssetOptions` 

```
class ai::lucidtech::las::sdk::UpdateAssetOptions
  : public ai.lucidtech.las.sdk.NameAndDescriptionOptions< UpdateAssetOptions >
```  

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public `[`UpdateAssetOptions`] [`setContent`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_update_asset_options_1a2c82436e7cf26983ee2c2d892d159773)`(byte[] content)` | 
`public `[`UpdateAssetOptions`] [`setContent`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_update_asset_options_1ad86efbed928b01bc637eedda9f19c733)`(InputStream content)` | 
`public JSONObject `[`addOptions`]`(JSONObject body)` | 
`public JSONObject `[`toJson`]`()` | 

## Members

#### `public `[`UpdateAssetOptions`] [`setContent`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_update_asset_options_1a2c82436e7cf26983ee2c2d892d159773)`(byte[] content)` 

#### `public `[`UpdateAssetOptions`] [`setContent`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_update_asset_options_1ad86efbed928b01bc637eedda9f19c733)`(InputStream content)` 

#### `public JSONObject `[`addOptions`]`(JSONObject body)` 

#### `public JSONObject `[`toJson`]`()` 

# class `ai::lucidtech::las::sdk::UpdateBatchOptions` 

```
class ai::lucidtech::las::sdk::UpdateBatchOptions
  : public ai.lucidtech.las.sdk.NameAndDescriptionOptions< UpdateBatchOptions >
```  

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------

## Members

# class `ai::lucidtech::las::sdk::UpdateModelOptions` 

```
class ai::lucidtech::las::sdk::UpdateModelOptions
  : public ai.lucidtech.las.sdk.NameAndDescriptionOptions< UpdateModelOptions >
```  

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public `[`UpdateModelOptions`] [`setWidth`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_update_model_options_1a01fc78feb68e7ee3aeaf43a271761a66)`(Integer width)` | 
`public `[`UpdateModelOptions`] [`setHeight`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_update_model_options_1a2da6e50d998b640fa77a9236d0673065)`(Integer height)` | 
`public `[`UpdateModelOptions`] [`setFieldConfig`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_update_model_options_1aea4fd4d0f263cf1a5f3516bbd7910efc)`(`[`FieldConfig`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_field_config)` fieldConfig)` | 
`public `[`UpdateModelOptions`] [`setModelStatus`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_update_model_options_1ad1d2a5b7900a8e46bcf11dc24ad288a2)`(`[`ModelStatus`](#enumai_1_1lucidtech_1_1las_1_1sdk_1_1_model_status)` modelStatus)` | 
`public `[`UpdateModelOptions`] [`setPreprocessConfig`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_update_model_options_1ac462fc8fa030b5c7853ccae24782fb3c)`(`[`PreprocessConfig`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_preprocess_config)` preprocessConfig)` | 
`public JSONObject `[`addOptions`]`(JSONObject body)` | 
`public JSONObject `[`toJson`]`()` | 

## Members

#### `public `[`UpdateModelOptions`] [`setWidth`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_update_model_options_1a01fc78feb68e7ee3aeaf43a271761a66)`(Integer width)` 

#### `public `[`UpdateModelOptions`] [`setHeight`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_update_model_options_1a2da6e50d998b640fa77a9236d0673065)`(Integer height)` 

#### `public `[`UpdateModelOptions`] [`setFieldConfig`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_update_model_options_1aea4fd4d0f263cf1a5f3516bbd7910efc)`(`[`FieldConfig`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_field_config)` fieldConfig)` 

#### `public `[`UpdateModelOptions`] [`setModelStatus`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_update_model_options_1ad1d2a5b7900a8e46bcf11dc24ad288a2)`(`[`ModelStatus`](#enumai_1_1lucidtech_1_1las_1_1sdk_1_1_model_status)` modelStatus)` 

#### `public `[`UpdateModelOptions`] [`setPreprocessConfig`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_update_model_options_1ac462fc8fa030b5c7853ccae24782fb3c)`(`[`PreprocessConfig`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_preprocess_config)` preprocessConfig)` 

#### `public JSONObject `[`addOptions`]`(JSONObject body)` 

#### `public JSONObject `[`toJson`]`()` 

# class `ai::lucidtech::las::sdk::UpdateSecretOptions` 

```
class ai::lucidtech::las::sdk::UpdateSecretOptions
  : public ai.lucidtech.las.sdk.NameAndDescriptionOptions< UpdateSecretOptions >
```  

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public `[`UpdateSecretOptions`] [`setData`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_update_secret_options_1a85cd3d884163f771962f080a7cfe9e08)`(JSONObject data)` | 
`public `[`UpdateSecretOptions`] [`setData`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_update_secret_options_1ac88357dcd64d7a950b560e7bf60f9fe4)`(Map< String, String > data)` | 
`public JSONObject `[`addOptions`]`(JSONObject body)` | 
`public JSONObject `[`toJson`]`()` | 

## Members

#### `public `[`UpdateSecretOptions`] [`setData`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_update_secret_options_1a85cd3d884163f771962f080a7cfe9e08)`(JSONObject data)` 

#### `public `[`UpdateSecretOptions`] [`setData`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_update_secret_options_1ac88357dcd64d7a950b560e7bf60f9fe4)`(Map< String, String > data)` 

#### `public JSONObject `[`addOptions`]`(JSONObject body)` 

#### `public JSONObject `[`toJson`]`()` 

# class `ai::lucidtech::las::sdk::UpdateTransitionExecutionOptions` 

```
class ai::lucidtech::las::sdk::UpdateTransitionExecutionOptions
  : public ai.lucidtech.las.sdk.Options
```  

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public `[`UpdateTransitionExecutionOptions`] [`setOutput`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_update_transition_execution_options_1afc7f677cd0d46baaea8376d2f02a621d)`(JSONObject error)` | 
`public `[`UpdateTransitionExecutionOptions`] [`setError`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_update_transition_execution_options_1a7df40cd9c5c3735c8abfb6f9d91a8f8e)`(JSONObject output)` | 
`public `[`UpdateTransitionExecutionOptions`] [`setStartTime`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_update_transition_execution_options_1a91eaf567d5e65b0fb5eb3afd8f68c253)`(String startTime)` | 
`public `[`UpdateTransitionExecutionOptions`] [`setStartTime`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_update_transition_execution_options_1af03251ca5b54aa8c4ac5623496490286)`(ZonedDateTime startTime)` | 
`public JSONObject `[`addOptions`]`(JSONObject body)` | 
`public JSONObject `[`toJson`]`()` | 

## Members

#### `public `[`UpdateTransitionExecutionOptions`] [`setOutput`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_update_transition_execution_options_1afc7f677cd0d46baaea8376d2f02a621d)`(JSONObject error)` 

#### `public `[`UpdateTransitionExecutionOptions`] [`setError`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_update_transition_execution_options_1a7df40cd9c5c3735c8abfb6f9d91a8f8e)`(JSONObject output)` 

#### `public `[`UpdateTransitionExecutionOptions`] [`setStartTime`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_update_transition_execution_options_1a91eaf567d5e65b0fb5eb3afd8f68c253)`(String startTime)` 

#### `public `[`UpdateTransitionExecutionOptions`] [`setStartTime`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_update_transition_execution_options_1af03251ca5b54aa8c4ac5623496490286)`(ZonedDateTime startTime)` 

#### `public JSONObject `[`addOptions`]`(JSONObject body)` 

#### `public JSONObject `[`toJson`]`()` 

# class `ai::lucidtech::las::sdk::UpdateTransitionOptions` 

```
class ai::lucidtech::las::sdk::UpdateTransitionOptions
  : public ai.lucidtech.las.sdk.NameAndDescriptionOptions< UpdateTransitionOptions >
```  

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public `[`UpdateTransitionOptions`] [`setInputJsonSchema`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_update_transition_options_1a2e6d97d967f6270b2f9de77eabebc86d)`(JSONObject schema)` | 
`public `[`UpdateTransitionOptions`] [`setOutputJsonSchema`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_update_transition_options_1adcaad2be6ae5fe6c41052101eee65926)`(JSONObject schema)` | 
`public JSONObject `[`addOptions`]`(JSONObject body)` | 
`public JSONObject `[`toJson`]`()` | 

## Members

#### `public `[`UpdateTransitionOptions`] [`setInputJsonSchema`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_update_transition_options_1a2e6d97d967f6270b2f9de77eabebc86d)`(JSONObject schema)` 

#### `public `[`UpdateTransitionOptions`] [`setOutputJsonSchema`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_update_transition_options_1adcaad2be6ae5fe6c41052101eee65926)`(JSONObject schema)` 

#### `public JSONObject `[`addOptions`]`(JSONObject body)` 

#### `public JSONObject `[`toJson`]`()` 

# class `ai::lucidtech::las::sdk::UpdateUserOptions` 

```
class ai::lucidtech::las::sdk::UpdateUserOptions
  : public ai.lucidtech.las.sdk.UserOptions< UpdateUserOptions >
```  

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------

## Members

# class `ai::lucidtech::las::sdk::UpdateWorkflowOptions` 

```
class ai::lucidtech::las::sdk::UpdateWorkflowOptions
  : public ai.lucidtech.las.sdk.NameAndDescriptionOptions< UpdateWorkflowOptions >
```  

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------

## Members

# class `ai::lucidtech::las::sdk::UserOptions` 

```
class ai::lucidtech::las::sdk::UserOptions
  : public ai.lucidtech.las.sdk.Options
```  

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public T `[`setName`]`(String name)` | 
`public T `[`setAvatar`]`(String avatar)` | 
`public T `[`setAvatar`]`(byte[] avatar)` | 
`public JSONObject `[`addOptions`]`(JSONObject body)` | 
`public JSONObject `[`toJson`]`()` | 

## Members

#### `public T `[`setName`]`(String name)` 

#### `public T `[`setAvatar`]`(String avatar)` 

#### `public T `[`setAvatar`]`(byte[] avatar)` 

#### `public JSONObject `[`addOptions`]`(JSONObject body)` 

#### `public JSONObject `[`toJson`]`()` 

# class `ai::lucidtech::las::sdk::WorkflowCompletedConfig` 

```
class ai::lucidtech::las::sdk::WorkflowCompletedConfig
  : public ai.lucidtech.las.sdk.Options
```  

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public `[`WorkflowCompletedConfig`] [`setImageUrl`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_workflow_completed_config_1a098d36b9e6bbd2fbe61552e897882c19)`(String imageUrl)` | 
`public `[`WorkflowCompletedConfig`] [`setSecretId`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_workflow_completed_config_1ac2dcc7edfbc11762c43d26343eef1c2d)`(String secretId)` | 
`public `[`WorkflowCompletedConfig`] [`setEnvironmentSecrets`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_workflow_completed_config_1a8e29416dbfccb4320b35d2f8e0b7b09e)`(String[] environmentSecrets)` | 
`public `[`WorkflowCompletedConfig`] [`setEnvironment`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_workflow_completed_config_1a4c20fb980273b190060ce5c75acb315f)`(Map< String, String > environment)` | 
`public JSONObject `[`addOptions`]`(JSONObject body)` | 

## Members

#### `public `[`WorkflowCompletedConfig`] [`setImageUrl`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_workflow_completed_config_1a098d36b9e6bbd2fbe61552e897882c19)`(String imageUrl)` 

#### `public `[`WorkflowCompletedConfig`] [`setSecretId`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_workflow_completed_config_1ac2dcc7edfbc11762c43d26343eef1c2d)`(String secretId)` 

#### `public `[`WorkflowCompletedConfig`] [`setEnvironmentSecrets`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_workflow_completed_config_1a8e29416dbfccb4320b35d2f8e0b7b09e)`(String[] environmentSecrets)` 

#### `public `[`WorkflowCompletedConfig`] [`setEnvironment`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_workflow_completed_config_1a4c20fb980273b190060ce5c75acb315f)`(Map< String, String > environment)` 

#### `public JSONObject `[`addOptions`]`(JSONObject body)` 

# class `ai::lucidtech::las::sdk::WorkflowErrorConfig` 

```
class ai::lucidtech::las::sdk::WorkflowErrorConfig
  : public ai.lucidtech.las.sdk.Options
```  

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public `[`WorkflowErrorConfig`] [`setEmail`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_workflow_error_config_1ac0fa13c1d6704a9805eeee56d7de34b6)`(String email)` | 
`public `[`WorkflowErrorConfig`] [`setManualRetry`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_workflow_error_config_1a058574fcc2a8856e766c6c29c8786359)`(Boolean manualRetry)` | 
`public JSONObject `[`addOptions`]`(JSONObject body)` | 

## Members

#### `public `[`WorkflowErrorConfig`] [`setEmail`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_workflow_error_config_1ac0fa13c1d6704a9805eeee56d7de34b6)`(String email)` 

#### `public `[`WorkflowErrorConfig`] [`setManualRetry`](#classai_1_1lucidtech_1_1las_1_1sdk_1_1_workflow_error_config_1a058574fcc2a8856e766c6c29c8786359)`(Boolean manualRetry)` 

#### `public JSONObject `[`addOptions`]`(JSONObject body)` 

Generated by [Moxygen](https://sourcey.com/moxygen)