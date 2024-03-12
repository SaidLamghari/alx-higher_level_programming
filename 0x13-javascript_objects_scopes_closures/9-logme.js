#!/usr/bin/node

// Autor: Said LAMGHARI
// a function that prints
// the number of arguments already printed
// and the new argument value.

let countLog = 0;

exports.logMe = function (item) {
  console.log(countLog + ': ' + item);

  countLog++;
};
