#!/usr/bin/node
const fs = require('fs');

let filePath = process.argv[2]; // Get the file path from command line arguments

fs.readFile(filePath, 'utf-8', (err, data) => {
 if (err) {
   console.error(err);
 } else {
   console.log(data);
 }
});
