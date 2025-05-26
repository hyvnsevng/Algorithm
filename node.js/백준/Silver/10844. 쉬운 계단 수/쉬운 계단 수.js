const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString();

let arr = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1];
const n = parseInt(input);

for (let i = 1; i < n; i++) {
  var newArr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0];
  for (let j = 0; j < 10; j++) {
    if (j > 0) {
      newArr[j - 1] = (newArr[j - 1] + arr[j]) % 1000000000;
    }

    if (j < 9) {
      newArr[j + 1] = (newArr[j + 1] + arr[j]) % 1000000000;
    }
  }
  arr = newArr;
}

let sum = 0;

arr.forEach((v) => (sum += v));
console.log(sum % 1000000000);
