const fs = require("fs");
//   const input = fs.readFileSync("/dev/stdin").toString().trim().split(" ");
const input = fs
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n")
  .map((el) =>
    el
      .replace("\r", "")
      .split(" ")
      .map((n) => Number(n))
  );

function Combination(arr, n) {
  const combinations = [];
  for (let bit = 0; bit < 1 << n; bit++) {
    const subset = [];

    for (let i = 0; i < n; i++) {
      if (bit & (1 << i)) {
        subset.push(arr[i]);
      }
    }

    if (subset.length === 6) {
      combinations.push(subset);
    }
  }
  combinations.sort((a, b) => {
    for (let i = 0; i < a.length; i++) {
      if (a[i] !== b[i]) {
        return a[i] - b[i];
      }
    }
  });
  return combinations;
}

for (let i = 0; i < input.length - 1; i++) {
  let n = input[i][0];
  const arr = input[i].slice(1);
  const combinations = Combination(arr, n);
  combinations.forEach((el) => {
    console.log(el.join(" "));
  });
  console.log();
}
