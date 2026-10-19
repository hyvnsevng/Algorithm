from collections import deque

DR = [1, -1, 0, 0]
DC = [0, 0, 1, -1]
INF = 1000000

def get_dist_same_floor(sr, sc, er, ec, grid, n, m):
    q = deque()
    q.append((sr, sc, 0))
    visited = [[False] * m for _ in range(n)]
    visited[sr][sc] = True
    
    while q:
        r, c, dist = q.popleft()
        # 목표지점 도달한 경우 dist 반환
        if r == er and c == ec:
            return dist
        for i in range(4):
            nr, nc = r + DR[i], c + DC[i]
            if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc] and grid[nr][nc] in ('.', '@'):
                q.append((nr, nc, dist + 1))
                visited[nr][nc] = True
    
    return INF
                
                
def tsp(dists, visited, prereq, curr, v):
    k = len(prereq)
    full_mask = (1 << k) - 1
    
    dp = [[INF] * k for _ in range(1 << k)]
    dp[0][0] = 0
    for mask in range(full_mask):
        for curr in range(k):
            # 현재 방문 상태에 도달할 수 없는 경우 건너뛰기
            if dp[mask][curr] == INF:
                continue
            
            # 다음으로 활성화할 패널 선택
            for nxt in range(k):
                bit = 1 << nxt
                
                # 이미 활성화한 패널이면 건너뛰기
                if mask & bit:
                    continue
                
                # 선행 패널이 활성화되지 않은 경우 건너뛰기
                if (mask & prereq[nxt]) != prereq[nxt]:
                    continue
                
                nxt_mask = mask | bit
                cost = dp[mask][curr] + dists[curr][nxt]
                dp[nxt_mask][nxt] = min(dp[nxt_mask][nxt], cost)
    
    return min(dp[full_mask])
    

def solution(h, grid, panels, seqs):
    answer = 0
    n = len(grid)
    m = len(grid[0])
    k = len(panels)
    
    # 1. 각 패널과 엘리베이터까지의 거리 구하기
    elevator_dists = []
    er, ec = -1, -1
    for r in range(n):
        for c in range(m):
            if grid[r][c] == '@':
                er = r
                ec = c
                break
    
    for i in range(k):
        elevator_dists.append(get_dist_same_floor(er, ec, panels[i][1] - 1, panels[i][2] - 1, grid, n, m))
    
    # 2. 패널 사이의 거리 구하기
    dists = [[INF for __ in range(k)] for _ in range(k)]
    for i in range(k):
        ed = elevator_dists[i]
        for j in range(i, k):
            if i == j:
                dists[i][j] = 0
                continue
            if panels[i][0] == panels[j][0]:
                dist = get_dist_same_floor(panels[i][1] - 1, panels[i][2] - 1, panels[j][1] - 1, panels[j][2] - 1, grid, n, m)
                dists[i][j] = dist
                dists[j][i] = dist
            else:
                dist = abs(panels[i][0] - panels[j][0]) + ed + elevator_dists[j]
                dists[i][j] = dist
                dists[j][i] = dist
                
    # 3. 패널 활성화 선행조건 구하기
    prereq = [0] * k
    for prev, curr in seqs:
        prereq[curr - 1] |= 1 << (prev - 1)
    
    # 4. tsp로 최소 시간 구하기
    visited = [[INF] * (1 << k) for _ in range(k)]    # [현재 위치][방문 상황]
    return tsp(dists, visited, prereq, 0, 0)
    