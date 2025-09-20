const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "boj_1759.txt";
const input = fs.readFileSync(filePath).toString().split("\n");
const [L, C] = input[0].split(" ").map((e) => Number(e));
const letters = input[1].split(" ").sort();

queue = [...letters];

while (queue.length) {
  const code = queue.shift();
  if (code.length === L && condition(code)) console.log(code);
  for (
    let i = letters.findIndex((e) => e === code[code.length - 1]) + 1;
    i < C;
    i++
  ) {
    queue.push(code + letters[i]);
  }
}

function condition(code) {
  let nc = 0,
    nv = 0;
  for (const letter of code) {
    if ("aeiou".includes(letter)) nv++;
    else nc++;
  }
  if (nv >= 1 && nc >= 2) return true;
  return false;
}
