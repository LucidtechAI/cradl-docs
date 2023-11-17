---
sidebar_position: 3
title: REST API
---

# Rest API

- You can find the Open API specification file in [JSON](pathname:///oas.json) or [YAML](pathname:///oas.yaml)
- Endpoint URL is https://api.lucidtech.ai/v1

## Reference

- See full reference [here](/rest-api-reference)
- See full reference on [Postman](https://www.postman.com/cradlai)

## Changelog

### 2023-11-17

- It is now possible to set up an email address which can be used to execute workflows. JPEG, PNG, TIFF and PDF 
attachments in the email will each start en execution of the specific workflow. 
- Added optional `emailConfig` to `POST /workflows`
- Added optional `emailConfig` to `PATCH /workflows/:id`

### 2023-10-25

- Added `GET /models/:id/dataBundles/:id`
- Added `GET /models/:id/trainings/:id`

### 2023-10-02

- Added new endpoint `/datasets/:id/transformations`. Transformations are operations performed on all documents in a
dataset. Currently, the only supported transformation is `remove-duplicates`.
- Added `GET /datasets/:id/transformations`
- Added `POST /datasets/:id/transformations`
- Added `DELETE /datasets/:id/transformations/:id`
- Added optional `pages` to `groundTruth` for `/documents`. Specifying `pages` gives you better results when training
models.

### 2023-09-14

- Added optional query parameter `modelId` to `GET /predictions`
- Added new permission action `delegate` in `/roles` that specifies which roles can be delegated to other resources 
such as `/users` and `/appClients`. Trying to assign roles to `/users` and `/appClients` without the `delegate` 
permission action will result in a `403 Forbidden`

### 2023-09-07

- Added optional `metadata` to `/workflows`
- Removed deprecated `avatar`, `name` and `email` from `/users`

### 2023-08-25

- Added new endpoint `/roles`. Roles can be attached to `/users` and `/appClients` to limit which API resources they 
can access.
- Added `GET /roles`
- Added `GET /roles/:id`
- Added `roleIds` to `/users`
- Added `roleIds` to `/appClients`

### 2023-06-27

- Added fileserver endpoint that can be utilized to upload larger files than 4.5MB and get thumbnails and resized
images of documents. The fileserver URL is contained in the response body of `/documents` and accepts `GET` and `PUT`
operations.
- Added `fileUrl` to `/documents`. Use this URL to access the file using your Authorization token.
- `content` and `contentType` is now optional in `POST /documents`. Instead of providing `content` and `contentType`, 
you may upload the document to `fileUrl` directly without base64 encoding. The maximum document size you can upload to
the fileserver is 64MB.

### 2023-06-14

- Added optional `preprocessConfig` to `POST /predictions`. `autoRotate`, `imageQuality`, `maxPages` and `rotation` 
should now be specified as part of `preprocessConfig` instead and will be deprecated June 14th 2024.
- Added optional `pages` to `preprocessConfig` to specify which specific pages to process when invoking 
`POST /predictions`. `pages` is 0-indexed and supports negative indices for reverse indexing such that index `0`
translates to the first page of the document and `-1` to the last page of the document.
- All individual parameters in `preprocessConfig` are now optional and may be specified as needed.

### 2023-06-07

- Added new possible `status` `running-final-evaluation` for `/models/:id/trainings` which takes place after `running`
and before `succeeded`

### 2023-03-23

- Added `preprocessConfig` and `postprocessConfig` to `/predictions`
- Removed deprecated `width` and `height` from `/models`

### 2023-03-02

- Added signin with Google.
- Added `GET /profiles/:id`, `GET /profiles/me`.
- Added `PATCH /profiles/me`.
- Added `POST /organizations`.
- Added `GET /organizations`.
- Deprecated `avatar`, `name` and `email` in `/users`, they will be removed May 20th 2023. Use `/profiles` instead
- Removed `POST /signup`.

### 2023-02-27

- Added optional `rotation` to `POST /predictions`

### 2023-02-10

- Added `page` to predictions in `/predictions` when page information is available.
- Added `owner` query parameter to `GET /models`. Use this feature to list pre-trained models. `GET /models?owner=las:organization:cradl`
- Added support for creating predictions using a pre-trained model. Specify the organization that owns the model to `POST /predictions` using the composite `modelId` form (e.g. `las:organization:cradl/las:model:invoice`)

### 2022-12-20

- Added `warmStartConfig` to `POST /models/:id/trainings`. Use this parameter to specify which `trainingId` to continue training from. 
- Added support for nested output for `/predictions`.

### 2022-10-13

- Removed deprecated `timestamp` from `/predictions`
- Deprecated `height`, `width` in `/models`. They will be deleted on December 12th, 2022.

### 2022-09-28

- Added `parameters` to `PATCH /transitions/:id`. Use `parameters` to update transitions with `transitionType=docker` or `transitionType=manual` specific parameters.
- Added `parameters.cpu`, `parameters.memory`, `parameters.imageUrl`, `parameters.secretId`, `parameters.environment` and `parameters.environmentSecrets` to `PATCH /transitions/:id` for `transitionType=docker`.
- Added `parameters.assets` to `PATCH /transitions/:id` for `transitionType=manual`.
- Deprecated `environment`, `environmentSecrets` and `assets` in `PATCH /transitions/:id` and will be removed on December 16th. Use `parameters.environment`, `parameters.environmentSecrets` and `parameters.assets` instead.
- Added query parameter `fromStartTime` and `toStartTime` to `GET /workflows/:id/executions`.
- Fixed a bug causing `GET /documents/:id` to fail with status code 500.
- Fixed a bug causing `POST /predictions` to fail with status code 500.

### 2022-09-27

- Fixed a bug causing `POST /predictions` to fail with TIFF images containing 2 or more pages.
- Fixed a bug causing community `/datasets` and `/models` to not be added to new users. Existing users that were affected by this bug must contact support to have them added to their organization.
- Added additional `cpu` (`512`, `1024`) and `memory` (`4096`, `8192`) options for docker `/transitions`.

### 2022-09-15

- Added query parameter `documentId` to `GET /documents`
- Fixed a bug causing `/models/:id/dataBundles` to fail with status `failed` when certain combinations of `ground_truth` value `types` and `model.fieldConfig` were present.
- Fixed a bug causing `/models/:id/dataBundles` to show `validity=1.0` when no `ground_truth` values were successfully parsed.
- Fixed a bug causing `/models/:id/dataBundles` to fail with status `failed` when no documents with valid `ground_truth` values were present.

### 2022-09-13

- Several improvements have been made to `summary` in `/models/:id/dataBundles`. You can now see which `/documents` are duplicates, which `groundTruth` values are duplicates, the distribution of characters and lengths of your data. You can also see which `documents` had errors in them while processing the data and which labels in the `groundTruth` that were erroneous. For a complete list of error codes see [list of error codes](/concepts/training-data.mdx#error-handling)
- Removed deprecated types `all`, `alphanum`, `alphanumext`, `letter`, `number` and `phone` in `fieldConfig` in `/models`. 
- Added type `numeric` to `fieldConfig` in `/models`
- Added `contentMD5` to `/documents`
- Added `retentionInDays` to `/models/:id/dataBundles`. This change reflects that PII can occur in data bundles and should thus be removed in accordance with the DPA.

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

