const fs = require("fs");
const input = fs.readFileSync(0, "utf8").trim().split("\n");

const [L, C] = input[0].split(" ").map((e) => Number(e));
const alphabets = input[1].split(" ").sort();
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

function dfs(pw, i) {
  if (i > C) return;
  if (pw.length == L && check(pw)) {
    ans.push(pw);
    return;
  }

  dfs(pw + alphabets[i], i + 1);
  dfs(pw, i + 1);
}

dfs("", 0);

ans.sort();
for (const pw of ans) console.log(pw);
