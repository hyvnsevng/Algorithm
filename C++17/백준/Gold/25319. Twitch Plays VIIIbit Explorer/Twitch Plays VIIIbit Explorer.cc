#include <bits/stdc++.h>
using namespace std;

static inline long long manhattan(int x, int y, int tx, int ty) {
    return llabs(x - tx) + llabs(y - ty);
}

static inline void emit_moves(int &x, int &y, int tx, int ty, string &buf) {
    while (x < tx) { buf.push_back('D'); x++; }
    while (x > tx) { buf.push_back('U'); x--; }
    while (y < ty) { buf.push_back('R'); y++; }
    while (y > ty) { buf.push_back('L'); y--; }
}

static inline void flush_buf(string &buf) {
    if (!buf.empty()) {
        cout << buf;
        buf.clear();
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, M, Ls;
    cin >> N >> M >> Ls;
    vector<string> grid(N);
    for (int i = 0; i < N; i++) cin >> grid[i];
    string S;
    cin >> S;

    array<int, 26> gcnt{}; gcnt.fill(0);
    array<int, 26> scnt{}; scnt.fill(0);

    for (int i = 0; i < N; i++)
        for (int j = 0; j < M; j++)
            gcnt[grid[i][j] - 'a']++;

    for (char c : S) scnt[c - 'a']++;

    int C = INT_MAX;
    for (int k = 0; k < 26; k++) {
        if (scnt[k] > 0) C = min(C, gcnt[k] / scnt[k]);
    }
    if (C == INT_MAX) C = 0;

    vector<pair<int,int>> pos[26];
    for (int k = 0; k < 26; k++) pos[k].reserve(gcnt[k]);

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            pos[grid[i][j] - 'a'].push_back({i, j});
        }
    }
    
    array<int, 26> idx;
    for (int k = 0; k < 26; k++) idx[k] = (int)pos[k].size();

    long long L = 0;
    int x = 0, y = 0;
    auto idx1 = idx;

    for (int rep = 0; rep < C; rep++) {
        for (char ch : S) {
            int k = ch - 'a';
            int p = --idx1[k];
            auto [tx, ty] = pos[k][p];
            L += manhattan(x, y, tx, ty) + 1;
            x = tx; y = ty;
        }
    }
    
    L += manhattan(x, y, N - 1, M - 1);

    cout << C << ' ' << L << "\n";

    int x2 = 0, y2 = 0;
    auto idx2 = idx;

    string buf;
    buf.reserve(1 << 20);

    for (int rep = 0; rep < C; rep++) {
        for (char ch : S) {
            int k = ch - 'a';
            int p = --idx2[k];
            auto [tx, ty] = pos[k][p];

            emit_moves(x2, y2, tx, ty, buf);
            buf.push_back('P');

            if ((int)buf.size() >= (1 << 20) - 1024) flush_buf(buf);
        }
    }
    emit_moves(x2, y2, N - 1, M - 1, buf);
    flush_buf(buf);

    cout << "\n";
    return 0;
}
