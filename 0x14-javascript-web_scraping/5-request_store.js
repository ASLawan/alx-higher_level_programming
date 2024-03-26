#!/usr/bin/node

const fs = require('fs');
const request = require('request');

if (process.argv.length < 4) {
  console.log('Usage: ./script.js <url> <filename>');
  process.exit(1);
}

const url = process.argv[2];
const filename = process.argv[3];

request.get(url, { encoding: 'utf-8' }, (err, response, body) => {
  if (err) {
    console.error(err);
    process.exit(1);
  }

  fs.writeFile(filename, body, 'utf-8', (err) => {
    if (err) {
      console.error(err);
      process.exit(1);
    }

    console.log(`${filename}`);
  });
});
