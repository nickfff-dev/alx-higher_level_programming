#!/usr/bin/node
const request = require('request');

const apiUrl = process.argv[2]; // Get the API URL from command line arguments
let count = 0;

request.get(apiUrl, (err, res, body) => {
  if (err) {
    console.error(err);
  } else {
    const films = JSON.parse(body).results;
    films.forEach((film) => {
      request.get(film.characters[0], (err, res, body) => {
        if (!err && JSON.parse(body).name === 'Wedge Antilles') {
          count++;
        }
      });
    });
    setTimeout(() => {
      console.log(count);
    }, 5000);
  }
});
