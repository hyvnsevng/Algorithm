# 백준 1967번 트리의 지름

# dfs를 이용해 그래프 탐색하기
# 아무 지점 O에서부터 가장 먼 지점 A를 구한다.
# 다시 A로부터 가장 먼 지점 B를 구한다.
# A와 B 사이의 거리가 트리의 지름이 된다.

import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)


def dfs(node, d):
    result = (node, d)
    visited[node] = True
    for adj, w in edges[node]:
        if not visited[adj]:
            tmp = dfs(adj, d+w)
            if tmp[1] > result[1]:
                result = tmp
    visited[node] = False
    return result


n = int(input())        # 노드의 개수
edges = [[] for _ in range(n+1)]
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    n1, n2, cost = map(int, input().split())
    edges[n1].append([n2, cost])
    edges[n2].append([n1, cost])

visited = [False]*(n+1)

start = dfs(n, 0)
end, diameter = dfs(start[0], 0)
print(diameter)
