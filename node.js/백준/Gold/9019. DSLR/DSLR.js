const fs = require("fs");
const input = fs
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

let idx = 0;
const T = Number(input[idx++]);

for (idx; idx < T + 1; idx++) {
  const [a, b] = input[idx]
    .trim()
    .split(" ")
    .map((e) => Number(e));

  const from = Array(10000).fill(-1),
    how = Array(10000).fill("");

  const q = [a];
  from[a] = a;

  while (q.length) {
    const num = q.shift();

    if (num === b) break;

    for (const [next, cmd] of [
      [D(num), "D"],
      [S(num), "S"],
      [L(num), "L"],
      [R(num), "R"],
    ]) {
      if (from[next] === -1) {
        from[next] = num;
        how[next] = how[num] + cmd;
        q.push(next);
      }
    }
  }
  console.log(how[b]);
}

function D(n) {
  return (n * 2) % 10000;
}

function S(n) {
  return n === 0 ? 9999 : (n - 1) % 10000;
}

function L(n) {
  return (n % 1000) * 10 + Math.floor(n / 1000);
}

function R(n) {
  return (n % 10) * 1000 + Math.floor(n / 10);
}
