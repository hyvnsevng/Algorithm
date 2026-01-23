#include <iostream>
#include <algorithm>
using namespace std;

int N;
int apt[25][25];

int dfs(int r, int c, int cnt) {
    apt[r][c] = 0;
    if (r > 0 && apt[r-1][c]) cnt += dfs(r-1, c, 1);
    if (r < N-1 && apt[r+1][c]) cnt += dfs(r+1, c, 1);
    if (c < N-1 && apt[r][c+1]) cnt += dfs(r, c+1, 1);
    if (c > 0 && apt[r][c-1]) cnt += dfs(r, c-1, 1);
    return cnt;
}

int main() {
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);
    
    cin >> N;
    
    char x;
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            cin >> x;
            apt[i][j] = x - '0';
        }
    }
    
    int cnts[N*N];
    int len=0;
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            if (apt[i][j]) cnts[len++] = dfs(i, j, 1);
        }
    }

    sort(cnts, cnts + len);
    cout << len;
    for (int _=0; _<len; ++_) cout << "\n" << cnts[_];
}