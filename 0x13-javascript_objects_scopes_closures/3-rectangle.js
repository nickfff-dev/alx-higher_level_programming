#!/usr/bin/node
/**
 * Defines a rectangle checks types
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
}
module.exports = Rectangle;
