const fs = require("fs");
const filePath = process.platform == "linux" ? "/dev/stdin" : "input.txt";
const input = fs
  .readFileSync(filePath)
  .toString()
  .trim()
  .split("\n")
  .map((line) => line.split(" ").map((n) => Number(n)));

const [C, N] = input.shift();
const maxNum = Math.max(...input.map((e) => e[1]));
const maxIdx = C + maxNum;

const dp = Array(maxIdx + 1).fill(100000); // idx명 유치 최소 비용

for (const [a, b] of input) {
  dp[b] = Math.min(dp[b], a);
}

for (const [cost, customers] of input) {
  for (let i = customers; i < maxIdx; ++i) {
    dp[i] = Math.min(dp[i], dp[i - customers] + cost);
  }
}

console.log(Math.min(...dp.slice(C)));
