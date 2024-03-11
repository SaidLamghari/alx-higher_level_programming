#!/usr/bin/node
// Autor: Said LAMGHARI

const ValArg = process.argv[2];

const CnvNum = parseInt(ValArg);

if (Number.isInteger(CnvNum)) {
  console.log(`My number: ${CnvNum}`);
} else {
  console.log('Not a number');
}
