#!/usr/bin/node

const request = require('request');

if (process.argv.length < 3) {
  console.log('Usage: ./script <url>');
  process.exit(1);
}

const url = process.argv[2];

request.get(url, (err, response) => {
  if (err) {
    console.error(err);
    process.exit(1);
  }
  console.log(`code: ${response.statusCode}`);
});
