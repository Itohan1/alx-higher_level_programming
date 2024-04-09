#!/usr/bin/node

const { argv } = require('node:process');
const firstValue = Number(argv[2]);
const secondValue = Number(argv[3]);

function add (a, b) {
  console.log(a + b);
}
add(firstValue, secondValue);
