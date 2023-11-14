#!/usr/bin/node

exports.converter = function (radix) {
  return function (n) {
    return n.toString(radix);
  };
};
