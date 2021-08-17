# Define model

### Create model

Let's create a model we can start training using our datasets. A model requires some configuration in order to know what it should look for and train to predict values for. We can do this using a _field config_. Here we can define the name of our fields, and what type of values we expect them to return. These fields should match the ground truths given in the previous step while uploading documents.

Let's create a field config file that looks something like this:

{% code title="field\_config.json" %}
```javascript
{
  "total_amount": { "type": "amount", "maxLength": 20, "description": "" },
  "purchase_date": { "type": "date", "maxLength": 10, "description": "" }
}
```
{% endcode %}

{% tabs %}
{% tab title="CLI" %}
```bash
$ las models create --name "Receipt model" 1281 801 field_config.json
```
{% endtab %}
{% endtabs %}

{% hint style="info" %}
See [models concepts](../concepts/models.md) for detailed information about field config and other parameters used to define and create a model.
{% endhint %}

Link to create model in Cradl

### Create data bundle / data report

Before we go to the next step of training our newly created model, it is wise to make sure that our training data is varied and has good coverage of all the various fields we want to train our model for. We can do this by selecting datasets with our training data, and create a data quality report on them.

{% tabs %}
{% tab title="CLI" %}
```bash
$ las models create-data-bundle --name "Initial data report" las:model:<model id> las:dataset:<dataset id>
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
{% endtab %}
{% endtabs %}

A data report takes a few minutes to process. After it has been processed we can look at the summary to get an idea of how good our data is.

{% tabs %}
{% tab title="CLI" %}
```bash
$ las models list-data-bundles las:model:<model id>
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
{% endtab %}
{% endtabs %}

{% hint style="success" %}
See [models concepts](../concepts/models.md) for detailed information about data quality and how to improve it
{% endhint %}

