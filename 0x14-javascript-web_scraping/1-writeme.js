#!/usr/bin/node
// Write a script that writes a string to a file

const name = process.argv[2];

const fs = require('fs');

fs.writeFile('my_file.txt', name, err => {
  if (err) throw err;
});
