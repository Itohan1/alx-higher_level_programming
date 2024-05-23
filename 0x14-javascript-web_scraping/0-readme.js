#!/usr/bin/node
// Write a script that reads and prints the content of a file

const fs = require('fs');
const name = process.argv[2];

fs.readFile(name, 'utf8', (err) => {
  if (err) console.error(err);
});
