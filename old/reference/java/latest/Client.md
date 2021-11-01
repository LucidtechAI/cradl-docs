# class `ai::lucidtech::las::sdk::Client` 

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public  `[`Client`]`(`[`Credentials`](docs/ai::lucidtech::las::sdk::Credentials.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_credentials)` credentials)` | A client to invoke api methods from Lucidtech AI Services.
`public JSONObject `[`createAppClient`]`(`[`CreateAppClientOptions`](docs/ai::lucidtech::las::sdk::CreateAppClientOptions.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_create_app_client_options)` options)` | Create an app client, calls the POST /appClients endpoint.
`public JSONObject `[`createAppClient`]`()` | Create an app client, calls the POST /appClients endpoint.
`public JSONObject `[`updateAppClient`]`(String appClientId,`[`UpdateAppClientOptions`](docs/ai::lucidtech::las::sdk::UpdateAppClientOptions.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_update_app_client_options)` options)` | Update an appClient, calls the PATCH /appClients/{appClientId} endpoint.
`public JSONObject `[`listAppClients`]`(`[`ListAppClientsOptions`](docs/ai::lucidtech::las::sdk::ListAppClientsOptions.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_list_app_clients_options)` options)` | List appClients available, calls the GET /appClients endpoint.
`public JSONObject `[`listAppClients`]`()` | List appClients available, calls the GET /appClients endpoint.
`public JSONObject `[`deleteAppClient`]`(String appClientId)` | Delete an appClient, calls the DELETE /appClients/{appClientId} endpoint.
`public JSONObject `[`createAsset`]`(byte[] content,`[`CreateAssetOptions`](docs/ai::lucidtech::las::sdk::CreateAssetOptions.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_create_asset_options)` options)` | Create an asset, calls the POST /assets endpoint.
`public JSONObject `[`createAsset`]`(InputStream content,`[`CreateAssetOptions`](docs/ai::lucidtech::las::sdk::CreateAssetOptions.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_create_asset_options)` options)` | Create an asset, calls the POST /assets endpoint.
`public JSONObject `[`createAsset`]`(byte[] content)` | Create an asset, calls the POST /assets endpoint.
`public JSONObject `[`createAsset`]`(InputStream content)` | Create an asset, calls the POST /assets endpoint.
`public JSONObject `[`listAssets`]`(`[`ListAssetsOptions`](docs/ai::lucidtech::las::sdk::ListAssetsOptions.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_list_assets_options)` options)` | List assets available, calls the GET /assets endpoint.
`public JSONObject `[`listAssets`]`()` | List assets available, calls the GET /assets endpoint.
`public JSONObject `[`getAsset`]`(String assetId)` | Get asset, calls the GET /assets/{assetId} endpoint.
`public JSONObject `[`updateAsset`]`(String assetId,`[`UpdateAssetOptions`](docs/ai::lucidtech::las::sdk::UpdateAssetOptions.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_update_asset_options)` options)` | Update an asset, calls the PATCH /assets/{assetId} endpoint.
`public JSONObject `[`deleteAsset`]`(String assetId)` | Delete an asset, calls the DELETE /assets/{assetId} endpoint.
`public JSONObject `[`createDocument`]`(byte[] content,`[`ContentType`](docs/ai::lucidtech::las::sdk::ContentType.md#enumai_1_1lucidtech_1_1las_1_1sdk_1_1_content_type)` contentType,`[`CreateDocumentOptions`](docs/ai::lucidtech::las::sdk::CreateDocumentOptions.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_create_document_options)` options)` | Create a document, calls the POST /documents endpoint.
`public JSONObject `[`createDocument`]`(InputStream content,`[`ContentType`](docs/ai::lucidtech::las::sdk::ContentType.md#enumai_1_1lucidtech_1_1las_1_1sdk_1_1_content_type)` contentType,`[`CreateDocumentOptions`](docs/ai::lucidtech::las::sdk::CreateDocumentOptions.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_create_document_options)` options)` | Create a document, calls the POST /documents endpoint.
`public JSONObject `[`createDocument`]`(InputStream content,`[`ContentType`](docs/ai::lucidtech::las::sdk::ContentType.md#enumai_1_1lucidtech_1_1las_1_1sdk_1_1_content_type)` contentType)` | Create a document, calls the POST /documents endpoint.
`public JSONObject `[`createDocument`]`(byte[] content,`[`ContentType`](docs/ai::lucidtech::las::sdk::ContentType.md#enumai_1_1lucidtech_1_1las_1_1sdk_1_1_content_type)` contentType)` | Create a document, calls the POST /documents endpoint.
`public JSONObject `[`listDocuments`]`(`[`ListDocumentsOptions`](docs/ai::lucidtech::las::sdk::ListDocumentsOptions.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_list_documents_options)` options)` | List documents, calls the GET /documents endpoint.
`public JSONObject `[`listDocuments`]`()` | List documents, calls the GET /documents endpoint.
`public JSONObject `[`deleteDocuments`]`(`[`DeleteDocumentsOptions`](docs/ai::lucidtech::las::sdk::DeleteDocumentsOptions.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_delete_documents_options)` options)` | Delete documents, calls the DELETE /documents endpoint.
`public JSONObject `[`deleteDocuments`]`()` | Delete documents, calls the DELETE /documents endpoint.
`public JSONObject `[`getDocument`]`(String documentId)` | Get document, calls the GET /documents/{documentId} endpoint.
`public JSONObject `[`updateDocument`]`(String documentId,`[`UpdateDocumentOptions`](docs/ai::lucidtech::las::sdk::UpdateDocumentOptions.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_update_document_options)` options)` | Update document, calls the PATCH /documents/{documentId} endpoint.
`public JSONObject `[`getLog`]`(String logId)` | Get log, calls the GET /logs/{logId} endpoint.
`public JSONObject `[`listLogs`]`(`[`ListLogsOptions`](docs/ai::lucidtech::las::sdk::ListLogsOptions.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_list_logs_options)` options)` | List logs, calls the GET /logs endpoint.
`public JSONObject `[`listLogs`]`()` | List logs, calls the GET /logs endpoint.
`public JSONObject `[`createModel`]`(int width,int height,`[`FieldConfig`](docs/ai::lucidtech::las::sdk::FieldConfig.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_field_config)` fieldConfig,`[`CreateModelOptions`](docs/ai::lucidtech::las::sdk::CreateModelOptions.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_create_model_options)` options)` | Create a model, calls the POST /models endpoint.
`public JSONObject `[`createModel`]`(int width,int height,`[`FieldConfig`](docs/ai::lucidtech::las::sdk::FieldConfig.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_field_config)` fieldConfig)` | Create a model, calls the POST /models endpoint.
`public JSONObject `[`updateModel`]`(String modelId,`[`UpdateModelOptions`](docs/ai::lucidtech::las::sdk::UpdateModelOptions.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_update_model_options)` options)` | Updates a model, calls the PATCH /models/{modelId} endpoint.
`public JSONObject `[`getModel`]`(String modelId)` | Get model, calls the GET /models/{modelId} endpoint.
`public JSONObject `[`listModels`]`(`[`ListModelsOptions`](docs/ai::lucidtech::las::sdk::ListModelsOptions.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_list_models_options)` options)` | List models, calls the GET /models endpoint.
`public JSONObject `[`listModels`]`()` | List models available, calls the GET /models endpoint.
`public JSONObject `[`createPrediction`]`(String documentId,String modelId,`[`CreatePredictionOptions`](docs/ai::lucidtech::las::sdk::CreatePredictionOptions.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_create_prediction_options)` options)` | Create a prediction on a document using specified model, calls the POST /predictions endpoint.
`public JSONObject `[`createPrediction`]`(String documentId,String modelId)` | Create a prediction on a document using specified model, calls the POST /predictions endpoint.
`public JSONObject `[`listPredictions`]`(`[`ListPredictionsOptions`](docs/ai::lucidtech::las::sdk::ListPredictionsOptions.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_list_predictions_options)` options)` | List predictions available, calls the GET /predictions endpoint.
`public JSONObject `[`listPredictions`]`()` | List predictions available, calls the GET /predictions endpoint.
`public JSONObject `[`createSecret`]`(JSONObject data,`[`CreateSecretOptions`](docs/ai::lucidtech::las::sdk::CreateSecretOptions.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_create_secret_options)` options)` | Create secret, calls the POST /secrets endpoint.
`public JSONObject `[`createSecret`]`(Map< String, String > data,`[`CreateSecretOptions`](docs/ai::lucidtech::las::sdk::CreateSecretOptions.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_create_secret_options)` options)` | Create a secret, calls the POST /secrets endpoint.
`public JSONObject `[`createSecret`]`(Map< String, String > data)` | Create a secret, calls the POST /secrets endpoint.
`public JSONObject `[`createSecret`]`(JSONObject data)` | Create a secret, calls the POST /secrets endpoint.
`public JSONObject `[`listSecrets`]`(`[`ListSecretsOptions`](docs/ai::lucidtech::las::sdk::ListSecretsOptions.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_list_secrets_options)` options)` | List secrets, calls the GET /secrets endpoint.
`public JSONObject `[`listSecrets`]`()` | List secrets, calls the GET /secrets endpoint.
`public JSONObject `[`updateSecret`]`(String secretId,`[`UpdateSecretOptions`](docs/ai::lucidtech::las::sdk::UpdateSecretOptions.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_update_secret_options)` options)` | Update a secret, calls the PATCH /secrets/{secretId} endpoint.
`public JSONObject `[`deleteSecret`]`(String secretId)` | Delete a secret, calls the DELETE /secrets/{secretId} endpoint.
`public JSONObject `[`createTransition`]`(`[`TransitionType`](docs/ai::lucidtech::las::sdk::TransitionType.md#enumai_1_1lucidtech_1_1las_1_1sdk_1_1_transition_type)` transitionType,`[`CreateTransitionOptions`](docs/ai::lucidtech::las::sdk::CreateTransitionOptions.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_create_transition_options)` options)` | Create a transition, calls the POST /transitions endpoint.
`public JSONObject `[`createTransition`]`(`[`TransitionType`](docs/ai::lucidtech::las::sdk::TransitionType.md#enumai_1_1lucidtech_1_1las_1_1sdk_1_1_transition_type)` transitionType)` | Create a transition, calls the POST /transitions endpoint.
`public JSONObject `[`listTransitions`]`(`[`ListTransitionsOptions`](docs/ai::lucidtech::las::sdk::ListTransitionsOptions.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_list_transitions_options)` options)` | List transitions, calls the GET /transitions endpoint.
`public JSONObject `[`listTransitions`]`()` | List transitions, calls the GET /transitions endpoint.
`public JSONObject `[`getTransition`]`(String transitionId)` | Get transition, calls the GET /transitions/{transitionId} endpoint.
`public JSONObject `[`updateTransition`]`(String transitionId,`[`UpdateTransitionOptions`](docs/ai::lucidtech::las::sdk::UpdateTransitionOptions.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_update_transition_options)` options)` | Updates a transition, calls the PATCH /transitions/{transitionId} endpoint.
`public JSONObject `[`executeTransition`]`(String transitionId)` | Start executing a manual transition, calls the POST /transitions/{transitionId}/executions endpoint.
`public JSONObject `[`deleteTransition`]`(String transitionId)` | Delete a transition, calls the DELETE /transitions/{transitionId} endpoint. Will fail if transition is in use by one or more workflows.
`public JSONObject `[`listTransitionExecutions`]`(String transitionId,`[`ListTransitionExecutionsOptions`](docs/ai::lucidtech::las::sdk::ListTransitionExecutionsOptions.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_list_transition_executions_options)` options)` | List executions in a transition, calls the GET /transitions/{transitionId}/executions endpoint.
`public JSONObject `[`listTransitionExecutions`]`(String transitionId)` | List executions in a transition, calls the GET /transitions/{transitionId}/executions endpoint.
`public JSONObject `[`getTransitionExecution`]`(String transitionId,String executionId)` | Get an execution of a transition, calls the GET /transitions/{transitionId}/executions/{executionId} endpoint
`public JSONObject `[`updateTransitionExecution`]`(String transitionId,String executionId,`[`TransitionExecutionStatus`](docs/ai::lucidtech::las::sdk::TransitionExecutionStatus.md#enumai_1_1lucidtech_1_1las_1_1sdk_1_1_transition_execution_status)` status,`[`UpdateTransitionExecutionOptions`](docs/ai::lucidtech::las::sdk::UpdateTransitionExecutionOptions.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_update_transition_execution_options)` options)` | Ends the processing of the transition execution, calls the PATCH /transitions/{transitionId}/executions/{executionId} endpoint.
`public JSONObject `[`sendHeartbeat`]`(String transitionId,String executionId)` | Send heartbeat for a manual execution to signal that we are still working on it. Must be done at minimum once every 60 seconds or the transition execution will time out, calls the POST /transitions/{transitionId}/executions/{executionId}/heartbeats endpoint.
`public JSONObject `[`createUser`]`(String email,`[`CreateUserOptions`](docs/ai::lucidtech::las::sdk::CreateUserOptions.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_create_user_options)` options)` | Create a user, calls the POST /users endpoint.
`public JSONObject `[`createUser`]`(String email)` | Create a user, calls the POST /users endpoint.
`public JSONObject `[`listUsers`]`(`[`ListUsersOptions`](docs/ai::lucidtech::las::sdk::ListUsersOptions.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_list_users_options)` options)` | List users, calls the GET /users endpoint.
`public JSONObject `[`listUsers`]`()` | List users, calls the GET /users endpoint.
`public JSONObject `[`getUser`]`(String userId)` | Get user, calls the GET /users/{userId} endpoint.
`public JSONObject `[`updateUser`]`(String userId,`[`UpdateUserOptions`](docs/ai::lucidtech::las::sdk::UpdateUserOptions.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_update_user_options)` options)` | Updates a user, calls the PATCH /users/{userId} endpoint.
`public JSONObject `[`deleteUser`]`(String userId)` | Delete a user, calls the PATCH /users/{userId} endpoint.
`public JSONObject `[`createWorkflow`]`(JSONObject specification,`[`CreateWorkflowOptions`](docs/ai::lucidtech::las::sdk::CreateWorkflowOptions.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_create_workflow_options)` options)` | Creates a new workflow, calls the POST /workflows endpoint. Check out Lucidtech's tutorials for more info on how to create a workflow. see [https://docs.lucidtech.ai/getting-started/tutorials/setup_predict_and_approve](https://docs.lucidtech.ai/getting-started/tutorials/setup_predict_and_approve)
`public JSONObject `[`createWorkflow`]`(JSONObject specification)` | Creates a new workflow, calls the POST /workflows endpoint. Check out Lucidtech's tutorials for more info on how to create a workflow. see [https://docs.lucidtech.ai/getting-started/tutorials/setup_predict_and_approve](https://docs.lucidtech.ai/getting-started/tutorials/setup_predict_and_approve)
`public JSONObject `[`listWorkflows`]`(`[`ListWorkflowsOptions`](docs/ai::lucidtech::las::sdk::ListWorkflowsOptions.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_list_workflows_options)` options)` | List workflows, calls the GET /workflows endpoint.
`public JSONObject `[`listWorkflows`]`()` | List workflows, calls the GET /workflows endpoint.
`public JSONObject `[`getWorkflow`]`(String workflowId)` | Get workflow, calls the GET /workflows/{workflowId} endpoint.
`public JSONObject `[`updateWorkflow`]`(String workflowId,`[`UpdateWorkflowOptions`](docs/ai::lucidtech::las::sdk::UpdateWorkflowOptions.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_update_workflow_options)` options)` | Update a workflow, calls the PATCH /workflows/{workflowId} endpoint.
`public JSONObject `[`deleteWorkflow`]`(String workflowId)` | Delete a workflow, calls the DELETE /workflows/{workflowId} endpoint.
`public JSONObject `[`executeWorkflow`]`(String workflowId,JSONObject content)` | Start a workflow execution, calls the POST /workflows/{workflowId}/executions endpoint.
`public JSONObject `[`listWorkflowExecutions`]`(String workflowId,`[`ListWorkflowExecutionsOptions`](docs/ai::lucidtech::las::sdk::ListWorkflowExecutionsOptions.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_list_workflow_executions_options)` options)` | List executions in a workflow, calls the GET /workflows/{workflowId}/executions endpoint.
`public JSONObject `[`listWorkflowExecutions`]`(String workflowId)` | List executions in a workflow, calls the GET /workflows/{workflowId}/executions endpoint.
`public JSONObject `[`deleteWorkflowExecution`]`(String workflowId,String executionId)` | Delete execution from workflow, calls the DELETE /workflows/{workflowId}/executions/{executionId} endpoint.

## Members

#### `public  `[`Client`]`(`[`Credentials`](docs/ai::lucidtech::las::sdk::Credentials.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_credentials)` credentials)` 

A client to invoke api methods from Lucidtech AI Services.

#### Parameters
* `credentials` [Credentials](docs/ai::lucidtech::las::sdk::Credentials.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_credentials) to use 

**See also**: [Credentials](docs/ai::lucidtech::las::sdk::Credentials.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_credentials)

#### `public JSONObject `[`createAppClient`]`(`[`CreateAppClientOptions`](docs/ai::lucidtech::las::sdk::CreateAppClientOptions.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_create_app_client_options)` options)` 

Create an app client, calls the POST /appClients endpoint.

**See also**: [CreateAppClientOptions](docs/ai::lucidtech::las::sdk::CreateAppClientOptions.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_create_app_client_options)

#### Parameters
* `options` Additional options to include in request body 

#### Returns
Asset response from API 

#### Exceptions
* `IOException` General IOException 

* `[APIException](docs/ai::lucidtech::las::sdk::APIException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_a_p_i_exception)` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException](docs/ai::lucidtech::las::sdk::MissingAccessTokenException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_missing_access_token_exception)` Raised if access token cannot be obtained

