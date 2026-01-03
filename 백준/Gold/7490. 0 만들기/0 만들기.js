const fs = require("fs");
const input = fs.readFileSync(0, "utf8").trim().split("\n");
let idx = 0;
const T = Number(input[idx++]);

let out = [];

function dfs(n, next, sum, last, exprParts) {
  if (next > n) {
    if (sum + last === 0) out.push(exprParts.join(""));
    return;
  }

  // 공백: last에 next를 이어붙이기
  const joined = last >= 0 ? last * 10 + next : last * 10 - next;
  exprParts.push(" " + next);
  dfs(n, next + 1, sum, joined, exprParts);
  exprParts.pop();

  // +
  exprParts.push("+" + next);
  dfs(n, next + 1, sum + last, +next, exprParts);
  exprParts.pop();

  // -
  exprParts.push("-" + next);
  dfs(n, next + 1, sum + last, -next, exprParts);
  exprParts.pop();
}

for (let tc = 0; tc < T; tc++) {
  const n = Number(input[idx++]);
  dfs(n, 2, 0, 1, ["1"]);
  out.push("");
}

process.stdout.write(out.join("\n"));
