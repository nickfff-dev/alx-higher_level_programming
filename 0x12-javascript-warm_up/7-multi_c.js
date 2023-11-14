#!/usr/bin/node
// script that prints argvs
if (process.argv[2]) {
  if ((!Number(process.argv[2])) && Number(process.argv[2]) !== 0) {
    console.log('Missing number of occurrences');
  } else {
    if (Number(process.argv[2])) {
      Array.from({ length: Number(process.argv[2]) }, (_, i) => i)
        .forEach(item => console.log('C is fun'));
    }
  }
} else {
  console.log('Missing number of occurrences');
}
