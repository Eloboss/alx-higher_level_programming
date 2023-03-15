#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  for (const elo in list) {
    if (list[elo] === searchElement) {
      count++;
    }
  }
  return count;
};
