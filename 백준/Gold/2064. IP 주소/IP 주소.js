const fs = require("fs");
const fileName = "input.txt";
const input = fs.readFileSync(0, "utf8").trim().split("\n");

const N = Number(input.shift());

function ipToBigInt(s) {
  const [a, b, c, d] = s.split(".").map(Number);
  return (
    (BigInt(a) << 24n) | (BigInt(b) << 16n) | (BigInt(c) << 8n) | BigInt(d)
  );
}

function bigIntToIp(x) {
  const a = Number((x >> 24n) & 255n);
  const b = Number((x >> 16n) & 255n);
  const c = Number((x >> 8n) & 255n);
  const d = Number(x & 255n);
  return `${a}.${b}.${c}.${d}`;
}

function prefixToMaskBigInt(prefix) {
  if (prefix === 0) return 0n;
  return ((1n << BigInt(prefix)) - 1n) << BigInt(32 - prefix);
}

let minIP = null,
  maxIP = null;
for (let i = 0; i < N; i++) {
  const ip = ipToBigInt(input[i]);
  if (minIP === null || ip < minIP) minIP = ip;
  if (maxIP === null || ip > maxIP) maxIP = ip;
}

let diff = minIP ^ maxIP; // diff = min XOR max
let prefix = 32;
if (diff !== 0n) {
  let msb = 0;
  while (diff > 0n) {
    diff >>= 1n;
    msb++;
  }
  // msb는 diff의 비트 길이(가장 오른쪽에 있는 1 위치+1)
  prefix = 32 - msb;
}

const mask =
  prefix === 0 ? 0n : ((1n << BigInt(prefix)) - 1n) << BigInt(32 - prefix);
const network = minIP & mask;

console.log(bigIntToIp(network));
console.log(bigIntToIp(mask));
