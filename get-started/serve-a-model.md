# Use model

After your model has been trained, it can be used and tested to make [predictions](../concepts/predictions.md). Assuming [good quality](../concepts/training-data.md#data-quality) input data has been used for training, you should see excellent predictions for your documents.

To make a prediction using a model, we need to provide a document id and a model id. We already have the id of our model, so let's upload a document to make a prediction on:

{% tabs %}
{% tab title="CLI" %}
```bash
las documents create receipt.pdf
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
}'
```
{% endtab %}

{% tab title="Python" %}
```python
document = client.create_document(b'<bytes data>', 'application/pdf')
```
{% endtab %}
{% endtabs %}

```javascript
{
  "documentId": "las:document:<document id>,
  ...
}
```

Using the document id from above, together with our model id, we get a prediction which includes the predicted values for each label, together with a confidence level suggesting how confident the model is of its prediction.

{% hint style="info" %}
See the [confidence section](../concepts/predictions.md#confidence) to read more about confidence levels and how you can use them to feel confident in your model's predictions.
{% endhint %}

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
--data-raw '{
    "documentId": "las:document:<document id>",
    "modelId": "las:model:<model id>"
}'
```
{% endtab %}

{% tab title="Python" %}
```python
prediction = client.create_prediction(document_id='las:document:<document id>', model_id='las:model:<model id>')
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

