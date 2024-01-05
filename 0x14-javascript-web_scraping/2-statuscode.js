#!/usr/bin/node
const request = require('request');

const url = process.argv[2]; // Get the URL from command line arguments

if (!url) {
  console.error('No URL given');
  process.exit(1);
}
request.get(url, (err, res) => {
  if (err) {
    console.error(err);
  } else {
    console.log(`code: ${res.statusCode}`);
  }
});
