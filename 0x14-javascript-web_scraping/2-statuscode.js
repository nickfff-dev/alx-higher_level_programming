#!/usr/bin/node
const request = require('request');

let url = process.argv[2]; // Get the URL from command line arguments

request.get(url, (err, res) => {
 if (err) {
 console.error(err);
 } else {
 console.log(`code: ${res.statusCode}`);
 }
});
