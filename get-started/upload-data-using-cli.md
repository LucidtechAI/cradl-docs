## Upload documents one by one to a dataset

After the dataset is created we can start uploading [documents](../concepts/documents.md) and assign them to our dataset. Since we want to use the documents for training, we'll also provide [ground truth values](../concepts/documents.md#setting-ground-truths) that will define the correct output for the model on each document. We'll have to make sure that the field names in the ground truth match those in the field config we made for our model.

{% hint style="warning" %}
It is important to have **correct** ground truth values for every document we use for training. Errors in the ground truth can degrade the training process as the model may learn to make the same mistakes.
{% endhint %}

{% tabs %}
{% tab title="CLI" %}
```bash
las documents create receipt.pdf --dataset-id <datasetId> --ground-truth-fields total_amount=300.00 date=2020-02-28
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
    "datasetId": <datasetId>,
    "groundTruth: [
      {
      "label": "total_amount",
      "value": "300.00"
      },
      {
        "label": "date",
        "value": "2020-02-28"
      }
    ]
}'
```
{% endtab %}

{% tab title="Python" %}
```python
ground_truth = [
  { 'label': 'total_amount', 'value': '300.00' },
  { 'label': 'date', 'value': '2020-02-28' }
]
document = client.create_document(b'<bytes data>', 'application/pdf', ground_truth=ground_truth, dataset_id=<datasetId>)
```
{% endtab %}
{% endtabs %}

```javascript
{
  "documentId": <documentId>,
  "contentType": "application/pdf",
  "retentionInDays": 1825,
  "createdTime": "2021-08-16T13:34:13.724393+0000",
  "updatedTime": null,
  "createdBy": <appClientId>,
  "updatedBy": null,
  "datasetId": <datasetId>,
  "groundTruth": [
    {
      "label": "total_amount",
      "value": "300.00"
    },
    {
      "label": "date",
      "value": "2020-02-28"
    }
  ]
}
```

{% hint style="success" %}
If you upload documents without assigning them to a dataset, or if you want to assign them to a different dataset in the future, you can do so easily using the API.
{% endhint %}

## Upload multiple documents to a dataset
Uploading documents one by one can be useful for testing purposes, but is not recommended for large scale training datasets.
For large-scale datasets we recommend using the `datasets create-documents` command from the [CLI](../reference/cli.md) . This allows you to upload your dataset in a fast and consistent way, without worrying about looping over all the documents yourself.

### Upload a folder with document and ground truth pairs
In order to upload all the documents in a folder, the following naming convention must be used:

1. each document in the folder must come with a ground truth as either a `.json|.yaml|.yml` file.
2. the ground truth is provided in the following format:
```json
[
    {
        "label": "total_amount",
        "value": "100.00"
    },
    {
        "label": "due_date",
        "value": "2021-10-30"
    },
    {
        "label": "vendor_name",
        "value": "Company X"
    }
]
```

3. The ground truth must have the same file name as the document. So if your document is named `a.pdf` the ground truth must be either `a.json`, `a.yaml` or `a.yml`. So your folder will need to look something like this:
```bash
my/new/training/data
├── invoice_a.pdf
├── invoice_a.json
├── invoice_b.png
├── invoice_b.json
├── invoice_c.png
└── invoice_c.json
```
When you have structured your data according to these 3 points you are ready to start uploading your data.

```shell
las datasets create-documents <datasetId> my/new/training/data
```

{% hint style="info" %}
If some of your documents are missing ground-truths they will simply be skipped.
{% endhint %}


### Upload a folder with all the meta data in one file
The other alternative is to specify a file that contains all the paths and ground truths to the documents we want to upload, let us call it `upload-specification.json`.
Below is an example of how this file would look if we only want to upload two documents.
```json
{
    "path/to/document1.pdf": {
        "ground_truth": [
            {
                "label": "total_amount",
                "value": "100.00"
            },
            {
                "label": "due_date",
                "value": "2021-10-30"
            },
            {
                "label": "vendor_name",
                "value": "Company X"
            }
        ]
    },
    "path/to/document2.png": {
        "ground_truth": [
            {
                "label": "total_amount",
                "value": "200.00"
            },
            {
                "label": "due_date",
                "value": "2021-11-30"
            },
            {
                "label": "vendor_name",
                "value": "Company Y"
            }
        ]
    }
}
```
The file is just a dictionary with the path to each document you want to upload as the keys, and their corresponding ground truth as values.
We are now ready to upload all the documents and their ground-truth by using the `create-documents` command in the `datasets` module.
```shell
las datasets create-documents <datasetId> upload-specification.json
```
This function automatically caches your progress, so if something interrupts the call it can be called again and take off right where it ended, without having to worry about the same documents being uploaded twice.
