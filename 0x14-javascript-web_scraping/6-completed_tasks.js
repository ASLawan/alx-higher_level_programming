#!/usr/bin/node

const request = require('request');

if (process.argv.length < 3) {
  console.log('Usage: ./script.js <api_url>');
  process.exit(1);
}

const apiUrl = process.argv[2];

request.get(apiUrl, (err, response, body) => {
  if (err) {
    console.error(err);
    process.exit(1);
  }

  const todosData = JSON.parse(body);

  const completedTasks = {};
  todosData.forEach(todo => {
    if (todo.completed) {
      if (!completedTasks[todo.userId]) {
        completedTasks[todo.userId] = 0;
      }
      completedTasks[todo.userId]++;
    }
  });
    console.log(completedTasks);
});
