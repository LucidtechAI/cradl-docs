# Models

A model in Cradl is a custom-made machine learning program, which can be used to make [Predictions](predictions.md) on [Documents](documents.md) to extract exactly the data that you need. Our models are tailored to the training data you supply as [Datasets](datasets.md), and are capable of extracting a range of data, whether that is date and total amount from receipts, specific payment data from invoices, or name and age from ID cards. 

## What is a model?

Our models are state-of-the-art machine learning algorithms. This means that you don't need to make any assumptions about the layout of the documents to make predictions on, such as supplying keywords or creating templates. Given sufficient training examples, our models learn how to search for and extract data from documents, based solely on the supplied training data.

The process of tailoring an algorithm to your specific use case is called _training_. Similar to how you would train a fresh employee to read out information from forms and documents, we teach our models how to extract data. This means we need to have a good set of _training data_ to begin teaching from, in the form of [Datasets](datasets.md) bundled together in a [Data bundle](training-data.md). 

{% hint style="warning" %}
It is important that the training is correct and of high quality. If the training data has errors, you will be teaching the model to make those same errors. Read more about [Data quality](training-data.md#data-quality) if you are in doubt whether your data will be sufficient.
{% endhint %}

## Creating a model

Every model has a specified `width`, `height` and `fieldConfig`. These describe the image resolution used for images 

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

| Field type | Description |
| :--- | :--- |
| date | A date |
| amount | **Difference between this and number?** |
| alphanum | Any alphanumeric value |
| alphanumext | **?** |
| all | **Anything?** |
| letter | **Only letters?** |
| number | A number |
| phone | A phone number |

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

