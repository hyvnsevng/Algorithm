const fs = require("fs");
const input = fs.readFileSync(0, "utf8").trim().split("\n");

const [L, C] = input[0].split(" ").map((e) => Number(e));
const alphabets = input[1].split(" ");
const ans = [];
const vowels = "aeiou";

function check(str) {
  let vowelCount = 0;
  for (const char of str) {
    if (vowels.includes(char)) vowelCount++;
  }
  if (vowelCount < 1 || str.length - vowelCount < 2) return false;
  return true;
}

function dfs(pw, used, ans) {
  if (pw.length == L && check(pw)) {
    ans.push(pw);
    return;
  }

  for (let i = 0; i < C; ++i) {
    if (
      !used[i] &&
      alphabets[i].charCodeAt() > pw[pw.length - 1].charCodeAt()
    ) {
      used[i] = 1;
      dfs(pw + alphabets[i], used, ans);
      used[i] = 0;
    }
  }
}

const used = Array(C).fill(0);
for (let i = 0; i < C; ++i) {
  used[i] = 1;
  dfs(alphabets[i], used, ans);
  used[i] = 0;
}

ans.sort();
for (const pw of ans) console.log(pw);