#!/usr/bin/node
const fs = require('fs');

const filePath = process.argv[2]; // Get the file path from command line arguments
const strToWrite = process.argv[3]; // Get the string to write from command line arguments
if (!strToWrite) {
  console.error('No string given');
  process.exit(1);
}
fs.writeFile(filePath, strToWrite, 'utf-8', (err) => {
  if (err) {
    console.error(err);
  }
});
