const fs = require("fs");
const input = fs.readFileSync(0, "utf-8").toString().trim().split("\n");

function checkByInterval(arr, interval) {
  let cnt = 1,
    loc = arr[0];
  for (let i = 1; i < arr.length; ++i) {
    if (arr[i] - loc >= interval) {
      cnt++;
      loc = arr[i];
    }
  }
  return cnt;
}

const [N, C] = input[0].split(" ").map((e) => Number(e));
const arr = input
  .slice(1)
  .map((e) => Number(e))
  .sort((a, b) => a - b);

let [l, r] = [1, arr[N - 1] - arr[0]];
while (l < r) {
  const m = (l + r + 1) >> 1;
  const cnt = checkByInterval(arr, m);
  if (cnt >= C) l = m;
  else r = m - 1;
}

console.log(l);
