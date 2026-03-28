from collections import deque

def solution(info, edges):
    n = len(info)
    neighbors = [[] for _ in range(n)]
    for a, b in edges:
        neighbors[a].append(b)
        
    answer = 0
    q = deque()
    q.append((0, 1, 0, set(neighbors[0])))    # 번호, 누적 늑대
    while q:
        node, sheeps, wolves, candidates = q.popleft()
        if not candidates:
            break
        candidates -= {node}
        
        answer = max(answer, sheeps)
        for candidate in candidates:
            n_sheeps, n_wolves = sheeps, wolves
            if info[candidate]:
                n_wolves += 1
            else:
                n_sheeps += 1
            if n_sheeps > n_wolves:
                q.append((candidate, n_sheeps, n_wolves, candidates | set(neighbors[candidate])))
    
    return answer