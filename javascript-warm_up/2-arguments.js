#!/usr/bin/node
const argsPassed = process.argv.length - 2;

if (argsPassed === 0)
  { console.log('No argument'); }
else if (argsPassed === 1)
  { console.log('Argument found'); }
else
  { console.log('Arguments found'); }
