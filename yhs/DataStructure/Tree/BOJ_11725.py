# DFS 이용한 코드

n = int(input())

edges = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)

parents = [0] * (n+1)
visited = [False]*(n+1)
stack = [1]
while stack:
    v = stack.pop()
    visited[v] = True
    for node in edges[v]:
        if visited[node]:
            parents[v] = node
        else:
            stack.append(node)

for i in range(2, n+1):
    print(parents[i])


# # BFS 이용한 코드
# from collections import deque
#
# n = int(input())
#
# edges = [[] for _ in range(n+1)]
#
# for _ in range(n-1):
#     a, b = map(int, input().split())
#     edges[a].append(b)
#     edges[b].append(a)
#
# parents = [0] * (n+1)
# visited = [False]*(n+1)
# q = deque()
# q.append(1)
# while q:
#     v = q.popleft()
#     visited[v] = True
#     for node in edges[v]:
#         if visited[node]:
#             parents[v] = node
#         else:
#             q.append(node)
#
# for i in range(2, n+1):
#     print(parents[i])
