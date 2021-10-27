
<a name="readmemd"></a>

# JavaScript SDK for Lucidtech AI Services API

## Installation

#### Browser version
```
$ yarn add @lucidtech/las-sdk-browser
$ npm install @lucidtech/las-sdk-browser
```

#### Node version
```
$ yarn add @lucidtech/las-sdk-node
$ npm install @lucidtech/las-sdk-node
```

## Usage

```javascript
import { Client } from '@lucidtech/las-sdk-core';
import { ClientCredentials } from '@lucidtech/las-sdk-node';
import { readFile } from 'fs/promises'

const fileBuffer = await readFile('...path/file.jpg')

const credentials = new ClientCredentials('<apiEndpoint>', '<clientId>',  '<clientSecret>', '<authEndpoint>');
const client = new Client(credentials);

const documentResponse = await client.createDocument(fileBuffer, 'image/jpeg');
```

## Contributing

Install dependencies
```
$ npm install && npm run upgrade-lucidtech
```

Build
```
$ npm run build
```

Run tests
```
$ npm run test test
```


<a name="classesclientmd"></a>

# Class: Client

A high-level http client for communicating with the Lucidtech REST API

## Constructors

### constructor

• **new Client**(`credentials`)

#### Parameters

 `credentials` [`Credentials`](#classescredentialsmd)



## Properties

### credentials

• **credentials**: [`Credentials`](#classescredentialsmd)



## Methods

### createAppClient

▸ **createAppClient**(`options`): `Promise`<[`AppClient`](#appclient)\>

Creates an app client, calls the POST /appClients endpoint.

#### Parameters

 `options` [`CreateAppClientOptions`](#createappclientoptions)

#### Returns

`Promise`<[`AppClient`](#appclient)\>

AppClient response from REST API



___

### createAsset

▸ **createAsset**(`content`): `Promise`<[`Asset`](#asset)\>

Creates an asset, calls the POST /assets endpoint.

#### Parameters

 `content` `string` Content to POST (base64-encoded string \| Buffer)

#### Returns

`Promise`<[`Asset`](#asset)\>

Asset response from REST API



___

### createBatch

▸ **createBatch**(`options`): `Promise`<[`Batch`](#batch)\>

**`deprecated`** Use the new [Client.createDataset](#createdataset) method instead.
Creates a batch, calls the POST /batches endpoint.

#### Parameters

 `options` [`CreateBatchOptions`](#createbatchoptions)

#### Returns

`Promise`<[`Batch`](#batch)\>

Batch response from REST API



___

### createDataBundle

▸ **createDataBundle**(`modelId`, `datasetIds`, `options`): `Promise`<[`DataBundle`](#databundle)\>

Creates a dataBundle, calls the POST /models/{modelId}/dataBundles endpoint.

#### Parameters

 `modelId` `string` Id of the model to create dataBundle for
 `datasetIds` `string`[] Ids of the datasets to create dataBundle with
 `options` [`CreateDataBundleOptions`](#createdatabundleoptions) -

#### Returns

`Promise`<[`DataBundle`](#databundle)\>

DataBundle response from REST API



___

### createDataset

▸ **createDataset**(`options`): `Promise`<[`Dataset`](#dataset)\>

Creates a dataset, calls the POST /datasets endpoint.

#### Parameters

 `options` [`CreateDatasetOptions`](#createdatasetoptions)

#### Returns

`Promise`<[`Dataset`](#dataset)\>

Dataset response from REST API



___

### createDocument

▸ **createDocument**(`content`, `contentType`, `options?`): `Promise`<`Pick`<[`LasDocument`](#lasdocument), ``"batchId"`` \| ``"consentId"`` \| ``"contentType"`` \| ``"datasetId"`` \| ``"documentId"`` \| ``"groundTruth"`` \| ``"retentionInDays"`` \| ``"createdTime"`` \| ``"updatedTime"`` \| ``"createdBy"`` \| ``"updatedBy"``\>\>

Creates a document, calls the POST /documents endpoint.

#### Parameters

 `content` `string` \| `Buffer` Content to POST (base64 string \| Buffer)
 `contentType` [`ContentType`](#contenttype) MIME type for the document
 `options?` [`CreateDocumentOptions`](#interfacescreatedocumentoptionsmd) -

#### Returns

`Promise`<`Pick`<[`LasDocument`](#lasdocument), ``"batchId"`` \| ``"consentId"`` \| ``"contentType"`` \| ``"datasetId"`` \| ``"documentId"`` \| ``"groundTruth"`` \| ``"retentionInDays"`` \| ``"createdTime"`` \| ``"updatedTime"`` \| ``"createdBy"`` \| ``"updatedBy"``\>\>

Document response from REST API



___

### createModel

▸ **createModel**(`fieldConfig`, `width`, `height`, `options?`): `Promise`<[`Model`](#model)\>

Creates a model, calls the POST /models endpoint.

#### Parameters

 `fieldConfig` `Record`<`string`, [`Field`](#field)\> Specification of the fields that the model is going to predict
 `width` `number` The number of pixels to be used for the input image width of your model
 `height` `number` The number of pixels to be used for the input image height of your model
 `options?` [`CreateModelOptions`](#createmodeloptions) -

#### Returns

`Promise`<[`Model`](#model)\>

Model response from REST API



___

### createPrediction

▸ **createPrediction**(`documentId`, `modelId`, `options?`): `Promise`<[`PredictionResponse`](#predictionresponse)\>

Create a prediction on a document using specified model, calls the POST /predictions endpoint.

#### Parameters

 `documentId` `string` Id of the document to run inference and create a prediction on
 `modelId` `string` Id of the model to use for inference
 `options?` [`CreatePredictionsOptions`](#interfacescreatepredictionsoptionsmd) -

#### Returns

`Promise`<[`PredictionResponse`](#predictionresponse)\>

Predicion response from REST API



___

### createSecret

▸ **createSecret**(`data`, `options?`): `Promise`<[`Secret`](#secret)\>

Creates a secret, calls the POST /secrets endpoint.

#### Parameters

 `data` `Record`<`any`, `any`\> Object containing the data you want to keep secret
 `options?` [`CreateSecretOptions`](#interfacescreatesecretoptionsmd) -

#### Returns

`Promise`<[`Secret`](#secret)\>

Secret response from REST API



___

### createTransition

▸ **createTransition**(`transitionType`, `options?`): `Promise`<[`Transition`](#transition)\>

Creates a transition, calls the POST /transitions endpoint.

#### Parameters

 `transitionType` [`TransitionType`](#transitiontype) Type of transition "docker"\|"manual"
 `options?` [`CreateTransitionOptions`](#interfacescreatetransitionoptionsmd) -

#### Returns

`Promise`<[`Transition`](#transition)\>

Transition response from REST API



___

### createUser

▸ **createUser**(`email`, `data?`): `Promise`<[`User`](#user)\>

Creates a new user, calls the POST /users endpoint.

#### Parameters

 `email` `string` Email to the new user
 `data?` [`CreateUserOptions`](#createuseroptions) -

#### Returns

`Promise`<[`User`](#user)\>

User response from REST API



___

### createWorkflow

▸ **createWorkflow**(`name`, `specification`, `options?`): `Promise`<[`Workflow`](#workflow)\>

Creates a new workflow, calls the POST /workflows endpoint.

#### Parameters

 `name` `string` Name of the workflow
 `specification` [`WorkflowSpecification`](#workflowspecification) Specification of the workflow
 `options?` [`CreateWorkflowOptions`](#createworkflowoptions) -

#### Returns

`Promise`<[`Workflow`](#workflow)\>

Workflow response from REST API



___

### deleteAppClient

▸ **deleteAppClient**(`appClientId`): `Promise`<[`AppClient`](#appclient)\>

Delete the app client, calls the DELETE /appClients/{appClientId} endpoint.

#### Parameters

 `appClientId` `string` of the app client

#### Returns

`Promise`<[`AppClient`](#appclient)\>

AppClient response from REST API



___

### deleteAsset

▸ **deleteAsset**(`assetId`): `Promise`<[`Asset`](#asset)\>

Delete an asset, calls the DELETE /assets/{assetId} endpoint.

#### Parameters

 `assetId` `string` of the app client

#### Returns

`Promise`<[`Asset`](#asset)\>

Asset response from REST API



___

### deleteBatch

▸ **deleteBatch**(`batchId`, `deleteDocuments?`): `Promise`<[`Batch`](#batch)\>

Deletes a batch, calls the DELETE /batches/{batchId} endpoint.

**`deprecated`** Use the new [Client.deleteDataset](#deletedataset) method instead.

#### Parameters

 `batchId` `string` `undefined` Id of the batch
 `deleteDocuments` `boolean` `false` Set to true to delete documents in batch before deleting batch

#### Returns

`Promise`<[`Batch`](#batch)\>

Batch response from REST API



___

### deleteDataBundle

▸ **deleteDataBundle**(`modelId`, `dataBundleId`): `Promise`<[`DataBundle`](#databundle)\>

Delete a dataBundle, calls the DELETE /dataBundles/{dataBundleId} endpoint.

#### Parameters

 `modelId` `string` of the model
 `dataBundleId` `string` of the dataBundle

#### Returns

`Promise`<[`DataBundle`](#databundle)\>

DataBundle response from REST API



___

### deleteDataset

▸ **deleteDataset**(`datasetId`, `deleteDocuments?`): `Promise`<[`Dataset`](#dataset)\>

Deletes a dataset, calls the DELETE /datasets/{datasetId} endpoint.

#### Parameters

 `datasetId` `string` `undefined` Id of the dataset
 `deleteDocuments` `boolean` `false` Set to true to delete documents in dataset before deleting dataset

#### Returns

`Promise`<[`Dataset`](#dataset)\>

Dataset response from REST API



___

### deleteDocument

▸ **deleteDocument**(`documentId`): `Promise`<[`LasDocument`](#lasdocument)\>

Delete an document, calls the DELETE /documents/{documentId} endpoint.

#### Parameters

 `documentId` `string` of the document

#### Returns

`Promise`<[`LasDocument`](#lasdocument)\>

Document response from REST API



___

### deleteDocuments

▸ **deleteDocuments**(`options?`): `Promise`<[`LasDocumentList`](#lasdocumentlist)\>

Delete documents with the provided consentId, calls the DELETE /documents endpoint.
Will delete all documents when no consentId is provided.

#### Parameters

 `options?` [`DeleteDocumentOptions`](#deletedocumentoptions)

#### Returns

`Promise`<[`LasDocumentList`](#lasdocumentlist)\>

Documents response from REST API



___

### deleteModel

▸ **deleteModel**(`modelId`): `Promise`<[`Model`](#model)\>

Delete an model, calls the DELETE /models/{modelId} endpoint.

#### Parameters

 `modelId` `string` of the app client

#### Returns

`Promise`<[`Model`](#model)\>

Model response from REST API



___

### deleteTransition

▸ **deleteTransition**(`transitionId`): `Promise`<[`Transition`](#transition)\>

Delete the transition with the provided transitionId, calls the DELETE /transitions/{transitionId} endpoint.
Will fail if transition is in use by one or more workflows.

#### Parameters

 `transitionId` `string` Id of the transition

#### Returns

`Promise`<[`Transition`](#transition)\>

Transition response from REST API



___

### deleteUser

▸ **deleteUser**(`userId`): `Promise`<[`User`](#user)\>

Delete a user, calls the DELETE /users/{userId} endpoint.

#### Parameters

 `userId` `string` Id of the user

#### Returns

`Promise`<[`User`](#user)\>

User response from REST API



___

### deleteWorkflow

▸ **deleteWorkflow**(`workflowId`): `Promise`<[`Workflow`](#workflow)\>

Delete the workflow with the provided workflowId, calls the DELETE /workflows/{workflowId} endpoint.

#### Parameters

 `workflowId` `string` Id of the workflow

#### Returns

`Promise`<[`Workflow`](#workflow)\>

Workflow response from REST API



___

### deleteWorkflowExecution

▸ **deleteWorkflowExecution**(`workflowId`, `executionId`): `Promise`<[`WorkflowExecution`](#workflowexecution)\>

Deletes the execution with the provided executionId from workflowId,
calls the DELETE /workflows/{workflowId}/executions/{executionId} endpoint.

#### Parameters

 `workflowId` `string` Id of the workflow
 `executionId` `string` Id of the execution

#### Returns

`Promise`<[`WorkflowExecution`](#workflowexecution)\>

WorkflowExecution response from REST API



___

### executeTransition

▸ **executeTransition**(`transitionId`): `Promise`<[`TransitionExecution`](#transitionexecution)\>

Start executing a manual transition, calls the POST /transitions/{transitionId}/executions endpoint.

#### Parameters

 `transitionId` `string` Id of the transition

#### Returns

`Promise`<[`TransitionExecution`](#transitionexecution)\>

Transition execution response from REST API



___

### executeWorkflow

▸ **executeWorkflow**(`workflowId`, `input`): `Promise`<[`WorkflowExecution`](#workflowexecution)\>

Start a workflow execution, calls the POST /workflows/{workflowId}/executions endpoint.

#### Parameters

 `workflowId` `string` Id of the workflow
 `input` `object` Input to the first step of the workflow

#### Returns

`Promise`<[`WorkflowExecution`](#workflowexecution)\>

Workflow execution response from REST API



___

### getAsset

▸ **getAsset**(`assetId`): `Promise`<[`Asset`](#asset)\>

Get asset from the REST API, calls the GET /assets/{assetId} endpoint.

#### Parameters

 `assetId` `string` Id of the asset

#### Returns

`Promise`<[`Asset`](#asset)\>

Asset response from REST API



___

### getDataset

▸ **getDataset**(`datasetId`): `Promise`<[`Dataset`](#dataset)\>

Get dataset from the REST API, calls the GET /datasets/{datasetId} endpoint.

#### Parameters

 `datasetId` `string` Id of the dataset

#### Returns

`Promise`<[`Dataset`](#dataset)\>

Dataset response from REST API



___

### getDocument

▸ **getDocument**(`documentId`): `Promise`<[`LasDocument`](#lasdocument)\>

Get document from the REST API, calls the GET /documents/{documentId} endpoint.

#### Parameters

 `documentId` `string` Id of the document

#### Returns

`Promise`<[`LasDocument`](#lasdocument)\>

Document response from REST API



___

### getLog

▸ **getLog**(`logId`): `Promise`<[`Log`](#log)\>

Get log, calls the GET /logs/{logId} endpoint.

#### Parameters

 `logId` `string` Id of the log

#### Returns

`Promise`<[`Log`](#log)\>

Log response from REST API



___

### getModel

▸ **getModel**(`modelId`): `Promise`<[`Model`](#model)\>

Get model from the REST API, calls the GET /models/{modelId} endpoint.

#### Parameters

 `modelId` `string` Id of the model

#### Returns

`Promise`<[`Model`](#model)\>

Model response from REST API



___

### getOrganization

▸ **getOrganization**(`organizationId`): `Promise`<[`Organization`](#organization)\>

Get organization from the REST API, calls the GET /organizations/{organizationId} endpoint.

#### Parameters

 `organizationId` `string` Id of the organization

#### Returns

`Promise`<[`Organization`](#organization)\>

Organization response from REST API



___

### getTransition

▸ **getTransition**(`transitionId`): `Promise`<[`Transition`](#transition)\>

Get the transition with the provided transitionId, calls the GET /transitions/{transitionId} endpoint.

#### Parameters

 `transitionId` `string` Id of the transition

#### Returns

`Promise`<[`Transition`](#transition)\>

Transition response from REST API



___

### getTransitionExecution

▸ **getTransitionExecution**(`transitionId`, `transitionExecutionId`): `Promise`<[`TransitionExecution`](#transitionexecution)\>

Get an execution of a transition, calls the GET /transitions/{transitionId}/executions/{executionId} endpoint

#### Parameters

 `transitionId` `string` Id of the transition
 `transitionExecutionId` `string` Id of the execution

#### Returns

`Promise`<[`TransitionExecution`](#transitionexecution)\>

Transition execution responses from REST API



___

### getUser

▸ **getUser**(`userId`): `Promise`<[`User`](#user)\>

Get information about a specific user, calls the GET /users/{userId} endpoint.

#### Parameters

 `userId` `string` Id of the user

#### Returns

`Promise`<[`User`](#user)\>

User response from REST API



___

### getWorkflow

▸ **getWorkflow**(`workflowId`): `Promise`<[`Workflow`](#workflow)\>

Get the workflow with the provided workflowId, calls the GET /workflows/{workflowId} endpoint.

#### Parameters

 `workflowId` `string` Id of the workflow

#### Returns

`Promise`<[`Workflow`](#workflow)\>

Workflow response from REST API



___

### getWorkflowExecution

▸ **getWorkflowExecution**(`workflowId`, `executionId`): `Promise`<[`WorkflowExecution`](#workflowexecution)\>

Get a workflow execution, calls the GET /workflows/{workflowId}/executions/{executionId} endpoint.

#### Parameters

 `workflowId` `string` Id of the workflow that performs the execution
 `executionId` `string` Id of the execution to get

#### Returns

`Promise`<[`WorkflowExecution`](#workflowexecution)\>

Workflow execution response from REST API



___

### listAppClients

▸ **listAppClients**(`options?`): `Promise`<[`AppClientList`](#appclientlist)\>

List app clients, calls the GET /appClients endpoint.

#### Parameters

 `options?` [`PaginationOptions`](#interfacespaginationoptionsmd)

#### Returns

`Promise`<[`AppClientList`](#appclientlist)\>

AppClientList response from REST API



___

### listAssets

▸ **listAssets**(`options?`): `Promise`<[`AssetList`](#assetlist)\>

List assets available, calls the GET /assets endpoint.

#### Parameters

 `options?` [`PaginationOptions`](#interfacespaginationoptionsmd)

#### Returns

`Promise`<[`AssetList`](#assetlist)\>

Assets response from REST API without the content of each asset



___

### listBatches

▸ **listBatches**(`options?`): `Promise`<[`BatchList`](#batchlist)\>

List batches, calls the GET /batches endpoint.

**`deprecated`** Use the new [Client.listDatasets](#listdatasets) method instead.

#### Parameters

 `options?` [`PaginationOptions`](#interfacespaginationoptionsmd)

#### Returns

`Promise`<[`BatchList`](#batchlist)\>

BatchList response from REST API



___

### listDataBundles

▸ **listDataBundles**(`modelId`, `options?`): `Promise`<[`DataBundleList`](#databundlelist)\>

List dataBundles available, calls the GET /dataBundles endpoint.

#### Parameters

 `modelId` `string` of the model
 `options?` [`PaginationOptions`](#interfacespaginationoptionsmd) -

#### Returns

`Promise`<[`DataBundleList`](#databundlelist)\>

DataBundles response from REST API



___

### listDatasets

▸ **listDatasets**(`options?`): `Promise`<[`DatasetList`](#datasetlist)\>

List datasets, calls the GET /datasets endpoint.

#### Parameters

 `options?` [`PaginationOptions`](#interfacespaginationoptionsmd)

#### Returns

`Promise`<[`DatasetList`](#datasetlist)\>

DatasetList response from REST API



___

### listDocuments

▸ **listDocuments**(`options?`): `Promise`<[`LasDocumentList`](#lasdocumentlist)\>

List documents available for inference, calls the GET /documents endpoint.

#### Parameters

 `options?` [`ListDocumentsOptions`](#listdocumentsoptions)

#### Returns

`Promise`<[`LasDocumentList`](#lasdocumentlist)\>

Documents response from REST API



___

### listModels

▸ **listModels**(`options?`): `Promise`<[`ModelList`](#modellist)\>

List models available, calls the GET /models endpoint.

#### Parameters

 `options?` [`PaginationOptions`](#interfacespaginationoptionsmd)

#### Returns

`Promise`<[`ModelList`](#modellist)\>

Models response from the REST API



___

### listPredictions

▸ **listPredictions**(`options?`): `Promise`<[`PredictionList`](#predictionlist)\>

#### Parameters

 `options?` [`PaginationOptions`](#interfacespaginationoptionsmd)

#### Returns

`Promise`<[`PredictionList`](#predictionlist)\>



___

### listSecrets

▸ **listSecrets**(`options?`): `Promise`<[`SecretList`](#secretlist)\>

List secrets available, calls the GET /secrets endpoint.

#### Parameters

 `options?` [`PaginationOptions`](#interfacespaginationoptionsmd)

#### Returns

`Promise`<[`SecretList`](#secretlist)\>

Secrets response from REST API without the username of each secret



___

### listTransitionExecutions

▸ **listTransitionExecutions**(`transitionId`, `options?`): `Promise`<[`TransitionExecutionList`](#transitionexecutionlist)\>

List executions in a transition, calls the GET /transitions/{transitionId}/executions endpoint.

#### Parameters

 `transitionId` `string` Id of the transition
 `options?` [`TransitionExecutionListOptions`](#transitionexecutionlistoptions) -

#### Returns

`Promise`<[`TransitionExecutionList`](#transitionexecutionlist)\>

Transition executions responses from REST API



___

### listTransitions

▸ **listTransitions**(`options?`): `Promise`<[`TransitionList`](#transitionlist)\>

List transitions, calls the GET /transitions endpoint.

#### Parameters

 `options?` [`ListTransitionOptions`](#listtransitionoptions)

#### Returns

`Promise`<[`TransitionList`](#transitionlist)\>

Transitions response from REST API



___

### listUsers

▸ **listUsers**(`options?`): `Promise`<[`UserList`](#userlist)\>

List users, calls the GET /users endpoint.

#### Parameters

 `options?` [`PaginationOptions`](#interfacespaginationoptionsmd)

#### Returns

`Promise`<[`UserList`](#userlist)\>

User response from REST API



___

### listWorkflowExecutions

▸ **listWorkflowExecutions**(`workflowId`, `options?`): `Promise`<[`WorkflowExecutionList`](#workflowexecutionlist)\>

List executions in a workflow, calls the GET /workflows/{workflowId}/executions endpoint.

#### Parameters

 `workflowId` `string` Id of the workflow
 `options?` [`ListWorkflowExecutionsOptions`](#listworkflowexecutionsoptions) -

#### Returns

`Promise`<[`WorkflowExecutionList`](#workflowexecutionlist)\>

Workflow executions responses from REST API



___

### listWorkflows

▸ **listWorkflows**(`options?`): `Promise`<[`WorkflowList`](#workflowlist)\>

List workflows, calls the GET /workflows endpoint.

#### Parameters

 `options?` [`PaginationOptions`](#interfacespaginationoptionsmd)

#### Returns

`Promise`<[`WorkflowList`](#workflowlist)\>

Workflows response from REST API



___

### makeDeleteRequest

▸ **makeDeleteRequest**<`T`\>(`path`, `query?`): `Promise`<`T`\>

#### Type parameters

 `T`

#### Parameters

 `path` `string`
 `query?` `any`

#### Returns

`Promise`<`T`\>



___

### makeGetRequest

▸ **makeGetRequest**<`T`\>(`path`, `query?`): `Promise`<`T`\>

#### Type parameters

 `T`

#### Parameters

 `path` `string`
 `query?` `any`

#### Returns

`Promise`<`T`\>



___

### makePatchRequest

▸ **makePatchRequest**<`T`\>(`path`, `body`): `Promise`<`T`\>

#### Type parameters

 `T`

#### Parameters

 `path` `string`
 `body` `any`

#### Returns

`Promise`<`T`\>



___

### makePostRequest

▸ **makePostRequest**<`T`\>(`path`, `body`): `Promise`<`T`\>

#### Type parameters

 `T`

#### Parameters

 `path` `string`
 `body` `any`

#### Returns

`Promise`<`T`\>



___

### sendHeartbeat

▸ **sendHeartbeat**(`transitionId`, `transitionExecutionId`): `Promise`<`unknown`\>

Send heartbeat for a manual execution to signal that we are still working on it.
Must be done at minimum once every 60 seconds or the transition execution will time out.
Calls the POST /transitions/{transitionId}/executions/{executionId}/heartbeats endpoint.

#### Parameters

 `transitionId` `string` Id of the transition
 `transitionExecutionId` `string` Id of the transition execution

#### Returns

`Promise`<`unknown`\>

Empty response



___

### updateAppClient

▸ **updateAppClient**(`appClientId`, `options`): `Promise`<[`AppClient`](#appclient)\>

Updates an appClient, calls the PATCH /appClients/{appClientId} endpoint.

#### Parameters

 `appClientId` `string` Id of the appClient
 `options` [`UpdateAppClientOptions`](#updateappclientoptions) -

#### Returns

`Promise`<[`AppClient`](#appclient)\>

AppClient response from REST API with content



___

### updateAsset

▸ **updateAsset**(`assetId`, `data`): `Promise`<[`Asset`](#asset)\>

Updates an asset, calls the PATCH /assets/{assetId} endpoint.

#### Parameters

 `assetId` `string` Id of the asset
 `data` [`UpdateAssetOptions`](#interfacesupdateassetoptionsmd) -

#### Returns

`Promise`<[`Asset`](#asset)\>

Asset response from REST API with content



___

### updateBatch

▸ **updateBatch**(`batchId`, `options`): `Promise`<[`Batch`](#batch)\>

Updates an batch, calls the PATCH /batches/{batchId} endpoint.

**`deprecated`** Use the new [Client.updateDataset](#updatedataset) method instead.

#### Parameters

 `batchId` `string` Id of the batch
 `options` [`UpdateBatchOptions`](#updatebatchoptions) -

#### Returns

`Promise`<[`Batch`](#batch)\>

Batch response from REST API with content



___

### updateDataBundle

▸ **updateDataBundle**(`modelId`, `dataBundleId`, `options`): `Promise`<[`DataBundle`](#databundle)\>

Updates a dataBundle, calls the PATCH /dataBundles/{dataBundleId} endpoint.

#### Parameters

 `modelId` `string` of the model
 `dataBundleId` `string` Id of the dataBundle
 `options` [`UpdateDataBundleOptions`](#updatedatabundleoptions) -

#### Returns

`Promise`<[`DataBundle`](#databundle)\>

DataBundle response from REST API



___

### updateDataset

▸ **updateDataset**(`datasetId`, `options`): `Promise`<[`Dataset`](#dataset)\>

Updates a dataset, calls the PATCH /datasets/{datasetId} endpoint.

#### Parameters

 `datasetId` `string` Id of the dataset
 `options` [`UpdateDatasetOptions`](#updatedatasetoptions) -

#### Returns

`Promise`<[`Dataset`](#dataset)\>

Dataset response from REST API with content



___

### updateDocument

▸ **updateDocument**(`documentId`, `data`): `Promise`<[`LasDocument`](#lasdocument)\>

Post ground truth to the REST API, calls the PATCH /documents/{documentId} endpoint.
Posting ground truth means posting the ground truth data for the particular document.
This enables the API to learn from past mistakes.

#### Parameters

 `documentId` `string` Id of the document
 `data` [`UpdateDocumentOptions`](#interfacesupdatedocumentoptionsmd) -

#### Returns

`Promise`<[`LasDocument`](#lasdocument)\>

Document response from REST API



___

### updateModel

▸ **updateModel**(`modelId`, `options`): `Promise`<[`Model`](#model)\>

Updates a model, calls the PATCH /models/{modelId} endpoint.

#### Parameters

 `modelId` `string` Id of the model
 `options` [`UpdateModelOptions`](#updatemodeloptions) -

#### Returns

`Promise`<[`Model`](#model)\>

Model response from REST API



___

### updateOrganization

▸ **updateOrganization**(`organizationId`, `options`): `Promise`<[`Organization`](#organization)\>

Updates an organization, calls the PATCH /organizations/{organizationId} endpoint.

#### Parameters

 `organizationId` `string` Id of the organization
 `options` [`UpdateOrganizationOptions`](#updateorganizationoptions) -

#### Returns

`Promise`<[`Organization`](#organization)\>

Organization response from REST API with content



___

### updateSecret

▸ **updateSecret**(`secretId`, `data`): `Promise`<[`Secret`](#secret)\>

Updates a secret, calls the PATCH /secrets/{secretId} endpoint.

#### Parameters

 `secretId` `string` Id of the secret
 `data` [`UpdateSecretOptions`](#interfacesupdatesecretoptionsmd) -

#### Returns

`Promise`<[`Secret`](#secret)\>



___

### updateTransition

▸ **updateTransition**(`transitionId`, `data`): `Promise`<[`Transition`](#transition)\>

Updates a transition, calls the PATCH /transitions/{transitionId} endpoint.

#### Parameters

 `transitionId` `string` Id of the transition
 `data` [`UpdateTransitionOptions`](#updatetransitionoptions) Transition fields to PATCH

#### Returns

`Promise`<[`Transition`](#transition)\>

Transition response from REST API



___

### updateTransitionExecution

▸ **updateTransitionExecution**(`transitionId`, `executionId`, `data`): `Promise`<[`TransitionExecution`](#transitionexecution)\>

Ends the processing of the transition execution, calls the
PATCH /transitions/{transitionId}/executions/{executionId} endpoint.

#### Parameters

 `transitionId` `string` Id of the transition that performs the execution
 `executionId` `string` Id of the execution to update
 `data` [`UpdateTransitionExecution`](#interfacesupdatetransitionexecutionmd) -

#### Returns

`Promise`<[`TransitionExecution`](#transitionexecution)\>

Transition execution response from REST API



___

### updateUser

▸ **updateUser**(`userId`, `data`): `Promise`<[`User`](#user)\>

Updates a user, calls the PATCH /users/{userId} endpoint.

#### Parameters

 `userId` `string` Id of the user
 `data` [`UpdateUserOptions`](#updateuseroptions) -

#### Returns

`Promise`<[`User`](#user)\>

User response from REST API



___

### updateWorkflow

▸ **updateWorkflow**(`workflowId`, `data`): `Promise`<[`Workflow`](#workflow)\>

Updates a workflow, calls the PATCH /workflows/{workflowId} endpoint.

#### Parameters

 `workflowId` `string` Id of the workflow
 `data` [`UpdateWorkflowOptions`](#interfacesupdateworkflowoptionsmd) Workflow fields to PATCH

#### Returns

`Promise`<[`Workflow`](#workflow)\>

Workflow response from REST API



___

### updateWorkflowExecution

▸ **updateWorkflowExecution**(`workflowId`, `executionId`, `data`): `Promise`<[`WorkflowExecution`](#workflowexecution)\>

Retry or end the processing of a workflow execution,
calls the PATCH /workflows/{workflowId}/executions/{executionId} endpoint.

#### Parameters

 `workflowId` `string` Id of the workflow that performs the execution
 `executionId` `string` Id of the execution to update
 `data` [`UpdateWorkflowExecutionOptions`](#interfacesupdateworkflowexecutionoptionsmd) -

#### Returns

`Promise`<[`WorkflowExecution`](#workflowexecution)\>

Workflow execution response from REST API




<a name="classescredentialsmd"></a>

# Class: Credentials

Use to fetch and store credentials and to generate/cache an access token

## Properties

### apiEndpoint

• `Readonly` **apiEndpoint**: `string`



## Methods

### getAccessToken

▸ **getAccessToken**(): `Promise`<`string`\>

Method used to get and cache an access token. Algorithm used:
1. Look for a valid token in memory.
2. Look for a valid token in the storage (if provided);
3. Fetch a new token from server and cache it (both in memory and in storage).

#### Returns

`Promise`<`string`\>




<a name="classestokenmd"></a>

# Class: Token

Wrapper class for an AWS Cognito token

## Constructors

### constructor

• **new Token**(`accessToken`, `expiration`, `refreshToken?`)

#### Parameters

 `accessToken` `string`
 `expiration` `number`
 `refreshToken?` `string`



## Properties

### accessToken

• `Readonly` **accessToken**: `string`



___

### expiration

• `Readonly` **expiration**: `number`



___

### refreshToken

• `Optional` `Readonly` **refreshToken**: `string`



## Methods

### isValid

▸ **isValid**(): `boolean`

Checks if current timestamp is larger than token expiration time

#### Returns

`boolean`




<a name="interfacescreatedocumentoptionsmd"></a>

# Interface: CreateDocumentOptions

## Properties

### batchId

• `Optional` **batchId**: `string`



___

### consentId

• `Optional` **consentId**: `string`



___

### datasetId

• `Optional` **datasetId**: `string`



___

### groundTruth

• `Optional` **groundTruth**: [`GroundTruth`](#groundtruth)[]



___

### retentionInDays

• `Optional` **retentionInDays**: `number`




<a name="interfacescreatepredictionsoptionsmd"></a>

# Interface: CreatePredictionsOptions

## Properties

### autoRotate

• `Optional` **autoRotate**: `boolean`



___

### imageQuality

• `Optional` **imageQuality**: ``"LOW"`` \| ``"HIGH"``



___

### maxPages

• `Optional` **maxPages**: `number`




<a name="interfacescreatesecretoptionsmd"></a>

# Interface: CreateSecretOptions

## Properties

### description

• `Optional` **description**: `string`




<a name="interfacescreatetransitionoptionsmd"></a>

# Interface: CreateTransitionOptions

## Properties

### description

• `Optional` **description**: ``null`` \| `string`



___

### inputJsonSchema

• `Optional` **inputJsonSchema**: `Record`<`any`, `any`\>



___

### name

• `Optional` **name**: ``null`` \| `string`



___

### outputJsonSchema

• `Optional` **outputJsonSchema**: `Record`<`any`, `any`\>



___

### parameters

• `Optional` **parameters**: [`CreateTransitionDockerParams`](#createtransitiondockerparams) \| [`CreateTransitionManualParams`](#createtransitionmanualparams)




<a name="interfacespaginationoptionsmd"></a>

# Interface: PaginationOptions

## Properties

### maxResults

• `Optional` **maxResults**: `number`



___

### nextToken

• `Optional` **nextToken**: `string`




<a name="interfacestokenstoragemd"></a>

# Interface: TokenStorage<T\>

## Type parameters

 `T` extends [`Token`](#classestokenmd)

## Methods

### getPersistentToken

▸ **getPersistentToken**(): ``null`` \| `T`

#### Returns

``null`` \| `T`



___

### setPersistentToken

▸ **setPersistentToken**(`value`): `void`

#### Parameters

 `value` `T`

#### Returns

`void`




<a name="interfacesupdateassetoptionsmd"></a>

# Interface: UpdateAssetOptions

## Properties

### content

• `Optional` **content**: `string` \| `Buffer`




<a name="interfacesupdatedocumentoptionsmd"></a>

# Interface: UpdateDocumentOptions

## Properties

### groundTruth

• `Optional` **groundTruth**: [`GroundTruth`](#groundtruth)[]



___

### retentionInDays

• `Optional` **retentionInDays**: `number`




<a name="interfacesupdatesecretoptionsmd"></a>

# Interface: UpdateSecretOptions

## Properties

### data

• `Optional` **data**: `Record`<`any`, `any`\>



___

### description

• `Optional` **description**: ``null`` \| `string`



___

### name

• `Optional` **name**: ``null`` \| `string`




<a name="interfacesupdatetransitionexecutionmd"></a>

# Interface: UpdateTransitionExecution

## Properties

### error

• `Optional` **error**: `Object`

#### Type declaration

 `message` `string`



___

### output

• `Optional` **output**: `Record`<`any`, `any`\>



___

### startTime

• `Optional` **startTime**: `string`



___

### status

• **status**: ``"succeeded"`` \| ``"failed"`` \| ``"retry"`` \| ``"rejected"``




<a name="interfacesupdateworkflowexecutionoptionsmd"></a>

# Interface: UpdateWorkflowExecutionOptions

## Properties

### nextTransitionId

• **nextTransitionId**: `string`




<a name="interfacesupdateworkflowoptionsmd"></a>

# Interface: UpdateWorkflowOptions

## Properties

### completedConfig

• `Optional` **completedConfig**: [`WorkflowCompletedConfig`](#workflowcompletedconfig)



___

### description

• `Optional` **description**: ``null`` \| `string`



___

### errorConfig

• `Optional` **errorConfig**: [`WorkflowErrorConfig`](#workflowerrorconfig)



___

### name

• `Optional` **name**: ``null`` \| `string`




<a name="modulesmd"></a>

# @lucidtech/las-sdk-core

## Classes

- [Client](#classesclientmd)
- [Credentials](#classescredentialsmd)
- [Token](#classestokenmd)

## Interfaces

- [CreateDocumentOptions](#interfacescreatedocumentoptionsmd)
- [CreatePredictionsOptions](#interfacescreatepredictionsoptionsmd)
- [CreateSecretOptions](#interfacescreatesecretoptionsmd)
- [CreateTransitionOptions](#interfacescreatetransitionoptionsmd)
- [PaginationOptions](#interfacespaginationoptionsmd)
- [TokenStorage](#interfacestokenstoragemd)
- [UpdateAssetOptions](#interfacesupdateassetoptionsmd)
- [UpdateDocumentOptions](#interfacesupdatedocumentoptionsmd)
- [UpdateSecretOptions](#interfacesupdatesecretoptionsmd)
- [UpdateTransitionExecution](#interfacesupdatetransitionexecutionmd)
- [UpdateWorkflowExecutionOptions](#interfacesupdateworkflowexecutionoptionsmd)
- [UpdateWorkflowOptions](#interfacesupdateworkflowoptionsmd)

## Type aliases

### AppClient

Ƭ **AppClient**: `Object`

#### Type declaration

 `appClientId` `string`
 `callbackUrls` `string`[] \| ``null``
 `clientId` `string`
 `clientSecret?` `string`
 `createdBy` `string` \| ``null``
 `createdTime` `string` \| ``null``
 `defaultLoginUrl` `string` \| ``null``
 `description` `string` \| ``null``
 `hasSecret` `boolean`
 `loginUrls` `string`[] \| ``null``
 `logoutUrls` `string`[] \| ``null``
 `name` `string` \| ``null``
 `updatedBy` `string` \| ``null``
 `updatedTime` `string` \| ``null``



___

### AppClientList

Ƭ **AppClientList**: `Object`

#### Type declaration

 `appClients` [`AppClient`](#appclient)[]
 `nextToken` `string` \| ``null``



___

### Asset

Ƭ **Asset**: `Object`

#### Type declaration

 `assetId` `string`
 `content` `string`



___

### AssetList

Ƭ **AssetList**: `Object`

#### Type declaration

 `assets` [`AssetWithoutContent`](#assetwithoutcontent)[]
 `nextToken` `string` \| ``null``



___

### AssetWithoutContent

Ƭ **AssetWithoutContent**: `Omit`<[`Asset`](#asset), ``"content"``\>



___

### AuthorizationHeaders

Ƭ **AuthorizationHeaders**: `Object`

#### Type declaration

 `Authorization` `string`



___

### AxiosFn

Ƭ **AxiosFn**: <T, R\>(`url`: `string`, `body?`: `any`, `config?`: `AxiosRequestConfig`) => `Promise`<`R`\>

#### Type declaration

▸ <`T`, `R`\>(`url`, `body?`, `config?`): `Promise`<`R`\>

##### Type parameters

 `T` `any`
 `R` `AxiosResponse`<`T`\>

##### Parameters

 `url` `string`
 `body?` `any`
 `config?` `AxiosRequestConfig`

##### Returns

`Promise`<`R`\>



___

### Batch

Ƭ **Batch**: `Object`

#### Type declaration

 `batchId` `string`
 `containsPersonallyIdentifiableInformation` `boolean`
 `createdTime` `string`
 `description` `string`
 `name` `string`
 `numDocuments` `number`
 `retentionInDays` `number`
 `storageLocation` ``"EU"``



___

### BatchList

Ƭ **BatchList**: `Object`

#### Type declaration

 `batches` [`Batch`](#batch)[]
 `nextToken` `string` \| ``null``



___

### ContentType

Ƭ **ContentType**: ``"application/pdf"`` \| ``"image/jpeg"`` \| ``"image/png"`` \| ``"image/tiff"``



___

### CreateAppClientOptions

Ƭ **CreateAppClientOptions**: `Object`

#### Type declaration

 `callbackUrls?` `string`[]
 `defaultLoginUrl?` `string`
 `description?` `string`
 `generateSecret?` `boolean`
 `loginUrls?` `string`[]
 `logoutUrls?` `string`[]
 `name?` `string`



___

### CreateBatchOptions

Ƭ **CreateBatchOptions**: `Object`

#### Type declaration

 `containsPersonallyIdentifiableInformation?` `boolean`
 `description?` `string`
 `name?` `string`



___

### CreateDataBundleOptions

Ƭ **CreateDataBundleOptions**: `Object`

#### Type declaration

 `description?` `string`
 `name?` `string`



___

### CreateDatasetOptions

Ƭ **CreateDatasetOptions**: `Object`

#### Type declaration

 `containsPersonallyIdentifiableInformation?` `boolean`
 `description?` `string`
 `name?` `string`



___

### CreateModelOptions

Ƭ **CreateModelOptions**: `Object`

#### Type declaration

 `description?` `string`
 `name?` `string`
 `preprocessConfig?` [`PreprocessConfig`](#preprocessconfig)



___

### CreateTransitionDockerParams

Ƭ **CreateTransitionDockerParams**: `Object`

#### Type declaration

 `cpu?` ``256``
 `credentials?` `Object`
 `credentials.password` `string`
 `credentials.username` `string`
 `environment?` `object`
 `imageUrl` `string`
 `memory?` ``512`` \| ``1024`` \| ``2048``



___

### CreateTransitionManualParams

Ƭ **CreateTransitionManualParams**: `Object`

#### Type declaration

 `assets?` { `jsRemoteComponent?`: `string`  } & `Record`<`string`, `string`\>



___

### CreateTransitionParams

Ƭ **CreateTransitionParams**: [`CreateTransitionDockerParams`](#createtransitiondockerparams) \| [`CreateTransitionManualParams`](#createtransitionmanualparams)



___

### CreateUserOptions

Ƭ **CreateUserOptions**: `Object`

#### Type declaration

 `appClientId?` `string`
 `avatar?` `string`
 `name?` `string`



___

### CreateWorkflowOptions

Ƭ **CreateWorkflowOptions**: `Object`

#### Type declaration

 `completedConfig?` [`WorkflowCompletedConfig`](#workflowcompletedconfig)
 `description?` `string` \| ``null``
 `errorConfig?` [`WorkflowErrorConfig`](#workflowerrorconfig)



___

### DataBundle

Ƭ **DataBundle**: `Object`

#### Type declaration

 `createdBy` `string` \| ``null``
 `createdTime` `string`
 `dataBundleId` `string`
 `datasets` [`Dataset`](#dataset)[]
 `description` `string` \| ``null``
 `modelId` `string`
 `name` `string` \| ``null``
 `status` ``"ready"`` \| ``"processing"`` \| ``"failed"``
 `summary` `Record`<`string`, `any`\>
 `updatedBy` `string` \| ``null``
 `updatedTime` `string`



___

### DataBundleList

Ƭ **DataBundleList**: `Object`

#### Type declaration

 `dataBundles` [`DataBundle`](#databundle)[]
 `nextToken` `string` \| ``null``



___

### Dataset

Ƭ **Dataset**: `Object`

#### Type declaration

 `containsPersonallyIdentifiableInformation` `boolean`
 `createdBy` `string` \| ``null``
 `createdTime` `string`
 `datasetId` `string`
 `description` `string`
 `groundTruthSummary` `Record`<`string`, `number`\>
 `name` `string`
 `numberOfDocuments` `number`
 `retentionInDays` `number`
 `storageLocation` ``"EU"``
 `updatedBy` `string` \| ``null``
 `updatedTime` `string`
 `version` `number`



___

### DatasetList

Ƭ **DatasetList**: `Object`

#### Type declaration

 `datasets` [`Dataset`](#dataset)[]
 `nextToken` `string` \| ``null``



___

### DeleteDocumentOptions

Ƭ **DeleteDocumentOptions**: [`PaginationOptions`](#interfacespaginationoptionsmd) & { `batchId?`: `string` \| `string`[] ; `consentId?`: `string` \| `string`[] ; `datasetId?`: `string` \| `string`[]  }



___

### Field

Ƭ **Field**: `Object`

#### Type declaration

 `description` `string`
 `maxLength` `number`
 `type` ``"all"`` \| ``"alphanum"`` \| ``"alphanumext"`` \| ``"amount"`` \| ``"date"`` \| ``"letter"`` \| ``"number"`` \| ``"phone"`` \| ``"string"`` \| ``"digits"``



___

### FieldConfig

Ƭ **FieldConfig**: `Record`<`string`, [`Field`](#field)\>



___

### GroundTruth

Ƭ **GroundTruth**: `Object`

#### Type declaration

 `label` `string` maxLength: 36, minLength: 1, pattern: ^[0-9A-Za-z_]+$
 `value` `string` \| `boolean` \| ``null`` maxLength: 64, minLength: 1



___

### LasDocument

Ƭ **LasDocument**: `Object`

#### Type declaration

 `batchId?` `string`
 `consentId?` `string`
 `content` `string`
 `contentType` [`ContentType`](#contenttype)
 `createdBy` `string` \| ``null``
 `createdTime` `string` \| ``null``
 `datasetId?` `string`
 `documentId` `string`
 `groundTruth?` [`GroundTruth`](#groundtruth)[]
 `retentionInDays` `number`
 `updatedBy` `string` \| ``null``
 `updatedTime` `string` \| ``null``



___

### LasDocumentList

Ƭ **LasDocumentList**: `Object`

#### Type declaration

 `batchId?` `string`
 `documents` [`LasDocumentWithoutContent`](#lasdocumentwithoutcontent)[]
 `nextToken` `string` \| ``null``



___

### LasDocumentWithoutContent

Ƭ **LasDocumentWithoutContent**: `Omit`<[`LasDocument`](#lasdocument), ``"content"``\>



___

### ListAppClientsOptions

Ƭ **ListAppClientsOptions**: [`PaginationOptions`](#interfacespaginationoptionsmd)



___

### ListAssetsOptions

Ƭ **ListAssetsOptions**: [`PaginationOptions`](#interfacespaginationoptionsmd)



___

### ListBatchesOptions

Ƭ **ListBatchesOptions**: [`PaginationOptions`](#interfacespaginationoptionsmd)



___

### ListDataBundleOptions

Ƭ **ListDataBundleOptions**: [`PaginationOptions`](#interfacespaginationoptionsmd)



___

### ListDatasetsOptions

Ƭ **ListDatasetsOptions**: [`PaginationOptions`](#interfacespaginationoptionsmd)



___

### ListDocumentsOptions

Ƭ **ListDocumentsOptions**: [`PaginationOptions`](#interfacespaginationoptionsmd) & { `batchId?`: `string` \| `string`[] ; `consentId?`: `string` \| `string`[] ; `datasetId?`: `string` \| `string`[]  }



___

### ListModelsOptions

Ƭ **ListModelsOptions**: [`PaginationOptions`](#interfacespaginationoptionsmd)



___

### ListPredictionsOptions

Ƭ **ListPredictionsOptions**: [`PaginationOptions`](#interfacespaginationoptionsmd)



___

### ListSecretsOptions

Ƭ **ListSecretsOptions**: [`PaginationOptions`](#interfacespaginationoptionsmd)



___

### ListTransitionOptions

Ƭ **ListTransitionOptions**: [`PaginationOptions`](#interfacespaginationoptionsmd) & { `transitionType?`: `string` \| `string`[]  }



___

### ListUsersOptions

Ƭ **ListUsersOptions**: [`PaginationOptions`](#interfacespaginationoptionsmd)



___

### ListWorkflowExecutionsOptions

Ƭ **ListWorkflowExecutionsOptions**: [`PaginationOptions`](#interfacespaginationoptionsmd) & { `order?`: ``"ascending"`` \| ``"descending"`` ; `sortBy?`: ``"startTime"`` \| ``"endTime"`` ; `status?`: `string` \| `string`[]  }



___

### ListWorkflowOptions

Ƭ **ListWorkflowOptions**: [`PaginationOptions`](#interfacespaginationoptionsmd)



___

### Log

Ƭ **Log**: `Object`

#### Type declaration

 `events` `Record`<`any`, `any`\>[]
 `logId` `string`
 `transitionId?` `string` \| ``null``



___

### Model

Ƭ **Model**: `Object`

#### Type declaration

 `createdBy` `string` \| ``null``
 `createdTime` `string` \| ``null``
 `description` `string` \| ``null``
 `fieldConfig` [`FieldConfig`](#fieldconfig) \| ``null``
 `height` `number`
 `modelId` `string`
 `name` `string` \| ``null``
 `preprocessConfig` [`PreprocessConfig`](#preprocessconfig)
 `status` ``"active"`` \| ``"inactive"`` \| ``"training"``
 `updatedBy` `string` \| ``null``
 `updatedTime` `string` \| ``null``
 `width` `number`



___

### ModelList

Ƭ **ModelList**: `Object`

#### Type declaration

 `models` [`Model`](#model)[]
 `nextToken` `string` \| ``null``



___

### Organization

Ƭ **Organization**: `Object`

#### Type declaration

 `description` `string` \| ``null``
 `monthlyNumberOfDataBundlesAllowed` `number`
 `monthlyNumberOfDataBundlesCreated` `number`
 `monthlyNumberOfDocumentsAllowed` `number`
 `monthlyNumberOfDocumentsCreated` `number`
 `monthlyNumberOfPredictionsAllowed` `number`
 `monthlyNumberOfPredictionsCreated` `number`
 `monthlyNumberOfTransitionExecutionsAllowed` `number`
 `monthlyNumberOfTransitionExecutionsCreated` `number`
 `monthlyNumberOfWorkflowExecutionsAllowed` `number`
 `monthlyNumberOfWorkflowExecutionsCreated` `number`
 `monthlyUsageSummary` `Record`<`string`, `any`\>
 `name` `string` \| ``null``
 `numberOfAppClientsAllowed` `number`
 `numberOfAppClientsCreated` `number`
 `numberOfAssetsAllowed` `number`
 `numberOfAssetsCreated` `number`
 `numberOfBatchesAllowed` `number`
 `numberOfBatchesCreated` `number`
 `numberOfDatasetsAllowed` `number`
 `numberOfDatasetsCreated` `number`
 `numberOfModelsAllowed` `number`
 `numberOfModelsCreated` `number`
 `numberOfSecretsAllowed` `number`
 `numberOfSecretsCreated` `number`
 `numberOfTransitionsAllowed` `number`
 `numberOfTransitionsCreated` `number`
 `numberOfUsersAllowed` `number`
 `numberOfUsersCreated` `number`
 `numberOfWorkflowsAllowed` `number`
 `numberOfWorkflowsCreated` `number`
 `organizationId` `string`



___

### PostPredictions

Ƭ **PostPredictions**: [`CreatePredictionsOptions`](#interfacescreatepredictionsoptionsmd) & { `documentId`: `string` ; `modelId`: `string`  }



___

### Prediction

Ƭ **Prediction**: [`GroundTruth`](#groundtruth) & { `confidence`: `number`  }



___

### PredictionList

Ƭ **PredictionList**: `Object`

#### Type declaration

 `nextToken` `string` \| ``null``
 `predictions` [`PredictionResponse`](#predictionresponse)[]



___

### PredictionResponse

Ƭ **PredictionResponse**: `Object`

#### Type declaration

 `documentId` `string`
 `inferenceTime` `number`
 `modelId` `string`
 `predictionId` `string`
 `predictions` [`Prediction`](#prediction)[]
 `timestamp` `number`



___

### PreprocessConfig

Ƭ **PreprocessConfig**: `Object`

#### Type declaration

 `autoRotate` `boolean`
 `imageQuality` ``"LOW"`` \| ``"HIGH"``
 `maxPages` `number`



___

### Secret

Ƭ **Secret**: `Object`

#### Type declaration

 `description` `string` \| ``null``
 `name` `string` \| ``null``
 `secredId` `string`



___

### SecretList

Ƭ **SecretList**: `Object`

#### Type declaration

 `nextToken` `string` \| ``null``
 `secrets` [`Secret`](#secret)[]



___

### Transition

Ƭ **Transition**: `Object`

#### Type declaration

 `assets?` `Record`<`string`, `string`\>
 `description` `string`
 `inputJsonSchema` `unknown`
 `name` `string`
 `outputJsonSchema?` `unknown`
 `parameters` `Record`<`string`, `any`\>
 `transitionId` `string`
 `transitionType` [`TransitionType`](#transitiontype)



___

### TransitionExecution

Ƭ **TransitionExecution**: `Object`

#### Type declaration

 `completedBy` `string` \| ``null``
 `endTime` `string` \| ``null``
 `executionId` `string`
 `input` `Record`<`any`, `any`\>
 `logId` `string` \| ``null``
 `startTime` `string` \| ``null``
 `status` [`TransitionExecutionStatus`](#transitionexecutionstatus)
 `transitionId` `string`



___

### TransitionExecutionList

Ƭ **TransitionExecutionList**: `Object`

#### Type declaration

 `executions` [`TransitionExecution`](#transitionexecution)[]
 `nextToken` `string` \| ``null``
 `transitionId` `string`



___

### TransitionExecutionListOptions

Ƭ **TransitionExecutionListOptions**: [`PaginationOptions`](#interfacespaginationoptionsmd) & { `executionId?`: `string` \| `string`[] ; `order?`: ``"ascending"`` \| ``"descending"`` ; `sortBy?`: ``"startTime"`` \| ``"endTime"`` ; `status?`: [`TransitionExecutionStatus`](#transitionexecutionstatus) \| [`TransitionExecutionStatus`](#transitionexecutionstatus)[]  }



___

### TransitionExecutionStatus

Ƭ **TransitionExecutionStatus**: ``"succeeded"`` \| ``"failed"`` \| ``"retry"`` \| ``"running"`` \| ``"rejected"``



___

### TransitionList

Ƭ **TransitionList**: `Object`

#### Type declaration

 `nextToken` `string` \| ``null``
 `transitions` [`Transition`](#transition)[]



___

### TransitionType

Ƭ **TransitionType**: ``"docker"`` \| ``"manual"``



___

### UpdateAppClientOptions

Ƭ **UpdateAppClientOptions**: `Object`

#### Type declaration

 `defaultLoginUrl?` `string`
 `description?` `string`
 `loginUrls?` `string`[]
 `name?` `string`



___

### UpdateBatchOptions

Ƭ **UpdateBatchOptions**: `Object`

#### Type declaration

 `description?` `string`
 `name?` `string`



___

### UpdateDataBundleOptions

Ƭ **UpdateDataBundleOptions**: `Object`

#### Type declaration

 `description?` `string`
 `name?` `string`



___

### UpdateDatasetOptions

Ƭ **UpdateDatasetOptions**: `Object`

#### Type declaration

 `description?` `string`
 `name?` `string`



___

### UpdateModelOptions

Ƭ **UpdateModelOptions**: `Object`

#### Type declaration

 `description?` `string`
 `fieldConfig?` [`FieldConfig`](#fieldconfig)
 `height?` `number`
 `name?` `string`
 `preprocessConfig?` [`PreprocessConfig`](#preprocessconfig)
 `status?` ``"training"``
 `width?` `number`



___

### UpdateOrganizationOptions

Ƭ **UpdateOrganizationOptions**: `Object`

#### Type declaration

 `description?` `string`
 `name?` `string`



___

### UpdateTransitionOptions

Ƭ **UpdateTransitionOptions**: `Object`

#### Type declaration

 `description?` `string`
 `inputJsonSchema?` `Record`<`any`, `any`\>
 `name?` `string`
 `outputJsonSchema?` `Record`<`any`, `any`\>



___

### UpdateUserOptions

Ƭ **UpdateUserOptions**: `Object`

#### Type declaration

 `avatar?` `string` \| ``null``
 `name?` `string` \| ``null``



___

### User

Ƭ **User**: `Object`

#### Type declaration

 `avatar` `string` \| ``null``
 `createdBy` `string` \| ``null``
 `createdTime` `string` \| ``null``
 `email` `string`
 `name` `string` \| ``null``
 `updatedBy` `string` \| ``null``
 `updatedTime` `string` \| ``null``
 `userId` `string`



___

### UserList

Ƭ **UserList**: `Object`

#### Type declaration

 `nextToken` `string` \| ``null``
 `users` [`User`](#user)[]



___

### Workflow

Ƭ **Workflow**: `Object`

#### Type declaration

 `completedConfig` [`WorkflowCompletedConfig`](#workflowcompletedconfig)
 `description` `string` \| ``null``
 `errorConfig` [`WorkflowErrorConfig`](#workflowerrorconfig)
 `name` `string` \| ``null``
 `numberOfRunningExecutions` `number`
 `workflowId` `string`



___

### WorkflowCompletedConfig

Ƭ **WorkflowCompletedConfig**: `Object`

#### Type declaration

 `environment?` `Record`<`string`, `string`\>
 `environmentSecrets?` `string`[]
 `imageUrl` `string`
 `secretId?` `string`



___

### WorkflowErrorConfig

Ƭ **WorkflowErrorConfig**: `Object`

#### Type declaration

 `email?` `string`
 `manualRetry?` `boolean`



___

### WorkflowExecution

Ƭ **WorkflowExecution**: `Object`

#### Type declaration

 `completedBy` `string`[]
 `endTime` `string` \| ``null``
 `executionId` `string`
 `input` `Record`<`any`, `any`\>
 `logId` `string` \| ``null``
 `output` `Record`<`any`, `any`\>
 `startTime` `string` \| ``null``
 `status` ``"succeeded"`` \| ``"failed"`` \| ``"running"`` \| ``"rejected"`` \| ``"retry"`` \| ``"error"``
 `transitionExecutions` `Record`<`string`, `string`[]\> \| ``null``
 `workflowId` `string`



___

### WorkflowExecutionList

Ƭ **WorkflowExecutionList**: `Object`

#### Type declaration

 `executions` `Required`<[`WorkflowExecution`](#workflowexecution)\>[]
 `nextToken` `string` \| ``null``
 `status?` ``"succeeded"`` \| ``"failed"`` \| ``"running"`` \| ``"rejected"``
 `workflowId` `string`



___

### WorkflowList

Ƭ **WorkflowList**: `Object`

#### Type declaration

 `workflows` [`Workflow`](#workflow)[]



___

### WorkflowSpecification

Ƭ **WorkflowSpecification**: `Object`

#### Type declaration

 `definition` `object`
 `language?` ``"ASL"``
 `version?` ``"1.0.0"``