#### `public JSONObject `[`createAppClient`]`()` 

Create an app client, calls the POST /appClients endpoint.

#### Returns
Asset response from API 

#### Exceptions
* `IOException` General IOException 

* `[APIException](docs/ai::lucidtech::las::sdk::APIException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_a_p_i_exception)` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException](docs/ai::lucidtech::las::sdk::MissingAccessTokenException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_missing_access_token_exception)` Raised if access token cannot be obtained

#### `public JSONObject `[`updateAppClient`]`(String appClientId,`[`UpdateAppClientOptions`](docs/ai::lucidtech::las::sdk::UpdateAppClientOptions.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_update_app_client_options)` options)` 

Update an appClient, calls the PATCH /appClients/{appClientId} endpoint.

**See also**: [UpdateAppClientOptions](docs/ai::lucidtech::las::sdk::UpdateAppClientOptions.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_update_app_client_options)

#### Parameters
* `appClientId` Id of the appClient 

* `options` Additional options to include in request body 

#### Returns
AppClient response from REST API 

#### Exceptions
* `IOException` General IOException 

* `[APIException](docs/ai::lucidtech::las::sdk::APIException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_a_p_i_exception)` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException](docs/ai::lucidtech::las::sdk::MissingAccessTokenException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_missing_access_token_exception)` Raised if access token cannot be obtained

