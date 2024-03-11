#!/usr/bin/node
// Autor: Said LAMGHARI

const ValArg = process.argv[2];

let cnt;

const sz = parseInt(ValArg);

if (Number.isNaN(sz)) {
  console.log('Missing size');
} else if (sz <= 0) {
// is negative or size = zero
} else {
  for (cnt = 0; cnt < sz; cnt++) {
    console.log('X'.repeat(sz));
  }
}
