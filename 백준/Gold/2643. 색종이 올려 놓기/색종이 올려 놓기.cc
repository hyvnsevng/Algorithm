#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N; cin >> N;
    vector<pair<int,int>> P(N);
    for (auto &p: P) {
        int a,b; cin >> a >> b;
        if (a > b) swap(a,b);
        p = {a,b};
    }

    sort(P.begin(), P.end(), [](auto &x, auto &y){
        if (x.first != y.first) return x.first > y.first;
        return x.second > y.second;
    });

    vector<int> dp(N, 1);
    int ans = 1;
    for (int i=0;i<N;i++){
        for (int j=0;j<i;j++){
            if (P[i].first <= P[j].first && P[i].second <= P[j].second) {
                dp[i] = max(dp[i], dp[j] + 1);
            }
        }
        ans = max(ans, dp[i]);
    }
    cout << ans;
}