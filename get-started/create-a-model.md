# Define model

### Create model

Let's create a model we can start training using our datasets. A model requires some configuration in order to know what it should look for and train to predict values for. We can do this using a _field config_. Here we can define the name of our fields, and what type of values we expect them to return. These fields should match the ground truths given in the previous step while uploading documents.

Let's create a field config file that looks something like this:

{% code title="field\_config.json" %}
```javascript
{
  "total_amount": { "type": "amount", "maxLength": 20, "description": "" },
  "purchase_date": { "type": "date", "maxLength": 10, "description": "" },
}
```
{% endcode %}

{% hint style="info" %}
See [models concepts](../concepts/models.md) for detailed information about field config and other parameters
{% endhint %}

Link to create model in Cradl

### Link model with training data

### Create data bundle / data report



