#!/usr/bin/node
// Write a script that prints the title of a Star Wars

const request = require('request');

const url = process.argv[2];

request(url, { json: true }, (error, response, body) => {
  if (error) console.log(error);
  const vare = body.results;

  const elementKey = vare.find(element => typeof element === 'object' && 'characters' in element);
  if (elementKey) {
    for (const i of elementKey.characters) {
      const words = i.split('e/');
      if (words[1] === '18/') {
        const moreWords = 'e/';
        const newWords = words[0].concat(moreWords, words[1]);
        request(newWords, { json: true }, (error, anodaResponse, anodabody) => {
          if (error) console.log(error);
          console.log(anodabody.films.length);
        });
      }
    }
  }
});
