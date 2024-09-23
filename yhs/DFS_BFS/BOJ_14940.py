# 백준 14940번 쉬운 최단경로

# BFS 이용해 2차원 배열의 각 지점과 목표지점까지의 거리를 계산
# 0이 여러 겹일 경우 visited 배열이 갱신되지 않아 -1로 출력되는 예외를 처리하는 것에서 막혔다.

from collections import deque


def bfs(row, col):
    dr, dc = [1, -1, 0, 0], [0, 0, 1, -1]
    q = deque()
    q.append([row, col, 0])
    graph[row][col] = 0
    visited[row][col] = True
    while q:
        r, c, dist = q.popleft()
        graph[r][c] = dist
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc]:
                if graph[nr][nc]:
                    q.append([nr, nc, dist+1])
                visited[nr][nc] = True

    for i in range(n):
        for j in range(m):
            if not visited[i][j]:
                print(-1, end=' ')
            else:
                print(graph[i][j], end=' ')
        print()


n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]
done = False
row, col = 0, 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            row, col = i, j
        if not graph[i][j]:
            visited[i][j] = True

bfs(row, col)
