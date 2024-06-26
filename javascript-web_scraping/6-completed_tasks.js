#!/usr/bin/node
const request = require('request');
const { argv } = require('node:process');

request(argv[2], function (err, response, body) {
  if (err) {
    console.error(err);
  }
  const users = {};
  for (const task of JSON.parse(body)) {
    if (task.userId && task.completed) {
      if (users[task.userId]) {
        users[task.userId]++;
      } else {
        users[task.userId] = 1;
      }
    }
  }
  console.log(users);
});
