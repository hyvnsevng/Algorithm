const fs = require("fs");
const input = fs.readFileSync(0, "utf8").trim().split("\n");

const n = Number(input[0]);
const boxes = input[1].split(" ").map((e) => Number(e));
const dp = Array(n).fill(0);

for (let i = 0; i < n; ++i) {
  const size = boxes[i];
  let tmp = 0;
  for (let j = i - 1; j >= 0; --j) {
    if (boxes[j] < size && dp[j] > tmp) {
      tmp = dp[j];
    }
  }
  dp[i] = tmp + 1;
}

console.log(Math.max(...dp));
