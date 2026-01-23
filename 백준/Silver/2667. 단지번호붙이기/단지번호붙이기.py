from collections import deque


def bfs(row, col):
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]

    houses = 0
    q = deque([[row, col]])
    visited[row][col]=True

    while q:
        r, c = q.popleft()
        if graph[r][c]:
            houses += 1
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc] and graph[nr][nc]:
                visited[nr][nc] = True
                q.append([nr, nc])


    return houses


n = int(input())
graph = [list(map(int, input())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
ans = []
for i in range(n):
    for j in range(n):
        if graph[i][j] and not visited[i][j]:
            ans.append(bfs(i, j))

ans.sort()
print(len(ans))
for house in ans:
    print(house)