## Upload documents one by one to a dataset

After the dataset is created we can start uploading [documents](../concepts/documents.md) and assign them to our dataset. Since we want to use the documents for training, we'll also provide [ground truth values](../concepts/documents.md#setting-ground-truths) that will define the correct output for the model on each document. We'll have to make sure that the field names in the ground truth match those in the field config we made for our model.

{% hint style="warning" %}
It is important to have **correct** ground truths for each document we want to use for training. They are what will guide our model to making correct predictions. If there are mistakes in the ground truths, our model will learn to make those mistakes.
{% endhint %}

{% tabs %}
{% tab title="CLI" %}
```bash
las documents create receipt.pdf --dataset-id <datasetId> --ground-truth-fields total_amount=300.00 date=2020-02-28
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
    "datasetId": <datasetId>,
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
document = client.create_document(b'<bytes data>', 'application/pdf', ground_truth=ground_truth, dataset_id=<datasetId>)
```
{% endtab %}
{% endtabs %}

```javascript
{
  "documentId": <documentId>,
  "contentType": "application/pdf",
  "retentionInDays": 1825,
  "createdTime": "2021-08-16T13:34:13.724393+0000",
  "updatedTime": null,
  "createdBy": <appClientId>,
  "updatedBy": null,
  "datasetId": <datasetId>,
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
If you upload documents without assigning them to a dataset, or if you want to assign them to a different dataset in the future, you can do so easily using the API.
{% endhint %}

