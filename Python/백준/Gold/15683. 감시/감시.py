import sys
input = sys.stdin.readline

dirs = [None, 
        [(0,), (1,), (2,), (3,)],
        [(0, 2), (1, 3)], 
        [(0, 1), (1, 2), (2, 3), (3, 0)],
        [(0, 1, 2), (1, 2, 3), (2, 3, 0), (3, 0, 1)],
        [(0, 1, 2, 3)]
        ]

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
cctvs = []
emptys = 0
for i in range(n):
    for j in range(m):
        status = graph[i][j]
        if status == 0:
            emptys += 1
        elif 1 <= status <= 5:
            cctvs.append((i, j, graph[i][j]))

watched = [[set() for _ in range(4)] for __ in range(len(cctvs))]
# 위부터 시계방향
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
for i in range(len(cctvs)):
    r, c, s = cctvs[i]
    for j in range(4):
        nr, nc = r + dr[j], c + dc[j]
        while 0 <= nr < n and 0 <= nc < m and graph[nr][nc] != 6:
            if graph[nr][nc] == 0:
                watched[i][j].add((nr, nc))
            nr += dr[j]
            nc += dc[j]

def solve(cctvs, depth, max_cnts, arr = []):
    if depth == len(cctvs):
        ws = set()
        for i in range(depth):
            for d in arr[i]:
                ws |= watched[i][d]
        if max_cnts < len(ws):
            return len(ws)
        return max_cnts
    
    r, c, s = cctvs[depth]
    dir = dirs[s]
    for ds in dir:
        res = solve(cctvs, depth + 1, max_cnts, arr + [ds])
        if res > max_cnts:
            max_cnts = res
    
    return max_cnts


print(emptys - solve(cctvs, 0, 0))