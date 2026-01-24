const fs = require("fs");
const fileName = "input.txt";
const input = fs.readFileSync(0, "utf8").trim().split("\n");

const [n, m, s] = input.shift().split(" ").map(Number);
const id = input.pop();
const map = input.map((line) => line.split(""));

const cmd = ["U", "D", "L", "R"];
const dx = [-1, 1, 0, 0];
const dy = [0, 0, -1, 1];

const vis = Array.from({ length: n }, () => Array(m).fill(0));
let stamp = 0;

const px = Array.from({ length: n }, () => Array(m).fill(-1));
const py = Array.from({ length: n }, () => Array(m).fill(-1));
const pdir = Array.from({ length: n }, () => Array(m).fill(-1));

const qx = new Int16Array(n * m);
const qy = new Int16Array(n * m);

function buildPath(tx, ty, sx, sy) {
  const out = [];
  let x = tx, y = ty;
  while (!(x === sx && y === sy)) {
    const d = pdir[x][y];
    out.push(cmd[d]);
    const nx = px[x][y], ny = py[x][y];
    x = nx; y = ny;
  }
  out.reverse();
  return out.join("");
}

function findCharFast(ch, sx, sy) {
  stamp++;
  let head = 0, tail = 0;

  vis[sx][sy] = stamp;
  px[sx][sy] = -1; py[sx][sy] = -1; pdir[sx][sy] = -1;

  qx[tail] = sx; qy[tail] = sy; tail++;

  // immediate hit
  if (map[sx][sy] === ch) return ["P", sx, sy];

  while (head < tail) {
    const x = qx[head], y = qy[head]; head++;

    for (let d = 0; d < 4; d++) {
      const nx = x + dx[d], ny = y + dy[d];
      if (nx < 0 || nx >= n || ny < 0 || ny >= m) continue;
      if (vis[nx][ny] === stamp) continue;

      vis[nx][ny] = stamp;
      px[nx][ny] = x; py[nx][ny] = y; pdir[nx][ny] = d;

      if (map[nx][ny] === ch) {
        const path = buildPath(nx, ny, sx, sy);
        return [path + "P", nx, ny];
      }

      qx[tail] = nx; qy[tail] = ny; tail++;
    }
  }
  return ["", undefined, undefined];
}

function findExitFast(sx, sy) {
  const tx = n - 1, ty = m - 1;
  if (sx === tx && sy === ty) return "";

  stamp++;
  let head = 0, tail = 0;

  vis[sx][sy] = stamp;
  px[sx][sy] = -1; py[sx][sy] = -1; pdir[sx][sy] = -1;

  qx[tail] = sx; qy[tail] = sy; tail++;

  while (head < tail) {
    const x = qx[head], y = qy[head]; head++;

    for (let d = 0; d < 4; d++) {
      const nx = x + dx[d], ny = y + dy[d];
      if (nx < 0 || nx >= n || ny < 0 || ny >= m) continue;
      if (vis[nx][ny] === stamp) continue;

      vis[nx][ny] = stamp;
      px[nx][ny] = x; py[nx][ny] = y; pdir[nx][ny] = d;

      if (nx === tx && ny === ty) {
        return buildPath(tx, ty, sx, sy);
      }

      qx[tail] = nx; qy[tail] = ny; tail++;
    }
  }
  
  return "";
}

const cnts = {};
const idCnts = {};

for (const row of map) {
  for (const ch of row) cnts[ch] = (cnts[ch] || 0) + 1;
}
for (const ch of id) idCnts[ch] = (idCnts[ch] || 0) + 1;

let t = 2500;
for (const ch in idCnts) {
  t = Math.min(t, Math.floor((cnts[ch] || 0) / idCnts[ch]));
}

let action = "";
let rf = 0;
let x = 0, y = 0;

while (t--) {
  let res = "";
  for (const ch of id) {
    const [act, nx, ny] = findCharFast(ch, x, y);
    if (act.length === 0) {
      res = "";
      break;
    }
    map[nx][ny] = undefined;
    res += act;
    x = nx; y = ny;
  }
  if (res.length === 0) break;
  rf++;
  action += res;
}

action += findExitFast(x, y);

console.log(rf, action.length);
console.log(action);