#### `public JSONObject `[`listAppClients`]`(`[`ListAppClientsOptions`](docs/ai::lucidtech::las::sdk::ListAppClientsOptions.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_list_app_clients_options)` options)` 

List appClients available, calls the GET /appClients endpoint.

**See also**: [ListAppClientsOptions](docs/ai::lucidtech::las::sdk::ListAppClientsOptions.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_list_app_clients_options)

#### Parameters
* `options` Additional options to pass along as query parameters 

#### Returns
AppClients response from REST API 

#### Exceptions
* `IOException` General IOException 

* `[APIException](docs/ai::lucidtech::las::sdk::APIException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_a_p_i_exception)` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException](docs/ai::lucidtech::las::sdk::MissingAccessTokenException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_missing_access_token_exception)` Raised if access token cannot be obtained

#### `public JSONObject `[`listAppClients`]`()` 

List appClients available, calls the GET /appClients endpoint.

#### Returns
AppClients response from REST API 

#### Exceptions
* `IOException` General IOException 

* `[APIException](docs/ai::lucidtech::las::sdk::APIException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_a_p_i_exception)` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException](docs/ai::lucidtech::las::sdk::MissingAccessTokenException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_missing_access_token_exception)` Raised if access token cannot be obtained

#### `public JSONObject `[`deleteAppClient`]`(String appClientId)` 

Delete an appClient, calls the DELETE /appClients/{appClientId} endpoint.

#### Parameters
* `appClientId` Id of the appClient 

#### Returns
AppClient response from REST API 

#### Exceptions
* `IOException` General IOException 

* `[APIException](docs/ai::lucidtech::las::sdk::APIException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_a_p_i_exception)` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException](docs/ai::lucidtech::las::sdk::MissingAccessTokenException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_missing_access_token_exception)` Raised if access token cannot be obtained

#### `public JSONObject `[`createAsset`]`(byte[] content,`[`CreateAssetOptions`](docs/ai::lucidtech::las::sdk::CreateAssetOptions.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_create_asset_options)` options)` 

Create an asset, calls the POST /assets endpoint.

**See also**: [CreateAssetOptions](docs/ai::lucidtech::las::sdk::CreateAssetOptions.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_create_asset_options)

#### Parameters
* `content` Binary data 

* `options` Additional options to include in request body 

#### Returns
Asset response from API 

#### Exceptions
* `IOException` General IOException 

* `[APIException](docs/ai::lucidtech::las::sdk::APIException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_a_p_i_exception)` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException](docs/ai::lucidtech::las::sdk::MissingAccessTokenException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_missing_access_token_exception)` Raised if access token cannot be obtained

#### `public JSONObject `[`createAsset`]`(InputStream content,`[`CreateAssetOptions`](docs/ai::lucidtech::las::sdk::CreateAssetOptions.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_create_asset_options)` options)` 

Create an asset, calls the POST /assets endpoint.

**See also**: [CreateAssetOptions](docs/ai::lucidtech::las::sdk::CreateAssetOptions.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_create_asset_options)

#### Parameters
* `content` Data from input stream 

* `options` Additional options to include in request body 

#### Returns
Asset response from API 

#### Exceptions
* `IOException` General IOException 

* `[APIException](docs/ai::lucidtech::las::sdk::APIException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_a_p_i_exception)` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException](docs/ai::lucidtech::las::sdk::MissingAccessTokenException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_missing_access_token_exception)` Raised if access token cannot be obtained

#### `public JSONObject `[`createAsset`]`(byte[] content)` 

Create an asset, calls the POST /assets endpoint.

#### Parameters
* `content` Binary data 

#### Returns
Asset response from API 

#### Exceptions
* `IOException` General IOException 

* `[APIException](docs/ai::lucidtech::las::sdk::APIException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_a_p_i_exception)` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException](docs/ai::lucidtech::las::sdk::MissingAccessTokenException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_missing_access_token_exception)` Raised if access token cannot be obtained

#### `public JSONObject `[`createAsset`]`(InputStream content)` 

Create an asset, calls the POST /assets endpoint.

#### Parameters
* `content` Data from input stream 

#### Returns
Asset response from API 

#### Exceptions
* `IOException` General IOException 

* `[APIException](docs/ai::lucidtech::las::sdk::APIException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_a_p_i_exception)` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException](docs/ai::lucidtech::las::sdk::MissingAccessTokenException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_missing_access_token_exception)` Raised if access token cannot be obtained

#### `public JSONObject `[`listAssets`]`(`[`ListAssetsOptions`](docs/ai::lucidtech::las::sdk::ListAssetsOptions.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_list_assets_options)` options)` 

List assets available, calls the GET /assets endpoint.

**See also**: [ListAssetsOptions](docs/ai::lucidtech::las::sdk::ListAssetsOptions.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_list_assets_options)

#### Parameters
* `options` Additional options to pass along as query parameters 

#### Returns
Assets response from REST API 

#### Exceptions
* `IOException` General IOException 

* `[APIException](docs/ai::lucidtech::las::sdk::APIException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_a_p_i_exception)` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException](docs/ai::lucidtech::las::sdk::MissingAccessTokenException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_missing_access_token_exception)` Raised if access token cannot be obtained

#### `public JSONObject `[`listAssets`]`()` 

List assets available, calls the GET /assets endpoint.

#### Returns
Assets response from REST API 

#### Exceptions
* `IOException` General IOException 

* `[APIException](docs/ai::lucidtech::las::sdk::APIException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_a_p_i_exception)` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException](docs/ai::lucidtech::las::sdk::MissingAccessTokenException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_missing_access_token_exception)` Raised if access token cannot be obtained

#### `public JSONObject `[`getAsset`]`(String assetId)` 

Get asset, calls the GET /assets/{assetId} endpoint.

#### Parameters
* `assetId` Id of the asset 

#### Returns
Asset response from REST API 

#### Exceptions
* `IOException` General IOException 

* `[APIException](docs/ai::lucidtech::las::sdk::APIException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_a_p_i_exception)` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException](docs/ai::lucidtech::las::sdk::MissingAccessTokenException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_missing_access_token_exception)` Raised if access token cannot be obtained

#### `public JSONObject `[`updateAsset`]`(String assetId,`[`UpdateAssetOptions`](docs/ai::lucidtech::las::sdk::UpdateAssetOptions.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_update_asset_options)` options)` 

Update an asset, calls the PATCH /assets/{assetId} endpoint.

**See also**: [UpdateAssetOptions](docs/ai::lucidtech::las::sdk::UpdateAssetOptions.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_update_asset_options)

#### Parameters
* `assetId` Id of the asset 

* `options` Additional options to include in request body 

#### Returns
Asset response from REST API 

#### Exceptions
* `IOException` General IOException 

* `[APIException](docs/ai::lucidtech::las::sdk::APIException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_a_p_i_exception)` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException](docs/ai::lucidtech::las::sdk::MissingAccessTokenException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_missing_access_token_exception)` Raised if access token cannot be obtained

#### `public JSONObject `[`deleteAsset`]`(String assetId)` 

Delete an asset, calls the DELETE /assets/{assetId} endpoint.

#### Parameters
* `assetId` Id of the asset 

#### Returns
Asset response from REST API 

#### Exceptions
* `IOException` General IOException 

* `[APIException](docs/ai::lucidtech::las::sdk::APIException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_a_p_i_exception)` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException](docs/ai::lucidtech::las::sdk::MissingAccessTokenException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_missing_access_token_exception)` Raised if access token cannot be obtained

#### `public JSONObject `[`createDocument`]`(byte[] content,`[`ContentType`](docs/ai::lucidtech::las::sdk::ContentType.md#enumai_1_1lucidtech_1_1las_1_1sdk_1_1_content_type)` contentType,`[`CreateDocumentOptions`](docs/ai::lucidtech::las::sdk::CreateDocumentOptions.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_create_document_options)` options)` 

