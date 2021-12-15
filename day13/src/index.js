const {input} = require('./input.js');

class Sheet {
  constructor(dots) {
    this.dots = dots;
  }

  foldSheet(fold) {
    const dots = {}; // assigning to new obj ensures new keys are unique
    Object.values(this.dots).forEach((dot) => {
      dot.move(fold);
      dots[`${dot.x},${dot.y}`] = dot;
    });
    this.dots = dots;
  }

  render() {
    const dotValues = Object.values(this.dots);
    const width = dotValues.reduce((x, dot) => (dot.x > x ? dot.x : x), 0) + 1;
    const height = dotValues.reduce((y, dot) => (dot.y > y ? dot.y : y), 0) + 1;

    let lines = "";
    for (let y = 0; y < height; y++) {
      let line = "";
      for (let x = 0; x < width; x++) {
        if (this.dots[x + "," + y]) {
          line += "#";
        } else {
          line += " ";
        }
      }
      lines += line + "\n";
    }

    return lines;
  }
}

class Dot {
  constructor(x, y) {
    this.x = Number(x);
    this.y = Number(y);
  }

  move(fold) {
    if (this[fold.axis] > fold.at) {
      const newPos = fold.at - Math.abs(fold.at - this[fold.axis]);
      this[fold.axis] = newPos;
    }
  }
}

class Fold {
  constructor(axis, at) {
    this.axis = axis;
    this.at = at;
  }
}

function getSheet(dotsInput) {
  const dots = {};

  dotsInput.split("\n").forEach((dot) => {
    dots[dot] = new Dot(...dot.split(","));
  });

  return new Sheet(dots);
}

function getFolds(foldsInput) {
  return foldsInput.split("\n").map((line) => {
    const [axisStr, atStr] = line.split("=");
    return new Fold(axisStr[axisStr.length - 1], Number(atStr));
  });
}

function parseInput(input) {
  const [dotStr, foldStr] = input.trim().split("\n\n");
  return [getSheet(dotStr), getFolds(foldStr)];
}

const [sheet, folds] = parseInput(input);

folds.forEach((fold) => {
  sheet.foldSheet(fold);
});

console.log(sheet.render());
