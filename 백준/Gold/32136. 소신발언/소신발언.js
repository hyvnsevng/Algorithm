const fs = require("fs");
const input = fs.readFileSync(0, "utf-8").toString().trim().split("\n");

const N = Number(input[0]);
const arr = input[1].split(" ").map((e) => Number(e));

function check(arr, t) {
  const N = arr.length;
  let [mini, maxi] = [0n, BigInt(N - 1)];
  for (let j = 0; j < N; ++j) {
    const tmini = -1n * (t / BigInt(arr[j])) + BigInt(j);
    const tmaxi = t / BigInt(arr[j]) + BigInt(j);
    mini = mini < tmini ? tmini : mini;
    maxi = maxi > tmaxi ? tmaxi : maxi;
    if (mini > maxi) return false;
  }
  return true;
}

let maxA = 0;
for (let i = 0; i < N; ++i) {
  maxA = Math.max(maxA, (N - 1 - i) * arr[i], i * arr[i]);
}

let [l, r] = [1n, BigInt(maxA)];
while (l < r) {
  const m = (l + r) >> 1n;
  if (check(arr, m)) r = m;
  else l = m + 1n;
}

console.log(String(l));