Create a document, calls the POST /documents endpoint.

**See also**: [CreateDocumentOptions](docs/ai::lucidtech::las::sdk::CreateDocumentOptions.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_create_document_options)

#### Parameters
* `content` Binary data 

* `contentType` A mime type for the document 

* `options` Additional options to include in request body 

#### Returns
Document response from REST API 

#### Exceptions
* `IOException` General IOException 

* `[APIException](docs/ai::lucidtech::las::sdk::APIException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_a_p_i_exception)` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException](docs/ai::lucidtech::las::sdk::MissingAccessTokenException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_missing_access_token_exception)` Raised if access token cannot be obtained

#### `public JSONObject `[`createDocument`]`(InputStream content,`[`ContentType`](docs/ai::lucidtech::las::sdk::ContentType.md#enumai_1_1lucidtech_1_1las_1_1sdk_1_1_content_type)` contentType,`[`CreateDocumentOptions`](docs/ai::lucidtech::las::sdk::CreateDocumentOptions.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_create_document_options)` options)` 

Create a document, calls the POST /documents endpoint.

**See also**: [CreateDocumentOptions](docs/ai::lucidtech::las::sdk::CreateDocumentOptions.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_create_document_options)

#### Parameters
* `content` Data from input stream 

* `contentType` A mime type for the document 

* `options` Additional options to include in request body 

#### Returns
Document response from REST API 

#### Exceptions
* `IOException` General IOException 

* `[APIException](docs/ai::lucidtech::las::sdk::APIException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_a_p_i_exception)` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException](docs/ai::lucidtech::las::sdk::MissingAccessTokenException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_missing_access_token_exception)` Raised if access token cannot be obtained

#### `public JSONObject `[`createDocument`]`(InputStream content,`[`ContentType`](docs/ai::lucidtech::las::sdk::ContentType.md#enumai_1_1lucidtech_1_1las_1_1sdk_1_1_content_type)` contentType)` 

Create a document, calls the POST /documents endpoint.

**See also**: [CreateDocumentOptions](docs/ai::lucidtech::las::sdk::CreateDocumentOptions.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_create_document_options)

#### Parameters
* `content` Data from input stream 

* `contentType` A mime type for the document 

#### Returns
Document response from REST API 

#### Exceptions
* `IOException` General IOException 

* `[APIException](docs/ai::lucidtech::las::sdk::APIException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_a_p_i_exception)` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException](docs/ai::lucidtech::las::sdk::MissingAccessTokenException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_missing_access_token_exception)` Raised if access token cannot be obtained

#### `public JSONObject `[`createDocument`]`(byte[] content,`[`ContentType`](docs/ai::lucidtech::las::sdk::ContentType.md#enumai_1_1lucidtech_1_1las_1_1sdk_1_1_content_type)` contentType)` 

Create a document, calls the POST /documents endpoint.

**See also**: [CreateDocumentOptions](docs/ai::lucidtech::las::sdk::CreateDocumentOptions.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_create_document_options)

#### Parameters
* `content` Binary data 

* `contentType` A mime type for the document 

#### Returns
Document response from REST API 

#### Exceptions
* `IOException` General IOException 

* `[APIException](docs/ai::lucidtech::las::sdk::APIException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_a_p_i_exception)` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException](docs/ai::lucidtech::las::sdk::MissingAccessTokenException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_missing_access_token_exception)` Raised if access token cannot be obtained

#### `public JSONObject `[`listDocuments`]`(`[`ListDocumentsOptions`](docs/ai::lucidtech::las::sdk::ListDocumentsOptions.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_list_documents_options)` options)` 

List documents, calls the GET /documents endpoint.

**See also**: [ListDocumentsOptions](docs/ai::lucidtech::las::sdk::ListDocumentsOptions.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_list_documents_options)

#### Parameters
* `options` Additional options to pass along as query parameters 

#### Returns
Documents response from REST API 

#### Exceptions
* `IOException` General IOException 

* `[APIException](docs/ai::lucidtech::las::sdk::APIException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_a_p_i_exception)` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException](docs/ai::lucidtech::las::sdk::MissingAccessTokenException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_missing_access_token_exception)` Raised if access token cannot be obtained

#### `public JSONObject `[`listDocuments`]`()` 

List documents, calls the GET /documents endpoint.

#### Returns
Documents response from REST API 

#### Exceptions
* `IOException` General IOException 

* `[APIException](docs/ai::lucidtech::las::sdk::APIException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_a_p_i_exception)` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException](docs/ai::lucidtech::las::sdk::MissingAccessTokenException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_missing_access_token_exception)` Raised if access token cannot be obtained

#### `public JSONObject `[`deleteDocuments`]`(`[`DeleteDocumentsOptions`](docs/ai::lucidtech::las::sdk::DeleteDocumentsOptions.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_delete_documents_options)` options)` 

Delete documents, calls the DELETE /documents endpoint.

**See also**: [DeleteDocumentsOptions](docs/ai::lucidtech::las::sdk::DeleteDocumentsOptions.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_delete_documents_options)

#### Parameters
* `options` Additional options to pass along as query parameters 

#### Returns
Documents response from REST API 

#### Exceptions
* `IOException` General IOException 

* `[APIException](docs/ai::lucidtech::las::sdk::APIException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_a_p_i_exception)` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException](docs/ai::lucidtech::las::sdk::MissingAccessTokenException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_missing_access_token_exception)` Raised if access token cannot be obtained

#### `public JSONObject `[`deleteDocuments`]`()` 

Delete documents, calls the DELETE /documents endpoint.

**See also**: [Client::createDocument](docs/createDocument.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_client_1a20f4fcce80169d0d9b5444c13c1ef20f)

#### Returns
Documents response from REST API 

#### Exceptions
* `IOException` General IOException 

* `[APIException](docs/ai::lucidtech::las::sdk::APIException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_a_p_i_exception)` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException](docs/ai::lucidtech::las::sdk::MissingAccessTokenException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_missing_access_token_exception)` Raised if access token cannot be obtained

#### `public JSONObject `[`getDocument`]`(String documentId)` 

Get document, calls the GET /documents/{documentId} endpoint.

#### Parameters
* `documentId` Id of the document 

#### Returns
Document response from REST API 

#### Exceptions
* `IOException` General IOException 

* `[APIException](docs/ai::lucidtech::las::sdk::APIException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_a_p_i_exception)` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException](docs/ai::lucidtech::las::sdk::MissingAccessTokenException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_missing_access_token_exception)` Raised if access token cannot be obtained

#### `public JSONObject `[`updateDocument`]`(String documentId,`[`UpdateDocumentOptions`](docs/ai::lucidtech::las::sdk::UpdateDocumentOptions.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_update_document_options)` options)` 

Update document, calls the PATCH /documents/{documentId} endpoint.

**See also**: [Client::createDocument](docs/createDocument.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_client_1a20f4fcce80169d0d9b5444c13c1ef20f)

#### Parameters
* `documentId` The document id to post groundTruth to. 

* `options` Additional options to include in request body 

#### Returns
Document response from REST API 

#### Exceptions
* `IOException` General IOException 

* `[APIException](docs/ai::lucidtech::las::sdk::APIException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_a_p_i_exception)` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException](docs/ai::lucidtech::las::sdk::MissingAccessTokenException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_missing_access_token_exception)` Raised if access token cannot be obtained

#### `public JSONObject `[`getLog`]`(String logId)` 

Get log, calls the GET /logs/{logId} endpoint.

#### Parameters
* `logId` Id of the log 

#### Returns
Log response from REST API 

#### Exceptions
* `IOException` General IOException 

* `[APIException](docs/ai::lucidtech::las::sdk::APIException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_a_p_i_exception)` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException](docs/ai::lucidtech::las::sdk::MissingAccessTokenException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_missing_access_token_exception)` Raised if access token cannot be obtained

#### `public JSONObject `[`listLogs`]`(`[`ListLogsOptions`](docs/ai::lucidtech::las::sdk::ListLogsOptions.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_list_logs_options)` options)` 

List logs, calls the GET /logs endpoint.

**See also**: [ListLogsOptions](docs/ai::lucidtech::las::sdk::ListLogsOptions.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_list_logs_options)

#### Parameters
* `options` Additional options to pass along as query parameters 

#### Returns
Logs response from REST API 

#### Exceptions
* `IOException` General IOException 

* `[APIException](docs/ai::lucidtech::las::sdk::APIException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_a_p_i_exception)` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException](docs/ai::lucidtech::las::sdk::MissingAccessTokenException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_missing_access_token_exception)` Raised if access token cannot be obtained

#### `public JSONObject `[`listLogs`]`()` 

List logs, calls the GET /logs endpoint.

#### Returns
Logs response from REST API 

#### Exceptions
* `IOException` General IOException 

