#!/usr/bin/node

exports.esrever = function (list) {
  const reversedlist = [];

  for (let i in list) {
    if (list[i] === undefined) {
    }
    reversedlist.push(list[i]);
  }
  return (reversedlist);
};
