#!/usr/bin/node
// Autor: Said LAMGHARI

const NbreArgs = process.argv.length;

if (NbreArgs === 2) {
 console.log('No argument');
} else if (NbreArgs === 3) {
 console.log('Argument found');
} else {
console.log('Arguments found');
}
