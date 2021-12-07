const part2 = require("./part2");
const fs = require('fs');
const path = require('path');

describe('part 2...', () => {
  test('passes given test case', () => {
    const input = `forward 5
    down 5
    forward 8
    up 3
    down 8
    forward 2
    `;

    expect(part2(input)).toEqual(900)
  });

  test("what's the real input result?", async () => {
    const data = fs.readFileSync(path.join(__dirname, 'input1.txt'), 'utf-8')

    expect(part2(data)).toEqual(2086261056);
  })
})
