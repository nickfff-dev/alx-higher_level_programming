#!/usr/bin/node
const request = require('request');

let movieId = process.argv[2]; // Get the movie ID from command line arguments

request.get(`https://swapi-api.alx-tools.com/api/films/${movieId}`, (err, res, body) => {
 if (err) {
  console.error(err);
 } else {
  let jsonBody = JSON.parse(body);
  jsonBody.characters.forEach((characterUrl) => {
    request.get(characterUrl, (err, res, body) => {
      if (err) {
        console.error(err);
      } else {
        let characterJson = JSON.parse(body);
        console.log(characterJson.name);
      }
    });
  });
 }
});
