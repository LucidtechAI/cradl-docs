# Data bundles

To attach a data bundle to a model you need to specify the modelId and one or more datasetIds, optionally giving it a name and description.

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