* `[APIException](docs/ai::lucidtech::las::sdk::APIException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_a_p_i_exception)` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException](docs/ai::lucidtech::las::sdk::MissingAccessTokenException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_missing_access_token_exception)` Raised if access token cannot be obtained

#### `public JSONObject `[`createModel`]`(int width,int height,`[`FieldConfig`](docs/ai::lucidtech::las::sdk::FieldConfig.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_field_config)` fieldConfig,`[`CreateModelOptions`](docs/ai::lucidtech::las::sdk::CreateModelOptions.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_create_model_options)` options)` 

Create a model, calls the POST /models endpoint.

**See also**: [CreateModelOptions](docs/ai::lucidtech::las::sdk::CreateModelOptions.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_create_model_options)

**See also**: [FieldConfig](docs/ai::lucidtech::las::sdk::FieldConfig.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_field_config)

#### Parameters
* `width` The number of pixels to be used for the input image width of your model 

* `height` The number of pixels to be used for the input image height of your model 

* `fieldConfig` Specification of the fields that the model is going to predict 

* `options` Additional options to include in request body 

#### Returns
Model response from API 

#### Exceptions
* `IOException` General IOException 

* `[APIException](docs/ai::lucidtech::las::sdk::APIException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_a_p_i_exception)` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException](docs/ai::lucidtech::las::sdk::MissingAccessTokenException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_missing_access_token_exception)` Raised if access token cannot be obtained

#### `public JSONObject `[`createModel`]`(int width,int height,`[`FieldConfig`](docs/ai::lucidtech::las::sdk::FieldConfig.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_field_config)` fieldConfig)` 

Create a model, calls the POST /models endpoint.

**See also**: [FieldConfig](docs/ai::lucidtech::las::sdk::FieldConfig.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_field_config)

#### Parameters
* `width` The number of pixels to be used for the input image width of your model 

* `height` The number of pixels to be used for the input image height of your model 

* `fieldConfig` Specification of the fields that the model is going to predict 

#### Returns
Model response from API 

#### Exceptions
* `IOException` General IOException 

* `[APIException](docs/ai::lucidtech::las::sdk::APIException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_a_p_i_exception)` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException](docs/ai::lucidtech::las::sdk::MissingAccessTokenException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_missing_access_token_exception)` Raised if access token cannot be obtained

#### `public JSONObject `[`updateModel`]`(String modelId,`[`UpdateModelOptions`](docs/ai::lucidtech::las::sdk::UpdateModelOptions.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_update_model_options)` options)` 

Updates a model, calls the PATCH /models/{modelId} endpoint.

**See also**: [UpdateModelOptions](docs/ai::lucidtech::las::sdk::UpdateModelOptions.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_update_model_options)

#### Parameters
* `modelId` Id of the model 

* `options` Additional options to include in request body 

#### Returns
Model response from REST API 

#### Exceptions
* `IOException` General IOException 

* `[APIException](docs/ai::lucidtech::las::sdk::APIException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_a_p_i_exception)` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException](docs/ai::lucidtech::las::sdk::MissingAccessTokenException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_missing_access_token_exception)` Raised if access token cannot be obtained

#### `public JSONObject `[`getModel`]`(String modelId)` 

Get model, calls the GET /models/{modelId} endpoint.

#### Parameters
* `modelId` Id of the model 

#### Returns
Model response from REST API 

#### Exceptions
* `IOException` General IOException 

* `[APIException](docs/ai::lucidtech::las::sdk::APIException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_a_p_i_exception)` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException](docs/ai::lucidtech::las::sdk::MissingAccessTokenException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_missing_access_token_exception)` Raised if access token cannot be obtained

#### `public JSONObject `[`listModels`]`(`[`ListModelsOptions`](docs/ai::lucidtech::las::sdk::ListModelsOptions.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_list_models_options)` options)` 

List models, calls the GET /models endpoint.

**See also**: [ListModelsOptions](docs/ai::lucidtech::las::sdk::ListModelsOptions.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_list_models_options)

#### Parameters
* `options` Additional options to pass along as query parameters 

#### Returns
Models response from REST API 

#### Exceptions
* `IOException` General IOException 

* `[APIException](docs/ai::lucidtech::las::sdk::APIException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_a_p_i_exception)` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException](docs/ai::lucidtech::las::sdk::MissingAccessTokenException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_missing_access_token_exception)` Raised if access token cannot be obtained

#### `public JSONObject `[`listModels`]`()` 

List models available, calls the GET /models endpoint.

#### Returns
Models response from REST API 

#### Exceptions
* `IOException` General IOException 

* `[APIException](docs/ai::lucidtech::las::sdk::APIException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_a_p_i_exception)` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException](docs/ai::lucidtech::las::sdk::MissingAccessTokenException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_missing_access_token_exception)` Raised if access token cannot be obtained

#### `public JSONObject `[`createPrediction`]`(String documentId,String modelId,`[`CreatePredictionOptions`](docs/ai::lucidtech::las::sdk::CreatePredictionOptions.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_create_prediction_options)` options)` 

Create a prediction on a document using specified model, calls the POST /predictions endpoint.

**See also**: [Client::createDocument](docs/createDocument.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_client_1a20f4fcce80169d0d9b5444c13c1ef20f)

**See also**: [CreatePredictionOptions](docs/ai::lucidtech::las::sdk::CreatePredictionOptions.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_create_prediction_options)

#### Parameters
* `documentId` The document id to run inference and create a prediction on. 

* `modelId` The id of the model to use for inference 

* `options` Additional options to include in request body 

#### Returns
Prediction response from REST API 

#### Exceptions
* `IOException` General IOException 

* `[APIException](docs/ai::lucidtech::las::sdk::APIException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_a_p_i_exception)` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException](docs/ai::lucidtech::las::sdk::MissingAccessTokenException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_missing_access_token_exception)` Raised if access token cannot be obtained

#### `public JSONObject `[`createPrediction`]`(String documentId,String modelId)` 

Create a prediction on a document using specified model, calls the POST /predictions endpoint.

**See also**: [Client::createDocument](docs/createDocument.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_client_1a20f4fcce80169d0d9b5444c13c1ef20f)

#### Parameters
* `documentId` The document id to run inference and create a prediction on. 

* `modelId` The id of the model to use for inference 

#### Returns
Prediction response from REST API 

#### Exceptions
* `IOException` General IOException 

* `[APIException](docs/ai::lucidtech::las::sdk::APIException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_a_p_i_exception)` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException](docs/ai::lucidtech::las::sdk::MissingAccessTokenException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_missing_access_token_exception)` Raised if access token cannot be obtained

#### `public JSONObject `[`listPredictions`]`(`[`ListPredictionsOptions`](docs/ai::lucidtech::las::sdk::ListPredictionsOptions.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_list_predictions_options)` options)` 

List predictions available, calls the GET /predictions endpoint.

**See also**: [ListPredictionsOptions](docs/ai::lucidtech::las::sdk::ListPredictionsOptions.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_list_predictions_options)

#### Parameters
* `options` Additional options to pass along as query parameters 

#### Returns
Predictions response from REST API 

#### Exceptions
* `IOException` General IOException 

* `[APIException](docs/ai::lucidtech::las::sdk::APIException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_a_p_i_exception)` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException](docs/ai::lucidtech::las::sdk::MissingAccessTokenException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_missing_access_token_exception)` Raised if access token cannot be obtained

#### `public JSONObject `[`listPredictions`]`()` 

List predictions available, calls the GET /predictions endpoint.

#### Returns
Predictions response from REST API 

#### Exceptions
* `IOException` General IOException 

* `[APIException](docs/ai::lucidtech::las::sdk::APIException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_a_p_i_exception)` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException](docs/ai::lucidtech::las::sdk::MissingAccessTokenException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_missing_access_token_exception)` Raised if access token cannot be obtained

#### `public JSONObject `[`createSecret`]`(JSONObject data,`[`CreateSecretOptions`](docs/ai::lucidtech::las::sdk::CreateSecretOptions.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_create_secret_options)` options)` 

Create secret, calls the POST /secrets endpoint.

**See also**: [CreateSecretOptions](docs/ai::lucidtech::las::sdk::CreateSecretOptions.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_create_secret_options)

#### Parameters
* `data` Key-Value pairs to store secretly 

* `options` Additional options to include in request body 

#### Returns
Secret response from API 

#### Exceptions
* `IOException` General IOException 

* `[APIException](docs/ai::lucidtech::las::sdk::APIException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_a_p_i_exception)` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException](docs/ai::lucidtech::las::sdk::MissingAccessTokenException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_missing_access_token_exception)` Raised if access token cannot be obtained

#### `public JSONObject `[`createSecret`]`(Map< String, String > data,`[`CreateSecretOptions`](docs/ai::lucidtech::las::sdk::CreateSecretOptions.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_create_secret_options)` options)` 

Create a secret, calls the POST /secrets endpoint.

**See also**: [CreateSecretOptions](docs/ai::lucidtech::las::sdk::CreateSecretOptions.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_create_secret_options)

#### Parameters
* `data` Key-Value pairs to store secretly 

* `options` Additional options to include in request body 

#### Returns
Secret response from API 

#### Exceptions
* `IOException` General IOException 

