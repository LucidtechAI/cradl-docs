# Datasets

A _dataset_ in Cradl is a collection of [Documents](documents.md), preferably from a single source. When you have uploaded a sufficient amount of documents in your datasets they can be bundled together in [Data bundles](training-data.md) for training a [Model](models.md).

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
  "datasetId": <datasetId>,
  "description": "From accounting system",
  "name": "Invoices 2020",
  "numberOfDocuments": 0,
  "storageLocation": "EU",
  "containsPersonallyIdentifiableInformation": true,
  "version": 0
}
```

The `datasetId` is used to include datasets in [Data bundles](training-data.md) and to [add documents to datasets](datasets.md#adding-documents-to-a-dataset). The `version` field is used to identify changes to a dataset, i.e. when adding/removing/updating contained documents.

{% hint style="warning" %}
Give your datasets clear names and descriptions. This will be helpful when keeping track of which data you train your model from.
{% endhint %}

## Adding documents to a dataset

Documents can be assigned to a dataset either at creation time or in an update.

{% tabs %}
{% tab title="CLI" %}
```bash
las documents create path/to/my/document.pdf --dataset-id <datasetId>
las documents update <documentId> --dataset-id <datasetId>
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
document = client.update_document(<documentId>, datasetId=<datasetId>)
```
{% endtab %}
{% endtabs %}

{% hint style="warning" %}
A document cannot be added to more than one dataset.
{% endhint %}


## Deleting a dataset

A dataset may not be deleted unless all documents contained in the dataset are deleted first. Our SDK's and CLI supports doing this in one single command, for instructions on how to delete all documents from a dataset see the [Documents](documents.md#deleting-documents) page.

{% tabs %}
{% tab title="CLI" %}
```bash
las datasets delete <datasetId> --delete-documents
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
client.delete_dataset(dataset_id=<datasetId>, delete_documents=True)
```
{% endtab %}
{% endtabs %}

