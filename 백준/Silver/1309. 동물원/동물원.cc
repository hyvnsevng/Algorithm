#include <iostream>

using namespace std;
int MOD = 9901;

int main() {
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);
    
    int N;
    cin >> N;
    
    int l=1, r=1, n=1;
    
    while (--N){
        n += (l+r)%MOD;
        l = (n-l)%MOD;
        r = (n-r)%MOD;
    }

    int ans = (l+r+n)%MOD;
    while (ans < 0) ans += MOD;
    cout << ans;
}