* `[APIException](docs/ai::lucidtech::las::sdk::APIException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_a_p_i_exception)` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException](docs/ai::lucidtech::las::sdk::MissingAccessTokenException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_missing_access_token_exception)` Raised if access token cannot be obtained

#### `public JSONObject `[`createSecret`]`(Map< String, String > data)` 

Create a secret, calls the POST /secrets endpoint.

#### Parameters
* `data` Key-Value pairs to store secretly 

#### Returns
Secret response from API 

#### Exceptions
* `IOException` General IOException 

* `[APIException](docs/ai::lucidtech::las::sdk::APIException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_a_p_i_exception)` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException](docs/ai::lucidtech::las::sdk::MissingAccessTokenException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_missing_access_token_exception)` Raised if access token cannot be obtained

#### `public JSONObject `[`createSecret`]`(JSONObject data)` 

Create a secret, calls the POST /secrets endpoint.

#### Parameters
* `data` Key-Value pairs to store secretly 

#### Returns
Secret response from API 

#### Exceptions
* `IOException` General IOException 

* `[APIException](docs/ai::lucidtech::las::sdk::APIException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_a_p_i_exception)` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException](docs/ai::lucidtech::las::sdk::MissingAccessTokenException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_missing_access_token_exception)` Raised if access token cannot be obtained

#### `public JSONObject `[`listSecrets`]`(`[`ListSecretsOptions`](docs/ai::lucidtech::las::sdk::ListSecretsOptions.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_list_secrets_options)` options)` 

List secrets, calls the GET /secrets endpoint.

**See also**: [ListSecretsOptions](docs/ai::lucidtech::las::sdk::ListSecretsOptions.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_list_secrets_options)

#### Parameters
* `options` Additional options to pass along as query parameters 

#### Returns
Secrets response from REST API 

#### Exceptions
* `IOException` General IOException 

* `[APIException](docs/ai::lucidtech::las::sdk::APIException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_a_p_i_exception)` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException](docs/ai::lucidtech::las::sdk::MissingAccessTokenException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_missing_access_token_exception)` Raised if access token cannot be obtained

#### `public JSONObject `[`listSecrets`]`()` 

List secrets, calls the GET /secrets endpoint.

#### Returns
Secrets response from REST API 

#### Exceptions
* `IOException` General IOException 

* `[APIException](docs/ai::lucidtech::las::sdk::APIException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_a_p_i_exception)` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException](docs/ai::lucidtech::las::sdk::MissingAccessTokenException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_missing_access_token_exception)` Raised if access token cannot be obtained

#### `public JSONObject `[`updateSecret`]`(String secretId,`[`UpdateSecretOptions`](docs/ai::lucidtech::las::sdk::UpdateSecretOptions.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_update_secret_options)` options)` 

Update a secret, calls the PATCH /secrets/{secretId} endpoint.

**See also**: [UpdateSecretOptions](docs/ai::lucidtech::las::sdk::UpdateSecretOptions.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_update_secret_options)

#### Parameters
* `secretId` Id of the secret 

* `options` Additional options to include in request body 

#### Returns
Secret response from REST API 

#### Exceptions
* `IOException` General IOException 

* `[APIException](docs/ai::lucidtech::las::sdk::APIException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_a_p_i_exception)` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException](docs/ai::lucidtech::las::sdk::MissingAccessTokenException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_missing_access_token_exception)` Raised if access token cannot be obtained

#### `public JSONObject `[`deleteSecret`]`(String secretId)` 

Delete a secret, calls the DELETE /secrets/{secretId} endpoint.

#### Parameters
* `secretId` Id of the secret 

#### Returns
Secret response from REST API 

#### Exceptions
* `IOException` General IOException 

* `[APIException](docs/ai::lucidtech::las::sdk::APIException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_a_p_i_exception)` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException](docs/ai::lucidtech::las::sdk::MissingAccessTokenException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_missing_access_token_exception)` Raised if access token cannot be obtained

#### `public JSONObject `[`createTransition`]`(`[`TransitionType`](docs/ai::lucidtech::las::sdk::TransitionType.md#enumai_1_1lucidtech_1_1las_1_1sdk_1_1_transition_type)` transitionType,`[`CreateTransitionOptions`](docs/ai::lucidtech::las::sdk::CreateTransitionOptions.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_create_transition_options)` options)` 

Create a transition, calls the POST /transitions endpoint.

**See also**: [CreateTransitionOptions](docs/ai::lucidtech::las::sdk::CreateTransitionOptions.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_create_transition_options)

**See also**: [TransitionType](docs/ai::lucidtech::las::sdk::TransitionType.md#enumai_1_1lucidtech_1_1las_1_1sdk_1_1_transition_type)

#### Parameters
* `transitionType` Type of transition 

* `options` Additional options to include in request body 

#### Returns
Transition response from API 

#### Exceptions
* `IOException` General IOException 

* `[APIException](docs/ai::lucidtech::las::sdk::APIException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_a_p_i_exception)` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException](docs/ai::lucidtech::las::sdk::MissingAccessTokenException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_missing_access_token_exception)` Raised if access token cannot be obtained

#### `public JSONObject `[`createTransition`]`(`[`TransitionType`](docs/ai::lucidtech::las::sdk::TransitionType.md#enumai_1_1lucidtech_1_1las_1_1sdk_1_1_transition_type)` transitionType)` 

Create a transition, calls the POST /transitions endpoint.

**See also**: [TransitionType](docs/ai::lucidtech::las::sdk::TransitionType.md#enumai_1_1lucidtech_1_1las_1_1sdk_1_1_transition_type)

#### Parameters
* `transitionType` Type of transition 

#### Returns
Transition response from API 

#### Exceptions
* `IOException` General IOException 

* `[APIException](docs/ai::lucidtech::las::sdk::APIException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_a_p_i_exception)` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException](docs/ai::lucidtech::las::sdk::MissingAccessTokenException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_missing_access_token_exception)` Raised if access token cannot be obtained

#### `public JSONObject `[`listTransitions`]`(`[`ListTransitionsOptions`](docs/ai::lucidtech::las::sdk::ListTransitionsOptions.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_list_transitions_options)` options)` 

List transitions, calls the GET /transitions endpoint.

**See also**: [ListTransitionsOptions](docs/ai::lucidtech::las::sdk::ListTransitionsOptions.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_list_transitions_options)

#### Parameters
* `options` Additional options to pass along as query parameters 

#### Returns
Transitions response from REST API 

#### Exceptions
* `IOException` General IOException 

* `[APIException](docs/ai::lucidtech::las::sdk::APIException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_a_p_i_exception)` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException](docs/ai::lucidtech::las::sdk::MissingAccessTokenException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_missing_access_token_exception)` Raised if access token cannot be obtained

#### `public JSONObject `[`listTransitions`]`()` 

List transitions, calls the GET /transitions endpoint.

#### Returns
Transitions response from REST API 

#### Exceptions
* `IOException` General IOException 

* `[APIException](docs/ai::lucidtech::las::sdk::APIException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_a_p_i_exception)` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException](docs/ai::lucidtech::las::sdk::MissingAccessTokenException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_missing_access_token_exception)` Raised if access token cannot be obtained

#### `public JSONObject `[`getTransition`]`(String transitionId)` 

Get transition, calls the GET /transitions/{transitionId} endpoint.

#### Parameters
* `transitionId` Id of the transition 

#### Returns
Transition response from REST API 

#### Exceptions
* `IOException` General IOException 

* `[APIException](docs/ai::lucidtech::las::sdk::APIException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_a_p_i_exception)` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException](docs/ai::lucidtech::las::sdk::MissingAccessTokenException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_missing_access_token_exception)` Raised if access token cannot be obtained

#### `public JSONObject `[`updateTransition`]`(String transitionId,`[`UpdateTransitionOptions`](docs/ai::lucidtech::las::sdk::UpdateTransitionOptions.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_update_transition_options)` options)` 

Updates a transition, calls the PATCH /transitions/{transitionId} endpoint.

**See also**: [UpdateTransitionOptions](docs/ai::lucidtech::las::sdk::UpdateTransitionOptions.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_update_transition_options)

#### Parameters
* `transitionId` Id of the transition 

* `options` Additional options to include in request body 

#### Returns
Transition response from REST API 

#### Exceptions
* `IOException` General IOException 

* `[APIException](docs/ai::lucidtech::las::sdk::APIException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_a_p_i_exception)` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException](docs/ai::lucidtech::las::sdk::MissingAccessTokenException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_missing_access_token_exception)` Raised if access token cannot be obtained

#### `public JSONObject `[`executeTransition`]`(String transitionId)` 

Start executing a manual transition, calls the POST /transitions/{transitionId}/executions endpoint.

#### Parameters
* `transitionId` Id of the transition 

#### Returns
TransitionExecution response from REST API 

#### Exceptions
* `IOException` General IOException 

* `[APIException](docs/ai::lucidtech::las::sdk::APIException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_a_p_i_exception)` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException](docs/ai::lucidtech::las::sdk::MissingAccessTokenException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_missing_access_token_exception)` Raised if access token cannot be obtained

