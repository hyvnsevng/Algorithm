from collections import deque
from heapq import heappop, heappush

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
    
    return 0
                
                
def tsp(dists, visited, indegree, seq_edges, curr, v):
    k = len(indegree)
    
    # 모든 패널 활성화한 경우
    if v == (1 << k) - 1:
        return 0
    
    # 이미 같은 경로로 방문한 경우
    if visited[curr][v] != INF:
        return visited[curr][v]
    
    for i in range(k):
        # 이미 활성화한 패널이면 건너뛰기
        if v & (1 << i):
            continue
            
        # 안전 순서 지켜지지 않은 경우 건너뛰기
        if indegree[i] != 0:
            continue
            
        nv = v | (1 << i)
        
        # i번째 패널 활성화
        for next_panel in seq_edges[i]:
            indegree[next_panel] -= 1
            
        # 최소 시간 갱신
        cost = tsp(dists, visited, indegree, seq_edges, i, nv) + dists[curr][i]
        visited[curr][v] = min(visited[curr][v], cost)
        
        # 활성화한 패널 복구
        for next_panel in seq_edges[i]:
            indegree[next_panel] += 1
    
    return visited[curr][v]
    

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
        for j in range(k):
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
                
    # 3. 위상정렬로 패널 활성화 순서 구하기
    indegree = [0] * k
    seq_edges = [[] for _ in range(k)]
    for prev, curr in seqs:
        indegree[curr - 1] += 1
        seq_edges[prev - 1].append(curr - 1)
    
    # 4. tsp로 최소 시간 구하기
    visited = [[INF] * (1 << k) for _ in range(k)]    # [현재 위치][방문 상황]
    return tsp(dists, visited, indegree, seq_edges, 0, 0)
    
