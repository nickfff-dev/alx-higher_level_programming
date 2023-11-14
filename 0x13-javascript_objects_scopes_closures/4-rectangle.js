#!/usr/bin/node
/**
 * function to check class attributes
 */
class Rectangle {
  constructor (w, h) {
    if (typeof w === 'number' && w > 0 && typeof h === 'number' && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let x = 0; x < this.height; x++) {
      let m = '';
      let y = 0;
      while (y < this.width) {
        m += 'X';
        y++;
      }

      console.log(m);
    }
  }

  rotate () {
    let dim = 0;
    dim = this.width;
    this.width = this.height;
    this.height = dim;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}
module.exports = Rectangle;
