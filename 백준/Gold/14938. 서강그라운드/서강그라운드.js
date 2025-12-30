const fs = require("fs");
const filePath = process.platform == "linux" ? "/dev/stdin" : "input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
const INF = 10000;

const [n, m, r] = input
  .shift()
  .split(" ")
  .map((e) => Number(e));
const T = input
  .shift()
  .split(" ")
  .map((e) => Number(e));

edges = Array.from({ length: n + 1 }, () => []);
const FW = Array.from({ length: n + 1 }, (_, r) =>
  Array.from({ length: n + 1 }, (_, c) => (r == c ? 0 : INF))
);

for (let i = 0; i < r; ++i) {
  const [a, b, l] = input[i].split(" ").map((e) => Number(e));
  if (FW[a][b] > l) {
    FW[a][b] = l;
    FW[b][a] = l;
  }
}

for (let k = 1; k < n + 1; ++k) {
  for (let i = 1; i < n + 1; ++i) {
    for (let j = 1; j < n + 1; ++j)
      FW[i][j] = Math.min(FW[i][j], FW[i][k] + FW[k][j]);
  }
}

let ans = 0;
for (let i = 1; i < n + 1; ++i) {
  let tmp = 0;
  for (let j = 1; j < n + 1; ++j) tmp += FW[i][j] > m ? 0 : T[j - 1];
  if (tmp > ans) ans = tmp;
}

console.log(ans);
