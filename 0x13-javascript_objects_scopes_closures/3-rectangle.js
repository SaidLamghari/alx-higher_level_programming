#!/usr/bin/node

// Autor: Said LAMGHARI
// class Rectangle that defines a rectangle

let cnt;

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    } else {
      Object.create(null);
    }
  }

  print () {
    for (cnt = 0; cnt < this.height; cnt++) {
      console.log('X'.repeat(this.width));
    }
  }
}
