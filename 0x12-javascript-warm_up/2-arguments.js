#!/usr/bin/node
// script that prints argvs

if (!process.argv[2]) {
  console.log('No Argument');
} else if (process.argv[2]) {
  if (!process.argv[3]) {
    console.log('Argument Found');
  } else {
    console.log('Arguments Found');
  }
}
