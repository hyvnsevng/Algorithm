#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<long long> v; // 모든 감소하는 수

void solve(long long num, int lastDigit) {
    v.push_back(num);

    for (int i = 0; i < lastDigit; i++) {
        // 현재 마지막 자릿수보다 작은 숫자들을 뒤에 붙임
        solve(num * 10 + i, i);
    }
}

int main() {
    int n;
    cin >> n;

    // i로 시작하는 감소하는 수 생성
    for (int i = 0; i <= 9; i++) {
        solve(i, i);
    }

    sort(v.begin(), v.end());

    if (n >= v.size()) {
        cout << -1;
    } else {
        cout << v[n];
    }

    return 0;
}