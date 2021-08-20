# Choose training data

Before we go to the next step of training our newly created model, it is wise to make sure that our training data is varied and has good coverage of all the various fields we want to train our model for. We can do this by selecting datasets with our training data, and create a data quality report on them.

{% tabs %}
{% tab title="CLI" %}
```bash
las models create-data-bundle --name "Initial data report" las:model:<model id> las:dataset:<dataset id>
```
{% endtab %}

{% tab title="cURL" %}
```bash
curl -X POST 'https://api.cradl.ai/v1/models/<model id>/dataBundles' \
--header 'Content-Type: application/json' \
--data-raw '{
    "datasetIds": [
        "las:dataset:<dataset id>"
    ],
    "name": "Initial data report"
}'
```
{% endtab %}

{% tab title="Python" %}
```python
data_bundle = client.create_data_bundle(model_id='las:model:<model id>', dataset_ids=['las:dataset:<dataset id>'], name='Initial data report')
```
{% endtab %}
{% endtabs %}

```javascript
{
  "dataBundleId": "las:model-data-bundle:<data bundle id>",
  "modelId": "las:model:<model id>",
  "name": "Initial data report",
  "datasets": [
    {
      "datasetId": "las:dataset:<dataset id>",
      "numberOfDocuments": 3354,
      "createdTime": "2021-08-12T07:18:40.533029+0000",
      "retentionInDays": 1825,
      "storageLocation": "EU",
      "containsPersonallyIdentifiableInformation": true,
      "version": 3354,
      ...
    }
  ],
  "summary": null,
  "status": "processing",
  "createdTime": "2021-08-17T07:11:30.430841+0000",
  ...
}
```

A data report takes a few minutes to process. After it has been processed \(its status has changed from `processing` to `ready`\) we can look at the summary to get an idea of how good our data is.

{% tabs %}
{% tab title="CLI" %}
```bash
las models list-data-bundles las:model:<model id> 
```
{% endtab %}

{% tab title="cURL" %}
```bash
curl 'https://api.cradl.ai/v1/models/<model id>/dataBundles'
```
{% endtab %}

{% tab title="Python" %}
```python
data_bundle = client.list_data_bundles(model_id='las:model:<model id>')
```
{% endtab %}
{% endtabs %}

```javascript
{
  "dataBundles": [
    {
      "dataBundleId": "las:model-data-bundle:<data bundle id>",
      "datasets": [...],
      "status": "ready",
      ...,
      "summary": {
        "aggregate": {
          "numberOfDocuments": 3043,
          "completeness": 1.0,
          "validity": 1.0,
          "coverage": 1.0,
          "uniqueness": 0.9395333552415379,
          "uniformity": 0.9739045113959695,
          "variation": 0.9567189333187538,
          "overallScore": 0.9783594666593769
        },
        "labels": {
          "total_amount": {
            "numberOfValids": 3043,
            "numberOfDistinctValids": 3039,
            "numberOfErrors": 0,
            "errorPercent": 0.0,
            "completeness": 1.0,
            "validity": 1.0,
            "coverage": 1.0,
            "uniqueness": 0.9953992770292475,
            "uniformity": 0.9997728008596639,
            "variation": 0.9975860389444557
          },
          "purchase_date": {
            "numberOfValids": 3043,
            "numberOfDistinctValids": 2110,
            "numberOfErrors": 0,
            "errorPercent": 0.0,
            "completeness": 1.0,
            "validity": 1.0,
            "coverage": 1.0,
            "uniqueness": 0.8836674334538285,
            "uniformity": 0.9480362219322751,
            "variation": 0.9158518276930518
          }
        }
      }
    }
  ]
}
```

{% hint style="success" %}
See [data quality section](../concepts/training-data.md#data-quality) for detailed information about data quality and how to improve it
{% endhint %}

