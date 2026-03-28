#include <bits/stdc++.h>

using namespace std;

int solution(vector<int> citations) {
    int answer = 0;
    int n = citations.size();
    sort(citations.begin(), citations.end(), greater<int>());
    for (int i = 0; i < n; ++i) {
        int h = citations[i];
        if (i + 1 >= h) return i;
    }
    return n;
}