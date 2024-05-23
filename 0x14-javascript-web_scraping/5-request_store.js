#!/usr/bin/node
// Write a script that gets the contents of a webpage and stores it in a file

const request = require('request');
const fs = require('fs');
const name = process.argv[2];

request(name, (err, response, body) => {
  if (err) console.error(err);

  fs.writeFile('loripsum', body, (err) => {
    if (err) console.error(err);
  });
});
