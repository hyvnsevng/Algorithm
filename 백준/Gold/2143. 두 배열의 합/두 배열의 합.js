const fs = require("fs");
const input = fs.readFileSync(0, "utf-8").toString().trim().split("\n");

let idx = 0;
const T = Number(input[idx++]);
const n = Number(input[idx++]);
const A = input[idx++].split(" ").map((e) => Number(e));
const m = Number(input[idx++]);
const B = input[idx++].split(" ").map((e) => Number(e));

function accSum(arr, l) {
  const res = [0];
  let s = 0;
  for (let i = 0; i < l; ++i) {
    s += arr[i];
    res.push(s);
  }
  return res;
}

function accSumCnt(sumArr, l) {
  const res = new Map();
  for (let subs = 0; subs < l; ++subs) {
    for (let add = subs + 1; add < l + 1; ++add) {
      const calc = sumArr[add] - sumArr[subs];
      const cnt = res.get(calc);
      res.set(calc, cnt ? cnt + 1 : 1);
    }
  }
  return res;
}

const sA = accSum(A, n);
const sB = accSum(B, m);

const cA = accSumCnt(sA, n);
const cB = accSumCnt(sB, m);

const scA = [...cA.keys()];

let ans = 0;

for (const sumA of scA) {
  const req = T - sumA;
  const b = cB.get(req);
  if (b) ans += b * cA.get(sumA);
}

console.log(ans);
