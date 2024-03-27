#!/usr/bin/node

if (isNaN(parseInt(process.argv[2]))) {
  console.log('Missing size');
} else {
  for (let i = 0; i < parseInt(process.argv[2]); i++) {
    let row = '';
    for (let j = 0; j < parseInt(process.argv[2]); j++) {
      row = row + 'X';
    }
    console.log(row);
  }
}
