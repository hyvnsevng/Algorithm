#include <iostream>
using namespace std;

int n, m, h=99999, t=99999, b, c, A[100000], Q[200000];

int insert(int x) {
    if (h >= t) return x;
    Q[h]=x;
    --t;
    --h;
    return Q[t+1];
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
  
    cin >> n;
    for (int i=0; i<n; ++i) {
        cin >> A[i];
    }

    for (int i=0; i<n; ++i) {
        cin >> b;
        if (!A[i]) {
            ++t;
            Q[t]=b;
        }
    }

    cin >> m;
    for (int i=0; i<m; ++i) {
        cin >> c;
        cout << insert(c) << " ";
    }
}

