#!/usr/bin/node

exports.esrever = function (list) {
  const reversedlist = [];

  for (let i = list.length; i >= 0; i--) {
    if (list[i] === undefined) {
    }
    reversedlist.push(list[i]);
  }
  return (reversedlist);
};
