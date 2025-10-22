const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "boj_1285.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

const n = Number(input[0]);
const coins = input.slice(1).map((e) => e.split(""));
const status = ["H", "T"];

let answer = n ** 2;

for (let colMask = 0; colMask < 1 << n; ++colMask) {
  // 열 뒤집는 경우의 수
  const cols = Array(n);
  for (let i = 0; i < n; i++) {
    cols[i] = colMask & (1 << i) ? 1 : 0;
  }

  let count = 0; // 이 케이스에서의 최소 개수

  for (let row = 0; row < n; ++row) {
    // 행 별로 최소개수 구하기
    let tmp = 0;
    for (let col = 0; col < n; ++col) {
      // 열 뒤집은 것 판단해서 개수 더하기
      if (coins[row][col] == status[cols[col]]) {
        ++tmp;
      }
    }
    // 행 그대로 or 뒤집은 것 중 작은 개수 더하기
    count += Math.min(tmp, n - tmp);
  }

  answer = Math.min(count, answer); // 최소값 갱신
}

console.log(answer);
