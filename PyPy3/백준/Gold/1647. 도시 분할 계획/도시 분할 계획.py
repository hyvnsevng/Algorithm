from heapq import heappop, heappush

n, m = map(int, input().split())

edges = [[] for _ in range(n + 1)]
n_span = 0

for _ in range(m):
    a, b, c = map(int, input().split())    
    edges[a].append((c, b))
    edges[b].append((c, a))

hq = [(0, 1)]
visited = [False] * (n + 1)
uzb = []
while hq:
    dist, node = heappop(hq)

    if visited[node]:
        continue
    visited[node] = True
    
    # MST 완성되기 바로 전 단계 -> 마을이 두개로 쪼개진 상태
    n_span += 1
    uzb.append(dist)

    for cost, next in edges[node]:
        heappush(hq, (cost, next))

print(sum(uzb) - max(uzb))
