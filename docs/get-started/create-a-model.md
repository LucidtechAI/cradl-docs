---
sidebar_position: 4
---

# Define model

## Create model

After testing the demo model, we're ready to build on our very own model. We'll begin by creating a model that fits our data and use case.

A model requires some configuration to know what values it's supposed to predict. This is summarized in a **field config**, where we define the name of the fields and what type of values we expect them to be.

Let's pretend that we have some receipts and that we'd like to extract the total amount and date from them. We can create a field config file that looks something like this:

{% code title="field\_config.json" %}
```javascript
{
  "total_amount": { "type": "amount", "maxLength": 20},
  "date": { "type": "date", "maxLength": 10}
}
```
{% endcode %}

Next we'll use the field config to create an un-trained model:

{% tabs %}
{% tab title="CLI" %}
```bash
las models create --name "Receipt model" --width 1281 --height 801 --field-config-path field_config.json
```
{% endtab %}

{% tab title="cURL" %}
```bash
curl -X POST 'https://api.cradl.ai/v1/models' \
--header 'Content-Type: application/json' \
--data-raw '{
    "fieldConfig": {
      "total_amount": { "type": "amount", "maxLength": 20},
      "purchase_date": { "type": "date", "maxLength": 10}
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
  'total_amount': { 'type': 'amount', 'maxLength': 20},
  'purchase_date': { 'type': 'date', 'maxLength': 10}
}
model = client.create_model(width=1281, height=801, field_config=field_config, name='Receipt model')
```
{% endtab %}
{% endtabs %}

{% hint style="info" %}
See [models concepts](../concepts/models.md) for more information about field configs, and what the width and height parameters mean when creating a model.
{% endhint %}
