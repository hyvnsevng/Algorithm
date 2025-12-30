#include <iostream>
#include <vector>

using namespace std;

int n, FULL, INF = 1e9;
vector<vector<int>> DP;

int main() {
    
    cin >> n;
    int W[n][n];
    FULL = (1 << n) - 1;
    for (int i = 0; i < n; ++i) for (int j = 0; j < n; ++j) cin >> W[i][j];
    
    DP.assign(FULL + 1, vector<int>(n, INF));
    DP[1 << 0][0] = 0;

    for (int mask = 1; mask < FULL + 1; ++mask) {
        for (int i = 0; i < n; ++i) {
            int cur = DP[mask][i];
            if (mask & (1 << i) && cur < INF) {
                for (int j = 0; j < n; ++j) {
                    int nxt = DP[mask | 1 << j][j]; 
                    if (!(mask & (1 << j)) && W[i][j] && nxt > cur + W[i][j]) {
                        DP[mask | 1 << j][j] = cur + W[i][j];
                    }
                }
            }
        }
    }

    int ans = INF;
    for (int i = 1; i < n; ++i) {
        if (DP[FULL][i] >= INF) continue;
        if (W[i][0] == 0) continue;
        ans = min(ans, DP[FULL][i] + W[i][0]);
    }

    cout << ans;
}