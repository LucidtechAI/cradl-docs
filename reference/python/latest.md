# las package

## Module contents


### class las.Client(credentials: Optional[las.credentials.Credentials] = None)
Bases: `object`

A low level client to invoke api methods from Lucidtech AI Services.


#### create_app_client(generate_secret=True, logout_urls=None, callback_urls=None, login_urls=None, default_login_url=None, \*\*optional_args)
Creates an appClient, calls the POST /appClients endpoint.

```python
>>> from las.client import Client
>>> client = Client()
>>> client.create_app_client(name='<name>', description='<description>')
```


* **Parameters**

    
    * **name** (*Optional**[**str**]*) – Name of the appClient


    * **description** (*Optional**[**str**]*) – Description of the appClient


    * **generate_secret** (*Boolean*) – Set to False to ceate a Public app client, default: True


    * **logout_urls** (*List**[**str**]*) – List of logout urls


    * **callback_urls** (*List**[**str**]*) – List of callback urls


    * **login_urls** (*List**[**str**]*) – List of login urls


    * **default_login_url** (*str*) – Default login url



* **Returns**

    AppClient response from REST API



* **Return type**

    dict



* **Raises**

    `InvalidCredentialsException`, `TooManyRequestsException`, `LimitExceededException`, `requests.exception.RequestException`



#### create_asset(content: Union[bytes, bytearray, str, pathlib.Path, io.IOBase], \*\*optional_args)
Creates an asset, calls the POST /assets endpoint.

```python
>>> from las.client import Client
>>> client = Client()
>>> client.create_asset(b'<bytes data>')
```


* **Parameters**

    
    * **content** (*Content*) – Content to POST


    * **name** (*Optional**[**str**]*) – Name of the asset


    * **description** (*Optional**[**str**]*) – Description of the asset



* **Returns**

    Asset response from REST API



* **Return type**

    dict



* **Raises**

    `InvalidCredentialsException`, `TooManyRequestsException`, `LimitExceededException`, `requests.exception.RequestException`



#### create_batch(\*\*optional_args)
Creates a batch, calls the POST /batches endpoint.

```python
>>> from las.client import Client
>>> client = Client()
>>> client.create_batch(description='<description>')
```


* **Parameters**

    
    * **name** (*Optional**[**str**]*) – Name of the batch


    * **description** (*Optional**[**str**]*) – Description of the batch



* **Returns**

    Batch response from REST API



* **Return type**

    dict



* **Raises**

    `InvalidCredentialsException`, `TooManyRequestsException`, `LimitExceededException`, `requests.exception.RequestException`



#### create_data_bundle(model_id, dataset_ids, \*\*optional_args)
Creates a data bundle, calls the POST /models/{modelId}/dataBundles endpoint.


* **Parameters**

    
    * **model_id** (*str*) – Id of the model


    * **dataset_ids** (*List**[**str**]*) – Dataset Ids that will be included in the data bundle


    * **name** (*Optional**[**str**]*) – Name of the data bundle


    * **description** (*Optional**[**str**]*) – Description of the data bundle



* **Returns**

    Data Bundle response from REST API



* **Return type**

    dict



* **Raises**

    `InvalidCredentialsException`, `TooManyRequestsException`, `LimitExceededException`, `requests.exception.RequestException`



#### create_dataset(\*\*optional_args)
Creates a dataset, calls the POST /datasets endpoint.


* **Parameters**

    
    * **name** (*Optional**[**str**]*) – Name of the dataset


    * **description** (*Optional**[**str**]*) – Description of the dataset



* **Returns**

    Dataset response from REST API



* **Return type**

    dict



* **Raises**

    `InvalidCredentialsException`, `TooManyRequestsException`, `LimitExceededException`, `requests.exception.RequestException`



#### create_document(content: Union[bytes, bytearray, str, pathlib.Path, io.IOBase], content_type: Optional[str] = None, \*, consent_id: Optional[str] = None, batch_id: Optional[str] = None, dataset_id: Optional[str] = None, ground_truth: Optional[Sequence[Dict[str, str]]] = None, retention_in_days: Optional[int] = None)
Creates a document, calls the POST /documents endpoint.

```python
>>> from las.client import Client
>>> client = Client()
>>> client.create_document(b'<bytes data>', 'image/jpeg', consent_id='<consent id>')
```


* **Parameters**

    
    * **content** (*Content*) – Content to POST


    * **content_type** (*str*) – MIME type for the document


    * **consent_id** (*Optional**[**str**]*) – Id of the consent that marks the owner of the document


    * **batch_id** (*Optional**[**str**]*) – Id of the associated batch


    * **dataset_id** (*Optional**[**str**]*) – Id of the associated dataset


    * **ground_truth** – List of items {‘label’: label, ‘value’: value}


representing the ground truth values for the document
:type ground_truth: Optional[Sequence[Dict[str, str]]]
:return: Document response from REST API
:rtype: dict


* **Raises**

    `InvalidCredentialsException`, `TooManyRequestsException`, `LimitExceededException`, `requests.exception.RequestException`



#### create_model(width: int, height: int, field_config: dict, \*, preprocess_config: Optional[dict] = None, name: Optional[str] = None, description: Optional[str] = None, \*\*optional_args)
Creates a model, calls the POST /models endpoint.


* **Parameters**

    
    * **width** (*int*) – The number of pixels to be used for the input image width of your model


    * **height** (*int*) – The number of pixels to be used for the input image height of your model


    * **field_config** (*dict*) – Specification of the fields that the model is going to predict


    * **preprocess_config** (*dict*) – Specification of the processing steps prior to the prediction of an image


    * **name** (*Optional**[**str**]*) – Name of the model


    * **description** (*Optional**[**str**]*) – Description of the model



* **Returns**

    Model response from REST API



* **Return type**

    dict



* **Raises**

    `InvalidCredentialsException`, `TooManyRequestsException`, `LimitExceededException`, `requests.exception.RequestException`



#### create_prediction(document_id: str, model_id: str, \*, max_pages: Optional[int] = None, auto_rotate: Optional[bool] = None, image_quality: Optional[str] = None)
Create a prediction on a document using specified model, calls the POST /predictions endpoint.

```python
>>> from las.client import Client
>>> client = Client()
>>> client.create_prediction(document_id='<document id>', model_id='<model id>')
```


