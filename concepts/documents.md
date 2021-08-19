# Documents

A _document_ in Cradl represents a single data point which can be used for training or [Predictions](predictions.md). It consists of a file, with optional metadata containing the ground truth of what should be extracted from the document when used for training. Collections of documents for training are called [Datasets](datasets.md).

## Creating a Document

Documents can either be uploaded directly to Cradl in the documents interface, or programmatically.

{% hint style="success" %}
Allowed formats for documents are PDF, JPEG, PNG and TIFF.
{% endhint %}

{% tabs %}
{% tab title="CLI" %}
```bash
las documents create path/to/my/document.pdf
```
{% endtab %}

{% tab title="cURL" %}
```bash
curl -X POST 'https://api.cradl.ai/v1/documents' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer eyJra...' \
--data-raw '{
    "content": "JVBERi0xLjQ...",
    "contentType": "application/pdf"
 }'
```
{% endtab %}
{% endtabs %}

```javascript
{
  "documentId": "las:document:84ed1bb2d2634072bd3134274ed56ebe",
  "contentType": "application/pdf"
}
```

The returned`documentId` can be used together with a `modelId` to make a [prediction](predictions.md#making-a-prediction) on the document. 

## Setting a ground truth

Before using a document to training a model, the document must be described by a ground truth. The ground truth can be provided when you create the document, or it can be added as an update to an existing document.

{% tabs %}
{% tab title="CLI" %}
```bash
las documents create path/to/document.pdf --ground-truth-fields amount=100.00 due_date='2021-05-20'
las documents create path/to/document.pdf --ground-truth-path path/to/ground_truth.json
las documents update <document-id> --ground-truth-fields amount=100.00 due_date='2021-05-20'
las documents update <document-id> --ground-truth-path path/to/ground_truth.json
```
{% endtab %}

{% tab title="cURL" %}
```bash
curl -X POST 'https://api.cradl.ai/v1/documents' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer eyJra...' \
--data-raw '{
    "content": "JVBERi0xLjQ...",
    "contentType": "application/pdf"
    "groundTruth": [
      {
        "label": "amount",
        "value": "100.00"
      },
      {
        "label": "due_date",
        "value": "2021-05-20"
      }
    ]
  }'


curl -X PATCH 'https://api.cradl.ai/v1/documents/<documentId>' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer eyJra...' \
--data-raw '{
    "groundTruth": [
      {
        "label": "amount",
        "value": "100.00"
      },
      {
        "label": "due_date",
        "value": "2021-05-20"
      }
    ]
  }'
```
{% endtab %}
{% endtabs %}

The document can now be added to a [Dataset](datasets.md), and from there on be used as training data. The JSON format for a ground truth file is an array of objects containing `label` and `value` fields. Labels and values must be strings.

{% tabs %}
{% tab title="ground\_truth.json" %}
```python
[
    {
      "label": "amount",
      "value": "100.00"
    },
    {
      "label": "due_date",
      "value": "2021-05-20"
    }
]
```
{% endtab %}
{% endtabs %}

{% hint style="info" %}
The label name is used as a key in several places. Ensure that you are consistent in using the same label names across documents and models.
{% endhint %}

## Documents with personal consents

In addition to grouping documents in datasets, documents can be assigned a `consentId` to facilitate deletion of single-user data. If your application requires users to register data use consent, you should label this consent by a user-unique ID, and label all user data uploaded to Cradl with a corresponding `consentId` at creation time.

{% tabs %}
{% tab title="CLI" %}
```bash
las documents create path/to/document.pdf --consent-id <user-unique-id>
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
    "consentId": <user-unique-id>
 }'
```
{% endtab %}
{% endtabs %}

## Deleting documents

Documents may be deleted one-by-one:

{% tabs %}
{% tab title="CLI" %}
```bash
las documents delete <document-id>
```
{% endtab %}

{% tab title="cURL" %}
```bash
curl -X DELETE 'https://api.cradl.ai/v1/documents/<documentId>' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer eyJra...' \
```
{% endtab %}
{% endtabs %}

Or using a group identifier \(`consentId` or `datasetId`\):

{% tabs %}
{% tab title="CLI" %}
```bash
las documents delete-all --dataset-id <dataset-id>
```
{% endtab %}

{% tab title="cURL" %}
```bash
curl -X DELETE 'https://api.cradl.ai/v1/documents/<documentId>' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer eyJra...' \
--data-raw '{
    "datasetId": <datasetId>
 }'
```
{% endtab %}
{% endtabs %}

```javascript
{
  "documents": [...],
  "consentId": [...]
}
```

The delete-all command will delete all documents with the given group identifier.

