#include <bits/stdc++.h>

using namespace std;

int solution(vector<int> citations) {
    int answer = 0;
    int n = citations.size();
    int cited[10001] = {0,};
    for (auto cite: citations) {
        cited[cite]++;
    }
    
    int prevSum = 0;
    for (int h=0; h<10001; ++h) {
        if (n - prevSum >= h) answer = h;
        prevSum += cited[h];
    }
    return answer;
}