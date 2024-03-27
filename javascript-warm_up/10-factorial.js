#!/usr/bin/node
const { argv } = require('node:process');
function fact (int) {
  if (Number(int) === 0 || Number(int) === 1 || isNaN(Number(int))) {
    return 1;
  } else {
    return (int * fact(int - 1));
  }
}
console.log(fact(argv[2]));
