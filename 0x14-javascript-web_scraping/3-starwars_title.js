#!/usr/bin/node
const request = require('request');

const id = process.argv[2]; // Get the movie ID from command line arguments

request.get(`https://swapi-api.alx-tools.com/api/films/${id}`, (err, res, body) => {
  if (err) {
    console.error(err);
  } else {
    const jsonBody = JSON.parse(body);
    console.log(jsonBody.title);
  }
});
