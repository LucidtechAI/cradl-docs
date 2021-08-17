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



## Data report

## Data quality





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

