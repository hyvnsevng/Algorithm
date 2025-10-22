const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "boj_1285.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

const n = Number(input[0]);
const rows = new Array(n);

// "H"/"T" → 비트열(예: T=1, H=0)
for (let r = 1; r <= n; r++) {
  let bits = 0;
  const line = input[r];
  for (let c = 0; c < n; c++) {
    if (line[c] === 'T') bits |= (1 << c);
  }
  rows[r - 1] = bits;
}

function popcount(x) {
  // Kernighan’s algorithm
  let cnt = 0;
  while (x) { x &= (x - 1); cnt++; }
  return cnt;
}

let answer = n * n;
for (let colMask = 0; colMask < (1 << n); colMask++) {
  let sum = 0;
  for (let r = 0; r < n; r++) {
    const flipped = rows[r] ^ colMask;
    const ones = popcount(flipped);
    sum += Math.min(ones, n - ones);
    if (sum >= answer) break; // 가지치기
  }
  if (sum < answer) answer = sum;
}

console.log(answer);
