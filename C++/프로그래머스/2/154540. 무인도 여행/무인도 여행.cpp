#include <string>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

vector<int> solution(vector<string> maps) {
    vector<int> answer;
    int n = maps.size();
    int m = maps[0].length();
    
    int DR[] = {1, -1, 0, 0};
    int DC[] = {0, 0, 1, -1};
    
    vector<vector<bool>> visited(n, vector<bool>(m));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (!visited[i][j] && maps[i][j] != 'X') {
                queue<pair<int, int>> q;
                q.push({i, j});
                int days = 0;
                visited[i][j] = true;
                while (!q.empty()) {
                    auto curr = q.front();
                    int r = curr.first, 
                        c = curr.second;
                    days += (maps[r][c] - '0');
                    q.pop();
                    for (int d = 0; d < 4; d++) {
                        int nr = r + DR[d];
                        int nc = c + DC[d];
                        if (nr < 0 || nr >= n || nc < 0 || nc >= m) continue;
                        if (visited[nr][nc] || maps[nr][nc] == 'X') continue;
                        q.push({nr, nc});
                        visited[nr][nc] = true;
                    }
                }
                answer.push_back(days);
            }
        }
    }
    
    if (answer.empty()) {
        answer.push_back(-1);
    }
    else {
        sort(answer.begin(), answer.end());
    }
    
    return answer;
}