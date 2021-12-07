const {getPwr} = require("./day03")
const { getLifeSupportRating } = require("./day03-2")
const { testInput, input } = require("./day3input")

test('testinput', () => {
  expect(getPwr(testInput)).toBe(198)
})

test('input', () => {
  expect(getPwr(input)).toBe(3429254);
})

test('life support testInput', () => {
  expect(getLifeSupportRating(testInput)).toBe(230);
})

test('life support real input', () => {
  expect(getLifeSupportRating(input)).toBe(5410338);
})
