#!/usr/bin/node
// Autor: Said LAMGHARI

exports.addMeMaybe = function (number, theFunction) {
  number = number + 1;

  theFunction(number);
};
