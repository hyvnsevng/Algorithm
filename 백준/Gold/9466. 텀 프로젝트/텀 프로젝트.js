const fs = require("fs");
const input = fs.readFileSync(0, "utf8").trim().split("\n");

main(input);

function main(input) {
  let idx = 0;
  let T = Number(input[idx++]);
  while (T--) {
    const n = Number(input[idx++]);
    const students = [0].concat(input[idx++].split(" ").map((e) => Number(e)));
    const indegree = Array(n + 1).fill(0);
    for (let i = 1; i < n + 1; ++i) {
      indegree[students[i]]++;
    }
    const queue = new Int32Array(n);
    let head = 0,
      tail = 0;

    for (let i = 1; i < n + 1; ++i) {
      if (indegree[i] == 0) queue[tail++] = i;
    }

    let ans = 0;
    while (head < tail) {
      const node = queue[head++];
      ans++;
      const want = students[node];
      if (--indegree[want] == 0) queue[tail++] = want;
    }
    console.log(ans);
  }
}
