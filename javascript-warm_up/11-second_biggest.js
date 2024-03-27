#!/usr/bin/node
const args = process.argv.slice(2);

if (args.length === 0 || args.length === 1) {
  console.log(0);
} else {
  const nums = args.map(arg => parseInt(arg, 10));
  const sortedNums = nums.sort((a, b) => b - a);
  console.log(sortedNums[1]);
}
