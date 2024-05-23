#!/usr/bin/node
// Write a script that computes the number of tasks completed by user id

const name = process.argv[2];
const request = require('request');

request(name, { json: true }, (err, response, body) => {
  if (err) console.error(err);

  const newtodo = {};
  for (const i of body) {
    if (i.completed === true) {
      if (newtodo[i.userId] === undefined) {
        newtodo[i.userId] = 0;
      }
      newtodo[i.userId] += 1;
    }
  }
  console.log(newtodo);
});
