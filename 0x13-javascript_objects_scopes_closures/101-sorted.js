#!/usr/bin/node

// Autor: Said LAMGHARI
// imports a dictionary of occurrences by user id
// computes a dictionary of user ids by Evn.

const { dict } = require('./101-data');

const MyNwDict = {};

for (const UsId in dict) {
  const Evn = dict[UsId];

  if (Evn in MyNwDict) {
    MyNwDict[Evn].push(UsId.toString());
  } else {
    MyNwDict[Evn] = [UsId.toString()];
  }
}

console.log(MyNwDict);
