import { Collection, RequestAuth } from 'postman-collection';
import { convert } from 'openapi-to-postmanv2';
import { readFileSync, writeFileSync } from 'fs';

function setAuth(parent) {
  for (const member of parent.items.members) {
    if (member.items) {
      setAuth(member);
    }
    if (member.request) {
      console.log(`${member.request.method} ${member.request.name}`);
      if (member.request.method == 'OPTIONS') {
        member.request.auth = new RequestAuth({type: 'noauth'});
      } else {
        member.request.auth = new RequestAuth({type: 'inherit'});
      }
    }
  }
}

const oasYaml = readFileSync('../static/oas.yaml', {encoding: 'utf-8'});

convert({type: 'string', data: oasYaml}, {}, (error, conversion) => {
  if (error) {
    console.error(`Error when converting OAS spec to Postman Collection: ${error}`);
  } else if (!conversion.result) {
    console.error(`Error when converting OAS spec to Postman Collection: ${conversion.reason}`);
  } else {
    console.log('Successfully converted.');
    const collection = new Collection(conversion.output[0].data);
    collection.auth = new RequestAuth({
      type: 'oauth2',
      oauth2: [
        {key: 'accessTokenUrl', value: 'https://auth.lucidtech.ai/oauth2/token'},
        {key: 'grant_type', value: 'client_credentials'},
        {key: 'scope', value: ''},
        {key: 'clientId', value: '<YOUR CLIENT ID HERE>'},
        {key: 'clientSecret', value: '<YOUR CLIENT SECRET HERE>'},
      ]
    });
    setAuth(collection);
    writeFileSync('postman_collection.json', JSON.stringify(collection, null, 2));
  }
});
