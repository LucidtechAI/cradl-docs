# Create dataset

#### **Create dataset**

After defining our model, we'd like to get it trained and ready for work. To train a model, we need to provide it with a sufficiently many example [documents](../concepts/documents.md). The documents are bundled together in the form of [datasets](../concepts/datasets.md), so before we start uploading documents, let's create a dataset to hold all of them together.

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

### Upload documents to a dataset

After creating a dataset, we can start uploading [documents](../concepts/documents.md) and assign them to it. Since we want to use these documents for training, we'll also assign [ground truth values](../concepts/documents.md#setting-ground-truths) to them. That way, the model will know what the desired output looks like while it's training. The ground truth field names must match those in the field config defined for your model.

{% hint style="warning" %}
It is important to have **correct** ground truths for each document you want to use for training. They are what will guide your model to making correct predictions. If the ground truths contain mistakes, the model will learn to make those mistakes.
{% endhint %}

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
If you upload documents without assigning them to a dataset, or if you want to assign them to a different dataset in the future, you can do so easily using the API. However, it is even easier to assign them directly to a dataset right away!
{% endhint %}

