#### DELETE /models/{modelId}


| Path name | Path value |
| --- | --- |
| modelId | Id of model on the form las:model:&lt;hex&gt; |


| Header name | Header value |
| --- | --- |
| Authorization | Bearer &lt;your access token here&gt; |








##### Response body JSON Schema
```json
{
  "title": "model",
  "required": [
    "createdBy",
    "createdTime",
    "description",
    "fieldConfig",
    "height",
    "modelId",
    "name",
    "numberOfDataBundles",
    "preprocessConfig",
    "status",
    "updatedBy",
    "updatedTime",
    "width"
  ],
  "type": "object",
  "properties": {
    "updatedTime": {
      "pattern": "^[0-9]{4}-?[0-9]{2}-?[0-9]{2}( |T)?[0-9]{2}:?[0-9]{2}:?[0-9]{2}(.[0-9]{1,6})?(Z|[+][0-9]{2}(:|)[0-9]{2})$",
      "type": "string",
      "nullable": true
    },
    "updatedBy": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "modelId": {
      "pattern": "^las:model:[a-f0-9]{32}$",
      "type": "string"
    },
    "description": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "fieldConfig": {
      "type": "object",
      "additionalProperties": {
        "required": [
          "maxLength",
          "type"
        ],
        "type": "object",
        "properties": {
          "description": {
            "anyOf": [
              {
                "maxLength": 4096,
                "type": "string"
              },
              null
            ]
          },
          "type": {
            "type": "string",
            "enum": [
              "date",
              "amount",
              "number",
              "letter",
              "phone",
              "alphanum",
              "alphanumext",
              "all",
              "string",
              "digits"
            ]
          },
          "maxLength": {
            "maximum": 100,
            "minimum": 1,
            "type": "integer"
          }
        }
      }
    },
    "preprocessConfig": {
      "required": [
        "autoRotate",
        "imageQuality",
        "maxPages"
      ],
      "type": "object",
      "properties": {
        "maxPages": {
          "maximum": 3,
          "minimum": 1,
          "type": "integer"
        },
        "autoRotate": {
          "type": "boolean"
        },
        "imageQuality": {
          "type": "string",
          "enum": [
            "LOW",
            "HIGH"
          ]
        }
      },
      "additionalProperties": false
    },
    "createdBy": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "name": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "width": {
      "maximum": 1921,
      "minimum": 97,
      "type": "integer"
    },
    "numberOfDataBundles": {
      "minimum": 0,
      "type": "integer"
    },
    "createdTime": {
      "pattern": "^[0-9]{4}-?[0-9]{2}-?[0-9]{2}( |T)?[0-9]{2}:?[0-9]{2}:?[0-9]{2}(.[0-9]{1,6})?(Z|[+][0-9]{2}(:|)[0-9]{2})$",
      "type": "string",
      "nullable": true
    },
    "height": {
      "maximum": 1921,
      "minimum": 97,
      "type": "integer"
    },
    "status": {
      "type": "string",
      "enum": [
        "active",
        "training",
        "inactive"
      ]
    }
  },
  "additionalProperties": false
}
```


#### GET /models/{modelId}


| Path name | Path value |
| --- | --- |
| modelId | Id of model on the form las:model:&lt;hex&gt; |


| Header name | Header value |
| --- | --- |
| Authorization | Bearer &lt;your access token here&gt; |








##### Response body JSON Schema
```json
{
  "title": "model",
  "required": [
    "createdBy",
    "createdTime",
    "description",
    "fieldConfig",
    "height",
    "modelId",
    "name",
    "numberOfDataBundles",
    "preprocessConfig",
    "status",
    "updatedBy",
    "updatedTime",
    "width"
  ],
  "type": "object",
  "properties": {
    "updatedTime": {
      "pattern": "^[0-9]{4}-?[0-9]{2}-?[0-9]{2}( |T)?[0-9]{2}:?[0-9]{2}:?[0-9]{2}(.[0-9]{1,6})?(Z|[+][0-9]{2}(:|)[0-9]{2})$",
      "type": "string",
      "nullable": true
    },
    "updatedBy": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "modelId": {
      "pattern": "^las:model:[a-f0-9]{32}$",
      "type": "string"
    },
    "description": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "fieldConfig": {
      "type": "object",
      "additionalProperties": {
        "required": [
          "maxLength",
          "type"
        ],
        "type": "object",
        "properties": {
          "description": {
            "anyOf": [
              {
                "maxLength": 4096,
                "type": "string"
              },
              null
            ]
          },
          "type": {
            "type": "string",
            "enum": [
              "date",
              "amount",
              "number",
              "letter",
              "phone",
              "alphanum",
              "alphanumext",
              "all",
              "string",
              "digits"
            ]
          },
          "maxLength": {
            "maximum": 100,
            "minimum": 1,
            "type": "integer"
          }
        }
      }
    },
    "preprocessConfig": {
      "required": [
        "autoRotate",
        "imageQuality",
        "maxPages"
      ],
      "type": "object",
      "properties": {
        "maxPages": {
          "maximum": 3,
          "minimum": 1,
          "type": "integer"
        },
        "autoRotate": {
          "type": "boolean"
        },
        "imageQuality": {
          "type": "string",
          "enum": [
            "LOW",
            "HIGH"
          ]
        }
      },
      "additionalProperties": false
    },
    "createdBy": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "name": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "width": {
      "maximum": 1921,
      "minimum": 97,
      "type": "integer"
    },
    "numberOfDataBundles": {
      "minimum": 0,
      "type": "integer"
    },
    "createdTime": {
      "pattern": "^[0-9]{4}-?[0-9]{2}-?[0-9]{2}( |T)?[0-9]{2}:?[0-9]{2}:?[0-9]{2}(.[0-9]{1,6})?(Z|[+][0-9]{2}(:|)[0-9]{2})$",
      "type": "string",
      "nullable": true
    },
    "height": {
      "maximum": 1921,
      "minimum": 97,
      "type": "integer"
    },
    "status": {
      "type": "string",
      "enum": [
        "active",
        "training",
        "inactive"
      ]
    }
  },
  "additionalProperties": false
}
```


