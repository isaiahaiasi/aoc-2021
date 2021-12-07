// lsr = ogr * csr
// filter by:
// only first bit

const { sum, flip, getCol } = require("./day03");

const getMostCommon = (arr) => (sum(arr) >= arr.length / 2 ) ? 1 : 0;

const getLeastCommon = (arr) => flip(getMostCommon(arr));

// input = array of strings
function getRating(input, commonalityFn) {
  // for each column:
  //  - find mostcommon
  //  - filter input by

  let filteredInput = input;

  for (let i = 0; i < input.length; i++) {
    const col = getCol(filteredInput, i);
    const cmn = commonalityFn(col);
    filteredInput = filteredInput.filter(num => num[i] == cmn);

    if (filteredInput.length === 1) break;
  }

  return parseInt(filteredInput[0], 2);
}

const getOxyRating = (input) => getRating(input, getMostCommon);
const getCO2Rating = (input) => getRating(input, getLeastCommon);

const getLifeSupportRating = (rawInput) => {
  const input = cleanInput(rawInput);
  return getOxyRating(input) * getCO2Rating(input);
}

function cleanInput(rawInput) {
  return rawInput.trim().split('\n').map(str => str.trim());
}

module.exports = { getLifeSupportRating }