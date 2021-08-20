# Create dataset

#### **Create dataset**

After defining our model, we'd like to get it trained and ready for work. To train a model, we need to provide it with a sufficiently many example [documents](../concepts/documents.md). The documents are bundled together in the form of [datasets](../concepts/datasets.md), so before we start uploading documents, let's create a dataset to hold all of them together.

{% hint style="warning" %}
It is important to have correct ground truth values for each document, in order to train your model to give correct predictions for each field you want to extract! These ground truth fields should match the field config defined for your model.
{% endhint %}

{% tabs %}
{% tab title="CLI" %}
```bash
las datasets create --name "Receipts" --description "Initial training data"
```
{% endtab %}

{% tab title="cURL" %}
```bash
curl -X POST 'https://api.cradl.ai/v1/datasets' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer eyJra...' \
--data-raw '{
    "name": "Receipts",
    "description": "Initial training data"
}'
```
{% endtab %}

{% tab title="Python" %}
```python
dataset = client.create_dataset(name='Initial training data')
```
{% endtab %}
{% endtabs %}

```javascript
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

Insert direct link to Cradl that takes you to datasets

### Upload documents to a dataset

After we've created a dataset, we can start uploading [documents](../concepts/documents.md) and assign them to it directly.

{% tabs %}
{% tab title="CLI" %}
```bash
las documents create receipt.pdf --dataset-id las:dataset:<dataset id> --ground-truth-fields total_amount=300.00 date=2020-02-28
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
    "groundTruth: [
      {
      "label": "total_amount",
      "value": "300.00"
      },
      {
        "label": "date",
        "value": "2020-02-28"
      }
    ]
}'
```
{% endtab %}

{% tab title="Python" %}
```python
ground_truth = [
  { 'label': 'total_amount', 'value': '300.00' },
  { 'label': 'date', 'value': '2020-02-28' }
]
document = client.create_document(b'<bytes data>', 'application/pdf', ground_truth=ground_truth)
```
{% endtab %}
{% endtabs %}

```javascript
{
  "documentId": "las:document:<document id>",
  "contentType": "application/pdf",
  "retentionInDays": 1825,
  "createdTime": "2021-08-16T13:34:13.724393+0000",
  "updatedTime": null,
  "createdBy": "las:app-client:<appClient id>",
  "updatedBy": null,
  "datasetId": "las:dataset:<dataset id>",
  "groundTruth": [
    {
      "label": "total_amount",
      "value": "300.00"
    },
    {
      "label": "date",
      "value": "2020-02-28"
    }
  ]
}
```

{% hint style="success" %}
If you upload documents without assigning them to a dataset, or if you want to change the dataset in the future, this is possible to do easily using the API. However, it is a lot easier to upload them directly to a dataset right away!
{% endhint %}

