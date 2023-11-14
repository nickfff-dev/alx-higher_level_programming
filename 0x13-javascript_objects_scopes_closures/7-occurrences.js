#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let instances = 0;

  for (let k = 0; k < list.length; k++) {
    instances = (list[k] === searchElement ? instances + 1 : instances);
  }

  return instances;
};
