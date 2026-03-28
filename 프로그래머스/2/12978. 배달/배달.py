from heapq import heappop, heappush

def solution(N, road, K):
    answer = 0
    
    edges = [[] for _ in range(N+1)]
    for a, b, c in road:
        edges[a].append((c, b))
        edges[b].append((c, a))
    
    h = [(0, 1)]
    distance = [K+1 for _ in range(N+1)]
    while h:
        cost, curr = heappop(h)
        if distance[curr] < cost:
            continue
        distance[curr] = cost
            
        for w, nxt in edges[curr]:
            if distance[nxt] > cost+w:
                heappush(h, (cost+w, nxt))
        
    for i in range(1, N+1):
        if distance[i] <= K:
            answer += 1

    return answer