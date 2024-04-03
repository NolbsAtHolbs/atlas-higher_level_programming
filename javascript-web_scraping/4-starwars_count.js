#!/usr/bin/node
const { argv } = require('node:process');
const request = require('request');
let wedges = 0;

request(argv[2], (err, res, body) => {
  if (err) {
    console.error(err);
  } else {
    const data = JSON.parse(body);
    for (const film of data.results) {
      for (const character of film.characters) {
        const tokens = character.split('/');
        if (tokens[5] === '18') {
          wedges++;
        }
      }
    }
    console.log(wedges);
  }
});
