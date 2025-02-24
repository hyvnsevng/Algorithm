from collections import deque

n, m = map(int, input().split())
matrix = [list(map(int, input())) for _ in range(n)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs(start):
    sx, sy = start
    queue = deque()
    queue.append((sx, sy, 0))
    visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
    visited[sx][sy][0] = 1
    
    while queue:
        tx, ty, broken = queue.popleft()

        if tx == n - 1 and ty == m - 1:
            return visited[n - 1][m - 1][broken]
        
        for k in range(4):
            nx = tx + dx[k]
            ny = ty + dy[k]
                
            if 0 <= nx < n and 0 <= ny < m:
                if matrix[nx][ny] == 0 and visited[nx][ny][broken] == 0:
                    visited[nx][ny][broken] = visited[tx][ty][broken] + 1
                    queue.append((nx, ny, broken))
                elif matrix[nx][ny] == 1 and broken == 0:
                    visited[nx][ny][1] = visited[tx][ty][broken] + 1
                    queue.append((nx, ny, 1))

    return -1

print(bfs((0, 0)))