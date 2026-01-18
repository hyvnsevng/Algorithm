#include <bits/stdc++.h>

using namespace std;

int M, N, K;
int baechu[51][51];
int dr[4] = {1, 0, -1, 0};
int dc[4] = {0, 1, 0, -1};

int dfs(int r, int c) {
    baechu[r][c] = 0;
    int nr, nc;
    for (int i = 0; i < 4; ++i) {
        nr = r + dr[i]; nc = c + dc[i];
        if (nr >= 0 && nr < N && nc >= 0 && nc < M && baechu[nr][nc] == 1) {
            dfs(nr, nc);
        }
    }
    
    return 1;
}

int solve(int M, int N, int K) {
    int r, c;
    for (int i = 0; i < K; ++i) {
        cin >> c >> r;
        baechu[r][c] = 1;
    }
    
    int cnt=0;
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < M; ++j) {
            if (baechu[i][j]) cnt += dfs(i, j);
        }
    }

    return cnt;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int tc; cin >> tc;
    
    while (tc--) {
        cin >> M >> N >> K;
        cout << solve(M, N, K) << "\n";
    }
}