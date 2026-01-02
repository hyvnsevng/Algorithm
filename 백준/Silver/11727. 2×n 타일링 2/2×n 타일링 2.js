const fs = require("fs");
const filePath = process.platform == "linux" ? "/dev/stdin" : "input.txt";
const N = Number(fs.readFileSync(filePath).toString());

function solve(N) {
  if (N == 1) return 1;
  const ans = [1, 3];
  for (let i = 2; i < N; ++i) {
    const last = ans[1];
    ans[1] = (ans[0] * 2 + ans[1]) % 10007;
    ans[0] = last;
  }
  return ans[1];
}

console.log(solve(N));
