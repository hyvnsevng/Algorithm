#include <iostream>
#include <vector>
using namespace std;

int N;
char n, l, r;
vector<vector<int>> tree;
vector<char> wjsdnl, wnddnl, gndnl;

int str2int(char ch) {
    return int(ch) - 65;
}

char int2str(int num) {
    return char(num + 65);
}

int solve(int node) {
    if (node < 0) return 0;
    int left = tree[node][0], right = tree[node][1];
    
    // 전위
    wjsdnl.push_back(int2str(node));
    // 중위
    solve(left);
    wnddnl.push_back(int2str(node));
    // 후위
    solve(right);
    gndnl.push_back(int2str(node));
    return 0;
}

int main() {
    ios_base :: sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    cin >> N;
    tree.assign(N, {-1, -1});

    for (int i = 0; i < N; i++) {
        cin >> n >> l >> r;
        tree[str2int(n)] = {str2int(l), str2int(r)};
    }

    solve(0);
    for (int i = 0; i < N; i++) {
        cout << wjsdnl[i];
    }
    cout << '\n';
    for (int i = 0; i < N; i++) {
        cout << wnddnl[i];
    }
    cout << '\n';
    for (int i = 0; i < N; i++) {
        cout << gndnl[i];
    }
}
