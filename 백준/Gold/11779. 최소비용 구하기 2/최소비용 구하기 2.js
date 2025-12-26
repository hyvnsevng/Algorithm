
function push(x) {
  let i = heap.length;
  heap.push(x);

  while (i > 0) {
    const p = (i - 1) >> 1;
    if (heap[p] <= x) break;
    heap[i] = heap[p];
    i = p;
  }
  heap[i] = x;
}

function pop() {
  const n = heap.length;
  if (n === 0) return undefined;

  const res = heap[0];
  const x = heap.pop();
  if (n === 1) return res;

  const m = heap.length;
  let i = 0;
  const half = m >> 1;

  while (i < half) {
    let l = i * 2 + 1;
    let r = l + 1;
    let c = r < m && heap[r] < heap[l] ? r : l;
    if (heap[c] >= x) break;
    heap[i] = heap[c];
    i = c;
  }
  heap[i] = x;
  return res;
}

const fs = require("fs");
const filePath = process.platform == "linux" ? "/dev/stdin" : "input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

const n = Number(input.shift());
const m = Number(input.shift());
const [start, end] = input
  .pop()
  .split(" ")
  .map((e) => Number(e));

const edges = Array.from({ length: n + 1 }, () => []);
for (const line of input) {
  const [s, e, c] = line.split(" ").map((e) => Number(e));
  edges[s].push([e, c]);
}

const heap = [];
const distance = Array(n + 1).fill(10e9);
const path = Array(n + 1).fill(-1);
heap.push([0, start]);
while (heap.length) {
  const [dist, node] = heap.pop();
  if (distance[node] < dist) continue;
  for (const [nxt, cost] of edges[node]) {
    const w = cost + dist;
    if (w < distance[nxt]) {
      path[nxt] = node;
      heap.push([w, nxt]);
      distance[nxt] = w;
    }
  }
}

const ans = [end];
let node = end;
while (node !== start) {
  node = path[node];
  ans.push(node);
}
console.log(distance[end]);
console.log(ans.length);
console.log(...ans.reverse());
