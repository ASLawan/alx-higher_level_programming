#!/usr/bin/node

exports.esrever = function (list) {
  const len = list.length - 1;
  const newList = [];

  if (!list || !Array.isArray(list)) {
    return [];
  }
  for (let i = len; i >= 0; i--) {
    newList.push(list[i]);
  }
  return newList;
};
