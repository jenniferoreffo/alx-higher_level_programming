#!/usr/bin/node

//A script that prints x times of a command
const x = Math.floor(Number(process.atgv[2]);
if (isNaN(x)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
}
