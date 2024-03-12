#!/usr/bin/node

// Autor: Said LAMGHARI
// a function that returns the number
// of occurrences in a list

exports.nbOccurences = function (list, searchElement) {
  let cntoc = 0;

    for (let cnt = 0; cnt < list.length; cnt++) {
      if (list[i] === searchElement) {
        cntoc++;
      }
    }

  return cntoc;

};
