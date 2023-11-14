#!/usr/bin/node
// script that prints argvs

console.log(
  process.argv[2]
    ? !Number(process.argv[2])
        ? 'Not a number'
        : 'My number: ' + process.argv[2]
    : 'Not a number');
