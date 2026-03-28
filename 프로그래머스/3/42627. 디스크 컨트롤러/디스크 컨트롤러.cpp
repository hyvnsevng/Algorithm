#include <bits/stdc++.h>

using namespace std;

int solution(vector<vector<int>> jobs) {
    int answer = 0;
    int N = jobs.size();
    
    vector<vector<int>> tasks;
    for (int i = 0; i < N; ++i) {
        int reqTime = jobs[i][0];
        int taskTime = jobs[i][1];
        tasks.push_back({reqTime, taskTime, i});
    }
    
    sort(tasks.begin(), tasks.end());
    
    int totalTime = 0;
    priority_queue<vector<int>, vector<vector<int>>, greater<vector<int>>> pq;
    int lastIdx = 0;
    int cnt = 0;
    while (cnt < N) {
        for (int i = lastIdx; i < N; ++i) {
            if (tasks[i][0] > totalTime) {
                lastIdx = i;
                break;
            }
            pq.push({tasks[i][1], tasks[i][0], tasks[i][2]});
            
            if (i == N-1) lastIdx = N;
        }
        
        if (pq.empty()) {
            totalTime  = totalTime = tasks[lastIdx][0];
            continue;
        }
        else {
            int qTT = pq.top()[0];
            int qRT = pq.top()[1];
            pq.pop();
            totalTime += qTT;
            answer += (totalTime - qRT);
            cnt++;
        }
    }
    
    answer /= jobs.size();
    
    return answer;
}