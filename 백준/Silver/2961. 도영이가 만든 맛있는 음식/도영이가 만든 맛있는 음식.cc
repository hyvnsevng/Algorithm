#include <iostream>
using namespace std;

int n, s, b;
int main() {
  cin >> n;
  int S[n], B[n];
  for (int i=0;i<n;++i){
    cin >> S[i] >> B[i];
  }
  int minDiff = 1000000000;
  for (int mask = 1; mask < 1 << n; ++mask) {
    s=1; b=0;
    for (int i=0; i<n; ++i) {
      if ((1<<i)&mask) {
        s *= S[i];
        b += B[i];
      }
    }
    if (abs(s-b) < minDiff) minDiff = abs(s-b);
  }
  cout << minDiff;
}