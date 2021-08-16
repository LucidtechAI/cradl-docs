# Define model

### Create model

Let's create a model we can start training using our datasets. A model requires some configuration in order to know what it should look for and train to predict values for. We can do this using a _field config_. Here we can define the name of our fields, and what type of values we expect them to return. These fields should match the ground truths given in the previous step while uploading documents.

A field config looks something like this:

```javascript
{
  "total_amount": { "type": "amount", "maxLength": 20, "description": "" },
  "purchase_date": { "type": "date", "maxLength": 10, "description": "" },
  "currency": { "type": "alphanum", "maxLength": 3, "description": "" }
}
```

Where the different types a field can be is one of these:

| Field type | Description |
| :--- | :--- |
| date | A date |
| amount | Difference between this and number? |
| alphanum | Any alphanumeric value |
| alphanumext | ? |
| all | Anything? |
| letter | Only letters? |
| number | A number |
| phone | A phone number |



Link to create model in Cradl

### Link model with training data

### Create data bundle / data report



