
<a name="readmemd"></a>

@lucidtech/las-sdk-core / [Exports](#modulesmd)

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

const credentials = new ClientCredentials('<apiEndpoint>', '<apiKey>', '<clientId>',  '<clientSecret>', '<authEndpoint>');
const client = new Client(credentials);

const content = '<read image content>'
client.createDocument(content, 'image/jpeg').then(documentResponse => {
    console.log(documentResponse);
}).catch(error => {
    console.log(error);
})
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


<a name="classesclientclient-1md"></a>

[@lucidtech/las-sdk-core](#readmemd) / [Exports](#modulesmd) / [client](#modulesclientmd) / Client

# Class: Client

[client](#modulesclientmd).Client

A high-level http client for communicating with the Lucidtech REST API

## Table of contents

### Constructors

- [constructor](#constructor)

### Properties

- [credentials](#credentials)

### Methods

- [createAsset](#createasset)
- [createBatch](#createbatch)
- [createDocument](#createdocument)
- [createPrediction](#createprediction)
- [createSecret](#createsecret)
- [createTransition](#createtransition)
- [createUser](#createuser)
- [createWorkflow](#createworkflow)
- [deleteDocuments](#deletedocuments)
- [deleteTransition](#deletetransition)
- [deleteUser](#deleteuser)
- [deleteWorkflow](#deleteworkflow)
- [deleteWorkflowExecution](#deleteworkflowexecution)
- [executeTransition](#executetransition)
- [executeWorkflow](#executeworkflow)
- [getAsset](#getasset)
- [getDocument](#getdocument)
- [getLog](#getlog)
- [getTransition](#gettransition)
- [getUser](#getuser)
- [getWorkflow](#getworkflow)
- [listAssets](#listassets)
- [listDocuments](#listdocuments)
- [listModels](#listmodels)
- [listPredictions](#listpredictions)
- [listSecrets](#listsecrets)
- [listTransitionExecutions](#listtransitionexecutions)
- [listTransitions](#listtransitions)
- [listUsers](#listusers)
- [listWorkflowExecutions](#listworkflowexecutions)
- [listWorkflows](#listworkflows)
- [makeDeleteRequest](#makedeleterequest)
- [makeGetRequest](#makegetrequest)
- [makePatchRequest](#makepatchrequest)
- [makePostRequest](#makepostrequest)
- [updateAsset](#updateasset)
- [updateDocument](#updatedocument)
- [updateSecret](#updatesecret)
- [updateTransition](#updatetransition)
- [updateTransitionExecution](#updatetransitionexecution)
- [updateUser](#updateuser)
- [updateWorkflow](#updateworkflow)

## Constructors

### constructor

\+ **new Client**(`credentials`: [*Credentials*](#classescredentialscredentials-1md)): [*Client*](#classesclientclient-1md)

#### Parameters:


`credentials` [*Credentials*](#classescredentialscredentials-1md)

**Returns:** [*Client*](#classesclientclient-1md)


## Properties

### credentials

• **credentials**: [*Credentials*](#classescredentialscredentials-1md)


## Methods

### createAsset

▸ **createAsset**(`content`: *string*): *Promise*<[*Asset*](#asset)\>

Creates an asset handle, calls the POST /assets endpoint.

#### Parameters:


`content` *string* Content to POST (base64-encoded string \| Buffer)  

**Returns:** *Promise*<[*Asset*](#asset)\>

Asset response from REST API


___

### createBatch

▸ **createBatch**(`options`: [*CreateBatchOptions*](#createbatchoptions)): *Promise*<[*Batch*](#batch)\>

Creates a batch, calls the POST /batches endpoint.

#### Parameters:


`options` [*CreateBatchOptions*](#createbatchoptions)

**Returns:** *Promise*<[*Batch*](#batch)\>

Batch response from REST API


___

### createDocument

▸ **createDocument**(`content`: *string* \| *Buffer*, `contentType`: [*ContentType*](#contenttype), `options?`: [*CreateDocumentOptions*](#interfacestypescreatedocumentoptionsmd)): *Promise*<[*LasDocument*](#lasdocument)\>

Creates a document handle, calls the POST /documents endpoint.

#### Parameters:


`content` *string* \| *Buffer* Content to POST (base64 string \| Buffer)  
`contentType` [*ContentType*](#contenttype) MIME type for the document handle  
`options?` [*CreateDocumentOptions*](#interfacestypescreatedocumentoptionsmd) -

**Returns:** *Promise*<[*LasDocument*](#lasdocument)\>

Document response from REST API


___

### createPrediction

▸ **createPrediction**(`documentId`: *string*, `modelId`: *string*, `options?`: [*CreatePredictionsOptions*](#interfacestypescreatepredictionsoptionsmd)): *Promise*<[*PredictionResponse*](#predictionresponse)\>

Create a prediction on a document using specified model, calls the POST /predictions endpoint.

#### Parameters:


`documentId` *string* Id of the document to run inference and create a prediction on  
`modelId` *string* Id of the model to use for inference  
`options?` [*CreatePredictionsOptions*](#interfacestypescreatepredictionsoptionsmd) -

**Returns:** *Promise*<[*PredictionResponse*](#predictionresponse)\>

Predicion response from REST API


___

### createSecret

▸ **createSecret**(`data`: *Record*<any, any\>, `options?`: [*CreateSecretOptions*](#interfacestypescreatesecretoptionsmd)): *Promise*<[*Secret*](#secret)\>

Creates an secret handle, calls the POST /secrets endpoint.

#### Parameters:


`data` *Record*<any, any\> Object containing the data you want to keep secret  
`options?` [*CreateSecretOptions*](#interfacestypescreatesecretoptionsmd) -

**Returns:** *Promise*<[*Secret*](#secret)\>

Secret response from REST API


___

### createTransition

▸ **createTransition**(`transitionType`: [*TransitionType*](#transitiontype), `options?`: [*CreateTransitionOptions*](#interfacestypescreatetransitionoptionsmd)): *Promise*<[*Transition*](#transition)\>

Creates a transition handle, calls the POST /transitions endpoint.

#### Parameters:


`transitionType` [*TransitionType*](#transitiontype) Type of transition "docker"\|"manual"  
`options?` [*CreateTransitionOptions*](#interfacestypescreatetransitionoptionsmd) -

**Returns:** *Promise*<[*Transition*](#transition)\>

Transition response from REST API


___

### createUser

▸ **createUser**(`email`: *string*, `data?`: [*CreateUserOptions*](#createuseroptions)): *Promise*<[*User*](#user)\>

Creates a new user, calls the POST /users endpoint.

#### Parameters:


`email` *string* Email to the new user  
`data?` [*CreateUserOptions*](#createuseroptions) -

**Returns:** *Promise*<[*User*](#user)\>

User response from REST API


___

### createWorkflow

▸ **createWorkflow**(`name`: *string*, `specification`: [*WorkflowSpecification*](#workflowspecification), `options?`: [*CreateWorkflowOptions*](#createworkflowoptions)): *Promise*<[*Workflow*](#workflow)\>

Creates a new workflow, calls the POST /workflows endpoint.

#### Parameters:


`name` *string* Name of the workflow  
`specification` [*WorkflowSpecification*](#workflowspecification) Specification of the workflow  
`options?` [*CreateWorkflowOptions*](#createworkflowoptions) -

**Returns:** *Promise*<[*Workflow*](#workflow)\>

Workflow response from REST API


___

### deleteDocuments

▸ **deleteDocuments**(`options?`: [*DeleteDocumentOptions*](#interfacestypesdeletedocumentoptionsmd)): *Promise*<[*LasDocumentList*](#lasdocumentlist)\>

Delete documents with the provided consentId, calls the DELETE /documents endpoint.
Will delete all documents when no consentId is provided.

#### Parameters:


`options?` [*DeleteDocumentOptions*](#interfacestypesdeletedocumentoptionsmd)

**Returns:** *Promise*<[*LasDocumentList*](#lasdocumentlist)\>

Documents response from REST API


___

### deleteTransition

▸ **deleteTransition**(`transitionId`: *string*): *Promise*<[*Transition*](#transition)\>

Delete the transition with the provided transitionId, calls the DELETE /transitions/{transitionId} endpoint.
Will fail if transition is in use by one or more workflows.

#### Parameters:


`transitionId` *string* Id of the transition  

**Returns:** *Promise*<[*Transition*](#transition)\>

Transition response from REST API


___

### deleteUser

▸ **deleteUser**(`userId`: *string*): *Promise*<[*User*](#user)\>

Delete the user with the provided user_id, calls the DELETE /users/{userId} endpoint.

#### Parameters:


`userId` *string* Id of the user  

**Returns:** *Promise*<[*User*](#user)\>

User response from REST API


___

### deleteWorkflow

▸ **deleteWorkflow**(`workflowId`: *string*): *Promise*<[*Workflow*](#workflow)\>

Delete the workflow with the provided workflowId, calls the DELETE /workflows/{workflowId} endpoint.

#### Parameters:


`workflowId` *string* Id of the workflow  

**Returns:** *Promise*<[*Workflow*](#workflow)\>

Workflow response from REST API


___

### deleteWorkflowExecution

▸ **deleteWorkflowExecution**(`workflowId`: *string*, `executionId`: *string*): *Promise*<[*WorkflowExecution*](#workflowexecution)\>

Deletes the execution with the provided execution_id from workflow_id,
calls the DELETE /workflows/{workflowId}/executions/{executionId} endpoint.

#### Parameters:


`workflowId` *string* Id of the workflow  
`executionId` *string* Id of the execution  

**Returns:** *Promise*<[*WorkflowExecution*](#workflowexecution)\>

WorkflowExecution response from REST API


___

### executeTransition

▸ **executeTransition**(`transitionId`: *string*): *Promise*<[*TransitionExecution*](#transitionexecution)\>

Start executing a manual transition, calls the POST /transitions/{transitionId}/executions endpoint.

#### Parameters:


`transitionId` *string* Id of the transition  

**Returns:** *Promise*<[*TransitionExecution*](#transitionexecution)\>

Transition execution response from REST API


___

### executeWorkflow

▸ **executeWorkflow**(`workflowId`: *string*, `input`: *object*): *Promise*<[*WorkflowExecution*](#workflowexecution)\>

Start a workflow execution, calls the POST /workflows/{workflowId}/executions endpoint.

#### Parameters:


`workflowId` *string* Id of the workflow  
`input` *object* Input to the first step of the workflow  

**Returns:** *Promise*<[*WorkflowExecution*](#workflowexecution)\>

Workflow execution response from REST API


___

### getAsset

▸ **getAsset**(`assetId`: *string*): *Promise*<[*Asset*](#asset)\>

Get asset from the REST API, calls the GET /assets/{assetId} endpoint.

#### Parameters:


`assetId` *string* Id of the asset  

**Returns:** *Promise*<[*Asset*](#asset)\>

Asset response from REST API


___

### getDocument

▸ **getDocument**(`documentId`: *string*): *Promise*<[*LasDocument*](#lasdocument)\>

Get document from the REST API, calls the GET /documents/{documentId} endpoint.

#### Parameters:


`documentId` *string* Id of the document  

**Returns:** *Promise*<[*LasDocument*](#lasdocument)\>

Document response from REST API


___

### getLog

▸ **getLog**(`logId`: *string*): *Promise*<[*Log*](#log)\>

Get log, calls the GET /logs/{logId} endpoint.

#### Parameters:


`logId` *string* Id of the log  

**Returns:** *Promise*<[*Log*](#log)\>

Log response from REST API


___

### getTransition

▸ **getTransition**(`transitionId`: *string*): *Promise*<[*Transition*](#transition)\>

Get the transition with the provided transitionId, calls the GET /transitions/{transitionId} endpoint.

#### Parameters:


`transitionId` *string* Id of the transition  

**Returns:** *Promise*<[*Transition*](#transition)\>

Transition response from REST API


___

### getUser

▸ **getUser**(`userId`: *string*): *Promise*<[*User*](#user)\>

Get information about a specific user, calls the GET /users/{user_id} endpoint.

#### Parameters:


`userId` *string* Id of the user  

**Returns:** *Promise*<[*User*](#user)\>

User response from REST API


___

### getWorkflow

▸ **getWorkflow**(`workflowId`: *string*): *Promise*<[*Workflow*](#workflow)\>

Get the workflow with the provided workflowId, calls the GET /workflows/{workflowId} endpoint.

#### Parameters:


`workflowId` *string* Id of the workflow  

**Returns:** *Promise*<[*Workflow*](#workflow)\>

Workflow response from REST API


___

### listAssets

▸ **listAssets**(`options?`: [*PaginationOptions*](#interfacestypespaginationoptionsmd)): *Promise*<[*AssetList*](#assetlist)\>

List assets available, calls the GET /assets endpoint.

#### Parameters:


`options?` [*PaginationOptions*](#interfacestypespaginationoptionsmd)

**Returns:** *Promise*<[*AssetList*](#assetlist)\>

Assets response from REST API without the content of each asset


___

### listDocuments

▸ **listDocuments**(`options?`: [*ListDocumentsOptions*](#listdocumentsoptions)): *Promise*<[*LasDocumentList*](#lasdocumentlist)\>

List documents available for inference, calls the GET /documents endpoint.

#### Parameters:


`options?` [*ListDocumentsOptions*](#listdocumentsoptions)

**Returns:** *Promise*<[*LasDocumentList*](#lasdocumentlist)\>

Documents response from REST API


___

### listModels

▸ **listModels**(`options?`: [*PaginationOptions*](#interfacestypespaginationoptionsmd)): *Promise*<[*ModelList*](#modellist)\>

List models available, calls the GET /models endpoint.

#### Parameters:


`options?` [*PaginationOptions*](#interfacestypespaginationoptionsmd)

**Returns:** *Promise*<[*ModelList*](#modellist)\>

Models response from the REST API


___

### listPredictions

▸ **listPredictions**(`options?`: [*PaginationOptions*](#interfacestypespaginationoptionsmd)): *Promise*<[*PredictionList*](#predictionlist)\>

#### Parameters:


`options?` [*PaginationOptions*](#interfacestypespaginationoptionsmd)

**Returns:** *Promise*<[*PredictionList*](#predictionlist)\>


___

### listSecrets

▸ **listSecrets**(`options?`: [*PaginationOptions*](#interfacestypespaginationoptionsmd)): *Promise*<[*SecretList*](#secretlist)\>

List secrets available, calls the GET /secrets endpoint.

#### Parameters:


`options?` [*PaginationOptions*](#interfacestypespaginationoptionsmd)

**Returns:** *Promise*<[*SecretList*](#secretlist)\>

Secrets response from REST API without the username of each secret


___

### listTransitionExecutions

▸ **listTransitionExecutions**(`transitionId`: *string*, `options?`: [*TransitionExecutionListOptions*](#transitionexecutionlistoptions)): *Promise*<[*TransitionExecutionList*](#transitionexecutionlist)\>

List executions in a transition, calls the GET /transitions/{transitionId}/executions endpoint.

#### Parameters:


`transitionId` *string* Id of the transition  
`options?` [*TransitionExecutionListOptions*](#transitionexecutionlistoptions) -

**Returns:** *Promise*<[*TransitionExecutionList*](#transitionexecutionlist)\>

Transition executions responses from REST API


___

### listTransitions

▸ **listTransitions**(`options?`: [*ListTransitionOptions*](#listtransitionoptions)): *Promise*<[*TransitionList*](#transitionlist)\>

List transitions, calls the GET /transitions endpoint.

#### Parameters:


`options?` [*ListTransitionOptions*](#listtransitionoptions)

**Returns:** *Promise*<[*TransitionList*](#transitionlist)\>

Transitions response from REST API


___

### listUsers

▸ **listUsers**(`options?`: [*PaginationOptions*](#interfacestypespaginationoptionsmd)): *Promise*<[*UserList*](#userlist)\>

List users, calls the GET /users endpoint.

#### Parameters:


`options?` [*PaginationOptions*](#interfacestypespaginationoptionsmd)

**Returns:** *Promise*<[*UserList*](#userlist)\>

User response from REST API


___

### listWorkflowExecutions

▸ **listWorkflowExecutions**(`workflowId`: *string*, `options?`: [*ListWorkflowExecutionsOptions*](#listworkflowexecutionsoptions)): *Promise*<[*WorkflowExecutionList*](#workflowexecutionlist)\>

List executions in a workflow, calls the GET /workflows/{workflowId}/executions endpoint.

#### Parameters:


`workflowId` *string* Id of the workflow  
`options?` [*ListWorkflowExecutionsOptions*](#listworkflowexecutionsoptions) -

**Returns:** *Promise*<[*WorkflowExecutionList*](#workflowexecutionlist)\>

Workflow executions responses from REST API


___

### listWorkflows

▸ **listWorkflows**(`options?`: [*PaginationOptions*](#interfacestypespaginationoptionsmd)): *Promise*<[*WorkflowList*](#workflowlist)\>

List workflows, calls the GET /workflows endpoint.

#### Parameters:


`options?` [*PaginationOptions*](#interfacestypespaginationoptionsmd)

**Returns:** *Promise*<[*WorkflowList*](#workflowlist)\>

Workflows response from REST API


___

### makeDeleteRequest

▸ **makeDeleteRequest**<T\>(`path`: *string*, `query?`: *any*): *Promise*<T\>

#### Type parameters:


`T`

#### Parameters:


`path` *string*
`query?` *any*

**Returns:** *Promise*<T\>


___

### makeGetRequest

▸ **makeGetRequest**<T\>(`path`: *string*, `query?`: *any*): *Promise*<T\>

#### Type parameters:


`T`

#### Parameters:


`path` *string*
`query?` *any*

**Returns:** *Promise*<T\>


___

### makePatchRequest

▸ **makePatchRequest**<T\>(`path`: *string*, `body`: *any*): *Promise*<T\>

#### Type parameters:


`T`

#### Parameters:


`path` *string*
`body` *any*

**Returns:** *Promise*<T\>


___

### makePostRequest

▸ **makePostRequest**<T\>(`path`: *string*, `body`: *any*): *Promise*<T\>

#### Type parameters:


`T`

#### Parameters:


`path` *string*
`body` *any*

**Returns:** *Promise*<T\>


___

### updateAsset

▸ **updateAsset**(`assetId`: *string*, `data`: [*UpdateAssetOptions*](#interfacestypesupdateassetoptionsmd)): *Promise*<[*Asset*](#asset)\>

Updates an asset, calls the PATCH /assets/assetId endpoint.

#### Parameters:


`assetId` *string* Id of the asset  
`data` [*UpdateAssetOptions*](#interfacestypesupdateassetoptionsmd) -

**Returns:** *Promise*<[*Asset*](#asset)\>

Asset response from REST API with content


___

### updateDocument

▸ **updateDocument**(`documentId`: *string*, `data`: [*UpdateDocumentOptions*](#interfacestypesupdatedocumentoptionsmd)): *Promise*<[*LasDocument*](#lasdocument)\>

Post ground truth to the REST API, calls the PATCH /documents/{documentId} endpoint.
Posting ground truth means posting the ground truth data for the particular document.
This enables the API to learn from past mistakes.

#### Parameters:


`documentId` *string* Id of the document  
`data` [*UpdateDocumentOptions*](#interfacestypesupdatedocumentoptionsmd) -

**Returns:** *Promise*<[*LasDocument*](#lasdocument)\>

Document response from REST API


___

### updateSecret

▸ **updateSecret**(`secretId`: *string*, `data`: [*UpdateSecretOptions*](#interfacestypesupdatesecretoptionsmd)): *Promise*<[*Secret*](#secret)\>

Updates a secret, calls the PATCH /secrets/secretId endpoint.

#### Parameters:


`secretId` *string* Id of the secret  
`data` [*UpdateSecretOptions*](#interfacestypesupdatesecretoptionsmd) -

**Returns:** *Promise*<[*Secret*](#secret)\>


___

### updateTransition

▸ **updateTransition**(`transitionId`: *string*, `data`: [*UpdateTransitionOptions*](#updatetransitionoptions)): *Promise*<[*Transition*](#transition)\>

Updates a transition, calls the PATCH /transitions/transitionId endpoint.

#### Parameters:


`transitionId` *string* Id of the transition  
`data` [*UpdateTransitionOptions*](#updatetransitionoptions) Transition fields to PATCH  

**Returns:** *Promise*<[*Transition*](#transition)\>

Transition response from REST API


___

### updateTransitionExecution

▸ **updateTransitionExecution**(`transitionId`: *string*, `executionId`: *string*, `data`: [*UpdateTransitionExecution*](#interfacestypesupdatetransitionexecutionmd)): *Promise*<[*TransitionExecution*](#transitionexecution)\>

Ends the processing of the transition execution, calls the
PATCH /transitions/{transition_id}/executions/{execution_id} endpoint.

#### Parameters:


`transitionId` *string* Id of the transition that performs the execution  
`executionId` *string* Id of the execution to update  
`data` [*UpdateTransitionExecution*](#interfacestypesupdatetransitionexecutionmd) -

**Returns:** *Promise*<[*TransitionExecution*](#transitionexecution)\>

Transition execution response from REST API


___

### updateUser

▸ **updateUser**(`userId`: *string*, `data`: [*UpdateUserOptions*](#updateuseroptions)): *Promise*<[*User*](#user)\>

Updates a user, calls the PATCH /users/{userId} endpoint.

#### Parameters:


`userId` *string* Id of the user  
`data` [*UpdateUserOptions*](#updateuseroptions) -

**Returns:** *Promise*<[*User*](#user)\>

User response from REST API


___

### updateWorkflow

▸ **updateWorkflow**(`workflowId`: *string*, `data`: [*UpdateWorkflowOptions*](#interfacestypesupdateworkflowoptionsmd)): *Promise*<[*Workflow*](#workflow)\>

Updates a workflow, calls the PATCH /workflows/workflowId endpoint.

#### Parameters:


`workflowId` *string* Id of the workflow  
`data` [*UpdateWorkflowOptions*](#interfacestypesupdateworkflowoptionsmd) Workflow fields to PATCH  

**Returns:** *Promise*<[*Workflow*](#workflow)\>

Workflow response from REST API



<a name="classescredentialscredentials-1md"></a>

[@lucidtech/las-sdk-core](#readmemd) / [Exports](#modulesmd) / [credentials](#modulescredentialsmd) / Credentials

# Class: Credentials

[credentials](#modulescredentialsmd).Credentials

Use to fetch and store credentials and to generate/cache an access token

## Table of contents

### Properties

- [apiEndpoint](#apiendpoint)
- [apiKey](#apikey)

### Methods

- [getAccessToken](#getaccesstoken)

## Properties

### apiEndpoint

• `Readonly` **apiEndpoint**: *string*


___

### apiKey

• `Readonly` **apiKey**: *string*


## Methods

### getAccessToken

▸ **getAccessToken**(): *Promise*<string\>

Method used to get and cache an access token. Algorithm used:
1. Look for a valid token in memory.
2. Look for a valid token in the storage (if provided);
3. Fetch a new token from server and cache it (both in memory and in storage).

**Returns:** *Promise*<string\>



<a name="classescredentialstokenmd"></a>

[@lucidtech/las-sdk-core](#readmemd) / [Exports](#modulesmd) / [credentials](#modulescredentialsmd) / Token

# Class: Token

[credentials](#modulescredentialsmd).Token

Wrapper class for an AWS Cognito token

## Table of contents

### Constructors

- [constructor](#constructor)

### Properties

- [accessToken](#accesstoken)
- [expiration](#expiration)
- [refreshToken](#refreshtoken)

### Methods

- [isValid](#isvalid)

## Constructors

### constructor

\+ **new Token**(`accessToken`: *string*, `expiration`: *number*, `refreshToken?`: *string*): [*Token*](#classescredentialstokenmd)

#### Parameters:


`accessToken` *string*
`expiration` *number*
`refreshToken?` *string*

**Returns:** [*Token*](#classescredentialstokenmd)


## Properties

### accessToken

• `Readonly` **accessToken**: *string*


___

### expiration

• `Readonly` **expiration**: *number*


___

### refreshToken

• `Optional` `Readonly` **refreshToken**: *undefined* \| *string*


## Methods

### isValid

▸ **isValid**(): *boolean*

Checks if current timestamp is larger than token expiration time

**Returns:** *boolean*



<a name="interfacesindexcreatedocumentoptionsmd"></a>

[@lucidtech/las-sdk-core](#readmemd) / [Exports](#modulesmd) / [index](#modulesindexmd) / CreateDocumentOptions

# Interface: CreateDocumentOptions

[index](#modulesindexmd).CreateDocumentOptions

## Table of contents

### Properties

- [batchId](#batchid)
- [consentId](#consentid)
- [groundTruth](#groundtruth)

## Properties

### batchId

• `Optional` **batchId**: *undefined* \| *string*


___

### consentId

• `Optional` **consentId**: *undefined* \| *string*


___

### groundTruth

• `Optional` **groundTruth**: *undefined* \| [*GroundTruth*](#groundtruth)[]



<a name="interfacesindexcreatepredictionsoptionsmd"></a>

[@lucidtech/las-sdk-core](#readmemd) / [Exports](#modulesmd) / [index](#modulesindexmd) / CreatePredictionsOptions

# Interface: CreatePredictionsOptions

[index](#modulesindexmd).CreatePredictionsOptions

## Table of contents

### Properties

- [autoRotate](#autorotate)
- [maxPages](#maxpages)

## Properties

### autoRotate

• `Optional` **autoRotate**: *undefined* \| *boolean*


___

### maxPages

• `Optional` **maxPages**: *undefined* \| *number*



<a name="interfacesindexcreatesecretoptionsmd"></a>

[@lucidtech/las-sdk-core](#readmemd) / [Exports](#modulesmd) / [index](#modulesindexmd) / CreateSecretOptions

# Interface: CreateSecretOptions

[index](#modulesindexmd).CreateSecretOptions

## Table of contents

### Properties

- [description](#description)

## Properties

### description

• `Optional` **description**: *undefined* \| *string*



<a name="interfacesindexcreatetransitionoptionsmd"></a>

[@lucidtech/las-sdk-core](#readmemd) / [Exports](#modulesmd) / [index](#modulesindexmd) / CreateTransitionOptions

# Interface: CreateTransitionOptions

[index](#modulesindexmd).CreateTransitionOptions

## Table of contents

### Properties

- [description](#description)
- [inputJsonSchema](#inputjsonschema)
- [name](#name)
- [outputJsonSchema](#outputjsonschema)
- [parameters](#parameters)

## Properties

### description

• `Optional` **description**: *undefined* \| *null* \| *string*


___

### inputJsonSchema

• `Optional` **inputJsonSchema**: *undefined* \| *Record*<any, any\>


___

### name

• `Optional` **name**: *undefined* \| *null* \| *string*


___

### outputJsonSchema

• `Optional` **outputJsonSchema**: *undefined* \| *Record*<any, any\>


___

### parameters

• `Optional` **parameters**: *undefined* \| [*CreateTransitionDockerParams*](#createtransitiondockerparams) \| [*CreateTransitionManualParams*](#createtransitionmanualparams)



<a name="interfacesindexdeletedocumentoptionsmd"></a>

[@lucidtech/las-sdk-core](#readmemd) / [Exports](#modulesmd) / [index](#modulesindexmd) / DeleteDocumentOptions

# Interface: DeleteDocumentOptions

[index](#modulesindexmd).DeleteDocumentOptions

## Table of contents

### Properties

- [consentId](#consentid)

## Properties

### consentId

• `Optional` **consentId**: *undefined* \| *string* \| *string*[]



<a name="interfacesindexpaginationoptionsmd"></a>

[@lucidtech/las-sdk-core](#readmemd) / [Exports](#modulesmd) / [index](#modulesindexmd) / PaginationOptions

# Interface: PaginationOptions

[index](#modulesindexmd).PaginationOptions

## Table of contents

### Properties

- [maxResults](#maxresults)
- [nextToken](#nexttoken)

## Properties

### maxResults

• `Optional` **maxResults**: *undefined* \| *number*


___

### nextToken

• `Optional` **nextToken**: *undefined* \| *string*



<a name="interfacesindexupdateassetoptionsmd"></a>

[@lucidtech/las-sdk-core](#readmemd) / [Exports](#modulesmd) / [index](#modulesindexmd) / UpdateAssetOptions

# Interface: UpdateAssetOptions

[index](#modulesindexmd).UpdateAssetOptions

## Table of contents

### Properties

- [content](#content)

## Properties

### content

• `Optional` **content**: *undefined* \| *string* \| *Buffer*



<a name="interfacesindexupdatedocumentoptionsmd"></a>

[@lucidtech/las-sdk-core](#readmemd) / [Exports](#modulesmd) / [index](#modulesindexmd) / UpdateDocumentOptions

# Interface: UpdateDocumentOptions

[index](#modulesindexmd).UpdateDocumentOptions

## Table of contents

### Properties

- [groundTruth](#groundtruth)

## Properties

### groundTruth

• `Optional` **groundTruth**: *undefined* \| [*GroundTruth*](#groundtruth)[]



<a name="interfacesindexupdatesecretoptionsmd"></a>

[@lucidtech/las-sdk-core](#readmemd) / [Exports](#modulesmd) / [index](#modulesindexmd) / UpdateSecretOptions

# Interface: UpdateSecretOptions

[index](#modulesindexmd).UpdateSecretOptions

## Table of contents

### Properties

- [data](#data)
- [description](#description)
- [name](#name)

## Properties

### data

• `Optional` **data**: *undefined* \| *Record*<any, any\>


___

### description

• `Optional` **description**: *undefined* \| *null* \| *string*


___

### name

• `Optional` **name**: *undefined* \| *null* \| *string*



<a name="interfacesindexupdatetransitionexecutionmd"></a>

[@lucidtech/las-sdk-core](#readmemd) / [Exports](#modulesmd) / [index](#modulesindexmd) / UpdateTransitionExecution

# Interface: UpdateTransitionExecution

[index](#modulesindexmd).UpdateTransitionExecution

## Table of contents

### Properties

- [error](#error)
- [output](#output)
- [status](#status)

## Properties

### error

• `Optional` **error**: *undefined* \| { `message`: *string*  }


___

### output

• `Optional` **output**: *undefined* \| *Record*<any, any\>


___

### status

• **status**: *succeeded* \| *failed* \| *retry* \| *rejected*



<a name="interfacesindexupdateworkflowoptionsmd"></a>

[@lucidtech/las-sdk-core](#readmemd) / [Exports](#modulesmd) / [index](#modulesindexmd) / UpdateWorkflowOptions

# Interface: UpdateWorkflowOptions

[index](#modulesindexmd).UpdateWorkflowOptions

## Table of contents

### Properties

- [description](#description)
- [name](#name)

## Properties

### description

• `Optional` **description**: *undefined* \| *string*


___

### name

• `Optional` **name**: *undefined* \| *string*



<a name="interfacesstoragetokenstoragemd"></a>

[@lucidtech/las-sdk-core](#readmemd) / [Exports](#modulesmd) / [storage](#modulesstoragemd) / TokenStorage

# Interface: TokenStorage<T\>

[storage](#modulesstoragemd).TokenStorage

## Type parameters


`T` [*Token*](#classescredentialstokenmd)

## Table of contents

### Properties

- [getPersistentToken](#getpersistenttoken)
- [setPersistentToken](#setpersistenttoken)

## Properties

### getPersistentToken

• **getPersistentToken**: () => *null* \| T

#### Type declaration:

▸ (): *null* \| T

**Returns:** *null* \| T



___

### setPersistentToken

• **setPersistentToken**: (`value`: T) => *void*

#### Type declaration:

▸ (`value`: T): *void*

#### Parameters:


`value` T

**Returns:** *void*




<a name="interfacestypescreatedocumentoptionsmd"></a>

[@lucidtech/las-sdk-core](#readmemd) / [Exports](#modulesmd) / [types](#modulestypesmd) / CreateDocumentOptions

# Interface: CreateDocumentOptions

[types](#modulestypesmd).CreateDocumentOptions

## Table of contents

### Properties

- [batchId](#batchid)
- [consentId](#consentid)
- [groundTruth](#groundtruth)

## Properties

### batchId

• `Optional` **batchId**: *undefined* \| *string*


___

### consentId

• `Optional` **consentId**: *undefined* \| *string*


___

### groundTruth

• `Optional` **groundTruth**: *undefined* \| [*GroundTruth*](#groundtruth)[]



<a name="interfacestypescreatepredictionsoptionsmd"></a>

[@lucidtech/las-sdk-core](#readmemd) / [Exports](#modulesmd) / [types](#modulestypesmd) / CreatePredictionsOptions

# Interface: CreatePredictionsOptions

[types](#modulestypesmd).CreatePredictionsOptions

## Table of contents

### Properties

- [autoRotate](#autorotate)
- [maxPages](#maxpages)

## Properties

### autoRotate

• `Optional` **autoRotate**: *undefined* \| *boolean*


___

### maxPages

• `Optional` **maxPages**: *undefined* \| *number*



<a name="interfacestypescreatesecretoptionsmd"></a>

[@lucidtech/las-sdk-core](#readmemd) / [Exports](#modulesmd) / [types](#modulestypesmd) / CreateSecretOptions

# Interface: CreateSecretOptions

[types](#modulestypesmd).CreateSecretOptions

## Table of contents

### Properties

- [description](#description)

## Properties

### description

• `Optional` **description**: *undefined* \| *string*



<a name="interfacestypescreatetransitionoptionsmd"></a>

[@lucidtech/las-sdk-core](#readmemd) / [Exports](#modulesmd) / [types](#modulestypesmd) / CreateTransitionOptions

# Interface: CreateTransitionOptions

[types](#modulestypesmd).CreateTransitionOptions

## Table of contents

### Properties

- [description](#description)
- [inputJsonSchema](#inputjsonschema)
- [name](#name)
- [outputJsonSchema](#outputjsonschema)
- [parameters](#parameters)

## Properties

### description

• `Optional` **description**: *undefined* \| *null* \| *string*


___

### inputJsonSchema

• `Optional` **inputJsonSchema**: *undefined* \| *Record*<any, any\>


___

### name

• `Optional` **name**: *undefined* \| *null* \| *string*


___

### outputJsonSchema

• `Optional` **outputJsonSchema**: *undefined* \| *Record*<any, any\>


___

### parameters

• `Optional` **parameters**: *undefined* \| [*CreateTransitionDockerParams*](#createtransitiondockerparams) \| [*CreateTransitionManualParams*](#createtransitionmanualparams)



<a name="interfacestypesdeletedocumentoptionsmd"></a>

[@lucidtech/las-sdk-core](#readmemd) / [Exports](#modulesmd) / [types](#modulestypesmd) / DeleteDocumentOptions

# Interface: DeleteDocumentOptions

[types](#modulestypesmd).DeleteDocumentOptions

## Table of contents

### Properties

- [consentId](#consentid)

## Properties

### consentId

• `Optional` **consentId**: *undefined* \| *string* \| *string*[]



<a name="interfacestypespaginationoptionsmd"></a>

[@lucidtech/las-sdk-core](#readmemd) / [Exports](#modulesmd) / [types](#modulestypesmd) / PaginationOptions

# Interface: PaginationOptions

[types](#modulestypesmd).PaginationOptions

## Table of contents

### Properties

- [maxResults](#maxresults)
- [nextToken](#nexttoken)

## Properties

### maxResults

• `Optional` **maxResults**: *undefined* \| *number*


___

### nextToken

• `Optional` **nextToken**: *undefined* \| *string*



<a name="interfacestypesupdateassetoptionsmd"></a>

[@lucidtech/las-sdk-core](#readmemd) / [Exports](#modulesmd) / [types](#modulestypesmd) / UpdateAssetOptions

# Interface: UpdateAssetOptions

[types](#modulestypesmd).UpdateAssetOptions

## Table of contents

### Properties

- [content](#content)

## Properties

### content

• `Optional` **content**: *undefined* \| *string* \| *Buffer*



<a name="interfacestypesupdatedocumentoptionsmd"></a>

[@lucidtech/las-sdk-core](#readmemd) / [Exports](#modulesmd) / [types](#modulestypesmd) / UpdateDocumentOptions

# Interface: UpdateDocumentOptions

[types](#modulestypesmd).UpdateDocumentOptions

## Table of contents

### Properties

- [groundTruth](#groundtruth)

## Properties

### groundTruth

• `Optional` **groundTruth**: *undefined* \| [*GroundTruth*](#groundtruth)[]



<a name="interfacestypesupdatesecretoptionsmd"></a>

[@lucidtech/las-sdk-core](#readmemd) / [Exports](#modulesmd) / [types](#modulestypesmd) / UpdateSecretOptions

# Interface: UpdateSecretOptions

[types](#modulestypesmd).UpdateSecretOptions

## Table of contents

### Properties

- [data](#data)
- [description](#description)
- [name](#name)

## Properties

### data

• `Optional` **data**: *undefined* \| *Record*<any, any\>


___

### description

• `Optional` **description**: *undefined* \| *null* \| *string*


___

### name

• `Optional` **name**: *undefined* \| *null* \| *string*



<a name="interfacestypesupdatetransitionexecutionmd"></a>

[@lucidtech/las-sdk-core](#readmemd) / [Exports](#modulesmd) / [types](#modulestypesmd) / UpdateTransitionExecution

# Interface: UpdateTransitionExecution

[types](#modulestypesmd).UpdateTransitionExecution

## Table of contents

### Properties

- [error](#error)
- [output](#output)
- [status](#status)

## Properties

### error

• `Optional` **error**: *undefined* \| { `message`: *string*  }


___

### output

• `Optional` **output**: *undefined* \| *Record*<any, any\>


___

### status

• **status**: *succeeded* \| *failed* \| *retry* \| *rejected*



<a name="interfacestypesupdateworkflowoptionsmd"></a>

[@lucidtech/las-sdk-core](#readmemd) / [Exports](#modulesmd) / [types](#modulestypesmd) / UpdateWorkflowOptions

# Interface: UpdateWorkflowOptions

[types](#modulestypesmd).UpdateWorkflowOptions

## Table of contents

### Properties

- [description](#description)
- [name](#name)

## Properties

### description

• `Optional` **description**: *undefined* \| *string*


___

### name

• `Optional` **name**: *undefined* \| *string*



<a name="modulesmd"></a>

[@lucidtech/las-sdk-core](#readmemd) / Exports

# @lucidtech/las-sdk-core

## Table of contents

### Modules

- [client](#modulesclientmd)
- [credentials](#modulescredentialsmd)
- [index](#modulesindexmd)
- [storage](#modulesstoragemd)
- [types](#modulestypesmd)


<a name="modulesclientmd"></a>

[@lucidtech/las-sdk-core](#readmemd) / [Exports](#modulesmd) / client

# Module: client

## Table of contents

### References

- [default](#default)

### Classes

- [Client](#classesclientclient-1md)

## References

### default

Renames and exports: [Client](#classesclientclient-1md)


<a name="modulescredentialsmd"></a>

[@lucidtech/las-sdk-core](#readmemd) / [Exports](#modulesmd) / credentials

# Module: credentials

## Table of contents

### Classes

- [Credentials](#classescredentialscredentials-1md)
- [Token](#classescredentialstokenmd)


<a name="modulesindexmd"></a>

[@lucidtech/las-sdk-core](#readmemd) / [Exports](#modulesmd) / index

# Module: index

## Table of contents

### References

- [Client](#client)
- [Credentials](#credentials)
- [Token](#token)
- [TokenStorage](#tokenstorage)

### Interfaces

- [CreateDocumentOptions](#interfacesindexcreatedocumentoptionsmd)
- [CreatePredictionsOptions](#interfacesindexcreatepredictionsoptionsmd)
- [CreateSecretOptions](#interfacesindexcreatesecretoptionsmd)
- [CreateTransitionOptions](#interfacesindexcreatetransitionoptionsmd)
- [DeleteDocumentOptions](#interfacesindexdeletedocumentoptionsmd)
- [PaginationOptions](#interfacesindexpaginationoptionsmd)
- [UpdateAssetOptions](#interfacesindexupdateassetoptionsmd)
- [UpdateDocumentOptions](#interfacesindexupdatedocumentoptionsmd)
- [UpdateSecretOptions](#interfacesindexupdatesecretoptionsmd)
- [UpdateTransitionExecution](#interfacesindexupdatetransitionexecutionmd)
- [UpdateWorkflowOptions](#interfacesindexupdateworkflowoptionsmd)

### Type aliases

- [Asset](#asset)
- [AssetList](#assetlist)
- [AssetWithoutContent](#assetwithoutcontent)
- [AuthorizationHeaders](#authorizationheaders)
- [AxiosFn](#axiosfn)
- [Batch](#batch)
- [ContentType](#contenttype)
- [CreateBatchOptions](#createbatchoptions)
- [CreateTransitionDockerParams](#createtransitiondockerparams)
- [CreateTransitionManualParams](#createtransitionmanualparams)
- [CreateTransitionParams](#createtransitionparams)
- [CreateUserOptions](#createuseroptions)
- [CreateWorkflowOptions](#createworkflowoptions)
- [GroundTruth](#groundtruth)
- [LasDocument](#lasdocument)
- [LasDocumentList](#lasdocumentlist)
- [ListAssetsOptions](#listassetsoptions)
- [ListDocumentsOptions](#listdocumentsoptions)
- [ListModelsOptions](#listmodelsoptions)
- [ListPredictionsOptions](#listpredictionsoptions)
- [ListSecretsOptions](#listsecretsoptions)
- [ListTransitionOptions](#listtransitionoptions)
- [ListUsersOptions](#listusersoptions)
- [ListWorkflowExecutionsOptions](#listworkflowexecutionsoptions)
- [ListWorkflowOptions](#listworkflowoptions)
- [Log](#log)
- [Model](#model)
- [ModelList](#modellist)
- [PostPredictions](#postpredictions)
- [Prediction](#prediction)
- [PredictionList](#predictionlist)
- [PredictionResponse](#predictionresponse)
- [Secret](#secret)
- [SecretList](#secretlist)
- [Transition](#transition)
- [TransitionExecution](#transitionexecution)
- [TransitionExecutionList](#transitionexecutionlist)
- [TransitionExecutionListOptions](#transitionexecutionlistoptions)
- [TransitionList](#transitionlist)
- [TransitionType](#transitiontype)
- [UpdateTransitionOptions](#updatetransitionoptions)
- [UpdateUserOptions](#updateuseroptions)
- [User](#user)
- [UserList](#userlist)
- [Workflow](#workflow)
- [WorkflowExecution](#workflowexecution)
- [WorkflowExecutionList](#workflowexecutionlist)
- [WorkflowList](#workflowlist)
- [WorkflowSpecification](#workflowspecification)

## References

### Client

Re-exports: [Client](#classesclientclient-1md)

___

### Credentials

Re-exports: [Credentials](#classescredentialscredentials-1md)

___

### Token

Re-exports: [Token](#classescredentialstokenmd)

___

### TokenStorage

Re-exports: [TokenStorage](#interfacesstoragetokenstoragemd)

## Type aliases

### Asset

Ƭ **Asset**: *object*

#### Type declaration:


`assetId` *string*
`content` *string*


___

### AssetList

Ƭ **AssetList**: *object*

#### Type declaration:


`assets` [*AssetWithoutContent*](#assetwithoutcontent)[]
`nextToken` *string* \| *null*


___

### AssetWithoutContent

Ƭ **AssetWithoutContent**: *object*

#### Type declaration:


`assetId` *string*


___

### AuthorizationHeaders

Ƭ **AuthorizationHeaders**: *object*

#### Type declaration:


`Authorization` *string*
`X-Api-Key` *string*


___

### AxiosFn

Ƭ **AxiosFn**: <T, R\>(`url`: *string*, `body?`: *any*, `config?`: AxiosRequestConfig) => *Promise*<R\>

#### Type declaration:

▸ <T, R\>(`url`: *string*, `body?`: *any*, `config?`: AxiosRequestConfig): *Promise*<R\>

#### Type parameters:


`T` *any*
`R` *AxiosResponse*<T\>

#### Parameters:


`url` *string*
`body?` *any*
`config?` AxiosRequestConfig

**Returns:** *Promise*<R\>


___

### Batch

Ƭ **Batch**: *object*

#### Type declaration:


`batchId` *string*
`description` *string*
`name` *string*


___

### ContentType

Ƭ **ContentType**: *application/pdf* \| *image/jpeg*


___

### CreateBatchOptions

Ƭ **CreateBatchOptions**: *object*

#### Type declaration:


`description`? *string*
`name`? *string*


___

### CreateTransitionDockerParams

Ƭ **CreateTransitionDockerParams**: *object*

#### Type declaration:


`cpu`? *256*
`credentials`? *object*
`credentials.password` *string*
`credentials.username` *string*
`environment`? *object*
`imageUrl` *string*
`memory`? *512* \| *1024* \| *2048*


___

### CreateTransitionManualParams

Ƭ **CreateTransitionManualParams**: *object*

#### Type declaration:


`assets`? { `jsRemoteComponent?`: *string*  } & *Record*<string, string\>


___

### CreateTransitionParams

Ƭ **CreateTransitionParams**: [*CreateTransitionDockerParams*](#createtransitiondockerparams) \| [*CreateTransitionManualParams*](#createtransitionmanualparams)


___

### CreateUserOptions

Ƭ **CreateUserOptions**: *object*

#### Type declaration:


`avatar`? *string* \| *null*
`name`? *string* \| *null*


___

### CreateWorkflowOptions

Ƭ **CreateWorkflowOptions**: *object*

#### Type declaration:


`description`? *string*
`errorConfig`? *object*
`errorConfig.email` *string*


___

### GroundTruth

Ƭ **GroundTruth**: *object*

#### Type declaration:


`label` *string* maxLength: 36, minLength: 1, pattern: ^[0-9A-Za-z_]+$  
`value` *string* \| *boolean* \| *null* maxLength: 64, minLength: 1  


___

### LasDocument

Ƭ **LasDocument**: *object*

#### Type declaration:


`batchId`? *string* pattern: ^las:batch:[a-f0-9]{32}$  
`consentId`? *string* pattern: ^las:consent:[a-f0-9]{32}$  
`content`? *string* minimum: 1  
`contentType` [*ContentType*](#contenttype) -
`documentId` *string* pattern: ^las:document:[a-f0-9]{32}$  
`groundTruth`? [*GroundTruth*](#groundtruth)[] -
`inferenceTime`? *number* minimum: 0  
`predictions`? [*Prediction*](#prediction)[] -
`updated`? *number* minimum: 1  


___

### LasDocumentList

Ƭ **LasDocumentList**: *object*

#### Type declaration:


`batchId`? *string*
`consentId`? *string*
`documents` [*LasDocument*](#lasdocument)[]
`nextToken`? *string*


___

### ListAssetsOptions

Ƭ **ListAssetsOptions**: [*PaginationOptions*](#interfacestypespaginationoptionsmd)


___

### ListDocumentsOptions

Ƭ **ListDocumentsOptions**: [*PaginationOptions*](#interfacestypespaginationoptionsmd) & { `batchId?`: *string* \| *string*[] ; `consentId?`: *string* \| *string*[]  }


___

### ListModelsOptions

Ƭ **ListModelsOptions**: [*PaginationOptions*](#interfacestypespaginationoptionsmd)


___

### ListPredictionsOptions

Ƭ **ListPredictionsOptions**: [*PaginationOptions*](#interfacestypespaginationoptionsmd)


___

### ListSecretsOptions

Ƭ **ListSecretsOptions**: [*PaginationOptions*](#interfacestypespaginationoptionsmd)


___

### ListTransitionOptions

Ƭ **ListTransitionOptions**: [*PaginationOptions*](#interfacestypespaginationoptionsmd) & { `transitionType?`: *string* \| *string*[]  }


___

### ListUsersOptions

Ƭ **ListUsersOptions**: [*PaginationOptions*](#interfacestypespaginationoptionsmd)


___

### ListWorkflowExecutionsOptions

Ƭ **ListWorkflowExecutionsOptions**: [*PaginationOptions*](#interfacestypespaginationoptionsmd) & { `order?`: *ascending* \| *descending* ; `sortBy?`: *startTime* \| *endTime* ; `status?`: *string* \| *string*[]  }


___

### ListWorkflowOptions

Ƭ **ListWorkflowOptions**: [*PaginationOptions*](#interfacestypespaginationoptionsmd)


___

### Log

Ƭ **Log**: *object*

#### Type declaration:


`events` *Record*<any, any\>[]
`logId` *string*
`transitionId`? *string* \| *null*


___

### Model

Ƭ **Model**: *object*

#### Type declaration:


`description` *string* \| *null*
`height` *number*
`modelId` *string*
`name` *string* \| *null*
`width` *number*


___

### ModelList

Ƭ **ModelList**: *object*

#### Type declaration:


`models` [*Model*](#model)[]
`nextToken` *string* \| *null*


___

### PostPredictions

Ƭ **PostPredictions**: [*CreatePredictionsOptions*](#interfacestypescreatepredictionsoptionsmd) & { `documentId`: *string* ; `modelId`: *string*  }


___

### Prediction

Ƭ **Prediction**: [*GroundTruth*](#groundtruth) & { `confidence`: *number*  }


___

### PredictionList

Ƭ **PredictionList**: *object*

#### Type declaration:


`nextToken` *string* \| *null*
`predictions` [*PredictionResponse*](#predictionresponse)[]


___

### PredictionResponse

Ƭ **PredictionResponse**: *object*

#### Type declaration:


`documentId` *string*
`inferenceTime` *number*
`modelId` *string*
`predictionId` *string*
`predictions` [*Prediction*](#prediction)[]
`timestamp` *number*


___

### Secret

Ƭ **Secret**: *object*

#### Type declaration:


`description` *string* \| *null*
`name` *string* \| *null*
`secredId` *string*


___

### SecretList

Ƭ **SecretList**: *object*

#### Type declaration:


`nextToken`? *string* \| *null*
`secrets` [*Secret*](#secret)[]


___

### Transition

Ƭ **Transition**: *object*

#### Type declaration:


`assets`? *Record*<string, string\>
`description` *string*
`inputJsonSchema` *unknown*
`name` *string*
`outputJsonSchema`? *unknown*
`transitionId` *string*
`transitionType` [*TransitionType*](#transitiontype)


___

### TransitionExecution

Ƭ **TransitionExecution**: *object*

#### Type declaration:


`completedBy` *string* \| *null*
`endTime` *string* \| *null*
`executionId` *string*
`input` *Record*<any, any\>
`startTime` *string* \| *null*
`status` *succeeded* \| *failed* \| *retry* \| *running* \| *rejected*
`transitionId` *string*


___

### TransitionExecutionList

Ƭ **TransitionExecutionList**: *object*

#### Type declaration:


`executions` [*TransitionExecution*](#transitionexecution)[]
`nextToken` *string* \| *null*
`transitionId` *string*


___

### TransitionExecutionListOptions

Ƭ **TransitionExecutionListOptions**: [*PaginationOptions*](#interfacestypespaginationoptionsmd) & { `executionId?`: *string* \| *string*[] ; `order?`: *ascending* \| *descending* ; `sortBy?`: *startTime* \| *endTime* ; `status?`: *succeeded* \| *failed* \| *retry* \| *running* \| *rejected*  }


___

### TransitionList

Ƭ **TransitionList**: *object*

#### Type declaration:


`nextToken`? *string*
`transitions` [*Transition*](#transition)[]


___

### TransitionType

Ƭ **TransitionType**: *docker* \| *manual*


___

### UpdateTransitionOptions

Ƭ **UpdateTransitionOptions**: *object*

#### Type declaration:


`description`? *string*
`inputJsonSchema`? *Record*<any, any\>
`name`? *string*
`outputJsonSchema`? *Record*<any, any\>


___

### UpdateUserOptions

Ƭ **UpdateUserOptions**: *object*

#### Type declaration:


`avatar`? *string* \| *null*
`name`? *string* \| *null*


___

### User

Ƭ **User**: *object*

#### Type declaration:


`avatar` *string* \| *null*
`email` *string*
`name` *string* \| *null*
`userId` *string*


___

### UserList

Ƭ **UserList**: *object*

#### Type declaration:


`nextToken`? *string*
`users` [*User*](#user)[]


___

### Workflow

Ƭ **Workflow**: *object*

#### Type declaration:


`description`? *string*
`name` *string*
`workflowId` *string*


___

### WorkflowExecution

Ƭ **WorkflowExecution**: *object*

#### Type declaration:


`completedBy` *string*[]
`endTime` *string* \| *null*
`executionId` *string*
`input` *Record*<any, any\>
`output` *Record*<any, any\>
`startTime` *string* \| *null*
`status`? *succeeded* \| *failed* \| *running* \| *rejected*
`transitionExecutions` *Record*<string, string[]\> \| *null*
`workflowId` *string*


___

### WorkflowExecutionList

Ƭ **WorkflowExecutionList**: *object*

#### Type declaration:


`executions` *Required*<[*WorkflowExecution*](#workflowexecution)\>[]
`nextToken`? *string*
`status`? *succeeded* \| *failed* \| *running* \| *rejected*
`workflowId` *string*


___

### WorkflowList

Ƭ **WorkflowList**: *object*

#### Type declaration:


`workflows` [*Workflow*](#workflow)[]


___

### WorkflowSpecification

Ƭ **WorkflowSpecification**: *object*

#### Type declaration:


`definition` *object*
`language`? *ASL*
`version`? *1.0.0*



<a name="modulesstoragemd"></a>

[@lucidtech/las-sdk-core](#readmemd) / [Exports](#modulesmd) / storage

# Module: storage

## Table of contents

### Interfaces

- [TokenStorage](#interfacesstoragetokenstoragemd)


<a name="modulestypesmd"></a>

[@lucidtech/las-sdk-core](#readmemd) / [Exports](#modulesmd) / types

# Module: types

## Table of contents

### Interfaces

- [CreateDocumentOptions](#interfacestypescreatedocumentoptionsmd)
- [CreatePredictionsOptions](#interfacestypescreatepredictionsoptionsmd)
- [CreateSecretOptions](#interfacestypescreatesecretoptionsmd)
- [CreateTransitionOptions](#interfacestypescreatetransitionoptionsmd)
- [DeleteDocumentOptions](#interfacestypesdeletedocumentoptionsmd)
- [PaginationOptions](#interfacestypespaginationoptionsmd)
- [UpdateAssetOptions](#interfacestypesupdateassetoptionsmd)
- [UpdateDocumentOptions](#interfacestypesupdatedocumentoptionsmd)
- [UpdateSecretOptions](#interfacestypesupdatesecretoptionsmd)
- [UpdateTransitionExecution](#interfacestypesupdatetransitionexecutionmd)
- [UpdateWorkflowOptions](#interfacestypesupdateworkflowoptionsmd)

### Type aliases

- [Asset](#asset)
- [AssetList](#assetlist)
- [AssetWithoutContent](#assetwithoutcontent)
- [AuthorizationHeaders](#authorizationheaders)
- [AxiosFn](#axiosfn)
- [Batch](#batch)
- [ContentType](#contenttype)
- [CreateBatchOptions](#createbatchoptions)
- [CreateTransitionDockerParams](#createtransitiondockerparams)
- [CreateTransitionManualParams](#createtransitionmanualparams)
- [CreateTransitionParams](#createtransitionparams)
- [CreateUserOptions](#createuseroptions)
- [CreateWorkflowOptions](#createworkflowoptions)
- [GroundTruth](#groundtruth)
- [LasDocument](#lasdocument)
- [LasDocumentList](#lasdocumentlist)
- [ListAssetsOptions](#listassetsoptions)
- [ListDocumentsOptions](#listdocumentsoptions)
- [ListModelsOptions](#listmodelsoptions)
- [ListPredictionsOptions](#listpredictionsoptions)
- [ListSecretsOptions](#listsecretsoptions)
- [ListTransitionOptions](#listtransitionoptions)
- [ListUsersOptions](#listusersoptions)
- [ListWorkflowExecutionsOptions](#listworkflowexecutionsoptions)
- [ListWorkflowOptions](#listworkflowoptions)
- [Log](#log)
- [Model](#model)
- [ModelList](#modellist)
- [PostPredictions](#postpredictions)
- [Prediction](#prediction)
- [PredictionList](#predictionlist)
- [PredictionResponse](#predictionresponse)
- [Secret](#secret)
- [SecretList](#secretlist)
- [Transition](#transition)
- [TransitionExecution](#transitionexecution)
- [TransitionExecutionList](#transitionexecutionlist)
- [TransitionExecutionListOptions](#transitionexecutionlistoptions)
- [TransitionList](#transitionlist)
- [TransitionType](#transitiontype)
- [UpdateTransitionOptions](#updatetransitionoptions)
- [UpdateUserOptions](#updateuseroptions)
- [User](#user)
- [UserList](#userlist)
- [Workflow](#workflow)
- [WorkflowExecution](#workflowexecution)
- [WorkflowExecutionList](#workflowexecutionlist)
- [WorkflowList](#workflowlist)
- [WorkflowSpecification](#workflowspecification)

## Type aliases

### Asset

Ƭ **Asset**: *object*

#### Type declaration:


`assetId` *string*
`content` *string*


___

### AssetList

Ƭ **AssetList**: *object*

#### Type declaration:


`assets` [*AssetWithoutContent*](#assetwithoutcontent)[]
`nextToken` *string* \| *null*


___

### AssetWithoutContent

Ƭ **AssetWithoutContent**: *object*

#### Type declaration:


`assetId` *string*


___

### AuthorizationHeaders

Ƭ **AuthorizationHeaders**: *object*

#### Type declaration:


`Authorization` *string*
`X-Api-Key` *string*


___

### AxiosFn

Ƭ **AxiosFn**: <T, R\>(`url`: *string*, `body?`: *any*, `config?`: AxiosRequestConfig) => *Promise*<R\>

#### Type declaration:

▸ <T, R\>(`url`: *string*, `body?`: *any*, `config?`: AxiosRequestConfig): *Promise*<R\>

#### Type parameters:


`T` *any*
`R` *AxiosResponse*<T\>

#### Parameters:


`url` *string*
`body?` *any*
`config?` AxiosRequestConfig

**Returns:** *Promise*<R\>


___

### Batch

Ƭ **Batch**: *object*

#### Type declaration:


`batchId` *string*
`description` *string*
`name` *string*


___

### ContentType

Ƭ **ContentType**: *application/pdf* \| *image/jpeg*


___

### CreateBatchOptions

Ƭ **CreateBatchOptions**: *object*

#### Type declaration:


`description`? *string*
`name`? *string*


___

### CreateTransitionDockerParams

Ƭ **CreateTransitionDockerParams**: *object*

#### Type declaration:


`cpu`? *256*
`credentials`? *object*
`credentials.password` *string*
`credentials.username` *string*
`environment`? *object*
`imageUrl` *string*
`memory`? *512* \| *1024* \| *2048*


___

### CreateTransitionManualParams

Ƭ **CreateTransitionManualParams**: *object*

#### Type declaration:


`assets`? { `jsRemoteComponent?`: *string*  } & *Record*<string, string\>


___

### CreateTransitionParams

Ƭ **CreateTransitionParams**: [*CreateTransitionDockerParams*](#createtransitiondockerparams) \| [*CreateTransitionManualParams*](#createtransitionmanualparams)


___

### CreateUserOptions

Ƭ **CreateUserOptions**: *object*

#### Type declaration:


`avatar`? *string* \| *null*
`name`? *string* \| *null*


___

### CreateWorkflowOptions

Ƭ **CreateWorkflowOptions**: *object*

#### Type declaration:


`description`? *string*
`errorConfig`? *object*
`errorConfig.email` *string*


___

### GroundTruth

Ƭ **GroundTruth**: *object*

#### Type declaration:


`label` *string* maxLength: 36, minLength: 1, pattern: ^[0-9A-Za-z_]+$  
`value` *string* \| *boolean* \| *null* maxLength: 64, minLength: 1  


___

### LasDocument

Ƭ **LasDocument**: *object*

#### Type declaration:


`batchId`? *string* pattern: ^las:batch:[a-f0-9]{32}$  
`consentId`? *string* pattern: ^las:consent:[a-f0-9]{32}$  
`content`? *string* minimum: 1  
`contentType` [*ContentType*](#contenttype) -
`documentId` *string* pattern: ^las:document:[a-f0-9]{32}$  
`groundTruth`? [*GroundTruth*](#groundtruth)[] -
`inferenceTime`? *number* minimum: 0  
`predictions`? [*Prediction*](#prediction)[] -
`updated`? *number* minimum: 1  


___

### LasDocumentList

Ƭ **LasDocumentList**: *object*

#### Type declaration:


`batchId`? *string*
`consentId`? *string*
`documents` [*LasDocument*](#lasdocument)[]
`nextToken`? *string*


___

### ListAssetsOptions

Ƭ **ListAssetsOptions**: [*PaginationOptions*](#interfacestypespaginationoptionsmd)


___

### ListDocumentsOptions

Ƭ **ListDocumentsOptions**: [*PaginationOptions*](#interfacestypespaginationoptionsmd) & { `batchId?`: *string* \| *string*[] ; `consentId?`: *string* \| *string*[]  }


___

### ListModelsOptions

Ƭ **ListModelsOptions**: [*PaginationOptions*](#interfacestypespaginationoptionsmd)


___

### ListPredictionsOptions

Ƭ **ListPredictionsOptions**: [*PaginationOptions*](#interfacestypespaginationoptionsmd)


___

### ListSecretsOptions

Ƭ **ListSecretsOptions**: [*PaginationOptions*](#interfacestypespaginationoptionsmd)


___

### ListTransitionOptions

Ƭ **ListTransitionOptions**: [*PaginationOptions*](#interfacestypespaginationoptionsmd) & { `transitionType?`: *string* \| *string*[]  }


___

### ListUsersOptions

Ƭ **ListUsersOptions**: [*PaginationOptions*](#interfacestypespaginationoptionsmd)


___

### ListWorkflowExecutionsOptions

Ƭ **ListWorkflowExecutionsOptions**: [*PaginationOptions*](#interfacestypespaginationoptionsmd) & { `order?`: *ascending* \| *descending* ; `sortBy?`: *startTime* \| *endTime* ; `status?`: *string* \| *string*[]  }


___

### ListWorkflowOptions

Ƭ **ListWorkflowOptions**: [*PaginationOptions*](#interfacestypespaginationoptionsmd)


___

### Log

Ƭ **Log**: *object*

#### Type declaration:


`events` *Record*<any, any\>[]
`logId` *string*
`transitionId`? *string* \| *null*


___

### Model

Ƭ **Model**: *object*

#### Type declaration:


`description` *string* \| *null*
`height` *number*
`modelId` *string*
`name` *string* \| *null*
`width` *number*


___

### ModelList

Ƭ **ModelList**: *object*

#### Type declaration:


`models` [*Model*](#model)[]
`nextToken` *string* \| *null*


___

### PostPredictions

Ƭ **PostPredictions**: [*CreatePredictionsOptions*](#interfacestypescreatepredictionsoptionsmd) & { `documentId`: *string* ; `modelId`: *string*  }


___

### Prediction

Ƭ **Prediction**: [*GroundTruth*](#groundtruth) & { `confidence`: *number*  }


___

### PredictionList

Ƭ **PredictionList**: *object*

#### Type declaration:


`nextToken` *string* \| *null*
`predictions` [*PredictionResponse*](#predictionresponse)[]


___

### PredictionResponse

Ƭ **PredictionResponse**: *object*

#### Type declaration:


`documentId` *string*
`inferenceTime` *number*
`modelId` *string*
`predictionId` *string*
`predictions` [*Prediction*](#prediction)[]
`timestamp` *number*


___

### Secret

Ƭ **Secret**: *object*

#### Type declaration:


`description` *string* \| *null*
`name` *string* \| *null*
`secredId` *string*


___

### SecretList

Ƭ **SecretList**: *object*

#### Type declaration:


`nextToken`? *string* \| *null*
`secrets` [*Secret*](#secret)[]


___

### Transition

Ƭ **Transition**: *object*s

#### Type declaration:


`assets`? *Record*<string, string\>
`description` *string*
`inputJsonSchema` *unknown*
`name` *string*
`outputJsonSchema`? *unknown*
`transitionId` *string*
`transitionType` [*TransitionType*](#transitiontype)


___

### TransitionExecution

Ƭ **TransitionExecution**: *object*

#### Type declaration:


`completedBy` *string* \| *null*
`endTime` *string* \| *null*
`executionId` *string*
`input` *Record*<any, any\>
`startTime` *string* \| *null*
`status` *succeeded* \| *failed* \| *retry* \| *running* \| *rejected*
`transitionId` *string*


___

### TransitionExecutionList

Ƭ **TransitionExecutionList**: *object*

#### Type declaration:


`executions` [*TransitionExecution*](#transitionexecution)[]
`nextToken` *string* \| *null*
`transitionId` *string*


___

### TransitionExecutionListOptions

Ƭ **TransitionExecutionListOptions**: [*PaginationOptions*](#interfacestypespaginationoptionsmd) & { `executionId?`: *string* \| *string*[] ; `order?`: *ascending* \| *descending* ; `sortBy?`: *startTime* \| *endTime* ; `status?`: *succeeded* \| *failed* \| *retry* \| *running* \| *rejected*  }


___

### TransitionList

Ƭ **TransitionList**: *object*

#### Type declaration:


`nextToken`? *string*
`transitions` [*Transition*](#transition)[]


___

### TransitionType

Ƭ **TransitionType**: *docker* \| *manual*


___

### UpdateTransitionOptions

Ƭ **UpdateTransitionOptions**: *object*

#### Type declaration:


`description`? *string*
`inputJsonSchema`? *Record*<any, any\>
`name`? *string*
`outputJsonSchema`? *Record*<any, any\>


___

### UpdateUserOptions

Ƭ **UpdateUserOptions**: *object*

#### Type declaration:


`avatar`? *string* \| *null*
`name`? *string* \| *null*


___

### User

Ƭ **User**: *object*

#### Type declaration:


`avatar` *string* \| *null*
`email` *string*
`name` *string* \| *null*
`userId` *string*


___

### UserList

Ƭ **UserList**: *object*

#### Type declaration:


`nextToken`? *string*
`users` [*User*](#user)[]


___

### Workflow

Ƭ **Workflow**: *object*

#### Type declaration:


`description`? *string*
`name` *string*
`workflowId` *string*


___

### WorkflowExecution

Ƭ **WorkflowExecution**: *object*

#### Type declaration:


`completedBy` *string*[]
`endTime` *string* \| *null*
`executionId` *string*
`input` *Record*<any, any\>
`output` *Record*<any, any\>
`startTime` *string* \| *null*
`status`? *succeeded* \| *failed* \| *running* \| *rejected*
`transitionExecutions` *Record*<string, string[]\> \| *null*
`workflowId` *string*


___

### WorkflowExecutionList

Ƭ **WorkflowExecutionList**: *object*

#### Type declaration:


`executions` *Required*<[*WorkflowExecution*](#workflowexecution)\>[]
`nextToken`? *string*
`status`? *succeeded* \| *failed* \| *running* \| *rejected*
`workflowId` *string*


___

### WorkflowList

Ƭ **WorkflowList**: *object*

#### Type declaration:


`workflows` [*Workflow*](#workflow)[]


___

### WorkflowSpecification

Ƭ **WorkflowSpecification**: *object*

#### Type declaration:


`definition` *object*
`language`? *ASL*
`version`? *1.0.0*

