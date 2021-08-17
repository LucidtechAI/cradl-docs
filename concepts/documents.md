# Documents

A document in Cradl represents a single data point which can be used for training or prediction. It consists of a file, possibly coupled with metadata describing the data that should be extracted from the document when used for training. Collections of document for training are called [Datasets](datasets.md).

## Creating a Document

Documents can either be uploaded directly to Cradl in the documents interface, or programmatically.

{% hint style="info" %}
Allowed formats for documents are .pdf or .jpeg.
{% endhint %}

```text
>> las documents create path/to/my/document.pdf
{
  "documentId": "las:document:84ed1bb2d2634072bd3134274ed56ebe",
  "contentType": "application/pdf"
}
```

The returned`documentId` can be used together with a `modelId` to make a prediction on the document. See [Predictions](predictions.md) for more details.

## Using a document as training data

To use a document to train a model, the document must be described by ground truth metadata. The metadata can be provided when you create the _Document_, or attached at a later stage.

```text
>> las documents create path/to/document.pdf --fields amount=100.00 due_date='2021-05-20'
>> las documents update <document-id> --fields amount=100.00 due_date='2021-05-20'
```

The document can now be added to a [Dataset](datasets.md), and from there on be used as training data.

## Documents with personal consents

## Deleting documents





What is a document?

How do I format the ground truth for a document?

How do I upload a document?

Which formats are allowed?

### Security and GDPR

How is the security of my documents ensured?

Are my documents being stored in compliance with GDPR?

How do I ensure my customers' right to be forgotten?





Our services help you control and automate the flow of your documents, and a _Document_ is therefore an important concept, and in this introduction you will see how a _Document_ can be created, controlled and used together with _Batches_, _Consents_, _Predictions_, and _Models_.

## 



