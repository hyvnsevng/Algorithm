# 백준 1238번 파티

import heapq
INF = 1E9


def dijkstra(start, destination):
    distance = [INF]*(n+1)
    distance[start] = 0
    hq = []
    heapq.heappush(hq, (0, start))
    while hq:
        dist, now = heapq.heappop(hq)
        if dist > distance[now]:
            continue

        for next, next_dist in edges[now]:
            cost = dist + next_dist
            if cost < distance[next]:
                distance[next] = cost
                heapq.heappush(hq, (cost, next))

    return distance[destination]


n, m, x = map(int, input().split())
edges = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, t = map(int, input().split())
    edges[a].append([b, t])

answer = 0
for i in range(1, n+1):
    time = dijkstra(i, x) + dijkstra(x, i)
    if time > answer:
        answer = time

print(answer)
