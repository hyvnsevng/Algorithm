const fs = require("fs");
const input = fs.readFileSync(0, "utf-8").toString().trim().split("\n");

const N = Number(input[0]);
const arr = input[1].split(" ").map((e) => Number(e));

function check(t) {
  let [lo, hi] = [0, N - 1];
  for (let j = 0; j < N; ++j) {
    const d = Math.floor(t / arr[j]);
    const tl = j - d;
    const th = j + d;
    lo = lo < tl ? tl : lo;
    hi = hi > th ? th : hi;
    if (lo > hi) return false;
  }
  return true;
}

const maxA = Math.max(...arr);

let [l, r] = [-1, maxA * (N - 1)];
while (l < r) {
  const m = Math.floor((l + r) / 2);
  if (check(m)) r = m;
  else l = m + 1;
}

console.log(l);
