const smallInput = `11111
19991
19191
19991
11111`;

const testInput = `5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526`;

const input = `3113284886
2851876144
2774664484
6715112578
7146272153
6256656367
3148666245
3857446528
7322422833
8152175168`;

const getCleanInput = (strInput) =>
  strInput
    .trim()
    .replace(/\n/g, "")
    .split("")
    .map((i) => +i);

class OctopusCavern {
  constructor(initialInput, width) {
    this.cavern = initialInput;
    this.width = width;
    this.flashes = 0;
    this.stepCount = 0;
    this.didSync = false;
  }

  step() {
    this.stepCount++;
    this.cavern = this.cavern.map((oct) => oct + 1);
    while (this.cavern.some((oct) => oct > 9)) {
      this.cavern.forEach((oct, i) => {
        if (oct > 9) {
          this.flash(i);
          this.cavern[i] = -1; // this indicates "flashed" state
        }
      });
    }
    this.cavern = this.cavern.map((oct) => (oct === -1 ? 0 : oct));
    if (this.cavern.every((n) => n === 0)) {
      console.log("syncflash", this.stepCount);
      this.didSync = true;
    }
  }

  // get all octs adjacent to i in cavern
  // only increase if >= 0
  flash(i) {
    this.flashes++;
    this.getAdjacent(i).forEach((pos) => {
      if (this.cavern[pos] >= 0) {
        this.cavern[pos] = this.cavern[pos] + 1;
      }
    });
  }

  // get all "adjacent" indices (without "wrapping" out-of-bounds)
  getAdjacent(i) {
    const adj = [];
    for (let x = -1; x <= 1; x++) {
      for (let y = -1; y <= 1; y++) {
        if (!(x === 0 && y === 0)) {
          adj.push(this.getRelativePos(i, [x, y]));
        }
      }
    }
    //console.log(i, adj);
    return adj.filter((pos) => pos !== null);
  }

  getRelativePos(i, [x, y]) {
    const newX = (i % this.width) + x;
    const newY = Number.parseInt(i / this.width, 10) + y;

    if (newX >= this.width || newX < 0 || newY >= this.width || newY < 0) {
      return null;
    } else {
      return i + x + y * this.width;
    }
  }

  render() {
    let out = [];
    for (let i = 0; i < this.width; i++) {
      const start = i * this.width;
      out.push(this.cavern.slice(start, start + this.width));
      out.push("\n");
    }
    return out.join("");
  }
}

const cavern = new OctopusCavern(getCleanInput(input), 10);

const doSteps = (cavern, maxSteps) => {
  for (let i = 0; i < maxSteps; i++) {
    cavern.step();
    if (cavern.didSync) {
      break;
    }
  }
  console.log(cavern.render());
  console.log(cavern.flashes);
};

doSteps(cavern, 601);