#### `public JSONObject `[`deleteTransition`]`(String transitionId)` 

Delete a transition, calls the DELETE /transitions/{transitionId} endpoint. Will fail if transition is in use by one or more workflows.

#### Parameters
* `transitionId` Id of the transition 

#### Returns
Transition response from REST API 

#### Exceptions
* `IOException` General IOException 

* `[APIException](docs/ai::lucidtech::las::sdk::APIException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_a_p_i_exception)` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException](docs/ai::lucidtech::las::sdk::MissingAccessTokenException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_missing_access_token_exception)` Raised if access token cannot be obtained

#### `public JSONObject `[`listTransitionExecutions`]`(String transitionId,`[`ListTransitionExecutionsOptions`](docs/ai::lucidtech::las::sdk::ListTransitionExecutionsOptions.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_list_transition_executions_options)` options)` 

List executions in a transition, calls the GET /transitions/{transitionId}/executions endpoint.

**See also**: [ListTransitionExecutionsOptions](docs/ai::lucidtech::las::sdk::ListTransitionExecutionsOptions.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_list_transition_executions_options)

#### Parameters
* `transitionId` Id of the transition 

* `options` Additional options to pass along as query parameters 

#### Returns
Transition executions response from REST API 

#### Exceptions
* `IOException` General IOException 

* `[APIException](docs/ai::lucidtech::las::sdk::APIException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_a_p_i_exception)` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException](docs/ai::lucidtech::las::sdk::MissingAccessTokenException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_missing_access_token_exception)` Raised if access token cannot be obtained

#### `public JSONObject `[`listTransitionExecutions`]`(String transitionId)` 

List executions in a transition, calls the GET /transitions/{transitionId}/executions endpoint.

#### Parameters
* `transitionId` Id of the transition 

#### Returns
Transition executions response from REST API 

#### Exceptions
* `IOException` General IOException 

* `[APIException](docs/ai::lucidtech::las::sdk::APIException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_a_p_i_exception)` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException](docs/ai::lucidtech::las::sdk::MissingAccessTokenException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_missing_access_token_exception)` Raised if access token cannot be obtained

#### `public JSONObject `[`getTransitionExecution`]`(String transitionId,String executionId)` 

Get an execution of a transition, calls the GET /transitions/{transitionId}/executions/{executionId} endpoint

#### Parameters
* `transitionId` Id of the transition 

* `executionId` Id of the execution 

#### Returns
TransitionExecution response from REST API 

#### Exceptions
* `IOException` General IOException 

* `[APIException](docs/ai::lucidtech::las::sdk::APIException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_a_p_i_exception)` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException](docs/ai::lucidtech::las::sdk::MissingAccessTokenException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_missing_access_token_exception)` Raised if access token cannot be obtained

#### `public JSONObject `[`updateTransitionExecution`]`(String transitionId,String executionId,`[`TransitionExecutionStatus`](docs/ai::lucidtech::las::sdk::TransitionExecutionStatus.md#enumai_1_1lucidtech_1_1las_1_1sdk_1_1_transition_execution_status)` status,`[`UpdateTransitionExecutionOptions`](docs/ai::lucidtech::las::sdk::UpdateTransitionExecutionOptions.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_update_transition_execution_options)` options)` 

Ends the processing of the transition execution, calls the PATCH /transitions/{transitionId}/executions/{executionId} endpoint.

**See also**: [UpdateTransitionExecutionOptions](docs/ai::lucidtech::las::sdk::UpdateTransitionExecutionOptions.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_update_transition_execution_options)

**See also**: [TransitionExecutionStatus](docs/ai::lucidtech::las::sdk::TransitionExecutionStatus.md#enumai_1_1lucidtech_1_1las_1_1sdk_1_1_transition_execution_status)

#### Parameters
* `transitionId` Id of the transition 

* `executionId` Id of the execution 

* `status` Status of the execution 

* `options` Additional options to include in request body 

#### Returns
Transition response from REST API 

#### Exceptions
* `IOException` General IOException 

* `[APIException](docs/ai::lucidtech::las::sdk::APIException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_a_p_i_exception)` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException](docs/ai::lucidtech::las::sdk::MissingAccessTokenException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_missing_access_token_exception)` Raised if access token cannot be obtained

#### `public JSONObject `[`sendHeartbeat`]`(String transitionId,String executionId)` 

Send heartbeat for a manual execution to signal that we are still working on it. Must be done at minimum once every 60 seconds or the transition execution will time out, calls the POST /transitions/{transitionId}/executions/{executionId}/heartbeats endpoint.

#### Parameters
* `transitionId` Id of the transition 

* `executionId` Id of the execution 

#### Returns
Empty response 

#### Exceptions
* `IOException` General IOException 

* `[APIException](docs/ai::lucidtech::las::sdk::APIException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_a_p_i_exception)` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException](docs/ai::lucidtech::las::sdk::MissingAccessTokenException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_missing_access_token_exception)` Raised if access token cannot be obtained

#### `public JSONObject `[`createUser`]`(String email,`[`CreateUserOptions`](docs/ai::lucidtech::las::sdk::CreateUserOptions.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_create_user_options)` options)` 

Create a user, calls the POST /users endpoint.

**See also**: [CreateUserOptions](docs/ai::lucidtech::las::sdk::CreateUserOptions.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_create_user_options)

#### Parameters
* `email` Email of the new user 

* `options` Additional options to include in request body 

#### Returns
User response from API 

#### Exceptions
* `IOException` General IOException 

* `[APIException](docs/ai::lucidtech::las::sdk::APIException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_a_p_i_exception)` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException](docs/ai::lucidtech::las::sdk::MissingAccessTokenException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_missing_access_token_exception)` Raised if access token cannot be obtained

#### `public JSONObject `[`createUser`]`(String email)` 

Create a user, calls the POST /users endpoint.

#### Parameters
* `email` Email to the new user 

#### Returns
User response from API 

#### Exceptions
* `IOException` General IOException 

* `[APIException](docs/ai::lucidtech::las::sdk::APIException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_a_p_i_exception)` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException](docs/ai::lucidtech::las::sdk::MissingAccessTokenException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_missing_access_token_exception)` Raised if access token cannot be obtained

#### `public JSONObject `[`listUsers`]`(`[`ListUsersOptions`](docs/ai::lucidtech::las::sdk::ListUsersOptions.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_list_users_options)` options)` 

List users, calls the GET /users endpoint.

**See also**: [ListUsersOptions](docs/ai::lucidtech::las::sdk::ListUsersOptions.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_list_users_options)

#### Parameters
* `options` Additional options to pass along as query parameters 

#### Returns
Users response from REST API 

#### Exceptions
* `IOException` General IOException 

* `[APIException](docs/ai::lucidtech::las::sdk::APIException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_a_p_i_exception)` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException](docs/ai::lucidtech::las::sdk::MissingAccessTokenException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_missing_access_token_exception)` Raised if access token cannot be obtained

#### `public JSONObject `[`listUsers`]`()` 

List users, calls the GET /users endpoint.

#### Returns
Users response from REST API 

#### Exceptions
* `IOException` General IOException 

* `[APIException](docs/ai::lucidtech::las::sdk::APIException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_a_p_i_exception)` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException](docs/ai::lucidtech::las::sdk::MissingAccessTokenException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_missing_access_token_exception)` Raised if access token cannot be obtained

#### `public JSONObject `[`getUser`]`(String userId)` 

Get user, calls the GET /users/{userId} endpoint.

#### Parameters
* `userId` Id of user 

#### Returns
User response 

#### Exceptions
* `IOException` General IOException 

* `[APIException](docs/ai::lucidtech::las::sdk::APIException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_a_p_i_exception)` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException](docs/ai::lucidtech::las::sdk::MissingAccessTokenException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_missing_access_token_exception)` Raised if access token cannot be obtained

#### `public JSONObject `[`updateUser`]`(String userId,`[`UpdateUserOptions`](docs/ai::lucidtech::las::sdk::UpdateUserOptions.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_update_user_options)` options)` 

Updates a user, calls the PATCH /users/{userId} endpoint.

**See also**: [UpdateUserOptions](docs/ai::lucidtech::las::sdk::UpdateUserOptions.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_update_user_options)

#### Parameters
* `userId` Id of user 

* `options` Additional options to include in request body 

#### Returns
User response from REST API 

#### Exceptions
* `IOException` General IOException 

* `[APIException](docs/ai::lucidtech::las::sdk::APIException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_a_p_i_exception)` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException](docs/ai::lucidtech::las::sdk::MissingAccessTokenException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_missing_access_token_exception)` Raised if access token cannot be obtained

#### `public JSONObject `[`deleteUser`]`(String userId)` 

Delete a user, calls the PATCH /users/{userId} endpoint.

#### Parameters
* `userId` Id of user 

#### Returns
User response from REST API 

#### Exceptions
* `IOException` General IOException 

