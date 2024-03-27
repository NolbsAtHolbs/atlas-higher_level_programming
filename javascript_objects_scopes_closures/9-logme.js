#!/usr/bin/node
let argsCount = 0;
exports.logMe = function (item) {
  argsCount++;
  console.log(argsCount - 1 + ': ' + item);
};
