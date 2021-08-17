# Datasets

A dataset in Cradl is a collection of [Documents](documents.md), typically from a single source, to be used for training. One or more datasets are collected in a data bundle when you specify which data to use when training a [Model](models.md).

## Creating a dataset

Datasets are created independently of the documents they contain.

```text
>> las datasets create --name "Invoices 2020" --description "From accounting system"
```

{% hint style="info" %}
Give your datasets clear names and descriptions. This will be helpful when specifying which data to train a model from.
{% endhint %}

## Adding documents to a dataset

Documents can be assigned to a dataset either at creation or from an update. It is not possible to assign a document to multiple datasets.



## Deleting a dataset

A dataset may not be deleted unless all documents contained in the dataset are deleted first.



I want to know:

* What is a dataset?
* Why do you want to use one?
* Should you group documents in a specific way?

