#!/usr/bin/node

//A script that converts number

const num  = Math.floor(Number(process.argv[2]));
console.log(isNaN(num) ? 'Not a number' : 'My number : ${num}');
