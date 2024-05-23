#!/usr/bin/node
//

const name = process.argv[2];
const baseurl = 'https://swapi-api.alx-tools.com/api/films/';
const url = baseurl + name;
const request = require('request');

request(url, { json: true }, (err, response, body) => {
  if (err) console.error(err);

  for (const i of body.characters) {
    request(i, { json: true }, (err, anodaresponse, anodabody) => {
      if (err) console.error(err);

      console.log(anodabody.name);
    });
  }
});
