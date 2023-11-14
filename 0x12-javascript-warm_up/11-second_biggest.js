#!/usr/bin/node
// script that calculates factorial recursively

if (process.argv.slice(2).length && process.argv.slice(2).length > 1) {
  console.log(process.argv.slice(2).sort((a, b) => b - a)[1]);
} else {
  console.log(0);
}
