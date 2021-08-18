# Models

A model in Cradl is a custom-made machine learning program, which can be used to make [Predictions](predictions.md) on [Documents](documents.md) to extract exactly the data that you need. The models are tailored to the training data you supply in [Data bundles](training-data.md), and are capable of extracting a range of data, whether that is date and total amount from receipts, specific payment data from invoices, or name and age from ID cards. 

## What is a model?

Our models are state-of-the-art machine learning algorithms. This means that you don't need to make any assumptions about the layout of the documents to make predictions on, such as supplying keywords or creating templates. Given sufficient training examples, your model learns how to search for and extract data from documents, based solely on the supplied training data.

The process of tailoring an algorithm to your specific use case is called _training_. Similar to how you would train a fresh employee to read out information from forms and documents, we teach your models how to extract data. This means we need to have a good set of _training data_ to begin teaching from, in the form of [Datasets](datasets.md) bundled together in a [Data bundle](training-data.md). 

{% hint style="warning" %}
It is important that there is enough training data, and that the data are correct and of high quality. If the training data has errors, you will be teaching your model to make those same errors. Read more about [Data quality](training-data.md#data-quality) if you are in doubt whether your data will be good enough.
{% endhint %}

## Creating a model

Every model has a specified `width`, `height` and `fieldConfig`. The `width` and `height` describe the image resolution used for input,  while the `fieldConfig` specifies which fields to extract, and what type of data the field represents. 

The `fieldConfig` input is specified in a JSON formatted file.

{% hint style="warning" %}
The label names \(`"total_amount"` and`"due_date"`in the example below\) must match the label names given in the training data.
{% endhint %}

{% tabs %}
{% tab title="CLI" %}
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
{% endtab %}
{% endtabs %}

Using this JSON file, you can define a model.

{% tabs %}
{% tab title="CLI" %}
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
{% endtab %}
{% endtabs %}

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

The field config is a definition of which fields your model should extract and what the maximum character length of the extracted value per field should be. It should, if possible, give hints as to which type of data the field contains, which will allow for an extra layer of data validation when creating a [Data bundle](training-data.md). 

A field config is formatted as 

{% tabs %}
{% tab title="field\_config.json" %}
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
{% endtab %}
{% endtabs %}

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

Once your model is defined, you can create one or more [Data bundles](training-data.md) linked to it to specify which data it should be trained on. You must create a data bundle of acceptable quality linked to your model before training is allowed. This is a safety measure to improve the quality of the trained model. Read more about data quality [here](training-data.md#data-quality).

## Training a model

When you have created your model and successfully created a data bundle to be used for training, you are ready to request training. **INSERT LINK TO TRAINING BUTTON.**

The model will change status to `training`. This means that our team has begun training and validation of your model, and you will receive a notification from us once the model is ready for testing. This process may take several days before an initial model is produced, depending on the complexity and novelty of your requested model. For example, if your model contains data that we haven't encountered before \(new characters, data types, document types etc.\) we may need to add extra attention to ensure the final product is satisfactory.

Once your model's training is complete, it will change status to `active`. It is now ready to make [Predictions](predictions.md) and you may test it as you see fit before shipping it off to production.

## Improving a model

Any program can be improved - and machine learning models are no exception. You may see that every so often, your model makes an incorrect prediction on a certain field - perhaps some fields more often than others. Or the [confidence](predictions.md#confidence) levels of your predictions may seem a little low, especially as time goes by and the current data being fed to your model drifts from the data that the model was trained on. 

Often, the key to improving your model is to supply more fresh data \(or simply more historical data\), or to improve the quality of already existing data. You may want to sample some of your training data to check whether the ground truth attached to the documents perfectly match the data on the documents, or check for more historical data in your source systems. 

In any case, new and improved data should be uploaded and added to new dataset\(s\), and you need to create a new data bundle containing the new dataset\(s\) and request training. We will then initiate a new training session with more and/or better data, and you should expect further improvement on your existing model.

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

### 

