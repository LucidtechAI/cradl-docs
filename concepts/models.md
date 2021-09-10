# Models

A model in Cradl is a custom machine learning model that can be trained to make [Predictions](predictions.md) on [Documents](documents.md) to extract exactly the data you need. The models will be tailored to the training data you supply in [Data bundles](training-data.md), and can extract a diverse range of data depending on your needs. Some examples: date and total amount from receipts, specific payment data from invoices, or name and age from ID cards.

## What is a model?

Our models are state-of-the-art machine learning algorithms. This means that you don't need to make any assumptions about the layout of the documents to make predictions on, such as supplying keywords or creating templates. Given sufficient training examples, your model learns how to search for and extract data from documents, based solely on the supplied training data.

The process of tailoring an algorithm to your specific use case is called _training_. Similar to how you would train a fresh employee to read out information from forms and documents, we teach your models how to extract data. This means we need to have a good set of _training data_ to begin teaching from, in the form of [Datasets](datasets.md) bundled together in a [Data bundle](training-data.md).

{% hint style="warning" %}
It is important to have enough high quality training data. If the training data has errors, you will be teaching your model to make those same errors. Read more about [Data quality](training-data.md#data-quality) if you are in doubt whether your data will be good enough.
{% endhint %}

## Creating a model

Every model has a specified `width`, `height` and `fieldConfig`. The `width` and `height` describe the image resolution used for input. The `fieldConfig` specifies which fields to extract and what type of data the field represents.

The `fieldConfig` input is specified in a JSON formatted file.

{% hint style="warning" %}
The label names \(`"total_amount"` and`"due_date"`in the example below\) must match the label names given in the training data.
{% endhint %}

{% tabs %}
{% tab title="field\_config.json" %}
```javascript
{
  "total_amount": {
    "type": "amount",
    "maxLength": 10
  },
  "due_date": {
    "type": "date",
    "maxLength": 10
  }
}
```
{% endtab %}
{% endtabs %}

Using this JSON layout, you can define a model.

{% tabs %}
{% tab title="CLI" %}
```bash
las models create 321 321 path/to/field_config.json --name "Invoice" --description "v1"
```
{% endtab %}

{% tab title="cURL" %}
```bash
curl -X POST 'https://api.cradl.ai/v1/models' \
--header 'Content-Type: application/json' \
--data-raw '{
    "fieldConfig": {
      "total_amount": { "type": "amount", "maxLength": 10 },
      "due_date": { "type": "date", "maxLength": 10 },
    },
    "height": 321,
    "width": 321,
    "name": "Invoice",
    "description": "v1"
}'
```
{% endtab %}

{% tab title="Python" %}
```python
field_config = {
  'total_amount': { 'type': 'amount', 'maxLength': 10, 'description': '' },
  'due_date': { 'type': 'date', 'maxLength': 10, 'description': '' },
}
model = client.create_model(
  width=321, 
  height=321, 
  field_config=field_config,
  name="Invoice",
  description="v1",
)
```
{% endtab %}
{% endtabs %}

```javascript
{
  "modelId": <modelId>,
  "name": "Invoice",
  "description": "v1",
  "height": 321,
  "width": 321,
  "preprocessConfig": {
    "imageQuality": "LOW",
    "autoRotate": false,
    "maxPages": 1
  },
  "fieldConfig": {
    "total_amount": {
      "type": "amount",
      "maxLength": 10
    },
    "due_date": {
      "type": "date",
      "maxLength": 10
    }
  },
  "status": "inactive"
}
```

The model is now defined, and in an `inactive` state. Once you start training, it will change status to `training`, and when it is deployed after training, it will be in an `active` state. Additionally, you may supply a `preprocessConfig` which describes how to preprocess images entering the model.

### Choosing model parameters

#### Height and width

The `height` and `width` parameters of the model define the shape of images that the model accepts. If you use a differently sized image, or a PDF, as input to the model, it will be resized to `height x width` before entering the model.

The size of the images has implications for training time, response time and accuracy of the model. This is because larger images require more computation to process, while higher resolution *may* improve the reading quality of the model - especially if your images contain fine print that would be illegible at lower resolutions.

{% hint style="warning" %}
We recommend that you choose image sizes as `(multiple of 320) + 1`, as this will map optimally with the underlying model structure, making training more efficient.

For example, you could choose `1281 x 961` for A4 documents with fine print or `321 x 321` for square documents with larger print.
{% endhint %}

#### Field config

The field config is a definition of which fields your model should extract and what the maximum character length of the extracted value per field should be. It gives hints about the data type of the field, allowing for an extra layer of data validation when creating a [Data bundle](training-data.md). **Note:** By specifying a `date` or `amount` type, outputs from the model will be automatically formatted.

A field config is formatted as

{% tabs %}
{% tab title="field\_config.json" %}
```python
{
  "field_name_1": {
    "type": "<field_type>",
    "maxLength": <integer max length of data>
  },
  "field_name_2": {
    "type": "<field_type>",
    "maxLength": <integer max length of data>
  },
  ...
}
```
{% endtab %}
{% endtabs %}

where the `<field_type>` is one of the following:

<table>
  <thead>
    <tr>
      <th style="text-align:left"><b>Field type</b>
      </th>
      <th style="text-align:left"><b>Data format</b>
      </th>
      <th style="text-align:left"><b>Characters in output</b>
      </th>
      <th style="text-align:left"><b>Output format</b>
      </th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left"><b><code>date</code></b>
      </td>
      <td style="text-align:left">Any valid date format</td>
      <td style="text-align:left"><code>-0123456789</code>
      </td>
      <td style="text-align:left"><code>YYYY-MM-DD</code>
      </td>
    </tr>
    <tr>
      <td style="text-align:left"><b><code>amount</code></b>
      </td>
      <td style="text-align:left">Decimal number</td>
      <td style="text-align:left"><code>-.0123456789</code>
      </td>
      <td style="text-align:left">
        <p><code> 123.45</code>
        </p>
        <p><code>-123.45</code>
        </p>
      </td>
    </tr>
    <tr>
      <td style="text-align:left"><b><code>alphanum</code></b>
      </td>
      <td style="text-align:left">String of alphanumeric characters (including space)</td>
      <td style="text-align:left">
        <p><code>␣0123456789</code>
        </p>
        <p><code>ABCDEFGHIJKLMNOPQRSTUVWXYZ</code>
        </p>
        <p><code>&#xC1;&#xC3;&#xC4;&#xC5;&#xC6;&#xC8;&#xC9;&#xCA;&#xCB;&#xCD;&#xCE;&#xD3;&#xD6;&#xD8;&#xDB;&#xDC;</code>
        </p>
      </td>
      <td style="text-align:left"><code>Any</code>
      </td>
    </tr>
    <tr>
      <td style="text-align:left"><b><code>alphanumext</code></b>
      </td>
      <td style="text-align:left">String of alphanumeric characters with common special characters (including space)</td>
      <td
      style="text-align:left">
        <p><code>␣0123456789</code>
        </p>
        <p><code>ABCDEFGHIJKLMNOPQRSTUVWXYZ</code>
        </p>
        <p><code>&#xC1;&#xC3;&#xC4;&#xC5;&#xC6;&#xC8;&#xC9;&#xCA;&#xCB;&#xCD;&#xCE;&#xD3;&#xD6;&#xD8;&#xDB;&#xDC;</code>
        </p>
        <p><code>&amp;,-./\</code>
        </p>
        </td>
        <td style="text-align:left"><code>Any</code>
        </td>
    </tr>
    <tr>
      <td style="text-align:left"><b><code>all</code></b>
      </td>
      <td style="text-align:left">String of alphanumeric characters with more special characters (including space)</td>
      <td
      style="text-align:left">
        <p><code>␣0123456789</code>
        </p>
        <p><code>ABCDEFGHIJKLMNOPQRSTUVWXYZ</code>
        </p>
        <p><code>&#xC1;&#xC3;&#xC4;&#xC5;&#xC6;&#xC8;&#xC9;&#xCA;&#xCB;&#xCD;&#xCE;&#xD3;&#xD6;&#xD8;&#xDB;&#xDC;</code>
        </p>
        <p><code>!&quot;#$%&amp;&apos;()*+,-./\:;&lt;=&gt;?@[]^_{|}&#xA7;</code>
        </p>
        </td>
        <td style="text-align:left"><code>Any</code>
        </td>
    </tr>
    <tr>
      <td style="text-align:left"><b><code>letter</code></b>
      </td>
      <td style="text-align:left">String of latin characters (including space)</td>
      <td style="text-align:left"><code>␣ABCDEFGHIJKLMNOPQRSTUVWXYZ</code>
      </td>
      <td style="text-align:left"><code>Any</code>
      </td>
    </tr>
    <tr>
      <td style="text-align:left"><b><code>number</code></b>
      </td>
      <td style="text-align:left">String of digits (including space)</td>
      <td style="text-align:left"><code>␣0123456789</code>
      </td>
      <td style="text-align:left"><code>Any</code>
      </td>
    </tr>
    <tr>
      <td style="text-align:left"><b><code>phone</code></b>
      </td>
      <td style="text-align:left">Phone number, country code optional</td>
      <td style="text-align:left"><code>+0123456789</code>
      </td>
      <td style="text-align:left"><code>Same as input format, w/o whitespace</code>
      </td>
    </tr>
  </tbody>
</table>

## Selecting training data

Once your model is defined, you can create one or more [Data bundles](training-data.md) to specify which data it should be trained on. You must create a data bundle of acceptable quality before training is allowed. Read more about data quality [here](training-data.md#data-quality).

{% hint style="info" %}
A Data bundle is model-specific, which means that it is defined as a nested resource under a specific model.
{% endhint %}

## Training a model

When you have created your model and successfully created a data bundle to be used for training, you are ready to request training. Training can be [requested in the Cradl UI](../get-started/train-a-model.md).

The model will change status to `training`. This means that our team has begun training and validation of your model, and you will receive a notification from us once the model is ready for testing. This process may take several days before an initial model is produced, depending on the complexity and novelty of your requested model. For example, if your model contains data that we haven't encountered before \(new characters, data types, document types etc.\) we may need to add extra attention to ensure that the final product is satisfactory.

Once your model's training is complete, it will change status to `active`. It is now ready to make [Predictions](predictions.md) and you may test it as you see fit before shipping it off to production.

## Improving a model

Any program can be improved - and machine learning models are no exception. You may see that every so often, your model makes an incorrect prediction on a certain field - perhaps some fields more often than others. Or the [confidence](predictions.md#confidence) levels of your predictions may seem a little low, especially as time goes by and the current data being fed to your model drifts from the data that the model was trained on.

Often, the key to improving your model is to supply more fresh data \(or simply more historical data\), or to improve the quality of already existing data. You may want to sample some of your training data to check whether the ground truth attached to the documents match the data on the documents, or check for more historical data in your source systems.

In any case, new and improved data should be uploaded and added to new dataset\(s\), which again is added to a new data bundle that will be used to request training. We will then initiate a new training session with more and/or better data, and you should expect further improvement on your existing model.

