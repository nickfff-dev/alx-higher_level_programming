#!/usr/bin/node
// script that prints argvs
const myArr = process.argv;
if (myArr.length < 3) {
  console.log('No Argument');
} else if (myArr.length === 3) {
  console.log('Argument Found');
} else {
  console.log('Arguments Found');
}
