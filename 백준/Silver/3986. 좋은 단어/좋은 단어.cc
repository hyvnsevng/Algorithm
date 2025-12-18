#include <iostream>
#include <stack>
using namespace std;

int n;
string word;
int ans = 0;

int check(string word) {
    int l = word.size();
    stack<char> st;
    for (int i = 0; i < l; ++i) {
        char ch = word[i];
        if (!st.empty() && st.top() == ch) st.pop();
        else st.push(ch);
    }
    return st.empty() ? 1 : 0;
}

int main() {
    ios_base :: sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> n;
    
    for (int i = 0; i < n; ++i) {
        cin >> word;
        ans += check(word);
    }
    cout << ans;
}
