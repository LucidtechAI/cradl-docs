# Create dataset

## **Create dataset**

After defining our model, the next step is to train it. This requires that we provide the model with a sufficient number of example [documents](../concepts/documents.md). Documents can be grouped together in [datasets](../concepts/datasets.md), so before we start uploading documents, let's create a dataset.

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
  "datasetId": <datasetId>,
  "description": "Initial training data",
  "name": "Receipts",
  "numberOfDocuments": 0,
  "createdTime": "2021-08-16T12:53:13.374930+0000",
  "updatedTime": null,
  "createdBy": <appClientId>,
  "updatedBy": null,
  "retentionInDays": 1825,
  "storageLocation": "EU",
  "containsPersonallyIdentifiableInformation": true,
  "version": 0
}
```
