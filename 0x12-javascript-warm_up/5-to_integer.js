#!/usr/bin/node

const process = require('process');

const convertInt = parseInt(process.argv[2]);

if (convertInt === undefined) {
  console.log('Not a number');
} else if (!convertInt) {
  console.log('Not a number');
} else {
  console.log(`My number: ${convertInt}`);
}
