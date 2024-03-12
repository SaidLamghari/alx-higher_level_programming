#!/usr/bin/node
// Autor: Said LAMGHARI

exports.callMeMoby = function (x, theFunction) {
  if (x > 0) {
    theFunction();

    exports.callMeMoby(x - 1, theFunction);
  }
};
