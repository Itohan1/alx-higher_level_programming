#!/usr/bin/node

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      super.print();
      c = 'X';
    } else {
      for (let i = 0; i < this.width; i++) {
        let row = '';
        for (let j = 0; j < this.height; j++) {
          row += 'C';
        }
        console.log(row);
      }
    }
  }
}

module.exports = Square;
