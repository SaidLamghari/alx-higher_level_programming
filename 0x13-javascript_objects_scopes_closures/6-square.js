#!/usr/bin/node

// Autor: Said LAMGHARI
// class Square that defines a square and inherits
// from Square of 5-square.js

const SquareBase = require('./5-square');

class Square extends SquareBase {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    const Slne = c.repeat(this.width);
    for (let cnt = 0; cnt < this.height; cnt++) {
      console.log(Slne);
    }
  }
}

module.exports = Square;
