#include <bits/stdc++.h>

using namespace std;

int answer = 2000 * 2000;
int N, M, K;

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    cin >> N >> M >> K;
    
    string basis = "BW";
    char chessboard[N+1][M+1];
    vector<vector<int>> sums(N+1, vector<int> (M+1, 0));
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < M; ++j) {
            cin >> chessboard[i][j];
            sums[i+1][j+1] = int(chessboard[i][j] == basis[(i+j)%2]) + sums[i+1][j] + sums[i][j+1] - sums[i][j];
        }
    }

    vector<vector<int>> colsums (N+1, vector<int> (M-K+1, 0));
    for (int r=0; r < N-K+1; ++r) {
        for (int c=0; c < M-K+1; ++c) {
            int tmp = sums[r+K][c+K] - sums[r][c+K] - sums[r+K][c] + sums[r][c];
            answer = min({answer, tmp, K*K - tmp});
        }
    }

    cout << answer;
}