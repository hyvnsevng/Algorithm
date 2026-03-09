const fs = require("fs")
const input = fs.readFileSync(0, "utf-8").toString().trim().split("\n")

const [N, M] = input[0].split(" ").map(e => Number(e))
const A = input.slice(1, N+1).map(row => row.split(" ").map(e => Number(e)))
const clouds = [[N-1, 0], [N-1, 1], [N-2, 0], [N-2, 1]]
const dirs = [, [0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1]] // ←, ↖, ↑, ↗, →, ↘, ↓, ↙
const diag = [-1, 1]

for (let i=N+1; i<N+M+1; ++i) {
    const [d, s] = input[i].split(" ").map(e => Number(e))
    const newClouds = []
    const isCloud = Array.from({ length: N }, () => Array(N).fill(false));
    while (clouds.length) {
        const [r, c] = [...clouds.pop()]    // 이동 전 구름 좌표
        const [mr, mc] = [((r + dirs[d][0]*s) % N + N) % N, ((c + dirs[d][1]*s) % N + N) % N]   // 이동 후 구름 좌표
        newClouds.push([mr, mc])    // 이동
        isCloud[mr][mc] = true
        A[mr][mc] += 1
    }

  // 이동한 구름 좌표에서 물복사
    for (const cloud of newClouds) {
        let cnt = 0
        for (const dr of diag) {
            for (const dc of diag){
                const [nr, nc] = [cloud[0]+dr, cloud[1]+dc]
                if (nr >= 0 && nr < N && nc >= 0 && nc < N && A[nr][nc] > 0) {
                    cnt++
                }
            }
        }
        A[cloud[0]][cloud[1]] += cnt
    }

    // 구름 배열 수정
    for (let r=0; r<N; ++r) {
        for (let c=0; c<N; ++c) {
            if (A[r][c] >= 2 && !isCloud[r][c]) {
                A[r][c] -= 2
                clouds.push([r, c])
            }
        }
    }
}

let ans = 0
for (const line of A) {
  for (const water of line) ans += water
}
console.log(ans)