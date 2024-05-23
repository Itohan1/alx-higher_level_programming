#!/usr/bin/node
//

const request = require('request');
const fs = require('fs');
const name = process.argv[2];

request(name, (err, response, body) => {
  if (err) console.error(err);

  fs.writeFile('loripsum', body, (err) => {
    if (err) console.error(err);
  });
});
