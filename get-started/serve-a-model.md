# Serve model

After a model has been trained, it can be used and tested to make predictions. Assuming good quality input data has been used for training, you should see excellent predictions for your documents.

To make a prediction using a model, we need to provide a document id and a model id. We already have the id of our model, so let's upload a document to make a prediction on:

{% tabs %}
{% tab title="CLI" %}
```bash
$ las documents create receipt.pdf
{
  "documentId": "las:document:<document id>,
  ...
}
```
{% endtab %}
{% endtabs %}

{% tabs %}
{% tab title="CLI" %}
```bash
$ las predictions create las:document:<document id> las:model:<model id>
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
{% endtab %}
{% endtabs %}

{% hint style="info" %}
See [models concepts](../concepts/models.md) to read more about confidence levels and how you can use them to feel confident in the predictions
{% endhint %}

