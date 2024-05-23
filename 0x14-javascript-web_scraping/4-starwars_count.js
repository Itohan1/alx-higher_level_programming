#!/usr/bin/node
// Write a script that prints the title of a Star Wars

const request = require('request');

const url = process.argv[2];

request(url, { json: true }, (error, response, body) => {
  if (error) console.log(error);
  const vare = body.results;

  let count = 0;
  for (const i of vare) {
    if (i.characters) {
      for (const j of i.characters) {
        const words = j.split('e/');
        if (words[1] === '18/') {
          count++;
        }
      }
    }
  }
  console.log(count);
});
