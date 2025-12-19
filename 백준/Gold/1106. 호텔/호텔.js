const fs = require("fs");
const filePath = process.platform == "linux" ? "/dev/stdin" : "input.txt";
const input = fs
  .readFileSync(filePath)
  .toString()
  .trim()
  .split("\n")
  .map((line) => line.split(" ").map((n) => Number(n)));

const [C, N] = input[0];
const promos = [];
const dp = Array(2001).fill(200000); // idx명 유치 최소 비용

for (let i = 1; i < N + 1; ++i) {
  const [a, b] = input[i]; // [비용, 고객 수]
  promos.push([a, b]);
  dp[b] = Math.min(dp[b], a);
}

for (let i = 1; i < 2001; ++i) {
  for (const [cost, customers] of promos) {
    if (i + customers > 2000) continue;
    dp[i + customers] = Math.min(dp[i + customers], dp[i] + cost);
  }
}

console.log(Math.min(...dp.slice(C)));
