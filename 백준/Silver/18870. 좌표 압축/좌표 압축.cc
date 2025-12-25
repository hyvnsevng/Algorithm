#include <iostream>
#include <algorithm>
#include <map>
using namespace std;

int n;
map<int, int> nums;

int main() {
    ios_base :: sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> n;
    int arr[n], sorted[n];
    for (int i = 0; i < n; ++i) {
        cin >> arr[i];
        sorted[i] = arr[i];
    }
    
    sort(sorted, sorted + n);
    
    int cnt = 0;
    for (int i = 0; i < n; ++i) {
        if (i > 0 && sorted[i] == sorted[i-1]) {
            continue;
        }
        nums[sorted[i]] = cnt;
        cnt++;
    }

    for (int i = 0; i < n; ++i) {
        cout << nums[arr[i]] << ' ';        
    }
}