#!/usr/bin/node

const { argv } = require('node:process');
const value = parseInt(argv[2]);

if (isNaN(value)) {
  console.log('Missing number of occurrences');
}

for (let i = 0; i < value; i++) {
  console.log('C is fun');
}
