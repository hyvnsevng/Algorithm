function find(x, parents) {
  if (x !== parents[x]) parents[x] = find(parents[x], parents);
  return parents[x];
}

function union(x, y, parents) {
  const [px, py] = [find(x, parents), find(y, parents)];
  if (px > py) parents[px] = py;
  else parents[py] = px;
  return parents;
}

function cycle(x, y, parents) {
  const [px, py] = [find(x, parents), find(y, parents)];
  if (px > py) parents[py] = 0;
  else parents[px] = 0;
  return parents;
}

const fs = require("fs");
const input = fs.readFileSync(0, "utf8").trim().split("\n");

let idx = 0;
let t = 0;
while (++t) {
  const [n, m] = input[idx++].split(" ").map((e) => Number(e));

  if (n == 0 && m == 0) break;

  let ans = n;
  const parents = Array.from({ length: n + 1 }, (_, _idx) => _idx);

  for (let i = 0; i < m; ++i) {
    const [a, b] = input[idx++].split(" ").map((e) => Number(e));
    const [pa, pb] = [find(a, parents), find(b, parents)];
    if (pa != pb) {
      // 트리에 새 정점 추가
      union(a, b, parents);
      ans--;
    } else if (pa | pb) {
      cycle(a, b, parents);
      ans--;
    } // 이미 같은 트리에 속한 경우 -> 사이클 생성
    // 이미 사이클이 생성된 그래프 내에 간선 추가 -> 변화 없음
  }

  console.log(
    `Case ${t}:`,
    ans > 1
      ? `A forest of ${ans} trees.`
      : ans
        ? "There is one tree."
        : "No trees.",
  );
}
