# Create dataset

In order to train a model we need to provide it with a lot of documents. The easiest way to do this, is to bundle multiple documents together in the form of [_datasets_](../concepts/datasets.md). Before we start uploading documents, let's create a dataset to hold all of them together.

{% hint style="success" %}
If you upload documents without assigning them to a dataset, or you want to change the dataset in the future, this is possible to change easily using the API. However, it is a lot easier to upload them directly to a dataset right away!
{% endhint %}

{% tabs %}
{% tab title="CLI" %}
```bash
$ las datasets create --name "Receipts" --description "Initial training data"
{
  "datasetId": "las:dataset:<dataset id>",
  "description": "Initial training data",
  "name": "Receipts",
  "numberOfDocuments": 0,
  "createdTime": "2021-08-16T12:53:13.374930+0000",
  "updatedTime": null,
  "createdBy": "las:app-client:<appClient id>",
  "updatedBy": null,
  "retentionInDays": 1825,
  "storageLocation": "EU",
  "containsPersonallyIdentifiableInformation": true,
  "version": 0
}
```
{% endtab %}

{% tab title="cURL" %}
```

```
{% endtab %}

{% tab title="Python" %}
```

```
{% endtab %}
{% endtabs %}

Insert direct link to Cradl that takes you to datasets

### Upload documents to dataset



