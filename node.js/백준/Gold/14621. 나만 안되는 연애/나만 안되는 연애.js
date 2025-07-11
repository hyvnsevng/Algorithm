const fs = require("fs");
const input = fs
  .readFileSync("/dev/stdin")
  .toString()
  .split("\n");

let idx = 0;

const [n, m] = input[idx++].split(" ").map(Number);;
const genders = input[idx++].split(" ");

const parents = Array.from({ length: n }, (_, index) => index);

const routes = [];
for (idx; idx < input.length; idx++) {
  routes.push(input[idx].split(" ").map((c) => Number(c)));
}
routes.sort((a, b) => a[2] - b[2]);

function union(a, b) {
  const [rootA, rootB] = [find(a), find(b)];
  if (rootA !== rootB) {
    parents[rootB] = rootA;
  }
}

function find(x) {
  let parent = parents[x];
  while (parents[parent] !== parent) {
    parent = parents[parent];
  }
  return parent;
}

let answer = 0,
  cnt = 0;

for (const path of routes) {
  const [u, v, d] = path;

  if (genders[u - 1] !== genders[v - 1] && find(u - 1) !== find(v - 1)) {
    union(u - 1, v - 1);
    answer += d;
    cnt++;
  }
}

console.log(cnt === n - 1 ? answer : -1);
