const fs = require("fs");
const input = fs.readFileSync(0, "utf8").trim().split("\n");

const MAX = Math.pow(2, 31) - 1;
const N = Number(input.shift());
const matrix = input.map((matrix) =>
  matrix.split(" ").map((num) => Number(num)),
);
const dp = Array.from({ length: N }, () => Array(N).fill(0)); // dp[i][j]: i~j번째 행렬 곱연산 최소 횟수

for (let gap = 1; gap < N; ++gap) {
  for (let start = 0; start + gap < N; ++start) {
    let val = MAX;
    for (let b = 0; b < gap; b++) {
      val = Math.min(
        val,
        dp[start][start + b] +
          dp[start + b + 1][start + gap] +
          matrix[start][0] * matrix[start + b][1] * matrix[start + gap][1],
      );
    }
    dp[start][start + gap] = val;
  }
}

console.log(dp[0][N - 1]);