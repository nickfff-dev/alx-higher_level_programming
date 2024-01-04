#!/usr/bin/node
const request = require('request');
const fs = require('fs');

const url = process.argv[2]; // Get the URL from command line arguments
const filePath = process.argv[3]; // Get the file path from command line arguments

request.get(url, (err, res, body) => {
  if (err) {
    console.error(err);
  } else {
    fs.writeFile(filePath, body, 'utf-8', (err) => {
      if (err) {
        console.error(err);
      }
    });
  }
});
