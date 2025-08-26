R, C, M = map(int, input().split())
sharks = dict()
graph = [[[] for _ in range(C)] for _ in range(R)]

for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    sharks[z] = [r, c, s, d]
    graph[r-1][c-1].append(z)

def move_shark(r, c, s, d):
    coor = [r, c]
    
    if d == 1:  # 상
        limit = R - 1
        curr = r
        move = -s

    elif d == 2:    # 하
        limit = R - 1
        curr = r
        move = s

    elif d == 3:    # 우
        limit = C - 1
        curr = c
        move = s

    else:   # 좌
        limit = C - 1
        curr = c
        move = -s

    next, nd = nextLoc(curr, move, limit, d)
    coor[d // 3] = next
    return [*coor, nd]


def nextLoc(curr, move, limit, d):
    nd = d
    remainder = (curr + move - 1) % (2 * limit)
    if remainder < limit:
        next = remainder + 1
    else:
        next = limit - (remainder - limit) + 1
        nd += 1 if d % 2 else -1
    
    return (next, nd)

answer = 0
for col in range(1, C + 1):
    captured = [R + 1, 0, 0, 0, 0]  # r, c, s, d, z
    for z in sharks:
        r, c, s, d = sharks[z]
        if c == col and captured[0] > r:
            captured = [r, c, s, d, z]
            
    if captured[4]:
        answer += captured[4]
        del sharks[captured[4]]
        graph[captured[0] - 1][captured[1] - 1] = []

    del_list = []
    for z in sharks:
        r, c, s, d = sharks[z]
        nr, nc, nd = move_shark(r, c, s, d)
        node = graph[nr - 1][nc - 1]
        
        if node:
            del_list.append((nr, nc))
        graph[r - 1][c - 1].remove(z)
        graph[nr - 1][nc - 1].append(z)
        sharks[z] = [nr, nc, s, nd]

    for r, c in del_list:
        max_size = max(graph[r - 1][c - 1])
        for shark in graph[r - 1][c - 1]:
            if shark < max_size: del sharks[shark]
        graph[r - 1][c - 1] = [max_size]
                
    
print(answer)
    