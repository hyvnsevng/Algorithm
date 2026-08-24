from collections import deque

dr, dc = [1, -1, 0, 0], [0, 0, 1, -1]
EMPTY = ''


def remove(storage, request, n, m):
    if len(request) >= 2:
        return use_crane(storage, request[0], n, m)
    else:
        return use_jige(storage, request, n, m)

        
def use_crane(storage, request, n, m):
    remove_cnt = 0
    for r in range(1, n + 1):
        for c in range(1, m + 1):
            if storage[r][c] == request:
                storage[r][c] = EMPTY
                remove_cnt += 1
                
    return remove_cnt


def use_jige(storage, request, n, m):
    externals = get_externals(storage, n, m)
    removed = []
    for r in range(1, n + 1):
        for c in range(1, m + 1):
            if storage[r][c] == request and externals[r][c]:
                removed.append((r, c)) 
    
    remove_cnt = 0
    for r, c in removed:
        storage[r][c] = EMPTY
        remove_cnt += 1
    
    return remove_cnt
    
    
def get_externals(storage, n, m):
    externals = [[False for _ in range(m + 2)] for _ in range(n + 2)]
    q = deque()
    q.append((0, 0))
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr <= n + 1 and 0 <= nc <= m + 1 and not externals[nr][nc]:
                if storage[nr][nc] == EMPTY:
                    q.append((nr, nc))
                externals[nr][nc] = True
                
    return externals

    
def solution(storage, requests):
    n, m = len(storage), len(storage[0])
    edged_storage = [[storage[i - 1][j - 1] if 0 < i <= n and 0 < j <= m else EMPTY for j in range(m + 2)] for i in range(n + 2)]
    answer = n * m
    for r in requests:
        answer -= remove(edged_storage, r, n, m)
    return answer