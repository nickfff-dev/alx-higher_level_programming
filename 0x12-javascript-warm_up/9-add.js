#!/usr/bin/node
// script that prints sum of argvs

function add (a, b) {
  return a + b;
}

console.log(add(Number(process.argv[2]), Number(process.argv[3])));
