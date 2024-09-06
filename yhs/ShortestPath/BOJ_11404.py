# 백준 11404번 플로이드
# 플로이드-워셜

import sys
input = sys.stdin.readline

n = int(input())    # of city
m = int(input())    # of buses

# {행}번 도시에서 {열}번 도시로 가는 최소비용 배열
INF = int(1e9)
cost_info = [[INF]*(n+1) for _ in range(n+1)]
for i in range(1, n+1): # 자기 자신에서 자기 자신으로 가는 비용은 0
    cost_info[i][i] = 0

# i번 도시에서 1개의 버스를 통해 이동할 수 있는 도시와 비용 입력
for _ in range(m):
    a, b, c = map(int, input().split())     # start, goal, cost
    if c < cost_info[a][b]:                 # 가장 싼 비용의 버스 노선만 저장하기
        cost_info[a][b] = c

# Floyd-Warshall
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            cost_info[a][b] = min(cost_info[a][b], cost_info[a][k] + cost_info[k][b])

for i in range(1, n+1):
    for j in range(1, n+1):
        if cost_info[i][j] == INF:
            print(0, end=' ')
        else:
            print(cost_info[i][j], end=' ')
    print()
