class Heap {
  constructor() {
    this.heap = [];
  }

  size() {
    return this.heap.length;
  }

  push(elem) {
    this.heap.push(elem);
    this._bubbleUp();
  }

  pop() {
    if (this.size() == 1) {
      return this.heap.pop();
    }
    const res = this.heap[0];
    this.heap[0] = this.heap.pop();
    this._bubbleDown();
    return res;
  }

  _swap(idx1, idx2) {
    [this.heap[idx1], this.heap[idx2]] = [this.heap[idx2], this.heap[idx1]];
  }

  _bubbleUp() {
    let idx = this.size() - 1;
    let parentIdx = Math.floor((idx - 1) / 2);
    while (this.heap[parentIdx] > this.heap[idx]) {
      this._swap(parentIdx, idx);
      idx = parentIdx;
      parentIdx = Math.floor((idx - 1) / 2);
    }
  }

  _bubbleDown() {
    let idx = 0,
      leftIdx = idx * 2 + 1,
      rightIdx = idx * 2 + 2,
      childIdx;
    while (this.heap[leftIdx] && this.heap[leftIdx] < this.heap[idx]) {
      childIdx = leftIdx; // 왼쪽 자식 노드가 더 작다고 가정
      if (this.heap[rightIdx] && this.heap[childIdx] < this.heap[rightIdx]) {
        childIdx = rightIdx;
      }
      this._swap(childIdx, idx);
      idx = childIdx;
      leftIdx = idx * 2 + 1;
      rightIdx = idx * 2 + 1;
    }
  }
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

const heap = new Heap();
const distance = Array(n + 1).fill(10e9);
const path = Array(n + 1).fill(-1);
heap.push([0, start]);
while (heap.size()) {
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
