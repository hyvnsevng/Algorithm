const fs = require("fs");
const filePath = process.platform == "linux" ? "/dev/stdin" : "input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

const [N, M] = input
  .shift()
  .split(" ")
  .map((e) => Number(e));

const indegree = Array(N + 1).fill(0);
const edges = Array.from({ length: N + 1 }, () => []);
for (const line of input) {
  const [A, B] = line.split(" ").map((e) => Number(e));
  edges[A].push(B);
  indegree[B]++;
}

const queue = [];
for (let i = 1; i < N + 1; i++) {
  if (indegree[i] == 0) queue.push(i);
}

const answer = [];
while (queue.length) {
  const node = queue.shift();
  answer.push(node);
  for (const nxt of edges[node]) {
    indegree[nxt]--;
    if (indegree[nxt] == 0) {
      queue.push(nxt);
    }
  }
}

console.log(...answer);
