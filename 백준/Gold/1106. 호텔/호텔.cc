#include <iostream>
using namespace std;

int MAX = 100000;
int main() {
  int c, n;
  cin >> c >> n;
  int dp[MAX+1] = {0, }; // dp[i]: i명 유치하는데 드는 최소비용
  for (int i=1; i<=MAX; ++i) dp[i]=MAX;
  int a, b;  // 비용, 고객의 수
  for (int _=0; _<n; ++_) {
    cin >> a >> b;
    for (int cnt=b; cnt<=MAX; cnt++) {
      dp[cnt]=min(dp[cnt], dp[cnt-b]+a);
    }
  }

  int ans = MAX;
  for (int i=c; i<=MAX; ++i) ans = min(ans, dp[i]);
  cout << ans;
}