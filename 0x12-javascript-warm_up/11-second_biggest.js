#!/usr/bin/node
// Autor: Said LAMGHARI

const ValsArgs = process.argv.slice(2);

const Valintgrs = ValsArgs.map(ValArg => parseInt(ValArg));

if (Valintgrs.length <= 1) {
  console.log(0);
} else {
  const secondBig = Valintgrs.sort((a, b) => b - a);

  console.log(secondBig[1]);
}
