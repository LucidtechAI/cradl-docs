---
sidebar_position: 6
---

# Select and inspect training data

We have now defined a model and created a dataset. The next step is to train the model, but first we need to tell it what data to use when training. At this point, it would also be wise to take a step back and make sure that our training data is of good quality, so that the outcome of the training will be satisfactory. Good quality training data is varied and has lots of examples for all the fields we want the model to extract.

To tell the model which data to use, we select datasets containing our training data and attach them to the model in the form of a [data bundle](../concepts/training-data.md). Doing so will automatically create a [data quality report](../concepts/training-data.md#data-report) on the training data.

{% tabs %}
{% tab title="CLI" %}
```bash
las models create-data-bundle --name "Initial data report" <modelId> <datasetId>
```
{% endtab %}

{% tab title="cURL" %}
```bash
curl -X POST 'https://api.cradl.ai/v1/models/<model id>/dataBundles' \
--header 'Content-Type: application/json' \
--data-raw '{
    "modelId": <modelId>,
    "datasetIds": [
        <datasetId>
    ],
    "name": "Initial data report"
}'
```
{% endtab %}

{% tab title="Python" %}
```python
data_bundle = client.create_data_bundle(model_id=<modelId>, dataset_ids=[<datasetId>], name='Initial data report')
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
      "datasetId": <datasetId>,
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

A data report may take a few minutes to process. After it has been processed \(its status has changed from `processing` to `ready`\) we can look at the summary to get an idea of how good our data is.

{% tabs %}
{% tab title="CLI" %}
```bash
las models list-data-bundles <modelId>
```
{% endtab %}

{% tab title="cURL" %}
```bash
curl 'https://api.cradl.ai/v1/models/<modelId>/dataBundles'
```
{% endtab %}

{% tab title="Python" %}
```python
data_bundle = client.list_data_bundles(model_id=<modelId>)
```
{% endtab %}
{% endtabs %}

```javascript
{
  "dataBundles": [
    {
      "dataBundleId": <dataBundleId>,
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
See [data quality section](../concepts/training-data.md#data-quality) for detailed information about data quality and how to improve it.
{% endhint %}
