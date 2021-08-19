# Predictions

A prediction in Cradle represents an application of an active, trained [Model](models.md) to a [Document](documents.md) with the purpose of extracting data from the document. It supplies the extracted data together with confidence values representing the probability that the extracted data is correct.

## Making a prediction

Once a model is trained and active, it can be applied to documents by making a prediction.

{% tabs %}
{% tab title="CLI" %}
```bash
las predictions create <document id> <model id>
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
prediction = client.create_prediction(document_id=<document id>, model_id=<model id>)
```
{% endtab %}
{% endtabs %}

```javascript
{
  "predictionId": "<prediction id>",
  "modelId": "<model id>",
  "documentId": "<document id>",
  "predictions": [
    {
      "label": "total_amount",
      "value": "100.00",
      "confidence": 0.9758162361908527
    },
    {
      "label": "due_date",
      "value": "2021-05-20",
      "confidence": 0.96797316745869735
    },
  ],
  "timestamp": 1629188787,
  "inferenceTime": 2.7935566902160645
}
```

The above example shows an application to an example document. Each label in the model has a predicted value, together with a confidence value ranging from 0 \(worst\) to 1 \(best\).

## Confidence

Every field the model extracts has a corresponding confidence value. The confidence is different from a traditional OCR confidence in that it not only estimates the probability that the characters are interpreted correctly, but also that it has extracted the correct information \(e.g. the total amount and not the VAT amount\). 

#### What does a good confidence value look like?

What constitutes a good confidence value depends on how difficult it is to make a prediction for the field in question. For instance, account numbers often follow strict rules of composition and quite often located in obvious places, so a model can often confidently predict an account number once it has found a suitable candidate. On the other hand, predicting the name of a sales representative in a document can be hard, as it often requires reading a long string of characters which may be located in various places, often competing for attention with other names on the document. 

Your model will have different confidence profiles for each field, so while having a prediction with a confidence of 0.9 might be good for the sales representative name, it might be on the low end of confidence for the bank account number. Determining what is a good confidence should be handled on a field-by-field basis, but as a rule of thumb, confidences below 0.7 can be considered uncertain, confidences between 0.7 and 0.9 are more often than not correct, and confidences above 0.9 could be considered good, with confidences of 0.99 and above being near-certain.

#### Automation thresholds

Confidence levels can be used for automation - you may wish to use the predictions to pre-fill certain form values if the confidence exceeds a certain threshold, and to leave it blank or otherwise notify the user of uncertainty if the confidence is below that threshold. Since a model's confidence profile varies from field to field, you should have difference confidence levels per field.

The choice of automation threshold should be informed by your error acceptance rate. Any model will make mistakes, given enough work to do. The higher you set your automation threshold, the better your automated predictions will be, but the number of automated predictions will decline. When a model is fully trained, we can help you tune your thresholds to suit your use case.

#### How to boost a model's confidence

Confidence values are affected by the training process. If your training data contains errors in the ground truths, the model will be less confident in its predictions. The mechanism behind this is quite intuitive: if your model makes a correct prediction while training, but the ground truth \(erroneously\) says otherwise, the model will become less confident, just as a human trainee would be less confident in making predictions if their supervisor proclaimed they'd made a mistake when in fact they had not.

