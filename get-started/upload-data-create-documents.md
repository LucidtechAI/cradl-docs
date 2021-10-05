## Upload many documents to a dataset with `datasets create-documents`
Uploading documents one by one is useful for small tests, but for thousands of documents it can be a slow and painful experience.
To make the process smoother we recommend to use `datasets create-documents` in the [CLI](../reference/cli.md) . This allows you to upload your dataset in a fast and consistent way, without worrying about looping over all the documents yourself.

### Upload a folder with document and ground truth pairs
In order to upload all the documents in a folder the following convention must be utilized:

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


### Upload a folder with all the meta-data in one file
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
