#!/usr/bin/node
// script that calculates factorial recursively

function factorial (mynum) {
  if (mynum < 2) {
    return 1;
  }
  return mynum * factorial(mynum - 1);
}

if (Number(process.argv[2])) {
  console.log(factorial(Number(process.argv[2])));
} else {
  console.log(1);
}
