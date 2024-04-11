#!/usr/bin/node

const oldArray = require('./100-data').list;

const newArray = oldArray.map((x, i) => (x * i));

console.log(oldArray);
console.log(newArray);
