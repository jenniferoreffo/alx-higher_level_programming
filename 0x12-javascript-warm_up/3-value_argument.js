#!/usr/bin/node

//A script tha prints first arguement passed

console.log(typeof process.argv[2] === 'undefined' ? 'No Argument' : process.argv[2]);
