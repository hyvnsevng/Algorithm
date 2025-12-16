#include <iostream>
#include <vector>
#include <stack>
using namespace std;

int n;
vector<vector<pair<int, int>>> edges;

pair<int, long long> furthest (int start) {
    vector<long long> dist(n + 1, -1);
    dist[start] = 0;

    stack<int> st;
    st.push(start);

    while (!st.empty()) {
        int u = st.top(); st.pop();
        for (auto [v, w]: edges[u]) {
            if (dist[v] == -1) {
                dist[v] = dist[u] + w;
                st.push(v);
            }
        }
    }

    int idx = start;
    long long mx = 0;
    for (int i = 1; i <= n; ++i) {
        if (dist[i] > mx) {
            mx = dist[i];
            idx = i;
        }
    }
    
    return {idx, mx};
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> n;
    edges.assign(n + 1, {});

    for (int i = 0; i < n; ++i) {
        int v; cin >> v;
        while (true) {
            int a; cin >> a;    // 짝수번째 
            if (a == -1) break;
            int w; cin >> w;
            edges[v].push_back({a, w});
        }
    }

    auto [u, _] = furthest(1);
    auto [__, diameter] = furthest(u);
    cout << diameter;
    return 0;
}