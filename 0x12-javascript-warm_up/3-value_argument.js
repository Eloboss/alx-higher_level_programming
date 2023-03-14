#!/usr/bin/node
/*
  process.argv[0] contains the absolute path to the node binary file
  process.argv[1] contains the absolute file path to the .js file in
  which the js engine runs.
  so process.argv[2] ... contains users passed in arguments.
*/

const value = process.argv[2];
if (value === undefined) {
  console.log('No argument');
} else {
  console.log(value);
}
