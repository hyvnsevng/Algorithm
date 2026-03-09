const fs = require("fs");
const input = fs.readFileSync(0, "utf-8").toString().trim().split("\n");

class Grid {
    constructor(n, data) {
        this.N = n;
        this.cells = data;
    }

    // 격자 범위 내에 있는지 확인 (물복사 버그용)
    isValid(r, c) {
        return r >= 0 && r < this.N && c >= 0 && c < this.N;
    }

    // 물 증가
    addWater(r, c, amount = 1) {
        this.cells[r][c] += amount;
    }

    // 물 감소
    consumeWater(r, c) {
        this.cells[r][c] -= 2;
    }

    getWater(r, c) {
        return this.cells[r][c];
    }

    getTotalWater() {
        return this.cells.reduce((sum, row) => sum + row.reduce((a, b) => a + b, 0), 0);
    }
}

class CloudSystem {
    constructor(n) {
        this.N = n;
        // 초기 구름 설정
        this.clouds = [[n - 1, 0], [n - 1, 1], [n - 2, 0], [n - 2, 1]];
        this.dirs = [, [0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1]];
    }

    moveAndRain(d, s, grid) {
        const movedClouds = [];
        const isCloudIdx = Array.from({ length: this.N }, () => Array(this.N).fill(false));

        // 구름 이동 및 비 내리기
        for (const [r, c] of this.clouds) {
            let nr = (r + this.dirs[d][0] * (s % this.N) + this.N) % this.N;
            let nc = (c + this.dirs[d][1] * (s % this.N) + this.N) % this.N;

            grid.addWater(nr, nc);
            movedClouds.push([nr, nc]);
            isCloudIdx[nr][nc] = true;
        }

        // 물복사버그
        this.castWaterCopySpell(movedClouds, grid);

        // 새로운 구름 생성 (기존 구름 위치 제외)
        this.createNewClouds(isCloudIdx, grid);
    }

    castWaterCopySpell(movedClouds, grid) {
        for (const [r, c] of movedClouds) {
            let count = 0;
            const diags = [[-1, -1], [-1, 1], [1, 1], [1, -1]];
            
            for (const [dr, dc] of diags) {
                const nr = r + dr;
                const nc = c + dc;
                if (grid.isValid(nr, nc) && grid.getWater(nr, nc) > 0) {
                    count++;
                }
            }
            grid.addWater(r, c, count);
        }
    }

    createNewClouds(isCloudIdx, grid) {
        const nextClouds = [];
        for (let r = 0; r < this.N; r++) {
            for (let c = 0; c < this.N; c++) {
                if (grid.getWater(r, c) >= 2 && !isCloudIdx[r][c]) {
                    grid.consumeWater(r, c);
                    nextClouds.push([r, c]);
                }
            }
        }
        this.clouds = nextClouds;
    }
}

function solve() {
    const [N, M] = input[0].split(" ").map(Number);
    const initialGridData = input.slice(1, N + 1).map(row => row.split(" ").map(Number));
    const commands = input.slice(N + 1).map(row => row.split(" ").map(Number));

    const grid = new Grid(N, initialGridData);
    const cloudSystem = new CloudSystem(N);

    for (const [d, s] of commands) {
        cloudSystem.moveAndRain(d, s, grid);
    }

    console.log(grid.getTotalWater());
}

solve();