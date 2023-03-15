#!/usr/bin/node
const list = require('./100-data').list;
console.log(list);
const elo = list.map((boss, index) => boss * index);
console.log(elo);
