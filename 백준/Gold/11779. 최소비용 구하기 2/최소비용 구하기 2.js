function push(elem) {
  heap.push(elem);
  let idx = heap.length - 1;
  let parentIdx = Math.floor((idx - 1) / 2);
  while (heap[parentIdx] > heap[idx]) {
    [heap[parentIdx], heap[idx]] = [heap[idx], heap[parentIdx]];
    idx = parentIdx;
    parentIdx = Math.floor((idx - 1) / 2);
  }
}

function pop() {
  if (heap.length == 1) {
    return heap.pop();
  }
  const res = heap[0];
  heap[0] = heap.pop();
  let idx = 0,
    leftIdx = idx * 2 + 1,
    rightIdx = idx * 2 + 2,
    childIdx;
  while (heap[leftIdx] && heap[leftIdx] < heap[idx]) {
    childIdx = leftIdx; // 왼쪽 자식 노드가 더 작다고 가정
    if (heap[rightIdx] && heap[childIdx] < heap[rightIdx]) {
      childIdx = rightIdx;
    }
    [heap[childIdx], heap[idx]] = [heap[idx], heap[childIdx]];
    idx = childIdx;
    leftIdx = idx * 2 + 1;
    rightIdx = idx * 2 + 1;
  }
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
