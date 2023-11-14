#!/usr/bin/node
// script that prints argvs

if ((!Number(process.argv[2])) && Number(process.argv[2]) !== 0) {
  console.log('Missing size');
} else {
  if (Number(process.argv[2])) {
    const mynum = Number(process.argv[2]);
    for (let i = 0; i < mynum; i++) {
      let mystr = '';
      for (let x = 0; x < mynum; x++) {
        mystr += 'X';
      }
      console.log(mystr);
    }
  }
}
