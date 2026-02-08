const fs = require("fs");
const input = fs.readFileSync(0, "utf8").trim().split("\n");

main(input);

function solve(n, edges) {
  const visited = Array(n + 1).fill(0);
  let ans = 0;
  for (let i = 1; i < n + 1; ++i) {
    if (!visited[i]) {
      ans += dfs(i, edges, visited);
    }
  }
  return n - ans;
}

function dfs(curr, edges, visited) {
  if (visited[curr] == 1) {
    let node = curr,
      res = 1;
    while (edges[node] != curr) {
      res++;
      node = edges[node];
    }
    return res;
  }
  if (visited[curr] == 2) {
    return 0;
  }
  visited[curr] = 1;
  const res = dfs(edges[curr], edges, visited);
  visited[curr] = 2;
  return res;
}

function main(input) {
  let idx = 0;
  let T = Number(input[idx++]);
  while (T--) {
    const n = Number(input[idx++]);
    const students = [0].concat(input[idx++].split(" ").map((e) => Number(e)));
    console.log(solve(n, students));
  }
}
