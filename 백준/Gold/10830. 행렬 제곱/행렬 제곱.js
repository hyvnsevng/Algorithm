function solve(matrix, e) {
  if (e == 1) return matrix;
  const root = solve(matrix, Math.floor(e / 2));
  const res = multiple(root, root);
  return e % 2 ? multiple(res, matrix) : res;
}

function multiple(A, B) {
  const n = A.length;
  const res = Array.from({ length: n }, () => Array(n).fill(0));
  for (let i = 0; i < n; ++i) {
    for (let j = 0; j < n; ++j) {
      for (let k = 0; k < n; ++k) {
        res[i][j] += (A[i][k] * B[k][j]) % 1000;
      }
    }
  }
  return res;
}

const fs = require("fs");
const input = fs.readFileSync(0, "utf8").trim().split("\n");

const [N, B] = input
  .shift()
  .split(" ")
  .map((e) => Number(e));

const mat = [];
for (const line of input) {
  const row = line.split(" ").map((e) => Number(e));
  mat.push(row);
}

for (const line of solve(mat, B)) {
  const row = line.map((e) => e % 1000);
  console.log(row.join(" "));
}
