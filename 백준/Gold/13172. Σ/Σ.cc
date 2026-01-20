#include <iostream>
typedef long long ll;

using namespace std;
ll X = 1000000007;

ll mod(ll b, ll e) {
    if (e == 1) return b % X;

    ll m = mod(b, e / 2);
    if (e & 1) return (((m * m) % X) * b) % X;
    else return (m * m) % X;
}

int main() {
    ios_base::sync_with_stdio(0); 
    cin.tie(0);
    int tc;
    cin >> tc;
    
    ll ans = 0;
    ll a, b;
    while (tc--) {
        cin >> a >> b;
        ans += (b * mod(a, X-2) % X);
    }

    cout << ans % X;
}