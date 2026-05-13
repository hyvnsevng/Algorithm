from collections import deque

def solution(land):
    n = len(land)
    m = len(land[0])
    visited = [[0] * m for _ in range(n)]
    counts = [0] * m
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]
    for i in range(n):
        for j in range(m):
            if land[i][j] and not visited[i][j]:
                tmp = [0] * m
                q = deque()
                q.append((i, j))
                visited[i][j] = 1
                area = 0
                while q:
                    r, c = q.popleft()
                    area += 1
                    if tmp[c] == 0:
                        tmp[c] += 1
                    for d in range(4):
                        nr = r + dr[d]
                        nc = c + dc[d]
                        if 0 <= nr < n and 0 <= nc < m and land[nr][nc] and not visited[nr][nc]:
                            q.append((nr, nc))
                            visited[nr][nc] = 1
                
                for k in range(m):
                    if tmp[k]:
                        counts[k] += area
                        
    answer = max(counts)
    return answer