function findKevinBacon(i, edges) {
  let result = 0;
  for (let j = 0; j < n; j++) {
    if (i !== j) {
      const visited = Array(n).fill(false);
      result += bfs(i + 1, j + 1, 0, edges, visited);
    }
  }
  return result;
}

function bfs(member1, member2, cost, edges, visited) {
  const queue = Array();
  queue.push([member1, 0]);
  visited[member1 - 1] = true;

  while (queue.length > 0) {
    const [member, dist] = queue[0];
    queue.shift();
    if (member === member2) {
      return dist;
    }
    edges[member - 1].forEach((friend) => {
      if (visited[friend - 1] === false) {
        queue.push([friend, dist + 1]);
        visited[friend - 1] = true;
      }
    });
  }
}

const fs = require("fs");
const input = fs
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

const [n, m] = input[0].split(" ").map(Number);

const edges = Array.from({ length: n }, () => []);

// 인접 배열
for (let i = 1; i <= m; i++) {
  const [a, b] = input[i].split(" ").map(Number);
  edges[a - 1].push(b);
  edges[b - 1].push(a);
}

let answer = 0;
let minKevinBacon = 10000;

for (let i = 0; i < n; i++) {
  const kevinBacon = findKevinBacon(i, edges);
  if (minKevinBacon > kevinBacon) {
    answer = i + 1;
    minKevinBacon = kevinBacon;
  }
}

console.log(answer);