#### PATCH /models/{modelId}


| Path name | Path value |
| --- | --- |
| modelId | Id of model on the form las:model:&lt;hex&gt; |


| Header name | Header value |
| --- | --- |
| Content-Type | application/json |
| Authorization | Bearer &lt;your access token here&gt; |





##### Request body JSON Schema
```json
{
  "title": "PATCH /models/modelId",
  "minProperties": 1,
  "type": "object",
  "properties": {
    "preprocessConfig": {
      "required": [
        "autoRotate",
        "imageQuality",
        "maxPages"
      ],
      "type": "object",
      "properties": {
        "maxPages": {
          "maximum": 3,
          "minimum": 1,
          "type": "integer"
        },
        "autoRotate": {
          "type": "boolean"
        },
        "imageQuality": {
          "type": "string",
          "enum": [
            "LOW",
            "HIGH"
          ]
        }
      },
      "additionalProperties": false
    },
    "width": {
      "maximum": 1921,
      "minimum": 97,
      "type": "integer"
    },
    "name": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "description": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "fieldConfig": {
      "type": "object",
      "additionalProperties": {
        "required": [
          "maxLength",
          "type"
        ],
        "type": "object",
        "properties": {
          "description": {
            "maxLength": 4096,
            "type": "string",
            "nullable": true
          },
          "type": {
            "type": "string",
            "enum": [
              "date",
              "amount",
              "number",
              "letter",
              "phone",
              "alphanum",
              "alphanumext",
              "all",
              "string",
              "digits"
            ]
          },
          "maxLength": {
            "maximum": 100,
            "minimum": 1,
            "type": "integer"
          }
        }
      }
    },
    "height": {
      "maximum": 1921,
      "minimum": 97,
      "type": "integer"
    },
    "status": {
      "type": "string",
      "enum": [
        "active",
        "training",
        "inactive"
      ]
    }
  },
  "additionalProperties": false
}
```


##### Response body JSON Schema
```json
{
  "title": "model",
  "required": [
    "createdBy",
    "createdTime",
    "description",
    "fieldConfig",
    "height",
    "modelId",
    "name",
    "numberOfDataBundles",
    "preprocessConfig",
    "status",
    "updatedBy",
    "updatedTime",
    "width"
  ],
  "type": "object",
  "properties": {
    "updatedTime": {
      "pattern": "^[0-9]{4}-?[0-9]{2}-?[0-9]{2}( |T)?[0-9]{2}:?[0-9]{2}:?[0-9]{2}(.[0-9]{1,6})?(Z|[+][0-9]{2}(:|)[0-9]{2})$",
      "type": "string",
      "nullable": true
    },
    "updatedBy": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "modelId": {
      "pattern": "^las:model:[a-f0-9]{32}$",
      "type": "string"
    },
    "description": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "fieldConfig": {
      "type": "object",
      "additionalProperties": {
        "required": [
          "maxLength",
          "type"
        ],
        "type": "object",
        "properties": {
          "description": {
            "anyOf": [
              {
                "maxLength": 4096,
                "type": "string"
              },
              null
            ]
          },
          "type": {
            "type": "string",
            "enum": [
              "date",
              "amount",
              "number",
              "letter",
              "phone",
              "alphanum",
              "alphanumext",
              "all",
              "string",
              "digits"
            ]
          },
          "maxLength": {
            "maximum": 100,
            "minimum": 1,
            "type": "integer"
          }
        }
      }
    },
    "preprocessConfig": {
      "required": [
        "autoRotate",
        "imageQuality",
        "maxPages"
      ],
      "type": "object",
      "properties": {
        "maxPages": {
          "maximum": 3,
          "minimum": 1,
          "type": "integer"
        },
        "autoRotate": {
          "type": "boolean"
        },
        "imageQuality": {
          "type": "string",
          "enum": [
            "LOW",
            "HIGH"
          ]
        }
      },
      "additionalProperties": false
    },
    "createdBy": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "name": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "width": {
      "maximum": 1921,
      "minimum": 97,
      "type": "integer"
    },
    "numberOfDataBundles": {
      "minimum": 0,
      "type": "integer"
    },
    "createdTime": {
      "pattern": "^[0-9]{4}-?[0-9]{2}-?[0-9]{2}( |T)?[0-9]{2}:?[0-9]{2}:?[0-9]{2}(.[0-9]{1,6})?(Z|[+][0-9]{2}(:|)[0-9]{2})$",
      "type": "string",
      "nullable": true
    },
    "height": {
      "maximum": 1921,
      "minimum": 97,
      "type": "integer"
    },
    "status": {
      "type": "string",
      "enum": [
        "active",
        "training",
        "inactive"
      ]
    }
  },
  "additionalProperties": false
}
```

