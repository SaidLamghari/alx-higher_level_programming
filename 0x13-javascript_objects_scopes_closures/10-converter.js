#!/usr/bin/node

// Autor: Said LAMGHARI
// a function that converts a number
// from base 10 to another base
// passed as argument

exports.converter = function (base) {
  return function (ConvNber) {
    return ConvNber.toString(base);
  };
};
