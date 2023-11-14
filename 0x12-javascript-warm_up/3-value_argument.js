#!/usr/bin/node
// script that prints argvs

if (!process.argv[2]) {
  console.log('No Argument');
} else {
  console.log(process.argv[2]);
}
