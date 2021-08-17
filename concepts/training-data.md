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



## Data quality

