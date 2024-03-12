#!/usr/bin/node

// Autor: Said LAMGHARI
// a function that return
// the reversed version of a list

exports.esrever = function (list) {
  const rvrsdList = [];

  for (let cnt = 0; cnt < list.length; cnt++) {
    rvrsdList.unshift(list[cnt]);
  }

  return rvrsdList;
};
