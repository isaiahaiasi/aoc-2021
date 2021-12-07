const { formatInput } = require("./getDiveProduct");

// down(x) => aim += x
// up(x) => aim -= x;
// forward(x) => hor += x; depth += aim * x

function part2(input) {
  const cmdArray = formatInput(input);
  
  const resultArray = cmdArray.reduce((acc, [dir, mag]) => {
    let [hor, depth, aim] = acc;

    const inputCmds = {
      down: (x) => aim += x,
      up: (x) => aim -= x,
      forward: (x) => {
        hor += x;
        depth += aim * x;
      }
    }

    inputCmds[dir](parseInt(mag));

    return [hor, depth, aim];
  }, [0, 0, 0])

  return resultArray[0] * resultArray[1];
}

module.exports = part2;