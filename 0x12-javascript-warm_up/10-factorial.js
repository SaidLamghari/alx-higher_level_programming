#!/usr/bin/node
// Autor: Said LAMGHARI

function factorial (fn) {
  if (isNaN(fn)) {
    return 1;
  } else if (fn === 0) {
    return 1;
  } else {
    return fn * factorial(fn - 1);
  }
}

const ValArg = process.argv[2];

const ValF = parseInt(ValArg);

console.log(factorial(ValF));
