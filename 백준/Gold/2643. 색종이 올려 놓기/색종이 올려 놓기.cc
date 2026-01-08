#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int N, a, b;
vector<pair<int, int>> P;
vector<int> dp;


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> N;
    P.resize(N);
    dp.assign(N, 1);
    for (int i = 0; i < N; ++i) {
        cin >> a >> b;
        if (b > a) {   
            P[i].first = a;
            P[i].second = b;
        } else {
            P[i].first = b;
            P[i].second = a;
        }
    }

    sort(P.begin(), P.end());

    for (int i = 0; i < N; ++i) {
        a = P[i].first, b = P[i].second;
        for (int j = i - 1; j >= 0; --j) {
            int _a = P[j].first, _b = P[j].second;
            if (a < _a || b < _b) continue;
            dp[i] = max(dp[i], dp[j] + 1);
        }
    }

    int ans = 0;
    for (int i = 0; i < N; ++i) {
        ans = max(dp[i], ans);
    }

    cout << ans;
}   