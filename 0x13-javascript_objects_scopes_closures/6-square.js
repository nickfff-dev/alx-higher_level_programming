#!/usr/bin/node
/**
 * Square class that inherits from previous its parent square
 */
const ParentSquare = require('./5-square');

class Square extends ParentSquare {
  charPrint (c) {
    const j = c === undefined ? 'X' : c;
    for (let i = 0; i < this.height; i++) {
      let x = '';
      let y = 0;
      while (y < this.width) {
        x += j;
        y++;
      }

      console.log(x);
    }
  }
}

module.exports = Square;
