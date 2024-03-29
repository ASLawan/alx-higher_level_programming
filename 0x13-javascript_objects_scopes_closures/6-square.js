#!/usr/bin/node
const SSquare = require('./5-square');

class Square extends SSquare {
  charPrint (C) {
    if (C === undefined) {
      C = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      console.log(C.repeat(this.width));
    }
  }
}

module.exports = Square;
