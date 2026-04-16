#include <bits/stdc++.h>

using namespace std;
int INF = 100000000;

int dijkstra(int start, int end, vector<vector<pair<int, int>>> &edges) {
  priority_queue<pair<int, int>> pq;
  pq.push({0, start});

  vector<int> distances (edges.size(), INF);
  distances[start] = 0;
  
  while (!pq.empty()) {
    int cost = pq.top().first;
    int curr = pq.top().second;
    pq.pop();

    if (cost > distances[curr]) continue;

    for (auto p: edges[curr]) {
      int dist = p.first + cost;
      int neighbor = p.second;
      if (dist < distances[neighbor]) {
        distances[neighbor] = dist;
        pq.push({dist, neighbor});
      }
    }
  }

  return distances[end];
}

int main() {
  int n, m;
  cin >> n >> m;

  vector<vector<pair<int, int>>> edges(n+1);

  int a, b, c;
  for (int _=0; _<m; ++_) {
    cin >> a >> b >> c;
    edges[a].push_back({c, b});
  }

  int A, B;
  cin >> A >> B;
  cout << dijkstra(A, B, edges);
}