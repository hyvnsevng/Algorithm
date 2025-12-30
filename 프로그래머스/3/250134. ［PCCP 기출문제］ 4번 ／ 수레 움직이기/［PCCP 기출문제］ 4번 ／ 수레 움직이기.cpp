#include <string>
#include <vector>

using namespace std;

int n, m;
pair<int ,int> red, blue, RD, BD;
int dr[4] = {1, -1, 0, 0}, dc[4] = {0, 0, 1, -1};
vector<vector<pair<bool, bool>>> visited;
int minVal = 20;

void backtracking(vector<vector<int>> maze, pair<int, int> red, pair<int, int> blue, int depth) {
    if (depth >= minVal) return;
    bool RCheck = (red == RD), BCheck = (blue == BD); 
    if (RCheck & BCheck) {
        minVal = min(minVal, depth);
        return;
    }
    
    int rr = red.first, rc = red.second;
    int br = blue.first, bc = blue.second;

    for (int i = 0; i < 1 << 4; ++i) {
        // 다음 턴 빨강 좌표
        if (!RCheck) {
            rr = red.first + dr[((i & 12) >> 2)];
            rc = red.second + dc[((i & 12) >> 2)];
            if (rr < 0 || rr > n-1 || rc < 0 || rc > m-1 || visited[rr][rc].first || maze[rr][rc] == 5) continue;

        }

        // 다음 턴 파랑 좌표
        if (!BCheck) {
            br = blue.first + dr[i & 3];
            bc = blue.second + dc[i & 3];
            if (br < 0 || br > n-1 || bc < 0 || bc > m-1 || visited[br][bc].second || maze[br][bc] == 5) continue;
        }

        if (rr == br && rc == bc || rr == blue.first && rc == blue.second && br == red.first && bc == red.second) continue;
                
        // 방문처리 후 백트래킹
        if (!RCheck) visited[rr][rc].first = true;
        if (!BCheck) visited[br][bc].second = true;
        backtracking(maze, {rr, rc}, {br, bc}, depth + 1);
        // 방문처리 해제
        if (!RCheck) visited[rr][rc].first = false;
        if (!BCheck) visited[br][bc].second = false;
    }

    return;
}

int solution(vector<vector<int>> maze) {
    n = maze.size(), m = maze[0].size();
    visited.assign(n, vector<pair<bool, bool>>(m, {false, false}));
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            if (maze[i][j] == 1) {
                red = {i, j};
                visited[i][j].first = true;
            }
            if (maze[i][j] == 2) {
                blue = {i, j}; 
                visited[i][j].second = true;
            }
            if (maze[i][j] == 3) {
                RD = {i, j};
            }
            if (maze[i][j] == 4) {
                BD = {i, j};
            }
        }
    }
    
    backtracking(maze, red, blue, 0);
    return minVal == 20 ? 0 : minVal;
}