* `[APIException](docs/ai::lucidtech::las::sdk::APIException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_a_p_i_exception)` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException](docs/ai::lucidtech::las::sdk::MissingAccessTokenException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_missing_access_token_exception)` Raised if access token cannot be obtained

#### `public JSONObject `[`createWorkflow`]`(JSONObject specification,`[`CreateWorkflowOptions`](docs/ai::lucidtech::las::sdk::CreateWorkflowOptions.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_create_workflow_options)` options)` 

Creates a new workflow, calls the POST /workflows endpoint. Check out Lucidtech's tutorials for more info on how to create a workflow. see [https://docs.lucidtech.ai/getting-started/tutorials/setup_predict_and_approve](https://docs.lucidtech.ai/getting-started/tutorials/setup_predict_and_approve)

**See also**: [CreateWorkflowOptions](docs/ai::lucidtech::las::sdk::CreateWorkflowOptions.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_create_workflow_options)

#### Parameters
* `specification` Specification of the workflow, currently supporting ASL: [https://states-language.net/spec.html](https://states-language.net/spec.html). Check out the tutorials for more information: see [https://docs.lucidtech.ai/getting-started/tutorials/setup_predict_and_approve#creating-the-workflow](https://docs.lucidtech.ai/getting-started/tutorials/setup_predict_and_approve#creating-the-workflow)

* `options` Additional options to include in request body 

#### Returns
Workflow response from API 

#### Exceptions
* `IOException` General IOException 

* `[APIException](docs/ai::lucidtech::las::sdk::APIException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_a_p_i_exception)` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException](docs/ai::lucidtech::las::sdk::MissingAccessTokenException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_missing_access_token_exception)` Raised if access token cannot be obtained

#### `public JSONObject `[`createWorkflow`]`(JSONObject specification)` 

Creates a new workflow, calls the POST /workflows endpoint. Check out Lucidtech's tutorials for more info on how to create a workflow. see [https://docs.lucidtech.ai/getting-started/tutorials/setup_predict_and_approve](https://docs.lucidtech.ai/getting-started/tutorials/setup_predict_and_approve)

#### Parameters
* `specification` Specification of the workflow, currently supporting ASL: [https://states-language.net/spec.html](https://states-language.net/spec.html). Check out the tutorials for more information: see [https://docs.lucidtech.ai/getting-started/tutorials/setup_predict_and_approve#creating-the-workflow](https://docs.lucidtech.ai/getting-started/tutorials/setup_predict_and_approve#creating-the-workflow)

#### Returns
Workflow response from API 

#### Exceptions
* `IOException` General IOException 

* `[APIException](docs/ai::lucidtech::las::sdk::APIException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_a_p_i_exception)` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException](docs/ai::lucidtech::las::sdk::MissingAccessTokenException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_missing_access_token_exception)` Raised if access token cannot be obtained

#### `public JSONObject `[`listWorkflows`]`(`[`ListWorkflowsOptions`](docs/ai::lucidtech::las::sdk::ListWorkflowsOptions.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_list_workflows_options)` options)` 

List workflows, calls the GET /workflows endpoint.

**See also**: [ListWorkflowsOptions](docs/ai::lucidtech::las::sdk::ListWorkflowsOptions.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_list_workflows_options)

#### Parameters
* `options` Additional options to pass along as query parameters 

#### Returns
Workflows response from REST API 

#### Exceptions
* `IOException` General IOException 

* `[APIException](docs/ai::lucidtech::las::sdk::APIException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_a_p_i_exception)` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException](docs/ai::lucidtech::las::sdk::MissingAccessTokenException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_missing_access_token_exception)` Raised if access token cannot be obtained

#### `public JSONObject `[`listWorkflows`]`()` 

List workflows, calls the GET /workflows endpoint.

#### Returns
Workflows response from REST API 

#### Exceptions
* `IOException` General IOException 

* `[APIException](docs/ai::lucidtech::las::sdk::APIException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_a_p_i_exception)` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException](docs/ai::lucidtech::las::sdk::MissingAccessTokenException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_missing_access_token_exception)` Raised if access token cannot be obtained

#### `public JSONObject `[`getWorkflow`]`(String workflowId)` 

Get workflow, calls the GET /workflows/{workflowId} endpoint.

#### Parameters
* `workflowId` Id of the workflow 

#### Returns
Workflow response from REST API 

#### Exceptions
* `IOException` General IOException 

* `[APIException](docs/ai::lucidtech::las::sdk::APIException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_a_p_i_exception)` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException](docs/ai::lucidtech::las::sdk::MissingAccessTokenException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_missing_access_token_exception)` Raised if access token cannot be obtained

#### `public JSONObject `[`updateWorkflow`]`(String workflowId,`[`UpdateWorkflowOptions`](docs/ai::lucidtech::las::sdk::UpdateWorkflowOptions.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_update_workflow_options)` options)` 

Update a workflow, calls the PATCH /workflows/{workflowId} endpoint.

**See also**: [UpdateWorkflowOptions](docs/ai::lucidtech::las::sdk::UpdateWorkflowOptions.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_update_workflow_options)

#### Parameters
* `workflowId` Id of the workflow 

* `options` Additional options to include in request body 

#### Returns
Workflow response from REST API 

#### Exceptions
* `IOException` General IOException 

* `[APIException](docs/ai::lucidtech::las::sdk::APIException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_a_p_i_exception)` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException](docs/ai::lucidtech::las::sdk::MissingAccessTokenException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_missing_access_token_exception)` Raised if access token cannot be obtained

#### `public JSONObject `[`deleteWorkflow`]`(String workflowId)` 

Delete a workflow, calls the DELETE /workflows/{workflowId} endpoint.

**See also**: [Client::createWorkflow](docs/createWorkflow.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_client_1a13d79b4da5daf9385fd83c2f0ed66074)

#### Parameters
* `workflowId` Id of the workflow 

#### Returns
Workflow response from REST API 

#### Exceptions
* `IOException` General IOException 

* `[APIException](docs/ai::lucidtech::las::sdk::APIException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_a_p_i_exception)` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException](docs/ai::lucidtech::las::sdk::MissingAccessTokenException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_missing_access_token_exception)` Raised if access token cannot be obtained

#### `public JSONObject `[`executeWorkflow`]`(String workflowId,JSONObject content)` 

Start a workflow execution, calls the POST /workflows/{workflowId}/executions endpoint.

#### Parameters
* `workflowId` Id of the workflow 

* `content` Input to the first step of the workflow 

#### Returns
WorkflowExecution response from REST API 

#### Exceptions
* `IOException` General IOException 

* `[APIException](docs/ai::lucidtech::las::sdk::APIException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_a_p_i_exception)` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException](docs/ai::lucidtech::las::sdk::MissingAccessTokenException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_missing_access_token_exception)` Raised if access token cannot be obtained

#### `public JSONObject `[`listWorkflowExecutions`]`(String workflowId,`[`ListWorkflowExecutionsOptions`](docs/ai::lucidtech::las::sdk::ListWorkflowExecutionsOptions.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_list_workflow_executions_options)` options)` 

List executions in a workflow, calls the GET /workflows/{workflowId}/executions endpoint.

**See also**: [ListWorkflowExecutionsOptions](docs/ai::lucidtech::las::sdk::ListWorkflowExecutionsOptions.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_list_workflow_executions_options)

#### Parameters
* `workflowId` Id of the workflow 

* `options` Additional options to pass along as query parameters 

#### Returns
Workflow executions response from REST API 

#### Exceptions
* `IOException` General IOException 

* `[APIException](docs/ai::lucidtech::las::sdk::APIException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_a_p_i_exception)` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException](docs/ai::lucidtech::las::sdk::MissingAccessTokenException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_missing_access_token_exception)` Raised if access token cannot be obtained

#### `public JSONObject `[`listWorkflowExecutions`]`(String workflowId)` 

List executions in a workflow, calls the GET /workflows/{workflowId}/executions endpoint.

#### Parameters
* `workflowId` Id of the workflow 

#### Returns
Workflow executions response from REST API 

#### Exceptions
* `IOException` General IOException 

* `[APIException](docs/ai::lucidtech::las::sdk::APIException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_a_p_i_exception)` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException](docs/ai::lucidtech::las::sdk::MissingAccessTokenException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_missing_access_token_exception)` Raised if access token cannot be obtained

#### `public JSONObject `[`deleteWorkflowExecution`]`(String workflowId,String executionId)` 

Delete execution from workflow, calls the DELETE /workflows/{workflowId}/executions/{executionId} endpoint.

**See also**: [Client::executeWorkflow](docs/executeWorkflow.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_client_1af80e370f399feb814fb05fc00583bb8e)

#### Parameters
* `workflowId` Id of the workflow 

* `executionId` Id of the execution 

#### Returns
WorkflowExecution response from REST API 

#### Exceptions
* `IOException` General IOException 

* `[APIException](docs/ai::lucidtech::las::sdk::APIException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_a_p_i_exception)` Raised when API returns an erroneous status code 

* `[MissingAccessTokenException](docs/ai::lucidtech::las::sdk::MissingAccessTokenException.md#classai_1_1lucidtech_1_1las_1_1sdk_1_1_missing_access_token_exception)` Raised if access token cannot be obtained

