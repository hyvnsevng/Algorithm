import heapq


def prim():
    hq = []
    MST = [False]*(V+1)
    heapq.heappush(hq, (0, 1))
    result = 0
    while hq:
        cost, now = heapq.heappop(hq)
        if MST[now]:
            continue
        MST[now] = True
        result += cost
        for next, nextcost in edges[now]:
            if MST[next]:
                continue
            heapq.heappush(hq, (nextcost, next))

    return result


V, E = map(int, input().split())
edges = [[] for _ in range(V+1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    edges[a].append([b, c])
    edges[b].append([a, c])

print(prim())