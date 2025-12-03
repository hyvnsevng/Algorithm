from heapq import heappop, heappush
import sys

INF = float('inf')
input = sys.stdin.readline

n, e = map(int, input().split())
edges = [list() for _ in range(n+1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    edges[a].append((b, c))
    edges[b].append((a, c))

def dijkstra(start, end):
    distance = [INF] * (n+1)
    hq = [(0, start)]
    while hq:
        dist, curr = heappop(hq)
        if distance[curr] < dist:
            continue
        distance[curr] = dist 
        for nxt, cost in edges[curr]:
            w = dist+cost
            if w < distance[nxt]:
                heappush(hq, (w, nxt))
    return distance[end]


def min_path(start, x, y, end):
    return dijkstra(start, x) + dijkstra(x, y) + dijkstra(y, end)


def solve(start, v1, v2, end):
    path1 = min_path(start, v1, v2, end)
    path2 = min_path(start, v2, v1, end)
    result = min(path1, path2)
    if result == INF:
        return -1
    return result


v1, v2 = map(int, input().split())
print(solve(1, v1, v2, n))
