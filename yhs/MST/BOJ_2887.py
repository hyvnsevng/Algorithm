# 백준 2887번 행성 터널

# MST 문제지만 모든 정점 사이를 연결할 수 있으므로 메모리 초과를 피하기 위한 방법이 필요했다.
# 또한 그 가중치가 x, y, z 좌표 차의 절댓값 중 최소라는 점에서 x, y, z 좌표값 모두를 고려해야 했음.
# 단순하게 각 축별로 인접한 2개(작은 것 중 최대와 큰 것 중 최소)만 고려하면 일반적인 MST와 동일한 결과를 얻게 된다.

def find_set(x):  # 대표자 찾기
    if parents[x] == x:
        return x

    parents[x] = find_set(parents[x])
    return parents[x]


def union(x, y):  # union
    root_x = find_set(x)
    root_y = find_set(y)

    if root_x < root_y:
        parents[root_y] = root_x
    else:
        parents[root_x] = root_y


import sys
input = sys.stdin.readline

n = int(input())
edges = []
for i in range(n):
    X, Y, Z = list(map(int, input().split()))
    edges.append([X, Y, Z, i])

parents = [x for x in range(n)]
cnt = 0
sum_cost = 0
graph = []
for i in range(3):
    edges.sort(key=lambda x: x[i])
    for j in range(n-1):
        graph.append([edges[j][3], edges[j+1][3], abs(edges[j][i] - edges[j+1][i])])

graph.sort(key = lambda x: x[2])

for v1, v2, cost in graph:
    if find_set(v1) != find_set(v2):
        cnt += 1
        union(v1, v2)
        sum_cost += cost
        if cnt == n - 1:
            break

print(sum_cost)