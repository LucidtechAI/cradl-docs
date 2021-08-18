# Data bundles

A data bundle in Cradl is a collection of one or more [Datasets](datasets.md) attached to a [Model](models.md). When training a model, you must specify a data bundle that the model should use as training data. Since the quality of the trained model depends on the quality of the provided data, we require that any data bundles used for training must pass a statistical test in the form of a [Data Report](training-data.md#data-report) before being used as training data.

## Creating a data bundle

To attach a data bundle to a model you need to specify the `modelId` and one or more `datasetIds`, optionally giving it a name and description. See [Creating a model](models.md#creating-a-model) and [Creating a dataset](datasets.md#creating-a-dataset) for how to create models and datasets.

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

## Data quality

Having a good set of training data is the most important factor when making a machine learning model - and Cradl's models are no exception to this rule. Your data must check all of the following boxes if you want to successfully train a model that is accurate and able to generalize to previously unseen examples.

#### Sufficient quantity

We humans have a life of experience and context to help us conceptualize and speed up our learning process when learning new tasks, such as reading information out of documents. We can therefore learn from fewer examples than the most powerful AI algorithms today. In Cradl, we have therefore set a minimum count at 10 000 examples per field to allow training. If your data does not satisfy this requirement, you will need to procure more documents as training examples. 

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

