const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "boj_1566.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n")
  .map(line => line.split(" ").map(Number));

const [n, m] = input[0];
const A = input.slice(1);

// sign 함수: >0이면 1, <0이면 -1, 0이면 0
const sign = (x) => (x > 0 ? 1 : x < 0 ? -1 : 0);

let best = n + m + 1;          // 답(최소 뒤집기 수), 초기 큰 값
const c = new Array(m).fill(1); // 열 부호
const rowSum = new Array(n).fill(0); // 현재까지 배정된 열로 만든 행 합 누적

function dfs(col) {
  if (col === m) {
    // 모든 열 부호가 정해졌으면 행 부호 r 결정
    const r = new Array(n);
    for (let i = 0; i < n; i++) {
      const sg = sign(rowSum[i]);
      if (sg === 0) return;    // 행 합이 0이면 실패
      r[i] = sg;
    }
    // 열 고정점 검증: sign(sum_i r_i * a[i][j]) === c[j]
    for (let j = 0; j < m; j++) {
      let s = 0;
      for (let i = 0; i < n; i++) s += r[i] * A[i][j];
      const sg = sign(s);
      if (sg === 0 || sg !== c[j]) return;
    }
    // 뒤집기 수 계산
    let flips = 0;
    for (let i = 0; i < n; i++) if (r[i] < 0) flips++;
    for (let j = 0; j < m; j++) if (c[j] < 0) flips++;
    if (flips < best) best = flips;
    return;
  }

  // 가지 1: c[col] = +1
  c[col] = 1;
  for (let i = 0; i < n; i++) rowSum[i] += A[i][col];
  dfs(col + 1);
  for (let i = 0; i < n; i++) rowSum[i] -= A[i][col];

  // 가지 2: c[col] = -1
  c[col] = -1;
  for (let i = 0; i < n; i++) rowSum[i] -= A[i][col];
  dfs(col + 1);
  for (let i = 0; i < n; i++) rowSum[i] += A[i][col];
}

dfs(0);
console.log(best === n + m + 1 ? -1 : best);
