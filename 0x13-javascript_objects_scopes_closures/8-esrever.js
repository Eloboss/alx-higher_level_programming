#!/usr/bin/node
exports.esrever = function (list) {
  const arrayA = [];
  let elo = 0;
  for (let boss = list.length - 1; boss >= 0; boss--, elo++) {
    arrayA[elo] = list[boss];
  }
  return arrayA[elo];
};
