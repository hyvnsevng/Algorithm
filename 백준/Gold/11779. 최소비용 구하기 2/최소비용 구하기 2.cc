#include <bits/stdc++.h>
using namespace std;

int n, m, a, b, c, s, e;
int INF = 10E8;
vector<vector<pair<int, int>>> Edges;
vector<int> ans;
vector<int> path;

int dijkstra() {
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> PQ;
    PQ.push({0, s});

    vector<int> distances;
    distances.resize(n+1, INF);
    distances[s] = 0;
    
    while (!PQ.empty()) {
        int Dist = PQ.top().first;
        int Curr = PQ.top().second;
        PQ.pop();

        if (distances[Curr] < Dist) continue;
        
        for (int i = 0; i < Edges[Curr].size(); ++i) {
            int Next = Edges[Curr][i].first;
            int Cost = Edges[Curr][i].second;
            int nCost = Cost + Dist;
            
            if (distances[Next] > nCost){
                PQ.push({nCost, Next});
                distances[Next] = nCost;
                path[Next] = Curr;
            }
        }
    }

    return distances[e];
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> n >> m;
    Edges.resize(n+1);
    path.resize(n+1, -1);
    
    for (int _ = 0; _ < m; ++_) {
        cin >> a >> b >> c;
        Edges[a].push_back({b, c});
    }
    
    cin >> s >> e;
    cout << dijkstra() << "\n";
    
    ans.resize(0);
    for (int v = e; v != s; v = path[v]) {
        ans.push_back(v);
    }
    ans.push_back(s);

    int cnt = ans.size();
    cout << cnt << "\n";
    for (int i = cnt - 1; i >= 0; --i) cout << ans[i] << " ";
}
