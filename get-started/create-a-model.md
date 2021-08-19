# Define model

### Create model

Let's create a model that fits our data and use case. A model requires some configuration in order to know what it should look for and train to predict values for. We can do this using a **field config**. Here we can define the name of our fields, and what type of values we expect them to return.

Let's pretend that we have some receipts that we'd like to get the total amount, and date from. We can create a field config file that looks something like this:

{% code title="field\_config.json" %}
```javascript
{
  "total_amount": { "type": "amount", "maxLength": 20, "description": "" },
  "date": { "type": "date", "maxLength": 10, "description": "" }
}
```
{% endcode %}

{% tabs %}
{% tab title="CLI" %}
```bash
las models create --name "Receipt model" 1281 801 field_config.json
```
{% endtab %}

{% tab title="cURL" %}
```bash
curl -X POST 'https://api.cradl.ai/v1/models' \
--header 'Content-Type: application/json' \
--data-raw '{
    "fieldConfig": {
      "total_amount": { "type": "amount", "maxLength": 20, "description": "" },
      "purchase_date": { "type": "date", "maxLength": 10, "description": "" }
    },
    "height": 1281,
    "width": 801,
    "name": "Receipt model"
}'
```
{% endtab %}

{% tab title="Python" %}
```python
field_config = {
  'total_amount': { 'type': 'amount', 'maxLength': 20, 'description': '' },
  'purchase_date': { 'type': 'date', 'maxLength': 10, 'description': '' }
}
model = client.create_model(width=1281, height=801, field_config=field_config, name='Receipt model')
```
{% endtab %}
{% endtabs %}

{% hint style="info" %}
See [models concepts](../concepts/models.md) for detailed information about field config and other parameters used to define and create a model
{% endhint %}

Link to create model in Cradl

