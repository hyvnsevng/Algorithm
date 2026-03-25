#include <bits/stdc++.h>
using namespace std;

/**
 * i번 파이어볼의 위치 r, c, 질량 m, 방향 d, 속력 s
 * 방향은 위부터 시계방향으로 0~7
 * 1. 파이어볼이 방향 d로 속력 s만큼 이동(M번)
 * 2. 파이어볼이 2개 이상 있는 칸에선 파이어볼이 4개로 나누어지고 sum(m)/5, 속력은 sum(s)/(합쳐진 개수), 방향은 모두 홀/짝이면 0246 / 아니면 1357 (N*N번)
 * 3. 0인 애들은 소멸시킨다.
 * 
 * 1번과 N번은 연결되어있따.
 */

struct Fireball {
    int r, c, m, s, d;
};

int N, M, K;    // N: 격자크기, M: 파이어볼 개수, K: 이동 횟수
vector<Fireball> FB;
vector<int> graph[51][51];

int dr[] = {-1, -1, 0, 1, 1, 1, 0, -1};
int dc[] = {0, 1, 1, 1, 0, -1, -1, -1};

void merge() {
    vector<Fireball> next_FB;

    for (int r=0; r<N; ++r) {
        for (int c=0; c<N; ++c) {
            if (graph[r][c].size() == 0) continue;
            if (graph[r][c].size() == 1) {
                next_FB.push_back(FB[graph[r][c][0]]);
            }
            else {
                int m = 0;
                int s = 0;
                bool odd = false;
                bool even = false;
                int size = graph[r][c].size();
                
                for (int i=0; i<size; ++i) {
                    int idx = graph[r][c][i];
                    m += FB[idx].m;
                    s += FB[idx].s;
                    if (FB[idx].d % 2 == 1) odd = true;
                    else even = true;
                }

                m /= 5;
                if (m == 0) continue;

                s /= size;
                int d = odd && even ? 1 : 0;
                
                for (int k=0; k<4; ++k) {
                    next_FB.push_back({r, c, m, s, k*2+d});
                }

            }
        }
    }
    FB = next_FB;
}

void move() {
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) graph[i][j].clear();
    }

    for (int i=0; i<FB.size(); ++i) {
        Fireball fb = FB[i];
        int r = fb.r;
        int c = fb.c;
        int s = fb.s;
        int d = fb.d;

        int nr = (r + (s%N)*dr[d] + N) % N;
        int nc = (c + (s%N)*dc[d] + N) % N;

        FB[i].r= nr; FB[i].c = nc;

        graph[nr][nc].push_back(i);
    }
}

int main() {

    cin >> N >> M >> K;
    
    int r, c, m, d, s;
    for (int _=0; _<M; ++_) {
        cin >> r >> c >> m >> s >> d;
        FB.push_back({r-1, c-1, m, s, d});
    }

    while (K--) {
        move();
        merge();
    }

    int ans = 0;
    for (auto fb : FB) {
        ans += fb.m;
    }

    cout << ans;
}