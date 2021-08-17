# Models

A model in Cradl is a custom-made machine learning program, which can be used to make [Predictions](predictions.md) on [Documents](documents.md) to extract exactly the data that you need. Our models are tailored to the training data you supply in [Data bundles](training-data.md), and are capable of extracting a range of data, whether that is date and total amount from receipts, specific payment data from invoices, or name and age from ID cards. 

## What is a model?

Our models are state-of-the-art machine learning algorithms. This means that you don't need to make any assumptions about the layout of the documents to make predictions on, such as supplying keywords or creating templates. Given sufficient training examples, our models learn how to search for and extract data from documents, based solely on the supplied training data.

The process of tailoring an algorithm to your specific use case is called _training_. Similar to how you would train a fresh employee to read out information from forms and documents, we teach our models how to extract data. This means we need to have a good set of _training data_ to begin teaching from, in the form of [Datasets](datasets.md) bundled together in a [Data bundle](training-data.md). 

{% hint style="warning" %}
It is important that there is enough training data, and that the data are correct and of high quality. If the training data has errors, you will be teaching the model to make those same errors. Read more about [Data quality](training-data.md#data-quality) if you are in doubt whether your data will be good enough.
{% endhint %}

## Creating a model

Every model has a specified `width`, `height` and `fieldConfig`. The `width` and `height` describe the image resolution used for input,  while the `fieldConfig` specifies which fields to extract, and what type of data the field represents. 

The `fieldConfig` input is specified in a JSON formatted file.

{% hint style="warning" %}
The label names \(`"total_amount"` and`"due_date"`below\) must match the label names given in the training data.
{% endhint %}

```text
>> cat path/to_field_config.json
{
  "total_amount": {
    "type": "amount",
    "maxLength": 10
  },
  "due_date": {
    "type": "date",
    "maxLength": 10
  }
}
```

Using this JSON file, you can define a model.

```text
>> las models create 321 321 path/to/field_config.json --name "Invoice" --description "v1"
{
  "modelId": "las:model:d9b89270448642a6817fc83896cbbd6b",
  "name": "Invoice",
  "description": "v1",
  "height": 321,
  "width": 321,
  "preprocessConfig": {
    "imageQuality": "LOW",
    "autoRotate": false,
    "maxPages": 1
  },
  "fieldConfig": {
    "total_amount": {
      "type": "amount",
      "maxLength": 10
    },
    "due_date": {
      "type": "date",
      "maxLength": 10
    }
  },
  "status": "inactive"
}
```

The model is now defined, and in an `inactive` state. Once you start training, it will change status to `training`, and when it is deployed after training, it will be in an `active` state. Additionally, you may supply a `preprocessConfig` which describes how to preprocess images entering the model.

### Choosing model parameters

#### Height and width

The `height` and `width` parameters of the model define the shape of images that the model accepts. If you use differently sized image, or a PDF, as input to the model, it will be resized to `height x width` before entering the model.

The size of the images has implications for training time, response time and accuracy of the model, since larger images require more computation to process, while higher resolution \(up to a certain point\) can improve the reading quality of the model - especially if your images contain fine print that would be illegible at lower resolutions.

{% hint style="warning" %}
We recommend that you choose image sizes as `(multiple of 320) + 1`, as this will map optimally with the underlying model structure, making training more efficient. 

For example, you could choose `1281 x 961` for A4 documents with fine print or `321 x 321` for square documents with larger print. 
{% endhint %}

#### Field config

The field config is a definition of which fields the models should extract and what the maximum character length of the extracted value per field should be. It should, if possible, give hints as to which type of data the field contains, which will allow for an extra layer of data validation when creating a [Data bundle](training-data.md). 

A field config is formatted as 

```text
{
  "field_name_1": {
    "type": "<field_type>",
    "maxLength": <integer max length of data>
  },
  "field_name_2": {
    "type": "<field_type>",
    "maxLength": <integer max length of data>
  },
  ...
}
```

where the &lt;field\_type&gt; is one of the following:

| **Field type** | **Description** |
| :--- | :--- |
| `date` | A date string on the format "DD-MM-YYYY" |
| `amount` | An amount string on the format "123.45" |
| `alphanum` | Any string with alphanumeric format |
| `alphanumext` | Any string with alphanumeric format, including some special characters |
| `all` | Any string with alphanumeric format, including more special characters |
| `letter` | Any string with latin characters only |
| `number` | Any string with numbers only |
| `phone` | Any phone number with or without country code |

## Linking a data bundle before training

Once a model is defined, you can attach one or more [Data bundles](training-data.md) to it to specify which data it should be trained on. You must have a data bundle of acceptable quality attached to your model to begin training. Read more about data quality [here](training-data.md#data-quality).

## Models

* What is a model?
* How does it work, what does it actually do?
* What is the difference between this and OCR templates?
* What do I need to train a model?
* Can I train a model several times?
* How can I improve the model?
* How long does it take?
* Time vs cost?
* How can I test the improvement after training?

### Field config

What is a field config and why do we need one?

|  |
| :--- |


### Width and height

What on earth is this?

### Data bundles

Explain how you use data bundles/reports to check your training data

What constitutes a good data bundle for training?

* Sufficient amount
* Good variation
* Representative data
* Correct data

How can I improve my data?

#### Data quality score

Explain variation and coverage

* How often should I run a report?
* What is a good score, when do I stop?
* Do I keep running these after a model is trained?

