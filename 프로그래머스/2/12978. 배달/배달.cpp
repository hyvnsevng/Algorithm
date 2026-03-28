#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int solution(int N, vector<vector<int> > road, int K) {
    int answer = 0;

    vector<vector<pair<int, int>>> edges(N+1);
    for (auto info: road) {
        edges[info[0]].push_back({info[2], info[1]});
        edges[info[1]].push_back({info[2], info[0]});
    }
    
    vector<int> distance(N+1, K+1);
    
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
    distance[1] = 0;
    pq.push({0, 1});
    
    while (!pq.empty()) {
        pair<int, int> node = pq.top();
        int cost = node.first;
        int curr = node.second;
        pq.pop();
        
        for (auto next: edges[curr]) {
            int w = next.first;
            int dest = next.second;
            if (distance[curr] + w < distance[dest]) {
                distance[dest] = distance[curr] + w;
                pq.push({distance[dest], dest});
            }
        }
    }
    
    for (int i=1; i<N+1; ++i) {
        if (distance[i] <= K) answer++;
    }

    return answer;
}