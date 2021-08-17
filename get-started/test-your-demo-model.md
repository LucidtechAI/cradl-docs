# Test your demo model

After getting access to Cradl, you should have a demo model that is pre-trained available, that we can use for testing purposes.

{% hint style="warning" %}
Note that the demo model has been pre-trained for a specific use-case, using documents that are not necessarily representative of your own data. Hence the resulting predictions on your own documents during testing may not yield a great result.
{% endhint %}

First let's list our available models to get a model id we can use:

{% tabs %}
{% tab title="CLI" %}
```bash
$ las models list
{
  "models": [
    {
      "modelId": "las:model:<model id>",
      "name": "Demo model",
      "description": null,
      "height": 1281,
      "width": 801,
      "preprocessConfig": {
        "imageQuality": "LOW",
        "autoRotate": false,
        "maxPages": 1
      },
      "fieldConfig": {
        "total_amount": {
          "maxLength": 30,
          "type": "amount",
          "description": "Total amount"
        }
      },
      "status": "active",
      "createdTime": "2021-06-29T14:28:15.736079+0000",
      "updatedTime": null,
      "createdBy": null,
      "updatedBy": null
    }
  ]
}
```
{% endtab %}
{% endtabs %}

