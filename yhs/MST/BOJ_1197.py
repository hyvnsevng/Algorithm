# 백준 1197번 최소 스패닝 트리

# 최소신장트리의 기본 개념에 대한 문제이다. 프림 알고리즘을 써서 풀었으나, 크루스칼을 이용한 방법에 대해서도 생각해보자.

import heapq
import sys
input = sys.stdin.readline


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
