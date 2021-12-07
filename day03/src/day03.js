// bin
// gamma rate, epsilon rate
// pwr = g * e
// g = most common bit in each place, for each
// e = least common bit
// eg parseInt('0101', 2)

const { testInput } = require("./day3input");

function getCommon(arr) {
  return sum(arr) > arr.length / 2 ? 1 : 0;
}

function flip(b) {
  return b === 1 ? 0 : 1;
}

function sum(arr) {
  return arr.reduce((acc, n) => acc + parseInt(n), 0);
}

function getCol(input, index) {
  return input.reduce((acc, n) => [...acc, n[index]], []);
}

function getGamma(input) {
  let gamma = '';
  for (let i = 0; i < input[0].length; i++) {
    gamma += getCommon(getCol(input, i));
  }
  return parseInt(gamma, 2);
}

function getE(input) {
  let e = '';
  for (let i = 0; i < input[0].length; i++) {
    e += flip(getCommon(getCol(input, i)));
  }
  return parseInt(e, 2);
}

function getPwr(rawInput) {
  // array of strings
  const input = rawInput.trim().split('\n').map(str => str.trim())
  return getGamma(input) * getE(input);
}

getPwr(testInput)

module.exports = {getPwr, getCommon, sum, getCol, flip };