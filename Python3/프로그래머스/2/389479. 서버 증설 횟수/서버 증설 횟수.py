from collections import deque

def solution(players, m, k):
    answer = 0
    n = len(players)
    q = deque() # (증설 시간, 증설 개수)
    expanded = 0
    for i in range(n):
        num = players[i]
        if q and q[0][0] + k == i:
            t, c = q.popleft()
            expanded -= c
            
        need = num // m - expanded
        if need > 0:
            q.append((i, need))
            expanded += need
            answer += need
    
    return answer