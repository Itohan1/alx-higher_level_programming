#!/usr/bin/node
// Write a script that display the status code of a GET request

const request = require('request');

const name = process.argv[2];

request(name, (error, response) => {
  if (error) console.log(error);

  console.log('code:', response.statusCode);
});
