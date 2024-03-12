#!/usr/bin/node

// Autor: Said LAMGHARI
// class Rectangle that defines a rectangle

let cnt1;
let cnt2;

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (cnt1 = 0; cnt1 < this.height; cnt1++) {
      let wh = '';
      for (cnt2 = 0; cnt2 < this.width; cnt2++) {
        wh += 'X';
      }
      console.log(wh);
    }
  }
}
