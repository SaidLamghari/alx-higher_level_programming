#!/usr/bin/node
// Autor: Said LAMGHARI

let cnt;

const ValArg = process.argv[2];

const ValNum = parseInt(ValArg);

if (Number.isNaN(ValNum)) {
  console.log('Missing number of occurrences');
} else if (ValNum <= 0) {
  // is negative or zero occurrences
} else {
  for (cnt = 0; cnt < ValNum; cnt++) {
    console.log('C is fun');
  }
}
