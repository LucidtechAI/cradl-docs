---
sidebar_position: 2
title: REST API
---

# Rest API

- You can find the Open API specification file in [JSON](pathname:///oas.json) or [YAML](pathname:///oas.yaml)
- Endpoint URL is https://api.lucidtech.ai/v1

## Reference

- See full reference [here](/rest-api-reference)

## Changelog

### 2022-06-24

- Added `evaluation` to `/models/:id/trainings`

### 2022-05-31

- `groundTruthSummary` in `/datasets` is now also counting nested values. This change will not affect existing counts.

### 2022-05-27

- Added optional `postprocessConfig` to `/models`

### 2022-05-19

- Updates to the `enum` type in `fieldConfig`:
    - Enumerations must be unique and from `1` to `512` characters long
    - Maximum number of enumerations allowed is `500`
    - Added support for more characters in enumerations

### 2022-05-10

- You may now set `trainingId` to `null` in `PATCH /models/:id` to make the model `inactive`

### 2022-04-22

- Added `DELETE /paymentMethods/:id`
- Added `GET /paymentMethods/:id`
- Added `GET /paymentMethods`
- Added `PATCH /paymentMethods/:id`
- Added `POST /paymentMethods`
- Added `paymentMethodId` to `PATCH /organizations/:id`
- Fixed bug causing `/models/:id/dataBundles` to fail with `status=failed` if `/datasets` provided have 0 examples of any label defined in `fieldConfig` in `/models` 

### 2022-04-12

- Added `sortBy` query parameter to `GET /documents`
- Added `order` query parameter to `GET /documents`
- Providing `null` as `groundTruth` to `PATCH /documents/:id` is now supported
- Added `sortBy` query parameter to `GET /predictions`
- Added `order` query parameter to `GET /predictions`
- Added `createdBy` to `/predictions`
- Added `createdTime` to `/predictions`
- `timestamp` in `/predictions` is deprecated and will be removed after October 11th, 2022
- Added `planId` to `PATCH /organizations/:id`

### 2022-04-05

- You can now use `/models` with `status=inactive` in `POST /predictions` if you provide a `trainingId` with `status=succeeded`.

### 2022-03-31

- Increased limit of `maxLength` for fields specified in `fieldConfig` in `/models` to `512`.
- Fixed a bug causing users to not be added to organization in `POST /users`.
- Added optional `metadata` to `/users`
- Added optional `trainingId` to `/predictions` response

### 2022-03-16

- `width` and `height` is no longer required in `POST /models` and will default to `801` and `1281`.
- `maxLength` is no longer required for fields specified in `fieldConfig` in `/models`.
- Added type `enum` to fields specified in `fieldConfig` in `/models`. Specify valid enum values by using the key `enum` for fields with `enum` type. See below for example of how to do this.
- Added `monthlyNumberOfActiveModelsUsed`, `monthlyNumberOfFieldPredictionsUsed` and `monthlyNumberOfGpuHoursUsed` to /organizations
- Fixed a bug causing creation of `summary` in `/models/:id/dataBundles` to fail when using number values in JSON for fields of type `digits`.

Example of valid `fieldConfig` after the changes:
```json
{
  "dueDate": {
    "type": "date",
    "description": "Due date on invoice"
  },
  "totalAmount": {
    "type": "amount",
    "maxLength": 12
  },
  "category": {
    "type": "enum",
    "enum": ["TRANSPORTATION", "ACCOMMODATION", "OTHER"]
  }
}
```

### 2022-03-09

- Added trainingId to POST /predictions. You can now make predictions with a trainingId to test out new trainings.
- Added trainingId to /models. The trainingId for a model specifies which training is the one that's currently being used when making predictions.
- Added trainingId to PATCH /models/:id

### 2022-02-02

- Added metadata to /datasets
- Added metadata to /documents
- Added metadata to /models
- Added metadata to /models/:id/trainings

### 2022-01-20

- Now accepting more types for value in groundTruth in /documents. Additionally supported types are number, bool, empty string and nested lists. See the full OAS spec for details.

### 2022-01-06

- Added name and description to POST /documents
- Added name and description to PATCH /documents/:id

### 2022-01-05

- Added retentionInDays to PATCH /datasets/:id. retentionInDays for /documents already associated with datasets will not be affected by changing retentionInDays of datasets.
- Added containsPersonallyIdentifiableInformation to PATCH /datasets/:id

### 2021-12-10

- Removed status 'training' in /models. Status 'training' have been superseded by endpoint /models/:id/trainings. /models with status 'training' have had their status to 'active' or 'inactive'
- Added numberOfRunningTrainings to /models
- Renamed status 'processing' to 'running' in /models/:id/dataBundles
- Renamed status 'ready' to 'succeeded' in /models/:id/dataBundles
- Renamed status 'training' to 'running' in /models/:id/trainings
- Renamed status 'completed' to 'succeeded' in /models/:id/trainings
- Renamed status 'aborted' to 'cancelled' in /models/:id/trainings
- Added email notifications for /models/:id/trainings status change. Email notification will be sent to organization owner and user who initiated the training
- Added trainingsCreated to monthlyUsageSummary in /organizations
- Added PATCH /models/:id/trainings/:id
- Fixed bug causing /workflows/:id/executions to be started twice in some rare cases

### 2021-12-01

- Added /plans endpoint. Use this endpoint to see pricing details for different plans
- Added GET /plans
- Added GET /plans/:id
- Added /models/:id/trainings endpoint. Use this endpoint to initiate model training jobs
- Added GET /models/:id/trainings
- Added POST /models/:id/trainings

### 2021-11-04

- Removed restrictions on updating fieldConfig in /models, you may update fieldConfig regardless of model status
- Added postprocessConfig to POST /predictions. Currently supporting two strategies: BEST_FIRST and BEST_N_PAGES. BEST_FIRST returns predictions from the best page and may skip evaluating later pages if good predictions have already been found. BEST_N_PAGES returns predictions from the best N pages
- Added documentRetentionInDays to /organizations. This value will correspond to the retention of PII as specified in the DPA
- Fixed a bug causing monthlyNumberOfDataBundlesCreated in /organizations to not be reset each month
- Fixed a bug in data bundle creation causing documents with null values in groundTruth to be ignored

### 2021-10-12

- Deleted /batches endpoint. Use /datasets instead
- Added free signup! When signing up you'll get access to the community models. Go to [https://app.cradl.ai/signup](https://app.cradl.ai/signup)
- Removed outdated CORS allowed headers
- Added digits and string types to /models fieldConfig
- Added size limit on input to POST /workflows/:id/executions
- Updated email for signup, invite and verification code

### 2021-09-23

- Added retentionInDays to PATCH /documents/:id

### 2021-09-22

- Added groundTruthSummary to /datasets

### 2021-09-17

- Fixed a bug preventing resources to be deleted sometimes when calling DELETE /documents/:id or DELETE /assets/:id
- Fixed a bug causing negative values to be returned for several fields (e.g. numberOfDocuments, numberOfDataBundles)

### 2021-09-08

- Updated Login UI
- API key is no longer needed

### 2021-08-18

- Fixed a bug preventing a transition execution from starting for transitions with the docker type
- Added GET /datasets/:id
- Extended the period in which temporary credentials are valid upon first time invitation to Typenode or Flyt from 30 days to 90 days
- Listing endpoints like DELETE /documents and GET /documents should now respond faster
- Added more descriptive error message for 404 responses
- Added createdBy, updatedTime, updatedBy to /appClients
- Added createdTime, createdBy, updatedTime, updatedBy to /users
- Added createdTime, createdBy, updatedTime, updatedBy to /assets
- Added createdTime, createdBy, updatedTime, updatedBy to /documents
- Added createdBy, updatedBy to /models
- Added createdBy, updatedBy to /models/:id/dataBundles
- Added createdTime, createdBy, updatedTime, updatedBy to /secrets
- Added createdTime, createdBy, updatedTime, updatedBy to /transitions
- Added createdTime, createdBy, updatedTime, updatedBy to /workflows
- Added createdBy, updatedBy to /datasets
- Added updatedTime, updatedBy to /organizations
- Added retentionInDays to /documents. For documents with a datasetId, the minimum retentionInDays of the dataset and the document is chosen

### 2021-07-08

- Extended the period in which temporary credentials are valid upon first time invitation to Typenode or Flyt from 7 days to 30 days
- Added timeoutInSeconds to /transitions
- Fixed a bug preventing login to complete successfully in Typenode and Flyt
- Fixed a bug preventing expired users from getting new temporary credentials when invited again

### 2021-07-01

- Added datasetId query parameter to DELETE /documents
- Added datasetId query parameter to GET /documents
- Fixed a bug preventing completion config in /workflows to be executed in some situations
- Added datasetId to PATCH /documents/:id
- Fixed error in JSON schema for /datasets, numDocuments -> numberOfDocuments

### 2021-06-25

- Deprecated /batches endpoint. It's replaced by /datasets. Your current batches will be unaffected until 2021-09-06, after which we will remove the entire endpoint and all of its data. Documents in batches will not be affected, only the batches themselves. Until 2021-09-06 you will not be able to create new batches. Please consider replacing your batches with datasets.
- Added POST /datasets
- Added GET /datasets
- Added PATCH /datasets/:id
- Added DELETE /datasets/:id
- Added POST /models/:id/dataBundles
- Added GET /models/:id/dataBundles
- Added PATCH /models/:id/dataBundles/:id
- Added DELETE /models/:id/dataBundles/:id
- Fixed a bug causing incorrect error messages to be returned from the API
- POST /transitions will now attempt to return appropriate status 400 error message when imageUrl is incomplete
- PATCH /transitions/:id/executions/:id will now return status 400 error message when attempting to PATCH a timed out transition execution

### 2021-06-16

- Added loginUrls, defaultLoginUrl to PATCH /appClients/:id

### 2021-06-10

- Added GET /organizations/:id
- Added PATCH /organizations/:id
- Fixed a bug preventing the first log message to be written for workflow executions
- Updated the email invite and verification code layout
- Added numberOfRunningExecutions to /workflows

### 2021-05-26

- Added DELETE /models/:id
- description in /models fieldConfig is no longer required

### 2021-05-19

- Added loginUrls, defaultLoginUrl to /appClients
- Link to login button in invitation email now sends you to the app corresponding to the defaultLoginUrl in /appClients

### 2021-05-12

- Added PATCH /batches/:id
- Added PATCH /appClients/:id
- Added GET /models/:id
- Added PATCH /models/:id
- Added POST /models
- Updated OAuth2 scopes
- Added new possible value 'inactive' for status in /models

### 2021-04-27

- Added storageLocation, retentionInDays, containsPersonallyIdentifiableInformation to /batches
- Added DELETE /batches/:id. Documents in batch must be deleted before deleting the batch
- Added batchId query parameter to DELETE /documents

### 2021-04-23

- Added GET /logs. Use query parameters workflowId, workflowExecutionId, transitionId, transitionExecutionId to filter.
- Added default retry configuration for workflow transitions that don't explicitly define one.
- Added startTime, transitionExecutionId, workflowExecutionId to /logs

### 2021-04-14

- Now possible to create public app clients by using the generateSecret parameter set to false (defaults to true) and providing callback and logout urls
- Added createdTime, apiKey, callbackUrls, logoutUrls, hasSecret to /appClients
- Now preventing users from deleting themselves using DELETE /users/:id 
- Now preventing app clients from deleting itself using DELETE /appClients/:id

### 2021-04-13

- Added GET /batches
- Added createdTime and numDocuments to /batches
- Added POST /appClients
- Added GET /appClients
- Added DELETE /appClients/:id
- Added createdTime, updatedTime, fieldConfig, preprocessConfig and status to /models

### 2021-04-09

- Added DELETE /secrets/:id
- Added DELETE /assets/:id
- Added paging to DELETE /documents. Supports deleting up to 1000 documents each API call. 

