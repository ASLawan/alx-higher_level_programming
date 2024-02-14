#!/usr/bin/node
const occurrences = require('./101-data').occurrences;

const usersByOccurrence = {};

Object.keys(occurrences).map(function (key, index) {
  if (usersByOccurrence[occurrences[key]] === undefined) {
    usersByOccurrence[occurrences[key]] = [];
  }
  usersByOccurrence[occurrences[key]].push(key);
});

console.log(usersByOccurrence);