* **Parameters**

    
    * **document_id** (*str*) – Id of the document to run inference and create a prediction on


    * **model_id** (*str*) – Id of the model to use for inference


    * **max_pages** (*Optional**[**int**]*) – Maximum number of pages to run predictions on


    * **auto_rotate** (*Optional**[**bool**]*) – Whether or not to let the API try different rotations on            the document when running predictions


    * **image_quality** (*Optional**[**int**]*) – image quality for prediction “LOW|HIGH”.             high quality could give better result but will also take longer time.



* **Returns**

    Prediction response from REST API



* **Return type**

    dict



* **Raises**

    `InvalidCredentialsException`, `TooManyRequestsException`, `LimitExceededException`, `requests.exception.RequestException`



#### create_secret(data: dict, \*\*optional_args)
Creates an secret, calls the POST /secrets endpoint.

```python
>>> from las.client import Client
>>> client = Client()
>>> data = {'username': '<username>', 'password': '<password>'}
>>> client.create_secret(data, description='<description>')
```


* **Parameters**

    
    * **data** (*str*) – Dict containing the data you want to keep secret


    * **name** (*Optional**[**str**]*) – Name of the secret


    * **description** (*Optional**[**str**]*) – Description of the secret



* **Returns**

    Secret response from REST API



* **Return type**

    dict



* **Raises**

    `InvalidCredentialsException`, `TooManyRequestsException`, `LimitExceededException`, `requests.exception.RequestException`



#### create_transition(transition_type: str, \*, in_schema: Optional[dict] = None, out_schema: Optional[dict] = None, parameters: Optional[dict] = None, \*\*optional_args)
Creates a transition, calls the POST /transitions endpoint.

```python
>>> import json
>>> from pathlib import Path
>>> from las.client import Client
>>> client = Client()
>>> in_schema = {'$schema': 'https://json-schema.org/draft-04/schema#', 'title': 'in', 'properties': {...} }
>>> out_schema = {'$schema': 'https://json-schema.org/draft-04/schema#', 'title': 'out', 'properties': {...} }
>>> # A typical docker transition
>>> docker_params = {
>>>     'imageUrl': '<image_url>',
>>>     'credentials': {'username': '<username>', 'password': '<password>'}
>>> }
>>> client.create_transition('docker', in_schema=in_schema, out_schema=out_schema, params=docker_params)
>>> # A manual transition with UI
>>> assets = {'jsRemoteComponent': 'las:asset:<hex-uuid>', '<other asset name>': 'las:asset:<hex-uuid>'}
>>> manual_params = {'assets': assets}
>>> client.create_transition('manual', in_schema=in_schema, out_schema=out_schema, params=manual_params)
```


* **Parameters**

    
    * **transition_type** (*str*) – Type of transition “docker”|”manual”


    * **in_schema** (*Optional**[**dict**]*) – Json-schema that defines the input to the transition


    * **out_schema** (*Optional**[**dict**]*) – Json-schema that defines the output of the transition


    * **name** (*Optional**[**str**]*) – Name of the transition


    * **parameters** (*Optional**[**dict**]*) – Parameters to the corresponding transition type


    * **description** (*Optional**[**str**]*) – Description of the transition



* **Returns**

    Transition response from REST API



* **Return type**

    dict



* **Raises**

    `InvalidCredentialsException`, `TooManyRequestsException`, `LimitExceededException`, `requests.exception.RequestException`



#### create_user(email: str, \*, app_client_id, \*\*optional_args)
Creates a new user, calls the POST /users endpoint.

```python
>>> from las.client import Client
>>> client = Client()
>>> client.create_user('<email>', name='John Doe')
```


* **Parameters**

    
    * **email** (*str*) – Email to the new user


    * **name** (*Optional**[**str**]*) – Name of the user


    * **avatar** (*Optional**[**str**]*) – base64 encoded JPEG avatar of the user



* **Returns**

    User response from REST API



* **Return type**

    dict



* **Raises**

    `InvalidCredentialsException`, `TooManyRequestsException`, `LimitExceededException`, `requests.exception.RequestException`



#### create_workflow(specification: dict, \*, error_config: Optional[dict] = None, completed_config: Optional[dict] = None, \*\*optional_args)
Creates a new workflow, calls the POST /workflows endpoint.
Check out Lucidtech’s tutorials for more info on how to create a workflow.

```python
>>> from las.client import Client
>>> from pathlib import Path
>>> client = Client()
>>> specification = {'language': 'ASL', 'version': '1.0.0', 'definition': {...}}
>>> error_config = {'email': '<error-recipient>'}
>>> client.create_workflow(specification, error_config=error_config)
```


