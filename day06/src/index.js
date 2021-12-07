// lanternfish
// reproduce after 7 days
// or 9 days if first cycle
import input from "./input";

const testInput = [3, 4, 3, 1, 2];

const getDaysArray = (input) =>
  input.reduce((acc, f) => {
    const arr = [...acc]
    arr[f]++;
    console.log(f)
    console.log(arr)
    return arr;
  }, initialArray);

const incrementDay = (arr) => {
  const newArr = [...arr];
  let tmp = 0n;
  for (let i = 0; i < 9; i++) {
    if (i === 0) {
      tmp = newArr[0];
    } else {
      newArr[i - 1] = newArr[i];
      newArr[i] = 0n;
    }
  }
  newArr[6] += tmp;
  newArr[8] = tmp;
  return newArr;
};

const incrementDays = (fish, days) => {
  let newFish = [...fish];
  for (let i = 0; i < days; i++) {
    newFish = incrementDay(newFish);
  }
  return newFish;
};

const array = getDaysArray(input);
const nextDay = incrementDays(array, 256);

const countFish = (arr) => arr.reduce((acc, n) => acc + n);
console.log("" + countFish(nextDay));

export { testInput, getDaysArray, incrementDay, countFish };
