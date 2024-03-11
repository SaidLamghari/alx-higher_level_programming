#!/usr/bin/node
// Autor: Said LAMGHARI

function add (a, b) {
  return a + b;
}

const ValArg1 = process.argv[2];

const ValArg2 = process.argv[3];

const ValA = parseInt(ValArg1);

const ValB = parseInt(ValArg2);

console.log(add(ValA, ValB));