* **Parameters**

    
    * **specification** (*dict*) – Specification of the workflow,
    currently supporting ASL: [https://states-language.net/spec.html](https://states-language.net/spec.html)


    * **name** (*Optional**[**str**]*) – Name of the workflow


    * **description** (*Optional**[**str**]*) – Description of the workflow


    * **error_config** (*Optional**[**dict**]*) – Configuration of error handler


    * **completed_config** (*Optional**[**dict**]*) – Configuration of a job to run whenever a workflow execution ends



* **Returns**

    Workflow response from REST API



* **Return type**

    dict



* **Raises**

    `InvalidCredentialsException`, `TooManyRequestsException`, `LimitExceededException`, `requests.exception.RequestException`



#### delete_app_client(app_client_id: str)
Delete the appClient with the provided appClientId, calls the DELETE /appClients/{appClientId} endpoint.

```python
>>> from las.client import Client
>>> client = Client()
>>> client.delete_app_client('<app_client_id>')
```


* **Parameters**

    **app_client_id** (*str*) – Id of the appClient



* **Returns**

    AppClient response from REST API



* **Return type**

    dict



* **Raises**

    `InvalidCredentialsException`, `TooManyRequestsException`, `LimitExceededException`, `requests.exception.RequestException`



#### delete_asset(asset_id: str)
Delete the asset with the provided asset_id, calls the DELETE /assets/{assetId} endpoint.

```python
>>> from las.client import Client
>>> client = Client()
>>> client.delete_asset('<asset_id>')
```


* **Parameters**

    **asset_id** (*str*) – Id of the asset



* **Returns**

    Asset response from REST API



* **Return type**

    dict



* **Raises**

    `InvalidCredentialsException`, `TooManyRequestsException`, `LimitExceededException`, `requests.exception.RequestException`



#### delete_batch(batch_id: str, delete_documents=False)
Delete the batch with the provided batch_id, calls the DELETE /batches/{batchId} endpoint.

```python
>>> from las.client import Client
>>> client = Client()
>>> client.delete_batch('<batch_id>')
```


* **Parameters**

    
    * **batch_id** (*str*) – Id of the batch


    * **delete_documents** (*bool*) – Set to true to delete documents in batch before deleting batch



* **Returns**

    Batch response from REST API



* **Return type**

    dict



* **Raises**

    `InvalidCredentialsException`, `TooManyRequestsException`, `LimitExceededException`, `requests.exception.RequestException`



#### delete_data_bundle(model_id: str, data_bundle_id: str)
Delete the data bundle with the provided data_bundle_id,
calls the DELETE /models/{modelId}/dataBundles/{dataBundleId} endpoint.


* **Parameters**

    
    * **model_id** (*str*) – Id of the model


    * **data_bundle_id** (*str*) – Id of the data bundle



* **Returns**

    Data Bundle response from REST API



* **Return type**

    dict



* **Raises**

    `InvalidCredentialsException`, `TooManyRequestsException`, `LimitExceededException`, `requests.exception.RequestException`



#### delete_dataset(dataset_id: str, delete_documents: bool = False)
Delete the dataset with the provided dataset_id, calls the DELETE /datasets/{datasetId} endpoint.


* **Parameters**

    
    * **dataset_id** (*str*) – Id of the dataset


    * **delete_documents** (*bool*) – Set to true to delete documents in dataset before deleting dataset



* **Returns**

    Dataset response from REST API



* **Return type**

    dict



* **Raises**

    `InvalidCredentialsException`, `TooManyRequestsException`, `LimitExceededException`, `requests.exception.RequestException`



#### delete_document(document_id: str)
Delete the document with the provided document_id, calls the DELETE /documents/{documentId} endpoint.

```python
>>> from las.client import Client
>>> client = Client()
>>> client.delete_document('<document_id>')
```


* **Parameters**

    **document_id** (*str*) – Id of the document



* **Returns**

    Model response from REST API



* **Return type**

    dict



* **Raises**

    `InvalidCredentialsException`, `TooManyRequestsException`, `LimitExceededException`, `requests.exception.RequestException`



#### delete_documents(\*, batch_id: Optional[Union[str, List[str]]] = None, consent_id: Optional[Union[str, List[str]]] = None, dataset_id: Optional[Union[str, List[str]]] = None, max_results: Optional[int] = None, next_token: Optional[str] = None, delete_all: Optional[bool] = False)
Delete documents with the provided consent_id, calls the DELETE /documents endpoint.

```python
>>> from las.client import Client
>>> client = Client()
>>> client.delete_documents(consent_id='<consent id>')
```


* **Parameters**

    
    * **batch_id** (*Optional**[**Queryparam**]*) – Ids of the batches to be deleted


    * **consent_id** (*Optional**[**Queryparam**]*) – Ids of the consents that marks the owner of the document


    * **dataset_id** (*Optional**[**Queryparam**]*) – Ids of the datasets to be deleted


    * **max_results** (*Optional**[**int**]*) – Maximum number of documents that will be deleted


    * **next_token** (*Optional**[**str**]*) – A unique token for each page, use the returned token to retrieve the next page.


    * **delete_all** – Delete all documents that match the given parameters doing multiple API calls if necessary.


Will throw an error if parameter max_results is also specified.
:type delete_all: Optional[bool]
:return: Documents response from REST API
:rtype: dict


* **Raises**

    `InvalidCredentialsException`, `TooManyRequestsException`, `LimitExceededException`, `requests.exception.RequestException`



#### delete_model(model_id: str)
Delete the model with the provided model_id, calls the DELETE /models/{modelId} endpoint.

```python
>>> from las.client import Client
>>> client = Client()
>>> client.delete_model('<model_id>')
```


* **Parameters**

    **model_id** (*str*) – Id of the model



* **Returns**

    Model response from REST API



* **Return type**

    dict



* **Raises**

    `InvalidCredentialsException`, `TooManyRequestsException`, `LimitExceededException`, `requests.exception.RequestException`



#### delete_secret(secret_id: str)
Delete the secret with the provided secret_id, calls the DELETE /secrets/{secretId} endpoint.

```python
>>> from las.client import Client
>>> client = Client()
>>> client.delete_secret('<secret_id>')
```


* **Parameters**

    **secret_id** (*str*) – Id of the secret



* **Returns**

    Secret response from REST API



* **Return type**

    dict



* **Raises**

    `InvalidCredentialsException`, `TooManyRequestsException`, `LimitExceededException`, `requests.exception.RequestException`



#### delete_transition(transition_id: str)
Delete the transition with the provided transition_id, calls the DELETE /transitions/{transitionId} endpoint.

    Will fail if transition is in use by one or more workflows.

```python
>>> from las.client import Client
>>> client = Client()
>>> client.delete_transition('<transition_id>')
```


* **Parameters**

    **transition_id** (*str*) – Id of the transition



* **Returns**

    Transition response from REST API



* **Return type**

    dict



* **Raises**

    `InvalidCredentialsException`, `TooManyRequestsException`, `LimitExceededException`, `requests.exception.RequestException`



#### delete_user(user_id: str)
Delete the user with the provided user_id, calls the DELETE /users/{userId} endpoint.

```python
>>> from las.client import Client
>>> client = Client()
>>> client.delete_user('<user_id>')
```


* **Parameters**

    **user_id** (*str*) – Id of the user



* **Returns**

    User response from REST API



* **Return type**

    dict



* **Raises**

    `InvalidCredentialsException`, `TooManyRequestsException`, `LimitExceededException`, `requests.exception.RequestException`



#### delete_workflow(workflow_id: str)
Delete the workflow with the provided workflow_id, calls the DELETE /workflows/{workflowId} endpoint.

```python
>>> from las.client import Client
>>> client = Client()
>>> client.delete_workflow('<workflow_id>')
```


* **Parameters**

    **workflow_id** (*str*) – Id of the workflow



* **Returns**

    Workflow response from REST API



* **Return type**

    dict



* **Raises**

    `InvalidCredentialsException`, `TooManyRequestsException`, `LimitExceededException`, `requests.exception.RequestException`



#### delete_workflow_execution(workflow_id: str, execution_id: str)
Deletes the execution with the provided execution_id from workflow_id,
calls the DELETE /workflows/{workflowId}/executions/{executionId} endpoint.

```python
>>> from las.client import Client
>>> client = Client()
>>> client.delete_workflow_execution('<workflow_id>', '<execution_id>')
```


* **Parameters**

    
    * **workflow_id** (*str*) – Id of the workflow


    * **execution_id** (*str*) – Id of the execution



* **Returns**

    WorkflowExecution response from REST API



* **Return type**

    dict



* **Raises**

    `InvalidCredentialsException`, `TooManyRequestsException`, `LimitExceededException`, `requests.exception.RequestException`



#### execute_transition(transition_id: str)
Start executing a manual transition, calls the POST /transitions/{transitionId}/executions endpoint.

```python
>>> from las.client import Client
>>> client = Client()
>>> client.execute_transition('<transition_id>')
```


* **Parameters**

    **transition_id** (*str*) – Id of the transition



* **Returns**

    Transition execution response from REST API



* **Return type**

    dict



* **Raises**

    `InvalidCredentialsException`, `TooManyRequestsException`, `LimitExceededException`, `requests.exception.RequestException`



#### execute_workflow(workflow_id: str, content: dict)
Start a workflow execution, calls the POST /workflows/{workflowId}/executions endpoint.

```python
>>> from las.client import Client
>>> from pathlib import Path
>>> client = Client()
>>> content = {...}
>>> client.execute_workflow('<workflow_id>', content)
```


* **Parameters**

    
    * **workflow_id** (*str*) – Id of the workflow


    * **content** (*dict*) – Input to the first step of the workflow



* **Returns**

    Workflow execution response from REST API



* **Return type**

    dict



* **Raises**

    `InvalidCredentialsException`, `TooManyRequestsException`, `LimitExceededException`, `requests.exception.RequestException`



#### get_asset(asset_id: str)
Get asset, calls the GET /assets/{assetId} endpoint.

```python
>>> from las.client import Client
>>> client = Client()
>>> client.get_asset(asset_id='<asset id>')
```


* **Parameters**

    **asset_id** (*str*) – Id of the asset



* **Returns**

    Asset response from REST API with content



* **Return type**

    dict



* **Raises**

    `InvalidCredentialsException`, `TooManyRequestsException`, `LimitExceededException`, `requests.exception.RequestException`



#### get_dataset(dataset_id: str)
Get dataset, calls the GET /datasets/{datasetId} endpoint.


* **Parameters**

    **dataset_id** (*str*) – Id of the dataset



* **Returns**

    Dataset response from REST API



* **Return type**

    dict



* **Raises**

    `InvalidCredentialsException`, `TooManyRequestsException`, `LimitExceededException`, `requests.exception.RequestException`



#### get_document(document_id: str)
Get document, calls the GET /documents/{documentId} endpoint.

```python
>>> from las.client import Client
>>> client = Client()
>>> client.get_document('<document id>')
```


* **Parameters**

    **document_id** (*str*) – Id of the document



* **Returns**

    Document response from REST API



* **Return type**

    dict



* **Raises**

    `InvalidCredentialsException`, `TooManyRequestsException`, `LimitExceededException`, `requests.exception.RequestException`



#### get_log(log_id)
get log, calls the GET /logs/{logId} endpoint.

```python
>>> from las.client import Client
>>> client = Client()
>>> client.get_log('<log_id>')
```


* **Parameters**

    **log_id** (*str*) – Id of the log



* **Returns**

    Log response from REST API



* **Return type**

    dict



* **Raises**

    `InvalidCredentialsException`, `TooManyRequestsException`, `LimitExceededException`, `requests.exception.RequestException`



#### get_model(model_id: str)
Get a model, calls the GET /models/{modelId} endpoint.


* **Parameters**

    **model_id** (*str*) – The Id of the model



* **Returns**

    Model response from REST API



* **Return type**

    dict



* **Raises**

    `InvalidCredentialsException`, `TooManyRequestsException`, `LimitExceededException`, `requests.exception.RequestException`



#### get_organization(organization_id: str)
Get an organization, calls the GET /organizations/{organizationId} endpoint.


* **Parameters**

    **organization_id** (*str*) – The Id of the organization



* **Returns**

    Organization response from REST API



* **Return type**

    dict



* **Raises**

    `InvalidCredentialsException`, `TooManyRequestsException`, `LimitExceededException`, `requests.exception.RequestException`



#### get_transition(transition_id: str)
Get the transition with the provided transition_id, calls the GET /transitions/{transitionId} endpoint.

```python
>>> from las.client import Client
>>> client = Client()
>>> client.get_transition('<transition_id>')
```


* **Parameters**

    **transition_id** (*str*) – Id of the transition



* **Returns**

    Transition response from REST API



* **Return type**

    dict



* **Raises**

    `InvalidCredentialsException`, `TooManyRequestsException`, `LimitExceededException`, `requests.exception.RequestException`



#### get_transition_execution(transition_id: str, execution_id: str)
Get an execution of a transition, calls the GET /transitions/{transitionId}/executions/{executionId} endpoint

```python
>>> from las.client import Client
>>> client = Client()
>>> client.get_transition_execution('<transition_id>', '<execution_id>')
```


* **Parameters**

    
    * **transition_id** (*str*) – Id of the transition


    * **execution_id** (*str*) – Id of the executions



* **Returns**

    Transition execution responses from REST API



* **Return type**

    dict



* **Raises**

    `InvalidCredentialsException`, `TooManyRequestsException`, `LimitExceededException`, `requests.exception.RequestException`



#### get_user(user_id: str)
Get information about a specific user, calls the GET /users/{user_id} endpoint.

```python
>>> from las.client import Client
>>> client = Client()
>>> client.get_user('<user_id>')
```


* **Parameters**

    **user_id** (*str*) – Id of the user



* **Returns**

    User response from REST API



* **Return type**

    dict



* **Raises**

    `InvalidCredentialsException`, `TooManyRequestsException`, `LimitExceededException`, `requests.exception.RequestException`



#### get_workflow(workflow_id: str)
Get the workflow with the provided workflow_id, calls the GET /workflows/{workflowId} endpoint.

```python
>>> from las.client import Client
>>> client = Client()
>>> client.get_workflow('<workflow_id>')
```


* **Parameters**

    **workflow_id** (*str*) – Id of the workflow



* **Returns**

    Workflow response from REST API



* **Return type**

    dict



* **Raises**

    `InvalidCredentialsException`, `TooManyRequestsException`, `LimitExceededException`, `requests.exception.RequestException`



#### get_workflow_execution(workflow_id: str, execution_id: str)
Get a workflow execution, calls the GET /workflows/{workflow_id}/executions/{execution_id} endpoint.

```python
>>> from las.client import Client
>>> client = Client()
>>> client.get_workflow_execution('<workflow_id>', '<execution_id>')
```


* **Parameters**

    
    * **workflow_id** (*str*) – Id of the workflow that performs the execution


    * **execution_id** (*str*) – Id of the execution to get



* **Returns**

    Workflow execution response from REST API



* **Return type**

    dict



* **Raises**

    `InvalidCredentialsException`, `TooManyRequestsException`, `LimitExceededException`, `requests.exception.RequestException`



#### list_app_clients(\*, max_results: Optional[int] = None, next_token: Optional[str] = None)
List appClients available, calls the GET /appClients endpoint.

```python
>>> from las.client import Client
>>> client = Client()
>>> client.list_app_clients()
```


* **Parameters**

    
    * **max_results** (*Optional**[**int**]*) – Maximum number of results to be returned


    * **next_token** (*Optional**[**str**]*) – A unique token for each page, use the returned token to retrieve the next page.



* **Returns**

    AppClients response from REST API without the content of each appClient



* **Return type**

    dict



* **Raises**

    `InvalidCredentialsException`, `TooManyRequestsException`, `LimitExceededException`, `requests.exception.RequestException`



#### list_assets(\*, max_results: Optional[int] = None, next_token: Optional[str] = None)
List assets available, calls the GET /assets endpoint.

```python
>>> from las.client import Client
>>> client = Client()
>>> client.list_assets()
```


* **Parameters**

    
    * **max_results** (*Optional**[**int**]*) – Maximum number of results to be returned


    * **next_token** (*Optional**[**str**]*) – A unique token for each page, use the returned token to retrieve the next page.



* **Returns**

    Assets response from REST API without the content of each asset



* **Return type**

    dict



* **Raises**

    `InvalidCredentialsException`, `TooManyRequestsException`, `LimitExceededException`, `requests.exception.RequestException`



#### list_batches(\*, max_results: Optional[int] = None, next_token: Optional[str] = None)
List batches available, calls the GET /batches endpoint.

```python
>>> from las.client import Client
>>> client = Client()
>>> client.list_batches()
```


* **Parameters**

    
    * **max_results** (*Optional**[**int**]*) – Maximum number of results to be returned


    * **next_token** (*Optional**[**str**]*) – A unique token for each page, use the returned token to retrieve the next page.



* **Returns**

    Batches response from REST API without the content of each batch



* **Return type**

    dict



* **Raises**

    `InvalidCredentialsException`, `TooManyRequestsException`, `LimitExceededException`, `requests.exception.RequestException`



#### list_data_bundles(model_id, \*, max_results: Optional[int] = None, next_token: Optional[str] = None)
List data bundles available, calls the GET /models/{modelId}/dataBundles endpoint.


* **Parameters**

    
    * **model_id** (*str*) – Id of the model


    * **max_results** (*Optional**[**int**]*) – Maximum number of results to be returned


    * **next_token** (*Optional**[**str**]*) – A unique token for each page, use the returned token to retrieve the next page.



* **Returns**

    Data Bundles response from REST API



* **Return type**

    dict



* **Raises**

    `InvalidCredentialsException`, `TooManyRequestsException`, `LimitExceededException`, `requests.exception.RequestException`



#### list_datasets(\*, max_results: Optional[int] = None, next_token: Optional[str] = None)
List datasets available, calls the GET /datasets endpoint.


* **Parameters**

    
    * **max_results** (*Optional**[**int**]*) – Maximum number of results to be returned


    * **next_token** (*Optional**[**str**]*) – A unique token for each page, use the returned token to retrieve the next page.



* **Returns**

    Datasets response from REST API without the content of each dataset



* **Return type**

    dict



* **Raises**

    `InvalidCredentialsException`, `TooManyRequestsException`, `LimitExceededException`, `requests.exception.RequestException`



#### list_documents(\*, batch_id: Optional[Union[str, List[str]]] = None, consent_id: Optional[Union[str, List[str]]] = None, dataset_id: Optional[Union[str, List[str]]] = None, max_results: Optional[int] = None, next_token: Optional[str] = None)
List documents available for inference, calls the GET /documents endpoint.

```python
>>> from las.client import Client
>>> client = Client()
>>> client.list_documents(batch_id='<batch_id>', consent_id='<consent_id>')
```


* **Parameters**

    
    * **batch_id** (*Optional**[**Queryparam**]*) – Ids of batches that contains the documents of interest


    * **consent_id** (*Optional**[**Queryparam**]*) – Ids of the consents that marks the owner of the document


    * **dataset_id** (*Optional**[**Queryparam**]*) – Ids of datasets that contains the documents of interest


    * **max_results** (*Optional**[**int**]*) – Maximum number of results to be returned


    * **next_token** (*Optional**[**str**]*) – A unique token for each page, use the returned token to retrieve the next page.



* **Returns**

    Documents response from REST API



* **Return type**

    dict



* **Raises**

    `InvalidCredentialsException`, `TooManyRequestsException`, `LimitExceededException`, `requests.exception.RequestException`



#### list_logs(\*, workflow_id: Optional[str] = None, workflow_execution_id: Optional[str] = None, transition_id: Optional[str] = None, transition_execution_id: Optional[str] = None, max_results: Optional[int] = None, next_token: Optional[str] = None)
List logs, calls the GET /logs endpoint.

```python
>>> from las.client import Client
>>> client = Client()
>>> client.list_logs()
```


* **Parameters**

    
    * **workflow_id** (*Optional**[**str**]*) – Only show logs from this workflow


    * **workflow_execution_id** (*Optional**[**str**]*) – Only show logs from this workflow execution


    * **transition_id** (*Optional**[**str**]*) – Only show logs from this transition


    * **transition_execution_id** (*Optional**[**str**]*) – Only show logs from this transition execution


    * **max_results** (*Optional**[**int**]*) – Maximum number of results to be returned


    * **next_token** (*Optional**[**str**]*) – A unique token for each page, use the returned token to retrieve the next page.



* **Returns**

    Logs response from REST API



* **Return type**

    dict



* **Raises**

    `InvalidCredentialsException`, `TooManyRequestsException`, `LimitExceededException`, `requests.exception.RequestException`



#### list_models(\*, max_results: Optional[int] = None, next_token: Optional[str] = None)
List models available, calls the GET /models endpoint.

```python
>>> from las.client import Client
>>> client = Client()
>>> client.list_models()
```


* **Parameters**

    
    * **max_results** (*Optional**[**int**]*) – Maximum number of results to be returned


    * **next_token** (*Optional**[**str**]*) – A unique token for each page, use the returned token to retrieve the next page.



* **Returns**

    Models response from REST API without the content of each model



* **Return type**

    dict



* **Raises**

    `InvalidCredentialsException`, `TooManyRequestsException`, `LimitExceededException`, `requests.exception.RequestException`



#### list_predictions(\*, max_results: Optional[int] = None, next_token: Optional[str] = None)
List predictions available, calls the GET /predictions endpoint.

```python
>>> from las.client import Client
>>> client = Client()
>>> client.list_predictions()
```


* **Parameters**

    
    * **max_results** (*Optional**[**int**]*) – Maximum number of results to be returned


    * **next_token** (*Optional**[**str**]*) – A unique token for each page, use the returned token to retrieve the next page.



* **Returns**

    Predictions response from REST API without the content of each prediction



* **Return type**

    dict



* **Raises**

    `InvalidCredentialsException`, `TooManyRequestsException`, `LimitExceededException`, `requests.exception.RequestException`



#### list_secrets(\*, max_results: Optional[int] = None, next_token: Optional[str] = None)
List secrets available, calls the GET /secrets endpoint.

```python
>>> from las.client import Client
>>> client = Client()
>>> client.list_secrets()
```


* **Parameters**

    
    * **max_results** (*Optional**[**int**]*) – Maximum number of results to be returned


    * **next_token** (*Optional**[**str**]*) – A unique token for each page, use the returned token to retrieve the next page.



* **Returns**

    Secrets response from REST API without the username of each secret



* **Return type**

    dict



* **Raises**

    `InvalidCredentialsException`, `TooManyRequestsException`, `LimitExceededException`, `requests.exception.RequestException`



#### list_transition_executions(transition_id: str, \*, status: Optional[Union[str, List[str]]] = None, execution_id: Optional[Union[str, List[str]]] = None, max_results: Optional[int] = None, next_token: Optional[str] = None, sort_by: Optional[str] = None, order: Optional[str] = None)
List executions in a transition, calls the GET /transitions/{transitionId}/executions endpoint.

```python
>>> from las.client import Client
>>> client = Client()
>>> client.list_transition_executions('<transition_id>', '<status>')
```


* **Parameters**

    
    * **transition_id** (*str*) – Id of the transition


    * **status** (*Optional**[**Queryparam**]*) – Statuses of the executions


    * **order** (*Optional**[**str**]*) – Order of the executions, either ‘ascending’ or ‘descending’


    * **sort_by** (*Optional**[**str**]*) – the sorting variable of the executions, either ‘endTime’, or ‘startTime’


    * **execution_id** (*Optional**[**Queryparam**]*) – Ids of the executions


    * **max_results** (*Optional**[**int**]*) – Maximum number of results to be returned


    * **next_token** (*Optional**[**str**]*) – A unique token for each page, use the returned token to retrieve the next page.



* **Returns**

    Transition executions responses from REST API



* **Return type**

    dict



* **Raises**

    `InvalidCredentialsException`, `TooManyRequestsException`, `LimitExceededException`, `requests.exception.RequestException`



#### list_transitions(\*, transition_type: Optional[Union[str, List[str]]] = None, max_results: Optional[int] = None, next_token: Optional[str] = None)
List transitions, calls the GET /transitions endpoint.

```python
>>> from las.client import Client
>>> client = Client()
>>> client.list_transitions('<transition_type>')
```


* **Parameters**

    
    * **transition_type** (*Optional**[**Queryparam**]*) – Types of transitions


    * **max_results** (*Optional**[**int**]*) – Maximum number of results to be returned


    * **next_token** (*Optional**[**str**]*) – A unique token for each page, use the returned token to retrieve the next page.



* **Returns**

    Transitions response from REST API



* **Return type**

    dict



* **Raises**

    `InvalidCredentialsException`, `TooManyRequestsException`, `LimitExceededException`, `requests.exception.RequestException`



#### list_users(\*, max_results: Optional[int] = None, next_token: Optional[str] = None)
List users, calls the GET /users endpoint.

```python
>>> from las.client import Client
>>> client = Client()
>>> client.list_users()
```


* **Parameters**

    
    * **max_results** (*Optional**[**int**]*) – Maximum number of results to be returned


    * **next_token** (*Optional**[**str**]*) – A unique token for each page, use the returned token to retrieve the next page.



* **Returns**

    Users response from REST API



* **Return type**

    dict



* **Raises**

    `InvalidCredentialsException`, `TooManyRequestsException`, `LimitExceededException`, `requests.exception.RequestException`



#### list_workflow_executions(workflow_id: str, \*, status: Optional[Union[str, List[str]]] = None, sort_by: Optional[str] = None, order: Optional[str] = None, max_results: Optional[int] = None, next_token: Optional[str] = None)
List executions in a workflow, calls the GET /workflows/{workflowId}/executions endpoint.

```python
>>> from las.client import Client
>>> client = Client()
>>> client.list_workflow_executions('<workflow_id>', '<status>')
```


* **Parameters**

    
    * **workflow_id** (*str*) – Id of the workflow


    * **order** (*Optional**[**str**]*) – Order of the executions, either ‘ascending’ or ‘descending’


    * **sort_by** (*Optional**[**str**]*) – the sorting variable of the executions, either ‘endTime’, or ‘startTime’


    * **status** (*Optional**[**Queryparam**]*) – Statuses of the executions


    * **max_results** (*Optional**[**int**]*) – Maximum number of results to be returned


    * **next_token** (*Optional**[**str**]*) – A unique token for each page, use the returned token to retrieve the next page.



* **Returns**

    Workflow executions responses from REST API



* **Return type**

    dict



* **Raises**

    `InvalidCredentialsException`, `TooManyRequestsException`, `LimitExceededException`, `requests.exception.RequestException`



#### list_workflows(\*, max_results: Optional[int] = None, next_token: Optional[str] = None)
List workflows, calls the GET /workflows endpoint.

```python
>>> from las.client import Client
>>> client = Client()
>>> client.list_workflows()
```


* **Parameters**

    
    * **max_results** (*Optional**[**int**]*) – Maximum number of results to be returned


    * **next_token** (*Optional**[**str**]*) – A unique token for each page, use the returned token to retrieve the next page.



* **Returns**

    Workflows response from REST API



* **Return type**

    dict



* **Raises**

    `InvalidCredentialsException`, `TooManyRequestsException`, `LimitExceededException`, `requests.exception.RequestException`



#### send_heartbeat(transition_id: str, execution_id: str)
Send heartbeat for a manual execution to signal that we are still working on it.
Must be done at minimum once every 60 seconds or the transition execution will time out,
calls the POST /transitions/{transitionId}/executions/{executionId}/heartbeats endpoint.

```python
>>> from las.client import Client
>>> client = Client()
>>> client.send_heartbeat('<transition_id>', '<execution_id>')
```


* **Parameters**

    
    * **transition_id** (*str*) – Id of the transition


    * **execution_id** (*str*) – Id of the transition execution



* **Returns**

    Empty response



* **Return type**

    None



* **Raises**

    `InvalidCredentialsException`, `TooManyRequestsException`, `LimitExceededException`, `requests.exception.RequestException`



#### update_app_client(app_client_id, \*\*optional_args)
Updates an appClient, calls the PATCH /appClients/{appClientId} endpoint.


* **Parameters**

    
    * **app_client_id** (*str*) – Id of the appClient


    * **name** (*Optional**[**str**]*) – Name of the appClient


    * **description** (*Optional**[**str**]*) – Description of the appClient



* **Returns**

    AppClient response from REST API



* **Return type**

    dict



* **Raises**

    `InvalidCredentialsException`, `TooManyRequestsException`, `LimitExceededException`, `requests.exception.RequestException`



#### update_asset(asset_id: str, \*\*optional_args)
Updates an asset, calls the PATCH /assets/{assetId} endpoint.

```python
>>> from las.client import Client
>>> client = Client()
>>> client.update_asset('<asset id>', content=b'<bytes data>')
```


* **Parameters**

    
    * **asset_id** (*str*) – Id of the asset


    * **content** (*Optional**[**Content**]*) – Content to PATCH


    * **name** (*Optional**[**str**]*) – Name of the asset


    * **description** (*Optional**[**str**]*) – Description of the asset



* **Returns**

    Asset response from REST API



* **Return type**

    dict



* **Raises**

    `InvalidCredentialsException`, `TooManyRequestsException`, `LimitExceededException`, `requests.exception.RequestException`



#### update_batch(batch_id, \*\*optional_args)
Updates a batch, calls the PATCH /batches/{batchId} endpoint.


* **Parameters**

    
    * **batch_id** (*str*) – Id of the batch


    * **name** (*Optional**[**str**]*) – Name of the batch


    * **description** (*Optional**[**str**]*) – Description of the batch



* **Returns**

    Batch response from REST API



* **Return type**

    dict



* **Raises**

    `InvalidCredentialsException`, `TooManyRequestsException`, `LimitExceededException`, `requests.exception.RequestException`



#### update_data_bundle(model_id: str, data_bundle_id: str, \*\*optional_args)
Updates a data bundle, calls the PATCH /models/{modelId}/dataBundles/{dataBundleId} endpoint.


* **Parameters**

    
    * **model_id** (*str*) – Id of the model


    * **data_bundle_id** (*str*) – Id of the data bundle


    * **name** (*Optional**[**str**]*) – Name of the data bundle


    * **description** (*Optional**[**str**]*) – Description of the data bundle



* **Returns**

    Data Bundle response from REST API



* **Return type**

    dict



* **Raises**

    `InvalidCredentialsException`, `TooManyRequestsException`, `LimitExceededException`, `requests.exception.RequestException`



#### update_dataset(dataset_id, \*\*optional_args)
Updates a dataset, calls the PATCH /datasets/{datasetId} endpoint.


* **Parameters**

    
    * **dataset_id** (*str*) – Id of the dataset


    * **name** (*Optional**[**str**]*) – Name of the dataset


    * **description** (*Optional**[**str**]*) – Description of the dataset



* **Returns**

    Dataset response from REST API



* **Return type**

    dict



* **Raises**

    `InvalidCredentialsException`, `TooManyRequestsException`, `LimitExceededException`, `requests.exception.RequestException`



#### update_document(document_id: str, ground_truth: Optional[Sequence[Dict[str, Union[str, None, bool]]]] = None, \*, dataset_id: Optional[str] = None)
Update ground truth for a document, calls the PATCH /documents/{documentId} endpoint.
Updating ground truth means adding the ground truth data for the particular document.
This enables the API to learn from past mistakes.


* **Parameters**

    
    * **document_id** (*str*) – Id of the document


    * **dataset_id** (*Optional**[**str**]*) – Id of the dataset you want to associate your document with


    * **ground_truth** (*Optional**[**Sequence**[**Dict**[**str**, **Union**[**Optional**[**str**]**, **bool**]**]**]**]*) – List of items {label: value} representing the ground truth values for the document



* **Returns**

    Document response from REST API



* **Return type**

    dict



* **Raises**

    `InvalidCredentialsException`, `TooManyRequestsException`, `LimitExceededException`, `requests.exception.RequestException`



#### update_model(model_id: str, \*, width: Optional[int] = None, height: Optional[int] = None, field_config: Optional[dict] = None, preprocess_config: Optional[dict] = None, status: Optional[str] = None, \*\*optional_args)
Updates a model, calls the PATCH /models/{modelId} endpoint.


* **Parameters**

    
    * **model_id** (*Optional**[**str**]*) – The Id of the model


    * **width** (*Optional**[**int**]*) – The number of pixels to be used for the input image width of your model


    * **height** (*Optional**[**int**]*) – The number of pixels to be used for the input image height of your model


    * **field_config** (*dict*) – Specification of the fields that the model is going to predict


    * **preprocess_config** (*dict*) – Specification of the processing steps prior to the prediction of an image


    * **status** (*Optional**[**str**]*) – New status for the model


    * **name** (*Optional**[**str**]*) – Name of the model


    * **description** (*Optional**[**str**]*) – Description of the model



* **Returns**

    Model response from REST API



* **Return type**

    dict



* **Raises**

    `InvalidCredentialsException`, `TooManyRequestsException`, `LimitExceededException`, `requests.exception.RequestException`



#### update_organization(organization_id: str, \*\*optional_args)
Updates an organization, calls the PATCH /organizations/{organizationId} endpoint.


* **Parameters**

    
    * **organization_id** (*Optional**[**str**]*) – The Id of the organization


    * **name** (*Optional**[**str**]*) – Name of the organization


    * **description** (*Optional**[**str**]*) – Description of the organization



* **Returns**

    Organization response from REST API



* **Return type**

    dict



* **Raises**

    `InvalidCredentialsException`, `TooManyRequestsException`, `LimitExceededException`, `requests.exception.RequestException`



#### update_secret(secret_id: str, \*, data: Optional[dict] = None, \*\*optional_args)
Updates an secret, calls the PATCH /secrets/secretId endpoint.

```python
>>> from las.client import Client
>>> client = Client()
>>> data = {'username': '<username>', 'password': '<password>'}
>>> client.update_secret('<secret id>', data, description='<description>')
```


* **Parameters**

    
    * **secret_id** (*str*) – Id of the secret


    * **data** (*Optional**[**dict**]*) – Dict containing the data you want to keep secret


    * **name** (*Optional**[**str**]*) – Name of the secret


    * **description** (*Optional**[**str**]*) – Description of the secret



* **Returns**

    Secret response from REST API



* **Return type**

    dict



* **Raises**

    `InvalidCredentialsException`, `TooManyRequestsException`, `LimitExceededException`, `requests.exception.RequestException`



#### update_transition(transition_id: str, \*, in_schema: Optional[dict] = None, out_schema: Optional[dict] = None, assets: Optional[dict] = None, environment: Optional[dict] = None, environment_secrets: Optional[list] = None, \*\*optional_args)
Updates a transition, calls the PATCH /transitions/{transitionId} endpoint.

```python
>>> import json
>>> from pathlib import Path
>>> from las.client import Client
>>> client = Client()
>>> client.update_transition('<transition-id>', name='<name>', description='<description>')
```


* **Parameters**

    
    * **transition_id** (*str*) – Id of the transition


    * **name** (*Optional**[**str**]*) – Name of the transition


    * **description** (*Optional**[**str**]*) – Description of the transition


    * **in_schema** (*Optional**[**dict**]*) – Json-schema that defines the input to the transition


    * **out_schema** (*Optional**[**dict**]*) – Json-schema that defines the output of the transition


    * **assets** (*Optional**[**dict**]*) – A dictionary where the values are assetIds that can be used in a manual transition


    * **environment** (*Optional**[**dict**]*) – Environment variables to use for a docker transition


    * **environment_secrets** – 


A list of secretIds that contains environment variables to use for a docker transition
:type environment_secrets: Optional[list]
:return: Transition response from REST API
:rtype: dict


* **Raises**

    `InvalidCredentialsException`, `TooManyRequestsException`, `LimitExceededException`, `requests.exception.RequestException`



#### update_transition_execution(transition_id: str, execution_id: str, status: str, \*, output: Optional[dict] = None, error: Optional[dict] = None, start_time: Optional[Union[str, datetime.datetime]] = None)
Ends the processing of the transition execution,
calls the PATCH /transitions/{transition_id}/executions/{execution_id} endpoint.

```python
>>> from las.client import Client
>>> client = Client()
>>> output = {...}
>>> client.update_transition_execution('<transition_id>', '<execution_id>', 'succeeded', output)
>>> error = {"message": 'The execution could not be processed due to ...'}
>>> client.update_transition_execution('<transition_id>', '<execution_id>', 'failed', error)
```


* **Parameters**

    
    * **transition_id** (*str*) – Id of the transition that performs the execution


    * **execution_id** (*str*) – Id of the execution to update


    * **status** (*str*) – Status of the execution ‘succeeded|failed’


    * **output** (*Optional**[**dict**]*) – Output from the execution, required when status is ‘succeded’


    * **error** (*Optional**[**dict**]*) – Error from the execution, required when status is ‘failed’, needs to contain ‘message’


    * **start_time** (*Optional**[**str**]*) – start time that will replace the original start time of the execution



* **Returns**

    Transition execution response from REST API



* **Return type**

    dict



* **Raises**

    `InvalidCredentialsException`, `TooManyRequestsException`, `LimitExceededException`, `requests.exception.RequestException`



#### update_user(user_id: str, \*\*optional_args)
Updates a user, calls the PATCH /users/{userId} endpoint.

```python
>>> from las.client import Client
>>> client = Client()
>>> client.update_user('<user id>', name='John Doe')
```


* **Parameters**

    
    * **user_id** (*str*) – Id of the user


    * **name** (*Optional**[**str**]*) – Name of the user


    * **avatar** (*Optional**[**str**]*) – base64 encoded JPEG avatar of the user



* **Returns**

    User response from REST API



* **Return type**

    dict



* **Raises**

    `InvalidCredentialsException`, `TooManyRequestsException`, `LimitExceededException`, `requests.exception.RequestException`



#### update_workflow(workflow_id: str, \*, error_config: Optional[dict] = None, completed_config: Optional[dict] = None, \*\*optional_args)
Updates a workflow, calls the PATCH /workflows/{workflowId} endpoint.

```python
>>> import json
>>> from pathlib import Path
>>> from las.client import Client
>>> client = Client()
>>> client.update_workflow('<workflow-id>', name='<name>', description='<description>')
```


* **Parameters**

    
    * **workflow_id** – Id of the workflow


    * **name** (*Optional**[**str**]*) – Name of the workflow


    * **description** (*Optional**[**str**]*) – Description of the workflow


    * **error_config** (*Optional**[**dict**]*) – Configuration of error handler


    * **completed_config** (*Optional**[**dict**]*) – Configuration of a job to run whenever a workflow execution ends



* **Returns**

    Workflow response from REST API



* **Return type**

    dict



* **Raises**

    `InvalidCredentialsException`, `TooManyRequestsException`, `LimitExceededException`, `requests.exception.RequestException`



#### update_workflow_execution(workflow_id: str, execution_id: str, next_transition_id: str)
Retry or end the processing of a workflow execution,
calls the PATCH /workflows/{workflow_id}/executions/{execution_id} endpoint.

```python
>>> from las.client import Client
>>> client = Client()
>>> client.update_workflow_execution('<workflow_id>', '<execution_id>', '<next_transition_id>')
```


* **Parameters**

    
    * **workflow_id** (*str*) – Id of the workflow that performs the execution


    * **execution_id** (*str*) – Id of the execution to update


    * **next_transition_id** – the next transition to transition into, to end the workflow-execution,


use: las:transition:commons-failed
:type next_transition_id: str
:return: Workflow execution response from REST API
:rtype: dict


* **Raises**

    `InvalidCredentialsException`, `TooManyRequestsException`, `LimitExceededException`, `requests.exception.RequestException`



### class las.Credentials(client_id: str, client_secret: str, auth_endpoint: str, api_endpoint: str, cached_profile: Optional[str] = None, cache_path: pathlib.Path = PosixPath('/home/runner/.lucidtech/token-cache.json'))
Bases: `object`

Used to fetch and store credentials and to generate/cache an access token.


* **Parameters**

    
    * **client_id** – The client id


    * **client_secret** – The client secret


    * **auth_endpoint** – The auth endpoint


    * **api_endpoint** – The api endpoint



#### property access_token(: str)
