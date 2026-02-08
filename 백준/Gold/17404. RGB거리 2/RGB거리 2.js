const fs = require("fs");
const input = fs.readFileSync(0, "utf8").trim().split("\n");

const MAX = 1000001;

let idx = 0;
const n = Number(input.shift());
const costs = input.map((line) => line.split(" ").map((e) => Number(e)));
const dp = Array.from({ length: n - 1 }, () =>
  Array.from({ length: 3 }, () => Array(3).fill(MAX)),
);

for (let c = 0; c < 3; ++c) {
  dp[0][c][c] = costs[0][c];
}

// i번째 집
for (let i = 1; i < n - 1; ++i) {
  // 시작 색
  for (let c = 0; c < 3; ++c) {
    // 마지막 색
    for (let lc = 0; lc < 3; ++lc) {
      dp[i][c][lc] =
        Math.min(dp[i - 1][c][(lc + 1) % 3], dp[i - 1][c][(lc + 2) % 3]) +
        costs[i][lc];
    }
  }
}
let ans = MAX;
// N번째 색
for (let i = 0; i < 3; ++i) {
  // 첫번째 색
  for (let j = 0; j < 3; ++j) {
    if (i == j) continue;
    ans = Math.min(
      ans,
      dp[n - 2][j][(i + 1) % 3] + costs[n - 1][i],
      dp[n - 2][j][(i + 2) % 3] + costs[n - 1][i],
    );
  }
}

console.log(ans);
