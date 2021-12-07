const fs = require('fs');
const path = require('path');

const {getDiveProduct} = require('./getDiveProduct');

describe('test case', () => {
  test('passes test case', () => {
    const input = `forward 5
    down 5
    forward 8
    up 3
    down 8
    forward 2
    `

    expect(getDiveProduct(input)).toBe(150);
  });

  test("what's the real input result?", async () => {
    await fs.readFile(
      path.join(__dirname, 'input1.txt'),
      'utf-8',
      (err, data) => {
        if (err) {
          return console.log(err);
        }

        expect(getDiveProduct(data)).toBe(2091984);
    })
  })
})
