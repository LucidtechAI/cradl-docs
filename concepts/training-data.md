# Data bundles

A _data bundle_ in Cradl is a collection of one or more [Datasets](datasets.md) attached to a [Model](models.md). Before training a model, you must specify a data bundle that the model should use as training data. Since the quality of the trained model depends on the quality of the training data, we require that any data bundles used for training must pass a statistical test in the form of a [Data Report](training-data.md#data-report) before training can begin.

## Creating a data bundle

To create a data bundle for a model you must specify the `modelId` and one or more `datasetIds`, optionally giving it a name and description. See [Creating a model](models.md#creating-a-model) and [Creating a dataset](datasets.md#creating-a-dataset) for how to create models and datasets.

{% tabs %}
{% tab title="CLI" %}
```bash
las models create-data-bundle <modelId> <datasetId_1> <datasetId_2> --name "Invoice training data v1" --description "Training data from first two datasets"  
```
{% endtab %}

{% tab title="cURL" %}
```bash
curl -X POST 'https://api.cradl.ai/v1/models/<modelId>/dataBundles' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer eyJra...' \
--data-raw '{
    "datasetIds": [
        "<datasetId_1>",
        "<datasetId_2>"
    ],
    "name": "Invoice model training data v1",
    "description": "Training data from first two datasets"
}'
```
{% endtab %}

{% tab title="Python" %}
```python
data_bundle = client.create_data_bundle(
    model_id=<model_id>, 
    dataset_ids=[<datasetId_1>, <datasetId_2>], 
    name="Invoice model training data v1",
    description="Training data from first two datasets",
)
```
{% endtab %}
{% endtabs %}

```javascript
{
  "dataBundleId": <dataBundleId>,
  "modelId": <modelId>,
  "name": "Invoice model training data v1",
  "description": "Training data from first two datasets",
  "datasets": [
    {
      ...
    },
    {
      ...
    }
  ],
  "summary": null,
  "status": "processing"
}
```

The data bundle will immediately begin to generate a [Data Report](training-data.md#data-report). This process may take a few minutes, depending on the size of the datasets being used. While this process is running, the data bundle will have status `processing`. When the data report is complete, the data bundle will be in a `ready` state.

## Updating a data bundle

Whenever you have updated a dataset, by adding, removing or updating documents, you must update the affected data bundles in order to use the updated data for training.

{% tabs %}
{% tab title="CLI" %}
```bash
las models update-data-bundle <modelId> <dataBundleId>
```
{% endtab %}

{% tab title="cURL" %}
```bash
curl -X PATCH 'https://api.cradl.ai/v1/models/<modelId>/dataBundles/<dataBundleId>' \
--header 'Authorization: Bearer eyJra...'
```
{% endtab %}

{% tab title="Python" %}
```python
data_bundle = client.update_data_bundle(
    model_id=<modelId>, 
    data_bundle_id=<dataBundleId>,
)
```
{% endtab %}
{% endtabs %}

## Data report

The data report can be viewed in the Cradl app. It scores the data contained in the data bundle, based on several measures of data quality. First, each label present in the underlying documents is scored based on the following statistical measures:

| Measure | Description |
| :--- | :--- |
| **Completeness** | Percentage of documents with values. |
| **Validity** | Percentage of valid values among occurring values. |
| **Coverage** | Percentage of documents with valid values. |
| **Uniqueness** | Percentage of values outside the top 10 most frequent. |
| **Uniformity** | Proportion of information entropy in values outside the top 10 most frequent, relative to maximum obtainable entropy. Put simply, this measures how much different information is present in the values. |
| **Variation** | Mean of Uniqueness and Uniformity. |

After scoring each label individually, the Coverage and Variation scores are aggregated to cross-label mean statistics. The overall score for the data bundle is the mean of these aggregate Coverage and Variation statistics.

If the overall score is acceptable \(suggested value is 70%-100%\), you can request training for your model with the data in the bundle as training data. If not, you should improve your data in one or more of the ways outlined in the section on [Data quality](training-data.md#data-quality).

## Data quality

Having a good set of training data is the most important factor when building a machine learning model, and Cradl models are no exception. Your data must check all of the following boxes if you want to successfully train a model that is accurate and able to generalize to new documents.

#### Sufficient quantity

Humans have a life of experience and context to help us conceptualize and speed up our learning process when faced with new tasks. We can therefore learn from fewer examples than the most powerful machine learning algorithms today. In Cradl, we have set a minimum of 10 000 documents to allow training. In fact, to achieve good results we recommend that each label have 10 000 associated ground truths.

{% hint style="info" %}
#### Example

Your datasets contain a total of 10 000 invoices, of which 800 contain a value for a field called`company_name` in the ground truth. 

While the number of documents in total is good, we would not be able to guarantee good results for predictions on the `company_name` field due to few examples.
{% endhint %}

#### Good variation

Machine learning algorithms are impressionable by nature, and can skew their predictions if the training data is skewed. One example of skewness is lack of variation: having too many similar examples in the training data.  The variation of your data is quantified in the Variation statistic of the [Data report](training-data.md#data-report). 

{% hint style="info" %}
#### Example

Building on the above example, suppose you have extracted an additional 10 000 invoices from your archive, all of which contain a`company_name`field, so you now have a total of 10 800 invoices with`company_name`values. This is a good number of `company_name` examples, but if all the additional 10 000 invoices were issued by just one company, over 90% of your examples would be from a single company. It is then easy for your model to predict only that company's name - after all, this strategy is successful 90% of the time, which is hard to beat. 

In this case, your data report get a low score on the Uniqueness statistic, and you should either find more varied examples containing`company_name` data, or leave the`company_name` field out of your model until you have collected enough data to properly train the model.
{% endhint %}

#### Representative data

Another way you data may be skewed is if it doesn't represent the range of documents you actually want the model to read. If, for instance, your training data contains documents issued in English and German, it will be hard for your model to read Chinese - or perhaps even Dutch - documents, since language, formatting and standards vary from country to country. This is not limited to geographical differences; if you train a model to read personal data from drivers' licences, you can't expect it to read data from passports without supplying a good amount of passport data as well.

Since our models don't now know in advance what sort of documents they will be used for reading, it is up to you to supply sufficient data for your use cases.

#### Correct data

Last, but not least: The ground truths for the training data you supply must be correct, so that your model does not inherit any errors from the underlying data. Our models learn by example, and if they are shown faulty examples, they may inherit those faults. The more errors are present in the data, the lower the quality of the predictions from the trained model.

To ensure that your data is correct, you should inspect it beforehand by taking samples and checking that the information presented in the ground truth of a document is, in fact, correct and present on the document.

{% hint style="info" %}
#### Example

You want to extract the due date of invoices, but due to clerical errors, some of the data entered into your archive system is actually the date of payment, which may be different from the due date. If such errors are present in only a few documents, it will not pose a large issue when training. However, if this is a systematic error, you should either discard the erroneous data and obtain new, correct data, or correct the erroneous data before training.
{% endhint %}

