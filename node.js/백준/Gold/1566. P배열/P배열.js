const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "boj_1566.txt";
const input = fs
  .readFileSync(filePath)
  .toString()
  .trim()
  .split("\n")
  .map((line) => line.split(" ").map(Number));

const [n, m] = input[0];
const A = input.slice(1);

const sign = (x) => (x > 0 ? 1 : x < 0 ? -1 : 0);

let best = n + m + 1; // sentinel

for (let mask = 0; mask < 1 << m; mask++) {
  // c_j from mask
  const c = Array(m);
  for (let j = 0; j < m; j++) c[j] = mask & (1 << j) ? -1 : 1;

  // r_i = sign(A * c)
  const r = Array(n);
  let ok = true;
  for (let i = 0; i < n; i++) {
    let s = 0;
    for (let j = 0; j < m; j++) s += A[i][j] * c[j];
    const sg = sign(s);
    if (sg === 0) {
      ok = false;
      break;
    }
    r[i] = sg; // this ensures each row sum > 0
  }
  if (!ok) continue;

  // Check fixed point on columns: c must be sign(A^T * r)
  for (let j = 0; j < m && ok; j++) {
    let t = 0;
    for (let i = 0; i < n; i++) t += A[i][j] * r[i];
    const sg = sign(t);
    if (sg === 0 || sg !== c[j]) ok = false;
  }
  if (!ok) continue;

  // Count flips
  let flips = 0;
  for (let i = 0; i < n; i++) if (r[i] < 0) flips++;
  for (let j = 0; j < m; j++) if (c[j] < 0) flips++;
  if (flips < best) best = flips;
}

console.log(best === n + m + 1 ? -1 : best);
