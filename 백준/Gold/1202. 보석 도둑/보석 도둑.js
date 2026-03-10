const fs = require('fs')
const input = fs.readFileSync(0, 'utf-8').toString().trim().split('\n')

class Heap {
  constructor(func = (a, b) => a-b) {
    this.heap = [null]
    this.func = func
  }

  size() {
    return this.heap.length - 1
  }
  
  push(v) {
    this.heap.push(v)
    this._bottomUp()
  }

  pop() {
    if (this.size() == 0) return null
    const res = this.heap[1];
    [this.heap[1], this.heap[this.size()]] = [this.heap[this.size()], this.heap[1]]
    this.heap.pop()
    this._topDown()
    return res
  }

  _topDown() {
    let parent = 1
    const size = this.size()
    while (1) {
      const leftChild = parent * 2, rightChild = parent * 2 + 1
      let candidate = parent
      
      if (leftChild <= size && this.func(this.heap[leftChild], this.heap[candidate]) > 0) {
        candidate = leftChild
      }
      if (rightChild <= size && this.func(this.heap[rightChild], this.heap[candidate]) > 0) {
        candidate = rightChild
      }

      if (candidate == parent) break
      [this.heap[candidate], this.heap[parent]] = [this.heap[parent], this.heap[candidate]]
      parent = candidate
    }
  }

  _bottomUp() {
    let child = this.size()
    while (child > 1) {
      const parent = Math.floor(child / 2)
      if (this.func(this.heap[child], this.heap[parent]) > 0) [this.heap[parent], this.heap[child]] = [this.heap[child], this.heap[parent]]
      child = parent
    }
  }
}

let idx = 0
const [N, K] = input[idx++].split(' ').map(e => Number(e))
const jewels = [];
for (let i = 0; i < N; i++) {
  jewels.push(input[idx++].split(' ').map(Number));
}

const bags = [];
for (let i = 0; i < K; i++) {
  bags.push(Number(input[idx++]));
}

jewels.sort((a, b) => a[0] - b[0]);
bags.sort((a, b) => a - b);

const pq = new Heap();
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