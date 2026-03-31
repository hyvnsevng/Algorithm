#include <bits/stdc++.h>

using namespace std;

int N, M;
int dr[4] = {1, -1, 0, 0};
int dc[4] = {0, 0, 1, -1};

int visited[301][301] = {{0, }, };
int ans = 0;

struct Point { int r, c; };
vector<Point> icebergs;

void melt(vector<vector<int>> &ocean) {
    vector<int> sea_count(icebergs.size());

    for(int i = 0; i < icebergs.size(); ++i) {
        int cnt = 0;
        for(int d = 0; d < 4; ++d) {
            int nr = icebergs[i].r + dr[d];
            int nc = icebergs[i].c + dc[d];
            if(nr >= 0  && nr < N && nc >= 0 && nc < M && ocean[nr][nc] == 0) cnt++;
        }
        sea_count[i] = cnt;
    }

    vector<Point> next_icebergs;
    for(int i = 0; i < icebergs.size(); ++i) {
        ocean[icebergs[i].r][icebergs[i].c] = max(0, ocean[icebergs[i].r][icebergs[i].c] - sea_count[i]);
        if(ocean[icebergs[i].r][icebergs[i].c] > 0) {
            next_icebergs.push_back(icebergs[i]);
        }
    }
    icebergs = next_icebergs;
}

bool bfs(vector<vector<int>> &ocean) {
    queue<pair<int, int>> q;
    int sr = icebergs[0].r;
    int sc = icebergs[0].c;
    q.push({sr, sc});
    visited[sr][sc] = ans;

    int cnt = 0;
    while (!q.empty()) {
        pair<int, int> coor = q.front();
        q.pop();
        cnt++;

        for (int i=0; i<4; ++i) {
            int nr = coor.first + dr[i];
            int nc = coor.second + dc[i];
            if(nr >= 0  && nr < N && nc >= 0 && nc < M && visited[nr][nc] < ans && ocean[nr][nc] > 0) {
                q.push({nr, nc});
                visited[nr][nc] = ans;
            }
        }
    }

    return cnt == icebergs.size();
}

int solve(vector<vector<int>> &ocean) {
    while (++ans) {
        melt(ocean);

        if (icebergs.empty()) return 0;
        if (!bfs(ocean)) return ans;
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
            if (ocean[i][j] > 0) icebergs.push_back({i, j});
        }
    }

    cout << solve(ocean);
}