#!/usr/bin/node
// script that prints argvs

if (process.argv.length < 3) {
  console.log('No Argument');
} else if (process.argv.length > 2) {
  if (process.argv.length === 3) {
    console.log('Argument Found');
  } else {
    console.log('Arguments Found');
  }
}
