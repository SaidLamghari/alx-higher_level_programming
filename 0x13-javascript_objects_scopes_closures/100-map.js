#!/usr/bin/node

// Autor: Said LAMGHARI
// imports an array
// computes a new array.

const { list } = require('./100-data');

const MyNewList = list.map((EleValue, indxEle) => EleValue * indxEle);

console.log(list);

console.log(MyNewList);
