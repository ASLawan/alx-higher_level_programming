#!/usr/bin/node

const fs = require('fs');

if (process.argv.length < 4) {
  console.log('Usage: ./script.js <filename> <string to write>');
  process.exit(1);
}

const filepath = process.argv[2];
const content = process.argv[3];

fs.writeFile(filepath, content, 'utf-8', (err) => {
  if (err) {
    console.error(err);
  }
});
