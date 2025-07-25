const fs = require("fs");
const input = fs
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

const [N, M] = input.slice(0, 2).map((e) => Number(e));
const S = input[2];

let answer = 0;
let start = false;
let prev = "";
let len = 0;

for (const letter of S) {
  // I
  if (letter === "I") {
    if (!start) {
      start = true;
    } else {
      if (prev === "O") {
        ++len;
        if (len >= N) {
          answer++;
        }
      } else {
        len = 0;
      }
    }
    prev = "I";
  } else {
    // O
    if (prev === "O") {
      start = false;
      len = 0;
    }
    prev = "O";
  }
  //   console.log(letter, start, prev, len, answer);
}

console.log(answer);
