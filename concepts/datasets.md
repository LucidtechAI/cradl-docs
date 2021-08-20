# Datasets

A _dataset_ in Cradl is a collection of [Documents](documents.md), preferably from a single source, to be used for training. Datasets are collected in [Data bundles](training-data.md) that can be used to train [Models](models.md).

## Creating a dataset

Datasets are created independently of the documents they contain. You can create a dataset directly in the Cradl datasets UI, or programmatically.

{% tabs %}
{% tab title="CLI" %}
```bash
las datasets create --name "Invoices 2020" --description "From accounting system"
```
{% endtab %}

{% tab title="cURL" %}
```bash
curl -X POST 'https://api.cradl.ai/v1/datasets' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer eyJra...' \
--data-raw '{
    "name": "Invoices 2020",
    "description": "From accounting system"
}'
```
{% endtab %}

{% tab title="Python" %}
```python
dataset = client.create_dataset(name='Invoices 2020', description='From accounting system')
```
{% endtab %}
{% endtabs %}

```javascript
{
  "datasetId": "las:dataset:05ebcb0c1a8c458ebb47725a0e21d59b",
  "description": "From accounting system",
  "name": "Invoices 2020",
  "numberOfDocuments": 0,
  "storageLocation": "EU",
  "containsPersonallyIdentifiableInformation": true,
  "version": 0
}
```

The `datasetId` is used to include datasets in [Data bundles](training-data.md) and to [add documents to datasets](datasets.md#adding-documents-to-a-dataset). The `version` field is used to identify changes to a dataset, i.e. when adding/removing/updating contained documents.

{% hint style="info" %}
Give your datasets clear names and descriptions. This will be helpful when keeping track of which data you  your model from.
{% endhint %}

## Adding documents to a dataset

Documents can be assigned to a dataset either at creation time or in an update. It is not possible to assign a document to multiple datasets.

{% tabs %}
{% tab title="CLI" %}
```bash
las documents create path/to/my/document.pdf --dataset-id <dataset-id>
las documents update <document-id> --dataset-id <dataset-id>
```
{% endtab %}

{% tab title="cURL" %}
```bash
curl -X POST 'https://api.cradl.ai/v1/documents' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer eyJra...' \
--data-raw '{
    "content": "JVBERi0xLjQ...",
    "contentType": "application/pdf",
    "datasetId": <datasetId>
}'

curl -X PATCH 'https://api.cradl.ai/v1/documents/<documentId>' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer eyJra...' \
--data-raw '{
    "datasetId": <datasetId>
  }'
```
{% endtab %}

{% tab title="Python" %}
```python
document = client.create_document(b'<bytes data>', 'application/pdf', datasetId=<datasetId>)
# or
document = client.update_document(<document_id>, datasetId=<datasetId>)
```
{% endtab %}
{% endtabs %}

## Deleting a dataset

A dataset may not be deleted unless all documents contained in the dataset are deleted first. Instructions on how to delete all documents from a dataset are found on the [Documents](documents.md#deleting-documents) page.

{% tabs %}
{% tab title="CLI" %}
```bash
las documents delete-all --dataset-id <dataset-id>
las datasets delete <dataset-id>
```
{% endtab %}

{% tab title="cURL" %}
```bash
curl -X DELETE 'https://api.cradl.ai/v1/documents' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer eyJra...' \
--data-raw '{
    "datasetId": <datasetId>
 }'
 
 curl -X DELETE 'https://api.cradl.ai/v1/datasets/<datasetId>' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer eyJra...' \
```
{% endtab %}

{% tab title="Python" %}
```python
client.delete_dataset(dataset_id=<dataset_id>, delete_documents=True)
```
{% endtab %}
{% endtabs %}

