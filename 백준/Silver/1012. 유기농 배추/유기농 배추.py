import sys
input = sys.stdin.readline

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]
T = int(input())
for t in range(T):
    m, n, k = map(int, input().split())
    baechu = [[0 for _ in range(m)] for _ in range(n)]
    for __ in range(k):
        c, r = map(int, input().split())
        baechu[r][c] = 1
        
    cnt = 0
    stack = []
    for i in range(n):
        for j in range(m):
            if baechu[i][j]:
                stack.append((i, j))
                while stack:
                    r, c = stack.pop()
                    for k in range(4):
                        nr = r + dr[k]
                        nc = c + dc[k]
                        if 0 <= nr < n and 0 <= nc < m and baechu[nr][nc]:
                            baechu[nr][nc] = 0
                            stack.append((nr, nc))
                cnt += 1
    
    print(cnt)
