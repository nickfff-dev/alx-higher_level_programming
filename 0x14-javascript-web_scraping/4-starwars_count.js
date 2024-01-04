#!/usr/bin/node
const request = require('request');

let apiUrl = process.argv[2]; // Get the API URL from command line arguments
let wedgeId = 18; // Wedge Antilles character ID
let count = 0;

request.get(apiUrl, (err, res, body) => {
 if (err) {
 console.error(err);
 } else {
 let films = JSON.parse(body).results;
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
