# Data bundles

A _data bundle_ in Cradl is a collection of one or more [Datasets](datasets.md) attached to a [Model](models.md). Before training a model, you must specify a data bundle that the model should use as training data. Since the quality of the trained model depends on the quality of the training data, we require that any data bundles used for training must pass a statistical test in the form of a [Data Report](training-data.md#data-report) before training can begin.

## Creating a data bundle

To create a data bundle for a model you must specify the `modelId` and one or more `datasetIds`, optionally giving it a name and description. See [Creating a model](models.md#creating-a-model) and [Creating a dataset](datasets.md#creating-a-dataset) for how to create models and datasets.

{% tabs %}
{% tab title="CLI" %}
```text
>> las models create-data-bundle <modelId> <datasetId_1> <datasetId_2> --name "Invoice model bundle v1" --description "Data bundle from first two datasets"  
{
  "dataBundleId": "las:model-data-bundle:dd0880f2ada445b595213ece5eaa6860",
  "modelId": "las:model:c613156351954b26a30e66412a218aef",
  "name": "Invoice model bundle v1",
  "description": "Data bundle from first two datasets",
  "datasets": [
    {
      ...
    },
    {
      ...
    }
  ],
  "summary": null,
  "status": "processing",
}

```
{% endtab %}
{% endtabs %}

The data bundle will immediately begin to generate a [Data Report](training-data.md#data-report). This process may take a few minutes, depending on the size of the datasets being used. While this process is running, the data bundle will have status `processing`. When the data report is complete, the data bundle will be in a `ready` state.

## Data report

The data report can be viewed in the Cradl app. It scores the data contained in the data bundle, based on several measures of data quality. Scores are first given to each label present in the underlying datasets,  based on the following statistical measures:

Completeness: The relative occurrence frequency of values for the label.

Validity: The percentage of valid values among the label's values.

Coverage: The product of Completeness and Validity, i.e. the relative occurrence frequency of valid values for the label.

Uniqueness: The percentage of values not among the top 10 most frequently occurring.

Uniformity: The contribution to Shannon entropy from values not among the top 10 most frequently occurring, in proportion to the maximally obtainable Shannon entropy for the label's data.

Variation: The mean of Uniqueness and Uniformity.

The scores for Coverage and Variation are then aggregated to cross-label statistics by taking the mean, and the mean score of these aggregate statistics constitutes the overall score for the data bundle.

If the overall score is at an acceptable level, you may request training for your model with the data in the bundle as training data. If the data are rejected, you will need to improve the data in one or more of the ways outlined in the section on [Data quality](training-data.md#data-quality).

Whenever you update an underlying dataset, by adding/removing/updating documents, you should re-run the data report for affected data bundles. Re-running a data report without changing the underlying data has no effect.

Once your model is trained, you do not need to continue running data reports unless you wish to re-train your model using different data.

## Data quality

Having a good set of training data is the most important factor when making a machine learning model - and Cradl's models are no exception to this rule. Your data must check all of the following boxes if you want to successfully train a model that is accurate and able to generalize to previously unseen examples.

#### Sufficient quantity

We humans have a life of experience and context to help us conceptualize and speed up our learning process when learning new tasks, such as reading information out of documents. We can therefore learn from fewer examples than the most powerful AI algorithms today. In Cradl, we have therefore set a minimum count at 10 000 examples per field  and a passable Coverage value to allow training. If your data do not satisfy these requirements, you will need to find more training examples.

{% hint style="info" %}
#### Example

Your datasets contain 10 000 invoices, of which 800 contain a value for`company_name` in the ground truth. 

You will not be able to train a model to extract the `company_name` data of your invoices, and must either find more examples containing`company_name` data, or leave the`company_name` field out of your model until enough data is collected to properly train the model.
{% endhint %}

#### Good variation

Machine learning algorithms are very impressionable by nature, and may skew their predictions if the data they are trained on is skewed in some way. One such example of skewness is lack of variation - having too   many similar examples in the training data.  The variation of your data is quantified in the Variation statistic of the [Data report](training-data.md#data-report). 

{% hint style="info" %}
#### Example

Building on the above example, suppose you have extracted an additional 10 000 invoices from your archival system, all of which contain a`company_name`field, for a total of 10 800 invoices with`company_name`. This is a sufficient quantity of `company_name` examples - however, if all the additional 10 000 invoices were issued by the same company, over 90% of your examples would be from a single company. It is then far too easy for your model to predict only that company's name - after all, that strategy is successful 90% of the time, which is hard to beat. 

In this case, your data report would fail on the Uniqueness statistic, and you would need to either find more varied examples containing`company_name` data, or leave the`company_name` field out of your model until enough data is collected to properly train the model.
{% endhint %}

#### Representative data

A more subtle way of having skewed data is not obtaining training data that represents the range of documents you want the model to read. If, for instance, your training data contains documents issued in English, Norwegian and German, you should not expect your model to be able to read Chinese - or perhaps even Dutch - documents, since the formatting and standards may vary from country to country. This is not limited to geographical differences; for instance, if you train a model to read personal data from drivers' licences, you shouldn't expect it to be able to read the same kind of data from passports without supplying a sufficient amount of passport data.

Since our models do now know in advance what sort of documents they will be used for reading, it is up to you to supply sufficient data for your use cases.

#### Correct data

Last, but not least: The training data you supply must, in large part, be correct, so that your model does not inherit the errors made in the underlying data. Our models learn by example, and if they are shown faulty examples, they will inherit those faults. Thus, the more errors are present in the data, the lower the quality of the predictions from the trained model.

To ensure that your data is correct, you should inspect the data beforehand by taking samples and checking that the information presented in the ground truth of a document is, in fact, present on the document.

{% hint style="info" %}
#### Example

You want to extract the due date of invoices, but due to clerical errors, some of the data entered into your archival system is in fact the date of issuance, which is different from the due date. If these errors are present in only a few documents, it will not pose a large issue when training. However, if this is a systematical error, you need to either discard the erroneous data and obtain new, correct data - or correct the erroneous data before training.
{% endhint %}

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

