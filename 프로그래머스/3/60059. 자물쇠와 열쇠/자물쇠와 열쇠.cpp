#include <string>
#include <vector>

using namespace std;

bool check(vector<vector<int>> &key, vector<vector<int>> &lock, int i, int j) {
    int n = lock.size();
    int m = key.size();
    
    for (int r=0; r<n; ++r) {
        int key_r = m-1-i+r;
        for (int c=0; c<n; ++c) {
            int key_c = m-1-j+c;
            if (key_r < 0 || key_r >= m || key_c < 0 || key_c >= m) {
                if (lock[r][c]) continue;
                return false;
            }

            if (!(lock[r][c] ^ key[key_r][key_c])) return false;
        }
    }
    return true;           
}

bool solution(vector<vector<int>> key, vector<vector<int>> lock) {
    
    int n = lock.size();
    int m = key.size();
    
    for (int k=0; k<4; ++k) {
        for (int i=0; i<n+m-1; ++i) { // 행 이동
            for (int j=0; j<n+m-1; ++j) { // 열 이동
                
                if (check(key, lock, i, j)) return true;
            }
        }
        // 회전
        vector<vector<int>> new_key (m, vector<int> (m, 0));
        for (int kr=0; kr<m; ++kr) {
            for (int kc=0; kc<m; ++kc) {
                new_key[kr][kc] = key[kc][m-kr-1];
            }
        }
        
        key = new_key;
    }
    
    return false;
}