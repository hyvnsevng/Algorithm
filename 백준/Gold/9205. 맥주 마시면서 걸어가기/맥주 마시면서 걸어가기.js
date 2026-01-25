const fs = require("fs");
const fileName = "input.txt";
const input = fs.readFileSync(0, "utf8").trim().split("\n");

let idx = 0;
let t = Number(input[idx++]);
while (t--) {
  const n = Number(input[idx++]);
  const nodes = [];
  for (let i = 0; i < n + 2; ++i) {
    nodes.push(input[idx++].split(" ").map((e) => Number(e)));
  }
  const [hx, hy] = nodes[0];
  const [px, py] = nodes[n + 1];
  const parents = Array.from({ length: n + 2 }, (_, idx) => idx);

  const queue = [0];

  function union(x, y) {
    const x1 = find(x);
    const y1 = find(y);
    if (x1 > y1) parents[x1] = y;
    else parents[y1] = x;
  }

  function find(x) {
    while (x != parents[x]) {
      x = parents[x];
    }
    return x;
  }

  while (queue.length) {
    const idx = queue.pop();
    for (let i = 0; i < n + 2; ++i) {
      if (
        find(i) != find(idx) &&
        Math.abs(nodes[i][0] - nodes[idx][0]) +
          Math.abs(nodes[i][1] - nodes[idx][1]) <=
          1000
      ) {
        union(i, idx);
        queue.push(i);
      }
    }
  }
  console.log(find(n + 1) ? "sad" : "happy");
}
