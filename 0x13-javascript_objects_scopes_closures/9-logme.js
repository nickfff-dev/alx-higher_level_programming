#!/usr/bin/node
// function that logs count
let count = 0;

exports.logMe = function (elem) {
  console.log(`${count}: ${elem}`);
  count += 1;
};
