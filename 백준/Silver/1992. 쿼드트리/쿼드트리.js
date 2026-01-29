const fs = require("fs");
const fileName = "input.txt";
const input = fs.readFileSync(0, "utf8").trim().split("\n");

const N = input.shift();
const vid = input;

function makeTree(size, r, c) {
  if (size == 1) return vid[r][c];

  const a1 = makeTree(size / 2, r, c);
  const a2 = makeTree(size / 2, r, c + size / 2);
  const a3 = makeTree(size / 2, r + size / 2, c);
  const a4 = makeTree(size / 2, r + size / 2, c + size / 2);

  if ((a1 == "0" || a1 == "1") && a1 == a2 && a2 == a3 && a3 == a4) return a1;
  return "(" + a1 + a2 + a3 + a4 + ")";
}

console.log(makeTree(N, 0, 0));
