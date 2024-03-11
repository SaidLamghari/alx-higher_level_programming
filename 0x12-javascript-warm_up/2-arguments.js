#!/usr/bin/node
// Autor: Said LAMGHARI

const NbreArgs = process.argv;

if (NbreArgs.length === 2) {
  console.log('No argument');
} else if (NbreArgs.length === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
