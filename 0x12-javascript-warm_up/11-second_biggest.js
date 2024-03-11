#!/usr/bin/node

/* eslint-disable semi */
/* eslint-disable comma-dangle */

const args = process.argv.slice(2).map(Number);

if (args.length === 0 || args.length === 1) {
  console.log(0);
} else {
  const sortedArgs = args.sort((a, b) => b - a);
  console.log(sortedArgs[1]);
}
