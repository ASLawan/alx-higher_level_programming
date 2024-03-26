#!/usr/bin/node

const request = require('request');

if (process.argv.length < 3) {
  console.log('Usage: ./script <api_url>');
  process.exit(1);
}

const apiUrl = process.argv[2];

request.get(apiUrl, (err, response, body) => {
  if (err) {
    console.error(err);
    process.exit(1);
  }

  const moviesData = JSON.parse(body);

  const wedgeMovies = moviesData.results.filter(movie =>
    movie.characters.some(character => character.endsWith('/18/'))
  );

  console.log(`${wedgeMovies.length}`);
});
