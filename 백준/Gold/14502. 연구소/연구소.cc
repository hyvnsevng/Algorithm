#include <bits/stdc++.h>
using namespace std;

int N, M;
int graph[8][8];
int dr[4] = {0, 0, 1, -1};
int dc[4] = {1, -1, 0, 0};
int ans = 0;

int countSZ() {
    int sz = 0;
    queue<pair<int, int>> q;
    int r, c, nr, nc;
    int visited[N][M];

    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < M; ++j) {
            visited[i][j] = graph[i][j];
            if (graph[i][j] == 2) q.push({i, j});
        }
    }

    while (!q.empty()) {
        r = q.front().first;
        c = q.front().second;
        q.pop();

        for (int i = 0; i < 4; ++i) {
            nr = r+dr[i]; nc = c+dc[i];
            if (0 <= nr && nr < N && 0 <= nc && nc < M && visited[nr][nc] == 0) {
                visited[nr][nc] = 2;
                q.push({nr, nc});
            }
        
        }
    }

    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < M; ++j) {
            if (visited[i][j] == 0) ++sz;
        }
    }

    return sz;
}

void backtracking(int loc, int d) {
    if (d == 3) {
        ans = max(ans, countSZ());
        return;
    }

    if (loc >= N*M) return;

    int r = loc / M; int c = loc % M;
    
    if (graph[r][c] == 0) {
        graph[r][c] = 1;
        backtracking(loc+1, d+1);
        graph[r][c] = 0;
    }

    backtracking(loc+1, d);
}

int main() {
    cin >> N >> M;
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < M; ++j) {
            cin >> graph[i][j];
        }
    }

    backtracking(0, 0);
    cout << ans;
}