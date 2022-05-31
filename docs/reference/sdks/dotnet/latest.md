# Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`namespace `[`Lucidtech::Las`](#a00024) | 
`namespace `[`Lucidtech::Las::Core`](#a00025) | 
`namespace `[`Lucidtech::Las::Utils`](#a00026) | 

# namespace `Lucidtech::Las` 

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`class `[`Lucidtech::Las::Client`](#a00046) | Client to invoke api methods from Lucidtech AI Services.

# class `Lucidtech::Las::Client` 

Client to invoke api methods from Lucidtech AI Services.

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`{property} RestClient `[`RestSharpClient`](#a00046_1a5e59cc310cc0dd101e74a16824f2fa3a) | 
`{property} `[`Credentials`](#a00070)` `[`LasCredentials`](#a00046_1aed1258913a65f014aa0ce4ef63bd6dfe) | 
`public  `[`Client`](#a00046_1a2a95a90e6dfa52e94d3e12a18d583fca)`(`[`Credentials`](#a00070)` credentials)` | Client constructor.
`public  `[`Client`](#a00046_1a0ba3cc00461a4ee4d4a346d9600efa4a)`()` | Client constructor with credentials read from local file.
`public object `[`CreateAppClient`](#a00046_1adbe8e2a3fefe5b6df86771a858de4864)`(bool generateSecret,List< string >? logoutUrls,List< string >? loginUrls,List< string >? callbackUrls,string? defaultLoginUrl,Dictionary< string, string?>? attributes)` | Creates an appClient, calls the POST /appClients endpoint.
`public object `[`ListAppClients`](#a00046_1afdd7a170f2d21b6643b5dcff0effc3d1)`(int? maxResults,string? nextToken)` | List available appClients, calls the GET /appClients endpoint.
`public object `[`UpdateAppClient`](#a00046_1a94257b036dd947a40bb10a243ad0fd53)`(string appClientId,Dictionary< string, string?>? attributes)` | Updates an existing appClient, calls the PATCH /appClients/{appClientId} endpoint.
`public object `[`DeleteAppClient`](#a00046_1acdfd1de4050f19d8cb167b865455ed88)`(string appClientId)` | Delete an appClient, calls the DELETE /appClients/{appClientId} endpoint.
`public object `[`CreateAsset`](#a00046_1afde4b9ed933fd6fc775770af3cd412e1)`(byte[] content,Dictionary< string, string?>? attributes)` | Creates an asset, calls the POST /assets endpoint.
`public object `[`ListAssets`](#a00046_1a3fe859d9bfd3d23d919c708f99141e4f)`(int? maxResults,string? nextToken)` | List available assets, calls the GET /assets endpoint.
`public object `[`GetAsset`](#a00046_1a8e338146001a43c4b0ca59d3f4afb901)`(string assetId)` | Get asset from the REST API, calls the GET /assets/{assetId} endpoint.
`public object `[`UpdateAsset`](#a00046_1a63e88e264995507702cfde3285150eae)`(string assetId,byte?[] content,Dictionary< string, string?>? attributes)` | Updates an asset, calls the PATCH /assets/{assetId} endpoint.
`public object `[`DeleteAsset`](#a00046_1a98d632656a3ecdf936a31d7a5f67ad54)`(string assetId)` | Delete an asset, calls the DELETE /assets/{assetId} endpoint.
`public object `[`CreateDocument`](#a00046_1ae4d0d8142ff3a2caa9b67e9cccdebf91)`(byte[] content,string contentType,string? consentId,List< Dictionary< string, string >>? groundTruth,string? datasetId)` | Creates a document handle, calls the POST /documents endpoint
`public object `[`ListDocuments`](#a00046_1ac62bb08bb19205bddfcb36b07264c9ce)`(string? consentId,int? maxResults,string? nextToken,string? datasetId)` | Get documents from the REST API, calls the GET /documents endpoint.
`public object `[`GetDocument`](#a00046_1a1638a8fd9c03e35934af0c16d05cf90b)`(string documentId)` | Get document from the REST API, calls the GET /documents/{documentId} endpoint.
`public object `[`UpdateDocument`](#a00046_1a1dc913a4653a26fb14622b3537f51141)`(string documentId,List< Dictionary< string, string >>? groundTruth,string? datasetId)` | Update ground truth of the document, calls the POST /documents/{documentId} endpoint. This enables the API to learn from past mistakes.
`public object `[`DeleteDocuments`](#a00046_1a25a8a26259a44104ed70ac0544266873)`(string? consentId,int? maxResults,string? nextToken,string? datasetId,bool deleteAll)` | Delete documents with specified consentId, calls DELETE /documents endpoint.
`public object `[`DeleteDocument`](#a00046_1aafd4deeebea97d6b937dbfe6227cd09d)`(string documentId)` | Delete a document, calls the DELETE /documents/{documentId} endpoint.
`public object `[`CreateDataset`](#a00046_1a5bc08562dca015280bb40201458c0e53)`(string? name,string? description)` | Create a dataset handle, calls the POST /datasets endpoint.
`public object `[`ListDatasets`](#a00046_1a0d2fe04da4566e86f5988c10aba8fee7)`(int? maxResults,string? nextToken)` | List datasets available, calls the GET /datasets endpoint.
`public object `[`UpdateDataset`](#a00046_1abb805616b3c28f137f57a6458dcec18b)`(string datasetId,Dictionary< string, string?>? attributes)` | Updates an existing dataset, calls the PATCH /datasets/{datasetId} endpoint.
`public object `[`DeleteDataset`](#a00046_1a9d124051fdb2024a4623e19e624fa5d7)`(string datasetId,bool deleteDocuments)` | Delete a dataset, calls the DELETE /datasets/{datasetId} endpoint.
`public object `[`CreatePrediction`](#a00046_1a0d5b71553d28eedb6e67afcc388e3039)`(string documentId,string modelId,int? maxPages,bool? autoRotate,string? imageQuality,Dictionary< string, object >? postprocessConfig)` | Run inference and create a prediction, calls the POST /predictions endpoint.
`public object `[`ListPredictions`](#a00046_1aa07c60058c89b9d2464ec8ccd2037a18)`(int? maxResults,string? nextToken)` | List predictions available, calls the GET /predictions endpoint.
`public object `[`ListLogs`](#a00046_1a48c31f9df10d39e5f6303032572c946d)`(string? transitionId,string? transitionExecutionId,string? workflowId,string? workflowExecutionId,int? maxResults,string? nextToken)` | List logs, calls the GET /logs endpoint.
`public object `[`CreateModel`](#a00046_1a46244b6d90855b929dd5c6b8a07cbfef)`(int width,int height,Dictionary< string, object > fieldConfig,Dictionary< string, object >? preprocessConfig,string? name,string? description,Dictionary< string, string?>? attributes)` | Creates a model, calls the POST /models endpoint.
`public object `[`ListModels`](#a00046_1a2a5979f62ac58a13cdd2fce28c174508)`(int? maxResults,string? nextToken)` | List models available, calls the GET /models endpoint.
`public object `[`GetModel`](#a00046_1af9964054bea7041345e16f51063409c7)`(string modelId)` | Get information about a specific model, calls the GET /models/{modelId} endpoint.
`public object `[`UpdateModel`](#a00046_1a5ad7270e6d1de683d5f7eb69b633e58c)`(string modelId,int? width,int? height,Dictionary< string, object >? fieldConfig,Dictionary< string, object >? preprocessConfig,string? name,string? description,string? status,Dictionary< string, string?>? attributes)` | Updates a model, calls the PATCH /models/{modelId} endpoint.
`public object `[`CreateDataBundle`](#a00046_1a854cc016def250aef026cf7cd9e485c0)`(string modelId,List< string > datasetIds,string? name,string? description)` | Create a data bundle handle, calls the POST /models/{modelId}/dataBundles endpoint.
`public object `[`ListDataBundles`](#a00046_1af376709c384dee0bd1dceb8e0a6ce93e)`(string modelId,int? maxResults,string? nextToken)` | List data bundles available, calls the GET /models/{modelId}/dataBundles endpoint.
`public object `[`UpdateDataBundle`](#a00046_1a2d4413c5567aeb21e42f07aa1a09d6d2)`(string modelId,string dataBundleId,Dictionary< string, string?>? attributes)` | Updates an existing data bundle, calls the PATCH /models/{modelId}/dataBundles/{dataBundleId} endpoint.
`public object `[`DeleteDataBundle`](#a00046_1a06fa74f82b181b50a8587fbc5ad08e36)`(string modelId,string dataBundleId)` | Delete a data bundle, calls the DELETE /models/{modelId}/dataBundles/{dataBundleId} endpoint.
`public object `[`CreateSecret`](#a00046_1ac9ee5b8c1cedfd849aa258bccdcd1de9)`(Dictionary< string, string > data,Dictionary< string, string?>? attributes)` | Creates an secret, calls the POST /secrets endpoint.
`public object `[`ListSecrets`](#a00046_1a4bf28ad750cf50ad0f6e0d8a3558f69f)`(int? maxResults,string? nextToken)` | List secrets available, calls the GET /secrets endpoint.
`public object `[`UpdateSecret`](#a00046_1a881282cf8a8cc3618b25a25c64c7feeb)`(string secretId,Dictionary< string, string >? data,Dictionary< string, string?>? attributes)` | Updates a secret, calls the PATCH /secrets/secretId endpoint.
`public object `[`DeleteSecret`](#a00046_1af74cb1bf2068af164bdc42acc033f012)`(string secretId)` | Delete a secret, calls the DELETE /secrets/{secretId} endpoint.
`public object `[`CreateTransition`](#a00046_1a5b96f5977dd3041a45770692e81a9d45)`(string transitionType,Dictionary< string, string >? inputJsonSchema,Dictionary< string, string >? outputJsonSchema,Dictionary< string, object?>? parameters,Dictionary< string, string?>? attributes)` | Creates a transition, calls the POST /transitions endpoint.
`public object `[`ListTransitions`](#a00046_1a7ecc9e71192ea2432b7efc410119477d)`(string? transitionType,int? maxResults,string? nextToken)` | List transitions, calls the GET /transitions endpoint.
`public object `[`GetTransition`](#a00046_1a56a0e83c4b6b97cbd1c59486a71343df)`(string transitionId)` | Get information about a specific transition, calls the GET /transitions/{transition_id} endpoint.
`public object `[`DeleteTransition`](#a00046_1aaf07d945d2519bd09cd48779d6d9fd27)`(string transitionId)` | Delete a transition, calls the DELETE /transitions/{transition_id} endpoint. Will fail if transition is in use by one or more workflows.
`public object `[`GetTransitionExecution`](#a00046_1a88ae688b39cf43c94052f76afa77fd99)`(string transitionId,string executionId)` | Get an execution of a transition, calls the GET /transitions/{transitionId}/executions/{executionId} endpoint
`public object `[`UpdateTransition`](#a00046_1a6ea482ad0644c6f8dd65b926a8b0d563)`(string transitionId,Dictionary< string, string >? inputJsonSchema,Dictionary< string, string >? outputJsonSchema,Dictionary< string, string >? assets,Dictionary< string, string >? environment,List< string >? environmentSecrets,Dictionary< string, string?> attributes)` | Updates an existing transition, calls the PATCH /transitions/{transitionId} endpoint.
`public object `[`ExecuteTransition`](#a00046_1a4e071632c9d31b235242e5de961bfb79)`(string transitionId)` | Start executing a manual transition, calls the POST /transitions/{transitionId}/executions endpoint.
`public object `[`ListTransitionExecutions`](#a00046_1af972fa3f12663bdc445c79f5a5e61257)`(string transitionId,string? status,List< string >? executionIds,int? maxResults,string? nextToken,string? sortBy,string? order)` | List executions in a transition, calls the GET /transitions/{transitionId}/executions endpoint.
`public object `[`ListTransitionExecutions`](#a00046_1af764a1fbd83178bf38db12f79decfdc2)`(string transitionId,List< string >? statuses,List< string >? executionIds,int? maxResults,string? nextToken,string? sortBy,string? order)` | List executions in a transition, calls the GET /transitions/{transitionId}/executions endpoint.
`public object `[`UpdateTransitionExecution`](#a00046_1a030d1ea9aa66afecd8a7e711ccbb0ef5)`(string transitionId,string executionId,string status,Dictionary< string, string >? output,Dictionary< string, string >? error,DateTime? startTime)` | Ends the processing of the transition execution, calls the PATCH /transitions/{transitionId}/executions/{executionId} endpoint.
`public object `[`SendHeartbeat`](#a00046_1a4d93ff7210887e14489f679963e38d25)`(string transitionId,string executionId)` | Send heartbeat for a manual execution, calls the POST /transitions/{transitionId}/executions/{executionId}/heartbeats endpoint.
`public object `[`CreateUser`](#a00046_1aa8b132ac281a0619bc1154a328bf8168)`(string email,Dictionary< string, string?>? attributes)` | Creates a new user, calls the POST /users endpoint.
`public object `[`ListUsers`](#a00046_1af3b5f1ae1ad592ed1891641c418506fd)`(int? maxResults,string? nextToken)` | List users, calls the GET /users endpoint.
`public object `[`GetUser`](#a00046_1adfa785e09a46221c1603483a5e646142)`(string userId)` | Get information about a specific user, calls the GET /users/{user_id} endpoint.
`public object `[`DeleteUser`](#a00046_1af045ddf4f025869ac32e393f8b6f52cb)`(string userId)` | Delete the user with the provided user_id, calls the DELETE /users/{userId} endpoint.
`public object `[`UpdateUser`](#a00046_1aa4a3d7f47f150f04c6552953dd6ceb90)`(string userId,Dictionary< string, object?> attributes)` | Updates a user, calls the PATCH /users/{userId} endpoint.
`public object `[`CreateWorkflow`](#a00046_1afb39b183ec5d50eca5686a2365803a21)`(Dictionary< string, object > specification,Dictionary< string, object >? errorConfig,Dictionary< string, object >? completedConfig,Dictionary< string, string?>? attributes)` | Creates a new workflow, calls the POST /workflows endpoint. Check out Lucidtech's tutorials for more info on how to create a workflow.
`public object `[`ListWorkflows`](#a00046_1a7938e99f5187033a817155e104d14641)`(int? maxResults,string nextToken)` | List workflows, calls the GET /workflows endpoint.
`public object `[`UpdateWorkflow`](#a00046_1af1be9d558960f0a159d042344cb2986b)`(string workflowId,Dictionary< string, object >? errorConfig,Dictionary< string, object >? completedConfig,Dictionary< string, string?> attributes)` | Creates a workflow handle, calls the PATCH /workflows/{workflowId} endpoint.
`public object `[`GetWorkflow`](#a00046_1ae3a74c1ee4ab596c0b72f5e3c82c0262)`(string workflowId)` | Get information about a specific workflow, calls the GET /workflows/{workflow_id} endpoint.
`public object `[`DeleteWorkflow`](#a00046_1aba8230db99366b8ede332149e8cb3473)`(string workflowId)` | Delete the workflow with the provided workflow_id, calls the DELETE /workflows/{workflowId} endpoint.
`public object `[`ExecuteWorkflow`](#a00046_1ae85ba2f8addcba40182b0ac7cce0443d)`(string workflowId,Dictionary< string, object > content)` | Start a workflow execution, calls the POST /workflows/{workflowId}/executions endpoint.
`public object `[`ListWorkflowExecutions`](#a00046_1ac2605a8e1b3cb18a76727146e3b5cb7c)`(string workflowId,string? status,int? maxResults,string? nextToken,string? sortBy,string? order)` | List executions in a workflow, calls the GET /workflows/{workflowId}/executions endpoint.
`public object `[`ListWorkflowExecutions`](#a00046_1a5c70fbfaa071dd68cd01a50d18aa99a3)`(string workflowId,List< string >? statuses,int? maxResults,string? nextToken,string? sortBy,string? order)` | List executions in a workflow, calls the GET /workflows/{workflowId}/executions endpoint.
`public object `[`GetWorkflowExecution`](#a00046_1a191edfca62f034eee423be5bcd11b4ab)`(string workflowId,string executionId)` | Get an execution of a workflow, calls the GET /workflows/{workflowId}/executions/{executionId} endpoint
`public object `[`UpdateWorkflowExecution`](#a00046_1a92ef9943044ebf642be2254eacd2611a)`(string workflowId,string executionId,string nextTransitionId)` | Retry or end the processing of a workflow execution, calls the PATCH /workflows/{workflowId}/executions/{executionId} endpoint.
`public object `[`DeleteWorkflowExecution`](#a00046_1a294ae39590c80ff6b48cb0881eaef5ac)`(string workflowId,string executionId)` | Deletes the execution with the provided execution_id from workflow_id, calls the DELETE /workflows/{workflowId}/executions/{executionId} endpoint.

## Members

#### `{property} RestClient `[`RestSharpClient`](#a00046_1a5e59cc310cc0dd101e74a16824f2fa3a) 

#### `{property} `[`Credentials`](#a00070)` `[`LasCredentials`](#a00046_1aed1258913a65f014aa0ce4ef63bd6dfe) 

#### `public  `[`Client`](#a00046_1a2a95a90e6dfa52e94d3e12a18d583fca)`(`[`Credentials`](#a00070)` credentials)` 

Client constructor.

#### Parameters
* `credentials` Keys, endpoints and credentials needed for authorization

#### `public  `[`Client`](#a00046_1a0ba3cc00461a4ee4d4a346d9600efa4a)`()` 

Client constructor with credentials read from local file.

#### `public object `[`CreateAppClient`](#a00046_1adbe8e2a3fefe5b6df86771a858de4864)`(bool generateSecret,List< string >? logoutUrls,List< string >? loginUrls,List< string >? callbackUrls,string? defaultLoginUrl,Dictionary< string, string?>? attributes)` 

Creates an appClient, calls the POST /appClients endpoint.

#### Parameters
* `generateSecret` Set to false to ceate a Public app client, default: true

* `logoutUrls` List of logout urls

* `callbackUrls` List of callback urls

* `loginUrls` List of login urls

* `defaultLoginUrl` default login url

* `attributes` Additional attributes

#### Returns
AppClient response from REST API

#### `public object `[`ListAppClients`](#a00046_1afdd7a170f2d21b6643b5dcff0effc3d1)`(int? maxResults,string? nextToken)` 

List available appClients, calls the GET /appClients endpoint.

```cpp
var response = client.ListAppClients();
```

#### Parameters
* `maxResults` Number of items to show on a single page

* `nextToken` Token to retrieve the next page

#### Returns
JSON object with two keys:

* "appClients" AppClients response from REST API without the content of each appClient

* "nextToken" allowing for retrieving the next portion of data

#### `public object `[`UpdateAppClient`](#a00046_1a94257b036dd947a40bb10a243ad0fd53)`(string appClientId,Dictionary< string, string?>? attributes)` 

Updates an existing appClient, calls the PATCH /appClients/{appClientId} endpoint.

#### Parameters
* `appClientId` Id of the appClient

* `attributes` Additional attributes

#### Returns
AppClient response from REST API

#### `public object `[`DeleteAppClient`](#a00046_1acdfd1de4050f19d8cb167b865455ed88)`(string appClientId)` 

Delete an appClient, calls the DELETE /appClients/{appClientId} endpoint.

` var response = client.DeleteAppClient("&lt;appClientId&gt;"); `

#### Parameters
* `appClientId` Id of the appClient

#### Returns
AppClient response from REST API

#### `public object `[`CreateAsset`](#a00046_1afde4b9ed933fd6fc775770af3cd412e1)`(byte[] content,Dictionary< string, string?>? attributes)` 

Creates an asset, calls the POST /assets endpoint.

```cpp
byte[] content = File.ReadAllBytes("myScript.js");
client.CreateAsset(content);
```

#### Parameters
* `content` Asset content

* `attributes` Additional attributes

#### Returns
Asset response from REST API

#### `public object `[`ListAssets`](#a00046_1a3fe859d9bfd3d23d919c708f99141e4f)`(int? maxResults,string? nextToken)` 

List available assets, calls the GET /assets endpoint.

```cpp
var response = client.ListAssets();
```

#### Parameters
* `maxResults` Number of items to show on a single page

* `nextToken` Token to retrieve the next page

#### Returns
JSON object with two keys:

* "assets" Assets response from REST API without the content of each asset

* "nextToken" allowing for retrieving the next portion of data

#### `public object `[`GetAsset`](#a00046_1a8e338146001a43c4b0ca59d3f4afb901)`(string assetId)` 

Get asset from the REST API, calls the GET /assets/{assetId} endpoint.

```cpp
var response = client.GetAsset("<asset_id>");
```

#### Parameters
* `assetId` Asset ID

#### Returns
Asset object

#### `public object `[`UpdateAsset`](#a00046_1a63e88e264995507702cfde3285150eae)`(string assetId,byte?[] content,Dictionary< string, string?>? attributes)` 

Updates an asset, calls the PATCH /assets/{assetId} endpoint.

```cpp
byte[] newContent = File.ReadAllBytes("MyScript.js");
var response = client.UpdateAsset("<asset_id>", newContent);
```

#### Parameters
* `assetId` Asset ID

* `content` New content

* `attributes` Additional attributes

#### Returns
Asset object

#### `public object `[`DeleteAsset`](#a00046_1a98d632656a3ecdf936a31d7a5f67ad54)`(string assetId)` 

Delete an asset, calls the DELETE /assets/{assetId} endpoint.

` var response = client.DeleteAsset("&lt;assetId&gt;"); `

#### Parameters
* `assetId` Id of the asset

#### Returns
Asset response from REST API

#### `public object `[`CreateDocument`](#a00046_1ae4d0d8142ff3a2caa9b67e9cccdebf91)`(byte[] content,string contentType,string? consentId,List< Dictionary< string, string >>? groundTruth,string? datasetId)` 

Creates a document handle, calls the POST /documents endpoint

#### Parameters
* `content` Content to POST 

* `contentType` A mime type for the document handle 

* `consentId` An identifier to mark the owner of the document handle 

* `datasetId` Specifies the dataset to which the document will be associated with 

* `groundTruth` A list of items {label: value}, representing the ground truth values for the document 

#### Returns
A deserialized object that can be interpreted as a Dictionary with the fields with documentId, contentType and consentId

#### `public object `[`ListDocuments`](#a00046_1ac62bb08bb19205bddfcb36b07264c9ce)`(string? consentId,int? maxResults,string? nextToken,string? datasetId)` 

Get documents from the REST API, calls the GET /documents endpoint.

Create a document handle for a jpeg image 
```cpp
var response = client.ListDocuments('<datasetId>');
```

#### Parameters
* `consentId` An identifier to mark the owner of the document handle 

* `datasetId` The dataset id that contains the documents of interest 

* `maxResults` Number of items to show on a single page

* `nextToken` Token to retrieve the next page

#### Returns
Documents from REST API

#### `public object `[`GetDocument`](#a00046_1a1638a8fd9c03e35934af0c16d05cf90b)`(string documentId)` 

Get document from the REST API, calls the GET /documents/{documentId} endpoint.

Get information of document specified by documentId 
```cpp
var response = client.GetDocument('<documentId>');
```

#### Parameters
* `documentId` The document id to run inference and create a prediction on 

#### Returns
Document information from REST API

#### `public object `[`UpdateDocument`](#a00046_1a1dc913a4653a26fb14622b3537f51141)`(string documentId,List< Dictionary< string, string >>? groundTruth,string? datasetId)` 

Update ground truth of the document, calls the POST /documents/{documentId} endpoint. This enables the API to learn from past mistakes.

#### Parameters
* `documentId` Path to document to upload, Same as provided to [CreateDocument](#a00046_1ae4d0d8142ff3a2caa9b67e9cccdebf91)

* `groundTruth` A list of ground truth items 

* `datasetId` change or add the documents datasetId 

#### Returns
A deserialized object that can be interpreted as a Dictionary with the fields documentId, consentId, uploadUrl, contentType and ground truth.

#### `public object `[`DeleteDocuments`](#a00046_1a25a8a26259a44104ed70ac0544266873)`(string? consentId,int? maxResults,string? nextToken,string? datasetId,bool deleteAll)` 

Delete documents with specified consentId, calls DELETE /documents endpoint.

```cpp
var response = client.DeleteConsent('<consentId>');
```

#### Parameters
* `consentId` Delete documents with provided consentId 

* `datasetId` Delete documents with provided datasetId 

* `maxResults` Maximum number of items to delete

* `nextToken` Token to retrieve the next page

#### Returns
A deserialized object that can be interpreted as a Dictionary with the fields consentId, nextToken and documents

#### `public object `[`DeleteDocument`](#a00046_1aafd4deeebea97d6b937dbfe6227cd09d)`(string documentId)` 

Delete a document, calls the DELETE /documents/{documentId} endpoint.

#### Parameters
* `documentId` Id of the document

#### Returns
Document response from REST API

#### `public object `[`CreateDataset`](#a00046_1a5bc08562dca015280bb40201458c0e53)`(string? name,string? description)` 

Create a dataset handle, calls the POST /datasets endpoint.

Create a new dataset with the provided description. on the document specified by datasetId 
```cpp
var response = client.CreateDataset("Data gathered from the Mars Rover Invoice Scan Mission");
```

#### Parameters
* `name` Name of the dataset

* `description` A brief description of the dataset 

#### Returns
A deserialized object that can be interpreted as a Dictionary with the fields datasetId and description. datasetId can be used as an input when posting documents to make them a part of this dataset.

#### `public object `[`ListDatasets`](#a00046_1a0d2fe04da4566e86f5988c10aba8fee7)`(int? maxResults,string? nextToken)` 

List datasets available, calls the GET /datasets endpoint.

```cpp
var response = client.ListDatasets();
```

#### Parameters
* `maxResults` Number of items to show on a single page

* `nextToken` Token to retrieve the next page

#### Returns
JSON object with two keys:

* "datasets" which contains a list of Dataset objects

* "nextToken" allowing for retrieving the next portion of data

#### `public object `[`UpdateDataset`](#a00046_1abb805616b3c28f137f57a6458dcec18b)`(string datasetId,Dictionary< string, string?>? attributes)` 

Updates an existing dataset, calls the PATCH /datasets/{datasetId} endpoint.

#### Parameters
* `datasetId` Id of the dataset

* `attributes` Additional attributes

#### Returns
Dataset response from REST API

#### `public object `[`DeleteDataset`](#a00046_1a9d124051fdb2024a4623e19e624fa5d7)`(string datasetId,bool deleteDocuments)` 

Delete a dataset, calls the DELETE /datasets/{datasetId} endpoint.

` var response = client.DeleteDataset("&lt;datasetId&gt;"); `

#### Parameters
* `datasetId` Id of the dataset

* `deleteDocuments` Set to true to delete documents in dataset before deleting dataset

#### Returns
Dataset response from REST API

#### `public object `[`CreatePrediction`](#a00046_1a0d5b71553d28eedb6e67afcc388e3039)`(string documentId,string modelId,int? maxPages,bool? autoRotate,string? imageQuality,Dictionary< string, object >? postprocessConfig)` 

Run inference and create a prediction, calls the POST /predictions endpoint.

Run inference and create a prediction using the invoice model on the document specified by documentId 
```cpp
var response = client.CreatePrediction('<documentId>',"las:model:99cac468f7cf47ddad12e5e017540389");
```

#### Parameters
* `documentId` Path to document to upload Same as provided to [CreateDocument](#a00046_1ae4d0d8142ff3a2caa9b67e9cccdebf91)

* `modelId` Id of the model to use for inference 

* `maxPages` Maximum number of pages to run predictions on 

* `autoRotate` Whether or not to let the API try different rotations on the document when running 

* `extras` Extra information to add to json body 

#### Returns
A deserialized object that can be interpreted as a Dictionary with the fields documentId and predictions, the value of predictions is the output from the model.

#### `public object `[`ListPredictions`](#a00046_1aa07c60058c89b9d2464ec8ccd2037a18)`(int? maxResults,string? nextToken)` 

List predictions available, calls the GET /predictions endpoint.

```cpp
var response = client.ListPredictions();
```

#### Parameters
* `maxResults` Number of items to show on a single page

* `nextToken` Token to retrieve the next page

#### Returns
JSON object with two keys:

* "predictions" which contains a list of Prediction objects

* "nextToken" allowing for retrieving the next portion of data

#### `public object `[`ListLogs`](#a00046_1a48c31f9df10d39e5f6303032572c946d)`(string? transitionId,string? transitionExecutionId,string? workflowId,string? workflowExecutionId,int? maxResults,string? nextToken)` 

List logs, calls the GET /logs endpoint.

```cpp
var response = client.ListLogs();
```

#### Parameters
* `transitionId` Only show logs from this transition

* `transitionExecutionId` Only show logs from this transition execution

* `workflowId` Only show logs from this workflow

* `workflowExecutionId` Only show logs from this workflow execution

* `maxResults` Number of items to show on a single page

* `nextToken` Token to retrieve the next page

#### Returns
Logs response from REST API

#### `public object `[`CreateModel`](#a00046_1a46244b6d90855b929dd5c6b8a07cbfef)`(int width,int height,Dictionary< string, object > fieldConfig,Dictionary< string, object >? preprocessConfig,string? name,string? description,Dictionary< string, string?>? attributes)` 

Creates a model, calls the POST /models endpoint.

#### Parameters
* `width` The number of pixels to be used for the input image width of your model

* `height` The number of pixels to be used for the input image height of your model

* `fieldConfig` Specification of the fields that the model is going to predict

* `preprocessConfig` Specification of the processing steps prior to the prediction of an image

* `name` Name of the model

* `description` Description of the model

* `attributes` Additional attributes

#### Returns
Model response from REST API

#### `public object `[`ListModels`](#a00046_1a2a5979f62ac58a13cdd2fce28c174508)`(int? maxResults,string? nextToken)` 

List models available, calls the GET /models endpoint.

```cpp
var response = client.ListModels();
```

#### Parameters
* `maxResults` Number of items to show on a single page

* `nextToken` Token to retrieve the next page

#### Returns
JSON object with two keys:

* "models" which contains a list of Prediction objects

* "nextToken" allowing for retrieving the next portion of data

#### `public object `[`GetModel`](#a00046_1af9964054bea7041345e16f51063409c7)`(string modelId)` 

Get information about a specific model, calls the GET /models/{modelId} endpoint.

#### Parameters
* `modelId` Id of the model

#### Returns
Model response from REST API

#### `public object `[`UpdateModel`](#a00046_1a5ad7270e6d1de683d5f7eb69b633e58c)`(string modelId,int? width,int? height,Dictionary< string, object >? fieldConfig,Dictionary< string, object >? preprocessConfig,string? name,string? description,string? status,Dictionary< string, string?>? attributes)` 

Updates a model, calls the PATCH /models/{modelId} endpoint.

#### Parameters
* `modelId` Id of the model

* `width` The number of pixels to be used for the input image width of your model

* `height` The number of pixels to be used for the input image height of your model

* `fieldConfig` Specification of the fields that the model is going to predict

* `preprocessConfig` Specification of the processing steps prior to the prediction of an image

* `name` Name of the model

* `description` Description of the model

* `status` New status for the model

* `attributes` Additional attributes

#### Returns
Model response from REST API

#### `public object `[`CreateDataBundle`](#a00046_1a854cc016def250aef026cf7cd9e485c0)`(string modelId,List< string > datasetIds,string? name,string? description)` 

Create a data bundle handle, calls the POST /models/{modelId}/dataBundles endpoint.

#### Parameters
* `modelId` Id of the model 

* `datasetIds` List of Dataset Ids that will be included in the data bundle 
#### Parameters
* `name` Name of the data bundle

* `description` A brief description of the data bundle 

#### Returns
Data Bundle response from REST API

#### `public object `[`ListDataBundles`](#a00046_1af376709c384dee0bd1dceb8e0a6ce93e)`(string modelId,int? maxResults,string? nextToken)` 

List data bundles available, calls the GET /models/{modelId}/dataBundles endpoint.

#### Parameters
* `modelId` Id of the model

* `maxResults` Number of items to show on a single page

* `nextToken` Token to retrieve the next page

#### Returns
JSON object with two keys:

* "dataBundles" which contains a list of data bundle objects

* "nextToken" allowing for retrieving the next portion of data

#### `public object `[`UpdateDataBundle`](#a00046_1a2d4413c5567aeb21e42f07aa1a09d6d2)`(string modelId,string dataBundleId,Dictionary< string, string?>? attributes)` 

Updates an existing data bundle, calls the PATCH /models/{modelId}/dataBundles/{dataBundleId} endpoint.

#### Parameters
* `modelId` Id of the model

* `dataBundleId` Id of the data bundle

* `attributes` Additional attributes

#### Returns
Data Bundle response from REST API

#### `public object `[`DeleteDataBundle`](#a00046_1a06fa74f82b181b50a8587fbc5ad08e36)`(string modelId,string dataBundleId)` 

Delete a data bundle, calls the DELETE /models/{modelId}/dataBundles/{dataBundleId} endpoint.

#### Parameters
* `modelId` Id of the model

* `dataBundleId` Id of the data bundle

#### Returns
Data Bundle response from REST API

#### `public object `[`CreateSecret`](#a00046_1ac9ee5b8c1cedfd849aa258bccdcd1de9)`(Dictionary< string, string > data,Dictionary< string, string?>? attributes)` 

Creates an secret, calls the POST /secrets endpoint.

```cpp
var data = new Dictionary<string, string>{
    {"key", "my_secret_value"}
}
var response = client.CreateSecret(data);
```

#### Parameters
* `data` A dictionary containing values to be hidden

* `attributes` Additional attributes

#### Returns
A Secret object

#### `public object `[`ListSecrets`](#a00046_1a4bf28ad750cf50ad0f6e0d8a3558f69f)`(int? maxResults,string? nextToken)` 

List secrets available, calls the GET /secrets endpoint.

```cpp
var response = client.ListSecrets();
```

#### Parameters
* `maxResults` Number of items to show on a single page

* `nextToken` Token to retrieve the next page

#### Returns
JSON object with two keys:

* "secrets" which contains a list of Prediction objects

* "nextToken" allowing for retrieving the next portion of data

#### `public object `[`UpdateSecret`](#a00046_1a881282cf8a8cc3618b25a25c64c7feeb)`(string secretId,Dictionary< string, string >? data,Dictionary< string, string?>? attributes)` 

Updates a secret, calls the PATCH /secrets/secretId endpoint.

```cpp
var data = new Dictionary<string, string>{
    {"key", "my_new_secret_value"}
}
var response = client.UpdateSecret("<secretId>", data);
```

#### Parameters
* `secretId` Secret ID

* `data` New data

* `attributes` Additional attributes

#### `public object `[`DeleteSecret`](#a00046_1af74cb1bf2068af164bdc42acc033f012)`(string secretId)` 

Delete a secret, calls the DELETE /secrets/{secretId} endpoint.

` var response = client.DeleteSecret("&lt;secretId&gt;"); `

#### Parameters
* `secretId` Id of the secret

#### Returns
Secret response from REST API

#### `public object `[`CreateTransition`](#a00046_1a5b96f5977dd3041a45770692e81a9d45)`(string transitionType,Dictionary< string, string >? inputJsonSchema,Dictionary< string, string >? outputJsonSchema,Dictionary< string, object?>? parameters,Dictionary< string, string?>? attributes)` 

Creates a transition, calls the POST /transitions endpoint.

```cpp
var inputSchema = new Dictionary<string, string>{
    {"$schema", "https://json-schema.org/draft-04/schema#"},
    {"title", "input"}
};
var outputSchema = new Dictionary<string, string>{
    {"$schema", "https://json-schema/draft-04/schema#"},
    {"title", "output"}
};
var params = new Dictionary<string, object>{
    {"imageUrl", "<image_url>"},
    {"credentials", new Dictionary<string, string>{
        {"username", "<username>"},
        {"password", "<password>"}
    }
};
var response = client.CreateTransition("<transition_type>", inputSchema, outputSchema, parameters: params);
```

#### Parameters
* `transitionType` Type of transition: "docker"|"manual"

* `inputJsonSchema` Json-schema that defines the input to the transition

* `outputJsonSchema` Json-schema that defines the output of the transition

* `parameters` Parameters to the corresponding transition type

* `attributes` Additional attributes

#### Returns
Transition response from REST API

#### `public object `[`ListTransitions`](#a00046_1a7ecc9e71192ea2432b7efc410119477d)`(string? transitionType,int? maxResults,string? nextToken)` 

List transitions, calls the GET /transitions endpoint.

```cpp
var response = client.ListTransitions();
```

#### Parameters
* `transitionType` Type of transitions

* `maxResults` Number of items to show on a single page

* `nextToken` Token to retrieve the next page

#### Returns
Transitions response from REST API

#### `public object `[`GetTransition`](#a00046_1a56a0e83c4b6b97cbd1c59486a71343df)`(string transitionId)` 

Get information about a specific transition, calls the GET /transitions/{transition_id} endpoint.

```cpp
var response = client.GetTransition("<transition_id>");
```

#### Parameters
* `transitionId` Id of the transition

#### Returns
Transition response from REST API

#### `public object `[`DeleteTransition`](#a00046_1aaf07d945d2519bd09cd48779d6d9fd27)`(string transitionId)` 

Delete a transition, calls the DELETE /transitions/{transition_id} endpoint. Will fail if transition is in use by one or more workflows.

```cpp
var response = client.DeleteTransition("<transition_id>");
```

#### Parameters
* `transitionId` Id of the transition

#### Returns
Transition response from REST API

#### `public object `[`GetTransitionExecution`](#a00046_1a88ae688b39cf43c94052f76afa77fd99)`(string transitionId,string executionId)` 

Get an execution of a transition, calls the GET /transitions/{transitionId}/executions/{executionId} endpoint

```cpp
var response = client.GetTransitionExecution("<transition_id>", "<execution_id>");
```

#### Parameters
* `transitionId` Id of the transition

* `executionId` Id of the execution

#### Returns
Transition execution response from REST API

#### `public object `[`UpdateTransition`](#a00046_1a6ea482ad0644c6f8dd65b926a8b0d563)`(string transitionId,Dictionary< string, string >? inputJsonSchema,Dictionary< string, string >? outputJsonSchema,Dictionary< string, string >? assets,Dictionary< string, string >? environment,List< string >? environmentSecrets,Dictionary< string, string?> attributes)` 

Updates an existing transition, calls the PATCH /transitions/{transitionId} endpoint.

```cpp
var response = client.UpdateTransition("<transitionId>");
```

#### Parameters
* `transitionId` Id of the transition

* `inputJsonSchema` Json-schema that defines the input to the transition

* `outputJsonSchema` Json-schema that defines the output of the transition

* `attributes` Additional attributes

#### Returns
Transition response from REST API

#### `public object `[`ExecuteTransition`](#a00046_1a4e071632c9d31b235242e5de961bfb79)`(string transitionId)` 

Start executing a manual transition, calls the POST /transitions/{transitionId}/executions endpoint.

```cpp
var response = client.ExecuteTransition("<transitionId>");
```

#### Parameters
* `transitionId` Id of the transition

#### Returns
Transition exexution response from REST API

#### `public object `[`ListTransitionExecutions`](#a00046_1af972fa3f12663bdc445c79f5a5e61257)`(string transitionId,string? status,List< string >? executionIds,int? maxResults,string? nextToken,string? sortBy,string? order)` 

List executions in a transition, calls the GET /transitions/{transitionId}/executions endpoint.

```cpp
var response = client.ListTransitionExecutions("<transitionId>", new [] {"succeeded", "failed"});
```

#### Parameters
* `transitionId` Id of the transition

* `status` Status to filter by

* `executionIds` List of execution ids to filter by

* `maxResults` Maximum number of results to be returned

* `nextToken` A unique token used to retrieve the next page

* `sortBy` The sorting variable of the execution: "endTime" | "startTime"

* `order` Order of the executions: "ascending" | "descending"

#### Returns
Transition executions response from the REST API

#### `public object `[`ListTransitionExecutions`](#a00046_1af764a1fbd83178bf38db12f79decfdc2)`(string transitionId,List< string >? statuses,List< string >? executionIds,int? maxResults,string? nextToken,string? sortBy,string? order)` 

List executions in a transition, calls the GET /transitions/{transitionId}/executions endpoint.

```cpp
var response = client.ListTransitionExecutions("<transitionId>", new [] {"succeeded", "failed"});
```

#### Parameters
* `transitionId` Id of the transition

* `statuses` List of execution statuses to filter by

* `executionIds` List of execution ids to filter by

* `maxResults` Maximum number of results to be returned

* `nextToken` A unique token used to retrieve the next page

* `sortBy` The sorting variable of the execution: "endTime" | "startTime"

* `order` Order of the executions: "ascending" | "descending"

#### Returns
Transition executions response from the REST API

#### `public object `[`UpdateTransitionExecution`](#a00046_1a030d1ea9aa66afecd8a7e711ccbb0ef5)`(string transitionId,string executionId,string status,Dictionary< string, string >? output,Dictionary< string, string >? error,DateTime? startTime)` 

Ends the processing of the transition execution, calls the PATCH /transitions/{transitionId}/executions/{executionId} endpoint.

```cpp
var output = new Dictionary<string, string>();
client.UpdateTransitionExecution("<transitionId>", "<executionId>, "succeeded", output: output);
```

#### Parameters
* `transitionId` Id of the transition

* `executionId` Id of the execution

* `status` Status of the execution: "succeeded" | "failed"

* `output` Output from the execution, required when status is "succeeded"

* `error` Error from the execution, required when status is "failed"

* `startTime` Utc start time that will replace the original start time of the execution

#### Returns
Transition execution response from REST API

#### `public object `[`SendHeartbeat`](#a00046_1a4d93ff7210887e14489f679963e38d25)`(string transitionId,string executionId)` 

Send heartbeat for a manual execution, calls the POST /transitions/{transitionId}/executions/{executionId}/heartbeats endpoint.

```cpp
var response = client.sendHeartbeat("<transitionId>", "<executionId>");
```

#### Parameters
* `transitionId` Id of the transition

* `executionId` Id of the execution

#### Returns
Transition exexution response from REST API

#### `public object `[`CreateUser`](#a00046_1aa8b132ac281a0619bc1154a328bf8168)`(string email,Dictionary< string, string?>? attributes)` 

Creates a new user, calls the POST /users endpoint.

```cpp
var response = client.CreateUser("foo@bar.com");
```

#### Parameters
* `email` New user's email

* `attributes` Additional attributes. Currently supported are: name, avatar

#### Returns
User response from REST API

#### `public object `[`ListUsers`](#a00046_1af3b5f1ae1ad592ed1891641c418506fd)`(int? maxResults,string? nextToken)` 

List users, calls the GET /users endpoint.

```cpp
var response = client.ListUsers();
```

#### Parameters
* `maxResults` Maximum number of results to be returned

* `nextToken` A unique token used to retrieve the next page

#### Returns
Users response from REST API

#### `public object `[`GetUser`](#a00046_1adfa785e09a46221c1603483a5e646142)`(string userId)` 

Get information about a specific user, calls the GET /users/{user_id} endpoint.

```cpp
var response = client.GetUser("<user_id>");
```

#### Parameters
* `userId` Id of the user

#### Returns
User response from REST API

#### `public object `[`DeleteUser`](#a00046_1af045ddf4f025869ac32e393f8b6f52cb)`(string userId)` 

Delete the user with the provided user_id, calls the DELETE /users/{userId} endpoint.

```cpp
var response = client.DeleteUser("<user_id>");
```

#### Parameters
* `userId` Id of the user

#### Returns
User response from REST API

#### `public object `[`UpdateUser`](#a00046_1aa4a3d7f47f150f04c6552953dd6ceb90)`(string userId,Dictionary< string, object?> attributes)` 

Updates a user, calls the PATCH /users/{userId} endpoint.

```cpp
var parameters = new Dictionary<string, string>{
    {"name", "User"}
};
var response = client.UpdateUser("<user_id>", parameters);
```

#### Parameters
* `userId` Id of the user

* `attributes` Attributes to update. Allowed attributes: name (string), avatar (base64-encoded image) 

#### Returns
User response from REST API

#### `public object `[`CreateWorkflow`](#a00046_1afb39b183ec5d50eca5686a2365803a21)`(Dictionary< string, object > specification,Dictionary< string, object >? errorConfig,Dictionary< string, object >? completedConfig,Dictionary< string, string?>? attributes)` 

Creates a new workflow, calls the POST /workflows endpoint. Check out Lucidtech's tutorials for more info on how to create a workflow.

```cpp
var specification = new Dictionary<string, object>{
    {"language", "ASL"},
    {"version", "1.0.0"},
    {"definition", {...}}
};
var environmentSecrets = new List<string>{ "las:secret:<hex-uuid>" };
var env = new Dictionary<string, string>{{"FOO", "BAR"}};
var completedConfig = new Dictionary<string, object>{
    {"imageUrl", "my/docker:image"},
    {"secretId", secretId},
    {"environment", env},
    {"environmentSecrets", environmentSecrets}
};
var errorConfig = new Dictionary<string, object>{
    {"email", "foo@example.com"},
    {"manualRetry", true}
};
var parameters = new Dictionary<string, string?>{
    {"name", name},
    {"description", description}
};
var response = Toby.CreateWorkflow(spec, errorConfig, completedConfig, parameters);
```

#### Parameters
* `specification` Workflow specification. Currently only ASL is supported: [https://states-language.net/spec.html](https://states-language.net/spec.html)

* `errorConfig` Error handler configuration

* `completedConfig` Configuration of a job to run whenever a workflow execution ends

* `attributes` Additional attributes. Currently supported are: name, description.

#### Returns
Workflow response from REST API

#### `public object `[`ListWorkflows`](#a00046_1a7938e99f5187033a817155e104d14641)`(int? maxResults,string nextToken)` 

List workflows, calls the GET /workflows endpoint.

```cpp
var response = client.ListWorkflows();
```

#### Parameters
* `maxResults` Maximum number of results to be returned

* `nextToken` A unique token used to retrieve the next page

#### Returns
Workflows response from REST API

#### `public object `[`UpdateWorkflow`](#a00046_1af1be9d558960f0a159d042344cb2986b)`(string workflowId,Dictionary< string, object >? errorConfig,Dictionary< string, object >? completedConfig,Dictionary< string, string?> attributes)` 

Creates a workflow handle, calls the PATCH /workflows/{workflowId} endpoint.

```cpp
var newParameters = new Dictionary<string, string>{
    {"name", "New Name"},
    {"description", "My updated awesome workflow"}
};
var response = client.UpdateWorkflow("<workflow_id>, newParameters);
```

#### Parameters
* `workflowId` Id of the workflow

* `attributes` Attributes to update. Currently supported are: name, description

#### Returns
Workflow response from REST API

#### `public object `[`GetWorkflow`](#a00046_1ae3a74c1ee4ab596c0b72f5e3c82c0262)`(string workflowId)` 

Get information about a specific workflow, calls the GET /workflows/{workflow_id} endpoint.

```cpp
var response = client.GetWorkflow("<workflow_id>");
```

#### Parameters
* `workflowId` Id of the workflow

#### Returns
Workflow response from REST API

#### `public object `[`DeleteWorkflow`](#a00046_1aba8230db99366b8ede332149e8cb3473)`(string workflowId)` 

Delete the workflow with the provided workflow_id, calls the DELETE /workflows/{workflowId} endpoint.

```cpp
var response = client.DeleteWorkflow("<workflow_id>");
```

#### Parameters
* `workflowId` Id of the workflow

#### Returns
Workflow response from REST API

#### `public object `[`ExecuteWorkflow`](#a00046_1ae85ba2f8addcba40182b0ac7cce0443d)`(string workflowId,Dictionary< string, object > content)` 

Start a workflow execution, calls the POST /workflows/{workflowId}/executions endpoint.

```cpp
var content = new Dictionary<string, object>();
var response = client.ExecuteWorkflow("<workflowId>, content);
```

#### Parameters
* `workflowId` Id of the workflow

* `content` Input to the first step of the workflow

#### Returns
Workflow execution response from REST API

#### `public object `[`ListWorkflowExecutions`](#a00046_1ac2605a8e1b3cb18a76727146e3b5cb7c)`(string workflowId,string? status,int? maxResults,string? nextToken,string? sortBy,string? order)` 

List executions in a workflow, calls the GET /workflows/{workflowId}/executions endpoint.

```cpp
var statuses = new [] {"running", "succeeded"};
var response = client.ListWorkflowExecutions("<workflow_id>", statuses);
```

#### Parameters
* `workflowId` Id of the workflow

* `status` Workflow execution status to filter by

* `maxResults` Maximum number of results to be returned

* `nextToken` A unique token used to retrieve the next page

* `sortBy` The sorting variable of the execution: "endTime" | "startTime"

* `order` Order of the executions: "ascending" | "descending"

#### Returns
WorkflowExecutions response from REST API

#### `public object `[`ListWorkflowExecutions`](#a00046_1a5c70fbfaa071dd68cd01a50d18aa99a3)`(string workflowId,List< string >? statuses,int? maxResults,string? nextToken,string? sortBy,string? order)` 

List executions in a workflow, calls the GET /workflows/{workflowId}/executions endpoint.

```cpp
var statuses = new [] {"running", "succeeded"};
var response = client.ListWorkflowExecutions("<workflow_id>", statuses);
```

#### Parameters
* `workflowId` Id of the workflow

* `statuses` Workflow execution statuses to filter by

* `maxResults` Maximum number of results to be returned

* `nextToken` A unique token used to retrieve the next page

* `sortBy` The sorting variable of the execution: "endTime" | "startTime"

* `order` Order of the executions: "ascending" | "descending"

#### Returns
WorkflowExecutions response from REST API

#### `public object `[`GetWorkflowExecution`](#a00046_1a191edfca62f034eee423be5bcd11b4ab)`(string workflowId,string executionId)` 

Get an execution of a workflow, calls the GET /workflows/{workflowId}/executions/{executionId} endpoint

```cpp
var response = client.GetWorkflowExecution("<workflow_id>", "<execution_id>");
```

#### Parameters
* `workflowId` Id of the workflow

* `executionId` Id of the execution

#### Returns
Workflow execution response from REST API

#### `public object `[`UpdateWorkflowExecution`](#a00046_1a92ef9943044ebf642be2254eacd2611a)`(string workflowId,string executionId,string nextTransitionId)` 

Retry or end the processing of a workflow execution, calls the PATCH /workflows/{workflowId}/executions/{executionId} endpoint.

```cpp
var response = client.UpdateWorkflowExecution("<workflow_id>", "<execution_id>", "<next_transition_id>");
```

#### Parameters
* `workflowId` Id of the workflow

* `executionId` Id of the execution

* `nextTransitionId` The next transition to transition into, to end the workflow-execution, use: las:transition:commons-failed

#### Returns
WorkflowExecution response from REST API

#### `public object `[`DeleteWorkflowExecution`](#a00046_1a294ae39590c80ff6b48cb0881eaef5ac)`(string workflowId,string executionId)` 

Deletes the execution with the provided execution_id from workflow_id, calls the DELETE /workflows/{workflowId}/executions/{executionId} endpoint.

```cpp
var response = client.DeleteWorkflowExecution("<workflow_id>", "<execution_id>");
```

#### Parameters
* `workflowId` Id of the workflow

* `executionId` Id of the execution

#### Returns
WorkflowExecution response from REST API

# namespace `Lucidtech::Las::Core` 

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`class `[`Lucidtech::Las::Core::ClientException`](#a00050) | A ClientException is raised if the client refuses to send request due to incorrect usage or bad request data.
`class `[`Lucidtech::Las::Core::Credentials`](#a00070) | Used to fetch and store credentials. One of 3 conditions must be met to successfully create credentials.
`class `[`Lucidtech::Las::Core::FeedbackResponse`](#a00082) | The structured format of the response from a send feedback request.
`class `[`Lucidtech::Las::Core::InvalidCredentialsException`](#a00054) | An InvalidCredentialsException is raised if access key id or secret access key is invalid.
`class `[`Lucidtech::Las::Core::LimitExceededException`](#a00062) | A LimitExceededException is raised if you have reached the limit of total requests per month associated with your credentials.
`class `[`Lucidtech::Las::Core::Prediction`](#a00074) | A class that contains all the necessary information regarding a prediction performed by ApiClient.
`class `[`Lucidtech::Las::Core::RequestException`](#a00066) | A RequestException is raised if something went wrong with the request.
`class `[`Lucidtech::Las::Core::RevokeResponse`](#a00078) | The structured format of the response from a revoke consent request.
`class `[`Lucidtech::Las::Core::TooManyRequestsException`](#a00058) | A TooManyRequestsException is raised if you have reached the number of requests per second limit associated with your credentials.

# class `Lucidtech::Las::Core::ClientException` 

```
class Lucidtech::Las::Core::ClientException
  : public Exception
```  

A ClientException is raised if the client refuses to send request due to incorrect usage or bad request data.

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public  `[`ClientException`](#a00050_1adcb7f76b61fa3b414e4e71ceaca9fdad)`(string s)` | 

## Members

#### `public  `[`ClientException`](#a00050_1adcb7f76b61fa3b414e4e71ceaca9fdad)`(string s)` 

# class `Lucidtech::Las::Core::Credentials` 

Used to fetch and store credentials. One of 3 conditions must be met to successfully create credentials.

* ClientId, ClientSecret, AuthEndpoint and ApiEndpoint are provided

* The path to the file where the credentials are stored is provided

* Credentials are located in default path ~/.lucidtech/credentials.cfg

Get credentials by contacting [hello@lucidtech.ai](mailto:hello@lucidtech.ai)

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`{property} string `[`ClientId`](#a00070_1a597f4891d6f0fe9ed9f04e7aae21608f) | Client ID. Provided by Lucidtech.
`{property} string `[`ClientSecret`](#a00070_1aec4e817805386c0c3c10e0d3fcd7b565) | Client Secret. Provided by Lucidtech.
`{property} string `[`AuthEndpoint`](#a00070_1aeb48746d4fcd7e93d0ba24aa1dd41659) | AWS Authorization endpoint. Provided by Lucidtech.
`{property} string `[`ApiEndpoint`](#a00070_1a5dc9073eba2810493f73a112d9d076ee) | AWS API Gateway API endpoint. Provided by Lucidtech.
`{property} RestClient `[`RestSharpClient`](#a00070_1a77da9eff9a94f2ac1f03d134d74636f4) | RestClient for making request to the authorization endpoint.
`public string `[`GetAccessToken`](#a00070_1a02857d4f347be1b9481ee23fae2547a8)`()` | Get Access token to API endpoint.
`public  `[`Credentials`](#a00070_1ae1684e3aa6a905cb350958b144f11443)`(string clientId,string clientSecret,string authEndpoint,string apiEndpoint)` | Credentials constructor where ClientId, ClientSecret, AuthEndpoint and ApiEndpoint are provided by Lucidtech.
`public  `[`Credentials`](#a00070_1a6b90bc8b8d133da49e129036886eefd5)`(string credentialsPath)` | Credentials constructor where the path to the credentials config is provided.
`public  `[`Credentials`](#a00070_1aa5fba45758ca0f5651c6e92ebc0250eb)`()` | Credentials constructor where the credentials are located at the default path. ~/.lucidtech/credentials.cfg for linux and USERPROFILE%.lucidtech\credentials.cfg for Windows.
`protected  `[`string`](#a00070_1a276748a80f0a2bc01026b8b45ae6d9cd) | 
`protected virtual void `[`CommonConstructor`](#a00070_1a3ac9a72bb9459b36fb660816cfad1a96)`()` | 

## Members

#### `{property} string `[`ClientId`](#a00070_1a597f4891d6f0fe9ed9f04e7aae21608f) 

Client ID. Provided by Lucidtech.

#### `{property} string `[`ClientSecret`](#a00070_1aec4e817805386c0c3c10e0d3fcd7b565) 

Client Secret. Provided by Lucidtech.

#### `{property} string `[`AuthEndpoint`](#a00070_1aeb48746d4fcd7e93d0ba24aa1dd41659) 

AWS Authorization endpoint. Provided by Lucidtech.

#### `{property} string `[`ApiEndpoint`](#a00070_1a5dc9073eba2810493f73a112d9d076ee) 

AWS API Gateway API endpoint. Provided by Lucidtech.

#### `{property} RestClient `[`RestSharpClient`](#a00070_1a77da9eff9a94f2ac1f03d134d74636f4) 

RestClient for making request to the authorization endpoint.

#### `public string `[`GetAccessToken`](#a00070_1a02857d4f347be1b9481ee23fae2547a8)`()` 

Get Access token to API endpoint.

#### `public  `[`Credentials`](#a00070_1ae1684e3aa6a905cb350958b144f11443)`(string clientId,string clientSecret,string authEndpoint,string apiEndpoint)` 

Credentials constructor where ClientId, ClientSecret, AuthEndpoint and ApiEndpoint are provided by Lucidtech.

#### Parameters
* `clientId` client id 

* `clientSecret` client secret 

* `authEndpoint` Authorization endpoint 

* `apiEndpoint` API endpoint 

#### Exceptions
* `ArgumentException`

#### `public  `[`Credentials`](#a00070_1a6b90bc8b8d133da49e129036886eefd5)`(string credentialsPath)` 

Credentials constructor where the path to the credentials config is provided.

#### Parameters
* `credentialsPath` Path to the file where the credentials are stored

#### `public  `[`Credentials`](#a00070_1aa5fba45758ca0f5651c6e92ebc0250eb)`()` 

Credentials constructor where the credentials are located at the default path. ~/.lucidtech/credentials.cfg for linux and USERPROFILE%.lucidtech\credentials.cfg for Windows.

#### `protected  `[`string`](#a00070_1a276748a80f0a2bc01026b8b45ae6d9cd) 

#### `protected virtual void `[`CommonConstructor`](#a00070_1a3ac9a72bb9459b36fb660816cfad1a96)`()` 

# class `Lucidtech::Las::Core::FeedbackResponse` 

The structured format of the response from a send feedback request.

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`{property} string `[`DocumentId`](#a00082_1a583fa4e93b2e4d42bc87a8de8e1155ae) | Document id
`{property} string `[`ConsentId`](#a00082_1a3cea748b281d1b4d14690c639f4e2ec6) | Consent id
`{property} string `[`ContentType`](#a00082_1a3410256cf5cb1e92bddb635c79590244) | Content type
`{property} List< Dictionary< string, string > > `[`Feedback`](#a00082_1a58bcc016725bbf3cd77d9d9707c8f633) | The same information as was uploaded as feedback.
`public  `[`FeedbackResponse`](#a00082_1a4d8a83b695036d1949218035465561a4)`(object response)` | 
`public string `[`ToJsonString`](#a00082_1ab7ca7a2e4f4362d7ba26a4f111bc7426)`(Formatting format)` | Convert an object of this class to a string ready to be interpreted as a json object.

## Members

#### `{property} string `[`DocumentId`](#a00082_1a583fa4e93b2e4d42bc87a8de8e1155ae) 

Document id

#### `{property} string `[`ConsentId`](#a00082_1a3cea748b281d1b4d14690c639f4e2ec6) 

Consent id

#### `{property} string `[`ContentType`](#a00082_1a3410256cf5cb1e92bddb635c79590244) 

Content type

#### `{property} List< Dictionary< string, string > > `[`Feedback`](#a00082_1a58bcc016725bbf3cd77d9d9707c8f633) 

The same information as was uploaded as feedback.

#### `public  `[`FeedbackResponse`](#a00082_1a4d8a83b695036d1949218035465561a4)`(object response)` 

#### `public string `[`ToJsonString`](#a00082_1ab7ca7a2e4f4362d7ba26a4f111bc7426)`(Formatting format)` 

Convert an object of this class to a string ready to be interpreted as a json object.

#### Parameters
* `format` The format of the string, either `Formatting.None` or `Formatting.Indented`

#### Returns
A string that is formatted as a json object

# class `Lucidtech::Las::Core::InvalidCredentialsException` 

```
class Lucidtech::Las::Core::InvalidCredentialsException
  : public Lucidtech.Las.Core.ClientException
```  

An InvalidCredentialsException is raised if access key id or secret access key is invalid.

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public  `[`InvalidCredentialsException`](#a00054_1a666a601ee2b46cd24f54dc062a228d85)`(string s)` | 

## Members

#### `public  `[`InvalidCredentialsException`](#a00054_1a666a601ee2b46cd24f54dc062a228d85)`(string s)` 

# class `Lucidtech::Las::Core::LimitExceededException` 

```
class Lucidtech::Las::Core::LimitExceededException
  : public Lucidtech.Las.Core.ClientException
```  

A LimitExceededException is raised if you have reached the limit of total requests per month associated with your credentials.

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public  `[`LimitExceededException`](#a00062_1a531eacc7391269340a13d3accebf5d6b)`(string s)` | 

## Members

#### `public  `[`LimitExceededException`](#a00062_1a531eacc7391269340a13d3accebf5d6b)`(string s)` 

# class `Lucidtech::Las::Core::Prediction` 

A class that contains all the necessary information regarding a prediction performed by ApiClient.

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`{property} string `[`ConsentId`](#a00074_1aff35bf96ba266b12fcd51c39f9980398) | Consent id
`{property} string `[`ModelName`](#a00074_1a3e77070cbaf240ad9e83cbc0d8ca0cae) | Upload url
`{property} string `[`DocumentId`](#a00074_1ad4c7eebd91ad8bf95fb920af3720ab45) | Document id
`{property} List< Dictionary< string, object > > `[`Fields`](#a00074_1ad88d7e901b90fcb00f6788bce2cde1ec) | A list of the responses from a prediction
`public  `[`Prediction`](#a00074_1ad2683829a91fd8809e00aeb35c412901)`(string documentId,string consentId,string modelName,List< Dictionary< string, object >> predictionResponse)` | Constructor of s Prediction object
`public string `[`ToJsonString`](#a00074_1a8e22ad69756c2a1d0582d8d6c2dbc9bc)`(Formatting format)` | Convert an object of this class to a string ready to be interpreted as a json object.

## Members

#### `{property} string `[`ConsentId`](#a00074_1aff35bf96ba266b12fcd51c39f9980398) 

Consent id

#### `{property} string `[`ModelName`](#a00074_1a3e77070cbaf240ad9e83cbc0d8ca0cae) 

Upload url

#### `{property} string `[`DocumentId`](#a00074_1ad4c7eebd91ad8bf95fb920af3720ab45) 

Document id

#### `{property} List< Dictionary< string, object > > `[`Fields`](#a00074_1ad88d7e901b90fcb00f6788bce2cde1ec) 

A list of the responses from a prediction

#### `public  `[`Prediction`](#a00074_1ad2683829a91fd8809e00aeb35c412901)`(string documentId,string consentId,string modelName,List< Dictionary< string, object >> predictionResponse)` 

Constructor of s Prediction object

#### Parameters
* `documentId` The id of the document used in the prediction 

* `consentId` The consent id 

* `modelName` The name of the model used 

* `predictionResponse` The response from prediction

#### `public string `[`ToJsonString`](#a00074_1a8e22ad69756c2a1d0582d8d6c2dbc9bc)`(Formatting format)` 

Convert an object of this class to a string ready to be interpreted as a json object.

#### Parameters
* `format` The format of the string, either `Formatting.None` or `Formatting.Indented`

#### Returns
A string that is formatted as a json object

# class `Lucidtech::Las::Core::RequestException` 

```
class Lucidtech::Las::Core::RequestException
  : public Lucidtech.Las.Core.ClientException
```  

A RequestException is raised if something went wrong with the request.

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`{property} IRestResponse `[`Response`](#a00066_1a20b3caf6340de32e418ba8c62ab05b82) | 
`public  `[`RequestException`](#a00066_1a587aab0b41a24b283809e77493870f2a)`(string s)` | 
`public  `[`RequestException`](#a00066_1ac3e3f5ebf0ec4517e27efabdc36c11d6)`(IRestResponse response)` | 

## Members

#### `{property} IRestResponse `[`Response`](#a00066_1a20b3caf6340de32e418ba8c62ab05b82) 

#### `public  `[`RequestException`](#a00066_1a587aab0b41a24b283809e77493870f2a)`(string s)` 

#### `public  `[`RequestException`](#a00066_1ac3e3f5ebf0ec4517e27efabdc36c11d6)`(IRestResponse response)` 

# class `Lucidtech::Las::Core::RevokeResponse` 

The structured format of the response from a revoke consent request.

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`{property} string `[`ConsentId`](#a00078_1a5c9404abd75b168b34bc451e3ee056c2) | The consent Id where documents where deleted.
`{property} List< string > `[`DocumentIds`](#a00078_1aab7c6599db6b09938ad642281f67cebb) | The document Ids of the deleted documents.
`public  `[`RevokeResponse`](#a00078_1a87c59407fc6eb36f9b868c412977970a)`(object deleteConsentResponse)` | 
`public string `[`ToJsonString`](#a00078_1a8b10fa6a2df43e00ea552a0c9814bb70)`(Formatting format)` | Convert an object of this class to a string ready to be interpreted as a json object.

## Members

#### `{property} string `[`ConsentId`](#a00078_1a5c9404abd75b168b34bc451e3ee056c2) 

The consent Id where documents where deleted.

#### `{property} List< string > `[`DocumentIds`](#a00078_1aab7c6599db6b09938ad642281f67cebb) 

The document Ids of the deleted documents.

#### `public  `[`RevokeResponse`](#a00078_1a87c59407fc6eb36f9b868c412977970a)`(object deleteConsentResponse)` 

#### `public string `[`ToJsonString`](#a00078_1a8b10fa6a2df43e00ea552a0c9814bb70)`(Formatting format)` 

Convert an object of this class to a string ready to be interpreted as a json object.

#### Parameters
* `format` The format of the string, either `Formatting.None` or `Formatting.Indented`

#### Returns
A string that is formatted as a json object

# class `Lucidtech::Las::Core::TooManyRequestsException` 

```
class Lucidtech::Las::Core::TooManyRequestsException
  : public Lucidtech.Las.Core.ClientException
```  

A TooManyRequestsException is raised if you have reached the number of requests per second limit associated with your credentials.

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public  `[`TooManyRequestsException`](#a00058_1a405f42f24fd1e1ffffb3609b6ea89bd2)`(string s)` | 

## Members

#### `public  `[`TooManyRequestsException`](#a00058_1a405f42f24fd1e1ffffb3609b6ea89bd2)`(string s)` 

# namespace `Lucidtech::Las::Utils` 

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`class `[`Lucidtech::Las::Utils::FileType`](#a00086) | Help determine the type of a file, inspired by pythons `imghdr.what()`.
`class `[`Lucidtech::Las::Utils::JsonSerialPublisher`](#a00090) | A Json publishes that allows the user to serialize and deserialize back and forth between serialized json objects and deserialized general objects and specific Dictionaries.

# class `Lucidtech::Las::Utils::FileType` 

Help determine the type of a file, inspired by pythons `imghdr.what()`.

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------

## Members

# class `Lucidtech::Las::Utils::JsonSerialPublisher` 

```
class Lucidtech::Las::Utils::JsonSerialPublisher
  : public ISerializer
  : public IDeserializer
```  

A Json publishes that allows the user to serialize and deserialize back and forth between serialized json objects and deserialized general objects and specific Dictionaries.

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`{property} string `[`ContentType`](#a00090_1a4bccd73b0ef7355d9e4013c4dc69ed0e) | 
`public  `[`JsonSerialPublisher`](#a00090_1a4c11e94dba401f14ed1d3315ca17be59)`(Newtonsoft.Json.JsonSerializer serializer)` | 
`public string `[`Serialize`](#a00090_1aabb184cf8d6e6511e7b2a5e34fe259af)`(object obj)` | Serialize a general object.
`public T `[`Deserialize< T >`](#a00090_1a4d40df27e6e8fe372ef4b3a0f14fe85a)`(IRestResponse response)` | Deserialize the content of an IRestResponse.

## Members

#### `{property} string `[`ContentType`](#a00090_1a4bccd73b0ef7355d9e4013c4dc69ed0e) 

#### `public  `[`JsonSerialPublisher`](#a00090_1a4c11e94dba401f14ed1d3315ca17be59)`(Newtonsoft.Json.JsonSerializer serializer)` 

#### `public string `[`Serialize`](#a00090_1aabb184cf8d6e6511e7b2a5e34fe259af)`(object obj)` 

Serialize a general object.

#### Parameters
* `obj` A general object to be serialized 

#### Returns
A string ready to be interpreted as a json file

#### `public T `[`Deserialize< T >`](#a00090_1a4d40df27e6e8fe372ef4b3a0f14fe85a)`(IRestResponse response)` 

Deserialize the content of an IRestResponse.

#### Parameters
* `response` The response from a request performed by ` RestSharp.RestClient `

#### Parameters
* `T` The type of the output, e.g. Dictionary or a List of some sort 

#### Returns
A deserialized object of type *T*

Generated by [Moxygen](https://sourcey.com/moxygen)