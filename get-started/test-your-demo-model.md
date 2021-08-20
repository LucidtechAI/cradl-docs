# Test your demo model

After getting access to Cradl, you should have a pre-trained demo model available, that we can use for testing purposes.

{% hint style="warning" %}
Note that the demo model has been pre-trained for a specific use-case, using documents that are not necessarily representative of your own data. Hence we'll also use the provided datasets with relevant documents during testing.
{% endhint %}

First let's list our available models to get a model id we can use:

{% tabs %}
{% tab title="CLI" %}
```bash
las models list
```
{% endtab %}

{% tab title="cURL" %}
```
curl https://api.cradl.ai/v1/models -H 'Authorization: Bearer eyJra...'
```
{% endtab %}

{% tab title="Python" %}
```python
from las import Client

client = Client()
models = client.list_models()
```
{% endtab %}
{% endtabs %}

```javascript
{
  "models": [
    {
      "modelId": "las:model:<model id>",
      "name": "Demo model",
      "description": null,
      "height": 1281,
      "width": 801,
      "preprocessConfig": {
        "imageQuality": "LOW",
        "autoRotate": false,
        "maxPages": 1
      },
      "fieldConfig": {
        "total_amount": {
          "maxLength": 30,
          "type": "amount",
          "description": "Total amount"
        }
      },
      "status": "active",
      "createdTime": "2021-06-29T14:28:15.736079+0000",
      "updatedTime": null,
      "createdBy": null,
      "updatedBy": null
    }
  ]
}
```

List the available datasets:

{% tabs %}
{% tab title="CLI" %}
```bash
las datasets list
```
{% endtab %}

{% tab title="cURL" %}
```bash
curl 'https://api.cradl.ai/v1/datasets' --header 'Authorization: Bearer eyJra...'
```
{% endtab %}

{% tab title="Python" %}
```python
datasets = client.list_datasets()
```
{% endtab %}
{% endtabs %}

```javascript
{
  "datasets": [
    {
      "datasetId": "las:dataset:<dataset id>",
      "description": null,
      "name": "Dataset generated: 2021-08-12T09:18:36.474767",
      "numberOfDocuments": 3354,
      "createdTime": "2021-08-12T07:18:40.533029+0000",
      "updatedTime": "2021-08-12T07:26:04.964639+0000",
      "createdBy": "las:app-client:<app-client id>",
      "updatedBy": null,
      "retentionInDays": 1825,
      "storageLocation": "EU",
      "containsPersonallyIdentifiableInformation": true,
      "version": 3354
    }
  ]
}
```

List the first page of documents from the dataset so that we can pick a document to use:

{% tabs %}
{% tab title="CLI" %}
```bash
las documents list --dataset-id las:dataset:<dataset id>
```
{% endtab %}

{% tab title="cURL" %}
```bash
curl 'https://api.cradl.ai/v1/documents?datasetId=las:dataset:<dataset id>'
```
{% endtab %}

{% tab title="Python" %}
```python
documents = client.list_documents(dataset_id='las:dataset:<dataset id>')
```
{% endtab %}
{% endtabs %}

```javascript
{
  "documents": [
    {
      "documentId": "las:document:<document id>",
      ...
    },
    ...
  ]
}
```

Once we have a document selected, we can make a prediction using the model on it:

{% tabs %}
{% tab title="CLI" %}
```bash
las predictions create las:document:<document id> las:model:<model id>
```
{% endtab %}

{% tab title="cURL" %}
```bash
curl -X POST 'https://api.cradl.ai/v1/predictions' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer eyJra...' \
--data-raw '{
    "documentId": "las:document:<document id>",
    "modelId": "las:model:<model id>"
}'
```
{% endtab %}

{% tab title="Python" %}
```python
prediction = client.create_prediction(document_id='<document id>', model_id='<model id>')
```
{% endtab %}
{% endtabs %}

```javascript
{
  "predictionId": "las:prediction:<prediction id>",
  "modelId": "las:model:<model id>",
  "documentId": "las:document:<document id>",
  "predictions": [
    {
      "label": "total_amount",
      "value": "5154.06",
      "confidence": 0.9758162361908527
    },
    {
      "label": "purchase_date",
      "value": "2019-12-23",
      "confidence": 0.96797316745869735
    },
  ],
  "timestamp": 1629188787,
  "inferenceTime": 2.7935566902160645
}
```

