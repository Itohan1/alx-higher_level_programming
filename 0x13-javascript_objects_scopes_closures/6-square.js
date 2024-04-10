#!/usr/bin/node

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    super.print();
    if (c === undefined) {
      c = 'X';
    } else {
      for (let i = 0; i < this.height; i++) {
        let row = '';
        for (let j = 0; j < this.width; j++) {
          row += 'C';
        }
        console.log(row);
      }
    }
  }
}

module.exports = Square;
