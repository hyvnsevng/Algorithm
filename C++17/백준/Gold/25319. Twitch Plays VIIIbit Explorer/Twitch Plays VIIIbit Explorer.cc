#include <iostream>
#include <string>
#include <vector>
using namespace std;

int N, M, S;
char dungeon[60][60], id[1001];
int dx[4] = {-1, 1, 0, 0}, dy[4] = {0, 0, -1, 1};
string dirs = "UDLR";
int x=0, y=0;
vector<pair<int, int>> where[30];
string ans;

void moveTo(int tx, int ty) {
    for (int i = 0; i < abs(tx - x); ++i) {
        ans += dirs[tx > x ? 1 : 0];
    }
    for (int i = 0; i < abs(ty - y); ++i) {
        ans += dirs[ty > y ? 3 : 2];
    }
    x = tx; y = ty;
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    cin >> N >> M >> S;

    int idcnts[26] = {0, };

    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < M; ++j) {
            cin >> dungeon[i][j];
            where[dungeon[i][j] - 'a'].push_back({i, j});
        }
    }

    for (int i = 0; i < S; ++i) {cin >> id[i]; idcnts[id[i] - 'a']++;}

    int C = 2500;
    for (int i = 0; i < 26; ++i) {
        if (idcnts[i] > 0) {
            C = min(C, (int)where[i].size() / idcnts[i]);
        }
    }

    cout << C << " ";

    int ptr[26] = {}, idx;
    for (int t = 0; t < C; ++t) {
        for (int i = 0; i < S; ++i) {
            idx = id[i] - 'a';
            auto [tx, ty] = where[idx][ptr[idx]++];
            moveTo(tx, ty);
            ans += "P";
        }
    }
    moveTo(N-1, M-1);

    cout << ans.size() << "\n" << ans;
}
