# Datasets

A _dataset_ in Cradl is a collection of [Documents](documents.md), preferably from a single source, to be used for training. One or more datasets are collected in a [Data bundle](training-data.md) when you specify which data to use when training a [Model](models.md).

## Creating a dataset

Datasets are created independently of the documents they contain. This can be done directly in the Cradl datasets UI or programmatically.

{% hint style="info" %}
Give your datasets clear names and descriptions. This will be helpful when specifying which data to train a model from.
{% endhint %}

{% tabs %}
{% tab title="CLI" %}
```text
>> las datasets create --name "Invoices 2020" --description "From accounting system"
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
{% endtab %}
{% endtabs %}

This creates an empty dataset for documents to be added to. The `datasetId` can be used to specify that this dataset is to be used when training a [Model](models.md). The `version` field is used to identify changes to a dataset, by adding/removing/updating contained documents.

## Adding documents to a dataset

Documents can be assigned to a dataset either at creation or from an update. It is not possible to assign a document to multiple datasets.

{% tabs %}
{% tab title="CLI" %}
```text
>> las documents create path/to/my/document.pdf --dataset-id <dataset-id>
>> las documents update <document-id> --dataset-id <dataset-id>
```
{% endtab %}
{% endtabs %}

## Deleting a dataset

A dataset may not be deleted unless all documents contained in the dataset are deleted first. Instructions on how to delete all documents from a dataset are found on the [Documents](documents.md#deleting-documents) page.

{% tabs %}
{% tab title="CLI" %}
```text
>> las documents delete-all --dataset-id <dataset-id>
>> las datasets delete <dataset-id>
```
{% endtab %}
{% endtabs %}

