#!/usr/bin/node
const request = require('request');

const url = process.argv[2]; // Get the URL from command line arguments

request.get(url, (err, res, body) => {
  if (err) {
    console.error(err);
  } else {
    const todos = JSON.parse(body);
    const completedTasks = {};

    todos.forEach((todo) => {
      if (!completedTasks[todo.userId]) {
        completedTasks[todo.userId] = 0;
      }

      if (todo.completed) {
        completedTasks[todo.userId]++;
      }
    });

    console.log(completedTasks);
  }
});
