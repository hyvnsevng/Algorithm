#include <string>
#include <vector>

using namespace std;


vector<vector<int>> answer;
int wall[101][101][2] = {{{0, 0}, }, };

bool checkCondition(int x, int y, int a, int b) {
    if (a == 0) {
        // 기둥을 삭제하는 경우: 좌측상단의 보, 윗칸의 보, 윗칸의 기둥 확인
        if (b == 0) {
            // 셋 중 하나라도 false면 false 반환
            if (x > 0 && wall[x-1][y+1][1] && !checkCondition(x-1, y+1, 1, 1) || wall[x][y+1][1] && !checkCondition(x, y+1, 1, 1) || wall[x][y+1][0] && !checkCondition(x, y+1, 0, 1)) return false;
            return true;
        }
        
        // 기둥을 세우는 경우: 왼쪽 혹은 현재칸에 보가 있거나 아래칸에 기둥이 있음
        else {
            if (y == 0) return true;
            if (x > 0 && wall[x-1][y][1]) return true;
            if (wall[x][y][1]) return true;
            if (y > 0 && wall[x][y-1][0]) return true;
            return false;
        }
    }
    
    else {
        // 보를 삭제하는 경우: 왼쪽칸과 오른쪽칸의 보, 현재칸과 오른쪽칸의 기둥 확인
        if (b == 0) {
            if (x > 0 && wall[x-1][y][1] && !checkCondition(x-1, y, 1, 1) || wall[x+1][y][1] && !checkCondition(x+1, y, 1, 1) || wall[x][y][0] && !checkCondition(x, y, 0, 1) || wall[x+1][y][0] && !checkCondition(x+1, y, 0, 1)) return false;
            return true;
        }
        
        // 보를 만드는 경우: 아래 혹은 우측 하단에 기둥이 있거나 왼&오른쪽에 보가 있음
        else {
            if (y > 0 && wall[x][y-1][0]) return true;
            if (wall[x+1][y-1][0]) return true;
            if (x > 0 && wall[x-1][y][1] && wall[x+1][y][1]) return true;
            return false;
        }
    }
}

void action(int x, int y, int a, int b) {
    wall[x][y][a] = b;
    if (!checkCondition(x, y, a, b)) {
        wall[x][y][a] = !b;
    }    
}

vector<vector<int>> solution(int n, vector<vector<int>> build_frame) {
    int x, y, a, b;
    for (int i=0; i<build_frame.size(); ++i) {
        x = build_frame[i][0];
        y = build_frame[i][1];
        a = build_frame[i][2];
        b = build_frame[i][3];
        
        action(x, y, a, b);
    }
    
    for (int i=0; i<n+1; ++i) {
        for (int j=0; j<n+1; ++j) {
            if (wall[i][j][0] == 1) {
                answer.push_back({i, j, 0});
            }
                
            if (wall[i][j][1] == 1) {
                answer.push_back({i, j, 1});
            }
        }
    }
    
    return answer;
}