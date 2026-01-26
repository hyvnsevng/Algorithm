#include <bits/stdc++.h>

using namespace std;

struct Family {
    vector<string> children;
    double power = 0.0;
    int indegree = 0;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int N, M;
    cin >> N >> M;

    unordered_map<string, Family> kingdom;
    string king;
    cin >> king;
    
    string child, p1, p2;
    for (int i=0; i<N; ++i) {
        cin >> child >> p1 >> p2;
        kingdom[p1].children.push_back(child);
        kingdom[p2].children.push_back(child);
        kingdom[child].indegree += 2;
    }

    kingdom[king].power = 1.0;

    queue<string> q;
    for (auto elem : kingdom) {
        if (elem.second.indegree == 0) q.push(elem.first);
    }

    while (!q.empty()) {
        string person = q.front();
        q.pop();
        for (auto child : kingdom[person].children) {
            kingdom[child].power += kingdom[person].power/2;
            kingdom[child].indegree--;
            if (kingdom[child].indegree == 0) {
                q.push(child);
            }
        }
    }

    double best = -1.0;
    string prince;
    string ans = "";
    for (int _ = 0; _ < M; ++_) {
        cin >> prince;
        if (best < kingdom[prince].power) {
            best = kingdom[prince].power;
            ans = prince;
        }
    }

    cout << ans;
}
