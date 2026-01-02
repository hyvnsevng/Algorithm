const fs = require("fs");
const input = fs.readFileSync(0, "utf8").trim().split("\n");

const N = Number(input[0]);
const A = input[1].split(" ").map((e) => Number(e));
const B = input[2].split(" ");
const M = Number(input[3]);
const C = input[4].split(" ").map((e) => Number(e));
const Q = [];

for (let i = 0; i < N; ++i) {
  if (A[i] == 0) Q.push(Number(B[i]));
}

Q.reverse();
const ans = [];
let head = 0;
for (let i = 0; i < M; ++i) {
  if (head == Q.length) {
    ans.push(C[i]);
  } else {
    Q.push(C[i]);
    ans.push(Q[head]);
    head++;
  }
}

console.log(...ans);
