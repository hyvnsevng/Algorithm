const fs = require("fs");
const filePath = process.platform == "linux" ? "/dev/stdin" : "input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

const N = Number(input[0]);
const dp = Array(N + 1).fill(10 ** 9);
dp[N] = 0;
for (let X = N; X > 0; X--) {
  let val = dp[X];
  dp[X - 1] = Math.min(dp[X - 1], val + 1);
  if (X % 3 == 0) dp[X / 3] = Math.min(dp[X / 3], val + 1);
  if (X % 2 == 0) dp[X / 2] = Math.min(dp[X / 2], val + 1);
}
console.log(dp[1]);
