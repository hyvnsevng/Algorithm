#include <bits/stdc++.h>

using namespace std;

int N, M;
int dr[4] = {1, -1, 0, 0};
int dc[4] = {0, 0, 1, -1};

void melt(vector<vector<int>> &ocean) {
    vector<vector<int>> diff(N, vector<int> (M, 0));

    for (int r=0; r<N; ++r) {
        for (int c=0; c<M; ++c) {
            int cnt = 0;
            for (int i=0; i<4; ++i) {
                int nr = r+dr[i];
                int nc = c+dc[i];
                if (nr >= 0 && nr < N && nc >= 0 && nc < M && ocean[nr][nc] == 0) {
                    cnt++;
                }
            }
            diff[r][c] = cnt;
        }
    }

    for (int r=0; r<N; ++r) {
        for (int c=0; c<M; ++c) {
            ocean[r][c] = max(0, ocean[r][c] - diff[r][c]);
        }
    }
}

bool dfs(int r, int c, vector<vector<int>> &ocean, vector<vector<int>> &visited) {
    if (visited[r][c]) return false;
    if (ocean[r][c] == 0) return false;
    
    visited[r][c] = 1;

    for (int i=0; i<4; ++i) {
        int nr = r+dr[i];
        int nc = c+dc[i];
        if (nr >= 0  && nr < N && nc >= 0 && nc < M && !visited[nr][nc] && ocean[nr][nc] > 0) {
            dfs(nr, nc, ocean, visited);
        }
    }
    return true;
}

int solve(vector<vector<int>> &ocean) {
    int ans = 0;
    while (++ans) {
        melt(ocean);

        stack<int> st;
        vector<vector<int>> visited (N, vector<int> (M, 0));
        int cnt = 0;
        for (int i=0; i<N; ++i) {
            for (int j=0; j<M; ++j) {
                if (dfs(i, j, ocean, visited)) {
                    cnt++;
                };
            }   
        }

        if (cnt > 1) return ans;
        if (cnt == 0) return 0;
    }
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    cin >> N >> M;

    vector<vector<int>> ocean (N, vector<int> (M, 0));
    for (int i=0; i<N; ++i) {
        for (int j=0; j<M; ++j) {
            cin >> ocean[i][j];
        }
    }

    cout << solve(ocean);
}