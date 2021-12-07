// split input by line
// split line into "direction" and "magnitude"
// two axes: horizontal position & depth
// should be able to reduce series of vectors into a single sum for each axis
// should be able to multiply the result

const formatInput = (input) => 
  input
  .trim()
  .split('\n')
  .map(cmd => cmd
    .trim()
    .split(' ')
  );

function getDiveProduct(input) {
  const commandsArray = input.trim().split('\n')
    .map(cmd => cmd.trim().split(' '));

  const axes = commandsArray.reduce((acc, [dir, mag]) => {
    const sign = dir === 'up' ? -1 : 1; // only decreases on 'up'
    const index = dir === 'forward' ? 0 : 1; // 'forward' only horizontal command
    acc[index] += parseInt(mag) * sign;
    return acc;
  }, [0, 0])

  return axes[0] * axes[1];
}

module.exports = { getDiveProduct, formatInput };