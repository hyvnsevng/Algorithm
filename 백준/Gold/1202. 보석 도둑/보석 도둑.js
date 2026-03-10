const fs = require('fs');
const input = fs.readFileSync(0, 'utf-8').toString().trim().split('\n');

class MaxHeap {
  constructor() {
    this.heap = [null];
  }

  push(val) {
    this.heap.push(val);
    let cur = this.heap.length - 1;
    let par = Math.floor(cur / 2);

    while (cur > 1 && this.heap[par] < this.heap[cur]) {
      [this.heap[par], this.heap[cur]] = [this.heap[cur], this.heap[par]];
      cur = par;
      par = Math.floor(cur / 2);
    }
  }

  pop() {
    if (this.heap.length <= 1) return null;
    if (this.heap.length === 2) return this.heap.pop();

    const res = this.heap[1];
    this.heap[1] = this.heap.pop();
    let cur = 1;

    while (true) {
      let left = cur * 2;
      let right = cur * 2 + 1;
      let target = cur;

      if (left < this.heap.length && this.heap[left] > this.heap[target]) target = left;
      if (right < this.heap.length && this.heap[right] > this.heap[target]) target = right;

      if (target === cur) break;
      [this.heap[cur], this.heap[target]] = [this.heap[target], this.heap[cur]];
      cur = target;
    }
    return res;
  }

  size() {
    return this.heap.length - 1;
  }
}

let line = 0;
const [N, K] = input[line++].split(' ').map(Number);

const jewels = [];
for (let i = 0; i < N; i++) {
  jewels.push(input[line++].split(' ').map(Number));
}

const bags = [];
for (let i = 0; i < K; i++) {
  bags.push(Number(input[line++]));
}

jewels.sort((a, b) => a[0] - b[0]);
bags.sort((a, b) => a - b);

const pq = new MaxHeap();
let jewelIdx = 0;
let totalValue = BigInt(0);

for (let i = 0; i < K; i++) {
  const currentBagCapacity = bags[i];

  while (jewelIdx < N && jewels[jewelIdx][0] <= currentBagCapacity) {
    pq.push(jewels[jewelIdx][1]);
    jewelIdx++;
  }

  const bestJewel = pq.pop();
  if (bestJewel !== null) {
    totalValue += BigInt(bestJewel);
  }
}

console.log(totalValue.toString());