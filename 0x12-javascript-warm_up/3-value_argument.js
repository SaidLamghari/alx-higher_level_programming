#!/usr/bin/node
// Autor: Said LAMGHARI

const ValArgs = process.argv[2];

if (ValArgs === undefined) {
  console.log('No argument');
} else {
  console.log(ValArgs);
}
