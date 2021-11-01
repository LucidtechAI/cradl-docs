#### POST /signup





| Header name | Header value |
| --- | --- |
| Content-Type | application/json |
| Authorization | Bearer &lt;your access token here&gt; |





##### Request body JSON Schema
```json
{
  "title": "POST /users",
  "required": [
    "email",
    "password",
    "reCaptchaResponse"
  ],
  "type": "object",
  "properties": {
    "password": {
      "pattern": "^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[\\^$*.\\[\\]{}\\(\\)?\\-\"!@#%&/,><':;|_~`])\\S{8,99}$",
      "type": "string"
    },
    "reCaptchaResponse": {
      "type": "string"
    },
    "name": {
      "maxLength": 4096,
      "type": "string",
      "nullable": true
    },
    "email": {
      "pattern": "^[A-Za-z0-9][-+._A-Za-z0-9]*@([-_.A-Za-z0-9]+\\.)+[A-Za-z]{2,}$",
      "type": "string"
    }
  },
  "additionalProperties": false
}
```


##### Response body JSON Schema
```json
{
  "title": "signup",
  "required": [
    "clientId",
    "username"
  ],
  "type": "object",
  "properties": {
    "clientId": {
      "type": "string"
    },
    "username": {
      "pattern": "^[A-Za-z0-9][-+._A-Za-z0-9]*@([-_.A-Za-z0-9]+\\.)+[A-Za-z]{2,}$",
      "type": "string"
    }
  },
  "additionalProperties": false
}
```

