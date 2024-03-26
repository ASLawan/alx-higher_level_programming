#!/usr/bin/node

const request = require('request');

if (process.argv.length < 3) {
  console.log('Usage: ./script.js <movieId>');
  process.exit(1);
}

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request.get(apiUrl, (err, response, body) => {
  if (err) {
    console.error(err);
    process.exit(1);
  }
  const movieData = JSON.parse(body);

  if (movieData.detail !== 'Not found') {
    movieData.characters.forEach(characterUrl => {
      request.get(characterUrl, (err, response, body) => {
        if (err) {
          console.error(err);
          process.exit(1);
        }

        const characterData = JSON.parse(body);
        console.log(characterData.name);
      });
    });
  }
});
