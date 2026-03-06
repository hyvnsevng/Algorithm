#include <iostream>
using namespace std;

int MAX = 100000;
int main() {
  int c, n;
  cin >> c >> n;
  int dp[c+1] = {0, }; // dp[i]: i명 유치하는데 드는 최소비용
  for (int i=1; i<=c; ++i) dp[i]=MAX;
  int a, b;  // 비용, 고객의 수
  for (int _=0; _<n; ++_) {
    cin >> a >> b;
    for (int cnt=0; cnt<=c; cnt++) {
      int i = cnt+b > c ? c : cnt+b; // 최대 인덱스 제한
      dp[i]=min(dp[i], dp[cnt]+a);
    }
  }

  cout << dp[c];
}