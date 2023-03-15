#!/usr/bin/node
exports.esrever = function (list) {
  const array = [];
  let elo = 0;
  for (let boss = list.length - 1; boss >= 0; boss--, elo++) {
    array[elo] = array[boss];
  }
  return array[elo];
};
