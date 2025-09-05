def dfs(r, c, depth):
    global ans
    if depth > ans:
        ans = depth
    visited[ord(graph[r][c]) - 65] = True
    for i in range(4):
        dr, dc = delta[i]
        nr, nc = r + dr, c + dc
        if 0 <= nr < R and 0 <= nc < C:
            if not visited[ord(graph[nr][nc]) - 65]:
                dfs(nr, nc, depth + 1)
                visited[ord(graph[nr][nc]) - 65] = False


R, C = map(int, input().split())
graph = [list(input()) for _ in range(R)]

delta = [[1, 0], [0, 1], [-1, 0], [0, -1]]
visited = [False] * 26
ans = 0
dfs(0, 0, 1)
print(ans)