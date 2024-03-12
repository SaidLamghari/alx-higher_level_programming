#!/usr/bin/node

// Autor: Said LAMGHARI
// a function that returns the number
// of occurrences in a list

exports.nbOccurences = function (list, searchElement) {
  let CntOccu = 0;

  for (let cnt = 0; cnt < list.length; cnt++) {
    if (list[cnt] === searchElement) {
      CntOccu++;
    }
  }

  return CntOccu;
};
