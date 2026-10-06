from collections import deque

DR = [1, -1, 0, 0]
DC = [0, 0, 1, -1]


def get_days(maps, visited, n, m, sr, sc):
    q = deque([(sr, sc)])
    visited[sr][sc] = 1
    res = 0
    while q:
        r, c = q.popleft()
        res += int(maps[r][c])
        for i in range(4):
            nr = r + DR[i]
            nc = c + DC[i]
            if 0 <= nr < n and 0 <= nc < m and maps[nr][nc].isdigit() and not visited[nr][nc]:
                q.append((nr, nc))
                visited[nr][nc] = 1
    return res
        

def solution(maps):
    answer = []
    n, m = len(maps), len(maps[0])
    visited = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if maps[i][j].isdigit() and not visited[i][j]:
                days = get_days(maps, visited, n, m, i, j)
                answer.append(days)
    
    if len(answer) == 0:
        answer.append(-1)
    else:
        answer.sort()
    return answer
