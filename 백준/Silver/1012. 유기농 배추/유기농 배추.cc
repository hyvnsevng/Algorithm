#include <bits/stdc++.h>

using namespace std;

int T, M, N, K;
vector<vector<int>> baechu;
int dr[4] = {1, 0, -1, 0};
int dc[4] = {0, 1, 0, -1};

int dfs(int r, int c) {
    int nr, nc;
    for (int i = 0; i < 4; ++i) {
        nr = r + dr[i]; nc = c + dc[i];
        if (nr >= 0 && nr < N && nc >= 0 && nc < M && baechu[nr][nc] == 1) {
            baechu[nr][nc] = 0;
            dfs(nr, nc);
        }
    }
    return 0;
}

int func(int r, int c) {
    if (!baechu[r][c]) {
        return 0;
    }

    dfs(r, c);
    return 1;
}

int solve(int M, int N, int K) {
    int r, c;
    vector<pair<int, int>> worms;
    baechu.assign(N, vector<int> (M, 0));
    for (int i = 0; i < K; ++i) {
        cin >> c >> r;
        worms.push_back({r, c});
        baechu[r][c] = 1;
    }
    
    int cnt=0;
    for (auto loc : worms) {
        cnt += func(loc.first, loc.second);
    }

    return cnt;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    cin >> T;
    
    for (int tc=0; tc < T; tc++) {
        cin >> M >> N >> K;
        cout << solve(M, N, K) << "\n";
    }
}