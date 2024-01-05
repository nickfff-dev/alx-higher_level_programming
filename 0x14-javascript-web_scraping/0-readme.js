#!/usr/bin/node
const fs = require('fs');

const filePath = process.argv[2]; // Get the file path from command line arguments

if (!filePath) {
  console.error('No path given');
  process.exit(1);
}
fs.readFile(filePath, 'utf-8', (err, data) => {
  if (err) {
    console.error(err);
  } else {
    console.log(data);
  }
});
